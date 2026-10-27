#!/usr/bin/env python3
"""Standalone arithmetic witness checks for prefix-free divisor constructions.

Finite witnesses illustrate the infinite proof; they do not establish the prime-number theorem.
Uses only the Python standard library.
"""
import math
from itertools import combinations


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    t = 3
    while t * t <= n:
        if n % t == 0:
            return False
        t += 2
    return True


def next_prime(n):
    while not is_prime(n):
        n += 1
    return n


def digits(n, base):
    out = []
    while n:
        out.append(n % base)
        n //= base
    return tuple(reversed(out))


def check_case(base, r, L, ell):
    g = 0
    a = base
    q = 2
    while q * q <= a:
        if a % q == 0:
            e = 0
            while a % q == 0:
                a //= q
                e += 1
            g = math.gcd(g, e)
        q += 1
    if a > 1:
        g = math.gcd(g, 1)
    assert is_prime(ell) and ell >= 3 and g % ell != 0
    primes = [next_prime(round(base ** (L + ell ** (-i))))
              for i in range(1, r + 1)]
    assert len(set(primes)) == r and all(is_prime(p) for p in primes)
    vals = [math.prod(primes[j] for j in range(r) if mask >> j & 1)
            for mask in range(1, 1 << r)]
    assert len(vals) == len(set(vals)) == (1 << r) - 1
    words = [digits(v, base) for v in vals]
    assert all(not u[:len(v)] == v and not v[:len(u)] == u
               for i, u in enumerate(words) for v in words[i + 1:])
    K = next(k for k in range(1, min(map(len, words)) + 1)
             if len({w[:k] for w in words}) == len(words))
    assert min(map(len, words)) >= K
    print('base', base, 'r', r, 'L', L, 'ell', ell,
          'prefix_length', K, 'divisors', len(vals),
          'prime_factors', ','.join(map(str, primes)))


if __name__ == '__main__':
    for case in [(2, 7, 26, 3), (3, 6, 16, 3), (5, 6, 12, 3),
                 (8, 5, 9, 5), (10, 5, 10, 3)]:
        check_case(*case)
    print('VERIFY_OK')
