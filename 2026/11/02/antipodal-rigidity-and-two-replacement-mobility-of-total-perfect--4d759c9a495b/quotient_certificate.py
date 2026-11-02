"""Algebraic antipodal-quotient verification for total perfect codes on Q_4.

Standard library only. Run with: python quotient_certificate.py
"""
from collections import Counter
from itertools import combinations

U = 15
rep = lambda v: min(v, v ^ U)
vertices = sorted({rep(v) for v in range(16)})
assert len(vertices) == 8
qedges = {tuple(sorted((rep(v), rep(v ^ (1 << j)))))
          for v in range(16) for j in range(4)}
assert len(qedges) == 16
parity = lambda v: v.bit_count() % 2
assert len([v for v in vertices if parity(v) == 0]) == 4
assert len([v for v in vertices if parity(v) == 1]) == 4
assert all(parity(a) != parity(b) for a, b in qedges)
assert all(tuple(sorted((a, b))) in qedges
           for a in vertices for b in vertices if parity(a) != parity(b))

# A quotient edge recovers exactly two antipodal pairs in Q_4.
codes = {edge: frozenset([a, a ^ U, b, b ^ U]) for edge in qedges for a, b in [edge]}
assert len(codes) == 16 and len(set(codes.values())) == 16
assert all(len(c) == 4 for c in codes.values())

def neighboring(v):
    return {v ^ (1 << j) for j in range(4)}

assert all(all(sum(w in c for w in neighboring(v)) == 1 for v in range(16))
           for c in codes.values())

# The line-graph equivalence is checked as a full adjacency-matrix identity.
for e, f in combinations(qedges, 2):
    overlap = len(codes[e] & codes[f])
    assert overlap == (2 if set(e) & set(f) else 0)
    assert (len(codes[e] - codes[f]) == 2) == bool(set(e) & set(f))

# A new direction (one of four unit basis vectors) and a coset of its
# four-element affine plane enumerate all 16 codes without duplicates.
by_planes = set()
for j in range(4):
    direction = 1 << j
    for x in range(16):
        by_planes.add(frozenset([x, x ^ direction, x ^ U, x ^ U ^ direction]))
assert len(by_planes) == 16
assert by_planes == set(codes.values())

# For disjoint quotient edges (a,b) and (c,d), the two cross edges
# are the only common neighbors in the line graph.
counts = Counter()
for e, f in combinations(qedges, 2):
    if set(e) & set(f):
        counts['adjacent'] += 1
    else:
        counts['distance_two'] += 1
        common = sum(bool(set(e) & set(h)) and bool(set(f) & set(h)) for h in qedges)
        assert common == 2
assert counts == {'adjacent': 48, 'distance_two': 72}
matchings = [quad for quad in combinations(qedges, 4)
             if len(set().union(*(set(e) for e in quad))) == 8]
assert len(matchings) == 24
assert all(sum(e in matching for matching in matchings) == 6 for e in qedges)
print('ANTIPODAL_QUOTIENT_K44_PASS', len(vertices), len(qedges), counts)
