#!/usr/bin/env python3
"""Exact arithmetic checks for two-pin cycle phase-order optimization.

Requirements: Python 3.10+, sympy. Optional: scipy, numpy for a
small nonlinear local-equilibrium regression test.
"""
import sympy as s

z, m, y, t = s.symbols("z m y t")
F = z*(z+2)*(2*z**2+4*z+9)/180
H = z*(z+1)*(z+2)*(z**2+2*z+2)/120
Cpoly = (
    (m-1)*(m+2)*(m**2+6)/360
    + y*(-m**3+12*m**2+22*m+60)/(360*m)
    - y**2*(7*m+30)/(360*m)
)
tests = 0

def check(ok, message):
    global tests
    tests += 1
    if not bool(ok):
        raise AssertionError(message)

def mat(m0):
    if m0 == 0:
        return s.zeros(0)
    A = 2*s.eye(m0)
    for j in range(m0-1):
        A[j,j+1] = -1
        A[j+1,j] = -1
    return A

# Verify the Dirichlet Green kernel itself and both polynomial sums
# against exact matrix inverses (independent of the closed-form reduction).
for n in range(1, 14):
    G = mat(n).inv()
    Q = s.Matrix(n,n,lambda i,j: s.Rational(
        min(i+1,j+1)*(n+1-max(i+1,j+1)),n+1))
    check(G == Q, ("green",n))
    check(s.trace(G*G)==F.subs(z,n), ("trace",n))
    ones=s.ones(n,1)
    check((ones.T*G*G*ones)[0]==H.subs(z,n),("row sum square",n))

# Verify the exact dimension-uniform polynomial and strict concavity.
ell=s.symbols("ell")
direct = F.subs(z,ell)+F.subs(z,m-ell)-(
    H.subs(z,ell)+H.subs(z,m-ell))/m
check(s.simplify(direct-Cpoly.subs(y,ell*(m-ell)))==0,"uniform polynomial")
check(s.simplify(s.diff(Cpoly,y,2)+(7*m+30)/(180*m))==0,"strict concavity")
even_delta=s.factor(Cpoly.subs(y,0)-Cpoly.subs(y,m**2/4))
odd_delta=s.factor(Cpoly.subs(y,0)-Cpoly.subs(y,(m**2-1)/4))
check(s.simplify(even_delta-
    m*(11*m**3-18*m**2-88*m-240)/5760)==0, "even gap")
check(s.simplify(odd_delta-
    (m-1)*(m+1)*(11*m**3-18*m**2-95*m-270)/(5760*m))==0,"odd gap")

# Exact finite exhaustive graph-level checks, using the full centered
# projection rather than the closed formula.
for N in range(4,31):
    M=N-2
    cost=[]
    for k in range(M//2+1):
        # Pin vertex 0 and vertex k+1; two Dirichlet arcs have k and M-k sites.
        G=s.diag(mat(k).inv() if k else s.zeros(0),
                 mat(M-k).inv() if M-k else s.zeros(0))
        one=s.ones(M,1)
        P=s.eye(M)-one*one.T/M
        q=s.trace(G*P*G)
        check(q==Cpoly.subs({m:M,y:k*(M-k)}),("centered exact",N,k))
        cost.append(q)
    winners={i for i,v in enumerate(cost) if v==min(cost)}
    expected={0} if 4<=N<=6 else {M//2}
    check(winners==expected,("optimal",N,winners,expected))
    # Fixed-reference mean-squared error has the opposite geometry
    # for all N >= 4: equal arc lengths minimize it.
    tracking=[F.subs(z,k)+F.subs(z,M-k) for k in range(M//2+1)]
    check({i for i,v in enumerate(tracking) if v==min(tracking)}=={M//2},
          ("tracking contrast",N))

# The two finite-size examples that separate the two geometries.
check(Cpoly.subs({m:4,y:0})==s.Rational(11,10),"N6 clustered")
check(Cpoly.subs({m:4,y:4})==s.Rational(11,9),"N6 balanced")
check(Cpoly.subs({m:5,y:0})==s.Rational(217,90),"N7 clustered")
check(Cpoly.subs({m:5,y:6})==s.Rational(407,180),"N7 balanced")
check(s.limit(Cpoly.subs(y,0)/Cpoly.subs(y,m**2/4),m,s.oo)==s.Rational(16,5),
      "large-cycle comparison")

# Optional independent sine-coupled stationary-equilibrium regression.
# This is a finite check of coefficients, not an infinite proof.
try:
    import numpy as np
    from scipy.optimize import root
    for N,k in [(6,0),(6,2),(7,0),(7,2),(12,1),(12,5)]:
        M=N-2
        pinned={0,k+1}
        free=[i for i in range(N) if i not in pinned]
        xi=np.array([1 if j%3 else -1 for j in range(M)],dtype=float)
        # Free frequencies do not need to sum to zero for the formula.
        g=1.7
        G= np.zeros((M,M))
        for j,v in enumerate(free):
            for nb in [(v-1)%N,(v+1)%N]:
                if nb in pinned:
                    G[j,j]+=1
                else:
                    G[j,j]+=1
                    G[j,free.index(nb)]-=1
        pred=(xi @ np.linalg.solve(G,(
             np.eye(M)-np.ones((M,M))/M)
             @np.linalg.solve(G,xi)))/(2*M*g*g)
        def equation(phi,eps):
            xx=np.zeros(N)
            xx[free]=phi
            return eps*xi+g*np.array([
                sum(np.sin(xx[nb]-xx[v]) for nb in ((v-1)%N,(v+1)%N))
                for v in free])
        vals=[]
        for eps in (0.016,0.008):
            sol=root(lambda x:equation(x,eps),np.zeros(M),tol=1e-12)
            check(np.linalg.norm(equation(sol.x,eps))<1e-12,
                  ("nonlinear root",N,k,eps))
            R=abs(np.mean(np.exp(1j*sol.x)))
            vals.append((1-R)/(eps*eps))
            check(abs((1-R)/(eps*eps)-pred)<0.002,("weak disorder",N,k,eps))
        check(abs(vals[1]-pred)<abs(vals[0]-pred)+1e-7,
              ("quartic decay",N,k))
except ImportError:
    print("Optional scipy/numpy nonlinear regression not run.")
print("PASS:",tests,"deterministic algebraic, graph, and local-equilibrium tests")
