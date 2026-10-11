#!/usr/bin/env python3
from functools import lru_cache
from collections import Counter
from itertools import combinations

FACETS = [
(1,3,7,13),(1,3,9,13),(1,5,7,11),(1,5,9,11),(1,7,11,13),(1,9,11,13),(2,4,8,14),
(2,4,10,14),(2,6,8,12),(2,6,10,12),(2,8,12,14),(2,10,12,14),(3,4,7,11),(3,4,7,12),
(3,6,10,11),(3,6,10,14),(3,7,12,13),(3,7,11,14),(3,9,12,13),(3,10,11,14),(4,5,8,12),
(4,5,8,13),(4,7,11,12),(4,8,11,12),(4,8,13,14),(4,10,13,14),(5,6,9,13),(5,6,9,14),
(5,7,11,14),(5,8,12,13),(5,9,12,13),(5,9,11,14),(6,8,11,12),(6,9,13,14),(6,10,11,12),
(6,10,13,14),(7,11,12,13),(8,12,13,14),(9,11,13,14),(10,11,12,14),(11,12,13,14)
]

def canon(fs):
    ss={frozenset(f) for f in fs}
    return tuple(sorted((f for f in ss if not any(f < g for g in ss)), key=lambda x:(len(x), tuple(sorted(x)))))

def verts(K):
    if not K: return set()
    out=set()
    for f in K: out |= set(f)
    return out

def deletion(K,v):
    return canon([(set(f)-{v}) if v in f else set(f) for f in K])

def link(K,v):
    return canon([set(f)-{v} for f in K if v in f])

@lru_cache(None)
def non_evasive(K):
    # Standard recursive convention: a one-vertex complex is non-evasive.
    # The complex {empty face} is not accepted as a base case.
    V=verts(K)
    if len(V)==1 and len(K)==1 and len(next(iter(K)))==1:
        return True
    if len(V)==0:
        return False
    for v in sorted(V):
        if non_evasive(deletion(K,v)) and non_evasive(link(K,v)):
            return True
    return False

def valid_roots(K):
    return tuple(v for v in sorted(verts(K)) if non_evasive(deletion(K,v)) and non_evasive(link(K,v)))

def all_faces(K):
    faces=set()
    for f in K:
        s=sorted(f)
        for r in range(1,len(s)+1):
            for a in combinations(s,r): faces.add(frozenset(a))
    return faces

R=canon(FACETS)
V=tuple(sorted(verts(R)))
assert V==tuple(range(1,15))
faces=all_faces(R)
fvec=tuple(sum(1 for f in faces if len(f)==r) for r in range(1,5))
assert fvec==(14,66,94,41)
roots=valid_roots(R)
assert roots==V
second={v:valid_roots(deletion(R,v)) for v in V}
second_counts=tuple(len(second[v]) for v in V)
assert second_counts==(11,11,11,11,11,11,9,9,9,9,5,5,5,5)
profile=Counter(second_counts)
assert profile==Counter({11:6,9:4,5:4})
# Directly check the two conditions defining validity for each first move.
for v in V:
    assert non_evasive(deletion(R,v))
    assert non_evasive(link(R,v))
print('VERIFY_OK facets=41 f=14,66,94,41 roots=14/14 second_profile=11x6,9x4,5x4 second_total=%d memo_states=%d' % (sum(second_counts), non_evasive.cache_info().currsize))
