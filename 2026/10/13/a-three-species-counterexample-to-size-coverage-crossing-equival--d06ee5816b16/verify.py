#!/usr/bin/env python3
"""Exact arithmetic checks for richness-versus-coverage ranking reversal."""
from fractions import Fraction as F
from itertools import product
from math import prod

P = (F(15, 20), F(4, 20), F(1, 20))
Q = (F(12, 20), F(7, 20), F(1, 20))


def richness(v, m):
    return sum((1 - (1 - x) ** m for x in v), F(0))


def coverage(v, m):
    return 1 - sum((x * (1 - x) ** m for x in v), F(0))


def enumerate_expectations(v, m):
    expected_richness = F(0)
    expected_coverage = F(0)
    total_mass = F(0)
    for seq in product(range(len(v)), repeat=m):
        weight = prod((v[j] for j in seq), start=F(1))
        present = set(seq)
        total_mass += weight
        expected_richness += weight * len(present)
        expected_coverage += weight * sum((v[j] for j in present), F(0))
    assert total_mass == 1
    return expected_richness, expected_coverage


def main():
    assert sum(P) == sum(Q) == 1
    assert all(F(0) < x < F(1) for v in (P, Q) for x in v)
    assert P[0] > Q[0]
    assert P[0] + P[1] == Q[0] + Q[1]
    assert coverage(P, 1) == F(121, 200)
    assert coverage(Q, 1) == F(97, 200)

    margins = [
        (coverage(P, 2) - coverage(Q, 2), F(69, 1000)),
        (coverage(Q, 3) - coverage(P, 2), F(3409, 80000)),
        (richness(Q, 2) - richness(P, 2), F(3, 25)),
        (coverage(P, 11) - coverage(Q, 7), F(15232306811121, 2048000000000000)),
        (coverage(Q, 8) - coverage(P, 11), F(1849849028879, 2048000000000000)),
        (richness(P, 11) - richness(Q, 8), F(211151851331, 5120000000000)),
    ]
    for obtained, expected in margins:
        assert obtained == expected and obtained > 0, (obtained, expected)
    assert coverage(P, 2) == F(39, 50)
    assert coverage(P, 11) == F(1954570132251121, 2048000000000000)
    assert richness(P, 11) == F(12007937655731, 5120000000000)
    assert richness(Q, 8) == F(29491964511, 12800000000)
    direct_states = 0
    for v in (P, Q):
        for m in (1, 2, 3):
            direct_r, direct_c = enumerate_expectations(v, m)
            assert direct_r == richness(v, m)
            assert direct_c == coverage(v, m)
            direct_states += 3**m
    for m in range(2, 41):
        assert richness(P, m) < richness(Q, m)
    print(f"VERIFY_OK exact_margins={len(margins)} direct_states={direct_states} sample_sizes_checked=2..40")


if __name__ == "__main__":
    main()
