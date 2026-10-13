#!/usr/bin/env python3
LIMIT = 200000

def sieve_spf(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p:
            for m in range(p*p, n+1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def factor(n, spf):
    out = {}
    while n > 1:
        p = spf[n]
        out[p] = out.get(p, 0) + 1
        n //= p
    return out

def sigma_from_factor(f):
    s = 1
    for p, a in f.items():
        s *= (p**(a+1)-1)//(p-1)
    return s

spf = sieve_spf(LIMIT + 1)
omega_big = [0]*(LIMIT+2)
aliquot = [0]*(LIMIT+2)
for n in range(1, LIMIT+2):
    f = factor(n, spf)
    omega_big[n] = sum(f.values())
    aliquot[n] = sigma_from_factor(f) - n

tested = 0
hits = []
for n in range(1, LIMIT+1):
    if omega_big[n] <= 2 and omega_big[n+1] <= 2:
        tested += 1
        if aliquot[n] == aliquot[n+1]:
            hits.append(n)

assert hits == [2], hits
print(f"VERIFY_OK limit={LIMIT} tested_low_omega_pairs={tested} hits={hits}")
