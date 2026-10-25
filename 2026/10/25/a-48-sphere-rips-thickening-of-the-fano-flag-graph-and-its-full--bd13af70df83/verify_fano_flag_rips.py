#!/usr/bin/env python3
"""Exact finite verification of the Fano-flag radius-two Rips complex.

Run: python verify_fano_flag_rips.py
Requires Python 3.9 or later; no third-party dependencies.
The accompanying fano_matching_certificate.json gives an explicit acyclic matching.
"""
from collections import Counter, deque
from itertools import combinations, permutations
import json
from math import lcm
from pathlib import Path

LINES = tuple(frozenset(((i) % 7, (i + 1) % 7, (i + 3) % 7)) for i in range(7))
assert len(set(LINES)) == 7
assert all(sum({p, q} <= line for line in LINES) == 1
           for p, q in combinations(range(7), 2))
FLAGS = tuple((p, j) for j, line in enumerate(LINES) for p in sorted(line))
FLAG_INDEX = {flag: i for i, flag in enumerate(FLAGS)}
assert len(FLAGS) == len(FLAG_INDEX) == 21

# The vertices of the line graph of the point-line incidence graph are flags.
# Its edges join flags at a common point or a common line.
NEIGH = [set() for _ in FLAGS]
for i, (p, line) in enumerate(FLAGS):
    for j, (q, other) in enumerate(FLAGS):
        if i != j and (p == q or line == other):
            NEIGH[i].add(j)
assert all(len(nb) == 4 for nb in NEIGH)
assert sum(map(len, NEIGH)) // 2 == 42

# Compute the graph square by actual distance-two paths, independently check
# that the Fano-plane cross-incidence description gives the same adjacency.
SQUARE = [set(nb) for nb in NEIGH]
for i, nb in enumerate(NEIGH):
    for j in nb:
        SQUARE[i].update(NEIGH[j])
    SQUARE[i].discard(i)
for i, (p, line) in enumerate(FLAGS):
    for j, (q, other) in enumerate(FLAGS):
        if i != j:
            predicted = p in LINES[other] or q in LINES[line]
            assert (j in SQUARE[i]) == predicted
assert sum(map(len, SQUARE)) // 2 == 126

# Enumerate every nonempty clique by extending only with larger vertices.
FACES_BY_SIZE = {1: {(i,) for i in range(21)}}
for size in range(2, 22):
    nxt = set()
    for face in FACES_BY_SIZE[size - 1]:
        for i in range(face[-1] + 1, 21):
            if all(i in SQUARE[j] for j in face):
                nxt.add(face + (i,))
    if not nxt:
        break
    FACES_BY_SIZE[size] = nxt
FACES = set().union(*FACES_BY_SIZE.values())
FVECTOR = tuple(len(FACES_BY_SIZE.get(i, set())) for i in range(1, 6))
assert FVECTOR == (21, 126, 238, 105, 21), FVECTOR
assert len(FACES) == 511
MAXIMAL = [f for f in FACES if not any(
            tuple(sorted(f + (v,))) in FACES for v in range(21) if v not in f)]
assert Counter(map(len, MAXIMAL)) == {3: 56, 5: 21}, Counter(map(len, MAXIMAL))

# Independently compute all boundary ranks over the field of two elements.
def binary_rank(columns):
    pivots = {}
    for column in columns:
        while column:
            row = column.bit_length() - 1
            if row in pivots:
                column ^= pivots[row]
            else:
                pivots[row] = column
                break
    return len(pivots)

boundary_ranks = []
for k in range(2, 6):
    rows = sorted(FACES_BY_SIZE[k-1])
    row_index = {face: j for j, face in enumerate(rows)}
    columns = [sum(1 << row_index[face] for face in combinations(simplex, k-1))
               for simplex in sorted(FACES_BY_SIZE[k])]
    boundary_ranks.append(binary_rank(columns))
assert boundary_ranks == [20, 106, 84, 21], boundary_ranks

# Check an explicit Forman matching on the complete face poset.
cert_path = Path(__file__).with_name('fano_matching_certificate.json')
cert = json.loads(cert_path.read_text(encoding='utf-8'))
assert cert['schema_version'] == 1
pairs = [(tuple(a), tuple(b)) for a, b in cert['face_pairs']]
assert len(pairs) == 231
seen = set()
for low, high in pairs:
    assert low in FACES and high in FACES
    assert len(high) == len(low) + 1 and set(low) < set(high)
    assert low not in seen and high not in seen
    seen.update((low, high))
crit2 = {tuple(t) for t in cert['critical_two_faces']}
crit0 = (cert['critical_vertex'],)
assert len(crit2) == 48 and all(len(t) == 3 for t in crit2)
assert FACES - seen == (crit2 | {crit0})

# Orient every unmatched face-poset covering downward, every matched cover
# upward, and verify that the resulting directed graph is acyclic.
up = {lo: hi for lo, hi in pairs}
vertices = sorted(FACES, key=lambda f: (len(f), f))
indeg = {f: 0 for f in FACES}
out = {f: [] for f in FACES}
for big in FACES:
    for low in combinations(big, len(big) - 1):
        if low in FACES:
            if up.get(low) == big:
                src, dst = low, big
            else:
                src, dst = big, low
            out[src].append(dst)
            indeg[dst] += 1
queue = deque(v for v in vertices if indeg[v] == 0)
processed = 0
while queue:
    u = queue.popleft()
    processed += 1
    for v in out[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            queue.append(v)
assert processed == len(FACES) == 511, (processed, len(FACES))
print('FANO_FLAGS_AND_LINE_GRAPH 21 42')
print('SQUARED_LINE_GRAPH_EDGES 126')
print('RIPS_FACE_VECTOR', *FVECTOR)
print('FACETS_SIZE3_SIZE5 56 21')
print('BINARY_BOUNDARY_RANKS', *boundary_ranks)
print('MORSE_MATCHED_PAIRS 231 CRITICAL_VECTOR 1 0 48')
print('COMPLETE_HASSE_DAG_ACYCLIC', processed)
print('INTEGRAL_HOMOTOPY_WEDGE_48_S2')

# Independently enumerate the color-preserving Fano-plane automorphisms.
LINE_LOOKUP = {line: j for j, line in enumerate(LINES)}
preserving = []
for pi in permutations(range(7)):
    images = [frozenset(pi[p] for p in line) for line in LINES]
    if all(img in LINE_LOOKUP for img in images):
        ell = tuple(LINE_LOOKUP[img] for img in images)
        preserving.append(tuple(FLAG_INDEX[(pi[p], ell[l])] for p, l in FLAGS))
assert len(set(preserving)) == 168

# A point-line duality of the Fano incidence relation: find a bijection
# lambda from points to lines making incidence self-adjoint.
polarity = None
for la in permutations(range(7)):
    if all((p in LINES[la[q]]) == (q in LINES[la[p]])
           for p in range(7) for q in range(7)):
        polarity = la
        break
assert polarity is not None
inverse = tuple(polarity.index(j) for j in range(7))
dual = tuple(FLAG_INDEX[(inverse[l], polarity[p])] for p, l in FLAGS)
assert len(set(dual)) == 21

aut_data = []
allperm = set()

def order_of(perm):
    visited = set()
    order = 1
    for i in range(21):
        if i not in visited:
            j = i
            length = 0
            while j not in visited:
                visited.add(j)
                j = perm[j]
                length += 1
            order = lcm(order, length)
    return order

def permutation_sign(values):
    return -1 if sum(values[i] > values[j]
            for i in range(len(values)) for j in range(i + 1, len(values))) % 2 else 1

for perm in preserving:
    for swap in (0, 1):
        g = tuple(dual[perm[i]] for i in range(21)) if swap else perm
        assert g not in allperm
        assert all({g[j] for j in NEIGH[i]} == NEIGH[g[i]]
                   for i in range(21))
        assert all({g[j] for j in SQUARE[i]} == SQUARE[g[i]]
                   for i in range(21))
        allperm.add(g)
        alternating_trace = 0
        for k, faces in FACES_BY_SIZE.items():
            fixed_signed = sum(permutation_sign([g[i] for i in face])
                 for face in faces if set(g[i] for i in face) == set(face))
            alternating_trace += (-1)**(k-1) * fixed_signed
        trace_h2 = alternating_trace - 1
        aut_data.append((order_of(g), swap, trace_h2))
assert len(allperm) == 336
counts = Counter(aut_data)
expected = {
  (1, 0, 48): 1,
  (2, 0, 0): 21,
  (2, 1, -4): 28,
  (3, 0, 3): 56,
  (4, 0, 0): 42,
  (6, 1, -1): 56,
  (7, 0, -1): 48,
  (8, 1, 0): 84,
}
assert counts == expected, (counts, expected)
assert sum(n*trace for (order,swap,trace),n in counts.items()) == 0
assert sum(n*trace for (order,swap,trace),n in counts.items() if not swap) == 168
for key, count in sorted(counts.items()):
    print('AUTOMORPHISM_ORDER_BIPARTITION_SWAP_TRACE_COUNT', *key, count)
print('COLOR_PRESERVING_FIXED_SUBSPACE_DIMENSION 1')
print('FULL_AUTOMORPHISM_FIXED_SUBSPACE_DIMENSION 0')
print('VERIFY_OK_FANO_FLAG_RIPS2_48_SPHERES_FULL_CHARACTER')
