#!/usr/bin/env python3
"""Exact integral discrete-Morse verification for a fixed graph complex.

Only Python's standard library is needed. Vertices are numbered 0,...,17.
The face test is: the induced subgraph has maximum degree at most one.
"""
import collections
import random
from functools import lru_cache

EDGES = [(0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),
         (3,4),(3,10),(4,5),(4,15),(5,6),(6,7),(6,11),
         (7,8),(7,14),(8,9),(9,10),(9,16),(10,11),(11,12),
         (12,13),(12,17),(13,14),(14,15),(15,16),(16,17)]
N = 18
NEIGH = [0] * N
for u,v in EDGES:
    NEIGH[u] |= 1 << v
    NEIGH[v] |= 1 << u
assert len(EDGES) == 27 and all(a.bit_count() == 3 for a in NEIGH)

# Dynamic, exhaustive face generation. Every face has its least-bit deletion
# as a face. This test is independent of the Morse differential routine.
valid = bytearray(1 << N)
valid[0] = 1
for mask in range(1,1 << N):
    pivot = mask & -mask
    v = pivot.bit_length()-1
    smaller = mask ^ pivot
    if not valid[smaller]:
        continue
    neighbors = NEIGH[v] & smaller
    valid[mask] = int(not neighbors or
        (neighbors.bit_count() == 1 and
         (NEIGH[neighbors.bit_length()-1] & smaller) == 0))
faces = [mask for mask in range(1,1 << N) if valid[mask]]
fvector = [sum(x.bit_count() == k for x in faces)
           for k in range(1,11)]
assert fvector == [18,153,762,2394,4806,6027,4428,1728,308,27], fvector
facet_counts = collections.Counter(s.bit_count()-1 for s in faces
    if all(not valid[s | (1<<v)] for v in range(N) if not s & (1<<v)))
assert facet_counts == {5:9, 7:333, 8:38, 9:27},facet_counts

# Fixed pivot order, stable across Python versions.
order = [11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12]
assert sorted(order) == list(range(N))
remaining = set(faces)
low_to_high = {}
high_to_low = {}
for v in order:
    bit = 1 << v
    for lo in faces:  # ascending integer mask order is immaterial
        hi = lo | bit
        if not lo & bit and lo in remaining and hi in remaining:
            remaining.remove(lo)
            remaining.remove(hi)
            low_to_high[lo] = hi
            high_to_low[hi] = lo
critical = sorted(remaining,key=lambda s:(s.bit_count(),s))
assert len(low_to_high) == 10319 and len(critical) == 13
assert len(critical) + 2*len(low_to_high) == len(faces)
assert collections.Counter(s.bit_count()-1 for s in critical) == {0:1,5:10,6:2}
assert all(hi.bit_count() == lo.bit_count()+1 for lo,hi in low_to_high.items())

# Complete finite acyclicity proof. Orient every unmatched face-poset cover
# from coface to face, but reverse the matched ones. Kahn topological sort
# must remove every node: this is an exhaustive, not statistical, test.
ids = {s:i for i,s in enumerate(faces)}
indegree = [0]*len(faces)
source_edges = [[] for _ in faces]
covers = 0
for hi in faces:
    j = ids[hi]
    for v in range(N):
        if hi & (1 << v):
            lo = hi ^ (1 << v)
            if lo == 0:
                continue
            covers += 1
            i = ids[lo]
            if low_to_high.get(lo) == hi:
                src,dst = i,j
            else:
                src,dst = j,i
            source_edges[src].append(dst)
            indegree[dst] += 1
queue = collections.deque(i for i,d in enumerate(indegree) if d == 0)
visited = 0
while queue:
    src = queue.popleft()
    visited += 1
    for dst in source_edges[src]:
        indegree[dst] -= 1
        if indegree[dst] == 0:
            queue.append(dst)
assert covers == 120222 and visited == len(faces)

# Integral Morse boundary via elementary signed algebraic cancellations.
# For a face s of dimension five, projection P(s) onto critical dimension-five
# cells is: itself if critical; 0 if upper in a matching; and if lower matched
# to h, solve the unit-coefficient relation boundary(h)=0 for s recursively.
crit_five = [s for s in critical if s.bit_count() == 6]
crit_six = [s for s in critical if s.bit_count() == 7]

@lru_cache(maxsize=None)
def project(s):
    assert s.bit_count() == 6
    if s in remaining:
        return {s: 1}
    if s in high_to_low:
        return {}
    hi = low_to_high[s]
    assert hi.bit_count() == 7
    pivot = (hi ^ s).bit_length()-1
    a = (-1) ** (hi & ((1 << pivot)-1)).bit_count()
    result = collections.defaultdict(int)
    for k,v in enumerate(i for i in range(N) if hi & (1<<i)):
        t = hi ^ (1<<v)
        if t == s:
            continue
        for c,multiplicity in project(t).items():
            result[c] -= a * ((-1)**k) * multiplicity
    return {c:x for c,x in result.items() if x}

rows = []
for hi in crit_six:
    result = collections.defaultdict(int)
    for k,v in enumerate(i for i in range(N) if hi & (1<<i)):
        for c,multiplicity in project(hi ^ (1<<v)).items():
            result[c] += ((-1)**k) * multiplicity
    rows.append([result.get(c,0) for c in crit_five])
assert rows == [[-1,0,0,-1,-1,0,0,0,0,0],
                [1,0,0,1,1,0,0,0,0,0]],rows
# The 10-by-2 differential has rank 1 and a unit entry. The quotient is free
# of rank 9 and its kernel is free of rank 1; the unit pivots cancel one
# six-cell with one five-cell in the resulting high-connected CW complex.
assert any(abs(x) == 1 for row in rows for x in row)
assert rows[1] == [-x for x in rows[0]]
print('vertices=18 edges=27')
print('faces=20651 f_vector=' + str(fvector))
print('facets=407 facets_by_dimension={5: 9, 7: 333, 8: 38, 9: 27}')
print('pairs=10319 critical_by_dimension={0: 1, 5: 10, 6: 2}')
print('cover_relations=120222 visited_in_directed_topological_sort=20651 acyclic=True')
print('critical_dim5_masks=' + str(crit_five))
print('critical_dim6_masks=' + str(crit_six))
print('morse_d6_rows=' + str(rows))
print('integral_elementary_divisors=[1]')
print('reduced_integral_betti={5: 9, 6: 1}')
print('PASS')
