#!/usr/bin/env python3
import math
MAX_N = 100000
isprime = bytearray(b"\x01") * (MAX_N + 1)
isprime[:2] = b"\x00\x00"
for p in range(2, math.isqrt(MAX_N) + 1):
    if isprime[p]:
        start = p * p
        isprime[start:MAX_N+1:p] = b"\x00" * (((MAX_N - start) // p) + 1)

def G(n):
    total = 0
    k = 1
    while k <= n:
        q = n // k
        if isprime[q]:
            total += 1
        k = n // q + 1
    return total

def largest_prime_factor(n):
    x = n
    ans = 1
    while x % 2 == 0:
        ans = 2
        x //= 2
    p = 3
    while p * p <= x:
        while x % p == 0:
            ans = p
            x //= p
        p += 2
    if x > 1:
        ans = max(ans, x)
    return ans

odd_count = 0
for n in range(5, MAX_N + 1, 2):
    odd_count += 1
    P = largest_prime_factor(n)
    predicted = 1 if P * P >= n else 0
    actual = G(n) - G(n - 1)
    assert actual == predicted, (n, actual, predicted, P)

primes = [p for p in range(3, MAX_N + 1, 2) if isprime[p]]
triple_count = 0
for i, p1 in enumerate(primes):
    if p1 * p1 * p1 > MAX_N:
        break
    for j in range(i + 1, len(primes)):
        p2 = primes[j]
        if p1 * p2 * p2 > MAX_N:
            break
        for k in range(j + 1, len(primes)):
            p3 = primes[k]
            n = p1 * p2 * p3
            if n > MAX_N:
                break
            triple_count += 1
            predicted = 1 if p3 > p1 * p2 else 0
            actual = G(n) - G(n - 1)
            assert actual == predicted, (n, p1, p2, p3, actual, predicted)

print(f"VERIFY_OK odd_n={odd_count} triple_cases={triple_count} max_n={MAX_N}")
