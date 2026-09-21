#!/usr/bin/env python3
"""Exact finite checks for the Nakayama Frobenius-dimension theorem.

The script enumerates cyclic Kupisch series with 2 <= c_i <= 2n-1 for
2 <= n <= 6, tests the standard cyclic Nakayama admissibility inequalities,
detects quasi-heredity via the existence of a simple module of projective
dimension 2, and computes F(A)=dim Hom_A(D(A),A) from uniserial Hom spaces.
The general theorem is proved symbolically in RESULT.md; this is only a
finite sanity check.
"""

from itertools import product

def valid_cyclic(c):
    n = len(c)
    return all(c[(i + 1) % n] >= c[i] - 1 for i in range(n))

def pd_simple(c, i, cap=200):
    n = len(c)
    top, length, steps = i, 1, 0
    while length != c[top]:
        top, length = (top + length) % n, c[top] - length
        steps += 1
        if steps > cap:
            return None
    return steps

def quasi_hereditary_cyclic(c):
    return any(pd_simple(c, i) == 2 for i in range(len(c)))

def cokupisch(c):
    n = len(c)
    M = max(c)
    out = []
    for socle in range(n):
        lengths = []
        for ell in range(1, M + n + 2):
            top = (socle - ell + 1) % n
            if ell <= c[top]:
                lengths.append(ell)
        out.append(max(lengths))
    return out

def homdim(c, source_top, source_len, target_top, target_len):
    n = len(c)
    low = max(0, target_len - source_len)
    return sum(
        1
        for r in range(low, target_len)
        if (target_top + r - source_top) % n == 0
    )

def frobdim(c):
    n = len(c)
    d = cokupisch(c)
    total = 0
    for socle in range(n):
        source_top = (socle - d[socle] + 1) % n
        for target_top in range(n):
            total += homdim(
                c, source_top, d[socle], target_top, c[target_top]
            )
    return total

for n in range(2, 7):
    count = 0
    maximum = -1
    maximizers = 0
    for c in product(range(2, 2 * n), repeat=n):
        if not valid_cyclic(c) or not quasi_hereditary_cyclic(c):
            continue
        count += 1
        f = frobdim(c)
        if f > maximum:
            maximum = f
            maximizers = 1
        elif f == maximum:
            maximizers += 1
    witness = (2,) + tuple(range(n + 1, 2, -1))
    print(
        f"n={n}: qh_cyclic={count}, max_F={maximum}, "
        f"expected={n*n+1}, maximizers={maximizers}, "
        f"witness_F={frobdim(witness)}"
    )
