"""Reproduce exact and numerical checks for minimax vertex coherence on weighted stars.

Requires Python 3 with numpy, scipy, sympy. Run: python verify.py
The analytic theorem, not finite sampling, establishes the infinite-parameter claim.
"""
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import pinvh
import sympy as sp


def allocation(prices, budget):
    c = np.asarray(prices, dtype=float)
    assert len(c) >= 2 and np.all(c > 0) and budget > 0
    m = len(c); alpha = m*m-1
    lo,hi=0.0,float(c.max())
    for _ in range(120):
        t=(lo+hi)/2
        if np.sum(np.maximum(c/t-1,0.0)) > alpha: lo=t
        else: hi=t
    tau=(lo+hi)/2
    y=np.minimum(1.,np.sqrt(c/tau))
    z=np.sum(c/y)
    r=(z/budget)*y
    p=np.maximum(c/tau-1,0.)/alpha
    F=(sum(r)+alpha*max(r))/(m+1)**2
    dual=(np.sum(np.sqrt(c*(1+alpha*p)))**2)/(budget*(m+1)**2)
    return tau,r,p,F,dual


def star_laplacian(r):
    m=len(r)
    w=1/np.asarray(r)
    L=np.zeros((m+1,m+1))
    for i in range(m):
        L[0,0]+=w[i];L[i+1,i+1]+=w[i]
        L[0,i+1]-=w[i];L[i+1,0]-=w[i]
    return L


# Exact rational check of the graph pseudoinverse identity and a 2-active-edge optimum.
rational_resistances=[sp.Rational(1),sp.Rational(1),sp.Rational(1,4),sp.Rational(1,2)]
N=len(rational_resistances)+1
L=sp.zeros(N)
for i,r in enumerate(rational_resistances,1):
    w=1/r
    L[0,0]+=w;L[i,i]+=w;L[0,i]-=w;L[i,0]-=w
J=sp.ones(N,N)/N
Ld=(L+J).inv()-J
S=sum(rational_resistances)
alpha=(N-2)*N
assert Ld[0,0]==S/N**2
for i,r in enumerate(rational_resistances,1):
    assert Ld[i,i]==(S+alpha*r)/N**2
assert max(Ld[i,i] for i in range(N))==sp.Rational(71,100)
cs=[240,32,1,4];B=284
tau,r,p,F,dual=allocation(cs,B)
assert abs(tau-16)<1e-11 and np.max(abs(r-np.array([1,1,.25,.5])))<1e-11
assert abs(F-.71)<1e-11 and abs(F-dual)<1e-11

# Boundary price vector, and distinct active-set profiles.
for c,k in [([9,1,1],1),([9,1,1],1),([100,1,1],1),([240,32,1,4],2),([2,3,4,5],4)]:
    t,r,p,F,d=allocation(c,1)
    assert abs(F-d)<=3e-11*max(1,F)
    assert sum(x>t+1e-9 for x in c)==k

rng=np.random.default_rng(202606)
checked=0
for m in range(2,10):
  for it in range(12):
    c=np.exp(rng.uniform(-5,5,m))
    B=float(np.exp(rng.uniform(-2,2)))
    tau,r,p,F,dual=allocation(c,B)
    assert abs(np.dot(c,1/r)-B)<1e-9*B
    assert abs(sum(p)-1)<1e-11
    assert abs(F-dual)<=1e-9*max(1,F)
    equal_value=(m*m+m-1)*sum(c)/(B*(m+1)**2)
    assert F<=equal_value*(1+1e-10)
    assert equal_value/F <= (m*m+m-1)/m**2+1e-8
    ld=pinvh(star_laplacian(r),rtol=1e-12)
    assert abs(ld.diagonal().max()-F)<=1e-8*max(1,F)
    assert abs(ld[0,0]-sum(r)/(m+1)**2)<=1e-8*max(1,F)
    for j in range(m):
      assert abs(ld[j+1,j+1]-(sum(r)+(m*m-1)*r[j])/(m+1)**2)<=1e-8*max(1,F)
    # Independent convex constrained optimization in resistance variables.
    def objective(x): return (sum(x[:m])+(m*m-1)*x[m])/(m+1)**2
    def g(x): return B-sum(c/x[:m])
    constraints=[{'type':'ineq','fun':g,'jac':lambda x: np.r_[c/x[:m]**2,0.]},
                 {'type':'ineq','fun':lambda x:x[m]-x[:m],
                  'jac':lambda x:np.column_stack((-np.eye(m),np.ones(m)))}]
    init=np.r_[np.full(m,sum(c)/B),sum(c)/B]
    opt=minimize(objective,init,method='SLSQP',bounds=[(1e-14,None)]*(m+1),
      constraints=constraints,options={'maxiter':1500,'ftol':1e-11})
    if opt.success:
      assert opt.fun+1e-6*max(1,F)>=F
      assert abs(opt.fun-F)<=2e-4*max(1,F)
    # Independent feasible random allocations verify exact sharp lower bound.
    for j in range(30):
      w=rng.dirichlet(np.ones(m))*(B/c)
      rv=1/w
      cmp=(sum(rv)+(m*m-1)*max(rv))/(m+1)**2
      assert cmp>=F-1e-9*max(1,F)
    checked+=1
print('PASS: exact five-vertex pseudoinverse and rational two-saturated-edge certificate')
print('PASS: uniform boundary and three distinct active-set profiles')
print(f'PASS: {checked} randomized positive-price problems: budget, dual equality, full pseudoinverse, convex competitors')
print(f'PASS: {30*checked} random feasible asymmetric allocations')
# Sharp ratio approached by concentrating unit cost on a single edge.
for m in range(2,9):
    c=np.r_[1.,np.full(m-1,1.e-12)]
    _,_,_,F,_=allocation(c,1.)
    eq=(m*m+m-1)*sum(c)/(m+1)**2
    assert abs(eq/F-(m*m+m-1)/m**2)<1e-4
print('PASS: sharp universal equal-weight comparison and its cost-concentration limit')
print('LIMIT: numerical checks are not a replacement for the all-parameter Cauchy/KKT proof')
