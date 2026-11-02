#!/usr/bin/env python3
"""Exact integer checks for the Walsh affine-codebook worst-case RAC theorem."""
from itertools import product


def walsh(v):
    u = list(v)
    n = len(u)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                a, b = u[j], u[j+h]
                u[j], u[j+h] = a+b, a-b
        h *= 2
    return u


def bent(m):
    assert m % 2 == 0
    s = []
    for x in range(1 << m):
        q = sum(((x >> (2*j)) & 1) * ((x >> (2*j+1)) & 1)
                for j in range(m//2)) % 2
        s.append(1 if q == 0 else -1)
    return s


def check_sign_vector(s):
    n = len(s)
    w = walsh(s)
    assert all(t in (-1, 1) for t in s)
    assert sum(t*t for t in w) == n*n
    total = sum(abs(t) for t in w)
    assert total <= n * int(n**0.5) if int(n**0.5)**2 == n else total*total <= n**3
    # The constructed signed affine mixture has coefficients w_a/total;
    # its evaluation must equal n*s_x/total identically for every coordinate.
    twice = walsh(w)
    assert all(tw == n*si for tw, si in zip(twice, s))
    assert total >= n
    # The per-coordinate success is (total+n)/(2*total).
    return total


for m in (2, 4, 6, 8):
    n = 1 << m
    s = bent(m)
    w = walsh(s)
    assert all(abs(t) == 1 << (m//2) for t in w)
    assert check_sign_vector(s) == n*(1 << (m//2))

# Complete census of truth tables at m=2 and m=4: every input succeeds
# at least at the claimed probability, and bent inputs attain equality.
for m, expected_bent in ((2, 8), (4, 896)):
    n = 1 << m
    worst_total = 0
    worst_count = 0
    for bits in range(1 << n):
        s = [1 - 2*((bits >> x) & 1) for x in range(n)]
        total = check_sign_vector(s)
        if total > worst_total:
            worst_total, worst_count = total, 1
        elif total == worst_total:
            worst_count += 1
    assert worst_total == n * (1 << (m//2))
    assert worst_count == expected_bent
print('AFFINE_RAC_VERIFY_OK')
