#!/usr/bin/env python3
"""Exact standard-library checker for dominating-set exchanges in the five-regular Clebsch graph."""
from collections import Counter, deque
from itertools import combinations, permutations

N = 16
DIRECTIONS = (1, 2, 4, 8, 15)
FULL = (1 << N) - 1
ADJ = [sum(1 << (x ^ d) for d in DIRECTIONS) for x in range(N)]
CLOSED = [ADJ[x] | (1 << x) for x in range(N)]

def selected(mask):
    return [i for i in range(N) if mask & (1 << i)]

def dominates(mask):
    return all(mask & CLOSED[v] for v in range(N))

def swaps(mask):
    sel = selected(mask)
    return {mask ^ (1 << a) ^ (1 << b)
            for a in sel for b in range(N) if not (mask & (1 << b))}

def induced_degrees(mask):
    pts = selected(mask)
    return tuple(sorted((ADJ[v] & mask).bit_count() for v in pts))

# Independent graph construction checks.
assert all(len({v ^ d for d in DIRECTIONS}) == 5 for v in range(N))
assert all((ADJ[v] >> v) & 1 == 0 for v in range(N))
assert all(((ADJ[u] >> v) & 1) == ((ADJ[v] >> u) & 1)
           for u in range(N) for v in range(N))
assert all((ADJ[u] & ADJ[v]).bit_count() == (0 if (ADJ[u] >> v) & 1 else 2)
           for u in range(N) for v in range(u + 1, N))

sets = {k: [sum(1 << v for v in c) for c in combinations(range(N), k)
            if dominates(sum(1 << v for v in c))] for k in range(6)}
assert all(not sets[k] for k in range(4))
assert len(sets[4]) == 80
assert Counter(induced_degrees(s) for s in sets[4]) == {
    (0, 0, 0, 0): 40, (2, 2, 2, 2): 40}
M4 = set(sets[4]);M5 = set(sets[5])
assert all(not (swaps(s) & M4) for s in M4)
assert len(M5) == 1056
assert Counter(induced_degrees(s) for s in M5) == {
    (0, 0, 0, 0, 0): 16,
    (1, 1, 1, 1, 4): 80,
    (0, 0, 0, 1, 1): 320,
    (0, 1, 1, 1, 3): 160,
    (1, 2, 2, 2, 3): 480}
print('OPTIMUM_OK gamma=4 four_sets=80 independent=40 C4=40 frozen=80')
print('FIVE_TYPES_OK', sorted(Counter(induced_degrees(s) for s in M5).items()))

S = sorted(M5)
ids = {x: i for i, x in enumerate(S)}
links = [sorted(ids[t] for t in swaps(s) & M5) for s in S]
assert all(i in links[j] for i, ns in enumerate(links) for j in ns)
assert Counter(map(len, links)) == {19: 960, 25: 96}
assert sum(map(len, links)) // 2 == 10320
print('EXCHANGE_OK vertices=1056 edges=10320 degrees={19:960,25:96}')

distance_profiles = Counter()
for root, ns in enumerate(links):
    distances = [-1] * len(S)
    distances[root] = 0
    q = deque([root])
    while q:
        x = q.popleft()
        for y in links[x]:
            if distances[y] < 0:
                distances[y] = distances[x] + 1
                q.append(y)
    assert min(distances) == 0 and max(distances) == 5
    profile = tuple(Counter(distances)[d] for d in range(6))
    expected = ((1, 19, 94, 316, 507, 119)
                if len(ns) == 19 else (1, 25, 130, 250, 570, 80))
    assert profile == expected
    distance_profiles[(len(ns), profile)] += 1
assert distance_profiles == {
    (19, (1, 19, 94, 316, 507, 119)): 960,
    (25, (1, 25, 130, 250, 570, 80)): 96}
print('METRIC_OK connected=1 radius=5 diameter=5', sorted(distance_profiles.items()))

# The five generators have one relation: their XOR is zero. Any permutation
# therefore gives an invertible linear map, and all 16 translations act too.
linear_maps = []
for perm in permutations(DIRECTIONS):
    table = []
    for v in range(N):
        image = 0
        for bit in range(4):
            if (v >> bit) & 1:
                image ^= perm[bit]
        table.append(image)
    assert set(table) == set(range(N))
    assert all((table[v] ^ table[v ^ d]) in DIRECTIONS
               for v in range(N) for d in DIRECTIONS)
    linear_maps.append(table)
assert len(set(map(tuple, linear_maps))) == 120

def orbit(s):
    p = selected(s)
    return {sum(1 << (lm[v] ^ translate) for v in p)
            for lm in linear_maps for translate in range(N)}

def classify(family):
    unseen = set(family)
    out = []
    while unseen:
        rep = min(unseen)
        orb = orbit(rep)
        assert orb <= set(family) and orb <= unseen
        unseen -= orb
        out.append((len(orb), induced_degrees(rep), len(links[ids[rep]]) if rep in ids else 0))
    return sorted(out)

assert classify(M4) == [(40, (0, 0, 0, 0), 0), (40, (2, 2, 2, 2), 0)]
assert classify(M5) == sorted([
    (16, (0, 0, 0, 0, 0), 25),
    (80, (1, 1, 1, 1, 4), 25),
    (160, (0, 1, 1, 1, 3), 19),
    (320, (0, 0, 0, 1, 1), 19),
    (480, (1, 2, 2, 2, 3), 19)])
print('AUTOMORPHISM_ORBITS_OK group_size=1920 min_orbits=[40,40] five_orbits=[16,80,160,320,480]')
print('ALL_VERIFY_OK')
