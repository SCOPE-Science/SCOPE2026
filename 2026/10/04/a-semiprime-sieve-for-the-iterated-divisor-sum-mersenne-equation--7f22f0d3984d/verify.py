#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt

LIMIT = 200_000
SPF_LIMIT = 400_000


def abundancy_prime_power(p, e):
    return Fraction(p ** (e + 1) - 1, p ** e * (p - 1))

# Exact odd-prime abundance obstructions.
assert abundancy_prime_power(2, 2) * abundancy_prime_power(3, 2) == Fraction(91, 36) > 2
assert abundancy_prime_power(2, 2) * abundancy_prime_power(5, 2) == Fraction(217, 100) > 2
assert abundancy_prime_power(2, 2) * abundancy_prime_power(7, 2) == Fraction(57, 28) > 2

# Exact power-of-two obstructions for p=3,7,31.
assert abundancy_prime_power(2, 3) == Fraction(15, 8) > Fraction(3, 2)
assert abundancy_prime_power(2, 4) == Fraction(31, 16) > Fraction(7, 4)
assert abundancy_prime_power(2, 6) == Fraction(127, 64) > Fraction(31, 16)

small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
covered = {}
for p in small_primes:
    if p in (3, 7, 31):
        covered[p] = 'two-adic'
    else:
        ds = [ell for ell in (3, 5, 7) if (p + 1) % ell == 0]
        assert ds
        covered[p] = tuple(ds)
assert set(covered) == set(small_primes)

# Smallest-prime-factor table for exact finite corroboration.
spf = list(range(SPF_LIMIT + 1))
spf[1] = 1
for p in range(2, isqrt(SPF_LIMIT) + 1):
    if spf[p] == p:
        for m in range(p * p, SPF_LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p


def factor(n):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def omega(n):
    return sum(factor(n).values()) if n > 1 else 0


def sigma(n):
    ans = 1
    for p, a in factor(n).items():
        ans *= (p ** (a + 1) - 1) // (p - 1)
    return ans

# Corroborate the parity criterion on a finite interval.
for n in range(1, 10_001):
    odd_sigma = sigma(n) % 2 == 1
    r = isqrt(n)
    square = r * r == n
    twice_square = n % 2 == 0 and isqrt(n // 2) ** 2 == n // 2
    assert odd_sigma == (square or twice_square), n

hits = []
composite_hits = []
max_sigma = 0
for n in range(2, LIMIT + 1):
    if omega(n) <= 2:
        s = sigma(n)
        max_sigma = max(max_sigma, s)
        assert s <= SPF_LIMIT, (n, s)
        if sigma(s) == 2 * n + 1:
            hits.append(n)
            if spf[n] != n:
                composite_hits.append(n)

expected = [3, 7, 31, 127, 8191, 131071]
assert hits == expected, hits
assert composite_hits == [], composite_hits
print('VERIFY_OK', f'limit={LIMIT}', f'max_sigma={max_sigma}', f'hits={hits}', 'composite_hits=0', f'small_prime_sieve={covered}')
