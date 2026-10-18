#!/usr/bin/env python3
"""Exact-arithmetic checks for the sixth Schemmel-iterate sum on prime powers.

This is a finite check of a proved classification, not a replacement for its proof.
Runs with Python 3 and no third-party packages.
"""
from math import gcd

BOUND = 1000
MAX_EXPONENT = 8


def primes_upto(n):
    isprime = [True] * (n + 1)
    isprime[:2] = [False, False]
    for d in range(2, int(n**0.5) + 1):
        if isprime[d]:
            for k in range(d*d, n+1, d):
                isprime[k] = False
    return [p for p in range(n+1) if isprime[p]]


PRIMES = primes_upto(BOUND)


def schemmel6(n):
    """The multiplicative function L_6, from the prime-power formula."""
    if n <= 1:
        return n
    rest, result = n, 1
    for p in PRIMES:
        if p*p > rest:
            break
        if rest % p:
            continue
        power = 1
        rest //= p
        while rest % p == 0:
            rest //= p
            power *= p
        if p <= 6:
            return 0
        result *= power * (p - 6)
    if rest > 1:
        if rest > BOUND:
            raise ValueError("A factor outside the proven check bound")
        if rest <= 6:
            return 0
        result *= rest - 6
    return result


def iterate_sum(n):
    result = 0
    while n > 1:
        new_n = schemmel6(n)
        assert 0 <= new_n < n
        n = new_n
        result += n
    return result


def predicted_abundant(p, a):
    return (p == 19 and a == 1) or (p >= 23 and p != 83 and gcd(p - 6, 15) == 1)


def test():
    tested = abundant = deficient = 0
    for p in PRIMES:
        for a in range(1, MAX_EXPONENT + 1):
            n = p**a
            s = iterate_sum(n)
            assert s != n, (p, a, s)
            assert (s > n) == predicted_abundant(p, a), (p, a, s)
            tested += 1
            abundant += s > n
            deficient += s < n
    for a in range(1, 26):
        n = 19**a
        s = iterate_sum(n)
        assert 18*s == 325*19**(a-1) + 53, (a, s)
    for a in range(2, 20):
        n = 83**a
        s = iterate_sum(n)
        assert s == 77*83**(a-1) + 385*83**(a-2), (a, s)
    assert iterate_sum(19) == 21
    assert iterate_sum(19**2) == 346
    assert iterate_sum(83) == 82
    assert iterate_sum(83**2) == 6776
    print("checked primes <=", BOUND, "exponents 1..", MAX_EXPONENT)
    print("prime-power checks", tested, "abundant", abundant, "deficient", deficient, "perfect 0")
    print("19 and 83 exceptional formulas: exact arithmetic PASS")


if __name__ == "__main__":
    test()
