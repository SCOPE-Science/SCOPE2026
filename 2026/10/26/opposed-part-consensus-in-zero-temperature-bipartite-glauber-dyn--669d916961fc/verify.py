#!/usr/bin/env python3
"""Exact finite-state checks for a two-population zero-temperature majority race."""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial, erf, sqrt


def beta_at_integers(x, y):
    assert x >= 1 and y >= 1
    return Fraction(factorial(x - 1) * factorial(y - 1), factorial(x + y - 1))


def beta_probability(m, n, a, b):
    assert m >= 3 and n >= 3 and m % 2 and n % 2
    u, v = (m - 1) // 2, (n - 1) // 2
    assert u + 1 <= a <= m and v + 1 <= b <= n
    den = beta_at_integers(v + 1, b - v)
    numerator = sum((Fraction(comb(a, j)) * beta_at_integers(v + 1 + j, b - v + a - j)
                    for j in range(u + 1, a + 1)), Fraction())
    return numerator / den


def independent_clock_race(m, n, a, b):
    """First-event equations for the reduced Markov jump process."""
    u, v = (m - 1) // 2, (n - 1) // 2

    @lru_cache(None)
    def state(i, j):
        if i <= u:
            return Fraction(0)
        if j <= v:
            return Fraction(1)
        return (Fraction(i, i+j)*state(i-1,j)
                + Fraction(j, i+j)*state(i,j-1))

    return state(a, b)


def gauss_window(m,n,a,b):
    p, q = a / m, b / n
    var = p * (2*p-1) * (1+m/n)
    return (1+erf((p-q)*sqrt(m)/sqrt(2*var))) / 2


def main():
    checked = 0
    for m in (3,5,7,9):
        for n in (3,5,7,9):
            for a in range((m+1)//2, m+1):
                for b in range((n+1)//2, n+1):
                    assert beta_probability(m,n,a,b) == independent_clock_race(m,n,a,b)
                    checked += 1
            assert beta_probability(m,n,m,n) == Fraction(1,2)
    assert checked == 196
    m,n,a,b = 31,101,25,61
    assert a+(n-b) < (m+n)/2
    val = float(beta_probability(m,n,a,b))
    assert 0.97868 < val < 0.97870, val
    critical = [(101,101,81,80),(101,151,91,133),(501,751,401,600)]
    for m,n,a,b in critical:
        exact = float(beta_probability(m,n,a,b))
        approximation = gauss_window(m,n,a,b)
        assert abs(exact-approximation) < .003,(m,n,a,b,exact,approximation)
    print('PASS: 196 exact-rational race identities; 16 polarization symmetries;')
    print('global-majority inversion:', format(val,'.15f'))
    print('PASS: 3 critical-window finite-size approximation comparisons')


if __name__ == '__main__':
    main()
