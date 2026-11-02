import numpy as np, math
from scipy.optimize import minimize
from verify_alternating_cycle import formula
rng=np.random.default_rng(393)
for m in [2,3,4,5,6]:
 for r in [.15,.55,.85,.99,1.]:
  n=2*m
  mass=np.array([r if j%2==0 else 1 for j in range(n)])
  q=np.sqrt(mass/mass.sum()); proj=np.outer(q,q)
  def mat(c):
   P=np.zeros((n,n));
   for j,x in enumerate(c):
    k=(j+1)%n; P[j,k]=x/mass[j];P[k,j]=x/mass[k]
   np.fill_diagonal(P,1-P.sum(axis=1))
   return np.sqrt(mass)[:,None]*P/np.sqrt(mass)[None,:]-proj
  constraints=[{'type':'ineq','fun':lambda z: mass-z[:-1]-np.roll(z[:-1],1)},
   {'type':'ineq','fun':lambda z: z[-1]-np.linalg.eigvalsh(mat(z[:-1]))[-1]},
   {'type':'ineq','fun':lambda z: z[-1]+np.linalg.eigvalsh(mat(z[:-1]))[0]}]
  a,mu,_,_=formula(m,r)
  best=1e3
  for rep in range(2):
   c=r*a*np.ones(n) if rep==0 else r*.2*rng.random(n)
   x0=np.append(c,.99)
   o=minimize(lambda z:z[-1],x0,method='SLSQP',bounds=[(0,None)]*n+[(0,1)],constraints=constraints, options={'ftol':1e-10,'maxiter':600})
   if o.success:best=min(best,o.fun)
  assert abs(best-mu)<3e-6, (m,r,mu,best)
  print(m,r,round(mu,7),round(best,7))
print('PASSED: 25 unrestricted numerical optimization cases, two starts each')
