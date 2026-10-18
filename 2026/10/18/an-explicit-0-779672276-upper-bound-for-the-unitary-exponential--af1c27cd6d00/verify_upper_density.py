#!/usr/bin/env python3
"""Exact finite certificate for an upper density bound in divisor-sum comparison.

No third-party packages or input files are required. The integer comparisons
are exact; floating-point logarithms only seed an integer search, which is
subsequently adjusted and checked by integer inequalities.
"""
from fractions import Fraction
from math import ceil, log

BASE, DEN = 1001, 1000
B, N, SCALE = 5003, 100000, 10**15


def primes_to(limit):
    flags = bytearray(b'\x01') * (limit + 1)
    flags[0:2] = b'\x00\x00'
    for d in range(2, int(limit**0.5) + 1):
        if flags[d]:
            flags[d*d:limit+1:d] = b'\x00' * ((limit-d*d)//d+1)
    return [i for i in range(limit+1) if flags[i]]


def exponent_divisors(a):
    return [d for d in range(1, a+1) if a % d == 0]


def cap(p):
    return {2: 12, 3: 10, 5: 6, 7: 5, 11: 4,
            13: 3, 17: 3, 19: 3, 23: 3}.get(p, 2)


def ratio_le_power(numer, denom, k):
    """Return numer/denom <= (1001/1000)**k, using only integers."""
    if k >= 0:
        return numer * DEN**k <= denom * BASE**k
    return numer * BASE**(-k) <= denom * DEN**(-k)


def upper_score(p, a):
    if a == 0:
        return 0
    numerator = 1 + p**a
    denominator = sum(p**d for d in exponent_divisors(a))
    guess = ceil(log(numerator/denominator) / log(BASE / DEN))
    while not ratio_le_power(numerator, denominator, guess):
        guess += 1
    while ratio_le_power(numerator, denominator, guess - 1):
        guess -= 1
    assert ratio_le_power(numerator, denominator, guess)
    assert not ratio_le_power(numerator, denominator, guess - 1)
    return guess


def local_certificate(primes):
    """Exact weighted residues for all allowable local valuation vectors."""
    state = {0: 1}
    modulus = 1
    for p in primes:
        amax = cap(p)
        possibilities = [(upper_score(p, a), (p-1)*p**(amax-a))
                         for a in range(amax+1)]
        updated = {}
        for old_score, count in state.items():
            for score, multiplicity in possibilities:
                j = old_score + score
                updated[j] = updated.get(j, 0) + count*multiplicity
        state = updated
        modulus *= p**(amax+1)
    favorable = sum(n for score, n in state.items() if score <= -2)
    assert favorable * 50000 > 11023 * modulus
    assert sum(state.values()) <= modulus
    return favorable, modulus, len(state)


def tail_certificate(all_primes):
    tail_primes = [p for p in all_primes if B < p <= N]
    # Each ceiling is an integer upper bound on 10**15/p**k.
    ceil_second = sum((SCALE+p*p-1)//(p*p) for p in tail_primes)
    ceil_third = sum((SCALE+p**3-1)//(p**3) for p in tail_primes)
    mean_upper = Fraction(ceil_second, SCALE) + Fraction(1, N)
    variance_upper = Fraction(ceil_third, SCALE) + Fraction(1, 2*N*N)
    assert mean_upper < Fraction(31, 10**6)
    assert variance_upper < Fraction(23, 10**10)
    # log(1+t)>t/(1+t): hence 2log(1001/1000)>2/1001.
    risk_upper = Fraction(23, 10**10) / (
        Fraction(2, 1001) - Fraction(31, 10**6))**2
    assert risk_upper < Fraction(3, 5000)
    return len(tail_primes), ceil_second, ceil_third, risk_upper


def independent_small_check():
    """A finite regression check, not an infinite proof."""
    primes = primes_to(30000)
    tested = 0
    for n in range(2, 30001):
        m = n
        good = True
        score = 0
        numerator = denominator = 1
        upper_tail = Fraction(0)
        for p in primes:
            if p*p > m:
                break
            if m % p:
                continue
            a = 0
            while m % p == 0:
                m //= p
                a += 1
            numerator *= 1+p**a
            denominator *= sum(p**d for d in exponent_divisors(a))
            if p <= B:
                if a > cap(p):
                    good = False
                else:
                    score += upper_score(p, a)
            else:
                upper_tail += Fraction(1, p)
        if m > 1:
            p = m
            numerator *= p+1
            denominator *= p
            if p <= B:
                score += upper_score(p, 1)
            else:
                upper_tail += Fraction(1, p)
        # Tail threshold: 2log(1001/1000)>2/1001.
        if good and score <= -2 and upper_tail < Fraction(2, 1001):
            assert numerator < denominator
            tested += 1
    return tested


def main():
    primes = primes_to(N)
    numer, denom, states = local_certificate([p for p in primes if p <= B])
    count, second, third, risk = tail_certificate(primes)
    deficit = Fraction(11023, 50000) * (1-Fraction(3, 5000))
    assert deficit > Fraction(11, 50)
    regression = independent_small_check()
    assert regression > 0
    print('VERIFY_OK')
    print('small_primes=%d states=%d cylinder_mass=%.12f' %
          (sum(p <= B for p in primes), states, numer/denom))
    print('tail_primes=%d ceil_second=%d ceil_third=%d' %
          (count, second, third))
    print('chebyshev_risk_bound=%.12f' % float(risk))
    print('deficiency_lower=%s > 11/50' % str(deficit))
    print('finite_implication_cases=%d' % regression)
    print('CONCLUSION: upper_density_sigma_star_gt_sigma_e < 39/50')


if __name__ == '__main__':
    main()
