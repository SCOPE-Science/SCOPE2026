"""Independent symbolic generator and numerical-filter checks for the stated stochastic model.
Requires Python 3 with sympy, numpy, scipy installed.
Run: python verify.py
"""
from math import exp, isclose
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm
import numpy as np

x,y,q,s=sp.symbols('x y q s', positive=True)

def basis(n):
    return [(i,n-i) for i in range(n,-1,-1)]

def L(i,j):
    return sp.expand(-i*x**i*y**j + (i*x**(i-1)*y**(j+1) if i else 0)
                     + (j*(j-1)*x**i*y**(j-2) if j>=2 else 0)
                     - (q*x**i*y**j if j else 0))

# Independently solve the stationary generator equations in degrees two and four.
expect = {(0,0):sp.S.One}
for degree in (2,4):
    unknowns={ij:sp.symbols('m%d%d'%ij) for ij in basis(degree)}
    eq=[]
    for ij in basis(degree):
        poly=sp.Poly(L(*ij),x,y)
        eq.append(sum(coef*(unknowns[ab] if ab in unknowns else expect.get(ab,0))
                      for ab,coef in poly.terms()))
    solution=sp.solve(eq,list(unknowns.values()),dict=True)
    assert len(solution)==1
    expect.update({ij:sp.factor(solution[0][unknowns[ij]]) for ij in unknowns})

# The row/column orientation is checked explicitly: column j is L(basis_j).
B=basis(3)+basis(1)
G=sp.zeros(6)
for col,(i,j) in enumerate(B):
    poly=sp.Poly(L(i,j),x,y)
    for row,ab in enumerate(B): G[row,col]=poly.coeff_monomial(x**ab[0]*y**ab[1])

initial_left=sp.Matrix([[expect[i+1,j] for i,j in B]])
initial_right=sp.Matrix([[expect[i+3,j] if i+j==1 else 0 for i,j in B]])
resolvent=(s*sp.eye(6)-G).inv()
observed=sp.factor((initial_right*resolvent[:,4]-initial_left*resolvent[:,0])[0])
Q=(6*q*q-9*q-9)*s**2+(17*q**3-q*q-45*q-27)*s+(14*q**4+23*q**3-21*q*q-42*q-18)
proposed=24*Q/(q*(q+1)**2*(q+2)*(q+3)*(s+q)**2*(s+1)*(s+3)*(s+q+1)*(s+q+2))
assert sp.factor(observed-proposed)==0

# Exact sign-decomposition, including the repeated-pole transition q=1.
a=2*q*(q+1)*(7*q+3)/(q-1)
b=-(8*q**3+35*q*q+6*q-9)/(q-1)
c=-3*(q+1)*(q+2)*(q+3)
assert sp.factor(Q/((s+q)**2*(s+1))-(a/(s+1)+b/(s+q)+c/(s+q)**2))==0
assert sp.factor(a+b-3*(2*q*q-3*q-3))==0
assert sp.factor(a*(q-1)+c-(q+1)*(11*q*q-9*q-18))==0
assert sp.factor((Q/((s+q)**2*(s+1))).subs(q,1)+12/(s+1)+32/(s+1)**2)==0
assert sp.factor(sp.limit(s**4*proposed,s,sp.oo)-72*(2*q*q-3*q-3)/(q*(q+1)**2*(q+2)*(q+3)))==0
assert sp.factor(sp.limit((s+1)*proposed,s,-1)-24*(7*q+3)/(q*(q-1)*(q+1)**2*(q+2)*(q+3)))==0

# Numerical independent route: the positive exponential convolution filters,
# versus the polynomial Markov-semigroup exponential. These routes do not
# compute the same intermediate numerical state.
def gfun(t,rate):
    if abs(rate-1.0)<1e-12:
        return (-12-32*t)*exp(-t)
    aa=float(a.subs(q,rate)); bb=float(b.subs(q,rate)); cc=float(c.subs(q,rate))
    return aa*exp(-t)+(bb+cc*t)*exp(-rate*t)

def delta_filter(t,rate):
    def rhs(u,z):
        return (gfun(u,rate)-3*z[0], z[0]-(rate+1)*z[1],
                z[1]-(rate+2)*z[2])
    out=solve_ivp(rhs,(0,t),(0,0,0),rtol=2e-12,atol=2e-13)
    assert out.success
    return 24*out.y[2,-1]/(rate*(rate+1)**2*(rate+2)*(rate+3))

def delta_matrix(t,rate):
    MM=np.array(G.subs(q,rate),dtype=float)
    vl=np.array(initial_left.subs(q,rate),dtype=float).reshape(-1)
    vr=np.array(initial_right.subs(q,rate),dtype=float).reshape(-1)
    E=expm(MM*t)
    return float(vr@E[:,4]-vl@E[:,0])

for rate in (.5,1.,1.25,1.5,2.,3.,5.):
    for t in (.1,.4,1.,3.,6.):
        f1=delta_filter(t,rate)
        f2=delta_matrix(t,rate)
        assert isclose(f1,f2,abs_tol=1e-10,rel_tol=2e-7),(rate,t,f1,f2)
for rate, t, sign in [(.5,1,-1),(1,2,-1),(1.5,1,-1),(1.5,3,1),(2, .1,-1),
                     (2,1,1),(3,.1,1),(5,1,1)]:
    assert sign*delta_filter(t,rate)>1e-9,(rate,t)
print('PASS: symbolic stationary moments, resolvent, factorization, limits, 35 cross-method numerical comparisons and 8 sign checks.')
print('Example at rate=1.5: A(1)=%.12f, A(3)=%.12f' %(delta_filter(1.,1.5),delta_filter(3.,1.5)))
