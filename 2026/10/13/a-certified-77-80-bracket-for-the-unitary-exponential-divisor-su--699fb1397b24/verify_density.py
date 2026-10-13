#!/usr/bin/env python3
"""Exact certificate for a two-sided divisor-function density bracket.

Runs with Python's standard library. Every finite comparison and final
threshold test uses integer or Fraction arithmetic. The infinite
steps (Euler products and Markov's inequality) are proved in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import prod

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
CAPS = (12, 9, 6, 4, 3, 3, 2, 2, 2, 2)
MARKOV_NUM, MARKOV_DEN = 29, 4000
ROUND_DEN = 10**6
EXPECTED_GOOD = 2060396086464126833643545810150335261409280
EXPECTED_NEG = 593415378686113363806646633931531172741120
EXPECTED_MARKOV_SUM = 57538357810785019098554221682665403810192916480
EXPECTED_COUNT_GOOD = 2096262
EXPECTED_COUNT_EQUAL = 6
EXPECTED_COEFFICIENT = Fraction(
    2016299456056220800244533835602991,
    265252859812191058636308480000000,
)
EXPECTED_UPPER = Fraction(
    17145880455178697494282924151970863011,
    21479832291515325918007548199218750000,
)


def primes_up_to(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b'\x00' * ((limit-p*p)//p + 1)
    return [p for p in range(2, limit+1) if sieve[p]]


def local_factors(p, cap):
    result = []
    for a in range(cap+1):
        if a == 0:
            numerator, denominator = 1, 1
        elif a == 1:
            numerator, denominator = p+1, p
        else:
            numerator = p**a + 1
            denominator = sum(p**d for d in range(1, a+1) if a % d == 0)
        # Density of v_p(n)=a equals (p-1)/p^(a+1).
        # All densities have the common denominator p^(cap+1).
        weight = (p-1) * p**(cap-a)
        result.append((numerator, denominator, weight))
    return result


def certificate():
    assert PRIMES == tuple(primes_up_to(29))
    local = [local_factors(p, cap) for p, cap in zip(PRIMES, CAPS)]
    common_den = prod(p**(cap+1) for p, cap in zip(PRIMES, CAPS))
    wgood = wnegative = wsum_markov = equality_count = good_count = 0
    mass = 0
    for vals in product(*local):
        a, b, c, d, e, f, g, h, i, j = vals
        numerator = a[0]*b[0]*c[0]*d[0]*e[0]*f[0]*g[0]*h[0]*i[0]*j[0]
        denominator = a[1]*b[1]*c[1]*d[1]*e[1]*f[1]*g[1]*h[1]*i[1]*j[1]
        weight = a[2]*b[2]*c[2]*d[2]*e[2]*f[2]*g[2]*h[2]*i[2]*j[2]
        mass += weight
        if numerator >= denominator:
            wgood += weight
            good_count += 1
            if numerator == denominator:
                equality_count += 1
        else:
            wnegative += weight
            # Let R=numerator/denominator<1. If the full ratio is >1,
            # the tail sum T must exceed 1-R. Markov gives upper
            # conditional probability min(1, mu/(1-R)), mu<29/4000.
            # Upward-round this rational number onto multiples of 1/10^6.
            x = ROUND_DEN * MARKOV_NUM * denominator
            y = MARKOV_DEN * (denominator-numerator)
            upper_integer = min(ROUND_DEN, (x+y-1)//y)
            wsum_markov += weight * upper_integer
    assert (wgood, wnegative, wsum_markov) == (
        EXPECTED_GOOD, EXPECTED_NEG, EXPECTED_MARKOV_SUM)
    assert (good_count, equality_count) == (EXPECTED_COUNT_GOOD, EXPECTED_COUNT_EQUAL)
    assert mass == wgood+wnegative
    assert Fraction(mass, common_den) == prod(
        (1-Fraction(1,p**(cap+1)) for p,cap in zip(PRIMES,CAPS)),
        start=Fraction(1,1),
    )

    # Upper bound for sum_(q>29 prime) 1/q^2: exact sieve and an
    # integer-ceiling rational majorant for each prime through 100000.
    primes = primes_up_to(100000)
    assert len(primes) == 9592
    scale = 10**10
    sieve_ceiling = sum((scale+p*p-1)//(p*p) for p in primes if p>29)
    tail_ceiling = scale // 100000  # sum_(m>100000) 1/m^2 < 1/100000
    assert (sieve_ceiling, tail_ceiling) == (72365244, 100000)
    assert sieve_ceiling+tail_ceiling < MARKOV_NUM*scale//MARKOV_DEN

    coefficient = Fraction(6*wgood, common_den)
    for p in PRIMES:
        coefficient /= 1-Fraction(1,p*p)
    upper = 1 - Fraction(ROUND_DEN*wnegative-wsum_markov,
                         ROUND_DEN*common_den)
    assert coefficient == EXPECTED_COEFFICIENT
    assert upper == EXPECTED_UPPER

    # Elementary rational proof of pi^2 < 987/100 using Machin's
    # identity pi=16 atan(1/5)-4 atan(1/239) and alternating series.
    def atan_partial(z, terms):
        return sum(((-1)**k*z**(2*k+1)/Fraction(2*k+1)
                    for k in range(terms)), Fraction())
    pi_upper = 16*atan_partial(Fraction(1,5),5) - 4*atan_partial(Fraction(1,239),2)
    assert pi_upper**2 < Fraction(987,100)
    lower_rational = coefficient/Fraction(987,100)
    assert lower_rational > Fraction(77,100)
    assert upper < Fraction(4,5)
    return {
        'patterns':prod(cap+1 for cap in CAPS),
        'good_patterns':good_count,
        'equal_patterns':equality_count,
        'coefficient_of_inverse_pi_squared':coefficient,
        'rational_lower':lower_rational,
        'rational_upper':upper,
    }

if __name__ == '__main__':
    ans=certificate()
    print('EXACT_CERTIFICATE_OK')
    for key,value in ans.items():
        print(f'{key}={value}')
