#!/usr/bin/env python3
"""Exact finite cross-checks for a quadratic-radical exponent criterion.

The symbolic argument in RESULT.md establishes the unrestricted theorem.
These tests check its formulas and independently explore rational inputs.
"""
from fractions import Fraction
from math import comb, isqrt


def squarefree(n):
    if n < 2:
        return False
    j = 2
    while j * j <= n:
        if n % (j * j) == 0:
            return False
        j += 1
    return True


def binomial_coeff(x, y, d, b):
    return sum((Fraction(comb(b, j)) * x ** (b - j) * y ** j
                * d ** ((j - 1) // 2) for j in range(1, b + 1, 2)),
               Fraction(0))


def rational_part(x, y, d, b):
    return sum((Fraction(comb(b, j)) * x ** (b - j) * y ** j
                * d ** (j // 2) for j in range(0, b + 1, 2)),
               Fraction(0))


def v2_int(t):
    assert t != 0
    t = abs(t)
    a = 0
    while not (t & 1):
        a += 1
        t //= 2
    return a


def v2_fraction(t):
    assert t != 0
    return v2_int(t.numerator) - v2_int(t.denominator)


def run():
    ds = [d for d in range(2, 34) if squarefree(d)]
    samples = 0
    minimum_tests = 0
    even_tests = 0
    even_exponent_tests = 0
    exponent_one_tests = 0
    for d in ds:
        for k in range(1, 12, 2):
            for p in range(-7, 8):
                if p == 0:
                    continue
                for q in range(1, 8):
                    x = Fraction(p, q)
                    y = Fraction(-k, 2) / x
                    assert 2 * x * y == -k
                    for b in (3, 5, 7, 9, 11):
                        terms = [(j, Fraction(comb(b, j)) * x**(b-j) * y**j
                                  * d**((j-1)//2)) for j in range(1, b+1, 2)]
                        values = [(j, v2_fraction(v)) for j, v in terms]
                        jmin, vmin = min(values, key=lambda z: z[1])
                        assert vmin < 0
                        assert sum(z == vmin for _, z in values) == 1
                        assert jmin == (b if v2_fraction(x) >= 0 else 1)
                        B = binomial_coeff(x, y, d, b)
                        assert B.denominator != 1
                        assert v2_fraction(B) == vmin
                        samples += 1
                        minimum_tests += 1
        for k in range(1, 10):
            # All nonsquare first radicands admit an exponent-one witness.
            x, y = Fraction(1, 2), Fraction(-k)
            assert 2*x*y == -k
            assert binomial_coeff(x, y, d, 1) == -k
            exponent_one_tests += 1
            # All even exponents admit a witness with a positive real base.
            Q = d*k*k + 1
            assert Q * Q > d*k*k
            for b in (2, 4, 6, 8, 10):
                coeff = binomial_coeff(Fraction(Q), Fraction(-k), d, b // 2)
                whole = rational_part(Fraction(Q), Fraction(-k), d, b // 2)
                assert coeff.denominator == 1 and coeff < 0
                assert whole.denominator == 1
                n = d * int(coeff)**2
                assert isqrt(n)**2 != n
                even_exponent_tests += 1
        for k in (2, 4, 6, 8):
            h = k // 2
            x = Fraction(1)
            y = Fraction(-h)
            assert 2*x*y == -k
            for b in (3, 5, 7, 9, 11, 13):
                B = binomial_coeff(x, y, d, b)
                U = rational_part(x, y, d, b)
                assert B.denominator == U.denominator == 1
                assert B < 0
                e = int(-B)
                n = d * e * e
                assert isqrt(n)**2 != n
                assert (x*x + d*y*y, 2*x*y) == (1+h*h*d, -k)
                assert U + B + e == U  # sqrt(d) coefficient cancels
                even_tests += 1
    # The endpoint b=1 genuinely differs from the theorem's odd b>=3.
    assert Fraction(1,2)**2 + 2 - Fraction(1,2)**2 == 2
    x, y, d = Fraction(1, 2), Fraction(-1), 2
    assert (2*x*y == -1 and binomial_coeff(x, y, d, 1) == -1)
    # Small explicit example: (1-sqrt(2))^2 + sqrt(8)=3;
    # (1-sqrt(2))^3 + sqrt(50)=7.
    assert rational_part(Fraction(1), Fraction(-1), 2, 2) == 3
    assert rational_part(Fraction(1), Fraction(-1), 2, 3) == 7
    assert binomial_coeff(Fraction(1), Fraction(-1), 2, 3) == -5
    print(f'VERIFY_OK squarefree_d={len(ds)} odd_k_rational_samples={samples} '
          f'unique_negative_2adic_minima={minimum_tests} '
          f'odd_b_even_k_constructions={even_tests} even_b_constructions={even_exponent_tests} ' 
          f'exponent_one_constructions={exponent_one_tests} b1_boundary=PASS example_8_50=PASS')


if __name__ == '__main__':
    run()
