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
    tau = 1
    sigma = 1
    phi = 1
    omega = 0
    for p, e in fac:
        omega += e
        tau *= e + 1
        sigma *= (p ** (e + 1) - 1) // (p - 1)
        phi *= p ** (e - 1) * (p - 1)
    return omega, tau, sigma, phi

def predicted(fac):
    omega = sum(e for _, e in fac)
    if omega == 1:
        return True

    if omega == 2:
        if len(fac) == 1:
            p, e = fac[0]
            assert e == 2
            return p != 3
        assert len(fac) == 2 and all(e == 1 for _, e in fac)
        return all(p % 2 == 1 for p, _ in fac)

    if omega == 3:
        if len(fac) == 1:
            p, e = fac[0]
            assert e == 3
            return p % 4 == 1

        if len(fac) == 2:
            repeated = [p for p, e in fac if e == 2]
            singleton = [p for p, e in fac if e == 1]
            assert len(repeated) == len(singleton) == 1
            p = repeated[0]
            q = singleton[0]
            return (
                q % 2 == 1
                and (
                    p % 3 == 1
                    or (p == 3 and q % 3 == 2)
                )
            )

        assert len(fac) == 3 and all(e == 1 for _, e in fac)
        primes = sorted(p for p, _ in fac)
        if primes[0] != 2:
            return True
        q, r = primes[1], primes[2]
        return q % 4 != r % 4

    raise AssertionError("prediction requested outside Omega<=3")

checked = [0, 0, 0, 0]
hits = [0, 0, 0, 0]
first_hits = []

for n in range(2, LIMIT + 1):
    fac = factor(n)
    omega, tau, sigma, phi = stats(fac)
    if omega > 3:
        continue
    checked[omega] += 1
    direct = ((sigma + phi) % tau == 0)
    pred = predicted(fac)
    assert direct == pred, (n, fac, tau, sigma, phi, direct, pred)
    if direct:
        hits[omega] += 1
        if len(first_hits) < 25:
            first_hits.append(n)

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"checked_Omega1={checked[1]}",
    f"checked_Omega2={checked[2]}",
    f"checked_Omega3={checked[3]}",
    f"hits_Omega1={hits[1]}",
    f"hits_Omega2={hits[2]}",
    f"hits_Omega3={hits[3]}",
    f"first_hits={first_hits}",
)
