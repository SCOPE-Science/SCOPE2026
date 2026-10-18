"""Reproducible finite checks for maximum open packings of the 8-cube.

Python 3 standard library. The unrestricted classification follows from the
mathematical proof; this program independently enumerates its finite inputs.
"""
from collections import Counter
from itertools import combinations, permutations

N = 7
trips = list(combinations(range(N), 3))
pairs = list(combinations(range(N), 2))
pidx = {p: i for i, p in enumerate(pairs)}
trip_masks = []
trip_pairs = []
for t in trips:
    pair_indices = [pidx[p] for p in combinations(t, 2)]
    trip_pairs.append(tuple(pair_indices))
    trip_masks.append(sum(1 << i for i in pair_indices))
full = (1 << len(pairs)) - 1
incidence = [[] for _ in pairs]
for ti, indices in enumerate(trip_pairs):
    for i in indices:
        incidence[i].append(ti)

systems = set()
def enumerate_triple_systems(covered, chosen):
    if covered == full:
        assert len(chosen) == 7
        systems.add(frozenset(chosen))
        return
    uncovered = [i for i in range(21) if not (covered >> i) & 1]
    key = min(uncovered, key=lambda i: sum((trip_masks[j] & covered) == 0 for j in incidence[i]))
    for j in incidence[key]:
        mask = trip_masks[j]
        if covered & mask == 0:
            enumerate_triple_systems(covered | mask, chosen + [j])
enumerate_triple_systems(0, [])
assert len(systems) == 30, len(systems)

# Reconstruct the unique 0-containing 1-perfect code of each Fano plane.
zero_codes = set()
for system in systems:
    lines = [sum(1 << i for i in trips[j]) for j in system]
    code = frozenset([0, 127] + lines + [127 ^ v for v in lines])
    assert len(code) == 16
    for a, b in combinations(code, 2):
        assert (a ^ b).bit_count() >= 3
    assert len({word ^ e for word in code for e in (0, 1, 2, 4, 8, 16, 32, 64)}) == 128
    zero_codes.add(code)
assert len(zero_codes) == 30
all_codes = {frozenset(word ^ t for word in code) for code in zero_codes for t in range(128)}
assert len(all_codes) == 240

# Independent parity-check construction of the 30 centered Hamming codes.
base = frozenset(word for word in range(128) if
                 (0 ^ (1 if word & 1 else 0) ^
                  (2 if word & 2 else 0) ^
                  (3 if word & 4 else 0) ^
                  (4 if word & 8 else 0) ^
                  (5 if word & 16 else 0) ^
                  (6 if word & 32 else 0) ^
                  (7 if word & 64 else 0)) == 0)
assert len(base) == 16
permuted_codes = {
    frozenset(sum(((word >> i) & 1) << p[i] for i in range(7)) for word in base)
    for p in permutations(range(7))
}
assert permuted_codes == zero_codes

# Count common Fano lines and subspace intersections for the 30 linear codes.
ref_lines = frozenset(v for v in base if v.bit_count() == 3)
common = Counter(len(ref_lines & frozenset(v for v in C if v.bit_count() == 3))
                 for C in zero_codes)
assert common == Counter({7: 1, 3: 7, 1: 14, 0: 8}), common

# Explicitly check open-neighborhood disjointness and 8 direction matching counts.
def lift(x, parity):
    return x | (((x.bit_count() & 1) ^ parity) << 7)

def direction_profile(A, B):
    profile = [0] * 8
    S = {lift(a, 0) for a in A} | {lift(b, 1) for b in B}
    assert len(S) == 32
    # For an open packing, same-parity centers may not be at distance two.
    seen = set()
    for v in S:
        neighbors = {v ^ (1 << i) for i in range(8)}
        assert seen.isdisjoint(neighbors)
        seen.update(neighbors)
    assert len(seen) == 256
    for a in A:
        near = [b for b in B if (a ^ b).bit_count() <= 1]
        assert len(near) == 1
        delta = a ^ near[0]
        j = 7 if delta == 0 else delta.bit_length() - 1
        profile[j] += 1
    assert sum(profile) == 16
    return tuple(sorted(profile, reverse=True))

# The 240 codes are transitive under cube isometries, hence the profile histogram
# for one A is multiplied by 240 to count all ordered (A,B) choices.
histogram_one_A = Counter(direction_profile(base, B) for B in all_codes)
expected_one_A = {
    (16,0,0,0,0,0,0,0): 8,
    (8,8,0,0,0,0,0,0): 56,
    (4,4,4,4,0,0,0,0): 112,
    (2,2,2,2,2,2,2,2): 64,
}
assert histogram_one_A == expected_one_A, histogram_one_A
assert sum(histogram_one_A.values()) == 240
assert 240 * sum(histogram_one_A.values()) == 57600
print('FANO_SYSTEMS=30 PERFECT_CODES=240')
print('COMMON_LINES=' + str(sorted(common.items())))
print('ALL_MAXIMUM_OPEN_PACKINGS=57600')
for pattern in sorted(expected_one_A, reverse=True):
    print('PROFILE=' + str(pattern) + ' COUNT=' + str(240 * expected_one_A[pattern]))
print('EXPLICIT_PACKINGS_VALIDATED=240')
print('VERIFY_OK')
