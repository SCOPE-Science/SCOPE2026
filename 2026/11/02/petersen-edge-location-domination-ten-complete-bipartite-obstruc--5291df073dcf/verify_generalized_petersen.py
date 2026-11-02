#!/usr/bin/env python3
"""Independent generalized-Petersen-model certificate for edge location-domination.

This implementation uses incidence lists, immutable frozensets, and direct pairwise
comparison of configurations, rather than bitsets or a Kneser graph construction.
"""
from itertools import combinations
from collections import Counter, deque

V=list(range(10))
E=sorted({tuple(sorted(pair)) for pair in
    ([(i,(i+1)%5) for i in range(5)]
     +[(5+i,5+(i+2)%5) for i in range(5)]
     +[(i,5+i) for i in range(5)])})
assert len(E)==15
N={f:frozenset(g for g in E if f!=g and not set(f).isdisjoint(g)) for f in E}

def is_location_dominating(S):
    uncovered=set(E)-S
    signatures=[N[f]&S for f in uncovered]
    return all(signatures) and len(set(signatures))==len(signatures)

for k in range(5):
    assert not any(is_location_dominating(frozenset(c)) for c in combinations(E,k))
sol=[frozenset(c) for c in combinations(E,5)
     if is_location_dominating(frozenset(c))]
assert len(sol)==246
A=[set() for x in sol]
for i in range(len(sol)):
    for j in range(i+1,len(sol)):
        if len(sol[i]^sol[j])==2:
            A[i].add(j);A[j].add(i)
assert Counter(map(len,A))=={11:120,12:60,13:60,20:6}
assert sum(map(len,A))==2940

# Explicit isomorphism from GP(5,2) to KG(5,2), checked edge by edge.
pairs=list(combinations(range(5),2))
phi=[0,7,3,4,9,8,6,5,2,1]
KGe={frozenset((a,b)) for a in range(10) for b in range(a+1,10)
     if set(pairs[a]).isdisjoint(pairs[b])}
assert {frozenset((phi[a],phi[b])) for a,b in E}==KGe

# Independent exhaustive breadth-first distances and exceptional-pair graph.
bins=Counter();exception=[];distprofiles=Counter()
for start in range(len(sol)):
    dst={start:0}; q=deque([start])
    while q:
        x=q.popleft()
        for y in A[x]:
            if y not in dst:
                dst[y]=dst[x]+1;q.append(y)
    assert len(dst)==len(sol)
    distprofiles[(len(A[start]),tuple(Counter(dst.values()).get(k,0) for k in range(6)))]+=1
    for j in range(start+1,len(sol)):
        baseline=5-len(sol[start]&sol[j]);gap=dst[j]-baseline
        assert gap in (0,1)
        bins[(gap,dst[j])]+=1
        if gap:exception.append((start,j))
assert sum(v for (gap,_),v in bins.items() if gap)==90
assert Counter({k:sum(n for (gap,d),n in bins.items() if d==k)
                for k in range(1,6)})=={1:1470,2:5100,3:9300,4:9945,5:4320}
assert distprofiles=={
 (11,(1,11,45,73,80,36)):120,
 (12,(1,12,36,81,84,32)):60,
 (13,(1,13,40,76,81,35)):60,
 (20,(1,20,40,70,65,50)):6}

# Defect vertices in the original cubic graph are defined directly by incidence.
def defect(C):
    degree=Counter(a for f in C for a in f)
    if len(degree)==10:return None
    assert sorted(degree.values())==[1]*8+[2]
    return next(a for a in degree if degree[a]==2)

defects=[defect(C) for C in sol]
assert Counter(defects)=={None:6,0:24,1:24,2:24,3:24,4:24,
                          5:24,6:24,7:24,8:24,9:24}
obs=[set() for _ in sol]
for i,j in exception:
    assert defects[i] is not None and defects[i]==defects[j]
    obs[i].add(j);obs[j].add(i)
assert Counter(map(len,obs))=={0:186,3:60}
assert all(bool(obs[i]) == (len(A[i]) == 12) for i in range(len(sol)))
for v in range(10):
    local=[i for i in range(len(sol)) if defects[i]==v and obs[i]]
    assert len(local)==6
    assert all(obs[i] <= set(local) for i in local)
    assert all(len(obs[i])==3 for i in local)
    assert not any(j in obs[i] and k in obs[i] and k in obs[j]
                   for i,j,k in combinations(local,3))
print('GENERALIZED_PETERSEN_DIRECT_PASS')
