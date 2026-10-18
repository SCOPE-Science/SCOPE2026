#!/usr/bin/env python3
"""Finite computational checks for an analytical multi-peak richness-variance theorem.

No finite check is used to justify the theorem for all community sizes.
"""
import math
from fractions import Fraction

L2 = math.log(2)


def f(z):
    u = math.exp(-z)
    return u * (2.0 * u - 1.0)


def derivative(t, rates):
    return math.fsum(rate * f(rate * t) for rate in rates)


def sign(x):
    return (x > 0) - (x < 0)


def test(n):
    rates = [20**j for j in range(n)]
    witnesses = [(0., 1, 'origin')]
    for j in range(n-1, -1, -1):
        witnesses.append((2*L2/rates[j], -1, f'a_{j+1}'))
        if j > 0:
            witnesses.append((L2/(2*rates[j-1]), 1, f'b_{j}'))
    assert len(witnesses) == 2*n
    assert all(witnesses[i][0] < witnesses[i+1][0]
               for i in range(len(witnesses)-1))
    observed = []
    for t, expected, label in witnesses:
        actual = derivative(t, rates)
        assert sign(actual) == expected, (n, label, t, actual)
        observed.append((label, expected))
    return observed


def test_rational_inequalities():
    assert Fraction(1, 19) < Fraction(1, 8)
    assert Fraction(40, 1024) < Fraction(1, 20)
    assert Fraction(1, 2) < Fraction(9, 16)  # 1/sqrt(2) < 3/4
    assert 20 * 2**(-190) < 0.5


def main():
    test_rational_inequalities()
    total = 0
    for n in range(1, 11):
        checked = test(n)
        total += len(checked)
        print(f'n={n:2d}: {len(checked)} derivative-sign witnesses pass; '
              f'predicted strict maxima={n}, strict minima={n-1}')
    print(f'PASS: {total} finite sign witnesses plus rational bounds')
    print('The infinite-size upper bound and all-size existence are analytical.')


if __name__ == '__main__':
    main()
