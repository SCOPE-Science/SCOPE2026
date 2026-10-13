#!/usr/bin/env python3
from math import factorial, isqrt


def primes_upto(n):
    if n < 2:
        return []
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n-p*p)//p)+1)
    return [p for p in range(2, n+1) if sieve[p]]


def squarefree_part_factorial(c):
    r = 1
    for p in primes_upto(c):
        e = 0
        q = c
        while q:
            q //= p
            e += q
        if e & 1:
            r *= p
    return r


def squarefree_part(n):
    r = 1
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e & 1:
            r *= p
        p += 1
    if n > 1:
        r *= n
    return r

# Exact finite part of the proof: c=12,...,49.
for c in range(12, 50):
    s = squarefree_part_factorial(c)
    assert s > c*c, (c, s, c*c)
assert squarefree_part_factorial(11) == 77 < 121
assert squarefree_part_factorial(12) == 231 > 144

# Exact small-prime exclusions.
witnesses = {2: 2, 3: 3, 5: 6, 7: 7, 11: 11}
for p, c in witnesses.items():
    assert squarefree_part(p * factorial(c)) < p, (p, c)

# Finite stress test of the prime classification well beyond the proof threshold.
ps = primes_upto(401)
for p in ps:
    predicted = p >= 13
    observed = True
    for c in range(0, 501):
        sc = squarefree_part_factorial(c)
        # Since p is prime and sc is squarefree, toggling p gives s(p*c!).
        spc = sc // p if sc % p == 0 else p * sc
        if spc < p:
            observed = False
            break
    assert observed == predicted, (p, observed, c)

print('VERIFY_OK finite_tail=38 small_prime_witnesses=5 prime_stress=%d c_max=500 threshold_11_12=77,231' % len(ps))
