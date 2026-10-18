#!/usr/bin/env python3
"""Exact illustrative checks for sharp shallow-apex cylinder thresholds.

These finite checks verify example substitutions, not the general theorem.
"""
from fractions import Fraction as F


def check_side(width, opposite_weight, apex_normal_coordinate):
    width, lam, y = map(F, (width, opposite_weight, apex_normal_coordinate))
    radius_sq = width * width / 4
    cutoff_sq = width * width * lam * (1 - lam)
    assert (y - width / 2) ** 2 + cutoff_sq == radius_sq
    assert cutoff_sq > 0
    return cutoff_sq, radius_sq


assert check_side(F(2), F(1, 3), F(2, 3)) == (F(8, 9), F(1))
assert check_side(F(2), F(1, 10), F(1, 5)) == (F(9, 25), F(1))
assert check_side(F(3, 2), F(1, 3), F(1, 2)) == (F(1, 2), F(9, 16))
print("Three exact apex-boundary identities verified.")
