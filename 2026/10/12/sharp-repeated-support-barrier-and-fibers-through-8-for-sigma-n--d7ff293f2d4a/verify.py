#!/usr/bin/env python3
from math import isqrt

LIMIT = 2_000_000

spf = list(range(LIMIT + 1))
spf[0] = 0
spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out

def sigma_phi(fac):
    sigma = 1
    phi = 1
    for p, e in fac:
        sigma *= (p ** (e + 1) - 1) // (p - 1)
        phi *= p ** (e - 1) * (p - 1)
    return sigma, phi

fibers = {k: [] for k in range(3, 9)}
two_support_boundary = []
three_support_min = None
three_support_arg = None

for n in range(2, LIMIT + 1):
    fac = factor(n)
    sigma, phi = sigma_phi(fac)
    z = sigma + phi - 2*n

    if 3 <= z <= 8:
        fibers[z].append(n)

    if len(fac) == 2 and any(e > 1 for _, e in fac):
        assert z >= 8, (n, fac, z)
        if z == 8:
            two_support_boundary.append(n)

    if len(fac) >= 3:
        assert z >= 20, (n, fac, z)
        if three_support_min is None or z < three_support_min:
            three_support_min = z
            three_support_arg = n

assert fibers == {
    3: [8],
    4: [27],
    5: [],
    6: [125],
    7: [16],
    8: [12, 343],
}, fibers
assert two_support_boundary == [12], two_support_boundary
assert three_support_min == 20 and three_support_arg == 30, (three_support_min, three_support_arg)

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"fibers={fibers}",
    f"two_support_boundary={two_support_boundary}",
    f"three_support_min=({three_support_arg},{three_support_min})",
)
