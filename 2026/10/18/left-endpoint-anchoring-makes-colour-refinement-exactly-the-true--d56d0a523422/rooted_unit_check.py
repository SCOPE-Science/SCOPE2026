#!/usr/bin/env python3
"""Exhaustively test a left-rooted graph invariant on proper interval orderings.
No outside packages required. A nondecreasing right-endpoint sequence encodes
every connected proper interval graph with a fixed left-to-right ordering.
"""
import sys
from collections import defaultdict

def encodings(n):
 def rec(i,lower,arr):
  if i==n:
   yield tuple(arr)
   return
  for x in range(max(lower,i+(i<n-1)),n):
   arr.append(x)
   yield from rec(i+1,x,arr)
   arr.pop()
 yield from rec(0,0,[])

def neighbors(R):
 n=len(R)
 return [frozenset(j for j in range(n) if j!=i and (i<j<=R[i] or j<i<=R[j])) for i in range(n)]

def refine(adj):
 n=len(adj);colors=[int(i==0) for i in range(n)]
 for _ in range(n+2):
  labels=[(colors[i],tuple(sorted(colors[j] for j in adj[i]))) for i in range(n)]
  ks={x:k for k,x in enumerate(sorted(set(labels)))}
  updated=[ks[x] for x in labels]
  if all((updated[i]==updated[j])==(colors[i]==colors[j]) for i in range(n) for j in range(n)):
   return updated
  colors=updated
 raise AssertionError('No convergence')

def check(n):
 total=0
 for R in encodings(n):
  total+=1
  adj=neighbors(R)
  colors=refine(adj)
  for u in range(n):
   for v in range(u+1,n):
    same=(colors[u]==colors[v])
    twin=(u!=0 and v!=0 and adj[u]|{u}==adj[v]|{v})
    if same!=twin:
     raise AssertionError((n,R,u,v,colors,sorted(adj[u]),sorted(adj[v])))
 return total

if __name__=='__main__':
 N=int(sys.argv[1]) if len(sys.argv)>1 else 11
 for n in range(1,N+1):print(n,check(n),flush=True)
