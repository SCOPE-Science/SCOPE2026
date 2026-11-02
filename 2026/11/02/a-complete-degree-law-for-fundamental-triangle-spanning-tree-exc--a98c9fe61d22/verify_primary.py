#!/usr/bin/env python3
"""Exact finite verification of wheel hub-triangle spanning-tree exchanges."""
from itertools import combinations
from collections import Counter, deque
from math import comb

def fib(n):
 a,b=0,1
 for _ in range(n):a,b=b,a+b
 return a

def enumerate_graph(r):
 edges=[(r,i) for i in range(r)]+[(i,(i+1)%r) for i in range(r)]
 def tree(s):
  par=list(range(r+1))
  def root(i):
   while i!=par[i]:i=par[i]
   return i
  for j in s:
   a,b=map(root,edges[j]);
   if a==b:return False
   par[a]=b
  return True
 states=[frozenset(c) for c in combinations(range(2*r),r) if tree(c)]
 idx={s:k for k,s in enumerate(states)}
 links=[set() for s in states]
 for i,s in enumerate(states):
  for j in range(r):
   face={j,(j+1)%r,r+j}
   if len(s&face)!=2:continue
   for old in s&face:
    new=(s-{old})|(face-s)
    assert new in idx
    links[i].add(idx[new])
 assert all(i in links[j] for i,a in enumerate(links) for j in a)
 seen={0};todo=[0]
 for i in todo:
  for j in links[i]:
   if j not in seen:seen.add(j);todo.append(j)
 assert len(seen)==len(states)
 distribution=Counter(len(a)//2 for a in links)
 assert all(len(a)%2==0 for a in links)
 assert sum(len(a) for a in links)//2 ==3*r*fib(2*r-2)
 return distribution

def gap_distribution(r):
 out=Counter()
 for mask in range(1,1<<r):
  spokes=[i for i in range(r) if mask>>i&1]
  gaps=[(spokes[(j+1)%len(spokes)]-spokes[j])%r or r for j in range(len(spokes))]
  current=Counter({0:1})
  for g in gaps:
   p=Counter({1:1 if g==1 else 2})
   if g>=3:p[2]=g-2
   nxt=Counter()
   for a,b in current.items():
    for c,w in p.items():nxt[a+c]+=b*w
   current=nxt
  out.update(current)
 return out
for r in range(3,9):
 direct=enumerate_graph(r)
 independent=gap_distribution(r)
 assert direct==independent,(r,direct,independent)
 assert independent[r]==1 and independent[1]==2*r
 print('WHEEL_PRIMARY_OK',r,'trees',sum(direct.values()),'edges',sum(k*v for k,v in direct.items()))
print('WHEEL_PRIMARY_COMPLETE')
