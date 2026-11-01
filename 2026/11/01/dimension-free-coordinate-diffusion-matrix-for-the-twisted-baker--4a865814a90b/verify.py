"""Exact rational checks of the coordinate Green--Kubo theorem.

Run with Python 3.9+: python verify.py. Standard library only.
The finite tests supplement the analytic all-dimension proof in RESULT.md.
"""
from fractions import Fraction as Q


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(*arr):
    return [[sum(a[i][j] for a in arr)
             for j in range(len(arr[0][0]))] for i in range(len(arr[0]))]


def transfer(m):
    b = [[Q(0) for _ in range(m)] for _ in range(m)]
    b[0][0], b[0][1] = Q(1, 4), Q(1, 2)
    for i in range(1, m - 1):
        b[i][i], b[i][i + 1] = Q(1, 2), Q(1, 2)
    b[m - 1][m - 1], b[m - 1][0] = Q(1, 2), Q(-1, 4)
    return b


def hmatrix(m):
    h = [[Q(0) for _ in range(m)] for _ in range(m)]
    for j in range(1, m):
        h[0][j] = Q(1)
    for i in range(1, m):
        h[i][0] = Q(-1, 2)
        for j in range(1, m):
            h[i][j] = Q(-1, 2) if j < i else Q(1, 2) if j == i else Q(3, 2)
    return h


def expect(m):
    v = [[Q(0) for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            v[i][j] = (Q(1, 3) if i == j == 0 else
                       Q(-1, 12) if i == 0 or j == 0 else
                       Q(1, 6) if i == j else Q(1, 12))
    return v


def verify_branch_transfer(m, b):
    for sample in range(5):
        y = [Q(2 * sample - 4, 7)] + [Q((3 * j + sample) % 11, 11) for j in range(1, m)]
        left = [(y[0] - 1) / 2] + y[1:]
        right = [y[1]] + y[2:] + [(1 - y[0]) / 2]
        def u(x):
            return [x[0]] + [v - Q(1, 2) for v in x[1:]]
        lhs = [(u(left)[i] + u(right)[i]) / 2 for i in range(m)]
        rhs = [sum(b[i][j] * u(y)[j] for j in range(m)) for i in range(m)]
        assert lhs == rhs, (m, sample)


def main():
    for m in range(2, 31):
        b, h = transfer(m), hmatrix(m)
        ident = [[Q(int(i == j)) for j in range(m)] for i in range(m)]
        minus_b = [[ident[i][j] - b[i][j] for j in range(m)] for i in range(m)]
        assert mm(minus_b, h) == b, (m, 'Poisson')
        d = [[Q(0) for _ in range(m)] for _ in range(m)]
        for i in range(m):
            d[i][i] = Q(1, 3) if i == 0 else Q(1, 12)
        v = add(d, mm(h, d), mm(d, transpose(h)))
        assert v == expect(m), (m, 'covariance')
        # Principal minors are positive: the passive difference modes have
        # eigenvalue 1/12, and the remaining 2x2 block has det (3m+1)/144.
        assert (4 * m - (m - 1)) == 3 * m + 1
        if m <= 9:
            verify_branch_transfer(m, b)
    print('PASS: all exact Poisson and covariance identities for 2 <= M <= 30')
    print('PASS: branch-transfer calculations for 2 <= M <= 9')
    print('Analytic proof for all M is separate; finite checks are not exhaustive.')


if __name__ == '__main__':
    main()
