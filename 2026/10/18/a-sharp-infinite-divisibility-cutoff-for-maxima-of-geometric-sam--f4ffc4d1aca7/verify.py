"""Exact-rational arithmetic tests for geometric-maxima count laws.

Finite cases are diagnostics, not a substitute for the analytic all-parameter proof.
"""
from fractions import Fraction
from itertools import product


def masses(q, n, kmax):
    return [(1-q**(k+1))**n - (1-q**k)**n for k in range(kmax+1)]


def via_cdf(q, n, k):
    count = 0
    # Direct enumeration of geometric probabilities, truncated at k. All samples
    # with maximum exactly k are included: no larger coordinates can appear.
    weights = [(1-q)*q**i for i in range(k+1)]
    for outcome in product(range(k+1), repeat=n):
        if max(outcome) == k:
            t = Fraction(1)
            for j in outcome:
                t *= weights[j]
            count += t
    return count


def d(q, n):
    return (1+q)**(2*n) + 1 - 2*(1+q+q*q)**n


def two_factor_coeffs(q, kmax):
    # G2(z)=(1-q)^2(1+qz)/((1-qz)(1-q^2z))
    out = []
    for k in range(kmax+1):
        coeff = sum(q**(i + 2*(k-i)) for i in range(k+1))
        if k:
            coeff += q*sum(q**(i + 2*(k-1-i)) for i in range(k))
        out.append((1-q)**2*coeff)
    return out


def run():
    tests = 0
    for q in [Fraction(j, 11) for j in range(1, 11)] + [Fraction(1, 30), Fraction(29, 30)]:
        p = masses(q, 2, 16)
        assert p == two_factor_coeffs(q, 16)
        tests += 17
        assert d(q, 2) == -q**4
        tests += 1
        for n in range(3, 26):
            assert d(q, n) > 0
            assert d(q, n+1) == (1+q)**2*d(q, n) + 2*q*(1+q+q*q)**n - (2*q+q*q)
            tests += 2
        for n in range(1, 5):
            for k in range(0, 5):
                assert masses(q, n, k)[-1] == via_cdf(q, n, k)
                tests += 1
    print(f'PASS: {tests} exact rational identities and distribution enumerations')


if __name__ == '__main__':
    run()
