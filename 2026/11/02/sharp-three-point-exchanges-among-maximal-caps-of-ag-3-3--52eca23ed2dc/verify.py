#!/usr/bin/env python3
"""Exact, dependency-free check of the three-swap graph on nine-caps in F_3^3."""
from collections import Counter, deque
from itertools import combinations

N = 27
DIGITS = tuple(tuple((v // (3 ** k)) % 3 for k in range(3)) for v in range(N))
THIRD = [[None] * N for _ in range(N)]
for a in range(N):
    for b in range(N):
        if a == b:
            continue
        THIRD[a][b] = sum((-(DIGITS[a][k] + DIGITS[b][k])) % 3 * (3 ** k) for k in range(3))

caps = []
size_ten = 0

def enumerate_caps(chosen, start, forbidden, mask):
    global size_ten
    if len(chosen) == 9:
        caps.append(mask)
    if len(chosen) == 10:
        size_ten += 1
        return
    if 10 - len(chosen) > N - start:
        # Still collect nine-caps when they are possible.
        if 9 - len(chosen) > N - start:
            return
    for x in range(start, N):
        if (forbidden >> x) & 1:
            continue
        next_forbidden = forbidden
        for y in chosen:
            next_forbidden |= 1 << THIRD[x][y]
        chosen.append(x)
        enumerate_caps(chosen, x + 1, next_forbidden, mask | (1 << x))
        chosen.pop()

enumerate_caps([], 0, 0, 0)
assert size_ten == 0, size_ten
assert len(caps) == 2106 and len(set(caps)) == 2106, len(caps)
caps.sort()
intersection_rows = Counter()
adj = [[] for _ in caps]
edge_count = 0
for i, a in enumerate(caps):
    for j in range(i + 1, len(caps)):
        k = (a & caps[j]).bit_count()
        intersection_rows[k] += 1
        if k == 6:
            adj[i].append(j)
            adj[j].append(i)
            edge_count += 1
assert intersection_rows == {0:2106,1:161109,2:682344,3:631800,4:549666,5:113724,6:75816},intersection_rows
assert edge_count == 75816
assert all(len(ns) == 72 for ns in adj)

expected_profile = {(0,9):1,(1,6):72,(2,3):576,(2,4):522,(2,5):108,
                    (3,1):153,(3,2):648,(3,3):24,(4,0):2}
for root in range(len(caps)):
    distance = [-1] * len(caps)
    distance[root] = 0
    Q = deque([root])
    while Q:
        v = Q.popleft()
        for w in adj[v]:
            if distance[w] == -1:
                distance[w] = distance[v] + 1
                Q.append(w)
    spectrum = Counter((distance[j], (caps[root] & caps[j]).bit_count()) for j in range(len(caps)))
    assert spectrum == expected_profile, (root,spectrum)
    if root == 0:
        print('ROOT_PROFILE',sorted(spectrum.items()))
print('CAPS_OK maximum_cardinality=9 count=2106')
print('INTERSECTION_OK pairs=',sum(intersection_rows.values()),'spectrum=',sorted(intersection_rows.items()))
print('SWAP_OK minimum_positive_size=3 degree=72 edges=75816 connected=1 diameter=4')
print('ANTIPODES_OK two_disjoint_caps_per_vertex')
print('ALL_VERIFY_OK')
