import numpy as np,itertools
checks=0
for n in range(3,10):
 A=np.zeros((2*n,2*n))
 for i in range(n):
  for j in range(n):
   if i!=j:A[i,n+j]=A[n+j,i]=1
 vals,vecs=np.linalg.eigh(A)
 evs=sorted(set(round(x,8) for x in vals))
 assert len(evs)==4, (n,evs)
 masks=range(1,2**(2*n)) if n<=5 else [1,2**n,(1<<n)|(1<<(2*n-1)),(1<<(2*n))-1]
 for mask in masks:
  T=[v for v in range(2*n) if mask>>v&1]
  I={v%n for v in T}; t=len(I)
  bright=np.zeros((2*n,2*n))
  rank=0
  for ev in evs:
   J=np.where(abs(vals-ev)<1e-6)[0]
   X=vecs[:,J]
   M=X[T,:]
   _,s,Vt=np.linalg.svd(M,full_matrices=True)
   r=int(np.sum(s>1e-8))
   rank+=r
   if r:
    U=X@Vt[:r,:].T
    bright+=U@U.T
  expected=2+2*min(t,n-1)
  assert rank==expected,(n,mask,rank,expected)
  for v in range(2*n):
   target=1. if v%n in I or t>=n-1 else 1/(n-t)
   assert abs(bright[v,v]-target)<1e-8,(n,mask,v,bright[v,v],target)
  checks+=1
 print(n,'checked',len(masks),'patterns')
print('NUMERIC_OK checks=',checks)
