from scipy.optimize import minimize
from verify import optimum
import random, numpy as np
rng=random.Random(1)
checks=0
solver_successes=0
for m in (2,3,4,5):
 for attempt in range(5):
  arms=[[float(rng.randrange(1,10)) for _ in range(rng.randrange(1,4))] for _ in range(m)]
  B=10.0
  w0,D,R=optimum(arms,B)
  c=np.array(sum(arms,[]));n=len(c)
  blocks=[];k=0
  for a in arms:
   blocks.append(np.arange(k,k+len(a)));k+=len(a)
  pairs=[np.r_[blocks[i],blocks[j]] for i in range(m) for j in range(i+1,m)]
  x0=np.r_[np.full(n,B/sum(c)),D*2]
  con=[{'type':'eq','fun':lambda x: np.dot(c,x[:n])-B,'jac':lambda x: np.r_[c,0]}]
  for ix in pairs:
   def f(x,ix=ix): return x[-1] - sum(1/x[ix])
   def df(x,ix=ix):
    y=np.zeros(n+1);y[ix]=1/x[ix]**2;y[-1]=1;return y
   con.append({'type':'ineq','fun':f,'jac':df})
  sol=minimize(lambda x:x[-1],x0,jac=lambda x: np.r_[np.zeros(n),1],bounds=[(1e-7,None)]*n+[(0,None)],constraints=con,method='SLSQP',options={'ftol':1e-11,'maxiter':500})
  assert abs(sol.fun-D)<1e-7, (m,attempt,sol.message,sol.fun,D)
  checks+=1
  solver_successes+=int(sol.success)
print('Numerical epigraph objective agreements',checks,'/20; optimizer success flags',solver_successes,'/20')
print('Non-success flags, if any, indicate line-search termination; objective tolerance is checked separately.')
