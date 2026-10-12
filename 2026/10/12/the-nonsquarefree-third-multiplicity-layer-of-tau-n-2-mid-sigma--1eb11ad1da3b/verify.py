#!/usr/bin/env python3
from math import isqrt

CUBE_BOUND = 200_000
PAIR_BOUND = 5_000

def primes_up_to(n):
    isprime = bytearray(b"\x01") * (n + 1)
    isprime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if isprime[p]:
            isprime[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return [p for p in range(2, n + 1) if isprime[p]]

def cube_direct(p):
    tau = 4
    sigma = p**3 + p**2 + p + 1
    phi = p**2 * (p - 1)
    return (sigma + phi) % (tau * tau) == 0

def repeated_direct(p, q):
    tau = 6
    sigma = (p*p + p + 1) * (q + 1)
    phi = p * (p - 1) * (q - 1)
    return (sigma + phi) % (tau * tau) == 0

def repeated_predicted(p, q):
    if p == q:
        return False
    return (
        (p == 3 and q % 36 == 11)
        or (q == 3 and p % 18 == 13)
        or (p % 18 == 1 and q % 12 == 11)
    )

cube_primes = primes_up_to(CUBE_BOUND)
pair_primes = [p for p in cube_primes if p <= PAIR_BOUND]

cube_hits = []
for p in cube_primes:
    direct = cube_direct(p)
    predicted = (p % 16 == 5)
    assert direct == predicted, (p, direct, predicted)
    if direct:
        cube_hits.append(p)

pair_hits = []
pair_checks = 0
for p in pair_primes:
    for q in pair_primes:
        if p == q:
            continue
        pair_checks += 1
        direct = repeated_direct(p, q)
        predicted = repeated_predicted(p, q)
        assert direct == predicted, (p, q, direct, predicted)
        if direct:
            pair_hits.append((p*p*q, p, q))

pair_hits.sort()

assert cube_hits[:5] == [5, 37, 53, 101, 149], cube_hits[:5]
assert pair_hits[:9] == [
    (99, 3, 11),
    (423, 3, 47),
    (507, 13, 3),
    (747, 3, 83),
    (1719, 3, 191),
    (2043, 3, 227),
    (2367, 3, 263),
    (2883, 31, 3),
    (3971, 19, 11),
], pair_hits[:9]

print(
    "VERIFY_OK",
    f"cube_bound={CUBE_BOUND}",
    f"cube_primes={len(cube_primes)}",
    f"cube_hits={len(cube_hits)}",
    f"pair_bound={PAIR_BOUND}",
    f"pair_checks={pair_checks}",
    f"pair_hits={len(pair_hits)}",
    f"first_cube_primes={cube_hits[:8]}",
    f"first_repeated_hits={pair_hits[:9]}",
)
