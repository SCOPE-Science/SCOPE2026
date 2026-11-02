"""Exact self-contained check of the Coxeter graph sandpile decomposition."""
import json
from itertools import combinations
from collections import deque
from pathlib import Path

P=Path(__file__).with_name('certificate.json')
C=json.loads(P.read_text())
V=[tuple(x) for x in combinations(range(7),3) if frozenset(x) not in {frozenset((i,(i+1)%7,(i+3)%7)) for i in range(7)}]
assert V==[tuple(x) for x in C['vertices']]
assert len(V)==28
Adj=[[int(i!=j and set(a).isdisjoint(b)) for j,b in enumerate(V)] for i,a in enumerate(V)]
assert all(sum(row)==3 for row in Adj)
assert sum(map(sum,Adj))==84
# BFS girth check: for each root, every non-tree edge yields a cycle.
girth=999
for root in range(28):
 dist=[-1]*28;par=[-1]*28;dist[root]=0;q=deque([root])
 while q:
  a=q.popleft()
  for b in range(28):
   if not Adj[a][b]:continue
   if dist[b]<0:dist[b]=dist[a]+1;par[b]=a;q.append(b)
   elif par[a]!=b:girth=min(girth,dist[a]+dist[b]+1)
 assert all(d>=0 for d in dist)
assert girth==7
L=[[3*(i==j)-Adj[i][j] for j in range(27)] for i in range(27)]
B=C['inverse_multiplier_56'];assert len(B)==27 and all(len(r)==27 for r in B)
assert all(sum(L[i][k]*B[k][j] for k in range(27))==(56 if i==j else 0) for i in range(27) for j in range(27))

def bareiss(A):
 a=[r[:] for r in A];n=len(a);prev=1;sign=1
 for k in range(n-1):
  if a[k][k]==0:
   j=next(j for j in range(k+1,n) if a[j][k]);a[j],a[k]=a[k],a[j];sign=-sign
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=a[i][j]*pivot-a[i][k]*a[k][j]
    assert num%prev==0
    a[i][j]=num//prev
  for i in range(k+1,n):a[i][k]=0
  prev=pivot
 return sign*a[-1][-1]
assert bareiss(L)==4405854208==2**18*7**5

def rank_mod(A,p):
 a=[[x%p for x in row] for row in A];nr=len(a);nc=len(a[0]);r=0
 for c in range(nc):
  t=next((i for i in range(r,nr) if a[i][c]),None)
  if t is None:continue
  a[t],a[r]=a[r],a[t]
  f=pow(a[r][c],-1,p);a[r]=[x*f%p for x in a[r]]
  for i in range(r+1,nr):
   f=a[i][c]
   if f:a[i]=[(x-f*y)%p for x,y in zip(a[i],a[r])]
  r+=1
 return r
assert rank_mod(L,2)==21 and rank_mod(L,7)==22
# A 56-multiple of the inverse is integral, hence every Smith factor divides 56.
# Six factors have positive 2-valuation summing to 18; thus each is 2^3.
# Five factors have positive 7-valuation summing to 5; thus each is 7.
# Divisibility forces these five 7 factors onto five of the six 8 factors.
print('COXETER_INTEGRAL_CERTIFICATE_PASS: 28 vertices; 42 edges; girth 7; critical group Z/8 + (Z/56)^5; tree count 4405854208')
