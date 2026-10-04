#!/usr/bin/env python3
import math

PRIMES = [5, 7, 11]
BASES = [2, 3, 5, 7, 11, 13]

def vp(n, p):
    if n == 0:
        return 10**9
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

cases = 0
lifts = 0
for p in PRIMES:
    for q in BASES:
        if p == q:
            continue
        B = [None]
        for j in range(1, 5):
            n = p**j
            B.append(math.comb(q*n, n))
        # Jacobsthal/Ljunggren growth used in the proof: selected exact instances.
        if vp(B[1] - q, p) < 3:
            raise SystemExit(("base_lift_failed", p, q, vp(B[1]-q,p)))
        for j in range(2, 4):
            if vp(B[j] - B[j-1], p) < 3*j:
                raise SystemExit(("jacobsthal_lift_failed", p, q, j, vp(B[j]-B[j-1],p)))
            lifts += 1
        for r in range(1, 5):
            mod = p**r
            direct = (B[r] - pow(q, p**r, mod)) % mod == 0
            # B_1 agrees with the p-adic binomial limit modulo p^r for r<=4,
            # since B_2-B_1 is divisible by p^6. q^(p^(r+2)) agrees with the
            # Teichmuller lift modulo p^r.
            beta_mod = B[1] % mod
            omega_mod = pow(q, p**(r+2), mod)
            predicted = (beta_mod - omega_mod) % mod == 0
            if direct != predicted:
                raise SystemExit(("classification_failed", p, q, r, direct, predicted))
            cases += 1
print(f"VERIFY_OK cases={cases} lifts={lifts} primes={PRIMES} bases={BASES} r=1..4")
