"""Exact finite verification of the six-rank sign-test calibration theorem.

All probabilities are fractions; no simulations or external dependencies.
"""
from fractions import Fraction as F
from itertools import combinations, product


def law(k_weights, low_mode):
    probs = {bits: F(0) for bits in product((0, 1), repeat=6)}
    for k, weight in k_weights.items():
        for subset in combinations(range(4), k):
            high = tuple(int(j in subset) for j in range(4))
            if low_mode == "upper":
                lows = ((0, 1), (1, 0)) if k != 2 else ((0, 0), (1, 1))
            else:
                lows = tuple(product((0, 1), repeat=2))
            for lo in lows:
                bits = tuple(lo) + high
                probs[bits] += weight / (len(tuple(combinations(range(4), k))) * len(lows))
    return probs


def rejection(bits):
    return sum((j + 1) * bits[j] for j in range(6)) >= 19


def check(probs, expected):
    assert sum(probs.values(), F(0)) == 1
    for i in range(6):
        assert sum(p for bits, p in probs.items() if bits[i]) == F(1, 2)
        for j in range(i + 1, 6):
            assert sum(p for bits, p in probs.items() if bits[i] and bits[j]) == F(1, 4)
    assert sum(p for bits, p in probs.items() if rejection(bits)) == expected


upper = law({1: F(1, 3), 2: F(1, 2), 4: F(1, 6)}, "upper")
lower = law({0: F(1, 6), 2: F(1, 2), 3: F(1, 3)}, "lower")
check(upper, F(1, 6))
check(lower, F(0))
assert sum(rejection(bits) for bits in product((0, 1), repeat=6)) == 3
assert F(3, 64) * F(32, 9) == F(1, 6)
for k in range(5):
    assert (k - 1) * (k - 2) >= 6 * (k == 4)
for t in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
    mixed = {bits: t * upper[bits] + (1-t) * lower[bits] for bits in upper}
    check(mixed, t / 6)
print("PASS: exact six-sign calibration, both sharp extremizers, mixtures, and moments")
