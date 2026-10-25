#!/usr/bin/env python3
"""Exact finite checks for the Kummer-biplane mod-two first-homology support theorem.

Requires Python 3.9+; no external packages or network access.
"""
from collections import Counter
from itertools import combinations, permutations

V = tuple(range(16))

def f(x):
    assert 0 <= x < 4
    return int(x != 0)

def q(x):
    return f(x & 3) ^ f(x >> 2)

def b(x, y):
    return q(x ^ y) ^ q(x) ^ q(y)

D = frozenset(x for x in V if q(x))
blocks = frozenset(frozenset(x ^ d for d in D) for x in V)
assert len(D) == 6 and len(blocks) == 16
assert all(len(s & t) == 2 for s, t in combinations(blocks, 2))
assert all(sum(x in s and y in s for s in blocks) == 2 for x, y in combinations(V, 2))
assert all(any(b(x, y) for y in V) for x in range(1, 16))

edges = tuple(combinations(V, 2))
edge_index = {e: i for i, e in enumerate(edges)}
all_triples = tuple(combinations(V, 3))
facial = frozenset(t for t in all_triples if any(set(t) <= s for s in blocks))
missing = frozenset(t for t in all_triples if t not in facial)
assert (len(edges), len(facial), len(missing)) == (120, 320, 240)
for t in all_triples:
    x, y, z = t
    assert (t in facial) == (b(x ^ y, x ^ z) == 1)
    # The edge cochain alpha([x,y]) = 1 + q(x+y) over F2.
    pairing = (1 ^ q(x ^ y)) ^ (1 ^ q(x ^ z)) ^ (1 ^ q(y ^ z))
    assert pairing == int(t in missing)

# Exact rank of the second boundary over F2: columns are triangle boundaries.
pivots = {}
for t in sorted(facial):
    value = 0
    for e in combinations(t, 2):
        value ^= 1 << edge_index[e]
    while value:
        i = value.bit_length()-1
        if i in pivots:
            value ^= pivots[i]
        else:
            pivots[i] = value
            break
assert len(pivots) == 104
# Since every pair is an edge, rank(d1)=15, so dim ker(d1)=120-15.
assert (len(edges) - 15) - len(pivots) == 1

# The omitted triples are exactly triples inside affine totally-isotropic
# four-point planes, with one such plane per omitted triple.
planes = set()
triple_coverage = Counter()
for x, y, z in missing:
    p = frozenset((x, y, z, x ^ y ^ z))
    assert len(p) == 4
    assert all(t in missing for t in combinations(sorted(p), 3))
    planes.add(p)
    triple_coverage[(x, y, z)] += 1
assert len(planes) == 60
assert all(sum(set(t) <= p for p in planes) == 1 for t in missing)

# Exhaust all subsets.  A subset carries nontrivial ambient H1 precisely
# when it contains at least one missing triangle.
noncarriers = Counter()
maximal = []
for k in range(17):
    for subset in combinations(V, k):
        if not any(set(t) <= set(subset) for t in missing):
            noncarriers[k] += 1
            if k == 6:
                maximal.append(frozenset(subset))
assert [noncarriers[k] for k in range(17)] == [1,16,120,320,320,96,16] + [0]*10
assert frozenset(maximal) == blocks

# Independently check affine symplectic transitivity by enumerating all
# invertible binary linear maps preserving b.  Their 16 translations give
# a transitive orbit on the 240 missing triangles.
def mat_map(cols):
    return tuple(
        (cols[0] if i & 1 else 0) ^
        (cols[1] if i & 2 else 0) ^
        (cols[2] if i & 4 else 0) ^
        (cols[3] if i & 8 else 0)
        for i in V)

def rank_vectors(cols):
    piv = {}
    for v in cols:
        while v:
            i = v.bit_length()-1
            if i in piv:
                v ^= piv[i]
            else:
                piv[i] = v
                break
    return len(piv)

symplectic = []
for cols in permutations(range(1, 16), 4):
    if rank_vectors(cols) != 4:
        continue
    if any(b(cols[i],cols[j]) != b(1<<i, 1<<j) for i in range(4) for j in range(i)):
        continue
    symplectic.append(mat_map(cols))
assert len(symplectic) == 720
rep = sorted(missing)[0]
orbit = {
    tuple(sorted(mp[x] ^ shift for x in rep))
    for mp in symplectic for shift in V
}
assert orbit == missing

print('VERIFY_OK_KUMMER_BIPLANE_SHORTEST_H1_CARRIERS')
print('BLOCKS', len(blocks), 'POINTS', len(V), 'EDGES', len(edges))
print('FACE_AND_MISSING_TRIANGLES', len(facial), len(missing))
print('D2_RANK_F2', len(pivots), 'H1_F2_DIM', 1)
print('LAGRANGIAN_AFFINE_PLANES', len(planes))
print('NO_AMBIENT_H1_SUPPORT_PROFILE', tuple(noncarriers[k] for k in range(17)))
print('MAXIMAL_NONCARRIER_SETS', len(maximal), 'ALL_ARE_BLOCKS', True)
print('AFFINE_SYMPLECTIC_GROUP_ORDER', len(symplectic)*16)
print('MISSING_TRIANGLES_SINGLE_AFFINE_ORBIT', len(orbit))
