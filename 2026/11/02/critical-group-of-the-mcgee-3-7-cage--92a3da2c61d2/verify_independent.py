#!/usr/bin/env python3
"""Independent exact p-adic computation for the McGee graph's critical group.

Runs with Python 3 standard library only. Constructs a separately indexed
edge realization and computes the reduced-Laplacian determinant (Bareiss)
and its primary Smith exponents by modular unit-pivot elimination.
"""
from math import prod

EDGE_TEXT = '''
0 1 0 17 0 23 1 13 1 2 2 3 2 9 3 20 3 4 4 16 4 5 5 12
5 6 6 23 6 7 7 19 7 8 8 15 8 9 9 10 10 11 10 22 11 12
11 18 12 13 13 14 14 15 14 21 15 16 16 17 17 18 18 19
19 20 20 21 21 22 22 23
'''
V = 24
numbers = [int(s) for s in EDGE_TEXT.split()]
edges = {tuple(sorted(numbers[i:i+2])) for i in range(0,len(numbers),2)}
assert len(numbers) == 72 and len(edges) == 36
assert all(u!=v and 0<=u<v<V for u,v in edges)
degrees = [0]*V
for u,v in edges:degrees[u]+=1;degrees[v]+=1
assert degrees == [3]*V

def girth(edge_set):
 adj = [[] for _ in range(V)]
 for u,v in edge_set:adj[u].append(v);adj[v].append(u)
 best=V+1
 for root in range(V):
  dist={root:0}; parents={root:-1};queue=[root]
  for u in queue:
   for v in adj[u]:
    if v not in dist:
     dist[v]=dist[u]+1;parents[v]=u;queue.append(v)
    elif parents[u]!=v:best=min(best,dist[u]+dist[v]+1)
  assert len(dist)==V
 return best
assert girth(edges)==7

def reduced_laplacian(edge_set):
 mat=[[0]*23 for _ in range(23)]
 for u,v in edge_set:
  if u<23:mat[u][u]+=1
  if v<23:mat[v][v]+=1
  if u<23 and v<23:mat[u][v]-=1;mat[v][u]-=1
 return mat

def bareiss(A):
 A=[r[:] for r in A]
 n=len(A); prev=1; sign=1
 for k in range(n-1):
  if A[k][k]==0:
   i=next((i for i in range(k+1,n) if A[i][k]),None)
   if i is None:return 0
   A[k],A[i]=A[i],A[k];sign=-sign
  pivot=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=A[i][j]*pivot-A[i][k]*A[k][j]
    assert num%prev==0
    A[i][j]=num//prev
  for i in range(k+1,n):A[i][k]=0
  prev=pivot
 return sign*A[-1][-1]

def valuations(A,p,precision):
 mod=p**precision
 B=[[x%mod for x in row] for row in A]
 n=len(B);result=[]
 def v_p(x):
  if x==0:return precision
  v=0
  while x%p==0:v+=1;x//=p
  return v
 for k in range(n):
  choices=[(v_p(B[i][j]),i,j) for i in range(k,n) for j in range(k,n)]
  exponent,i,j=min(choices)
  if exponent==precision:
   result.extend([precision]*(n-k));break
  B[k],B[i]=B[i],B[k]
  for row in B:row[k],row[j]=row[j],row[k]
  unit = B[k][k]//(p**exponent)
  inverse=pow(unit,-1,mod)
  B[k]=[(x*inverse)%mod for x in B[k]]
  assert B[k][k] == p**exponent
  for i in range(k+1,n):
   t=B[i][k]
   assert t%(p**exponent)==0
   q=t//(p**exponent)
   B[i]=[(x-q*y)%mod for x,y in zip(B[i],B[k])]
  for j in range(k+1,n):
   t=B[k][j]
   assert t%(p**exponent)==0
   q=t//(p**exponent)
   for i in range(n):B[i][j]=(B[i][j]-q*B[i][k])%mod
  assert all(B[k][j]==0 for j in range(k+1,n))
  assert all(B[i][k]==0 for i in range(k+1,n))
  result.append(exponent)
 return sorted(result)

M = reduced_laplacian(edges)
order=bareiss(M)
assert order==168664320,(order,'unexpected determinant')
expected={2:[2,2,4],3:[1,1],5:[1],11:[1,1,1,1]}
for p,vals in expected.items():
 r=valuations(M,p,10)
 assert [x for x in r if x] == vals,(p,r)
 assert sum(r)==sum(vals)
 assert order%(p**sum(vals))==0
print('INDEPENDENT_MODULAR_PASS')
print('vertices=24 edges=36 girth=7 determinant=',order)
print('primary_exponents=',expected)
