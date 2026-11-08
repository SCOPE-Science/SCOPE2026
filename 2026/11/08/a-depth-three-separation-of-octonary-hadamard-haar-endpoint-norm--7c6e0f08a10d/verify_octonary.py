#!/usr/bin/env python3
"""Exact-rational diagnostics for octonary Sylvester-Hadamard Haar sign transforms."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product


def block(mask):
    signs = [1 if mask & (1 << (a - 1)) else -1 for a in range(1, 8)]
    return tuple(sum(signs[a - 1] * (1 if (a & y).bit_count() % 2 == 0 else -1)
                     for a in range(1, 8)) for y in range(8))


profiles = {}
for mask in range(128):
    h = block(mask)
    key = (h[0], tuple(sorted(h[1:])))
    profiles[key] = mask
assert len(profiles) == 10, ('local Walsh profile census', len(profiles))
for key in profiles:
    h0, rest = key
    s = sum(abs(x) for x in rest)
    z = sum(1 if x > 0 else -1 for x in rest)
    for b, t in product((Q(1, 7), Q(1)), (Q(0), Q(1))):
        candidate = s + b * abs(h0) + t * (z + b * (1 if h0 > 0 else -1))
        target = 17 + b + t * (1 + b)
        assert candidate <= target, (key, b, t, candidate, target)
assert block(116)[0] == 1
assert sorted(block(116)[1:]) == [-3, -3, -3, 1, 1, 1, 5]
print('LOCAL_PROFILE_CENSUS_AND_40_EXACT_CORNER_INEQUALITIES_PASSED')

@lru_cache(None)
def bellman(depth, t):
    if depth == 0:
        return abs(t)
    return max(sum(abs(t + x) for x in rest) / Q(8)
               + bellman(depth - 1, (t + h0) / 8)
               for h0, rest in profiles)


def closed(depth):
    return Q(15, 7) * depth + Q(13, 49) + Q(36, 49 * 8 ** depth)


def shape(depth, t):
    a = Q(15, 7) * depth + Q(6, 49) * (1 - Q(1, 8 ** depth))
    b = Q(1, 7) + Q(6, 7 * 8 ** depth)
    return a + b * abs(t)

for depth in range(5):
    for t in map(Q, (-1, Q(-3, 4), Q(-1, 2), Q(-1, 4), 0,
                     Q(1, 4), Q(1, 2), Q(3, 4), 1)):
        assert bellman(depth, t) == shape(depth, t), (depth, t)
    assert bellman(depth, Q(1)) == closed(depth)
print('EXACT_BELLMAN_INDEPENDENT_RECURSION_CHECKS_PASSED depths=0..4')


def row_value(word):
    value = 1
    for j, digit in enumerate(word):
        if any(word[i] != 0 for i in range(j)):
            break
        value += 8 ** j * block(116)[digit]
    return value

for depth in range(7):
    total = sum(abs(row_value(word)) for word in product(range(8), repeat=depth))
    actual = Q(total, 8 ** depth)
    assert actual == closed(depth), (depth, actual, closed(depth))
    binary = Q(2 * (3 * depth), 3) + Q(5, 9) + Q(4, 9) * Q((-1) ** (3 * depth), 2 ** (3 * depth))
    if depth <= 2:
        assert actual == binary
    else:
        assert actual > binary
    print('DEPTH', depth, 'SIGNED_ROW_L1', actual, 'BINARY_3D', binary)
print('FULL_DIRECT_KERNEL_WITNESS_CHECKS_PASSED depths=0..6')
print('ALL_OCTONARY_HAAR_DIAGNOSTICS_PASSED')
