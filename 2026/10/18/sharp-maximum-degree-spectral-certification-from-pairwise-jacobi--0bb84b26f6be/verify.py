import numpy as np
from math import sqrt
rng=np.random.default_rng(64211)
checks=0
for n in range(2,22):
 for rep in range(300):
  graph=rng.random((n,n))<rng.uniform(.05,.8)
  graph=np.triu(graph,1); graph=graph|graph.T
  delta=int(np.max(graph.sum(0)))
  if delta==0:continue
  d=rng.normal(size=n)*10**rng.uniform(-2,3)
  eps=10**rng.uniform(-4,1)
  q=rng.uniform(-1,1,size=(n,n));q=np.triu(q,1);q=q+q.T
  A=np.diag(d)
  for i in range(n):
   for j in range(i+1,n):
    if graph[i,j]: A[i,j]=A[j,i]=q[i,j]*sqrt(eps*(abs(d[i]-d[j])+eps))
  lam=np.linalg.eigvalsh(A)[::-1]
  observed=float(np.max(np.abs(lam-np.sort(d)[::-1])))
  assert observed<=delta*delta*eps*(1+5e-7), (n,delta,eps,observed)
  checks+=1
for delta in range(1,9):
 eps=.25
 z=[]
 for H in [1e3,1e4,1e5]:
  t=sqrt(eps*(H+eps)); A=np.block([[H*np.eye(delta), t*np.ones((delta,delta))], [t*np.ones((delta,delta)),np.zeros((delta,delta))]])
  top=np.linalg.eigvalsh(A)[-1]-H
  z.append(top/(delta*delta*eps))
  assert top<=delta*delta*eps*(1+1e-5)
  checks+=1
 assert z[-1]>.95
print('DEGREE_PIVOT_CHECK_PASS',checks)
