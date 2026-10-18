#!/usr/bin/env python3
"""Exact Newton-sum checks for affine root-of-unity sums (stdlib only)."""
from functools import lru_cache
from fractions import Fraction
from math import comb

@lru_cache(None)
def cot_power_sum(modulus, exponent):
    """Sum of cot(pi*r/modulus)^exponent, 1<=r<modulus; exponent even."""
    assert modulus >= 2 and exponent >= 0 and exponent % 2 == 0
    degree = modulus - 1
    coefficients = {2*j: Fraction((-1)**j * comb(modulus, 2*j+1), modulus)
                    for j in range(1, (modulus-1)//2 + 1)}
    traces = [Fraction(degree)]
    for i in range(1, exponent+1):
        rhs = sum(coefficients[j]*traces[i-j]
                  for j in range(1, min(i-1, degree)+1)
                  if j in coefficients)
        if i <= degree and i in coefficients:
            rhs += i * coefficients[i]
        traces.append(-rhs)
    return traces[exponent]

@lru_cache(None)
def alternating_block(n):
    assert n % 2 == 0
    return (-1)**(n//2)*(2*cot_power_sum(n//2, n)-cot_power_sum(n, n))

def affine_sum_for_twice_prime_square(p):
    return alternating_block(2*p*p)+p*(p-1)*alternating_block(2*p)


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**.5)+1))


def prime_valuation_of_denominator(x, p):
    denominator = x.denominator
    order = 0
    while denominator % p == 0:
        denominator //= p
        order += 1
    return order, denominator

def run():
    assert alternating_block(6) == Fraction(1456, 27)
    assert alternating_block(10) == Fraction(762256, 5)
    assert alternating_block(14) == Fraction(13444304416, 7)
    for p in (5, 7, 11, 13, 17, 19):
        assert is_prime(p)
        block = alternating_block(2*p*p)
        total = affine_sum_for_twice_prime_square(p)
        assert total - block == p*(p-1)*alternating_block(2*p)
        exponent, cofactor = prime_valuation_of_denominator(total, p)
        assert (exponent, cofactor) == (2*p, 1), (p, exponent, cofactor)
        print('p=%d n=%d reduced_denominator=%d predicted=%d' %
              (p, 2*p*p, total.denominator, p**(2*p)))
    print('all_exact_checks_passed')

if __name__ == '__main__':
    run()
