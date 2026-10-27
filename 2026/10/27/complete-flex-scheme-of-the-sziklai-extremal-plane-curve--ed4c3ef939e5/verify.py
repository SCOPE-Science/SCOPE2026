#!/usr/bin/env python3
"""Exact sparse-polynomial checks of the Sziklai extremal curve's Hessian.
No third-party packages, no network.  Monomials map exponent triples to F_p coefficients.
"""
from itertools import permutations


def clean(P, p):
    return {m: c % p for m, c in P.items() if c % p}


def add(A, B, p):
    d = dict(A)
    for m, v in B.items():
        d[m] = (d.get(m, 0) + v) % p
    return clean(d, p)


def mul(A, B, p):
    d = {}
    for a, u in A.items():
        for b, v in B.items():
            m = tuple(a[k] + b[k] for k in range(3))
            d[m] = (d.get(m, 0) + u * v) % p
    return clean(d, p)


def diff(A, k, p):
    d = {}
    for m, v in A.items():
        if m[k]:
            n = tuple(m[j] - (j == k) for j in range(3))
            d[n] = (d.get(n, 0) + v * m[k]) % p
    return clean(d, p)


def determinant(M, p):
    d = {}
    for perm in permutations(range(3)):
        inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        val = {(0, 0, 0): (-1) ** inv}
        for i in range(3):
            val = mul(val, M[i][perm[i]], p)
        d = add(d, val, p)
    return d


def verify(p, e):
    q = p ** e
    F = {(q, 0, 0): 1, (1, 0, q-1): -1,
         (q-1, 1, 0): 1, (0, q, 0): -1}
    H = [[diff(diff(F, i, p), j, p) for j in range(3)] for i in range(3)]
    det = determinant(H, p)
    expected = {(2*q-3, 0, q-3): 2 % p}
    assert det == expected, (p, e, det)
    # The first derivatives cannot vanish simultaneously: F_Y = X^(q-1).
    assert diff(F, 1, p) == {(q-1, 0, 0): 1}
    assert diff(F, 0, p)[(0,0,q-1)] == p-1
    # At P=(0:0:1), F|_(X=0)=-Y^q, giving full contact q.
    assert {k:v for k,v in F.items() if k[0] == 0} == {(0,q,0):-1}
    # At Q=(1:t:0), t^q-t=1, F on its tangent Y=tX is -XZ^(q-1).
    # This holds because X^q + X^(q-1)tX - (tX)^q = (1+t-t^q)X^q.
    assert q >= 3 and p % 2 == 1
    assert q*(2*q-3) + q*(q-3) == 3*q*(q-2)
    assert (q//p)*p == q
    return q, len(det), (q//p)


if __name__ == '__main__':
    for p, e in [(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(11,1),(13,1)]:
        print('VERIFIED', verify(p,e))
    print('VERIFY_OK')
