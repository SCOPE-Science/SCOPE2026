#!/usr/bin/env python3
"""Exact enumeration of optimum strong edge-colourings and their class trades on the Fano incidence graph."""
from collections import Counter, defaultdict
from itertools import combinations, permutations

lines = [frozenset((j + i) % 7 for j in (0, 1, 3)) for i in range(7)]
assert len(set(lines)) == 7
assert all(sum(p in L for L in lines) == 3 for p in range(7))
assert all(len(L & M) == 1 for L, M in combinations(lines, 2))
flags = [(p, j) for p in range(7) for j, line in enumerate(lines) if p in line]
assert len(flags) == 21
index = {flag: k for k, flag in enumerate(flags)}

def compatible(i, j):
    p, a = flags[i]
    q, b = flags[j]
    return p != q and a != b and p not in lines[b] and q not in lines[a]

triples = [sum(1 << i for i in selection)
           for selection in combinations(range(21), 3)
           if all(compatible(i, j) for i, j in combinations(selection, 2))]
assert len(triples) == 84
assert not any(all(compatible(i, j) for i, j in combinations(selection, 2))
               for selection in combinations(range(21), 4))
print('INDEPENDENT_MATCHING_BOUND_OK edges=21 maximum=3 triples=84')

by_edge = [[t for t in triples if t & (1 << e)] for e in range(21)]
full = (1 << 21) - 1
colourings = []
def cover(used, classes):
    if used == full:
        assert len(classes) == 7
        colourings.append(tuple(sorted(classes)))
        return
    least_uncovered = next(e for e in range(21) if not used & (1 << e))
    for t in by_edge[least_uncovered]:
        if not used & t:
            cover(used | t, classes + [t])
cover(0, [])
colourings = sorted(colourings)
assert len(colourings) == len(set(colourings)) == 416
print('OPTIMAL_PARTITIONS_OK 416')

# A two-class change is possible only if six edges admit another split
# into induced triples. There are exceptional six-edge trades, but none
# occurs as a pair of classes in a full optimum coloring.
six_edge_splits = defaultdict(list)
for a, b in combinations(triples, 2):
    if a & b == 0:
        six_edge_splits[a | b].append((a, b))
assert Counter(map(len, six_edge_splits.values())) == {1: 2296, 4: 14}
assert all(len(six_edge_splits[a | b]) == 1
           for C in colourings for a, b in combinations(C, 2))
print('TWO_COLOUR_FROZEN_OK exceptional_six_edge_unions=14')

# The three-class move replaces the partition of the union of exactly
# three color classes. With two-class moves excluded, equivalently
# distinct colorings share exactly four of seven classes.
sets = list(map(frozenset, colourings))
G = [set() for _ in sets]
for i in range(len(sets)):
    for j in range(i):
        if len(sets[i] & sets[j]) == 4:
            G[i].add(j)
            G[j].add(i)
assert sum(map(len, G)) == 3136
assert Counter(map(len, G)) == {5: 112, 8: 280, 14: 24}
profiles = {}
for start in range(len(G)):
    distance = {start: 0}
    queue = [start]
    for x in queue:
        for y in G[x]:
            if y not in distance:
                distance[y] = distance[x] + 1
                queue.append(y)
    assert len(distance) == 416
    assert max(distance.values()) == 6
    profiles[start] = tuple(Counter(distance.values())[d] for d in range(7))
assert len(set(profiles.values())) == 6
print('THREE_COLOUR_CONNECTED_OK edges=1568 radius=6 diameter=6 degrees={5:112,8:280,14:24}')

# The full automorphism group of the Fano incidence graph includes
# point collineations and a point-line duality. Classify optimal colorings.
line_family = set(lines)
point_collineations = [p for p in permutations(range(7))
                       if {frozenset(p[x] for x in line) for line in lines} == line_family]
assert len(point_collineations) == 168
D = [7 + (-p) % 7 for p in range(7)] + [(-j) % 7 for j in range(7)]
permutations14 = []
for p in point_collineations:
    line_map = [next(j for j, M in enumerate(lines) if M == {p[x] for x in L})
                for L in lines]
    M = list(p) + [7 + j for j in line_map]
    permutations14.append(M)
    permutations14.append([D[x] for x in M])
assert len({tuple(M) for M in permutations14}) == 336
by_colouring = {C: k for k, C in enumerate(colourings)}
orbit_members = []
seen = set()
for C in colourings:
    representative = by_colouring[C]
    if representative in seen:
        continue
    orbit = set()
    for M in permutations14:
        edge_map = []
        for p, j in flags:
            a, b = M[p], M[7 + j]
            if a >= 7:
                a, b = b, a
            edge_map.append(index[(a, b - 7)])
        mapped = tuple(sorted(sum(1 << edge_map[i] for i in range(21) if t & (1 << i))
                              for t in C))
        orbit.add(by_colouring[mapped])
    assert not (seen & orbit)
    seen.update(orbit)
    orbit_members.append(orbit)
assert len(seen) == 416
assert sorted(map(len, orbit_members)) == [8, 16, 56, 112, 112, 112]
for orbit in orbit_members:
    assert len({profiles[i] for i in orbit}) == 1
print('AUTOMORPHISM_ORBITS_OK order=336 sizes=8,16,56,112,112,112')
for orbit in sorted(orbit_members, key=lambda o: (len(o), min(o))):
    i = min(orbit)
    print('ORBIT size={} degree={} distance_shells={}'.format(
        len(orbit), len(G[i]), ','.join(map(str, profiles[i]))))
print('FULL_VERIFY_OK')
