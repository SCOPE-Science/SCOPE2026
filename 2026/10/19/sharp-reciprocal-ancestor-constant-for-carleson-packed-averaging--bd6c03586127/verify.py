#!/usr/bin/env python3
"""Exact-rational finite checks for the reciprocal-ancestor Carleson inequality.

This program supplements, but does not replace, the proof for arbitrary chains.
It uses only Python's standard library.
"""
from fractions import Fraction as F
from itertools import product


def greedy(L, depth):
    assert L >= 1
    if L == 1:
        return [F(1)]
    masses = [F(1)]
    for _ in range(depth):
        old_total = sum(masses)
        masses.append(max(masses[-1], old_total / (L - 1)))
        assert sum(masses) <= L * masses[-1]
    return masses


def exact_constant(L):
    if L == 1:
        return F(1)
    n = L.numerator // L.denominator
    return F(n) + L * (L - 1) / n


def check_exact_tail(L):
    if L == 1:
        return
    n = L.numerator // L.denominator
    y = greedy(L, n + 11)
    assert y[:n] == [F(1)] * n
    assert y[n] == F(n) / (L - 1)
    ratio = L / (L - 1)
    for j in range(n, len(y)):
        assert y[j] == F(n) / (L - 1) * ratio ** (j - n)
    assert exact_constant(L) == F(n) + 1 / y[n] * ratio / (ratio - 1)
    assert exact_constant(L) <= 2 * L - 1
    assert exact_constant(L) <= L * L


def check_small_measure_spaces(L):
    # All measurable Omega on finite, initially nested atomic spaces.
    m = greedy(L, 7)
    point_masses = [m[0]] + [m[j] - m[j-1] for j in range(1,len(m))]
    for mask in range(1 << len(point_masses)):
        omega_mass = sum(point_masses[j] for j in range(len(point_masses)) if mask & (1 << j))
        included_prefixes = [j for j in range(len(point_masses)) if (mask & ((1 << (j + 1)) - 1)) == ((1 << (j + 1)) - 1)]
        mass_sum = sum(m[j] for j in included_prefixes)
        assert mass_sum <= L * omega_mass
    assert sum(1/t for t in m) < exact_constant(L)


def check_dominance(L):
    # Every explored rational monotone admissible prefix dominates the
    # coordinatewise-minimal sequence, not merely its final reciprocal sum.
    if L == 1:
        return
    z = greedy(L, 4)
    values = [F(k,2) for k in range(2,13)]
    for tail in product(values, repeat=3):
        x = (F(1),) + tail
        if any(x[i] > x[i+1] for i in range(3)):
            continue
        if any(sum(x[:j+1]) > L*x[j] for j in range(4)):
            continue
        for i in range(4):
            assert x[i] >= z[i]
        assert sum(1 / a for a in x) <= sum(1 / a for a in z[:4])


def main():
    values = sorted(set([F(1), F(11,10), F(5,4), F(3,2), F(19,10), F(2), F(5,2),
                        F(3),F(37,10),F(4),F(40,7),F(10)]
                        + [F(k,3) for k in range(3,31)]))
    for L in values:
        check_exact_tail(L)
        if L != 1:
            check_small_measure_spaces(L)
            check_dominance(L)
    print('VERIFY_OK:',len(values),'distinct rational Carleson parameters; exact tails,')
    print('             all subsets of sample chains, and constrained prefix comparisons.')


if __name__ == '__main__':
    main()
