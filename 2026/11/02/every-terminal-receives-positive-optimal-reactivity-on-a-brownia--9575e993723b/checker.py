"""Independent checks for partially absorbing metric-star resource allocation."""
import numpy as np
import sympy as sp
from scipy.optimize import minimize
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

x,ell,v=sp.symbols('x ell v',positive=True)
a=ell*(1+x*ell/2)/(1+x*ell)
b=x/(1+x*ell)
f=a-v*b
assert sp.simplify(sp.diff(f,x)+(ell**2/2+v)/(1+x*ell)**2)==0
assert sp.simplify(sp.diff(f,x,2)-2*ell*(ell**2/2+v)/(1+x*ell)**3)==0

def val(L,k):
 d=1+L*k
 return np.sum(L*(1+.5*L*k)/d)/np.sum(k/d)

rng=np.random.default_rng(20261025)
checks=0;maxresid=0
for n in range(3,9):
 for _ in range(35):
  L=10**rng.uniform(-1.3,1.3,size=n)
  K=10**rng.uniform(-2,1.7)
  opt=minimize(lambda z:val(L,z),K*rng.dirichlet(np.ones(n)),method='SLSQP',
    constraints=[{'type':'eq','fun':lambda z:sum(z)-K}], bounds=[(0,K)]*n,
    options={'ftol':1e-11,'maxiter':1500})
  if not opt.success and abs(sum(opt.x)-K)>1e-7:raise AssertionError('optimizer failure')
  assert all(opt.x>1e-7*K), (L,K,opt.x)
  V=val(L,opt.x)
  lag=(L*L/2+V)/(1+L*opt.x)**2
  maxresid=max(maxresid,np.ptp(lag)/max(1,np.mean(lag)))
  # A lower bound on the optimized lifetime, needed in the no-inactive-arm proof.
  assert V>=np.sum(L)/(2*K)-1e-8
  for _ in range(12):
   r=K*rng.dirichlet(np.ones(n))
   assert V<=val(L,r)+5e-7*max(1,V)
  checks+=1
print('PASS: strict-convexity symbolic derivatives and 210 randomized star optimizations')
print('PASS: 2520 independent Dirichlet allocations, budget lower bound, positive arms')
print('maximum relative KKT spread',maxresid)
