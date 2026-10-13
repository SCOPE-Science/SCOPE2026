#!/usr/bin/env python3
"""Exhaustive, standard-library verification for Heawood global perfect-matching forcing.

Run: python3 verify.py
Edges (p,l) use nonzero 3-bit F_2 vectors, p dot l = 0.
All finite loops are exhaustive, with no external package or dataset dependency.
"""
from collections import Counter
from itertools import combinations
from math import comb

U = tuple(range(1, 8))
def dot(a, b):
    return ((a & b).bit_count() & 1)
EDGES = tuple((p, l) for p in U for l in U if not dot(p, l))
IDX = {e: i for i, e in enumerate(EDGES)}
assert len(EDGES) == 21 and len(IDX) == 21
assert all(sum(x == p for x, _ in EDGES) == 3 for p in U)
assert all(sum(y == l for _, y in EDGES) == 3 for l in U)

# The recurrence explores each of seven point assignments and every incident line.
perfect = []
def backtrack(p, taken, mask):
    if p == 8:
        perfect.append(mask)
        return
    for l in U:
        if (p, l) in IDX and not taken & (1 << l):
            backtrack(p + 1, taken | (1 << l), mask | (1 << IDX[p, l]))
backtrack(1, 0, 0)
assert len(perfect) == len(set(perfect)) == 24
assert all(m.bit_count() == 7 for m in perfect)

# Independent Ryser inclusion-exclusion for the bipartite permanent.
ryser = 0
for s in range(1 << 7):
    r = 1
    for p in U:
        r *= sum(1 for j, l in enumerate(U) if (s & (1 << j)) and (p, l) in IDX)
    ryser += (-1 if (7 - s.bit_count()) & 1 else 1) * r
assert ryser == 24

# Nonempty difference sets characterize separation of every pair of matchings.
diff = tuple(sorted({a ^ b for a, b in combinations(perfect, 2)}))
assert len(diff) == 178
assert Counter(x.bit_count() for x in diff) == {6: 28, 10: 84, 12: 42, 14: 24}
hexagons = tuple(d for d in diff if d.bit_count() == 6)
decagons = tuple(d for d in diff if d.bit_count() == 10)
assert len(hexagons) == 28 and len(decagons) == 84

# Enumerate the entire six- and seven-edge layers of the 21-element edge set.
# A subset is globally forcing iff it hits each symmetric difference.
hex6 = []
force7 = []
for k in (6, 7):
    ct = 0
    for indices in combinations(range(21), k):
        b = sum(1 << i for i in indices)
        if k == 6:
            if all(b & d for d in hexagons):
                hex6.append(b)
        elif all(b & d for d in diff):
            force7.append(b)
        ct += 1
    assert ct == comb(21, k)
assert len(hex6) == 812
assert len(force7) == 8064
# Each six-edge set already hitting every short 6-cycle nonetheless fails some 10-cycle.
assert all(any(not (b & d) for d in decagons) for b in hex6)
assert all(not all(b & d for d in diff) for b in hex6)
assert all(len({(m & b) for m in perfect}) == 24 for b in force7)
assert 8795 in force7  # One explicit witness in this canonical edge labeling.

# Enumerate the 168 invertible linear maps of F_2^3 via image bases.
valid_bases = tuple((a, b, c) for a in U for b in U for c in U
                    if len({a, b, c, a ^ b, b ^ c, a ^ c, a ^ b ^ c}) == 7)
assert len(valid_bases) == 168
edge_perms = []
for a, b, c in valid_bases:
    def A(x):
        return (a if x & 1 else 0) ^ (b if x & 2 else 0) ^ (c if x & 4 else 0)
    pmap = {p: A(p) for p in U}
    # Contragradient dual action ensures incidence is preserved.
    lmap = {l: next(v for v in U
                    if all(dot(p, l) == dot(pmap[p], v) for p in U)) for l in U}
    for swap in (False, True):
        im = tuple(IDX[(lmap[l], pmap[p])] if swap else IDX[(pmap[p], lmap[l])]
                   for p, l in EDGES)
        assert set(im) == set(range(21))
        edge_perms.append(im)
edge_perms = tuple(edge_perms)
assert len(edge_perms) == len(set(edge_perms)) == 336

def image(mask, g):
    out = 0
    while mask:
        least = mask & (-mask)
        out |= 1 << g[least.bit_length() - 1]
        mask -= least
    return out

# Every incidence automorphism preserves the complete matching family.
pmset = set(perfect)
assert all({image(m, g) for m in perfect} == pmset for g in edge_perms)

# Orbit classification of *all* minimum forcing sets.
remaining = set(force7)
orbits = []
while remaining:
    m = min(remaining)
    orbit = {image(m, g) for g in edge_perms}
    assert orbit <= remaining
    remaining.difference_update(orbit)
    orbits.append((m, len(orbit)))
assert len(orbits) == 30
assert Counter(n for _, n in orbits) == {168: 12, 336: 18}
assert sum(n for _, n in orbits) == len(force7)

# Independently confirm the five orbits on the short-cycle six-edge transversals.
remaining = set(hex6)
hexorbits = []
while remaining:
    m = min(remaining)
    orbit = {image(m, g) for g in edge_perms}
    assert orbit <= remaining
    remaining.difference_update(orbit)
    hexorbits.append((m, len(orbit), min(sum(not (m & d) for d in decagons) for m in orbit)))
assert Counter(n for _, n, _ in hexorbits) == {56: 1, 84: 1, 168: 2, 336: 1}
assert all(k >= 1 for _, _, k in hexorbits)

# Check a second exact implementation directly via perfect-matching signatures
# across both boundary layers (not only for reported candidate solutions).
for k in (6, 7):
    hits = 0
    for indices in combinations(range(21), k):
        m = sum(1 << i for i in indices)
        if len({m & p for p in perfect}) == len(perfect):
            hits += 1
    assert hits == (0 if k == 6 else 8064)

print('VERIFY_OK H_vertices=14 H_edges=21 matchings=24 ryser_permanent=24')
print('VERIFY_OK matching_pair_differences=178 sizes=6:28,10:84,12:42,14:24')
print('VERIFY_OK six_edge_subsets=54264 hexagon_hitters=812 all_obstructed_by_decagons=YES')
print('VERIFY_OK seven_edge_subsets=116280 globally_forcing=8064 minimum_global_forcing=7')
print('VERIFY_OK group=336 seven_orbits=30 sizes=168x12+336x18 six_hex_orbits=5')
print('FORCING_ORBITS mask,size (30 lines)')
for m, n in sorted(orbits, key=lambda x: (x[1], x[0])):
    print(m, n)
print('HEX_HITTING_ORBITS mask,size,min_decagon_obstructions (5 lines)')
for rec in sorted(hexorbits, key=lambda x: (x[1], x[0])):
    print(*rec)
