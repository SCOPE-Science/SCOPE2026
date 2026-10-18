#!/usr/bin/env python3
"""Exact arithmetic checks for the prime-minus-one gap distribution theorem.
No external packages, data files, or network access are required.
"""
from collections import Counter
from fractions import Fraction
from math import gcd

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]


def missing_prime(r):
    for p in PRIMES:
        if (r - 1) % p:
            return p
    raise AssertionError('extend the prime list')


def records_to(bound):
    result = []
    r = 3
    while r <= bound:
        q = missing_prime(r)
        result.append((r, q))
        r += q - 1
    return result


def check():
    rows = records_to(1_000_000)
    assert [r for r, q in rows[:12]] == [3,5,7,11,13,17,19,23,25,29,31,37]
    # An independent next-record definition: least larger coprime integer.
    r = 3
    for target, q in rows[:2500]:
        assert r == target
        v = r + 1
        while gcd(v, r - 1) != 1:
            v += 1
        assert v - r == q - 1
        r = v

    P = [1]
    for p in PRIMES:
        P.append(P[-1] * p)
    old = Counter(q for r, q in rows if PRIMES[3] <= r <= P[3] + 1)
    assert old == Counter({3:4, 5:4, 7:1})
    tested = 0
    for n in range(4, 8):
        c = Counter(q for r, q in rows if PRIMES[n] <= r <= P[n] + 1)
        s = Counter(q for r, q in rows if PRIMES[n-1] <= r < PRIMES[n])
        for q in PRIMES[1:]:
            predicted = (PRIMES[n-1]*old[q]-s[q]
                         -int(q == PRIMES[n-1])+int(q == PRIMES[n]))
            assert c[q] == predicted, (n, q, c[q], predicted)
            tested += 1
        old = c

    # Exact recurrence beyond enumerable primorials: the small correction
    # windows below the next prime are fully enumerated by rows.
    c = Counter({3:4, 5:4, 7:1})
    for n in range(4, 13):
        s = Counter(q for r,q in rows if PRIMES[n-1] <= r < PRIMES[n])
        c = Counter({q:PRIMES[n-1]*c[q]-s[q]
                     -int(q == PRIMES[n-1])+int(q == PRIMES[n])
                     for q in PRIMES[1:]})
    for q, num in [(3,986204740216),(5,953846993907),
                   (7,212021089529),(11,32124407510)]:
        assert c[q] == num
    assert sum(c.values()) == 2187409671913
    assert P[12] == 7420738134810
    # The exact rational plus/minus 4/P_12 is a rigorous interval,
    # conditional on the symbolic theorem's bounding lemma.
    print('RECURRENCE_OK', tested, 'INDEPENDENT_GREEDY_OK 2500')
    for q in (3,5,7,11):
        value=Fraction(c[q],P[12]); error=Fraction(4,P[12])
        print('prime',q,'numerator',c[q], 'denominator',P[12],
              'approx',format(float(value),'.15f'),
              'error_lt', format(float(error),'.3g'))
    print('VERIFICATION_OK')

if __name__ == '__main__':
    check()
