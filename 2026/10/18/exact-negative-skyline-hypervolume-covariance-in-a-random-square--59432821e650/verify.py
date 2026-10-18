#!/usr/bin/env python3
"""Exact finite checks for planar skyline-cardinality/hypervolume covariance.

Only Python's standard library is required. All enumeration comparisons are exact
rational equalities. These finite checks corroborate rather than replace the proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial, log, pi


def harmonic(n, power=1):
    return sum((Fraction(1, j**power) for j in range(1, n + 1)), Fraction(0))


def closed_cov(n):
    N = n + 1
    h, h2 = harmonic(N), harmonic(N, 2)
    return -(h - h2 - 1 + h / N) / N


def closed_local(n, i):
    assert 1 <= i <= n
    return -(Fraction(i) - harmonic(i)) / ((n + 1) * i * (i + 1))


def brute_ranks(n):
    # A point ranked r in the Y order has expected Y value r/(n+1).
    # Independently, each of the n+1 X-order spacings has mean 1/(n+1).
    # Consequently E[A | Y-rank permutation] = sum(prefix maxima)/(n+1)^2.
    total_m = total_q = total_mq = 0
    local_m = [0] * n
    local_iq = [0] * n
    for perm in permutations(range(1, n + 1)):
        maxrank = count = rank_sum = 0
        for j, val in enumerate(perm):
            is_rec = val > maxrank
            if is_rec:
                maxrank = val
                count += 1
                local_m[j] += 1
            rank_sum += maxrank
        # second pass only for mixed local expectation: the full rank_sum is known.
        maxrank = 0
        for j, val in enumerate(perm):
            if val > maxrank:
                maxrank = val
                local_iq[j] += rank_sum
        total_m += count
        total_q += rank_sum
        total_mq += count * rank_sum
    den = factorial(n)
    ea = Fraction(total_q, den * (n + 1)**2)
    em = Fraction(total_m, den)
    ema = Fraction(total_mq, den * (n + 1)**2)
    assert em == harmonic(n), (n, em, harmonic(n))
    assert ea == 1 - harmonic(n + 1) / (n + 1), (n, ea)
    actual = ema - em * ea
    assert actual == closed_cov(n), (n, actual, closed_cov(n))
    for i in range(1, n + 1):
        ei = Fraction(local_m[i - 1], den)
        assert ei == Fraction(1, i)
        eia = Fraction(local_iq[i - 1], den * (n + 1)**2)
        assert eia - ei * ea == closed_local(n, i), (n, i, eia - ei * ea)
    return actual


def main():
    exact = 0
    for n in range(1, 10):
        brute_ranks(n)
        exact += 3 + n
    for n in range(1, 151):
        assert closed_cov(n) == sum((closed_local(n, i)
                                     for i in range(1, n + 1)), Fraction(0))
        if n >= 2:
            assert closed_cov(n) < 0
            assert all(closed_local(n, i) < 0 for i in range(2, n + 1))
        exact += 2 if n >= 2 else 1
    assert closed_cov(2) == Fraction(-1, 36)
    assert closed_cov(3) == Fraction(-13, 288)
    exact += 2
    for n in (10_000, 100_000, 1_000_000):
        # Accurate floating harmonic approximation via asymptotic expansion.
        N = n + 1
        gamma = 0.5772156649015328606
        h = log(N) + gamma + 1/(2*N) - 1/(12*N*N)
        h2 = pi*pi/6 - 1/N + 1/(2*N*N)
        cov = -(h - h2 - 1 + h/N)/N
        assert abs(n * (-cov) - log(n) - (gamma - pi*pi/6 - 1)) < 0.001
        uncovered = h / N
        assert 0.7 < -cov / uncovered < 1.0
    print(f'PASS: {exact} exact rational finite checks; '
          '6 explicitly bounded large-n scaling comparisons')


if __name__ == '__main__':
    main()
