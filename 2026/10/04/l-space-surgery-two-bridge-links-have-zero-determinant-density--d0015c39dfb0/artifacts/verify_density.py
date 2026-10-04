#!/usr/bin/env python3
"""Exact finite checks for the two-bridge L-space-surgery counting theorem."""

import math

def tau(n):
    out = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            out += 1 if d * d == n else 2
        d += 1
    return out

def is_square(n):
    return math.isqrt(n) ** 2 == n

def formula_count(p):
    if p == 2:
        return 1
    return (
        tau(p - 1) + tau(p + 1) - 2
        + int(is_square(p - 1)) + int(is_square(p + 1))
    ) // 2

def canonical_qs(p):
    return [
        q for q in range(1, p // 2 + 1, 2)
        if math.gcd(p, q) == 1
    ]

def lspace_qs(p):
    return [
        q for q in canonical_qs(p)
        if q == 1 or (p - 1) % q == 0 or (p + 1) % q == 0
    ]

def orbit_count(p, qs):
    qset = set(qs)
    seen = set()
    count = 0
    for q in qs:
        if q in seen:
            continue
        inv = pow(q, -1, p)
        partner = min(inv, p - inv)
        seen.add(q)
        if partner in qset:
            seen.add(partner)
        count += 1
    return count

for p in range(2, 1002, 2):
    got = orbit_count(p, lspace_qs(p))
    want = formula_count(p)
    assert got == want, (p, got, want)

scaled = []
for X in (100, 1000, 5000):
    numerator = sum(formula_count(p) for p in range(2, X + 1, 2))
    denominator = sum(
        orbit_count(p, canonical_qs(p))
        for p in range(2, X + 1, 2)
    )
    scaled.append((X, numerator, denominator, numerator / denominator * X / math.log(X)))

print(
    "VERIFY_OK "
    "exact_even_p_through=1000 "
    "scaled_density="
    + ",".join(
        f"{X}:{num}/{den}:{ratio:.8f}"
        for X, num, den, ratio in scaled
    )
    + f" target_pi2={math.pi**2:.8f}"
)
