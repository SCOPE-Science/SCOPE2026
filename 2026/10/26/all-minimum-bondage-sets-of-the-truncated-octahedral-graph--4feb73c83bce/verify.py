#!/usr/bin/env python3
"""Exact finite certificate for minimum bondage sets of the 4-permutahedron.

Run with Python 3: python verify.py
Only Python's standard library is required.
"""
from itertools import combinations, permutations
from collections import Counter

P = list(permutations(range(4)))
position = {p: i for i, p in enumerate(P)}
E = []
for i, p in enumerate(P):
    for t in range(3):
        q = list(p)
        q[t], q[t + 1] = q[t + 1], q[t]
        j = position[tuple(q)]
        if i < j:
            E.append((i, j))
assert len(P) == 24 and len(E) == 36

adj = [0] * 24
for u, v in E:
    adj[u] |= 1 << v
    adj[v] |= 1 << u
FULL = (1 << 24) - 1
D = []
for k in (6, 7, 8):
    count = 0
    for S in combinations(range(24), k):
        dominated = 0
        for u in S:
            dominated |= adj[u] | (1 << u)
        if dominated == FULL:
            count += 1
            if k == 8:
                D.append(sum(1 << u for u in S))
    assert (count == 0) if k < 8 else (count == 1767), (k, count)

incident = [[] for _ in range(24)]
for i, (u, v) in enumerate(E):
    incident[u].append((i, v))
    incident[v].append((i, u))

# For each original minimum dominating set S and outside vertex v,
# E(S,v) is exactly the incident edge set joining v to S.
# Deleting all E(S,v) makes S fail to dominate v.
killed = {}
for si, S in enumerate(D):
    for v in range(24):
        if S >> v & 1:
            continue
        witness = 0
        for ei, u in incident[v]:
            if S >> u & 1:
                witness |= 1 << ei
        assert 1 <= witness.bit_count() <= 3
        killed[witness] = killed.get(witness, 0) | (1 << si)
all_sets = (1 << len(D)) - 1

W = []
for F in combinations(range(36), 5):
    casualties = 0
    for r in (1, 2, 3):
        for piece in combinations(F, r):
            key = sum(1 << e for e in piece)
            casualties |= killed.get(key, 0)
    if casualties == all_sets:
        W.append(F)
assert len(W) == 276
assert sum(sum(1 << e for e in F) for F in W) % (1 << 64) == 2634785709493
x = 0
for F in W:
    x ^= sum(1 << e for e in F)
assert x == 68719476735

stars = [{i for i, (u, w) in enumerate(E) if v == u or v == w} for v in range(24)]
star_profile = Counter(sum(st.issubset(set(F)) for st in stars) for F in W)
assert star_profile == {1: 240, 2: 36}
assert sum(stars[0].issubset(set(F)) for F in W) == 13

# Explicit 48 graph automorphisms: any permutation of the four labels,
# followed optionally by reversal of their coordinate positions.
edge_index = {e: i for i, e in enumerate(E)}
actions = []
for pi in permutations(range(4)):
    for reverse in (False, True):
        vm = [position[tuple(pi[x] for x in (p[::-1] if reverse else p))] for p in P]
        em = tuple(edge_index[tuple(sorted((vm[u], vm[v])))] for u, v in E)
        actions.append(em)
assert len(set(actions)) == 48
remaining = set(W)
orbits = []
while remaining:
    representative = min(remaining)
    orbit = {tuple(sorted(a[e] for e in representative)) for a in actions}
    assert orbit <= remaining
    remaining -= orbit
    orbits.append((representative, len(orbit)))
expected = [
    ((0, 1, 2, 3, 4), 24),
    ((0, 1, 2, 3, 14), 48),
    ((0, 1, 2, 5, 6), 12),
    ((0, 1, 2, 5, 9), 48),
    ((0, 1, 2, 7, 8), 48),
    ((0, 1, 2, 8, 22), 24),
    ((0, 1, 2, 9, 10), 48),
    ((0, 1, 2, 9, 16), 24),
]
assert sorted(orbits) == sorted(expected)
print('VERIFY_OK')
print('minimum dominating sets:', len(D))
print('five-edge bondage sets:', len(W))
print('full vertex-star multiplicity:', dict(star_profile))
print('symmetry orbit representatives and sizes:', sorted(orbits))
