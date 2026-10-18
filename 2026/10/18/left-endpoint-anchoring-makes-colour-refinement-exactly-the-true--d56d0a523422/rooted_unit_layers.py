#!/usr/bin/env python3
"""Independent BFS-layer stress test for the connected proper-interval ordering lemma.
The input construction and the checker use different invariants from the
color-refinement verifier. Tests are finite corroboration, not the proof.
"""
import sys
from itertools import combinations
from collections import deque

def choices(n):
 def dfs(i,lo,seq):
  if i==n:
   yield tuple(seq)
  else:
   for v in range(max(lo,i+1 if i<n-1 else i),n):
    yield from dfs(i+1,v,seq+[v])
 yield from dfs(0,0,[])

def isadj(r,i,j):
 return i!=j and (j<=r[i] if i<j else i<=r[j])

def check(r):
 n=len(r)
 layers=[-1]*n;layers[0]=0
 queue=deque([0])
 while queue:
  i=queue.popleft()
  for j in range(n):
   if isadj(r,i,j) and layers[j]<0:
    layers[j]=layers[i]+1
    queue.append(j)
 assert all(t>=0 for t in layers)
 D=max(layers)
 for d in range(D+1):
  bucket=[i for i in range(n) if layers[i]==d]
  assert bucket==list(range(bucket[0],bucket[-1]+1)),(r,d,bucket)
  assert all(isadj(r,i,j) for i,j in combinations(bucket,2)),(r,d)
  if d==0:continue
  pre=[i for i in range(n) if layers[i]==d-1]
  post=[i for i in range(n) if layers[i]==d+1]
  for i,j in combinations(bucket,2):
   sig=lambda u:(sum(isadj(r,u,x) for x in pre),sum(isadj(r,u,x) for x in post))
   if sig(i)!=sig(j):continue
   assert all(isadj(r,i,k)==isadj(r,j,k) for k in range(n) if k not in (i,j)),(r,d,i,j)
   assert isadj(r,i,j)
 return D

if __name__=='__main__':
 N=int(sys.argv[1]) if len(sys.argv)>1 else 11
 for n in range(1,N+1):
  count=0;diam=0
  for r in choices(n):
   count+=1
   diam=max(diam,check(r))
  print(f'n={n} checked={count} max_diameter={diam}',flush=True)
