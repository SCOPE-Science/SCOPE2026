#!/usr/bin/env python3
"""Independent integer-arithmetic checks for the consecutive-square GCD identity."""
from math import gcd

N = 5000
B = [0, 1]
C = [1, 3]
for i in range(2, N + 1):
    B.append(6 * B[-1] - B[-2])
    C.append(6 * C[-1] - C[-2])

for k in range(1, 251):
    rolling = sum(C[j] * C[j] for j in range(1, k + 1))
    observed = 0
    for n in range(19):
        observed = gcd(observed, rolling)
        if n <= 4:
            assert 2 * rolling == k + B[k] * C[2*n + k + 1], (k,n)
        if n < 18:
            updated = rolling + C[n+k+1]**2 - C[n+1]**2
            assert updated - rolling == 8 * B[k] * B[2*n+k+2], (k,n)
            rolling = updated
    assert observed == gcd(k, B[k]), (k,observed,gcd(k,B[k]))

for k in range(1, 251):
    seq = [B[k + 2 + 2*n] for n in range(8)]
    g = 0
    for x in seq: g = gcd(g, x)
    assert g == (1 if k % 2 else 6)

print('PASS: k=1..250, 19 windows, exact sum/difference identities, stride gcds')
