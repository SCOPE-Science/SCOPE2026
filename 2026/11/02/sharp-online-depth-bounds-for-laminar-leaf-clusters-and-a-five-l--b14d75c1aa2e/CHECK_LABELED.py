#!/usr/bin/env python3
"""Separate labeled-partition enumeration and independent shattering recurrence."""
from functools import lru_cache
from itertools import product

def partitions(seq):
 res=[[(seq[0],)]]
 for x in seq[1:]:
  nxt=[]
  for p in res:
   for j in range(len(p)):
    q=[tuple(b) for b in p];q[j]=q[j]+(x,);nxt.append(q)
   nxt.append(p+[(x,)])
  res=nxt
 return [p for p in res if len(p)>1]

@lru_cache(None)
def hierarchies(ids):
 if len(ids)==1:return (ids[0],)
 out=[]
 for blocks in partitions(ids):
  for children in product(*(hierarchies(tuple(b)) for b in blocks)):
   out.append(tuple(children))
 return tuple(out)

def canon(t):
 return () if isinstance(t,int) else tuple(sorted((canon(x) for x in t),key=repr))

def masks(t):
 if isinstance(t,int):return [1<<t],1<<t
 out=[];v=0
 for c in t:
  sub,q=masks(c);out.extend(sub);v|=q
 return out+[v],v

def rank(clades,n):
 universe=(1<<len(clades))-1
 choices=[]
 for x in range(n):
  choices.append(sum((1<<i) for i,m in enumerate(clades) if (m>>x)&1))
 @lru_cache(None)
 def recurse(s):
  v=0
  for q in choices:
   a=s&q;b=s&~q
   if a and b:v=max(v,1+min(recurse(a),recurse(b)))
  return v
 return recurse(universe)

def run():
 for n in range(1,6):
  groups={}
  for t in hierarchies(tuple(range(n))):
   key=repr(canon(t))
   allc,_=masks(t)
   d=rank([0]+allc,n)
   groups.setdefault(key,set()).add(d)
  assert all(len(x)==1 for x in groups.values())
  ranks=[next(iter(x)) for x in groups.values()]
  print('LABELED_GENERATOR',n,'labeled',len(hierarchies(tuple(range(n)))),'types',len(groups),'Ldim_counts', {k:ranks.count(k) for k in set(ranks)})
  if n<=4:assert max(ranks)<=2
  if n==5:assert max(ranks)==3 and ranks.count(3)==3
 print('INDEPENDENT_LABELED_HIERARCHY_CHECK_PASS')
if __name__=='__main__':run()
