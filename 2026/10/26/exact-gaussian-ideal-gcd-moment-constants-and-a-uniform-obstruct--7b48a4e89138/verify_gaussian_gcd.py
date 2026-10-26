#!/usr/bin/env python3
"""Reproduce exact finite checks for the Gaussian-ideal gcd-moment constant.

Uses only the Python standard library.  Gaussian ideals are represented by
one generator a+bi with a>0, b>=0.  This is one representative per unit orbit.
"""
from math import isqrt


def norm(z):
    return z[0] * z[0] + z[1] * z[1]


def gaussian_representatives(limit):
    return [(a, b) for a in range(1, isqrt(limit) + 1)
            for b in range(isqrt(limit - a * a) + 1)]


def quotient_and_remainder(z, w):
    a, b = z
    c, d = w
    den = norm(w)
    assert den > 0
    # Nearest Gaussian integer to z/w; ties are resolved consistently.
    u = (2 * (a * c + b * d) + den) // (2 * den)
    v = (2 * (b * c - a * d) + den) // (2 * den)
    r = (a - (u * c - v * d), b - (u * d + v * c))
    assert norm(r) < den
    return (u, v), r


def gcd_norm(z, w):
    while w != (0, 0):
        _, r = quotient_and_remainder(z, w)
        z, w = w, r
    return norm(z)


def coefficients_via_character(limit):
    # a(k) is the Dirichlet convolution of 1 and chi_4.
    coeff = [0] * (limit + 1)
    for odd in range(1, limit + 1, 2):
        sign = 1 if odd % 4 == 1 else -1
        for multiple in range(odd, limit + 1, odd):
            coeff[multiple] += sign
    return coeff


def mobius_inverse(coeff):
    # Convolution inverse: coeff * mu_G = delta_1.
    limit = len(coeff) - 1
    mu = [0] * (limit + 1)
    mu[1] = 1
    for n in range(2, limit + 1):
        mu[n] = -sum(mu[d] * coeff[n // d]
                     for d in range(1, n) if n % d == 0)
    return mu


def check():
    maximum = 10000
    a = coefficients_via_character(maximum)
    A = [0] * (maximum + 1)
    for k in range(1, maximum + 1):
        A[k] = A[k-1] + a[k]
        assert 0 <= a[k]
        assert A[k] <= k
        assert a[k] * (A[k] + A[k-1]) <= (2*k - 1) * a[k]
    assert [a[k] for k in range(1, 11)] == [1, 1, 0, 1, 2, 0, 0, 1, 1, 2]
    assert [A[k] for k in range(1, 11)] == [1, 2, 2, 3, 5, 5, 5, 6, 7, 9]
    assert a[4] * (A[4]+A[3] - 7) == -2
    assert A[4]*A[4]-A[3]*A[3] == 5
    for X in [8, 15, 24, 40]:
        reps = gaussian_representatives(X)
        assert len(reps) == A[X]
        aa = [0]*(X+1)
        for z in reps:
            aa[norm(z)] += 1
        assert aa == a[:X+1]
        mu = mobius_inverse(a[:X+1])
        F = [0]*(X+1)
        for t in range(1, X+1):
            F[t] = sum(mu[d]*A[t//d]**2 for d in range(1, t+1))
        # Exact gcd and coprimality are independently calculated from pairs.
        direct_gcd_frequency = [0]*(X+1)
        direct_coprime = 0
        for z in reps:
            for w in reps:
                g = gcd_norm(z, w)
                direct_gcd_frequency[g] += 1
                if g == 1:
                    direct_coprime += 1
        assert direct_coprime == F[X]
        assert sum(direct_gcd_frequency) == A[X]**2
        for power in (2, 3, 4, 5):
            direct_sum = sum(k**power * direct_gcd_frequency[k]
                             for k in range(1, X+1))
            mobius_sum = sum(a[k] * k**power * F[X//k]
                             for k in range(1, X+1))
            assert direct_sum == mobius_sum, (X, power, direct_sum, mobius_sum)
    print('VERIFY_OK: 10000 exact ideal-count inequalities and 4 complete Gaussian-gcd pair enumerations (moments 2..5).')


if __name__ == '__main__':
    check()
