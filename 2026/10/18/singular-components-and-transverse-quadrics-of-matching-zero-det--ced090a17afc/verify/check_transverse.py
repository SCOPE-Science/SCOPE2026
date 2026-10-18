#!/usr/bin/env python3
"""Exact finite-field tangent-rank witnesses for corank-two matching-zero sections."""
from random import Random
from check_sparse import rank,det
P=101
rng=Random(23041)
def witness(n,k):
 r=n-2
 for _ in range(400):
  U=[[rng.randrange(1,P) for _ in range(r)] for i in range(n)]
  V=[]
  for i in range(n):
   if i<k:
    row=[rng.randrange(P) for _ in range(r-1)]
    row.append((-sum(U[i][t]*row[t] for t in range(r-1))*pow(U[i][-1],-1,P))%P)
   else:row=[rng.randrange(P) for _ in range(r)]
   V.append(row)
  A=[[sum(U[i][t]*V[j][t] for t in range(r))%P for j in range(n)] for i in range(n)]
  if rank(A,P)!=r:continue
  free=[(i,j) for i in range(n) for j in range(n) if not(i==j and i<k)]
  J=[]
  for di in range(n):
   for dj in range(n):
    g=[]
    for i,j in free:
     if i==di or j==dj:g.append(0);continue
     ii=[u for u in range(n) if u not in (di,i)]
     jj=[u for u in range(n) if u not in (dj,j)]
     g.append(((-1)**((i-(i>di))+(j-(j>dj))))*det([[A[t][s] for s in jj] for t in ii],P)%P)
    J.append(g)
  # rectangular rank
  m=[row[:] for row in J]; h=0
  for c in range(len(free)):
   pivot=next((t for t in range(h,len(m)) if m[t][c]%P),None)
   if pivot is None:continue
   m[h],m[pivot]=m[pivot],m[h]; inv=pow(m[h][c]%P,-1,P)
   for t in range(h+1,len(m)):
    mult=m[t][c]*inv%P
    if mult:
     m[t]=[(x-mult*y)%P for x,y in zip(m[t],m[h])]
   h+=1
   if h==len(m):break
  if h==4:return h,A
 raise AssertionError('No rank-four witness found')

if __name__=='__main__':
 for n in (4,5,6):
  for k in sorted(set((1,n//2,n))):
   j,a=witness(n,k)
   print('witness_GFp',P,'n',n,'k',k,'rank',rank(a,P),'Jacobian',j,'first_row',a[0])
 print('TRANSVERSE_OK')
