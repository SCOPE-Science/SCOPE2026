#!/usr/bin/env python3
"""Reproduce the finite topology and symmetry assertions for the cube's 3-non-matching complex.
Only Python's standard library is required. All 2^12 edge subsets and all 48 cube
coordinate symmetries are checked, not sampled.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from hashlib import sha256
import json

E = tuple((v, v ^ (1 << j)) for v in range(8) for j in range(3)
          if v < (v ^ (1 << j)))
assert len(E) == 12 and len(set(map(frozenset, E))) == 12
edge_index = {frozenset(e): i for i, e in enumerate(E)}
forbidden = tuple(sum(1 << i for i in ix) for ix in combinations(range(12), 3)
                  if len(set(v for i in ix for v in E[i])) == 6)
faces = {a for a in range(1 << 12)
         if all(a & b != b for b in forbidden)}
f_vector = dict(sorted(Counter(a.bit_count() - 1 for a in faces).items()))
assert len(forbidden) == 44
assert len(faces) == 601
assert f_vector == {-1: 1, 0: 12, 1: 66, 2: 176, 3: 222, 4: 108, 5: 16}

# An explicit Hasse matching. At each stage, pair all still-available
# faces differing by the specified vertex (edge) coordinate.
order = (2, 10, 11, 5, 0, 4, 9, 6, 7, 3, 8, 1)
unpaired = set(faces)
pairs = []
for j in order:
    for a in sorted(unpaired):
        b = a | (1 << j)
        if not (a & (1 << j)) and b in unpaired:
            pairs.append((a, b))
            unpaired.remove(a)
            unpaired.remove(b)
assert len(pairs) == 296
assert len(unpaired) == 9
assert all(a.bit_count() == 4 for a in unpaired)
assert (0, 1 << order[0]) in pairs
# Drop the empty-face pair. Then there is exactly one critical 0-cell
# and nine critical 3-cells, so we apply ordinary (not reduced) Morse theory.
pairs.remove((0, 1 << order[0]))
critical = set(unpaired) | {0, 1 << order[0]}
assert Counter(a.bit_count() - 1 for a in critical) == {-1: 1, 0: 1, 3: 9}

# Verify acyclicity for the actual ordinary-face matching, excluding the
# empty face. Orient unmatched Hasse arcs upward, matched arcs downward.
matched = set(pairs)
nonempty = faces - {0}
indegree = {a: 0 for a in nonempty}
adjacency = {a: [] for a in nonempty}
for b in nonempty:
    for j in range(12):
        if b & (1 << j):
            a = b & ~(1 << j)
            if a:
                assert a in faces
                tail, head = (b, a) if (a, b) in matched else (a, b)
                adjacency[tail].append(head)
                indegree[head] += 1
q = deque(a for a in nonempty if indegree[a] == 0)
visited = 0
while q:
    a = q.popleft()
    visited += 1
    for b in adjacency[a]:
        indegree[b] -= 1
        if indegree[b] == 0:
            q.append(b)
assert visited == len(nonempty), 'a directed gradient cycle exists'

# An independent chain-level rank check over F2.
levels = [[a for a in sorted(faces) if a.bit_count() == k] for k in range(1, 7)]
ranks = []
for k in range(1, 6):
    row_index = {a: i for i, a in enumerate(levels[k - 1])}
    pivots = {}
    for mask in levels[k]:
        vec = 0
        for j in range(12):
            if mask & (1 << j):
                vec ^= 1 << row_index[mask & ~(1 << j)]
        while vec:
            high = vec.bit_length() - 1
            if high in pivots:
                vec ^= pivots[high]
            else:
                pivots[high] = vec
                break
    ranks.append(len(pivots))
assert ranks == [11, 55, 121, 92, 16]

# All affine automorphisms x_j -> x_{sigma(j)} XOR b_j of the 3-cube.
def parity(items):
    return -1 if sum(items[i] > items[j]
                     for i in range(len(items))
                     for j in range(i + 1, len(items))) % 2 else 1

def permutation_trace(sigma, b):
    def vertex(v):
        return sum(((v >> sigma[j]) & 1) << j for j in range(3)) ^ b
    ep = [edge_index[frozenset((vertex(u), vertex(v)))] for u, v in E]
    assert set(ep) == set(range(12))
    # Since homology is only in degree 3, chi_H3 = -reduced Lefschetz,
    # and -L_red = sum_{stable edge sets F} (-1)^|F| * sign(g|_F).
    char = 0
    for a in faces:
        xs = [i for i in range(12) if a & (1 << i)]
        ys = [ep[i] for i in xs]
        if set(xs) == set(ys):
            char += (-1) ** len(xs) * parity(ys)
    return char

def module_trace(sigma, b):
    # P is the three-dimensional permutation module on coordinate directions;
    # U is the signed coordinate module. H = P + sgn(sigma)*(U + wedge^2 U).
    fix = sum(sigma[j] == j for j in range(3))
    tr_u = sum((-1) ** ((b >> j) & 1) for j in range(3) if sigma[j] == j)
    tr_wedge = 0
    for j, k in combinations(range(3), 2):
        if {sigma[j], sigma[k]} == {j, k}:
            orientation = 1 if sigma[j] == j else -1
            tr_wedge += orientation * (-1) ** (((b >> j) & 1) + ((b >> k) & 1))
    return fix + parity(sigma) * (tr_u + tr_wedge)

histogram = Counter()
for sigma in permutations(range(3)):
    for b in range(8):
        observed = permutation_trace(sigma, b)
        predicted = module_trace(sigma, b)
        assert observed == predicted, (sigma, b, observed, predicted)
        histogram[observed] += 1
assert sum(histogram.values()) == 48
assert module_trace((0, 1, 2), 0) == 9
result = {
    'graph_edges': E,
    'minimal_nonfaces': len(forbidden),
    'augmented_faces': len(faces),
    'augmented_f_vector': f_vector,
    'matching_pairs': len(pairs),
    'critical_zero_cells': 1,
    'critical_three_cells': 9,
    'critical_three_cell_masks': sorted(unpaired),
    'hasse_acyclic_checked': visited,
    'mod2_boundary_ranks_for_dimensions_1_through_5': ranks,
    'automorphisms_checked': 48,
    'character_histogram': dict(sorted(histogram.items()))
}
print(json.dumps(result, sort_keys=True, separators=(',', ':')))
