#!/usr/bin/env python3
from math import isqrt

LIMIT = 5000

def primes_upto(n):
    a = bytearray(b"\x01") * n
    a[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n - 1) + 1):
        if a[p]:
            a[p*p:n:p] = b"\x00" * (((n - 1 - p*p) // p) + 1)
    return [i for i in range(2, n) if a[i]]

primes = primes_upto(LIMIT)
pair_checks = 0
direct_hits = []
param_hits = []

for i, p in enumerate(primes):
    K = (p - 1) * (p + 2)
    for q in primes[i + 1:]:
        d = p + q + 1
        direct = ((p - 1) * (q - 1)) % d == 0
        param = K % d == 0
        assert direct == param, (p, q, d, direct, param)
        pair_checks += 1
        if direct:
            direct_hits.append((p, q))
        if param:
            param_hits.append((p, q))

assert direct_hits == param_hits

square_checks = 0
for p in primes:
    assert (p * (p - 1)) % (p + 1) != 0
    square_checks += 1

examples = [133, 403, 583, 713, 817]
example_factors = [(7,19),(13,31),(11,53),(23,31),(19,43)]
for n, (p, q) in zip(examples, example_factors):
    assert p * q == n
    s = 1 + p + q
    phi = (p - 1) * (q - 1)
    assert phi % s == 0
    assert ((p - 1) * (p + 2)) % s == 0

print(
    "VERIFY_OK",
    f"prime_limit={LIMIT}",
    f"pair_checks={pair_checks}",
    f"semiprime_hits={len(direct_hits)}",
    f"square_checks={square_checks}",
    f"first_hits={direct_hits[:10]}",
)
