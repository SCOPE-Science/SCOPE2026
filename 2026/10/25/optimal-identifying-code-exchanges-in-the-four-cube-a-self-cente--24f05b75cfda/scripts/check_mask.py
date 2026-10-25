#!/usr/bin/env python3
"""Exhaustive bit-mask certificate for minimum identifying-code exchanges in Q4.

Run with Python 3.10 or later: python scripts/check_mask.py
Every 16-bit mask is inspected; no solver or external data are used.
"""
from collections import Counter, deque
from itertools import permutations
import json

DIM = 4
VERTICES = 1 << DIM
BALLS = [sum(1 << y for y in range(VERTICES)
             if (x ^ y).bit_count() <= 1) for x in range(VERTICES)]


def identifies(mask):
    signatures = [mask & ball for ball in BALLS]
    return 0 not in signatures and len(set(signatures)) == VERTICES


# Normalization boundary: distinguishability without the required coverage.
weak_six = sum(1 for mask in range(1 << VERTICES)
               if mask.bit_count() == 6
               and len({mask & ball for ball in BALLS}) == VERTICES)
assert weak_six == 192
all_masks = [mask for mask in range(1 << VERTICES) if identifies(mask)]
minimum = min(mask.bit_count() for mask in all_masks)
codes = sorted(mask for mask in all_masks if mask.bit_count() == minimum)
assert minimum == 7
assert len(codes) == 960
assert all(not identifies(mask) for mask in range(1 << VERTICES)
           if mask.bit_count() < minimum)
index = {code: i for i, code in enumerate(codes)}
neighbor_sets = []
for code in codes:
    neighbors = set()
    for old in range(VERTICES):
        if code & (1 << old):
            for new in range(VERTICES):
                if not (code & (1 << new)):
                    candidate = code ^ (1 << old) ^ (1 << new)
                    if candidate in index:
                        neighbors.add(index[candidate])
    neighbor_sets.append(neighbors)
assert all(len(N) == 9 for N in neighbor_sets)
edge_count = sum(map(len, neighbor_sets)) // 2
assert edge_count == 4320
triangles_at_vertex = [sum(len(neighbor_sets[i] & neighbor_sets[j])
                           for j in neighbor_sets[i]) // 2
                       for i in range(len(codes))]
assert set(triangles_at_vertex) == {12}
assert sum(triangles_at_vertex) // 3 == 3840


def apply_isometry(code, coordinate_permutation, shift):
    result = 0
    for x in range(VERTICES):
        if code & (1 << x):
            y = sum(((x >> coordinate_permutation[j]) & 1) << j
                    for j in range(DIM)) ^ shift
            result |= 1 << y
    return result


def distances(start):
    d = {start: 0}
    todo = deque([start])
    while todo:
        a = todo.popleft()
        for b in neighbor_sets[a]:
            if b not in d:
                d[b] = d[a] + 1
                todo.append(b)
    assert len(d) == len(codes)
    return [Counter(d.values())[k] for k in range(max(d.values()) + 1)]

unassigned = set(codes)
orbits = []
perms = list(permutations(range(DIM)))
while unassigned:
    rep = min(unassigned)
    orbit = {apply_isometry(rep, perm, shift)
             for perm in perms for shift in range(VERTICES)}
    assert orbit <= set(codes)
    unassigned -= orbit
    orbits.append((rep, len(orbit), distances(index[rep])))
assert sorted(size for _, size, _ in orbits) == [192, 384, 384]
assert {tuple(shells) for _, _, shells in orbits} == {
    (1, 9, 35, 132, 300, 338, 130, 15)}

result = dict(dimension=DIM, minimum_size=minimum, optimal_codes=len(codes),
              weak_separating_six_sets=weak_six,
              exchanges=edge_count, degree=9,
              triangles=3840, local_triangles=12,
              natural_isometry_group_order=len(perms) * VERTICES,
              natural_orbits=[dict(representative=[x for x in range(VERTICES)
                                    if rep & (1 << x)], size=size,
                                   distance_shells=shells)
                              for rep, size, shells in orbits],
              radius=7, diameter=7)
print(json.dumps(result, sort_keys=True, indent=2))
