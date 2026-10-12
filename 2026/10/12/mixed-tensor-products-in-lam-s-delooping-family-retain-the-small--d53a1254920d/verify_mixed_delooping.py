#!/usr/bin/env python3
"""Finite structural checks for the mixed Lam-family delooping argument.

The infinite theorem is proved symbolically in RESULT.md.  This checker only
verifies the degree/support combinatorics used by that proof over a broad
finite sample of parameter pairs; it is not an exhaustive proof over all m,n.
"""
from collections import Counter


def arrows(r):
    out = {i: set() for i in range(1, r + 3)}
    out[1].update((1, 2))
    for i in range(2, r + 1):
        out[i].add(i + 1)
    out[r + 2].add(2)
    return out


def psupp(r, i):
    return {i} | arrows(r)[i]


def prod_psupp(m, n, i, j):
    return {(a, b) for a in psupp(m, i) for b in psupp(n, j)}


def pindex(r, degree):
    # Minimal resolution of T_r: degree 0 is P_{r+2}; degree a>=1 is P_{a+1}.
    assert 0 <= degree <= r
    return r + 2 if degree == 0 else degree + 1


def ext_degrees(m, n):
    # Ext^i(T_r,A_r) is one-dimensional exactly at i=1,r.
    c = Counter()
    for a in (1, m):
        for b in (1, n):
            c[a + b] += 1
    return c


def successors_product(m, n, v):
    i, j = v
    ans = set()
    for ii in arrows(m)[i]:
        ans.add((ii, j))
    for jj in arrows(n)[j]:
        ans.add((i, jj))
    return ans


def check_pair(m, n):
    q = min(m, n)
    ed = ext_degrees(m, n)
    assert all(ed[k] == 0 for k in range(3, q + 1))
    expected = Counter()
    for d in (2, m + 1, n + 1, m + n):
        expected[d] += 1
    # Counter coalesces equal degrees, as Kunneth does by direct sum.
    assert ed == expected

    W = {(1, 1), (1, 2), (2, 1), (2, 2)}
    V = {(i, j) for i in range(1, m + 2) for j in range(1, n + 2)}
    assert W <= V
    assert all(successors_product(m, n, v) <= V for v in V)

    # The mixed Omega^2 Loewy support is the same local five-vertex pattern.
    omega2 = {
        (m + 2, 3), (2, 2), (3, n + 2),
        (2, 3), (3, 2),
    }
    first_targets = (
        prod_psupp(m, n, 1, 1)
        | prod_psupp(m, n, m + 2, 2)
        | prod_psupp(m, n, 2, n + 2)
    )
    assert omega2 <= first_targets

    # The projectives appearing in the three-step local approximation do not
    # see tail vertices 4,... except for the distinguished endpoints m+2,n+2.
    allowed_first = {1, 2, 3, m + 2}
    allowed_second = {1, 2, 3, n + 2}
    assert all(i in allowed_first and j in allowed_second for i, j in first_targets)
    assert prod_psupp(m, n, 1, 1) == W

    # Degree-q term of the total minimal tensor resolution has a unique summand
    # whose support contains v=(m+2,q+1): the (0,q) summand.
    v = (m + 2, q + 1)
    degree_q = []
    for a in range(0, m + 1):
        b = q - a
        if 0 <= b <= n:
            degree_q.append((a, b, prod_psupp(m, n, pindex(m, a), pindex(n, b))))
    carriers = [(a, b) for a, b, supp in degree_q if v in supp]
    assert carriers == [(0, q)]
    # Its vertical differential lands in the (0,q-1) target and is nonzero at v.
    target = prod_psupp(m, n, pindex(m, 0), pindex(n, q - 1))
    assert v in target
    assert v not in V


for m in range(2, 13):
    for n in range(2, 13):
        check_pair(m, n)

print("CHECK_OK pairs=121 range=2..12")
