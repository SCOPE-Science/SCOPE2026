#!/usr/bin/env python3
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def primes_upto(n):
    return [q for q in range(2, n + 1) if is_prime(q)]

def vp_factorial(n, p):
    e = 0
    while n:
        n //= p
        e += n
    return e

def squarefree_kernel_factorial(n):
    out = 1
    for p in primes_upto(n):
        if vp_factorial(n, p) % 2:
            out *= p
    return out

expected = [1, 2, 6, 6, 30, 5, 35, 70, 70, 7]
actual = [squarefree_kernel_factorial(c) for c in range(1, 11)]
assert actual == expected, (actual, expected)
prime_cases = [(c, squarefree_kernel_factorial(c)) for c in range(1, 51)
               if is_prime(squarefree_kernel_factorial(c))]
assert prime_cases == [(2, 2), (6, 5), (10, 7)], prime_cases
for c in range(11, 51):
    interval = [q for q in primes_upto(c) if 2 * q > c]
    assert len(interval) >= 2, (c, interval)
    for q in interval:
        assert vp_factorial(c, q) == 1, (c, q, vp_factorial(c, q))
print('VERIFY_OK prime_cases=2:2,6:5,10:7 two_interval_primes_c=11..50')
