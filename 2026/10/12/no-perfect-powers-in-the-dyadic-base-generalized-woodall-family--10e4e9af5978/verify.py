#!/usr/bin/env python3
from math import isqrt

def iroot(n, k):
    if k == 2:
        return isqrt(n)
    lo, hi = 1, 2
    while pow(hi, k) <= n:
        hi *= 2
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if pow(m, k) <= n:
            lo = m
        else:
            hi = m
    return lo

def perfect_power(n):
    if n < 4:
        return False
    for k in range(2, n.bit_length() + 1):
        r = iroot(n, k)
        if r >= 2 and pow(r, k) == n:
            return (r, k)
    return False

checked = 0
for a in range(1, 7):
    for n in range(1, 31):
        w = n * (1 << (a*n)) - 1
        assert not perfect_power(w), (a, n, w)
        checked += 1

low = []
for a in range(1, 5):
    for n in range(1, 5):
        if a*n < 3:
            low.append((a, n, n * (1 << (a*n)) - 1))
assert sorted(low) == [(1,1,1),(1,2,7),(2,1,3)]

# Squared form of n*2^(n-1) >= (4n/3)^(3/2):
# 27*2^(2n-2) >= 64*n.
for n in range(3, 10001):
    assert 27 * (1 << (2*n - 2)) >= 64*n
    assert 4*n > n+1

print("VERIFY_OK", f"grid={checked}", f"low={sorted(low)}", "ineq_n=3..10000", "monotonicity=passed")
