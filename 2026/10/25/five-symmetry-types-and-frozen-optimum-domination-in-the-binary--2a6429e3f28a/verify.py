#!/usr/bin/env python3
"""Finite proof checks for paired and total domination in the binary five-cube.
Usage: python3 verify.py [--exhaustive]
"""
import sys
from collections import Counter
from itertools import combinations, permutations

D = 5
V = tuple(range(1 << D))
EVEN = tuple(v for v in V if v.bit_count() % 2 == 0)
ODD = tuple(v for v in V if v.bit_count() % 2 == 1)
N = {v: frozenset(w for w in V if (v ^ w).bit_count() == 1) for v in V}


def cover_four(source, target):
    target_set = frozenset(target)
    return frozenset(
        frozenset(c) for c in combinations(source, 4)
        if frozenset().union(*(N[x] for x in c)) == target_set
    )


def affine_cosets(side):
    result = set()
    for i, j in combinations(range(D), 2):
        subspace = (0, (1 << i) ^ (1 << j), 31 ^ (1 << i), 31 ^ (1 << j))
        for u in side:
            result.add(frozenset(u ^ a for a in subspace))
    return frozenset(result)


def paired(S):
    e = tuple(v for v in S if v in even_set)
    o = tuple(v for v in S if v in odd_set)
    if len(e) != 4 or len(o) != 4:
        return False
    return any(all((a ^ b).bit_count() == 1 for a, b in zip(e, p))
               for p in permutations(o))


def orbit(rep):
    a = set()
    for p in permutations(range(D)):
        transformed = tuple(sum(((v >> i) & 1) << p[i] for i in range(D)) for v in V)
        for shift in V:
            a.add(frozenset(transformed[v] ^ shift for v in rep))
    return frozenset(a)


even_set = frozenset(EVEN)
odd_set = frozenset(ODD)
E4 = cover_four(EVEN, ODD)
O4 = cover_four(ODD, EVEN)
assert len(E4) == len(O4) == 40
assert E4 == affine_cosets(EVEN)
assert O4 == affine_cosets(ODD)
print('PARITY_FOUR_SETS_OK 40+40 affine-plane cosets')

TOTAL = frozenset(frozenset(e | o) for e in E4 for o in O4)
assert len(TOTAL) == 1600
PAIRED = frozenset(S for S in TOTAL if paired(S))
assert len(PAIRED) == 1120
print('OPTIMUM_COUNTS_OK total=1600 paired=1120 nonpaired=480')

ORBIT_REPS = (
    (40, True, (0, 1, 2, 3, 28, 29, 30, 31)),
    (120, True, (0, 1, 14, 15, 18, 19, 28, 29)),
    (480, True, (0, 13, 14, 15, 16, 17, 19, 30)),
    (480, True, (0, 4, 14, 15, 18, 19, 25, 29)),
    (480, False, (0, 1, 13, 15, 17, 22, 26, 30)),
)
recovered = set()
for size, expected_paired, tup in ORBIT_REPS:
    o = orbit(tup)
    assert len(o) == size
    assert o <= TOTAL
    assert not (recovered & o)
    assert all((S in PAIRED) == expected_paired for S in o)
    recovered.update(o)
    print(f'ORBIT_OK size={size} paired={expected_paired}')
assert recovered == TOTAL

# Smaller, independent orbit calculation: fix one four-point even-parity plane.
# Its stabilizer in the parity-preserving 5-cube symmetry group acts on 40 odd planes.
fixed_even = frozenset((0, 3, 29, 30))
assert fixed_even in E4
stabilizer = []
for p in permutations(range(D)):
    xform = tuple(sum(((v >> i) & 1) << p[i] for i in range(D)) for v in V)
    for shift in EVEN:
        f = tuple(x ^ shift for x in xform)
        if frozenset(f[v] for v in fixed_even) == fixed_even:
            stabilizer.append(f)
assert len(stabilizer) == 48
local_reps = (
    (1, True, (1, 2, 28, 31)),
    (3, True, (4, 7, 25, 26)),
    (12, True, (1, 4, 26, 31)),
    (12, True, (4, 11, 21, 26)),
    (12, False, (1, 13, 22, 26)),
)
seen_odd = set()
for want, matching, odd_rep in local_reps:
    orbit_odd = {frozenset(f[v] for v in odd_rep) for f in stabilizer}
    assert len(orbit_odd) == want
    assert orbit_odd <= O4
    assert not seen_odd.intersection(orbit_odd)
    assert all(paired(fixed_even | b) == matching for b in orbit_odd)
    seen_odd.update(orbit_odd)
assert seen_odd == O4
print('FIXED_PARITY_STABILIZER_OK order=48 local_orbits=[1,3,12,12,12]')

# An exchange may move a chosen bit between parities, or within one parity.
# The structural argument says none can preserve total domination at size 8.
lookup = TOTAL
exchange_edges = 0
for S in TOTAL:
    for u in S:
        for v in V:
            if v not in S and frozenset((S - {u}) | {v}) in lookup:
                exchange_edges += 1
assert exchange_edges == 0
assert len(PAIRED) == 1120
print('EXCHANGE_OK total=1600_isolated paired=1120_isolated')

if '--exhaustive' in sys.argv:
    # Independent direct 8-subset enumeration, without parity-plane factorization.
    # Uses closed-neighborhood or open-neighborhood coverage only from graph edges.
    open_masks = [sum(1 << w for w in N[v]) for v in V]
    goal = (1 << len(V)) - 1
    direct = 0
    for c in combinations(V, 8):
        covered = 0
        for v in c:
            covered |= open_masks[v]
        if covered == goal:
            direct += 1
            assert frozenset(c) in TOTAL
    assert direct == 1600
    print('FULL_8_SUBSET_EXHAUSTIVE_OK count=1600')

print('ALL_VERIFY_OK')
