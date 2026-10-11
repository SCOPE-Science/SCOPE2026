"""Exact finite-case checks of the sharp near-independent sign-moment formula.

Usage: python3 verify.py
Pure Python standard library. Finite checks are not a proof in all dimensions.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial
from random import Random


def independent_nth(coeff):
    n = len(coeff)
    assert n % 2 == 0
    return sum(sum(c * s for c, s in zip(coeff, signs)) ** n
               for signs in product((-1, 1), repeat=n)) // 2**n


def dependent_nth(coeff, theta):
    n = len(coeff)
    return sum((Fraction(1) + theta * prod(signs)) *
               sum(c * s for c, s in zip(coeff, signs)) ** n
               for signs in product((-1, 1), repeat=n)) / 2**n


def prod(seq):
    value = 1
    for x in seq:
        value *= x
    return value


def flat_independent_moment(n):
    return sum(comb(n, j) * (n-2*j)**n for j in range(n+1)) // 2**n


def verify():
    rng = Random(320148)
    checks = 0
    for n in (4, 6, 8):
        m = flat_independent_moment(n)
        for theta in (Fraction(-1), Fraction(-1, 3), Fraction(0),
                      Fraction(1, 3), Fraction(1)):
            for j in range(13):
                a = tuple(rng.randrange(-3, 4) for _ in range(n))
                if not any(a):
                    a = (1,) + (0,) * (n-1)
                lhs = dependent_nth(a, theta)
                rhs = independent_nth(a) + theta*factorial(n)*prod(a)
                assert lhs == rhs, (n, theta, j, lhs, rhs)
                square = sum(x*x for x in a)
                assert lhs * n**(n//2) <= (m+abs(theta)*factorial(n))*square**(n//2), (n, theta, j)
                checks += 1
            flat = (1,)*n if theta >= 0 else (-1,) + (1,)*(n-1)
            at_flat = dependent_nth(flat, theta)
            assert at_flat * n**(n//2) == (m+abs(theta)*factorial(n))*n**(n//2)
            checks += 1
    assert Fraction(flat_independent_moment(4)+factorial(4), 4**2) == 4
    assert Fraction(flat_independent_moment(6)+factorial(6), 6**3) == Fraction(124,9)
    assert Fraction(flat_independent_moment(8)+factorial(8), 8**4) == 71
    print('NEAR_INDEPENDENT_ENDPOINT_EXACT_OK', checks)
    print('EVEN_CYCLE_CONSTANTS', {n: str(Fraction(flat_independent_moment(n)+factorial(n),n**(n//2))) for n in (4,6,8)})


if __name__ == '__main__':
    verify()
