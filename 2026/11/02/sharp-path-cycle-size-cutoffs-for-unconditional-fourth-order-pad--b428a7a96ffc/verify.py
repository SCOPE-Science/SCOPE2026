"""Finite exact-rational checks for the homogeneous path cutoff."""
from fractions import Fraction as F


def solve(a, b):
    """Solve with exact arithmetic for one or several right-hand sides."""
    n = len(a)
    aug = [[F(v) for v in row + rhs] for row, rhs in zip(a, b)]
    for j in range(n):
        i = next(i for i in range(j, n) if aug[i][j])
        aug[i], aug[j] = aug[j], aug[i]
        p = aug[j][j]
        aug[j] = [v / p for v in aug[j]]
        for i in range(n):
            if i != j and aug[i][j]:
                p = aug[i][j]
                aug[i] = [v - p * w for v, w in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def laplacian(n):
    return [[int(i == j) * (1 + int(0 < i < n-1)) - int(abs(i-j) == 1)
             for j in range(n)] for i in range(n)]


def pade(lap, t):
    n = len(lap)
    def poly(sgn, i, j):
        squared = sum(lap[i][k] * lap[k][j] for k in range(n))
        return 12 * int(i == j) + sgn * 6 * t * lap[i][j] + t*t*squared
    return solve([[poly(1, i, j) for j in range(n)] for i in range(n)],
                 [[poly(-1, i, j) for j in range(n)] for i in range(n)])


def q(t):
    return t*t + 6*t + 12


if __name__ == '__main__':
    for n in range(2, 11):
        lap = laplacian(n)
        # Impose zero mean in place of the redundant last Laplacian equation.
        a = lap[:-1] + [[1]*n]
        b = [[F(int(j == 0)) - F(1,n)] for j in range(n-1)] + [[0]]
        u = solve(a, b)
        assert u[1][0] == F((n-1)*(2*n-7), 6*n)
        if n >= 4:
            assert pade(lap, F(10000))[0][1] < 0
    for t in (F(0), F(1,100), F(1,2), F(2), F(100)):
        for n in (2, 3):
            m = pade(laplacian(n), t)
            assert m[0][1] == 12*t/q(n*t)
            if n == 3:
                assert m[1][2] == m[0][1]
                assert m[0][2] == 6*t*(1/q(t) - 1/q(3*t))
            assert all(sum(row) == 1 for row in m)
            assert all(m[i][j] == m[j][i] for i in range(n) for j in range(n))
            assert all(v >= 0 and (v > 0 or t == 0) for row in m for v in row)
    print('PASS: 9 path coefficients, 10 small-path kernels, 7 large-step witnesses')
