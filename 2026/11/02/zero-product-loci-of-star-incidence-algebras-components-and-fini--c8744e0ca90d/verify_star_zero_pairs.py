#!/usr/bin/env python3
"""Finite-field checks for annihilating pairs in star incidence matrix algebras.

Uses direct matrix multiplication, independent component-equation tests,
including a binary degree-two extension field. No third-party dependencies.
"""
from itertools import product
from math import comb


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def neg(a, q):
    return a if q == 4 else (-a) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    out = 0
    aa, bb = a, b
    while bb:
        if bb & 1:
            out ^= aa
        bb >>= 1
        aa <<= 1
        if aa & 4:
            aa ^= 7  # x^2 + x + 1
    return out


def rows(coords, r):
    n = r + 1
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        out[i][i] = coords[i]
    for i in range(1, n):
        out[0][i] = coords[n + i - 1]
    return out


def zero_product(a, b, r, q):
    A, B = rows(a, r), rows(b, r)
    n = r + 1
    for i in range(n):
        for j in range(n):
            z = 0
            for k in range(n):
                z = add(z, mul(A[i][k], B[k][j], q), q)
            if z:
                return False
    return True


def membership(a, b, r, q):
    n = r + 1
    x, y = a[0], b[0]
    X, Z = set(), set()
    for S in range(1 << r):
        if y:
            continue
        ok = True
        for i in range(r):
            ai, bi = a[i + 1], b[i + 1]
            alpha, beta = a[n + i], b[n + i]
            if (S >> i) & 1:
                if ai or add(mul(x, beta, q), mul(alpha, bi, q), q):
                    ok = False
                    break
            elif bi or beta:
                ok = False
                break
        if ok:
            X.add(S)
    for T in range(1 << r):
        if x:
            continue
        ok = True
        for i in range(r):
            ai, bi, alpha = a[i + 1], b[i + 1], a[n + i]
            if (T >> i) & 1:
                if ai or alpha:
                    ok = False
                    break
            elif bi:
                ok = False
                break
        if ok:
            Z.add(T)
    return X, Z


def formula(q, r):
    return (q - 1) * (q * (2 * q - 1)) ** r + q * (q * (q*q + q - 1)) ** r


def witness(r, kind, mask, q):
    n = r + 1
    a, b = [0] * (2*r + 1), [0] * (2*r + 1)
    if kind == 'X':
        a[0] = 1
        for i in range(r):
            if (mask >> i) & 1:
                b[i+1] = 1
                a[n+i] = 1
                b[n+i] = neg(1, q)
            else:
                a[i+1] = 1
                a[n+i] = 1
    else:
        b[0] = 1
        for i in range(r):
            if (mask >> i) & 1:
                b[i+1] = b[n+i] = 1
            else:
                a[i+1] = a[n+i] = b[n+i] = 1
    return tuple(a), tuple(b)


def run(q, r):
    d = 2*r + 1
    elements = list(product(range(q), repeat=d))
    total = 0
    for a in elements:
        for b in elements:
            product_is_zero = zero_product(a, b, r, q)
            X, Z = membership(a, b, r, q)
            if product_is_zero != bool(X or Z):
                raise AssertionError(('component cover', q, r, a, b, product_is_zero, X, Z))
            total += product_is_zero
    expected = formula(q, r)
    if total != expected:
        raise AssertionError(('point count', q, r, total, expected))
    for kind in ('X', 'Z'):
        for mask in range(1 << r):
            a, b = witness(r, kind, mask, q)
            if not zero_product(a, b, r, q):
                raise AssertionError(('witness product', q, r, kind, mask))
            X, Z = membership(a, b, r, q)
            if (X, Z) != (({mask}, set()) if kind == 'X' else (set(), {mask})):
                raise AssertionError(('component witness', q, r, kind, mask, X, Z))
    print(f'q={q} r={r}: zero_product_pairs={total}, components={2**(r+1)}, dimensions='+str([2*r+1]*2**r + [3*r+1-j for j in range(r+1) for _ in range(comb(r,j))]))


if __name__ == '__main__':
    cases = [(2,1), (2,2), (2,3), (2,4), (3,1), (3,2), (4,1), (5,1), (7,1)]
    for q, r in cases:
        run(q, r)
    print('STAR_INCIDENCE_ZERO_PRODUCT_GEOMETRY_OK', len(cases))
