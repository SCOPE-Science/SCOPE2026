#!/usr/bin/env python3
import bisect
import math

MAX_SIEVE = 10_000_000
PAIR_LIMIT = 2_000_000

def sieve_primes(n):
    a = bytearray(b"\x01") * (n + 1)
    a[:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if a[p]:
            a[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return a, [i for i in range(2, n + 1) if a[i]]

def beta(p):
    assert p % 2 == 1
    return 1 if p % 4 == 1 else -1

is_prime, primes = sieve_primes(MAX_SIEVE)

tested = 0
exceptional = 0
gcyclic = 0

pair_primes = primes[:bisect.bisect_right(primes, PAIR_LIMIT)]
for p in pair_primes:
    if p < 3:
        continue
    if p * p >= PAIR_LIMIT:
        break
    hi = bisect.bisect_right(pair_primes, PAIR_LIMIT // p)
    lo = bisect.bisect_right(pair_primes, p)
    for q in pair_primes[lo:hi]:
        phi_gauss = (p - beta(p)) * (q - beta(q))
        bad_gcd = math.gcd(p * q, phi_gauss) > 1
        bad_residue = (q - beta(q)) % p == 0
        assert bad_gcd == bad_residue, (p, q, phi_gauss)
        tested += 1
        if bad_gcd:
            exceptional += 1
        else:
            gcyclic += 1

assert tested == 328_564
assert exceptional == 45_757
assert gcyclic == 282_807

C_partial = 0.0
prime_count = 0
for p in primes:
    if p >= 3:
        C_partial += 1.0 / (p * (p - 1))
        prime_count += 1

tail_bound = 1.0 / MAX_SIEVE
lower = C_partial
upper = C_partial + tail_bound
assert 0.2731566631 < lower < 0.2731566633
assert 0.2731567631 < upper < 0.2731567633
assert round(lower, 6) == round(upper, 6) == 0.273157

print(
    "VERIFY_OK",
    f"semiprimes_tested={tested}",
    f"exceptions={exceptional}",
    f"gcyclic={gcyclic}",
    f"constant_primes={prime_count}",
    f"C_partial={C_partial:.16f}",
    f"C_upper={upper:.16f}",
    "six_decimals=0.273157",
)
