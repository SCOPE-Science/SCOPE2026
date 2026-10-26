"""Exact finite corroboration of elementary identities in the accompanying proof.

This script is not a proof of a universal or primality assertion.
"""
from fractions import Fraction
from math import gcd

LIMIT = 120000
spf = list(range(LIMIT + 1))
for p in range(2, int(LIMIT ** .5) + 1):
    if spf[p] == p:
        for n in range(p * p, LIMIT + 1, p):
            if spf[n] == n:
                spf[n] = p

def distinct_primes(n):
    a = []
    while n > 1:
        p = spf[n]
        a.append(p)
        while n % p == 0:
            n //= p
    return a

def deriv_squarefree(primes):
    n = 1
    for p in primes: n *= p
    return sum(n // p for p in primes)

# Source of the support classification: exact reciprocal inequalities.
assert sum([Fraction(1,p) for p in [2,3,5,7]]) == Fraction(247,210)
for ps in ([2,3,7], [2,5,7,11], [2,3,13,17], [2,3,11,17]):
    assert sum((Fraction(1,p) for p in ps),Fraction(0)) < 1
assert deriv_squarefree([2,3,5]) - 30 == 1
assert deriv_squarefree([2,3,11,13]) - 858 == 1

count = 0
positive4 = 0
for a in range(2, LIMIT + 1):
    primes = distinct_primes(a)
    radical = 1
    for p in primes: radical *= p
    if len(primes) > 4 or a != radical:
        continue
    delta = deriv_squarefree(primes) - a
    if delta <= 0:
        continue
    if len(primes) <= 3:
        assert primes == [2,3,5] and delta == 1
    if len(primes) == 4:
        positive4 += 1
        assert primes[:2] == [2,3]
        if primes[2] == 5:
            assert delta == primes[3] + 30
        elif primes[2] == 7:
            assert primes[3] < 42 and delta == 42 - primes[3]
        else:
            assert primes == [2,3,11,13] and delta == 1
        for q in [2,3,5,7]:
            if gcd(a,q) == 1 and delta == q**q:
                assert primes == [2,3,5,q**q-30]
    count += 1

# Independently check the local candidate arithmetic (not primality in general).
assert 7**7 - 30 == 29*73*389
assert 11**11 - 30 == 7*67*83*7329403
print('VERIFY_OK', 'squarefree_positive_surpluses', count,
      'four-prime_positive_surpluses', positive4,
      'search_limit', LIMIT)
