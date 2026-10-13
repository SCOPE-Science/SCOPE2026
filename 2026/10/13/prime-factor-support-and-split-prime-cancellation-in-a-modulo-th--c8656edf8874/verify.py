#!/usr/bin/env python3
"""Independent finite checks of a prime-factor theta-coefficient formula.
Uses only the Python standard library. Finite checks do not prove the theorem.
"""
from math import isqrt

COUNT_LIMIT = 10000
PART_LIMIT = 1200
MAX_NORM = 20 * (COUNT_LIMIT - 1) + 9

spf = list(range(MAX_NORM + 1))
for p in range(2, isqrt(MAX_NORM) + 1):
    if spf[p] == p:
        for q in range(p*p, MAX_NORM + 1, p):
            if spf[q] == q:
                spf[q] = p

def predicted(n):
    z = 20 * n + 9
    magnitude = 1
    while z > 1:
        p = spf[z]
        e = 0
        while z % p == 0:
            z //= p
            e += 1
        if p % 4 == 3 and e % 2:
            return 0
        if p % 20 in (13, 17) and e % 2:
            return 0
        if p % 20 in (1, 9):
            magnitude *= e + 1
    return magnitude

def gaussian_coefficient(n):
    norm = 20*n + 9
    total = 0
    for y in range(-isqrt(norm)//5-1, isqrt(norm)//5+2):
        Y=5*y
        x2 = norm - Y*Y
        if x2 < 0:
            continue
        X=isqrt(x2)
        if X*X != x2:
            continue
        for x in ((X,) if X == 0 else (X,-X)):
            if x % 5 == 2:
                # Unique representative in each Gaussian unit orbit.
                total += -1 if y%2 else 1
    return total

# Compute the actual bounded-partition counts modulo 3 independently
# of both Gaussian lattice enumeration and prime-factorization.
dp=[0]*(PART_LIMIT+1)
dp[0]=1
for k in range(1,PART_LIMIT+1):
    if k % 5 not in (0,1,4):
        continue
    nxt=dp[:]
    for i in range(k, PART_LIMIT+1):
        nxt[i]=(nxt[i]+dp[i-k])%3
    for i in range(2*k, PART_LIMIT+1):
        nxt[i]=(nxt[i]+dp[i-2*k])%3
    dp=nxt

for n in range(COUNT_LIMIT):
    g=gaussian_coefficient(n)
    mag=predicted(n)
    assert abs(g)==mag, ('prime-factor magnitude',n,g,mag)
    if n<=PART_LIMIT:
        assert g%3==dp[n], ('partition congruence',n,g,dp[n])

# An explicit split-prime cancellation not forced by sum-of-two-squares.
assert 20*31+9 == 629 and 629==17*37
assert gaussian_coefficient(31)==0 and predicted(31)==0
print('VERIFY_OK exact_coefficient_count=10000 direct_partition_count=1201 split_prime_cancellation_N629=PASS')
