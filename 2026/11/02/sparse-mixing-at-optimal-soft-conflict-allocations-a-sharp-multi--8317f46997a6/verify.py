#!/usr/bin/env python3
"""Exact finite checks of soft-conflict allocation theorem on small instances.
All calculations use integer arithmetic; exhaustive over occupancy matrices, not labeled copies.
"""
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def compositions(total, r):
    if r==1:
        return ((total,),)
    return tuple((x,)+rest for x in range(total+1) for rest in compositions(total-x,r-1))

def brute(parts, n):
    m=sum(parts); q,rem=divmod(m,n)
    quotas=(q+1,)*rem+(q,)*(n-rem)
    r=len(parts)
    # enumerate all occupancy matrices for all allocations of labeled items (types suffice)
    best=None
    mixed_at_opt=set()
    count=0
    def dfs(j,left,cost,mixed):
        nonlocal best,count
        if j==n:
            if any(left): return
            count+=1
            if best is None or cost<best:
                best=cost; mixed_at_opt.clear();mixed_at_opt.add(mixed)
            elif cost==best:
                mixed_at_opt.add(mixed)
            return
        for x in compositions(quotas[j],r):
            if any(x[t]>left[t] for t in range(r)):continue
            loss=sum(x[t]*x[u] for t in range(r) for u in range(t+1,r))
            dfs(j+1,tuple(left[t]-x[t] for t in range(r)),cost+loss,mixed+(sum(v>0 for v in x)>1))
    dfs(0,parts,0,0)
    return best, mixed_at_opt, count

def test():
    checked=0
    matrices=0
    for r in (2,3,4):
      for parts in product(range(1,5),repeat=r):
        if sum(parts)>9:continue
        for n in range(1,min(5,sum(parts))+1):
          optimum,mixes,ct=brute(parts,n); matrices+=ct
          if not mixes or min(mixes)>r-1:
             raise AssertionError(('forest bound',parts,n,optimum,mixes))
          if r==2 and sum(parts)%n==0:
             q=sum(parts)//n; d=parts[0]%q
             if optimum!=d*(q-d):
                raise AssertionError(('exact bipartite',parts,n,optimum,d*(q-d)))
             if (min(mixes)!=int(d!=0) or max(mixes)!=int(d!=0)):
                raise AssertionError(('all optimizers one mixed',parts,n,mixes,d))
          checked+=1
    for r in range(2,10):
        n=r-1
        part_sizes=(r-1,)*r
        q=r
        # every part has strictly fewer than q items, so every equal-sized bundle must mix
        assert sum(part_sizes)==n*q and max(part_sizes)<q
    for n in range(3,50,2):
        parts=(n,n);agents=n;q=2
        d=n%q
        assert d*(q-d)==1
        assert parts[0]*parts[1]//agents==n
    print(f'PASS {checked} complete types/agent cases; {matrices} occupancy matrices; sharpness r=2..9; odd n=3..49.')

if __name__=='__main__':test()
