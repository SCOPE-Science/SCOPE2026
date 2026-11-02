#!/usr/bin/env python3
"""Exact, self-contained checks for a three-class simple voting game."""
from itertools import product
from math import comb

BASE = (20, 15, 12)
MODELS = (((24, 18, 16), 73, (0, 0, 5)),
          ((30, 20, 16), 81, (3, 0, 0)))


def base_weight(profile):
    return sum(x * y for x, y in zip(profile, BASE))


def true_win(profile):
    s = base_weight(profile)
    return s == 59 or s >= 61


def predicted_win(profile, weights, quota):
    return sum(x * y for x, y in zip(profile, weights)) >= quota


def verify():
    near = list(product(range(4), range(5), range(6)))
    for weight, quota, exception in MODELS:
        # A global all-size certificate: at original weight >= 62,
        # the new score is >= min_i(w_i/base_i)*62 > quota.
        assert min(a / b for a, b in zip(weight, BASE)) * 62 > quota
        assert max(sum(a * b for a, b in zip(p, weight))
                   for p in near if base_weight(p) <= 58) < quota
        errors = [p for p in near if base_weight(p) <= 61
                  and true_win(p) != predicted_win(p, weight, quota)]
        assert errors == [exception], (weight, errors)
    low_profiles = {k: [p for p in near if base_weight(p) == k]
                    for k in (59, 60, 61)}
    assert low_profiles[59] == [(1, 1, 2)]
    assert low_profiles[60] == [(0, 0, 5), (0, 4, 0), (3, 0, 0)]
    assert low_profiles[61] == []

    checked = 0
    for m in range(5, 45):
        at_least = min(comb(m, 3), comb(m, 5))
        orbit_sizes = [m * m * comb(m, 2), comb(m, 3),
                       comb(m, 4), comb(m, 5)]
        assert min(orbit_sizes) == at_least
        predicted = []
        for w, quota, exception in MODELS:
            # Global classification certificate leaves one bad profile.
            predicted.append(comb(m, exception[0])
                             * comb(m, exception[1])
                             * comb(m, exception[2]))
        assert min(predicted) == at_least
        checked += 1

    # Independent full 15-voter check of the one-error construction.
    m = 5
    exhaustive = 0
    exceptional = []
    for mask in range(1 << (3 * m)):
        profile = tuple(((mask >> (m * i)) & ((1 << m) - 1)).bit_count()
                        for i in range(3))
        predicted = predicted_win(profile, MODELS[0][0], MODELS[0][1])
        if true_win(profile) != predicted:
            exhaustive += 1
            exceptional.append(mask)
    assert exhaustive == 1
    assert exceptional == [((1 << 5) - 1) << 10]
    print('VERIFY_OK low_profiles=120 parameter_sizes=40 '
          'exhaustive_m5=32768 errors_m5=1')


if __name__ == '__main__':
    verify()
