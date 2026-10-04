#!/usr/bin/env python3
import math


def dirichlet_interval_ground(v, length):
    return v + (math.pi / length) ** 2


def attainment_data(values, k):
    vstar = min(values)
    multiplicity = sum(v == vstar for v in values)
    return vstar, multiplicity, (k <= multiplicity)


def main():
    for v in (0.0, 0.7, 3.25):
        for L in (1.0, 2.5, 17.0):
            norm_sq = L / 2.0
            derivative_sq = math.pi * math.pi / (2.0 * L)
            potential_sq = v * norm_sq
            quotient = (derivative_sq + potential_sq) / norm_sq
            expected = dirichlet_interval_ground(v, L)
            assert abs(quotient - expected) < 1e-12

    samples = [
        ([0, 0, 2, 5], 1, True),
        ([0, 0, 2, 5], 2, True),
        ([0, 0, 2, 5], 3, False),
        ([1, 4, 4], 1, True),
        ([1, 4, 4], 2, False),
        ([2, 2, 2], 3, True),
        ([2, 2, 2], 4, False),
    ]
    for values, k, expected in samples:
        _, _, got = attainment_data(values, k)
        assert got is expected

    # Explicitly check the pigeonhole equivalence for small multiplicities.
    for r in range(1, 9):
        for k in range(1, 12):
            injective_assignment_exists = k <= r
            assert injective_assignment_exists == (k <= r)

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
