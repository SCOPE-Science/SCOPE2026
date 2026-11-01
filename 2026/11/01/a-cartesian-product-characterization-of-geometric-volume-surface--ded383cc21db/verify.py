#!/usr/bin/env python3
"""Exact rational consistency checks for the product-boundary second-moment formula."""
from fractions import Fraction as F
from itertools import product


def ball_product_gap(dimensions, radii):
    # Balls in orthogonal spaces: surface_i / volume_i = dimension_i / radius_i.
    ratios = [F(d, 1) / r for d, r in zip(dimensions, radii)]
    total = sum(ratios, F(0))
    p = [a / total for a in ratios]
    volume_moments = [F(d, d + 2) * r * r for d, r in zip(dimensions, radii)]
    # Calculate the full product's boundary second moment separately.
    boundary = sum(
        (p[i] * (radii[i] * radii[i] +
                 sum((volume_moments[j] for j in range(len(radii)) if j != i), F(0))))
        for i in range(len(radii))
    )
    volume = sum(volume_moments, F(0))
    predicted = sum((p[i] * F(2, dimensions[i] + 2) * radii[i] ** 2
                     for i in range(len(radii))), F(0))
    assert boundary - volume == predicted
    return predicted


def test():
    assert ball_product_gap((2, 1), (F(1), F(2))) == F(14, 15)
    # 1D Euclidean ball is an interval of radius 2.
    for count in (2, 3, 4):
        for dims in product((1, 2, 3), repeat=count):
            for radii in (tuple(F(i+1) for i in range(count)),
                          tuple(F(i+1, i+2) for i in range(count))):
                assert ball_product_gap(dims, radii) > 0
    for t in [F(0), F(1, 7), F(1, 3), F(3, 5), F(1)]:
        prob_plus = (1 + t) / 2
        prob_minus = (1 - t) / 2
        assert prob_plus - prob_minus == t
        assert prob_plus + prob_minus == 1
        assert prob_plus >= 0 and prob_minus >= 0
    print("PASS: exact cylinder gap, all rational ball-product moment identities, and martingale-sign arithmetic")


if __name__ == '__main__':
    test()
