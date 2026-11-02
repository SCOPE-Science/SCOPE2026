#!/usr/bin/env python3
"""Exact labeled-set checks for four-row Cartesian clique products.

Requires only Python 3 standard library. Rows are 0,1,2,3 and
columns are 0,...,n-1.  A four-bit mask encodes each selected column.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def falling(n, k):
    return factorial(n) // factorial(n-k) if 0 <= k <= n else 0


def pairs(mask):
    out = 0
    for index, (a,b) in enumerate(combinations(range(4), 2)):
        if mask & (1 << a) and mask & (1 << b):
            out |= 1 << index
    return out

PAIRS = tuple(pairs(j) for j in range(16))


def admissible(cols):
    used = 0
    for col in cols:
        if used & PAIRS[col]:
            return False
        used |= PAIRS[col]
    return True


def original_geodesic_test(cols):
    """Test selected endpoints via both actual two-edge shortest paths.

    In K_4 square K_n, different-row different-column endpoints
    have precisely the two cross-corner intermediate vertices.
    """
    n = len(cols)
    for i in range(n):
        for j in range(i):
            for a in range(4):
                if not cols[i] & (1 << a):
                    continue
                for b in range(4):
                    if a == b or not cols[j] & (1 << b):
                        continue
                    if cols[i] & (1 << b) and cols[j] & (1 << a):
                        return False
    return True


def maximal(cols):
    used = 0
    for c in cols:
        used |= PAIRS[c]
    for c in cols:
        others = used ^ PAIRS[c]  # permitted: no pair is repeated
        for row in range(4):
            b = 1 << row
            if not c & b and not (PAIRS[c | b] & others):
                return False
    return True


def complete_polynomial(n):
    out = Counter()
    for t in range(min(6,n) + 1):
        factor = comb(n,t) * falling(6,t)
        for k in range(n-t+1):
            out[2*t+k] += factor*comb(n-t,k)*4**k
    for t in range(min(3,n-1)+1):
        factor = 4*n*comb(n-1,t)*falling(3,t)
        for k in range(n-1-t+1):
            out[3+2*t+k] += factor*comb(n-1-t,k)*4**k
    for k in range(n):
        out[4+k] += n*comb(n-1,k)*4**k
    return +out


def maximal_polynomial(n):
    out = Counter()
    out[n+3] += n*4**(n-1) + 12*falling(n,2) + 4*falling(n,3)
    if n >= 3:
        out[n+4] += 12*falling(n,3)*2**(n-3)
    if n == 4:
        out[n+4] += 72  # four double columns use the edges of a C4
    if n >= 4:
        out[n+5] += 4*falling(n,4)*4**(n-4)
    if n >= 5:
        out[n+5] += 6*falling(n,5)*2**(n-5)
    if n >= 6:
        out[n+6] += falling(n,6)*4**(n-6)
    return +out


def check(n):
    poly = Counter()
    maximal_poly = Counter()
    tested = 0

    def record(cols):
        nonlocal tested
        tested += 1
        size = sum(int(c).bit_count() for c in cols)
        poly[size] += 1
        if maximal(cols):
            maximal_poly[size] += 1

    if n <= 5:
        for global_mask in range(1 << (4*n)):
            cols = tuple((global_mask >> (4*i)) & 15 for i in range(n))
            ok = admissible(cols)
            if n <= 4:
                assert ok == original_geodesic_test(cols), (n,global_mask)
            if ok:
                record(cols)
    else:
        # Independently enumerate admissible columns, pruning repeated row pairs.
        def search(cols, used):
            if len(cols) == n:
                record(cols)
                return
            for c in range(16):
                if PAIRS[c] & used:
                    continue
                search(cols+(c,), used | PAIRS[c])
        search((), 0)

    assert poly == complete_polynomial(n), (n, poly, complete_polynomial(n))
    assert maximal_poly == maximal_polynomial(n), (n, maximal_poly, maximal_polynomial(n))
    print("n=%d valid=%d maximal=%s" % (n,tested, sorted(maximal_poly.items())))
    return tested


if __name__ == "__main__":
    total = sum(check(n) for n in range(2,7))
    print("ALL_CHECKS_PASS total_admissible=%d" % total)
