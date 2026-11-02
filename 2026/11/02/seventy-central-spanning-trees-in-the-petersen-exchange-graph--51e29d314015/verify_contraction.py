from itertools import combinations
from collections import defaultdict
from math import comb
V=list(combinations(range(5),2))
E=[(i,j) for i in range(10) for j in range(i+1,10) if set(V[i]).isdisjoint(V[j])]
assert len(E)==15

def det(A):
 n=len(A)
 if n==0:return 1
 B=[row[:] for row in A];prev=1;sign=1
 for k in range(n-1):
  if B[k][k]==0:
   i=next((i for i in range(k+1,n) if B[i][k]!=0),None)
   if i is None:return 0
   B[k],B[i]=B[i],B[k];sign=-sign
  q=B[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    u=B[i][j]*q-B[i][k]*B[k][j]
    if u%prev:raise ValueError((u,prev,k))
    B[i][j]=u//prev
   B[i][k]=0
  prev=q
 return sign*B[-1][-1]

def contracted_trees(mask):
 par=list(range(10))
 def root(u):
  while u!=par[u]:u=par[u]
  return u
 for i,(u,v) in enumerate(E):
  if mask>>i&1:
   x,y=root(u),root(v)
   if x==y:return 0
   par[x]=y
 R={}
 cc=[]
 for u in range(10):
  v=root(u)
  if v not in R:R[v]=len(R)
  cc.append(R[v])
 n=len(R)
 L=[[0]*n for _ in range(n)]
 for i,(u,v) in enumerate(E):
  if mask>>i&1:continue
  a,b=cc[u],cc[v]
  if a==b:continue
  L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
 return det([r[:-1] for r in L[:-1]])

def test():
 A=[0]*10;N=0
 for m in range(1<<15):
  q=contracted_trees(m)
  if q:
   A[m.bit_count()]+=q*q;N+=1
 B=[sum((-1)**(j-r)*comb(j,r)*A[j] for j in range(r,10)) for r in range(10)]
 assert A[0]==4000000 and A[9]==2000
 print('nonzero forests',N, 'moments',A)
 print('intersection ordered',B)
 print('distance unordered',[B[9-d]//2 if d else B[9] for d in range(7)])
 assert sum(B)==4000000
 assert [B[9-d]//2 for d in range(1,7)] == [28140,222360,651080,748200,314220,35000]
 print('INDEPENDENT_CONTRACTION_MOMENTS_PASS')
if __name__=='__main__':test()
