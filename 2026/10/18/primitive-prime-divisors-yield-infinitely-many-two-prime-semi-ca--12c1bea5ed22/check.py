#!/usr/bin/env python3
"""Finite reproducibility checks for semiprime congruences (standard library only).

The infinite result uses the classical primitive-divisor theorem, not these checks.
"""
from math import isqrt


def prime_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def order_mod(a, q):
    if a % q == 0:
        return None
    v = 1
    for k in range(1, q):
        v = v * a % q
        if v == 1:
            return k
    raise AssertionError("multiplicative order not found")


def semiprime_condition(p, q):
    n = p * q
    return pow(p, n, n) == p and pow(q, n, n) == q


def reduced_condition(p, q):
    return pow(p, p - 1, q) == 1 and pow(q, q - 1, p) == 1


witnesses = [(5, 13), (7, 43), (11, 13421), (13, 28393),
             (17, 18913), (19, 199), (29, 427822081)]
for p, q in witnesses:
    assert prime_trial(p) and prime_trial(q) and p < q
    assert order_mod(p, q) == p - 1
    assert (q - 1) % (p - 1) == 0
    assert reduced_condition(p, q)
    assert semiprime_condition(p, q)
    print(f"primitive-divisor example: p={p}, q={q}, pq={p*q}, order={p-1}: PASS")

B = 100000
sieve = bytearray(b'\x01') * (B + 1)
sieve[:2] = b'\x00\x00'
for d in range(2, isqrt(B) + 1):
    if sieve[d]:
        sieve[d*d:B+1:d] = b'\x00' * ((B - d*d)//d + 1)
primes = [p for p in range(2, B + 1) if sieve[p]]
first16 = [65, 133, 301, 793, 2041, 2413, 2501, 2701, 3781,
           4699, 5617, 5963, 7081, 7991, 9073, 9881]
actual = []
checks = 0
for p in primes:
    if p*p > B:
        break
    for q in primes:
        if q <= p:
            continue
        if p*q > B:
            break
        checks += 1
        a = semiprime_condition(p, q)
        b = reduced_condition(p, q)
        assert a == b, (p, q, a, b)
        if a:
            n = p*q
            assert all(pow(d, n, n) == d % n for d in (1, p, q, n))
            actual.append(n)
actual.sort()
assert actual[:16] == first16, (actual[:16], first16)
print(f"all {checks} distinct semiprimes pq <= {B}: direct and reduced tests AGREE")
print(f"first 16 values match the listed reference values: {actual[:16]}")
print(f"total eligible semiprimes <= {B}: {len(actual)}")
print("ALL FINITE CHECKS PASSED")
