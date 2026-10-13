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

def arithmetic_values(fac):
    sigma1 = 1
    sigma2 = 1
    phi = 1
    for p, e in fac:
        sigma1 *= (p ** (e + 1) - 1) // (p - 1)
        sigma2 *= (p ** (2*(e + 1)) - 1) // (p*p - 1)
        phi *= p ** (e - 1) * (p - 1)
    return sigma1, sigma2, phi

exceptional = {4:3, 8:17, 9:7, 25:21}
low_exceptional = {}
boundary = []
primes_checked = 0
semiprimes_checked = 0
mixed_repeated_checked = 0
large_support_checked = 0

for n in range(2, LIMIT + 1):
    fac = factor(n)
    sigma1, sigma2, phi = arithmetic_values(fac)
    H = sigma2 + phi * sigma1 - 2*n*n

    is_prime = (len(fac) == 1 and fac[0][1] == 1)
    is_squarefree_semiprime = (len(fac) == 2 and fac[0][1] == fac[1][1] == 1)

    if is_prime:
        primes_checked += 1
        assert H == 0, (n, H)
    elif is_squarefree_semiprime:
        semiprimes_checked += 1
        assert H == 2, (n, H)
    elif len(fac) >= 2:
        if len(fac) == 2:
            mixed_repeated_checked += 1
        else:
            large_support_checked += 1
        assert H >= 34, (n, fac, H)

    predicted_low = is_prime or is_squarefree_semiprime or n in exceptional
    assert (H < 34) == predicted_low, (n, fac, H, predicted_low)

    if n in exceptional:
        assert H == exceptional[n], (n, H)
        low_exceptional[n] = H

    if H == 34:
        boundary.append(n)

assert low_exceptional == exceptional
assert boundary == [12], boundary

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"primes_checked={primes_checked}",
    f"semiprimes_checked={semiprimes_checked}",
    f"mixed_repeated_checked={mixed_repeated_checked}",
    f"large_support_checked={large_support_checked}",
    f"exceptions={sorted(low_exceptional.items())}",
    f"boundary={boundary}",
)
