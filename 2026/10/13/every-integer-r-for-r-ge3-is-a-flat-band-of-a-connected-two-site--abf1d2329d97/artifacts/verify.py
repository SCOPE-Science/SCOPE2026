#!/usr/bin/env python3
"""Exact finite checks of a two-orbit periodic flat-band construction.

The unrestricted theorem follows from the symbolic identities in RESULT.md;
finite examples here are diagnostics, not a proof of all parameter values.
"""
from collections import Counter


def data(r):
    assert isinstance(r, int) and r >= 2
    U = {2**j-1 for j in range(r)}
    V = {2**r*u for u in U}
    D_U = Counter(u-v for u in U for v in U)
    D_V = Counter(u-v for u in V for v in V)
    S = Counter(u+v for u in U for v in V)
    assert len(U) == len(V) == r
    assert D_U[0] == D_V[0] == r
    assert all(c == 1 for d, c in D_U.items() if d)
    assert all(c == 1 for d, c in D_V.items() if d)
    assert all(c == 1 for c in S.values())
    assert set(D_U).intersection(set(D_V)) == {0}
    return U, V, set(D_U) - {0}, set(D_V) - {0}, set(S)


def check(r):
    U, V, P, Q, S = data(r)
    assert 1 in P and -1 in P and 0 in S
    assert len(P) == len(Q) == r*(r-1) and len(S) == r*r
    # Laurent-polynomial determinant identity: (f_U+r)(f_V+r)=g(z)g(z^-1).
    L = Counter()
    for x in P | {0}:
        for y in Q | {0}:
            L[x+y] += (r if x == 0 else 1)*(r if y == 0 else 1)
    R = Counter(x-y for x in S for y in S)
    assert L == R
    # Laurent-polynomial eigenvector (v(z), -u(z^-1)) for energy -r.
    a = {v: 1 for v in V}
    b = {-u: -1 for u in U}
    out_a = Counter()
    out_b = Counter()
    for j, coeff in a.items():
        out_a[j] += r * coeff
        for shift in P:
            out_a[j+shift] += coeff
        for shift in S:
            out_b[j-shift] += coeff
    for j, coeff in b.items():
        out_b[j] += r * coeff
        for shift in Q:
            out_b[j+shift] += coeff
        for shift in S:
            out_a[j+shift] += coeff
    assert not any(out_a.values()) and not any(out_b.values())
    return len(P), len(Q), len(S)


if __name__ == '__main__':
    for r in range(2, 9):
        print('r=%d: within-A=%d within-B=%d cross=%d OK' % ((r,) + check(r)))
    assert data(3)[0] == {0,1,3}
    assert data(3)[1] == {0,8,24}
    print('VERIFY_OK exact_Laurent_and_compact_eigenvector r=2..8')
