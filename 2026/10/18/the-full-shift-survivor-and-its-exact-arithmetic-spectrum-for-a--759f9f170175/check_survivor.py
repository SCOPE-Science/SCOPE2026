"""Exact checks for the M-adic survivor dynamics of the numerator map.

All checks use integer and rational arithmetic. The infinite-dimensional
Hausdorff-measure statement is proved analytically, not by these tests.
"""
from fractions import Fraction
from itertools import product
from math import gcd, prod


def unit_digits(modulus):
    return tuple(r for r in range(1, modulus) if gcd(r, modulus) == 1)


def step_int(numerator, modulus):
    quotient, residue = divmod(numerator, modulus)
    return quotient * (modulus + residue)


def direct_survivors(modulus, depth):
    result = []
    for first in range(modulus ** depth):
        numerator = first
        for _ in range(depth):
            if gcd(numerator, modulus) != 1:
                break
            numerator = step_int(numerator, modulus)
        else:
            result.append(first)
    return result


def p_adic_step_on_rationals(x, modulus):
    assert gcd(x.denominator, modulus) == 1
    r = (x.numerator * pow(x.denominator, -1, modulus)) % modulus
    assert gcd(r, modulus) == 1
    return ((x - r) / modulus) * (modulus + r), r


def word_fixed_point(modulus, word):
    slope = Fraction(1)
    intercept = Fraction(0)
    for r in reversed(word):
        c = Fraction(modulus, modulus + r)
        slope, intercept = c * slope, Fraction(r) + c * intercept
    x = intercept / (1 - slope)
    b = [modulus + r for r in word]
    denominator = prod(b) - modulus ** len(word)
    numerator = sum(r * modulus**j * prod(b[j:]) for j, r in enumerate(word))
    assert x == Fraction(numerator, denominator)
    assert gcd(denominator, modulus) == 1
    return x


def check():
    tests = 0
    for modulus, max_depth in [(2, 9), (3, 8), (4, 7), (5, 6),
                                (6, 6), (7, 6), (8, 6), (9, 5),
                                (10, 5), (11, 5), (12, 5)]:
        digits = unit_digits(modulus)
        for depth in range(1, max_depth + 1):
            observed = direct_survivors(modulus, depth)
            assert len(observed) == len(digits) ** depth
            tests += 1
        for depth in range(1, 5):
            points = []
            for word in product(digits, repeat=depth):
                x = word_fixed_point(modulus, word)
                assert Fraction(modulus) < x < Fraction(2 * modulus)
                y = x
                encountered = []
                for _ in range(depth):
                    y, r = p_adic_step_on_rationals(y, modulus)
                    encountered.append(r)
                assert y == x and tuple(encountered) == word
                points.append(x)
                tests += 1
            assert len(set(points)) == len(digits) ** depth
    # Explicit nonconstant two-cycle in the 3-adic completion.
    x = Fraction(50, 11)
    y, r1 = p_adic_step_on_rationals(x, 3)
    z, r2 = p_adic_step_on_rationals(y, 3)
    assert (y, z, r1, r2) == (Fraction(52, 11), x, 1, 2)
    print('PASS: exact survivor counts, rational periodic-point formulas,')
    print('branch itineraries and independent two-cycle check')
    print('Number of direct count and periodic-point checks:', tests)
    print('Moduli:', list(range(2, 13)))
    print('Period range: 1..4')


if __name__ == '__main__':
    check()
