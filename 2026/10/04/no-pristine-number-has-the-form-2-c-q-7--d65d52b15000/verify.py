#!/usr/bin/env python3
from math import comb

def F7(c):
    return sum(comb(7, i) * comb(c + i, i) for i in range(8))

def G(c):
    return (
        c**6 + 69*c**5 + 1681*c**4 + 17667*c**3
        + 79318*c**2 + 143184*c + 80640
    )

def exact_kth_root(n, k):
    lo, hi = 0, 1
    while hi**k < n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        p = mid**k
        if p < n:
            lo = mid
        else:
            hi = mid
    if hi**k == n:
        return hi
    if lo**k == n:
        return lo
    return None

# Check the factorization exactly on enough integer points to certify
# the degree-7 polynomial identity.
for c in range(0, 8):
    assert 5040 * F7(c) == (c + 8) * G(c)

assert G(-8) == -147456
assert -147456 == -(2**14) * (3**2)
assert 4**7 > 5040

hits = []
for c in range(1, 5033):
    value = F7(c)
    root = exact_kth_root(value, 7)
    if root is not None:
        hits.append((c, root, value))

assert hits == []
print("VERIFY_OK")
