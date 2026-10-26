"""Exact and numerical checks for the competition model on a clique with a deleted matching.
Reproduce: python candidate_verify_43.py (requires sympy and scipy).
The universal statements rely on the accompanying analytic proof, not on these finite tests.
"""
from fractions import Fraction
from itertools import product
import sympy as sp
from scipy.integrate import solve_ivp

def graph(s, r):
    n = 2*s+r
    A = sp.ones(n,n)-sp.eye(n)
    for i in range(s):
        A[2*i,2*i+1] = A[2*i+1,2*i] = 0
    return A

def equilibrium_below(s, r, t):
    u = 1-2*t
    v = 1-t
    c = 1/(1 + t*(2*s/u+r/v))
    return sp.Matrix([c/u]*(2*s)+[c/v]*r)

checks = 0
for s in range(1,5):
    for r in range(0,5):
        n = 2*s+r
        if n<4: continue
        A = graph(s,r)
        for t in [sp.Rational(1,5),sp.Rational(2,5)]:
            Q = sp.eye(n)+t*A
            x = equilibrium_below(s,r,t)
            assert Q*x == sp.ones(n,1)
            assert all(z>0 for z in x)
            assert all(z>0 for z in Q.eigenvals())
            checks+=1
        t=sp.Rational(1,2)
        weights = [sp.Rational(i+1,s*(s+1)//2) for i in range(s)]
        xc = sp.Matrix([v for v in weights for _ in range(2)]+[0]*r)
        assert xc.T*sp.ones(n,1)==2*sp.ones(1,1)
        assert (sp.eye(n)+t*A)*xc == sp.ones(n,1)
        checks+=1
        for t in [sp.Rational(3,5),sp.Rational(4,5)]:
            for i in range(s):
                z = sp.zeros(n,1)
                z[2*i]=z[2*i+1]=1
                g = sp.ones(n,1)-(sp.eye(n)+t*A)*z
                assert all(g[j]==0 if j in [2*i,2*i+1] else g[j]==1-2*t for j in range(n))
                checks+=1
print('exact model identities:',checks)

# Check reduced dynamical difference identities symbolically, without replacing them by numerical testing.
s,r=3,2
t=sp.symbols('t',positive=True)
q=sp.symbols('q0:'+str(s),positive=True)
y=sp.symbols('y0:'+str(r),positive=True)
Q=sum(q);Y=sum(y)
qdot=[q[i]*(1-2*t*Q-t*Y+(2*t-1)*q[i]) for i in range(s)]
ydot=[y[j]*(1-2*t*Q-t*Y-(1-t)*y[j]) for j in range(r)]
for i in range(s):
    for j in range(s):
        assert sp.simplify(qdot[i]/q[i]-qdot[j]/q[j]-(2*t-1)*(q[i]-q[j]))==0
checks+=s*s
print('difference identities:',s*s)

# Numerical illustrations are finite checks only. Strictly positive, balanced-pair starts.
numerical=0
for s,r in [(1,3),(2,1),(3,2),(4,1)]:
    n=2*s+r
    A=graph(s,r)
    B=[list(map(float,A.row(i))) for i in range(n)]
    for t in [0.60,0.75,0.92]:
        q=[(i+1)/8 for i in range(s)]
        x0=[v for a in q for v in (a,a)]+[2+0.12*j for j in range(r)]
        def fun(_,x):
            return [x[i]*(1-x[i]-t*sum(B[i][j]*x[j] for j in range(n))) for i in range(n)]
        sol=solve_ivp(fun,(0,350),x0,rtol=1e-9,atol=1e-11)
        assert sol.success
        z=sol.y[:,-1]
        winner=s-1
        assert min(z[2*winner],z[2*winner+1])>0.999
        assert max([z[j] for j in range(n) if j not in (2*winner,2*winner+1)]) < 0.001
        numerical+=1
print('numerical winner tests:',numerical)
print('PASS')
