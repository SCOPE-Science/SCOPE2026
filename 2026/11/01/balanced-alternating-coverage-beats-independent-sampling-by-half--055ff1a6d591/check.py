#!/usr/bin/env python3
"""Exact finite tests for two balanced cover processes; no proof by enumeration."""
from fractions import Fraction
from math import comb


def complete_cdf(n, k):
    """Exact probability k uniform draws contain all n coupon types."""
    if k < n:
        return Fraction(0)
    return sum(((-1) ** j) * comb(n, j) * Fraction(n - j, n) ** k
               for j in range(n + 1))


def exact_gap(n):
    """Expected independent-uniform cover time minus alternating cover time."""
    harmonic = sum((Fraction(1, i) for i in range(1, 2 * n + 1)), Fraction())
    emax = -sum(((-1) ** (i+j)) * comb(n, i) * comb(n, j) *
                Fraction(n*n, n*(i+j)-i*j)
                for i in range(n+1) for j in range(n+1) if i+j)
    tie = sum(((-1) ** (i+j)) * comb(n, i) * comb(n, j) *
              Fraction(i*j, n*(i+j)-i*j)
              for i in range(1, n+1) for j in range(1, n+1))
    assert 0 < tie < 1
    return 2*n*harmonic - 1 - (2*emax - Fraction(3, 2) + tie/2)


def exact_dominance(n, t):
    """Compare completion CDFs at t steps after one fixed initial vertex."""
    a, b = t//2 + 1, (t+1)//2
    alternating = complete_cdf(n, a) * complete_cdf(n, b)
    iid = sum(Fraction(comb(t, k), 2**t) *
              complete_cdf(n, k+1) * complete_cdf(n, t-k)
              for k in range(t+1))
    return alternating, iid


def main():
    expected = {
        2: Fraction(4, 3),
        3: Fraction(52, 35),
        4: Fraction(724, 455),
        5: Fraction(112085972, 66927861),
        6: Fraction(22087031, 12660648),
        7: Fraction(43235626422003791, 23956744776174990),
    }
    checks = 0
    for n, value in expected.items():
        assert exact_gap(n) == value, (n, exact_gap(n))
        checks += 1
    for n in range(2, 8):
        for t in range(0, 8*n+1):
            alternating, iid = exact_dominance(n, t)
            assert alternating >= iid, (n, t, alternating, iid)
            checks += 1
    print('PASS:', checks, 'exact rational assertions')
    for n in expected:
        print('n =', n, 'exact mean difference =', expected[n], 'approx =', float(expected[n]))
    print('Infinite-parameter stochastic order and asymptotic coefficient require the analytic proof.')


if __name__ == '__main__':
    main()
