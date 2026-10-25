#!/usr/bin/env python3
"""Exhaustive small-order tests for stacking on triangle bouquets.

Pure standard-library script. Every unlabeled configuration under the graph's
pair-swap and blade-permutation automorphisms is represented exactly once.
"""
from functools import lru_cache

def canonical(c):
    pairs = sorted(tuple(sorted((c[2*i+1], c[2*i+2]))) for i in range((len(c)-1)//2))
    return (c[0],) + tuple(v for pair in pairs for v in pair)

def configurations(k, total):
    # enumerate weakly increasing leaf pair types by backtracking
    @lru_cache(None)
    def pairs(n, left, minimum):
        if n == 0:
            return ((),) if left == 0 else ()
        choices=[]
        for a in range(left+1):
            for b in range(a,left-a+1):
                if (a,b) < minimum: continue
                for tail in pairs(n-1,left-a-b,(a,b)):
                    choices.append(((a,b),)+tail)
        return tuple(choices)
    for h in range(total+1):
        for ps in pairs(k,total-h,(0,0)):
            yield (h,)+tuple(v for p in ps for v in p)

def adjacencies(k):
    adj=[set() for _ in range(2*k+1)]
    for i in range(k):
        u,v=2*i+1,2*i+2
        for a,b in ((0,u),(0,v),(u,v)):
            adj[a].add(b);adj[b].add(a)
    return tuple(tuple(sorted(x)) for x in adj)

def checker(k):
    adj=adjacencies(k)
    @lru_cache(None)
    def stackable(c):
        if sum(x>0 for x in c)==1: return True
        for u,number in enumerate(c):
            if number>=2:
                for v in adj[u]:
                    d=list(c);d[u]-=2;d[v]+=1
                    if stackable(canonical(d)): return True
        return False
    @lru_cache(None)
    def hub_reachable(c):
        if all(x==0 for x in c[1:]):return True
        for u,number in enumerate(c):
            if number>=2:
                for v in adj[u]:
                    d=list(c);d[u]-=2;d[v]+=1
                    if hub_reachable(canonical(d)):return True
        return False
    low=(1,1,1) if k==1 else (0,2*k+1,0)+tuple(x for _ in range(k-1) for x in (1,1))
    assert sum(low)==4*k-1 and not stackable(canonical(low)),(k,low)
    count=0
    for c in configurations(k,4*k):
        assert hub_reachable(c),('counterexample',k,c)
        count+=1
    print(f'k={k}: witness_at_{4*k-1}=not_stackable; exhaustive_orbits_at_{4*k}={count}; hub_only=all; stack_states={stackable.cache_info().currsize}; hub_states={hub_reachable.cache_info().currsize}')
for k in range(1,5): checker(k)
print('VERIFICATION_OK')
