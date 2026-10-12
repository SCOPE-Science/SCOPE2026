#!/usr/bin/env python3
from math import isqrt

LIMIT = 1_000_000

spf = list(range(LIMIT + 1))
spf[0] = 0
spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def factor_stats(n):
    x = n
    omega = 0
    sigma = 1
    phi = 1
    fac = []
    while x > 1:
        p = spf[x]
        e = 0
        pp = 1
        while x % p == 0:
            x //= p
            e += 1
            pp *= p
        fac.append((p, e))
        omega += e
        sigma *= (pp*p - 1) // (p - 1)
        phi *= p**(e-1) * (p-1)
    return fac, omega, sigma, phi

hits = []
checked = 0

for n in range(4, LIMIT + 1):
    fac, omega, sigma, phi = factor_stats(n)
    if omega > 3:
        continue
    if len(fac) == 1 and fac[0][1] == 1:
        continue
    checked += 1
    cototient = n - phi
    aliquot = sigma - n
    if aliquot % cototient == 0:
        hits.append((n, omega, aliquot // cototient))

assert hits == [(12, 3, 2)], hits

fac56, omega56, sigma56, phi56 = factor_stats(56)
assert fac56 == [(2, 3), (7, 1)]
assert omega56 == 4
assert sigma56 == 120
assert phi56 == 24
assert (sigma56 - 56) // (56 - phi56) == 2

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"composite_omega_le3_checked={checked}",
    f"hits={hits}",
    f"sharpness=(56,{omega56},{(sigma56-56)//(56-phi56)})",
)
