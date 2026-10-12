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
    omega = 0
    for p, e in fac:
        omega += e
        sigma *= (p ** (e + 1) - 1) // (p - 1)
        phi *= p ** (e - 1) * (p - 1)
    return sigma, phi, omega

hits = []
checked = [0, 0, 0, 0]

for n in range(2, LIMIT + 1):
    fac = factor(n)
    sigma, phi, omega = stats(fac)
    if omega > 3:
        continue
    checked[omega] += 1
    if (sigma - n) % phi == 0:
        hits.append((n, omega, (sigma - n) // phi))

assert hits == [
    (2, 1, 1),
    (6, 2, 3),
    (10, 2, 2),
    (12, 3, 4),
    (44, 3, 2),
], hits

fac90 = factor(90)
sigma90, phi90, omega90 = stats(fac90)
assert fac90 == [(2, 1), (3, 2), (5, 1)]
assert omega90 == 4
assert sigma90 - 90 == 144
assert phi90 == 24
assert (sigma90 - 90) // phi90 == 6

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"checked_Omega1={checked[1]}",
    f"checked_Omega2={checked[2]}",
    f"checked_Omega3={checked[3]}",
    f"hits={hits}",
    f"sharpness=(90,{omega90},{(sigma90-90)//phi90})",
)
