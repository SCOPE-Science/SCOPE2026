"""Standalone independent checks of a block-cut recurrence for GP polynomial.
Only Python standard library. All graphs are simple and labeled 0..n-1.
"""
from collections import deque
from itertools import combinations,product
from random import Random
from math import comb
from block_gp import gp_polynomial

def add(a,b):
 n=max(len(a),len(b));out=[0]*n
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i]+=x
 return out

def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out

def gp_dp_from_blocks(n,blocks):
 # Block-clique incidence tree. Original vertices 0..n-1; block nodes n..n+k-1.
 T=[[]for _ in range(n+len(blocks))]
 for j,vs in enumerate(blocks):
  for v in vs:T[n+j].append(v);T[v].append(n+j)
 if n==1 and not blocks:return [1,1]
 assert len(T)>n
 seen=set()
 def rec(v,p):
  seen.add(v)
  child=[rec(w,v) for w in T[v] if w!=p]
  prod=[1]
  for A,B in child:prod=mul(prod,add([1],A))
  prod=add(prod,[-1])
  B=[0]
  for A,Z in child:B=add(B,Z)
  if v<n:
   A=add(prod,[0,1])
   terms=[0]
   for X,Z in child:terms=add(terms,X)
   B=add(B,[0]+terms)
  else:A=prod
  return A,B
 A,B=rec(n,-1)
 assert len(seen)==len(T)
 return add([1],add(A,B))

def brute(n,blocks):
 adj=[set()for _ in range(n)]
 for block in blocks:
  for u,v in combinations(block,2):adj[u].add(v);adj[v].add(u)
 dist=[]
 for s in range(n):
  d=[n+1]*n;d[s]=0;Q=deque([s])
  while Q:
   v=Q.popleft()
   for w in adj[v]:
    if d[w]>d[v]+1:d[w]=d[v]+1;Q.append(w)
  assert max(d)<n
  dist.append(d)
 invalid_triples=[]
 for a,b,c in combinations(range(n),3):
  if (dist[a][b]+dist[b][c]==dist[a][c] or dist[a][c]+dist[c][b]==dist[a][b] or dist[b][a]+dist[a][c]==dist[b][c]):
   invalid_triples.append((1<<a)|(1<<b)|(1<<c))
 out=[0]*(n+1)
 for S in range(1<<n):
  if not any(S&M==M for M in invalid_triples):out[S.bit_count()]+=1
 return out

def build(profile):
 # Each new block is a clique sharing precisely one prior vertex.
 n=1;blocks=[]
 for anchor,size in profile:
  block=[anchor]+list(range(n,n+size-1));blocks.append(block);n+=size-1
 return n,blocks

def main():
 rng=Random(40051);cases=0;totalsets=0
 # Full enumeration of all small ordered block-attachment templates,
 # including trees, clique bouquets and chains.
 for lengths in range(1,5):
  for sizes in product((2,3,4),repeat=lengths):
   n=1+sum(t-1 for t in sizes)
   if n>13:continue
   for t in range(25):
    prof=[];N=1
    for s in sizes:
     prof.append((rng.randrange(N),s));N+=s-1
    n,blocks=build(prof)
    pred=gp_dp_from_blocks(n,blocks)
    actual=brute(n,blocks)
    assert pred+[0]*(len(actual)-len(pred))==actual,(prof,pred,actual)
    edges=set()
    for block in blocks:
     for e in combinations(block,2):edges.add(e)
    assert gp_polynomial(n,edges)==actual,(prof,actual)
    incid=[0]*n
    for block in blocks:
     for v in block:incid[v]+=1
    assert max(i for i,x in enumerate(actual) if x>0)==sum(k==1 for k in incid)
    cases+=1;totalsets+=1<<n
 # Deterministic multivariate large graphs: count all coefficients without brute force.
 for k in (30,50,100,200):
  profile=[];N=1
  for t in range(k):
   size=2+(t%5==0)
   profile.append((rng.randrange(N),size));N+=size-1
  n,blocks=build(profile)
  p=gp_dp_from_blocks(n,blocks)
  edges=set()
  for block in blocks:
   for e in combinations(block,2):edges.add(e)
  assert gp_polynomial(n,edges)==p+[0]*(n+1-len(p))
  assert p[:3]==[1,n,comb(n,2)], (n,p[:3])
  assert p[-1]>=0
  incid=[0]*n
  for block in blocks:
   for v in block:incid[v]+=1
  assert max(i for i,x in enumerate(p) if x>0)==sum(k==1 for k in incid)
 print(f'VERIFICATION_OK tested_block_graphs={cases} exhaustive_vertex_subsets={totalsets} large_blocks=30,50,100,200')
if __name__=='__main__':main()
