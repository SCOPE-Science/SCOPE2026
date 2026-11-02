#!/usr/bin/env python3
"""Independent exact-spin census and Walsh checks for a two-range Ising cube."""
from collections import Counter
from itertools import combinations
from fractions import Fraction
from math import comb


def char(d, mask):
    return tuple(1 if ((x & mask).bit_count() % 2 == 0) else -1 for x in range(1 << d))


def energy_terms(d, s):
    n = 1 << d
    near = sum(s[x] * s[x ^ (1 << j)] for x in range(n) for j in range(d) if not (x & (1 << j)))
    far = sum(s[x] * s[x ^ (n-1)] for x in range(n) if not (x & 1))
    return near, far


def predicted(d, k):
    eta = (-1)**d * k
    m = (1 << (d-1)) * (-d + min(eta, 2 - eta))
    full = (1 << d) - 1
    if eta < 1:
        masks = [full]
    elif eta > 1:
        masks = [full ^ (1 << j) for j in range(d)]
    else:
        masks = [full] + [full ^ (1 << j) for j in range(d)]
    states = {t for mask in masks for t in (char(d, mask), tuple(-v for v in char(d, mask)))}
    return m, states


def check_census(d, k):
    n = 1 << d
    best = None
    winners = set()
    for state in range(1 << n):
        spins = tuple(1 if (state >> i) & 1 else -1 for i in range(n))
        near, far = energy_terms(d, spins)
        value = near + k * far
        if best is None or value < best:
            best, winners = value, {spins}
        elif value == best:
            winners.add(spins)
    exp_e, exp_states = predicted(d, k)
    assert best == exp_e, (d, k, best, exp_e)
    assert winners == exp_states, (d, k, len(winners), len(exp_states), winners ^ exp_states)
    # Verify every Hamming-distance covariance exactly from the complete ground-state census.
    for r in range(d + 1):
        ratio = Fraction(sum(s[0]*s[(1 << r)-1] for s in winners), len(winners))
        if (-1)**d * k < 1:
            expected = Fraction((-1)**r, 1)
        elif (-1)**d * k > 1:
            expected = Fraction((-1)**r * (d - 2*r), d)
        else:
            expected = Fraction((-1)**r * (d+1 - 2*r), d+1)
        assert ratio == expected, (d, k, r, ratio, expected)
    return len(winners)


def check_walsh(d, k):
    n = 1 << d
    actual = []
    for mask in range(n):
        s = char(d, mask)
        # The adjacency (J=1) action is computed explicitly at every vertex.
        vals = []
        for x in range(n):
            vals.append(sum(s[x ^ (1 << j)] for j in range(d)) + k*s[x ^ (n-1)])
        assert len(set(v * s[x] for x, v in enumerate(vals))) == 1
        eig = vals[0] * s[0]
        expected = d - 2*mask.bit_count() + k * (-1)**mask.bit_count()
        assert eig == expected
        actual.append(eig)
    minpred = -d + min((-1)**d*k, 2-(-1)**d*k)
    assert min(actual) == minpred


if __name__ == '__main__':
    cases = 0
    spin_states = 0
    pair_check = 0
    spectral = 0
    for d in (2, 3, 4):
        for k in (-3, -2, -1, 0, 1, 2, 3, Fraction(-3,2), Fraction(-1,2), Fraction(1,2), Fraction(3,2)):
            count = check_census(d, k)
            cases += 1
            spin_states += 1 << (1 << d)
            pair_check += d + 1
            print(f'PASS d={d} K/J={k} minimum_count={count}')
    for d in range(2, 9):
        for k in (-5, -1, 0, 1, 5):
            check_walsh(d, k)
            spectral += 1
    print(f'PASS SUMMARY exhaustive_cases={cases} evaluated_spin_assignments={spin_states} exact_distance_correlations={pair_check} complete_walsh_cases={spectral}')
