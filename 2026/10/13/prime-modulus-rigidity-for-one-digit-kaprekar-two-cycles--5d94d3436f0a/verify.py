#!/usr/bin/env python3
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def kaprekar_step(x, b):
    q, r = divmod(x*x, b)
    return q + r

def direct_cycles(ell):
    b = ell + 1
    out = []
    for x in range(1, b):
        y = kaprekar_step(x, b)
        if 1 <= y < b and y != x and x < y and kaprekar_step(y, b) == x:
            out.append((x, y))
    return out

def predicted_cycles(ell):
    if ell % 3 != 1:
        return []
    roots = [
        z for z in range(2, ell)
        if (z*z + z + 1) % ell == 0
    ]
    assert len(roots) == 2
    u, v = sorted(roots)
    assert u + v == ell - 1
    inequality = u*u - (3*ell - 1)*u + (ell - 1)*(ell - 1)
    return [(u, v)] if inequality <= 0 else []

checked = 0
cycle_primes = []
for ell in range(2, 20000):
    if not is_prime(ell):
        continue
    got = direct_cycles(ell)
    want = predicted_cycles(ell)
    assert got == want, (ell, got, want)
    checked += 1
    if got:
        cycle_primes.append((ell, got[0]))

assert direct_cycles(7) == [(2, 4)]
assert direct_cycles(13) == []
assert direct_cycles(19) == [(7, 11)]
assert direct_cycles(67) == [(29, 37)]

assert cycle_primes[:8] == [
    (7, (2, 4)),
    (19, (7, 11)),
    (67, (29, 37)),
    (103, (46, 56)),
    (109, (45, 63)),
    (193, (84, 108)),
    (199, (92, 106)),
    (229, (94, 134)),
]

print(
    "VERIFY_OK",
    f"primes_checked={checked}",
    f"cycle_primes={len(cycle_primes)}",
    f"first={cycle_primes[:8]}",
)
