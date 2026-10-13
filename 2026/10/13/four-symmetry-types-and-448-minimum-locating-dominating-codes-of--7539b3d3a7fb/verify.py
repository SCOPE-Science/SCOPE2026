#!/usr/bin/env python3
"""Exact enumeration of locating-dominating codes of the Heawood graph.

Point p and line ell indexed 0..6 are incident precisely when
popcount((p+1) & (ell+1)) is even. Only the Python standard library is used.
"""
from itertools import combinations, product
from collections import Counter

V = tuple(range(14))
P = set(range(7))

def incident(p, ell):
    return ((p + 1) & (ell + 1)).bit_count() % 2 == 0

N = [set() for _ in V]
for p in range(7):
    for ell in range(7):
        if incident(p, ell):
            N[p].add(7 + ell)
            N[7 + ell].add(p)
assert all(len(s) == 3 for s in N)
assert all(len(N[p] & N[q]) == 1 for p in range(7) for q in range(p+1, 7))
assert all(len(N[7+p] & N[7+q]) == 1 for p in range(7) for q in range(p+1, 7))

# Set-valued signature calculation, independent of bitmask arithmetic.
def valid_set(s):
    sig = [frozenset(N[v] & s) for v in V if v not in s]
    return all(sig) and len(set(sig)) == len(sig)

codes = set()
for k in range(7):
    good = {frozenset(s) for s in combinations(V, k) if valid_set(set(s))}
    assert not good if k < 6 else len(good) == 448
    if k == 6:
        codes = good
assert len(codes) == 448

# Separate bitmask enumeration over all 2^14 subsets.
bits = [sum(1 << u for u in N[v]) for v in V]
bit_codes = set()
for mask in range(1 << 14):
    if mask.bit_count() != 6:
        continue
    signatures = []
    for v in V:
        if mask & (1 << v):
            continue
        signature = mask & bits[v]
        if not signature:
            break
        signatures.append(signature)
    else:
        if len(set(signatures)) == len(signatures):
            bit_codes.add(frozenset(v for v in V if mask & (1 << v)))
assert codes == bit_codes

# Verify the canonical Fano-plane incidence classification.
canonical = {
    (0, 1): [(0,1,2,6), (0,2,5,6), (1,2,4,6), (2,4,5,6)],
    (0, 1, 2): [(0,1,2), (0,5,6), (1,4,6), (2,4,5)],
    (0, 1, 3): [(0,2,6), (0,4,6), (1,2,6), (1,5,6), (2,4,6),
                (2,5,6), (3,4,6), (3,5,6), (4,5,6)],
}
for pts, expected in canonical.items():
    actual = {tuple(sorted(v-7 for v in code if v >= 7))
              for code in codes if tuple(sorted(code & P)) == pts}
    assert actual == set(expected), (pts, actual)

# Construct all 168 invertible binary 3x3 linear maps directly.
gl = []
for a, b, c in product(range(1, 8), repeat=3):
    if len({0, a, b, c, a^b, a^c, b^c, a^b^c}) != 8:
        continue
    point_image = [((a if x & 1 else 0) ^ (b if x & 2 else 0) ^
                    (c if x & 4 else 0)) - 1 for x in range(1, 8)]
    line_image = []
    for ell in range(7):
        image_pts = {point_image[p] for p in range(7) if incident(p,ell)}
        candidates = [i for i in range(7)
                      if {p for p in range(7) if incident(p,i)} == image_pts]
        assert len(candidates) == 1
        line_image.append(7 + candidates[0])
    gl.append(tuple(point_image + line_image))
assert len(set(gl)) == 168
swap = tuple([v + 7 if v < 7 else v - 7 for v in V])
automorphisms = set(gl) | {tuple(swap[perm[v]] for v in V) for perm in gl}
assert len(automorphisms) == 336
for perm in automorphisms:
    assert all((u in N[v]) == (perm[u] in N[perm[v]]) for v in V for u in V)

# Orbit-by-orbit certification of all six-vertex codes.
unclassified = set(codes)
observed = []
while unclassified:
    rep = next(iter(unclassified))
    orbit = {frozenset(perm[v] for v in rep) for perm in automorphisms}
    assert orbit <= codes
    unclassified -= orbit
    observed.append((len(orbit), Counter(len(code & P) for code in orbit),
                     Counter(sum(v in code for u in code for v in N[u])//2
                             for code in orbit)))
assert sorted(size for size, *_ in observed) == [28, 84, 168, 168]
assert Counter(len(code & P) for code in codes) == {2:84, 3:280, 4:84}
assert Counter(sum(v in code for u in code for v in N[u])//2 for code in codes) == {2:252, 3:196}

# Four orbit types: (selected point/line split, internal-edge count, orbit size).
classified = []
for size, splits, edges in observed:
    classified.append((tuple(sorted(splits.items())), tuple(sorted(edges.items())), size))
assert sorted(classified) == sorted([
    (((2,84),(4,84)),((2,168),),168),
    (((3,168),),((3,168),),168),
    (((3,84),),((2,84),),84),
    (((3,28),),((3,28),),28),
])
print('VERIFY_OK full_subsets=16384 size_six_candidates=3003 optimum_codes=448 '
      'part_counts=84+280+84 GL3=168 automorphisms=336 orbit_sizes=28,84,168,168 '
      'canonical_incidence_tables=4,4,9 independent_enumerations=agree')
