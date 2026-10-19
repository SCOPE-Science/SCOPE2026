"""Exact finite checks for frozen-leaf stars and dyadic opinion maps.

Run: python3 verification.py
The almost-sure and dimension assertions rely on the analytical proof, not these finite checks.
"""
from fractions import Fraction as F
from itertools import product
from math import floor


def receptive_leaves(values, epsilon):
    m = sum(values, F(0)) / len(values)
    return [abs(v - m) < epsilon for v in values]


def binary_canonical(k):
    return [F(1)] * (k // 2) + [F(0)] * (k - k // 2)


def star_step(hub, leaves, chosen, epsilon, rho):
    """Unrewired, pure-transitive NDW, exactly one selected star edge."""
    hub, leaves = F(hub), [F(v) for v in leaves]
    mean = sum(leaves, F(0)) / len(leaves)
    old_leaf = leaves[chosen]
    if abs(old_leaf - mean) < epsilon:
        leaves[chosen] = old_leaf + rho * (hub - old_leaf)
    hub = hub + rho * (old_leaf - hub)
    return hub, leaves


def verify():
    count = 0
    grid = [F(j, 4) for j in range(5)]
    for k in range(2, 7):
        sharp = F(k // 2, k)
        maximum = F(0)
        for values in product(grid, repeat=k):
            mean = sum(values, F(0)) / k
            d = min(abs(v - mean) for v in values)
            maximum = max(maximum, d)
            assert d <= sharp
            count += 1
        assert maximum == sharp, (k, maximum, sharp)
        leaves = binary_canonical(k)
        assert not any(receptive_leaves(leaves, sharp))
        assert any(receptive_leaves(leaves, sharp + F(1, 1000)))
        hub = F(1, 7)
        for t in range(80):
            hub, after = star_step(hub, leaves, t % k, sharp, F(1, 2))
            assert after == leaves
            assert F(0) <= hub <= F(1)
    # The two affine half-maps produce all dyadic cylinders exactly.
    for depth in range(1, 10):
        intervals = []
        for word in product((0, 1), repeat=depth):
            lo, hi = F(0), F(1)
            for bit in word:
                lo, hi = (lo + bit) / 2, (hi + bit) / 2
            intervals.append((lo, hi))
        assert sorted(intervals) == [(F(j, 2**depth), F(j+1, 2**depth))
                                      for j in range(2**depth)]
    for k in range(2, 31):
        p = F(k//2, k)
        # Stationary means and variances under H -> (H+B)/2.
        variance = p * (1-p) / 3
        assert p == (p+p)/2
        assert variance == variance / 4 + p*(1-p)/4
        assert (p == F(1, 2)) == (k % 2 == 0)
    print('PASS: 19,525 exact-grid star profiles; all canonical shells;')
    print('PASS: all dyadic cylinders through depth 9; stationary moment identities;')
    print('PASS: exact star transitions and all claimed boundary equalities.')
    print('LIMIT: finite checks do not establish almost-sure density or dimension.')


if __name__ == '__main__':
    verify()
