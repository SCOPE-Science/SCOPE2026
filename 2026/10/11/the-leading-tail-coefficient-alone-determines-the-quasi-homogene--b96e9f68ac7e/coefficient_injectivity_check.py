#!/usr/bin/env python3
"""Finite diagnostic for the leading-coefficient injectivity theorem.

This script is not a proof of the infinite theorem.  It checks the published
closed formula at high precision for a bounded range and reports the closest
pair of distinct coefficient values.
"""
from decimal import Decimal, getcontext

getcontext().prec = 80

def coeff(a: int, b: int) -> Decimal:
    if not (1 <= a < b):
        raise ValueError("require 1 <= a < b")
    A = Decimal(a)
    B = Decimal(b)
    d = B - A
    return (
        A * B * (A + B) / (d * d)
        - Decimal(2) * A * A * B * B / (d * d * d) * (B / A).ln()
    )

def main() -> None:
    values = []
    for a in range(1, 201):
        for b in range(a + 1, 201):
            values.append((coeff(a, b), a, b))
    values.sort(key=lambda t: t[0])

    min_gap = None
    closest = None
    for left, right in zip(values, values[1:]):
        gap = right[0] - left[0]
        if min_gap is None or gap < min_gap:
            min_gap = gap
            closest = (left, right)

    assert min_gap is not None and min_gap > 0
    print("pairs_checked =", len(values))
    print("minimum_gap =", min_gap)
    print("closest_left =", closest[0])
    print("closest_right =", closest[1])
    print("finite_stress_test = OK")

if __name__ == "__main__":
    main()
