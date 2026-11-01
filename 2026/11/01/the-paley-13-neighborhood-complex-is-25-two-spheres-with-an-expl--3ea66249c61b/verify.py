#!/usr/bin/env python3
"""Standalone finite certificate checker for the Paley-13 neighborhood complex.
Uses only Python's standard library. Run: python3 verify.py
"""
import collections
import itertools
import json
from pathlib import Path

P = 13
Q = {pow(t, 2, P) for t in range(1, P)}
assert Q == {1, 3, 4, 9, 10, 12}
N = [frozenset((v + r) % P for r in Q) for v in range(P)]
F = {frozenset(s) for hood in N for k in range(1, len(hood) + 1)
     for s in itertools.combinations(sorted(hood), k)}
counts = lambda X: {str(k): v for k, v in sorted(collections.Counter(map(len, X)).items())}
assert counts(F) == {'1': 13, '2': 78, '3': 221, '4': 195, '5': 78, '6': 13}
C = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
assert C['initial_face_counts'] == counts(F)

# An elementary free-face collapse must have exactly one coface of
# the next cardinality. This implies absence of higher cofaces.
for i, (small, large) in enumerate(C['collapses']):
    a, b = frozenset(small), frozenset(large)
    assert a in F and b in F, ('missing collapse face', i)
    assert len(b) == len(a) + 1 and a < b, ('wrong codimension', i)
    cofaces = [c for c in F if len(c) == len(b) and a < c]
    assert cofaces == [b], ('not a free pair', i)
    F.remove(a)
    F.remove(b)
assert len(C['collapses']) == 227
assert counts(F) == {'1': 13, '2': 59, '3': 72}
assert C['reduced_face_counts'] == counts(F)

vertices = {next(iter(s)) for s in F if len(s) == 1}
edges = {frozenset(s) for s in F if len(s) == 2}
triangles = {frozenset(s) for s in F if len(s) == 3}
assert vertices == set(range(P))
assert len(edges) == 59 and len(triangles) == 72

# Check the proposed tree really is a connected, acyclic spanning tree.
parent = {v: v for v in vertices}
def root(v):
    while v != parent[v]:
        v = parent[v]
    return v
T = set()
for k, pair in enumerate(C['spanning_tree']):
    e = frozenset(pair)
    assert e in edges and e not in T, ('tree edge missing/repeated', k)
    x, y = tuple(e)
    rx, ry = root(x), root(y)
    assert rx != ry, ('tree cycle', k)
    parent[rx] = ry
    T.add(e)
assert len(T) == 12 and len({root(v) for v in vertices}) == 1

# Every triangular relation contains exactly one not-yet-trivial
# generator and therefore kills it by a valid presentation elimination.
active = edges - T
for k, entry in enumerate(C['edge_eliminations']):
    t, e = frozenset(entry['triangle']), frozenset(entry['edge'])
    assert t in triangles and e <= t and len(e) == 2
    boundary = {t - {v} for v in t}
    assert boundary & active == {e}, ('not a unit-generator relation', k)
    active.remove(e)
assert len(C['edge_eliminations']) == 47 and not active

# Exact cellular Euler characteristic of the 2-dimensional remainder.
assert 13 - 59 + 72 == 26
assert (13 - 59 + 72) - 1 == 25

# Direct signed simplicial Lefschetz count, independent of the collapses.
# H^0=Q, H^2 has dimension 25, and all other rational homology vanishes.
original = {tuple(sorted(s)) for hood in N
            for k in range(1, len(hood) + 1)
            for s in itertools.combinations(sorted(hood), k)}
def sign(v):
    return (-1) ** sum(v[i] > v[j] for i in range(len(v))
                       for j in range(i + 1, len(v)))
def homology_trace(a, b):
    alternating = 0
    for s in original:
        image = [(a * x + b) % P for x in s]
        if tuple(sorted(image)) == s:
            alternating += (-1) ** (len(s) - 1) * sign(image)
    return alternating - 1
for a in Q:
    for b in range(P):
        measured = homology_trace(a, b)
        expected = 25 if (a, b) == (1, 0) else (-1 if a == 1 else 1)
        assert measured == expected, (a, b, measured, expected)
        perm_fixed = sum((a * x + b) % P == x for x in range(P))
        expected_decomposition = perm_fixed + (perm_fixed - 1)
        assert expected_decomposition == measured

print('INITIAL_FACE_COUNTS 13,78,221,195,78,13')
print('ELEMENTARY_COLLAPSES 227 VERIFIED')
print('REMAINING_FACE_COUNTS 13,59,72')
print('SPANNING_TREE 12 EDGES VERIFIED')
print('TRIANGULAR_RELATION_ELIMINATIONS 47 VERIFIED')
print('PI_1 TRIVIAL; CHI 26; H_2 INTEGRAL RANK 25')
print('AFFINE_CHARACTER 78 ELEMENTS VERIFIED')
print('CHARACTER_CLASSES identity=25 translations=-1 other_affine=1')
print('VERIFY_OK')
