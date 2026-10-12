#!/usr/bin/env python3
import math

# Square corroboration through a large exact finite range.
square_hits = []
for n in range(1, 5001):
    c = n * (1 << n) + 1
    z = math.isqrt(c)
    if z*z == c:
        square_hits.append((n,z))
assert square_hits == [(2,3),(3,5)], square_hits

# Exact integer kth-root helper for finite odd-exponent corroboration.
def iroot(x, k):
    lo, hi = 1, 2
    while hi**k <= x:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi)//2
        if mid**k <= x:
            lo = mid
        else:
            hi = mid
    return lo

odd_hits = []
for n in range(1, 301):
    c = n * (1 << n) + 1
    for k in range(3, 16, 2):
        y = iroot(c,k)
        if y**k == c:
            odd_hits.append((n,y,k))
assert odd_hits == [], odd_hits

# Recheck the inequalities used in the symbolic proof over a broad finite range.
for n in range(1, 10001):
    assert (1 << (3*n)) > n * (1 << n) + 1
for n in range(5, 10001):
    assert (1 << (n-2)) > n + 1

print('VERIFY_OK', 'square_limit=5000', f'square_hits={square_hits}', 'odd_n_limit=300', 'odd_k_max=15', 'odd_hits=0')
