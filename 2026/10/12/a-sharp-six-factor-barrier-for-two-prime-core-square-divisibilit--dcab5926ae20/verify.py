#!/usr/bin/env python3
from math import isqrt

PRIME_LIMIT = 5000

def sieve(n):
    isprime = bytearray(b"\x01") * (n + 1)
    isprime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if isprime[p]:
            isprime[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return [p for p in range(2, n + 1) if isprime[p]]

def sigma_pp(p, a):
    return (p ** (a + 1) - 1) // (p - 1)

primes = sieve(PRIME_LIMIT)

tested = 0
hits = []
for i, p in enumerate(primes):
    for q in primes[i+1:]:
        for a in range(1, 5):
            for b in range(1, 5):
                if a + b > 5:
                    continue
                tested += 1
                sig = sigma_pp(p, a) * sigma_pp(q, b)
                if sig % (p*p*q*q) == 0:
                    hits.append((p, q, a, b))

assert hits == [], hits

# Universal-proof inequality checks on representative primes.
ineq_checks = 0
for p in primes:
    if p >= 3:
        assert (p*p - 1)**2 > sigma_pp(p, 3)
        ineq_checks += 1
    assert sigma_pp(p, 4) < (2*p*p - 1)**2
    ineq_checks += 1

# Sharpness.
n = 2**5 * 3
gamma2 = (2*3)**2
sig96 = sigma_pp(2, 5) * sigma_pp(3, 1)
assert n == 96
assert gamma2 == 36
assert sig96 == 252
assert sig96 % gamma2 == 0
assert 5 + 1 == 6

print(
    "VERIFY_OK",
    f"prime_limit={PRIME_LIMIT}",
    f"low_multiplicity_cases={tested}",
    f"hits={hits}",
    f"inequality_checks={ineq_checks}",
    "sharpness_n=96",
    "sharpness_quotient=7",
)
