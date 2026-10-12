#!/usr/bin/env python3
from math import isqrt
from bisect import bisect_right

LIMIT = 2_000_000

isprime = bytearray(b"\x01") * (LIMIT + 1)
isprime[0:2] = b"\x00\x00"
for p in range(2, isqrt(LIMIT) + 1):
    if isprime[p]:
        isprime[p*p:LIMIT+1:p] = b"\x00" * (((LIMIT - p*p) // p) + 1)

primes = [p for p in range(2, LIMIT + 1) if isprime[p]]

square_checks = 0
pair_checks = 0
hits = []

for p in primes:
    if p*p > LIMIT:
        break
    square_checks += 1
    difference = 2*p + 1
    summation = 2*p*p + 1
    assert summation % difference != 0

for i, p in enumerate(primes):
    if p*p > LIMIT:
        break
    max_q = LIMIT // p
    stop = bisect_right(primes, max_q)
    for q in primes[i+1:stop]:
        pair_checks += 1

        difference = 2*(p + q)
        summation = 2*(p*q + 1)
        direct = (summation % difference == 0)

        divisor_form = ((p*p - 1) % (p + q) == 0)
        assert direct == divisor_form, (p, q, direct, divisor_form)

        if direct:
            k = (p*q + 1) // (p + q)
            assert 2 <= k < p
            a = p - k
            b = q - k
            assert a > 0 and a < b
            assert a*b == k*k - 1
            assert (p*p - 1) == (p + q) * a

            # Converse reconstruction from the quotient fiber.
            pp = k + a
            qq = k + b
            assert pp == p and qq == q
            assert pp*qq + 1 == k*(pp + qq)

            hits.append(p*q)

hits.sort()
assert hits[:10] == [15, 35, 95, 119, 143, 209, 287, 319, 323, 377], hits[:12]

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"square_checks={square_checks}",
    f"pair_checks={pair_checks}",
    f"hits={len(hits)}",
    f"first_hits={hits[:15]}",
)
