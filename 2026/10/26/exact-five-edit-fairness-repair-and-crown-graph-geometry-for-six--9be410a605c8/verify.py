#!/usr/bin/env python3
"""Exact finite verification of the six-voter fair tie-resolution theorem.
No third-party packages are required.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial

N = 6
FULL = (1 << N) - 1
TRIPLES = [sum(1 << i for i in I) for I in combinations(range(N), 3)]
PAIRS = sorted({min(s, s ^ FULL) for s in TRIPLES})
assert len(PAIRS) == 10


def winning_triples(z):
    return frozenset(s if z & (1 << j) else FULL ^ s
                     for j, s in enumerate(PAIRS))


def value(s, t):
    return int(s.bit_count() > 3 or
               (s.bit_count() == 3 and s in t))


def degrees(t):
    return tuple(sum(bool(s & (1 << i)) for s in t) for i in range(N))


FAIR = {}
for z in range(1 << 10):
    t = winning_triples(z)
    assert len(t) == 10
    assert sum(s.bit_count() for s in t) == 30
    assert all((s in t) != ((s ^ FULL) in t) for s in TRIPLES)
    d = degrees(t)
    if d == (5,) * N:
        FAIR[z] = t

EXPECTED = (220, 234, 316, 358, 425, 453, 570, 598, 665, 707, 789, 803)
assert tuple(sorted(FAIR)) == EXPECTED
assert len(FAIR) == 12

# Optimal repair distances for all 1024 deterministic neutral tie resolutions.
repair_distance = {z: min((z ^ good).bit_count() for good in FAIR)
                   for z in range(1 << 10)}
repair_counts = Counter(repair_distance.values())
assert repair_counts == Counter({0: 12, 1: 120, 2: 360,
                                 3: 380, 4: 140, 5: 12})
assert sum(repair_counts.values()) == 1024
assert max(repair_distance.values()) == 5
# The twelve hardest cases are exactly the six voter-specific
# tie dictatorships and the six corresponding tie anti-dictatorships.
extreme = set()
for i in range(N):
    dictator = sum(1 << j for j, s in enumerate(PAIRS) if s & (1 << i))
    extreme.update((dictator, dictator ^ ((1 << 10) - 1)))
assert len(extreme) == 12
assert extreme == {z for z, d in repair_distance.items() if d == 5}

# Derive both influence indices directly from their defining swing sums.
for z, t in FAIR.items():
    assert all(value(s, t) + value(FULL ^ s, t) == 1 for s in range(1 << N))
    for s in range(1 << N):
        for i in range(N):
            if not s & (1 << i):
                assert value(s, t) <= value(s | (1 << i), t)
    banzhaf_numerators = []
    shapley_numerators = []
    for i in range(N):
        swings = [s for s in range(1 << N) if not (s & (1 << i))
                  and value(s, t) == 0 and value(s | (1 << i), t) == 1]
        banzhaf_numerators.append(len(swings))  # denominator 2**5
        shapley_numerators.append(sum(factorial(s.bit_count()) *
                                       factorial(N-1-s.bit_count())
                                       for s in swings))  # denominator 6!
    assert banzhaf_numerators == [10] * N
    assert shapley_numerators == [120] * N
    assert all(sum(bool((1 << i) & s and (1 << j) & s) for s in t) == 2
               for i, j in combinations(range(N), 2))

spectrum = Counter((x ^ y).bit_count() for x, y in combinations(FAIR, 2))
assert spectrum == Counter({4: 30, 6: 30, 10: 6}), spectrum
adj = {z: {w for w in FAIR if w != z and (z ^ w).bit_count() == 4}
       for z in FAIR}
assert all(len(a) == 5 for a in adj.values())
assert all(z ^ 1023 in FAIR for z in FAIR)
# A crown graph: A and B each have six vertices; every cross-edge except antipodes.
A = {220, 358, 425, 570, 707, 789}
B = set(FAIR) - A
assert len(A) == len(B) == 6
for z in FAIR:
    assert adj[z] == ((B if z in A else A) - {1023 ^ z})

# A 720-element relabeling group acts transitively on 12 solutions, stabilizer 60.
rep = FAIR[220]
orbit = set()
for perm in permutations(range(N)):
    image = frozenset(sum(1 << perm[i] for i in range(N) if s & (1 << i))
                      for s in rep)
    assert image in FAIR.values()
    image_z = next(z for z, t in FAIR.items() if t == image)
    orbit.add(image_z)
assert set(FAIR) == orbit
print('PASS: all 1024 extensions, exact repair histogram 12/120/360/380/140/12')
print('PASS: sharp repair radius 5, attained only by 12 voter-specific tie dictators/anti-dictators')
print('PASS: 1024 neutral majority extensions exhausted')
print('PASS: 12 power-fair balanced selections, Banzhaf=10/32, Shapley=120/720')
print('PASS: each of 12 selections is a 2-(6,3,2) design')
print('PASS: pairwise Hamming distance multiplicities 4:30, 6:30, 10:6')
print('PASS: distance-four adjacency is K_(6,6) minus a perfect matching')
print('PASS: one S6 orbit, 60 permutations stabilizing each fair selection')
