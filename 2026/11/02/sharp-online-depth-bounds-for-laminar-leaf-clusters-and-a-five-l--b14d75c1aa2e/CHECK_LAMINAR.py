#!/usr/bin/env python3
"""Standalone finite verification for laminar leaf-cluster shattering."""
from functools import lru_cache
from itertools import combinations,combinations_with_replacement
from math import floor,log2

@lru_cache(None)
def leaves(t):
 return 1 if not t else sum(leaves(z) for z in t)

@lru_cache(None)
def shapes(n):
 if n==1:return ((),)
 available=tuple(sorted({t for k in range(1,n) for t in shapes(k)}, key=lambda t:(leaves(t),repr(t))))
 out=set()
 for k in range(2,n+1):
  for children in combinations_with_replacement(available,k):
   if sum(map(leaves,children))==n:out.add(children)
 return tuple(sorted(out,key=repr))

def clades(t):
 """Each node's leaf support, plus empty, with leaves numbered left-to-right."""
 pos=0;out=[]
 def visit(t):
  nonlocal pos
  if not t:
   v=1<<pos;pos+=1
  else:
   v=0
   for u in t:v|=visit(u)
  out.append(v)
  return v
 visit(t)
 assert len(set(out))==len(out)
 return [0]+out,pos

def full_rank(concepts,n):
 qu=[sum(1<<i for i,c in enumerate(concepts) if c>>j&1) for j in range(n)]
 @lru_cache(None)
 def f(mask):
  best=0
  for q in qu:
   yes=mask&q;no=mask&~q
   if yes and no:best=max(best,1+min(f(yes),f(no)))
  return best
 return f((1<<len(concepts))-1)

def vc_check(concepts,n):
 for k in range(n,0,-1):
  for s in combinations(range(n),k):
   if len({tuple((c>>j)&1 for j in s) for c in concepts})==1<<k:return k
 return 0

def complete(b,h):
 if h==0:return ()
 return tuple(complete(b,h-1) for _ in range(b))

def verify():
 for n in range(1,6):
  ranks=[]
  for t in shapes(n):
   concepts,m=clades(t)
   v=vc_check(concepts,m)
   assert v==(1 if n==1 else 2),(n,t,v)
   d=full_rank(concepts,m)
   assert d<=1+floor(log2(n))
   ranks.append(d)
  print('LEAF_SHAPES',n,'count',len(ranks),'rank_counts', {d:ranks.count(d) for d in set(ranks)})
  if n<=4: assert max(ranks)<=2
  if n==5:assert max(ranks)==3
 assert [len(shapes(n)) for n in range(1,6)]==[1,1,2,5,12]
 for b,hmax in [(2,4),(3,2),(4,2)]:
  for h in range(hmax+1):
   c,n=clades(complete(b,h));v=vc_check(c,n);d=full_rank(c,n)
   want=1+floor(log2(h+1))
   assert d==want,(b,h,d,want)
   assert v==(1 if h==0 else 2)
   print('COMPLETE_TREE',b,h,'leaves',n,'clades',len(c),'VC',v,'Ldim',d)
 print('ALL_LAMINAR_CLUSTER_CHECKS_PASS')
if __name__=='__main__':verify()
