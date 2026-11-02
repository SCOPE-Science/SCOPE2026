#!/usr/bin/env python3
"""Independent finite checks for exact distances in mutual-visibility token layers.
Only the mathematical properties of the input graphs are encoded here.
Run: python verify_mv_isometry.py
"""
from itertools import combinations
from collections import deque

def cycle_distance(n,a,b):
    d=abs(a-b)
    return min(d,n-d)

def visible_by_definition(n,S):
    for a,b in combinations(S,2):
        d=cycle_distance(n,a,b)
        ok=False
        for sign in (1,-1):
            if all((a+sign*i)%n not in S for i in range(1,d)) and (a+sign*d)%n==b:
                ok=True
        if not ok: return False
    return True

def gap_bounded(n,S,U):
    s=sorted(S)
    return max([s[i+1]-s[i] for i in range(len(s)-1)]+[s[0]+n-s[-1]])<=U

def adjacency(n,S):
    result=[]
    for x in S:
        for y in ((x+1)%n,(x-1)%n):
            if y not in S:
                result.append(tuple(sorted((set(S)-{x})|{y})))
    return set(result)

def bfs(adj,start):
    dist={start:0}
    q=deque([start])
    while q:
        s=q.popleft()
        for t in adj[s]:
            if t not in dist:
                dist[t]=dist[s]+1
                q.append(t)
    return dist

def cyclic_transport(n,S,T):
    a=set(S);b=set(T);total=0; vals=[]
    for j in range(n):
        total+=int(j in a)-int(j in b)
        vals.append(total)
    vals2=sorted(vals)
    median=vals2[n//2]
    return sum(abs(v-median) for v in vals)

pairs_total=0
for n in range(3,18):
    universe=list(combinations(range(n),3))
    good=[S for S in universe if visible_by_definition(n,S)]
    assert all(visible_by_definition(n,S)==gap_bounded(n,S,n//2) for S in universe)
    allset=set(universe); gset=set(good)
    adj_full={S:adjacency(n,S)&allset for S in universe}
    adj_good={S:adjacency(n,S)&gset for S in good}
    for S in good:
        d_full=bfs(adj_full,S)
        d_good=bfs(adj_good,S)
        assert len(d_good)==len(good),(n,S,'not connected')
        for T in good:
            assert d_full[T]==d_good[T]==cyclic_transport(n,S,T), (n,S,T,d_full[T],d_good[T],cyclic_transport(n,S,T))
            pairs_total+=1
    print(f'n={n}: {len(good)} visible triples, {len(good)**2} ordered pair distances agree')

# Strict slack in kU>n is necessary: equal-gap saturated configurations are frozen.
n,k,U=6,3,2
A=(0,2,4);B=(1,3,5)
assert gap_bounded(n,A,U) and gap_bounded(n,B,U)
assert not any(gap_bounded(n,T,U) for T in adjacency(n,A))
assert cyclic_transport(n,A,B)<100
print('VERIFY_OK: direct-geodesic predicate = cyclic gap criterion; exact layer and full token distances = cyclic median flow for',pairs_total,'ordered pairs; saturation obstruction checked')
