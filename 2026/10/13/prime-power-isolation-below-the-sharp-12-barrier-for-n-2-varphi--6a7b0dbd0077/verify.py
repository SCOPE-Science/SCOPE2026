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

def stats(fac):
    sigma = 1
    phi = 1
    for p, e in fac:
        sigma *= (p ** (e + 1) - 1) // (p - 1)
        phi *= p ** (e - 1) * (p - 1)
    return sigma, phi

expected_nonprime_low = [
    (4, 2), (8, 4), (9, 3), (16, 8),
    (25, 5), (27, 9), (49, 7), (121, 11),
]

nonprime_low = []
eq12 = []
mixed_checked = 0
prime_checked = 0

for n in range(2, LIMIT + 1):
    fac = factor(n)
    sigma, phi = stats(fac)
    F = n*n - phi*sigma
    assert F > 0

    if len(fac) == 1:
        p, a = fac[0]
        assert F == p ** (a - 1), (n, fac, F)
        if a == 1:
            assert F == 1
            prime_checked += 1
        elif F < 12:
            nonprime_low.append((n, F))
    else:
        mixed_checked += 1
        assert F >= 12, (n, fac, F)
        if F == 12:
            eq12.append(n)

assert nonprime_low == expected_nonprime_low, nonprime_low
assert eq12 == [6], eq12

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"prime_checked={prime_checked}",
    f"mixed_support_checked={mixed_checked}",
    f"nonprime_low={nonprime_low}",
    f"eq12={eq12}",
)
