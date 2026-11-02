#!/usr/bin/env python3
"""Stand-alone exact Smith certificate checker for the 24-vertex McGee graph.

Only the Python standard library is needed. Each recorded matrix operation is
integer-unimodular; replaying them proves the stated cokernel decomposition.
"""
import json
from math import prod
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent/'certificate.json').read_text(encoding='utf-8'))
assert DATA['schema_version']==1
assert DATA['lcf_steps']==[-12,7,-7] and DATA['lcf_repetitions']==8
n=len(DATA['lcf_steps'])*DATA['lcf_repetitions']
assert n==24 and DATA['root_vertex_zero_based']==23
edges=set()
for i in range(n):
 edges.add(tuple(sorted((i,(i+1)%n))))
 edges.add(tuple(sorted((i,(i+DATA['lcf_steps'][i%3])%n))))
assert len(edges)==36 and all(u!=v for u,v in edges)
deg=[0]*n;adj=[[] for _ in range(n)]
for u,v in edges:deg[u]+=1;deg[v]+=1;adj[u].append(v);adj[v].append(u)
assert deg==[3]*n

def girth():
 answer=n+1
 for root in range(n):
  distance={root:0};parent={root:-1};queue=[root]
  for u in queue:
   for v in adj[u]:
    if v not in distance:
     distance[v]=distance[u]+1;parent[v]=u;queue.append(v)
    elif parent[u]!=v:
     answer=min(answer,distance[u]+distance[v]+1)
  assert len(queue)==n
 return answer
assert girth()==7
A=[[0]*23 for _ in range(23)]
for u,v in edges:
 if u<23:A[u][u]+=1
 if v<23:A[v][v]+=1
 if u<23 and v<23:A[u][v]-=1;A[v][u]-=1
for op in DATA['operations']:
 kind=op[0]
 if kind=='row_swap':
  _,i,j=op;assert 0<=i<23 and 0<=j<23 and i!=j
  A[i],A[j]=A[j],A[i]
 elif kind=='col_swap':
  _,i,j=op;assert 0<=i<23 and 0<=j<23 and i!=j
  for row in A:row[i],row[j]=row[j],row[i]
 elif kind=='row_add':
  _,i,j,q=op;assert 0<=i<23 and 0<=j<23 and i!=j and isinstance(q,int)
  A[i]=[x+q*y for x,y in zip(A[i],A[j])]
 elif kind=='col_add':
  _,i,j,q=op;assert 0<=i<23 and 0<=j<23 and i!=j and isinstance(q,int)
  for row in A:row[i]+=q*row[j]
 elif kind=='row_neg':
  _,i=op;assert 0<=i<23;A[i]=[-x for x in A[i]]
 else:raise AssertionError(f'Unrecognized elementary operation {kind}')
diag=DATA['diagonal']
assert len(diag)==23 and diag==[1]*19+[11,44,132,2640]
assert all(A[i][j]==(diag[i] if i==j else 0) for i in range(23) for j in range(23))
assert all(diag[i]>0 and diag[i+1]%diag[i]==0 for i in range(22))
assert prod(diag)==DATA['spanning_tree_count']==168664320
print('INTEGER_SMITH_CERTIFICATE_PASS')
print('vertices',n,'edges',len(edges),'girth',girth(),'operations',len(DATA['operations']))
print('invariant_factors',diag[19:],'spanning_trees',prod(diag))
