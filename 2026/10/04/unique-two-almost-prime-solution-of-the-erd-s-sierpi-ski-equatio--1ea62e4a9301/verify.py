#!/usr/bin/env python3
LIMIT = 1_000_001

spf = list(range(LIMIT + 1))
if LIMIT >= 1:
    spf[1] = 1
for p in range(2, int(LIMIT**0.5) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

omega = [0] * (LIMIT + 1)
sigma = [1] * (LIMIT + 1)

for n in range(2, LIMIT + 1):
    x = n
    om = 0
    sig = 1
    while x > 1:
        p = spf[x]
        a = 0
        pp = 1
        while x % p == 0:
            x //= p
            a += 1
            pp *= p
        om += a
        sig *= (pp * p - 1) // (p - 1)
    omega[n] = om
    sigma[n] = sig

hits = []
tested = 0
for n in range(1, LIMIT):
    if omega[n] <= 2 and omega[n+1] <= 2:
        tested += 1
        if sigma[n] == sigma[n+1]:
            hits.append((n, n+1, sigma[n]))

assert hits == [(14, 15, 24)], hits
print(f"VERIFY_OK limit={LIMIT-1} low_omega_pairs={tested} hits={hits}")
