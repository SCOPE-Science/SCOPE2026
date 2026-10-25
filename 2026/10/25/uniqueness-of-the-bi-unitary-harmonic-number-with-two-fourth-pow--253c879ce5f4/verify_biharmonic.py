#!/usr/bin/env python3
"""Exact, exhaustive prime-pattern verifier; Python 3 standard library only.

All loops are finite for mathematical reasons explained in the accompanying proof.
The integer/factor and interval checks use exact integer arithmetic.
"""
from fractions import Fraction
from math import isqrt


def sieve(limit):
    t = bytearray(b'\x01') * (limit + 1)
    t[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit) + 1):
        if t[d]:
            t[d*d::d] = b'\x00' * (((limit-d*d)//d)+1)
    return t, [i for i in range(2, limit+1) if t[i]]

PRIME_BOUND = 150000
ISPRIME, PRIME_LIST = sieve(PRIME_BOUND)
SMALL_PRIMES = [p for p in PRIME_LIST if p < 397]


def local_ratio(p, exponent):
    if exponent == 1:
        return Fraction(p, p+1)
    assert exponent == 4
    return Fraction(p**4, p**4+p**3+p+1)


def integer_in_half_open_interval(lower, upper):
    # Does [lower, upper) contain an integer? Both endpoints exact.
    ceil_lower = -(-lower.numerator // lower.denominator)
    ceil_upper = -(-upper.numerator // upper.denominator)
    return ceil_lower < ceil_upper


def prime_factors_with_complete_trial_certificate(n):
    original = n
    assert n > 0
    ans = set()
    for p in PRIME_LIST:
        if n == 1:
            break
        if n % p == 0:
            ans.add(p)
            while n % p == 0:
                n //= p
    # This assertion is a complete factorization certificate in the
    # exhaustively reached cases. No unexamined cofactor is permitted.
    assert n == 1, (original, n)
    return ans


def check():
    # For sorted distinct primes a<b<c, their exponent order is a
    # permutation of (4,4,1). Each factor is monotone increasing in p.
    # At a>=97 all three factors make H strictly between 31 and 32.
    assert 32 * local_ratio(97,1)*local_ratio(97,4)**2 > 31
    patterns=((1,4,4), (4,1,4), (4,4,1))
    first=[p for p in SMALL_PRIMES if p <= 89]
    second=[p for p in SMALL_PRIMES if p <= 389]
    assert len(first) == 24
    # If b>=397, for each a and pattern H lies in an integer-free
    # interval [U*g_e2(397)*g_e3(397), U), U=32*g_e1(a).
    cutoff_checks=0
    for pattern in patterns:
        e1,e2,e3=pattern
        for a in first:
            U=32*local_ratio(a,e1)
            L=U*local_ratio(397,e2)*local_ratio(397,e3)
            assert not integer_in_half_open_interval(L,U), (pattern,a)
            cutoff_checks+=1
    assert cutoff_checks==72

    pairs_considered=0; pairs_possible=0; target_levels=0
    candidates_tested=0; max_prime_factor=0; largest_denominator=0
    findings=[]
    for pattern in patterns:
        e1,e2,e3=pattern
        for a in first:
            U1=32*local_ratio(a,e1)
            for b in second:
                if b<=a: continue
                pairs_considered+=1
                if not integer_in_half_open_interval(
                    U1*local_ratio(b,e2)*local_ratio(b,e3),U1):
                    continue
                pairs_possible+=1
                U2=U1*local_ratio(b,e2)
                B=U2.denominator
                largest_denominator=max(largest_denominator,B)
                prime_factors_B=prime_factors_with_complete_trial_certificate(B)
                if prime_factors_B:
                    max_prime_factor=max(max_prime_factor,max(prime_factors_B))
                # H=h< U2. Modulo c, the identity
                # A*c^e3 = h*B*sigma**(c^e3) forces c | h*B.
                for h in range(1,-(-U2.numerator//U2.denominator)):
                    target_levels+=1
                    eligible=prime_factors_B | prime_factors_with_complete_trial_certificate(h)
                    for c in sorted(eligible):
                        if c<=b: continue
                        candidates_tested+=1
                        if U2*local_ratio(c,e3)==h:
                            n=a**e1*b**e2*c**e3
                            sigma=(a**4+a**3+a+1 if e1==4 else a+1)
                            sigma*=(b**4+b**3+b+1 if e2==4 else b+1)
                            sigma*=(c**4+c**3+c+1 if e3==4 else c+1)
                            assert 32*n==h*sigma
                            findings.append((n,h,a,b,c,pattern))
    assert findings==[(9072,12,2,3,7,(4,4,1))], findings
    print('VERIFY_OK')
    print('cutoff_checks',cutoff_checks,'first_primes',len(first),'max_first',first[-1],
          'max_second',second[-1])
    print('ordered_prime_pattern_pairs_tested',pairs_considered,
          'interval_feasible_pairs',pairs_possible, 'integer_levels',target_levels,
          'last_prime_candidates',candidates_tested)
    print('largest_reduced_denominator',largest_denominator,
          'largest_denominator_prime_factor',max_prime_factor)
    print('solutions',findings)

if __name__=='__main__':
    check()
