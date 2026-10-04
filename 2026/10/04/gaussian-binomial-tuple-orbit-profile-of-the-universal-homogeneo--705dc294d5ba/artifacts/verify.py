#!/usr/bin/env python3
from itertools import combinations, product, combinations_with_replacement
from math import comb

Q = 5

def qbin(n, r, q):
    if r < 0 or r > n:
        return 0
    num = den = 1
    for i in range(r):
        num *= q**(n-i) - 1
        den *= q**(r-i) - 1
    return num // den

def rref_subspaces(n, r, q):
    if r == 0:
        return {()}
    out = set()
    for piv in combinations(range(n), r):
        free = []
        for i, p in enumerate(piv):
            for j in range(p+1, n):
                if j not in piv:
                    free.append((i, j))
        for vals in product(range(q), repeat=len(free)):
            rows = [[0]*n for _ in range(r)]
            for i, p in enumerate(piv):
                rows[i][p] = 1
            for (i,j), a in zip(free, vals):
                rows[i][j] = a
            out.add(tuple(tuple(row) for row in rows))
    return out

def profile(n, q):
    return sum(qbin(n, r, q) * q**comb(r+2, 3) for r in range(n+1))

# Independent subspace census versus Gaussian-binomial formula.
for n in range(5):
    for r in range(n+1):
        got = len(rref_subspaces(n, r, Q))
        want = qbin(n, r, Q)
        assert got == want, (n, r, got, want)

# Symmetric trilinear coordinates are indexed by 3-multisets of r basis indices.
for r in range(8):
    got = len(list(combinations_with_replacement(range(r), 3)))
    want = comb(r+2, 3)
    assert got == want, (r, got, want)

expected = [
    1,
    6,
    656,
    9785156,
    95368955582656,
    2910383120155532786132656,
]
assert [profile(n, Q) for n in range(6)] == expected

# Independent-tuples term is exactly the r=n summand.
for n in range(8):
    assert qbin(n, n, Q) * Q**comb(n+2, 3) == Q**comb(n+2, 3)

print('VERIFY_OK')
