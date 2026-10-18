#!/usr/bin/env python3
"""Exact row-sum, Rayleigh-defect checks and independent finite eigenvalue tests.

The checks illustrate, but do not replace, the proof for all matrix sizes.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt


def pair_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def pair_mul(x, y, h, q):
    return (x[0] * y[0] + x[1] * y[1] * q,
            x[0] * y[1] + x[1] * y[0] + x[1] * y[1] * h)


def evaluate_rayleigh(matrix, vec, h, q):
    out = (F(0), F(0))
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            out = pair_add(out, pair_mul(pair_mul(vec[i], (value, F(0)), h, q), vec[j], h, q))
    return out


def star(h, leaves):
    n = len(leaves) + 1
    mat = [[F(0) for _ in range(n)] for _ in range(n)]
    mat[0][0] = h
    for i, lval in enumerate(leaves, 1):
        mat[0][i] = lval
        mat[i][0] = lval
    return mat


def build_perturbation(h, leaves, rng):
    mat = star(h, leaves)
    m = len(leaves)
    for i in range(m):
        x = leaves[i] * F(rng.randrange(0, 5), 20)
        mat[i + 1][i + 1] = x
    for i in range(m):
        for j in range(i + 1, m):
            x = min(leaves[i], leaves[j]) * F(rng.randrange(0, 3), 20 * m)
            mat[i + 1][j + 1] = x
            mat[j + 1][i + 1] = x
    for i, leaf in enumerate(leaves, 1):
        mat[0][i] = leaf - sum(mat[i][j] for j in range(1, m + 1))
        mat[i][0] = mat[0][i]
        assert mat[0][i] >= 0
    mat[0][0] = h + sum(leaves) - sum(mat[0][1:])
    return mat


def eigmax_jacobi(a):
    b = [[float(v) for v in row] for row in a]
    n = len(b)
    for _ in range(100 * n * n):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)),
                   key=lambda ij: abs(b[ij[0]][ij[1]]))
        if abs(b[p][q]) < 1e-13:
            break
        t = (b[q][q] - b[p][p]) / (2 * b[p][q])
        tau = 1.0 / (abs(t) + sqrt(t*t + 1.0))
        if t < 0:
            tau = -tau
        c = 1.0 / sqrt(1 + tau*tau)
        s = tau * c
        app, aqq, apq = b[p][p], b[q][q], b[p][q]
        b[p][p] = app - tau * apq
        b[q][q] = aqq + tau * apq
        b[p][q] = b[q][p] = 0.0
        for k in range(n):
            if k != p and k != q:
                akp, akq = b[k][p], b[k][q]
                b[k][p] = b[p][k] = c * akp - s * akq
                b[k][q] = b[q][k] = s * akp + c * akq
    else:
        raise AssertionError('Jacobi diagonalization did not converge')
    return max(b[i][i] for i in range(n))


def check(h, leaves, rng):
    assert h >= 0 and len(leaves) >= 2 and min(leaves) > 0
    q = sum((li*li for li in leaves), F(0))
    lam = (float(h) + sqrt(float(h*h + 4*q)))/2
    assert lam > max(map(float, leaves))
    vec = [(F(0), F(1))] + [(li, F(0)) for li in leaves]
    nominal = star(h, leaves)
    expected_rows = [h + sum(leaves)] + leaves
    tests = [nominal] + [build_perturbation(h, leaves, rng) for _ in range(10)]
    for mat in tests:
        assert all(sum(row) == expected_rows[i] for i, row in enumerate(mat))
        assert all(v >= 0 for row in mat for v in row)
        assert all(mat[i][j] == mat[j][i] for i in range(len(mat)) for j in range(len(mat)))
        actual_diff = tuple(a-b for a,b in zip(evaluate_rayleigh(mat, vec, h, q),
                                                evaluate_rayleigh(nominal, vec, h, q)))
        expected_diff = (F(0), F(0))
        for i, li in enumerate(leaves, 1):
            x = ( -li, F(1))
            expected_diff = pair_add(expected_diff,
                pair_mul((mat[i][i], F(0)), pair_mul(x, x, h, q), h, q))
            for j in range(i+1, len(mat)):
                xj = (-leaves[j-1], F(1))
                expected_diff = pair_add(expected_diff,
                    pair_mul((2*mat[i][j], F(0)), pair_mul(x, xj, h, q), h, q))
        assert actual_diff == expected_diff, (h, leaves, actual_diff, expected_diff)
        eig = eigmax_jacobi(mat)
        deficit = (float(actual_diff[0]) + float(actual_diff[1])*lam) / (lam*lam + float(q))
        assert eig + 1e-10 >= lam + deficit, (eig, lam, deficit)
        if mat == nominal:
            assert abs(eig-lam) < 1e-10
        elif any(mat[i][j]>0 for i in range(1,len(mat)) for j in range(1,len(mat))):
            assert eig > lam + 1e-10
    return len(tests)


def main():
    rng=Random(73109)
    total=0
    for m in range(2,7):
        for k in range(9):
            leaves = [F(1 + rng.randrange(1,16), 10 + rng.randrange(0,7)) for _ in range(m)]
            h = F(rng.randrange(0,30), 10)
            total += check(h, leaves, rng)
    leaves = [F(2,5), F(2,5)]
    h = F(17,25)
    nominal = star(h,leaves)
    assert nominal == [[F(17,25),F(2,5),F(2,5)],
                       [F(2,5),F(0),F(0)],
                       [F(2,5),F(0),F(0)]]
    assert h + sum(v*v for v in leaves) == 1
    pert = [[F(22,25),F(3,10),F(3,10)],
            [F(3,10),F(0),F(1,10)],
            [F(3,10),F(1,10),F(0)]]
    assert eigmax_jacobi(pert) > 1
    assert abs(eigmax_jacobi(nominal)-1) < 1e-12
    q=sum((li*li for li in leaves),F(0))
    vec=[(F(0),F(1))]+[(li,F(0)) for li in leaves]
    dv=tuple(x-y for x,y in zip(evaluate_rayleigh(pert,vec,h,q),
                                 evaluate_rayleigh(nominal,vec,h,q)))
    assert (dv[0]+dv[1])/(1+q)==F(3,55)
    print('VERIFY_OK: %d exact symmetric row-sum/Rayleigh identities and numerical eigenvalue checks; sharp three-type threshold and stability 3/55' % total)

if __name__ == '__main__':
    main()
