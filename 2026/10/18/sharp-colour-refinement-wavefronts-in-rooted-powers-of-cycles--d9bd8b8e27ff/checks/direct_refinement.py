"""Finite independent graph-level regression checks for marked cycle powers.
No claim is made that finite tests prove the all-parameter theorem.
"""
from collections import Counter

def partition(c):
    classes = {}
    for u, x in enumerate(c):
        classes.setdefault(x, []).append(u)
    return frozenset(frozenset(x) for x in classes.values())

def refine(n, k):
    graph = [[v for v in range(n) if v != u and min((v-u)%n,(u-v)%n)<=k] for u in range(n)]
    colors = [1 if u == 0 else 0 for u in range(n)]
    out = [partition(colors)]
    for _ in range(n):
        sign = [(colors[u],tuple(sorted(Counter(colors[v] for v in graph[u]).items()))) for u in range(n)]
        ids = {s:i for i,s in enumerate(sorted(set(sign)))}
        nxt = [ids[s] for s in sign]
        part = partition(nxt)
        if part == out[-1]:
            break
        out.append(part)
        colors = nxt
    else: raise AssertionError('not stable')
    return out

def expected(n,k,r):
    D=n//2
    if r==0:
        dist_groups=[{0},set(range(1,D+1))]
    elif r==1:
        dist_groups=[{0},set(range(1,k+1)),set(range(k+1,D+1))]
    elif n==4*k:
        if r==2:
            dist_groups=[{d} for d in range(2*k-1)]+[{2*k-1,2*k}]
        else:
            dist_groups=[{d} for d in range(D+1)]
    else:
        boundary=min(r*k,D)
        dist_groups=[{d} for d in range(boundary+1)]+[set(range(boundary+1,D+1))]
    return frozenset(frozenset(u for u in range(n) if min(u,n-u) in g) for g in dist_groups if g)

count=0;vertices=0; round_total=0
for k in range(2,15):
    for n in range(4*k,10*k+13):
        observed=refine(n,k)
        D=n//2
        R=3 if n==4*k else max(2,(D-1+k-1)//k)
        assert len(observed)-1==R,(n,k,len(observed)-1,R)
        for r,p in enumerate(observed):
            assert p==expected(n,k,r),(n,k,r)
        count+=1;vertices+=n;round_total+=len(observed)
print('DIRECT_REFINEMENT_OK parameter_pairs=%d vertices=%d checked_round_partitions=%d'%(count,vertices,round_total))
