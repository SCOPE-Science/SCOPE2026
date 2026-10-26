"""Exact arithmetic replay for two nonsymmetric Dirichlet Laplacians.

The infinite-dimensional assertions are proved in RESULT.md. These checks verify
matrix coefficients and discrete energy identities on a finite test range.
"""
from fractions import Fraction as F
import random

BOUNDARY = {'BH': (24, -12, 0, 0), 'OS': (20, -6, -4, 1)}
DEFECT = {'BH': (-5, 4, -1, 0), 'OS': (-9, 10, -5, 1)}


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def build(n, name):
    D = [[(2 if i == j else -1 if abs(i - j) == 1 else 0)
          for j in range(n)] for i in range(n)]
    D2 = mm(D, D)
    B = [[12 * D[i][j] + D2[i][j] for j in range(n)]
         for i in range(n)]
    for i in (0, n - 1):
        for j in range(n):
            B[i][j] = 0
    b = BOUNDARY[name]
    for j, val in enumerate(b):
        B[0][j] = val
        B[n - 1][n - 1 - j] = val
    return D, D2, B


def quad(A, v):
    return sum(v[i] * A[i][j] * v[j] for i in range(len(v)) for j in range(len(v)))


def checksum(n, name, v):
    D, D2, B = build(n, name)
    defect = DEFECT[name]
    Bcore = [[12 * D[i][j] + D2[i][j] for j in range(n)]
             for i in range(n)]
    R = [[B[i][j] - Bcore[i][j] for j in range(n)] for i in range(n)]
    expect = [[0] * n for _ in range(n)]
    for j in range(4):
        expect[0][j] += defect[j]
        expect[-1][-j-1] += defect[j]
    assert R == expect
    assert quad(B, v) == 12 * quad(D, v) + quad(D2, v) + \
        v[0] * sum(defect[j] * v[j] for j in range(4)) + \
        v[-1] * sum(defect[j] * v[-j-1] for j in range(4))
    dv = [v[0]] + [v[i] - v[i-1] for i in range(1, n)] + [-v[-1]]
    assert sum(a*a for a in dv) == quad(D, v)
    assert sum(a*a for a in [sum(D[i][j]*v[j] for j in range(n)) for i in range(n)]) == quad(D2, v)
    assert quad(B, v) >= quad(D, v) + quad(D2, v)


def check_local_identity(name, a):
    # Exact completion of squares yielding q >= -(11/2) sum |d_j|^2.
    a = [F(t) for t in a]
    if name == 'BH':
        q = -2*a[0]**2 + 3*a[0]*a[1] - a[0]*a[2]
        sos = F(67,22)*a[0]**2 + F(11,2)*((a[1] + F(3,11)*a[0])**2 + (a[2] - F(1,11)*a[0])**2)
        assert q + F(11,2)*sum(t*t for t in a[:3]) == sos
    else:
        q = -3*a[0]**2 + 6*a[0]*a[1] - 4*a[0]*a[2] + a[0]*a[3]
        sos = F(1,11)*a[0]**2 + F(11,2)*((a[1]+F(6,11)*a[0])**2 + (a[2]-F(4,11)*a[0])**2 + (a[3]+F(1,11)*a[0])**2)
        assert q + F(11,2)*sum(t*t for t in a[:4]) == sos
    return True


def main():
    rng = random.Random(20260926)
    cases = 0
    for name in BOUNDARY:
        for _ in range(300):
            x = [rng.randint(-9, 9) for i in range(4)]
            assert check_local_identity(name, x)
            cases += 1
        for n in range(5, 36):
            for _ in range(8):
                v = [rng.randint(-5,5) for j in range(n)]
                checksum(n, name, v)
                cases += 1
    print(f'PASS {cases} exact local/matrix/energy checks; n=5..35.')
    print('Scope: finite replay confirms formulas; arbitrary-n coercivity follows from the analytic completion-of-squares argument.')

if __name__ == '__main__':
    main()
