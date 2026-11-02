#!/usr/bin/env python3
"""Exhaustive finite verifier for Clebsch edge-metric-basis exchanges.
Only Python's standard library is required. Python 3.10+.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from functools import reduce

N = 16
D = (1, 2, 4, 8, 15)
E = sorted({tuple(sorted((v, v ^ d))) for v in range(N) for d in D})
assert len(E) == 40
NEIGH = [set(x ^ d for d in D) for x in range(N)]
assert all(len(a) == 5 for a in NEIGH)
assert all(len(NEIGH[x] & NEIGH[y]) == (0 if y in NEIGH[x] else 2)
           for x in range(N) for y in range(x+1, N))

# Since every two distinct nonadjacent vertices are at distance two,
# the distance of a vertex to an edge is in {0,1,2}.
def vertex_edge_distance(v, e):
    a,b = e
    return min(0 if v == u else (1 if u in NEIGH[v] else 2)
               for u in (a,b))

SIG = [[vertex_edge_distance(v, e) for e in E] for v in range(N)]
edge_pairs = list(combinations(range(len(E)), 2))
assert len(edge_pairs) == 780
BIT = [sum((1 << j) for j,(a,b) in enumerate(edge_pairs)
           if SIG[v][a] != SIG[v][b]) for v in range(N)]
FULL = (1 << len(edge_pairs)) - 1

# Every one of the 2^16 labelled vertex subsets is checked.
resolved = [0] * (1 << N)
bases = []
min_size = N + 1
for s in range(1, 1 << N):
    low = s & -s
    resolved[s] = resolved[s ^ low] | BIT[low.bit_length()-1]
    k = s.bit_count()
    if resolved[s] == FULL:
        if k < min_size:
            min_size, bases = k, [s]
        elif k == min_size:
            bases.append(s)
assert min_size == 9 and len(bases) == 1600, (min_size, len(bases))
BASE = set(bases)

# Independently reconstruct all basis exchanges via 1->0, 0->1.
ADJ = {s: set() for s in bases}
for s in bases:
    present = [v for v in range(N) if s >> v & 1]
    missing = [v for v in range(N) if not(s >> v & 1)]
    for v in present:
        for w in missing:
            t = s ^ (1 << v) ^ (1 << w)
            if t in BASE:
                ADJ[s].add(t)
assert all(s in ADJ[t] for s in bases for t in ADJ[s])
assert Counter(map(len, ADJ.values())) == {15: 1440, 27: 160}
assert sum(map(len,ADJ.values())) // 2 == 12960

# All-source exact shortest paths, rather than just one sample source.
ecc = Counter()
for root in bases:
    d = {root: 0}
    q = deque([root])
    while q:
        v = q.popleft()
        for w in ADJ[v]:
            if w not in d:
                d[w] = d[v] + 1
                q.append(w)
    assert len(d) == len(bases)
    ecc[max(d.values())] += 1
assert ecc == {6: 160, 7: 1440}, ecc

# The five directions have the unique linear relation that their XOR is zero.
# Thus each permutation extends to an invertible linear map, followed by a translation.
AUT = []
for p in permutations(D):
    for t in range(N):
        a = []
        for x in range(N):
            z = t
            for i in range(4):
                if x & (1 << i):
                    z ^= p[i]
            a.append(z)
        assert len(set(a)) == N
        assert {tuple(sorted((a[x],a[y]))) for x,y in E} == set(E)
        AUT.append(tuple(a))
assert len(AUT) == len(set(AUT)) == 1920

# The 1920 graph automorphisms give four orbit types, each entirely valid.
unseen = set(bases)
orb_rows = []
while unseen:
    s = min(unseen)
    orbit = {sum(1 << a[v] for v in range(N) if s >> v & 1)
             for a in AUT}
    assert orbit <= unseen
    unseen -= orbit
    omitted = [v for v in range(N) if not(s >> v & 1)]
    signature = tuple(sorted(len(NEIGH[v] & set(omitted)) for v in omitted))
    assert all(tuple(sorted(len(NEIGH[v] & {u for u in range(N) if not(t >> u & 1)})
                            for v in range(N) if not(t >> v & 1))) == signature
               for t in orbit)
    orb_rows.append((len(orbit), len(ADJ[s]), signature, s))
assert sorted((n,d) for n,d,_,_ in orb_rows) == [(160,27),(240,15),(240,15),(960,15)]
assert len(set(sig for _,_,sig,_ in orb_rows)) == 4
assert sum(n for n,_,_,_ in orb_rows) == 1600
print('GRAPH_OK vertices=16 edges=40 regular_degree=5 sr_parameters=(16,5,0,2)')
print('EDGE_RESOLVING_OK exhaustive_subsets=65536 minimum_size=9 bases=1600')
print('EXCHANGE_OK components=1 vertices=1600 edges=12960 degree_15=1440 degree_27=160 radius=6 diameter=7')
print('ORBITS_OK automorphisms=1920 orbit_sizes=', sorted(n for n,_,_,_ in orb_rows))
for n,d,sig,rep in sorted(orb_rows):
    print('ORBIT', 'size='+str(n),'exchange_degree='+str(d),'omitted_induced_degrees='+str(sig),'basis_mask='+str(hex(rep)))
print('ALL_VERIFY_OK')
