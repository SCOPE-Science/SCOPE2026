#!/usr/bin/env python3
"""Exact rational checks for the affine-derangement prime-square theorem.

Only standard-library arithmetic is used.  These tests illustrate the proof;
finite tests are not a proof of the asserted identity for all primes.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


@lru_cache(maxsize=None)
def cot_power_sum(q, even_power):
    """Sum of cot(pi*r/q)**even_power for 1 <= r < q, by Newton sums."""
    assert q >= 1 and even_power > 0 and even_power % 2 == 0
    degree = q - 1
    coeff = [Fraction(0) for _ in range(degree + 1)]
    for j in range(2, degree + 1, 2):
        coeff[j] = (-1) ** (j // 2) * Fraction(comb(q, j + 1), q)
    sums = [Fraction(0) for _ in range(even_power + 1)]
    for k in range(2, even_power + 1, 2):
        val = -k * coeff[k] if k <= degree else Fraction(0)
        for j in range(2, min(k - 2, degree) + 1, 2):
            val -= coeff[j] * sums[k - j]
        sums[k] = val
    return sums[even_power]


@lru_cache(maxsize=None)
def alternating_cotangent_sum(even_n):
    """C_n = sum (-1)^r (i*cot(pi*r/n))**n, exactly rational."""
    assert even_n > 0 and even_n % 2 == 0
    half = even_n // 2
    return (-1) ** half * (
        2 * cot_power_sum(half, even_n) - cot_power_sum(even_n, even_n)
    )


def prime_square_affine_sum(p):
    """S_(2p^2) from an affine-derangement divisor decomposition."""
    assert p >= 5 and is_prime(p)
    return alternating_cotangent_sum(2*p*p) + p*(p-1)*alternating_cotangent_sum(2*p)


def prime_square_cyclotomic_sum(p):
    """Independent exact root-polynomial Newton recurrence for C_(2p^2)."""
    m = p*p
    power = 2*m
    # The roots of F_m(X) = ((X+1)^m-(X-1)^m)/(2m)
    # are the alpha=(1+omega)/(1-omega), omega^m=1, omega!=1.
    # Roots of G_m(X)=((X+1)^m+(X-1)^m)/2
    # represent odd-exponent cotangent contributions.
    def power_sums(coefficients, k):
        degree = len(coefficients) - 1
        out = [Fraction(0)]*(k+1)
        for i in range(1, k+1):
            total = i*coefficients[i] if i <= degree else Fraction(0)
            total += sum((coefficients[j]*out[i-j]
                          for j in range(1, min(i-1, degree)+1)), Fraction(0))
            out[i] = -total
        return out[k]
    # Reverse coefficients for monic polynomials: leading coefficient omitted
    f = [Fraction(1)] + [Fraction(comb(m,j+1),m) if j%2==0 else Fraction(0)
                         for j in range(1,m)]
    # For odd m, G_m is monic and has coefficients binom(m,j) for j even.
    g = [Fraction(1)] + [Fraction(comb(m,j)) if j%2==0 else Fraction(0)
                         for j in range(1,m+1)]
    return power_sums(f,power)-power_sums(g,power)


def main():
    records = []
    for p in (5,7,11,13,17):
        s = prime_square_affine_sum(p)
        expected = p ** (2*p)
        assert s.denominator == expected, (p, s.denominator, expected)
        scaled = s * expected
        assert scaled.denominator == 1
        expected_residue = (-2 * pow(3, -1, p)) % p
        assert scaled.numerator % p == expected_residue
        assert prime_square_cyclotomic_sum(p) == alternating_cotangent_sum(2*p*p)
        records.append((p,2*p*p,2*p,expected_residue))
    for p,n,exponent,residue in records:
        print(f'p={p} modulus={n} denominator={p}^{exponent} '
              f'scaled_numerator_mod_p={residue}')
    print(f'CERTIFICATE_OK prime_cases={len(records)} '
          'exact_newton_methods=2')


if __name__ == '__main__':
    main()
