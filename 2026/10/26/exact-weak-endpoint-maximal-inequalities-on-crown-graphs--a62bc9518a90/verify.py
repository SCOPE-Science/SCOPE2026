"""Exact-fraction stress checks for sharp weak-type crown-graph inequality.

The complete all-dimensions argument is in RESULT.md, not inferred from sampling.
Uses only Python standard library.
"""
from collections import deque
from fractions import Fraction as F
from itertools import combinations
import random


def balls(n, crown=True):
    N = 2*n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if not crown or i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    result = []
    for v in range(N):
        dist = [-1]*N
        dist[v] = 0
        q = deque([v])
        while q:
            u = q.popleft()
            for z in adj[u]:
                if dist[z] == -1:
                    dist[z] = dist[u]+1
                    q.append(z)
        assert min(dist) >= 0
        result.append([tuple(j for j in range(N) if dist[j] <= r) for r in range(max(dist)+1)])
    return result


def weak_ratio(n, nums, B):
    T = sum(nums)
    assert T > 0
    mx = [max(F(sum(nums[j] for j in b), len(b)) for b in B[v]) for v in range(2*n)]
    sx = sorted(mx, reverse=True)
    return max(F((j+1)*m,T) for j,m in enumerate(sx))


def compositions(total, parts):
    # Exhaustive integer compositions of total into parts, using separators.
    for sep in combinations(range(total+parts-1), parts-1):
        coords = (-1,)+sep+(total+parts-1,)
        yield tuple(coords[j+1]-coords[j]-1 for j in range(parts))


checks=0
for n in range(3,14):
    bc = balls(n,True)
    bk = balls(n,False)
    target = F(2*(n-1),n)
    comparison = F(2*n,n+1)
    inp=[1]*n+[0]*n
    assert weak_ratio(n,inp,bc)==target;checks+=1
    assert weak_ratio(n,inp,bk)==comparison;checks+=1
    assert comparison-target==F(2,n*(n+1));checks+=1
    for v in range(2*n):
        vals=bc[v][1]
        assert len(bc[v])==4 and len(vals)==n;checks+=1
    for v in range(2*n):
        assert set(bc[v][1]).isdisjoint(set(bc[(v+n)%(2*n)][1]));checks+=1
        assert len(set(bc[v][1]) | set(bc[(v+n)%(2*n)][1]))==2*n;checks+=1

rng=random.Random(240217)
for n in range(3,19):
    B=balls(n,True)
    for _ in range(550):
        inp=[rng.randrange(0,25) for _ in range(2*n)]
        if not sum(inp): inp[0]=1
        assert weak_ratio(n,inp,B)<=F(2*(n-1),n), (n,inp)
        checks+=1

for n,total in [(3,10),(4,7)]:
    B=balls(n,True)
    for inp in compositions(total,2*n):
        assert weak_ratio(n,inp,B)<=F(2*(n-1),n), (n,inp)
        checks+=1

print('ALL EXACT CHECKS PASSED:',checks)
