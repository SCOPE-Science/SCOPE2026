import numpy as np
from math import comb
for d in range(2,7):
  N=2**d; A=np.zeros((N,N))
  for i in range(N):
    for b in range(d): A[i,i^(1<<b)]=1
  for k in range(1,d+1):
    a=np.zeros(N);b=np.zeros(N);a[0]=1;b[(1<<k)-1]=1
    V=[]
    for j in range(d+1):
      V.extend([a.copy(),b.copy()]);a=A@a;b=A@b
    rank=np.linalg.matrix_rank(np.column_stack(V),tol=1e-6)
    expected= d+1 if k==d else 2*d
    assert rank==expected,(d,k,rank,expected)
print('PASS: all 20 pair-distance/rank tests for 2<=d<=6')
