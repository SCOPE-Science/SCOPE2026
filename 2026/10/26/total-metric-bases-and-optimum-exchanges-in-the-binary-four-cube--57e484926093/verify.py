#!/usr/bin/env python3
"""Exact total-metric-basis census and exchange graph for the binary four-cube.

Run: python3 verify.py
Uses only the Python standard library. Vertex labels are four-bit integers.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from math import comb

N = 16
D = [[(u ^ v).bit_count() for v in range(N)] for u in range(N)]
PAIRS = [(u,v) for u in range(N) for v in range(u+1,N)]
assert len(PAIRS) == 120

# For each unordered pair, compute the mask of admissible third-party landmarks.
REQUIREMENTS = [
    (u,v,sum(1 << w for w in range(N)
             if w != u and w != v and D[w][u] != D[w][v]))
    for u,v in PAIRS
]
assert Counter(D[u][v] for u,v in PAIRS) == {1:32,2:48,3:32,4:8}

def third_party_valid_direct(s):
    """Independent predicate: explicitly test each pair and each landmark."""
    a = [w for w in range(N) if s & (1 << w)]
    return all(any(w not in (u,v) and D[w][u] != D[w][v] for w in a)
               for u,v in PAIRS)

def predicate_masks(s):
    """Fast exact hitting-set predicate using precomputed admissible masks."""
    return all(s & req for _,_,req in REQUIREMENTS)

optima = set()
count_by_size = []
for k in range(7):
    success = 0
    for c in combinations(range(N),k):
        s = sum(1 << w for w in c)
        good = predicate_masks(s)
        if good:
            success += 1
            if k == 6: optima.add(s)
    count_by_size.append(success)
assert count_by_size == [0,0,0,0,0,0,1600], count_by_size
assert len(optima) == 1600
for s in optima:
    assert third_party_valid_direct(s)
print('OPTIMUM_OK dim_t=6 minima=1600 exhaustive_size_counts='+repr(count_by_size))

# A complementary certificate: distance-two pairs alone have 1608 six-point
# hitting sets. Exactly eight fail a pair at distance four.
r2 = [mask for u,v,mask in REQUIREMENTS if D[u][v] == 2]
r4 = [mask for u,v,mask in REQUIREMENTS if D[u][v] == 4]
shortlist = []
for c in combinations(range(N),6):
    s = sum(1<<x for x in c)
    if all(s & x for x in r2): shortlist.append(s)
extra = set(shortlist) - optima
assert len(shortlist) == 1608 and len(extra) == 8
assert all(not all(s & x for x in r4) for s in extra)
print('DISTANCE_TWO_FILTER_OK 1608 six-sets, eight excluded by antipodal pairs')

# Group of hypercube symmetries: four coordinate permutations and translations.
maps = []
for p in permutations(range(4)):
    for translation in range(N):
        image = []
        for x in range(N):
            y = translation
            for i,j in enumerate(p):
                if x & (1 << i): y ^= (1 << j)
            image.append(y)
        maps.append(image)
assert len(maps) == 384

def transform(s, image):
    return sum(1 << image[x] for x in range(N) if s & (1 << x))

unseen = set(optima)
orbit_sizes = []
while unseen:
    base = min(unseen)
    orb = {transform(base,m) for m in maps}
    assert orb <= optima
    orbit_sizes.append(len(orb))
    unseen -= orb
assert sorted(orbit_sizes) == sorted([32,32,96,96]+[192]*7), orbit_sizes
print('SYMMETRY_OK orbits='+repr(sorted(orbit_sizes)))

# Exchange graph: exactly one deleted and one inserted landmark.
indexed = sorted(optima)
idx = {s:i for i,s in enumerate(indexed)}
adj = [[] for _ in indexed]
for s,i in idx.items():
    ns = []
    for u in range(N):
        if s & (1<<u):
            for v in range(N):
                if not (s & (1<<v)):
                    t = s ^ (1<<u) ^ (1<<v)
                    if t in idx:ns.append(idx[t])
    assert len(ns) == len(set(ns))
    adj[i] = ns
assert all(i in adj[j] for i,a in enumerate(adj) for j in a)
deg = Counter(len(a) for a in adj)
assert deg == Counter({12:384,22:576,26:576,30:64}),deg
edges = sum(map(len,adj))//2
assert edges == 17088
seen = {0}
q = deque([0])
while q:
    for j in adj[q.popleft()]:
        if j not in seen:seen.add(j);q.append(j)
assert len(seen) == 1600
print('EXCHANGE_OK connected=1600 vertices=1600 edges=17088 degrees='+repr(sorted(deg.items())))
print('ALL_VERIFY_OK')
