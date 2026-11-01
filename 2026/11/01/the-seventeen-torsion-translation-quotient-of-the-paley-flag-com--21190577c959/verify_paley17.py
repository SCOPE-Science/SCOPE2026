#!/usr/bin/env python3
"""Exact finite checks for the Paley-17 clique complex and its affine action.

Requires only Python 3.9+ standard library. All simplices, matchings, group
permutations, and directed Hasse covers are constructed from the definition.
"""
from itertools import combinations
from collections import deque

P = 17
RESIDUES = frozenset((a * a) % P for a in range(1, P))
VERTICES = range(P)

def is_clique(simplex):
    return all(((y - x) % P) in RESIDUES for x, y in combinations(simplex, 2))

# The 4-clique check proves the flag complex is two-dimensional.
assert all(not is_clique(c) for c in combinations(VERTICES, 4))
faces = frozenset(frozenset(c) for k in range(1, 4)
                  for c in combinations(VERTICES, k) if is_clique(c))
assert {k: sum(len(c) == k for c in faces) for k in (1, 2, 3)} == {1: 17, 2: 68, 3: 68}

# Deterministic lexicographic vertex-toggle matching (not necessarily a
# simplicial collapse). Acyclicity is verified independently below.
unmatched = set(faces)
pairs = set()
for vertex in VERTICES:
    for small in tuple(sorted(unmatched, key=lambda c: (len(c), tuple(sorted(c))))):
        if vertex in small or small not in unmatched:
            continue
        large = small | {vertex}
        if large in unmatched:
            assert len(large) == len(small) + 1
            unmatched.remove(small)
            unmatched.remove(large)
            pairs.add((small, large))

assert len(pairs) == 68
assert len(unmatched) == 17
assert sum(len(s) == 1 for s in unmatched) == 1
assert sum(len(s) == 2 for s in unmatched) == 0
assert sum(len(s) == 3 for s in unmatched) == 16
assert frozenset({0}) in unmatched
assert len({s for pair in pairs for s in pair}) == 136
assert not any(s in unmatched for pair in pairs for s in pair)

# In the Hasse diagram, orient each matched cover upwards; all other covers
# downwards. A complete Kahn topological sort checks every gradient cycle.
adj = {s: [] for s in faces}
indeg = {s: 0 for s in faces}
cover_count = 0
for upper in faces:
    if len(upper) == 1:
        continue
    for x in upper:
        lower = upper - {x}
        assert lower in faces
        cover_count += 1
        u, v = (lower, upper) if (lower, upper) in pairs else (upper, lower)
        adj[u].append(v)
        indeg[v] += 1
assert cover_count == 340
queue = deque(s for s in faces if indeg[s] == 0)
processed = 0
while queue:
    s = queue.popleft()
    processed += 1
    for t in adj[s]:
        indeg[t] -= 1
        if indeg[t] == 0:
            queue.append(t)
assert processed == len(faces) == 153

# Direct integral alternating simplex-character calculation. The sign is
# the orientation sign on increasing-vertex simplices, not merely a fixed-
# simplex count. All 136 affine Paley automorphisms are tested.
counts = {1: [], 2: [], 3: []}
for s in faces:
    counts[len(s)].append(tuple(sorted(s)))
assert len(RESIDUES) == 8

def signed_fixed_trace(k, a, b):
    ans = 0
    for simplex in counts[k]:
        image = tuple((a * x + b) % P for x in simplex)
        if tuple(sorted(image)) != simplex:
            continue
        inversions = sum(image[i] > image[j] for i in range(k) for j in range(i+1, k))
        ans += -1 if inversions & 1 else 1
    return ans

classes = {"identity": 0, "nontrivial_translation": 0, "nontranslation": 0}
for a in sorted(RESIDUES):
    for b in VERTICES:
        lhs = sum((-1) ** (k-1) * signed_fixed_trace(k, a, b) for k in (1, 2, 3)) - 1
        rhs = 16 if (a, b) == (1, 0) else (-1 if a == 1 else 0)
        assert lhs == rhs, (a, b, lhs, rhs)
        typ = "identity" if (a, b) == (1, 0) else ("nontrivial_translation" if a == 1 else "nontranslation")
        classes[typ] += 1
assert classes == {"identity": 1, "nontrivial_translation": 16, "nontranslation": 119}

# Independently check the 68 x 68 triangle-boundary rank in three fields.
edges = counts[2]
triangles = counts[3]
boundary = [[0] * len(triangles) for _ in edges]
edge_index = {e: i for i, e in enumerate(edges)}
for j, tri in enumerate(triangles):
    for i in range(3):
        edge = tri[:i] + tri[i+1:]
        boundary[edge_index[edge]][j] += (-1) ** i

def modular_rank(rows, prime):
    matrix = [[x % prime for x in row] for row in rows]
    rank = 0
    nr, nc = len(matrix), len(matrix[0])
    for col in range(nc):
        piv = next((i for i in range(rank, nr) if matrix[i][col]), None)
        if piv is None:
            continue
        matrix[piv], matrix[rank] = matrix[rank], matrix[piv]
        inv = pow(matrix[rank][col], -1, prime)
        matrix[rank][col:] = [(x * inv) % prime for x in matrix[rank][col:]]
        for i in range(rank+1, nr):
            if matrix[i][col]:
                mult = matrix[i][col]
                matrix[i][col:] = [(u - mult * v) % prime for u, v in zip(matrix[i][col:], matrix[rank][col:])]
        rank += 1
    return rank

for prime in (2, 3, 17):
    assert modular_rank(boundary, prime) == 52

print("paley17_vertices=17 edges=68 triangles=68 four_cliques=0")
print("matching_pairs=68 critical_vertices=1 critical_edges=0 critical_triangles=16")
print("hasse_covers=340 directed_vertices=153 directed_acyclic=1")
print("affine_automorphisms=136 character=(16,-1,0) class_counts=(1,16,119)")
print("boundary2_rank_mod_2_3_17=52")
print("VERIFY_OK")
