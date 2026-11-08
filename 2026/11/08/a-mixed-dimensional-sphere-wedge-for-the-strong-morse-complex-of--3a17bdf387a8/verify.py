#!/usr/bin/env python3
"""Exact finite certificate for the full strong-Morse matching complex of a theta graph.
Standard-library Python; run with python3 verify.py. No external data needed.
"""
from collections import Counter, deque
from itertools import permutations

# The length-(2,2,3) theta: the three 0--1 paths are 0-2-1,
# 0-3-1, and 0-4-5-1. The graph is one-dimensional (unfilled cycles).
adjacency = {0: (2, 3, 4), 1: (2, 3, 5), 2: (0, 1),
             3: (0, 1), 4: (0, 5), 5: (1, 4)}
arcs = sorted((v, a) for v, neighbors in adjacency.items() for a in neighbors)
arc_index = {arc: i for i, arc in enumerate(arcs)}
assert len(arcs) == 14

# In a 1-complex a descending link is a cone iff it has one vertex.
# Thus each ordering produces exactly these vertex-edge pairs.
generators = set()
for order in permutations(range(6)):
    pos = {v: i for i, v in enumerate(order)}
    pairs = []
    for v in range(6):
        below = [u for u in adjacency[v] if pos[u] < pos[v]]
        if len(below) == 1:
            pairs.append(arc_index[(v, below[0])])
    generators.add(sum(1 << i for i in pairs))
assert len(generators) == 91
facets = {f for f in generators if not any(f != g and f & g == f for g in generators)}
assert len(facets) == 36
faces = set()
for facet in facets:
    f = facet
    while f:
        faces.add(f)
        f = (f - 1) & facet
f_vector = tuple(sum(f.bit_count() == dim + 1 for f in faces) for dim in range(4))
assert len(faces) == 139 and f_vector == (14, 57, 58, 10)
print('FACE_CENSUS_OK', len(generators), len(facets), f_vector)

# A deterministic acyclic matching on the 139 nonempty faces.
# For each toggled vertex j, greedily match every available f with f union {j}.
coordinate_order = (11, 12, 0, 2, 13, 3, 10, 5, 6, 9, 4, 1, 7, 8)
paired, matching = set(), []
for j in coordinate_order:
    for lower in sorted(faces, key=lambda f: (f.bit_count(), f)):
        if lower in paired or lower & (1 << j):
            continue
        upper = lower | (1 << j)
        if upper in faces and upper not in paired:
            paired.update((lower, upper))
            matching.append((lower, upper))
assert len(matching) == 66 and len(paired) == 132
critical = faces - paired
critical_vector = tuple(sum(f.bit_count() == dim + 1 for f in critical) for dim in range(4))
assert critical_vector == (1, 1, 5, 0)
print('MORSE_PAIRS_OK', len(matching), critical_vector, sorted(critical))

# Every incident cover relation: downward for unmatched, upward for matched.
matched_edges = set(matching)
nexts = {f: [] for f in faces}
indegree = {f: 0 for f in faces}
incidences = 0
for upper in faces:
    for j in range(14):
        if not (upper & (1 << j)):
            continue
        lower = upper ^ (1 << j)
        if lower == 0:
            continue
        assert lower in faces
        source, target = (lower, upper) if (lower, upper) in matched_edges else (upper, lower)
        nexts[source].append(target)
        indegree[target] += 1
        incidences += 1
queue = deque(sorted(f for f in faces if indegree[f] == 0))
topo = []
while queue:
    u = queue.popleft()
    topo.append(u)
    for v in nexts[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert len(topo) == len(faces) == 139
print('DIRECTED_HASSE_ACYCLIC_OK', len(topo), incidences)

# Signed simplex boundaries. Cancel all matched pairs over Z with unit pivots.
# This is the elementary chain cancellation associated to the Morse matching.
boundary = {}
for face in faces:
    bits = [j for j in range(14) if face & (1 << j)]
    boundary[face] = ({face ^ (1 << j): (-1) ** i for i, j in enumerate(bits)}
                      if len(bits) > 1 else {})
for idx, (lower, upper) in enumerate(matching):
    pivot = boundary[upper].get(lower, 0)
    assert abs(pivot) == 1, (idx, lower, upper, pivot)
    for other in list(boundary):
        if other == upper or other.bit_count() != upper.bit_count():
            continue
        multiplier = boundary[other].get(lower, 0) // pivot
        if multiplier:
            for f, c in boundary[upper].items():
                changed = boundary[other].get(f, 0) - multiplier * c
                if changed:
                    boundary[other][f] = changed
                else:
                    boundary[other].pop(f, None)
    for other in list(boundary):
        if other != upper:
            boundary[other].pop(upper, None)
            boundary[other].pop(lower, None)
    del boundary[upper]
    del boundary[lower]
assert set(boundary) == critical
assert all(not b for b in boundary.values())
print('INTEGRAL_MORSE_BOUNDARY_OK', 66, 7, 'all zero')
print('HOMOTOPY_OK', 'S1 wedge five S2', 'ALL_VERIFY_OK')
