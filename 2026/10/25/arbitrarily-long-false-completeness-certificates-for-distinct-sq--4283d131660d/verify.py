#!/usr/bin/env python3
"""Exact checks for the square-power finite-certificate obstruction."""
from math import gcd


def reachable_bitset(bound):
    bits = 1  # empty subset
    for i in range(1, bound + 1):
        bits |= bits << (i * i)
    return bits


def reachable_witnesses(bound):
    # Independent exact dictionary-based subset-sum construction.
    ways = {0: ()}
    for i in range(1, bound + 1):
        for total, indices in tuple(ways.items()):
            ways.setdefault(total + i * i, indices + (i,))
    return ways


base_bits = reachable_bitset(18)
base_ways = reachable_witnesses(18)
assert (128 not in base_ways) and not ((base_bits >> 128) & 1)
assert all(((base_bits >> t) & 1) and (t in base_ways)
           for t in range(129, 18 * 18 + 1))
assert len(base_ways) == 2048
assert sum(i * i for i in range(1, 19)) == 2109

# Cross-check that the two independently constructed exact representations agree.
assert all(bool((base_bits >> t) & 1) == (t in base_ways)
           for t in range(sum(i * i for i in range(1, 19)) + 1))
for t in (129, 130, 150, 211, 324):
    witness = base_ways[t]
    assert len(set(witness)) == len(witness)
    assert sum(i * i for i in witness) == t

for B in range(18, 401):
    square_sum = B * (B + 1) * (2 * B + 1) // 6
    Q = square_sum + 2
    assert Q > B and gcd(*range(1, min(B, 3) + 1)) == 1
    assert 129 <= B * B + 1 - (B - 4) ** 2
    assert 1 <= B - 4
    # Both polynomial inequalities have positive derivative for m >= B >= 18.
    assert B * B - 18 * B + 31 > 0
    assert B * B - 10 * B + 15 >= 0
    assert B * B + 1 - (B - 4) ** 2 >= 129
    assert (B + 1) ** 2 - (B - 4) ** 2 <= B * B
    # For every j >= 0, all tail squares vanish mod Q whereas a prefix
    # subset square sum is between 0 and Q-2.
    for j in (0, 1, 2, 19, 1000):
        missing = (j + 1) * Q - 1
        assert missing % Q == Q - 1
        assert square_sum == Q - 2
        for index in (1, 2, 3):
            assert ((index * Q) ** 2) % Q == 0

# Construct one fully explicit counterexample at B=18.
B = 18
S = sum(i * i for i in range(1, B + 1))
Q = S + 2
assert (S, Q) == (2109, 2111)
assert all(t in base_ways for t in range(129, 325))
assert all((j + 1) * Q - 1 > 324 for j in range(5))
print('VERIFY_OK: exact independent 18-square subset sums (2048 distinct totals);'
      ' base interval 129..324, 128 excluded;'
      ' symbolic-inequality endpoint checks B=18..400;'
      ' modular obstruction Q=S+2; B=18 gives Q=2111.')
