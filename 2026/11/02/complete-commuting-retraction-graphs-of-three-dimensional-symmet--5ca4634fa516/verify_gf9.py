"""Independent GF(9) extension-field test for the symmetric Leibniz retraction theorem.
Use GF(3)[t]/(t^2+1), encoding a+bt as a+3b.
"""
from itertools import product
from collections import Counter

Q=9
ADD=[[((i%3+j%3)%3)+3*((i//3+j//3)%3) for j in range(Q)] for i in range(Q)]
NEG=[(-i%3)+3*((-(i//3))%3) for i in range(Q)]
MUL=[[((i%3*j%3+2*(i//3)*(j//3))%3)+3*((i%3*(j//3)+(i//3)*(j%3))%3)
      for j in range(Q)] for i in range(Q)]
# A^{-1} equals 1/A for all nonzero entries; no inversions needed.

def add(*xs):
 s=0
 for x in xs:s=ADD[s][x]
 return s

def prod(x,y):return MUL[x][y]

def sub(x,y):return ADD[x][NEG[y]]

def matmul(A,B):
 return tuple(tuple(add(*(prod(A[i][k],B[k][j]) for k in range(3)))
                   for j in range(3)) for i in range(3))

def verify(lam):
 assert lam!=0
 split=NEG[lam] in {prod(x,x) for x in range(1,Q)}
 E=[]
 for a,b,d,e,s,t in product(range(Q),repeat=6):
  c=add(prod(a,a),prod(lam,prod(b,b)))
  if add(prod(d,d),prod(lam,prod(e,e))) != prod(lam,c):continue
  if add(prod(a,d),prod(lam,prod(b,e)))!=0:continue
  A=((a,d,0),(b,e,0),(s,t,c))
  if matmul(A,A)==A:E.append(A)
 Z=((0,0,0),)*3;I=((1,0,0),(0,1,0),(0,0,1))
 assert I in E and Z in E
 assert len(E)==(2+2*Q*Q if split else 2),(lam,len(E))
 E=[e for e in E if e not in (I,Z)]
 deg=[0]*len(E);edges=0
 for i in range(len(E)):
  for j in range(i+1,len(E)):
   if matmul(E[i],E[j])==matmul(E[j],E[i]):
    edges+=1;deg[i]+=1;deg[j]+=1
 assert edges==(Q*Q if split else 0)
 if split:
  assert Counter(deg)=={Q:2*Q,0:2*Q*(Q-1)}
 print(f'GF(9), lambda={lam}, split={split}: count={len(E)+2}, noncentral_edges={edges}')

if __name__=='__main__':
 nonsq=[x for x in range(1,Q) if NEG[x] not in {prod(t,t) for t in range(1,Q)}]
 assert nonsq
 verify(1);verify(nonsq[0]);print('VERIFY_GF9_OK')
