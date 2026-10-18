#!/usr/bin/env python3
"""Exact finite check of the Petersen graphic-matroid forest character.

Requires only the Python standard library. On failure raises AssertionError.
The independent face test and orbit-union test use distinct signed traces.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict

VERTICES = list(combinations(range(5), 2))
VERTEX_INDEX = {v: j for j, v in enumerate(VERTICES)}
EDGES = [(i, j) for i in range(10) for j in range(i + 1, 10)
         if set(VERTICES[i]).isdisjoint(VERTICES[j])]
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
assert len(VERTICES) == 10 and len(EDGES) == 15


def is_forest(mask):
    parent = list(range(10))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for pos, (a, b) in enumerate(EDGES):
        if not (mask >> pos) & 1:
            continue
        a, b = root(a), root(b)
        if a == b:
            return False
        parent[a] = b
    return True


def induced_edge_perm(perm):
    vertex_perm = [VERTEX_INDEX[tuple(sorted((perm[x], perm[y])))]
                   for x, y in VERTICES]
    return tuple(EDGE_INDEX[tuple(sorted((vertex_perm[a], vertex_perm[b])))]
                 for a, b in EDGES)


def cycles(perm):
    found = set()
    result = []
    for i in range(len(perm)):
        if i in found:
            continue
        orbit = []
        j = i
        while j not in found:
            found.add(j)
            orbit.append(j)
            j = perm[j]
        result.append(orbit)
    return result


def representative(parts):
    perm = list(range(5))
    start = 0
    for length in parts:
        for offset in range(length):
            perm[start + offset] = start + (offset + 1) % length
        start += length
    assert start == 5
    return perm


TYPES = {
    (1, 1, 1, 1, 1): [1, 15, 105, 455, 1365, 2991, 4875, 5805, 4680, 2000],
    (2, 1, 1, 1): [1, 9, 36, 80, 99, 63, 16],
    (2, 2, 1): [1, 9, 36, 80, 97, 45],
    (3, 1, 1): [1, 5, 9, 5],
    (3, 2): [1, 2, 1],
    (4, 1): [1, 5, 9, 5],
    (5,): [1, 1],
}

# First method: cycle-union enumeration, every conjugacy type.
for parts, expected in TYPES.items():
    orbit_masks = [sum(1 << j for j in orbit)
                   for orbit in cycles(induced_edge_perm(representative(parts)))]
    count = Counter()
    for subset in range(1 << len(orbit_masks)):
        mask = 0
        for j in range(len(orbit_masks)):
            if (subset >> j) & 1:
                mask |= orbit_masks[j]
        if is_forest(mask):
            count[subset.bit_count()] += 1
    got = [count[j] for j in range(len(orbit_masks) + 1)]
    while got and got[-1] == 0:
        got.pop()
    assert got == expected, (parts, got, expected)
    alt_sum = sum((-1 if k % 2 else 1) * n for k, n in count.items())
    assert -alt_sum == (240 if parts == (1, 1, 1, 1, 1) else 0)

# Second method: enumerate all faces once, calculate orientation signs
# on each invariant simplex, check every group element individually.
forests = [mask for mask in range(1 << len(EDGES)) if is_forest(mask)]
assert len(forests) == 22292
assert Counter(mask.bit_count() for mask in forests) == Counter({
    0: 1, 1: 15, 2: 105, 3: 455, 4: 1365, 5: 2991,
    6: 4875, 7: 5805, 8: 4680, 9: 2000})
for perm in permutations(range(5)):
    edge_perm = induced_edge_perm(perm)
    signed = 0
    for mask in forests:
        indices = [j for j in range(15) if (mask >> j) & 1]
        images = [edge_perm[j] for j in indices]
        if set(indices) != set(images):
            continue
        inversions = sum(images[a] > images[b]
                         for a in range(len(images))
                         for b in range(a + 1, len(images)))
        parity = (len(indices) - 1 + inversions) % 2
        signed += -1 if parity else 1
    assert signed == (240 if perm == tuple(range(5)) else 0), (perm, signed)

print('PASS: all 32768 masks, 22292 forests, seven orbit polynomials,')
print('PASS: all 120 direct signed action traces, exactly two regular characters.')
