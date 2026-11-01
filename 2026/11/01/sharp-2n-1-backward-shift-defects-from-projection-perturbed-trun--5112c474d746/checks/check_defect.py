"""Exact-rational checks for finite-model Toeplitz projection-perturbation kernels.

Run: python3 check_defect.py
This verifies finite instances only; the parameter-uniform proof is in RESULT.md.
"""
from fractions import Fraction


def rank(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    p = 0
    for c in range(cols):
        pivot = next((i for i in range(p, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[p], a[pivot] = a[pivot], a[p]
        scale = a[p][c]
        a[p] = [v / scale for v in a[p]]
        for i in range(rows):
            if i == p or not a[i][c]:
                continue
            mul = a[i][c]
            a[i] = [x - mul * y for x, y in zip(a[i], a[p])]
        p += 1
        if p == rows:
            break
    return p


def matmul(a, b):
    assert len(a[0]) == len(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def check(n):
    r = 2*n + 2
    m = 2*r
    a = [[0]*m for _ in range(m)]
    p = [[0]*m for _ in range(m)]
    t = [[0]*m for _ in range(m)]
    backward = [[0]*m for _ in range(m)]
    l = [[0]*m for _ in range(r)]
    b = [[0]*r for _ in range(m)]
    for i in range(r):
        a[r+i][i] = 1
        l[i][i] = 1
    for j in range(1, n+1):
        k = r+2*j
        p[k][k] = 1
        l[2*j][k] = -1
    for i in range(m):
        for j in range(m):
            t[i][j] = a[i][j]-p[i][j]
    for i in range(1, m):
        backward[i-1][i] = 1
    for k in range(r):
        b[r+k][k] = 1
    for j in range(1, n+1):
        b[2*j][2*j] = 1
    defect = matmul(l, matmul(backward,b))
    expected = [[0]*r for _ in range(r)]
    for j in range(1,n+1):
        expected[2*j-1][2*j] = 1
        expected[2*j][2*j+1] = -1
    expected[r-1][0] = 1
    assert defect == expected
    assert rank(p) == n
    assert all(p[i][j] == p[j][i] for i in range(m) for j in range(m))
    assert matmul(p,p) == p
    assert matmul(t,b) == [[0]*r for _ in range(m)]
    assert matmul(l,b) == [[0]*r for _ in range(r)]
    assert rank(t) == r
    assert rank(l) == r
    assert rank(b) == r
    assert b[0] == [0]*r
    assert rank(defect) == 2*n+1
    return m,r,rank(defect)


if __name__ == '__main__':
    for n in range(1,11):
        m,r,d = check(n)
        print('n=%d model_dimension=%d kernel_dimension=%d minimal_defect=%d' % (n,m,r,d))
    print('PASS: all exact-rational checks for n=1,...,10')
