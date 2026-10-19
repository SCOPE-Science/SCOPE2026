from itertools import product
from math import comb
L=((2,0),(0,1)); R=((0,-2),(1,0))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
for n in range(1,13):
 counts={}
 for w in product('LR',repeat=n):
  t=w.count('R')
  if t==0: continue
  A=((1,0),(0,1)); p=0; D=0
  for z in w:
   A=mm(L if z=='L' else R,A)
   p+=(z=='R');D+=(-1)**p
  if t%2==0:
   assert A[0][1]==A[1][0]==0
   assert (abs(A[0][0]),abs(A[1][1]))==(2**((n+D)//2),2**((n-D)//2)), (w,A,D)
   counts[D]=counts.get(D,0)+1
  else:
   assert A[0][0]==A[1][1]==0
   assert A[0][1]*A[1][0]==-(2**n), (w,A)
 exp={n-2*k:comb(n-1,k)-(k==0) for k in range(n)}
 exp={k:v for k,v in exp.items() if v>0}
 assert counts==exp,(n,counts,exp)
 print(n, 'real',sum(counts.values()),'complex',2**(n-1))
print('CHECK_OK')
