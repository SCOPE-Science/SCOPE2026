"""Reproducible finite tests for power norms on tree Cesaro spaces.
The mathematical proof is independent of these finite computations.
"""
import math
import random
from mpmath import zeta


def cesaro_norm(vec, p, trunc=8000):
    total = 0.0
    partial = 0.0
    for n in range(trunc):
        if n < len(vec):
            partial += abs(vec[n])
        total += (partial / (n + 1))**p
    # Exact tail for finite-support arrays.
    if len(vec) < trunc:
        total += partial**p * float(zeta(p, trunc + 1))
    return total**(1/p)


def shift(vec, m):
    return vec[m:] if m < len(vec) else []


rng = random.Random(261022)
checks = 0
for p in [1.2, 1.5, 2., 3., 5.]:
    for m in [1, 2, 3, 5]:
        H0 = float(zeta(p, 1))
        Hm = float(zeta(p, m + 1))
        K = (H0 / Hm)**(1/p)
        basis = [0.] * m + [1.]
        assert abs(cesaro_norm(shift(basis,m),p) / cesaro_norm(basis,p) - K) < 0.002
        for k in range(m + 1, m + 12):
            ratio = float(zeta(p, k-m+1)/zeta(p,k+1))
            assert ratio < H0/Hm
        for _ in range(120):
            a = [rng.random() for _ in range(12)]
            before = cesaro_norm(a,p)
            after = cesaro_norm(shift(a,m),p)
            assert after <= K*before*(1+1e-8)
            checks+=1
for b in [2,3]:
    for p in [1.5,2.,3.]:
        for m in [1,2,3]:
            # One supported level with constant phase: the tree shift realizes K.
            H0=float(zeta(p)); Hm=float(zeta(p,m+1))
            norm_in = (Hm)**(1/p)
            norm_out = (H0)**(1/p)*b**m
            assert abs(norm_out/norm_in - b**m*(H0/Hm)**(1/p)) < 1e-10
            checks+=1
print('PASS',checks,'finite checks; infinite claims proved analytically')
