#!/usr/bin/env python3
"""Exact finite weighted subset-automaton check for a reversible cyclic generator."""
from math import gcd
from heapq import heappush,heappop
from collections import deque

def step(mask,n,k,ch):
 out=0
 for q in range(n):
  if mask>>q&1:
   t=(q+1)%n if ch=='a' else ((q-1)%n if ch=='c' else (k if q==0 else q))
   out|=1<<t
 return out

def opt(n,k,prices):
 root=(1<<n)-1;h=[(0,root)];ds={root:0};ways={root:1}
 while h:
  d,s=heappop(h)
  if d!=ds[s]:continue
  if s.bit_count()==1:break
  for ch,cost in prices.items():
   t=step(s,n,k,ch);new=d+cost
   if new<ds.get(t,10**30):ds[t]=new;ways[t]=ways[s];heappush(h,(new,t))
   elif new==ds.get(t):ways[t]+=ways[s]
 vals=[(ds[s],ways[s]) for s in ds if s.bit_count()==1]
 if not vals:return None
 best=min(x for x,y in vals)
 return best,sum(y for x,y in vals if x==best)

def run():
 cases=0;blocked=0
 for n in range(2,10):
  for k in range(1,n):
   if gcd(n,k)>1:
    assert opt(n,k,{'a':1,'b':1,'c':1}) is None
    blocked+=1;continue
   for ac,cc,bc in [(1,1,1),(1,7,3),(7,1,3),(k,n-k,2),(2*k,2*(n-k),7),(5,8,1)]:
    v,cnt=opt(n,k,{'a':ac,'b':bc,'c':cc})
    expected=(n-1)*bc+(n-2)*min((n-k)*ac,k*cc)
    ways=2**(n-2) if (n-k)*ac==k*cc else 1
    assert (v,cnt)==(expected,ways),(n,k,ac,cc,bc,v,cnt,expected,ways)
    cases+=1
 print(f'VERIFY_OK n=2..9 weighted_cases={cases} noncoprime={blocked} tie_counts=true')
if __name__=='__main__':run()
