"""Exact finite checks for prime-power singleton-cofactor comparison counts."""
from bisect import bisect_right
from fractions import Fraction
from math import isqrt


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p::p] = b"\x00" * ((n - p * p) // p + 1)
    return [k for k in range(2, n + 1) if sieve[k]]


def proper_exponents(a):
    return [d for d in range(1, a) if a % d == 0]


def prime_bound(p, a):
    return p ** a + 1, sum(p ** d for d in proper_exponents(a)) - 1


def formula_count(P, a, x):
    c = 0
    for p in P:
        if 2 * p ** a > x:
            break
        h, delta = prime_bound(p, a)
        limit = min(x // p ** a, (h - 1) // delta)
        c += bisect_right(P, limit) - int(p <= limit)
    return c


def brute_count(P, a, x):
    c = 0
    for p in P:
        if 2 * p ** a > x:
            break
        h, delta = prime_bound(p, a)
        for q in P:
            if p ** a * q > x:
                break
            if q == p:
                continue
            unitary = (p ** a + 1) * (q + 1)
            exponential = q * sum(p ** d for d in proper_exponents(a) + [a])
            good = unitary > exponential
            assert good == (q * delta < h)
            c += int(good)
    return c


def run():
    P = primes_upto(250000)
    assert P[-1] >= 249989
    constants = {2: Fraction(27, 2), 3: Fraction(125, 12),
                 4: Fraction(12), 5: Fraction(729, 80),
                 6: Fraction(243, 20)}
    examples = {}
    for a in range(2, 7):
        d = max(proper_exponents(a))
        beta = a - d
        k = Fraction((a + beta) ** 2, beta) * (
            Fraction(1, beta + 1) + Fraction(1, a - 1))
        assert k == constants[a]
        assert beta >= 1
        for x in (10000, 100000, 1000000):
            assert formula_count(P, a, x) == brute_count(P, a, x)
        examples[a] = formula_count(P, a, 1000000)
    assert examples == {2: 861, 3: 261, 4: 63, 5: 124, 6: 28}, examples
    print('VERIFY_OK', 'exponents=2..6', 'X=10000,100000,1000000',
          'counts_at_1000000=' + repr(examples))


if __name__ == '__main__':
    run()
