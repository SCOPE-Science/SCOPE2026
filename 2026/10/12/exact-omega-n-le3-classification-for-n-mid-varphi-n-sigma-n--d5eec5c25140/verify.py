#!/usr/bin/env python3
from math import isqrt

LIMIT = 3_000_000

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

def prime(n):
    if n < 2:
        return False
    if n <= LIMIT:
        return spf[n] == n
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def predicted(n, fac):
    if n in (6, 18):
        return True
    if len(fac) != 2:
        return False
    # Family p^2 q with q = p^2+p+1 prime.
    repeated = [(p,e) for p,e in fac if e == 2]
    singles = [p for p,e in fac if e == 1]
    if len(repeated) != 1 or len(singles) != 1:
        return False
    p = repeated[0][0]
    q = singles[0]
    return q == p*p + p + 1 and prime(p) and prime(q)

hits = []
checked = 0
for n in range(2, LIMIT + 1):
    fac = factor(n)
    if sum(e for _,e in fac) > 3:
        continue
    checked += 1
    sigma, phi = sigma_phi(fac)
    direct = ((sigma * phi) % n == 0)
    expect = predicted(n, fac)
    assert direct == expect, (n, fac, sigma, phi, direct, expect)
    if direct:
        hits.append(n)

assert hits == [6,18,28,117,775,88723,2896363], hits
print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"omega_le3_checked={checked}",
    f"hits={hits}",
)
