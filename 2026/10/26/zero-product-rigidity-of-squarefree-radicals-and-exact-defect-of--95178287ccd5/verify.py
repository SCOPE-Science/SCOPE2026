#!/usr/bin/env python3
"""Finite-field checks of zero-product tensors for squarefree local algebras."""
from itertools import product


def kernel_basis(matrix, q):
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivots = []
    k = 0
    for j in range(cols):
        i0 = next((i for i in range(k, rows) if a[i][j]), None)
        if i0 is None:
            continue
        a[k], a[i0] = a[i0], a[k]
        t = pow(a[k][j], -1, q)
        a[k] = [v * t % q for v in a[k]]
        for i in range(rows):
            if i != k and a[i][j]:
                s = a[i][j]
                a[i] = [(v - s * w) % q for v, w in zip(a[i], a[k])]
        pivots.append(j)
        k += 1
        if k == rows:
            break
    basis = []
    for j in range(cols):
        if j in pivots:
            continue
        v = [0] * cols
        v[j] = 1
        for i, p in enumerate(pivots):
            v[p] = (-a[i][j]) % q
        basis.append(v)
    return basis


def zero_tensor_rank(r, q):
    n = 1 << r
    echelon = {}
    for tail in product(range(q), repeat=n - 1):
        a = (0,) + tail
        if not any(a):
            continue
        multiplication = [[0] * n for _ in range(n)]
        for mask, coefficient in enumerate(a):
            if coefficient:
                for j in range(n):
                    if not (mask & j):
                        multiplication[mask | j][j] = (multiplication[mask | j][j] + coefficient) % q
        for b in kernel_basis(multiplication, q):
            v = {i * n + j: ai * bj % q
                 for i, ai in enumerate(a) for j, bj in enumerate(b) if ai * bj % q}
            while v:
                pivot = min(v)
                if pivot not in echelon:
                    inverse = pow(v[pivot], -1, q)
                    echelon[pivot] = {index: value * inverse % q
                                      for index, value in v.items() if value * inverse % q}
                    break
                factor = v[pivot]
                rr = echelon[pivot]
                v = {index: (v.get(index, 0) - factor * rr.get(index, 0)) % q
                     for index in v.keys() | rr.keys()
                     if (v.get(index, 0) - factor * rr.get(index, 0)) % q}
    return len(echelon)


def psi(a, b, r, q):
    n = 1 << r
    uv = [0] * n
    for i in range(1, n):
        for j in range(1, n):
            if i & j == 0:
                uv[i | j] = (uv[i | j] + a[i] * b[j]) % q
    return ((a[0] * b[0]) % q,
            tuple((a[0] * b[i]) % q for i in range(1, n)),
            tuple((b[0] * a[i]) % q for i in range(1, n)),
            tuple(uv[i] for i in range(1, n) if i.bit_count() >= 2))


def direct_full_check(r, q):
    n = 1 << r
    vecs = list(product(range(q), repeat=n))
    for a in vecs:
        for b in vecs:
            ab = [0] * n
            for i, ai in enumerate(a):
                if ai:
                    for j, bj in enumerate(b):
                        if bj and (i & j) == 0:
                            ab[i | j] = (ab[i | j] + ai * bj) % q
            if not any(ab):
                assert not any(psi(a, b, r, q)[0:1])
                assert all(not any(z) for z in psi(a, b, r, q)[1:])


def main():
    for r in range(1, 7):
        n = 1 << r
        target = 1 + 2 * (n - 1) + (n - r - 1)
        assert target == 3 * n - r - 2
        assert n * n - n - (n * n - target) == 2 * n - r - 2
    for r, q in [(1, 2), (1, 3), (2, 2), (2, 3), (2, 5), (3, 2), (3, 3)]:
        actual = zero_tensor_rank(r, q)
        n = 1 << r
        expected = n * n - (3 * n - r - 2)
        assert actual == expected, (r, q, actual, expected)
        print('checked r=', r, 'field=', q, 'zero-pair span rank=', actual, 'defect=', 2 * n - r - 2)
    for r, q in [(1, 2), (1, 3), (2, 2), (2, 3)]:
        direct_full_check(r, q)
    # Symmetric nonfactorization at r=2: f(x1,x2)=1 but f(1,x1*x2)=0.
    r, q, n = 2, 3, 4
    one = (1, 0, 0, 0)
    x1 = (0, 1, 0, 0)
    x2 = (0, 0, 1, 0)
    x12 = (0, 0, 0, 1)
    assert psi(x1, x2, r, q)[3] == (1,)
    assert psi(one, x12, r, q)[3] == (0,)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
