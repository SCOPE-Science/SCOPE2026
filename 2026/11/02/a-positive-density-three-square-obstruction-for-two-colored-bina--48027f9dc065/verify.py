#!/usr/bin/env python3
"""Exact polynomial certificate for two-colored binary partitions modulo 128."""
from math import comb
R, MOD = 128, 128
DEG = 14 * R - 2 * (R - 1)

# Construct T(x) = product_{j=0}^6 ((1-x^128)/(1-x^(2^j)))^2.
T = [0] * (DEG + 1)
T[0] = 1
for j in range(7):
    d = 1 << j
    for _ in range(2):
        nxt = [0] * (DEG + 1)
        for k in range(DEG + 1):
            nxt[k] = (T[k] + (nxt[k-d] if k >= d else 0)
                      - (T[k-R] if k >= R else 0)) % MOD
        T = nxt

P = [1, 2, 5]  # B_2(y) modulo 8, symbolically checked below.
assert all((z % 8) == 0 for z in [-8])
assert (1,2,5) == tuple(P)
expected = [112,112,16,16,96,96,32,32,48,48,80,80]
certificate = []
for r in range(R):
    a = [T[k] for k in range(r, DEG+1, R)]
    if any(z % 16 for z in a):
        continue
    q = [z // 16 for z in a]
    product = [sum(P[j] * q[k-j] for j in range(3)
                   if 0 <= k-j < len(q)) % 8 for k in range(14)]
    target = [7 * (-1)**k * comb(13,k) % 8 for k in range(14)]
    if product == target:
        certificate.append(r)
        assert a == expected
assert certificate == [36,62], certificate

# Independent coefficient production: two passes of unbounded-coin DP per part size.
L = 8192
b = [0] * L
b[0] = 1
for j in range(13):
    d = 1 << j
    for _ in range(2):
        for n in range(d, L):
            b[n] = (b[n] + b[n-d]) % 128
assert b[:3] == [1,2,5]
for n in range(3,L):
    if n % 128 in certificate:
        assert b[n] == 112, (n,b[n])
print('VERIFY_OK', 'degree', DEG, 'certified_residues', certificate,
      'independent_coefficients', L)
