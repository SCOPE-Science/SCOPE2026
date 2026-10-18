#!/usr/bin/env python3
"""Exact checks for one-edge-defect cycle Laplacian controllability.

Requires Python 3 and SymPy; finite tests supplement the proof in RESULT.md.
"""
import sympy as sp


def laplacian(n, w):
    assert n >= 3
    L = sp.zeros(n)
    for i in range(n):
        j = (i + 1) % n
        edge = w if i == n - 1 else sp.Integer(1)
        L[i, i] += edge
        L[j, j] += edge
        L[i, j] -= edge
        L[j, i] -= edge
    return L


def krylov(L):
    n = L.rows
    x = sp.eye(n)[:, 0]
    cols = []
    for _ in range(n):
        cols.append(x)
        x = L * x
    return sp.Matrix.hstack(*cols)


def predicted(n, w):
    return (-1)**(n+1) * (w-1)**((n-1)//2) * (1+(n-1)*w)


def check():
    count = 0
    w = sp.symbols('w')
    for n in range(3, 7):
        K = krylov(laplacian(n, w))
        assert sp.factor(K.det(method='berkowitz') - predicted(n, w)) == 0
        count += 1

    for n in range(3, 19):
        for w in (sp.S(0), sp.Rational(1,3), sp.Rational(1,2), sp.S(1),
                  sp.Rational(3,2), sp.S(2), -sp.Rational(1,n-1)):
            K = krylov(laplacian(n, w))
            d = K.det(method='domain-ge')
            assert d == predicted(n,w), (n,w,d,predicted(n,w))
            count += 1
        K1 = krylov(laplacian(n, sp.Integer(1)))
        assert K1.rank() == n - (n-1)//2
        count += 1
    # At positive defects there is no hidden singularity; for negative
    # weight the second exceptional point agrees with the signed null mode.
    for n in range(3, 15):
        w = -sp.Rational(1, n-1)
        L = laplacian(n, w)
        assert L.nullspace().__len__() == 2
        count += 1
    print('PASS exact checks:', count)

if __name__ == '__main__':
    check()
