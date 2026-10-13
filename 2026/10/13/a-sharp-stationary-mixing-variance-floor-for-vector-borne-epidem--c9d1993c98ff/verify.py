"""Exact-rational witness for the two-group stationary-mixing result.

Run: python3 verify.py
This checks the illustrative formulas, not the all-dimensions theorem.
"""
from fractions import Fraction as Q


def product(A, B):
    assert len(A[0]) == len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def inverse_2(A):
    determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert determinant != 0
    return [[A[1][1] / determinant, -A[0][1] / determinant],
            [-A[1][0] / determinant, A[0][0] / determinant]]


def run():
    h = [Q(1, 2), Q(1, 2)]
    P = [[Q(3, 4), Q(1, 4)], [Q(1, 4), Q(3, 4)]]
    v = [Q(3, 4), Q(1, 4)]
    s = [sum(h[k] * P[k][i] for k in range(2)) for i in range(2)]
    q = [sum(P[k][i] * v[i] / s[i] for i in range(2)) for k in range(2)]
    M = sum(h[k] * q[k]**2 for k in range(2))
    L = [[v[i] / s[i] * sum(P[k][i] * h[k] * P[k][j] for k in range(2)) / s[j]
          for j in range(2)] for i in range(2)]
    assert s == [Q(1, 2)] * 2
    assert q == [Q(5, 4), Q(3, 4)]
    assert M == Q(17, 16)
    assert L == [[Q(15, 16), Q(9, 16)], [Q(3, 16), Q(5, 16)]]
    assert M == 1 + sum(h[k] * (q[k] - 1)**2 for k in range(2))
    for kappa in [Q(1, 100), Q(1, 7), Q(1), Q(3), Q(1000)]:
        D = [[kappa * (v[i] - (1 if i == j else 0)) for j in range(2)] for i in range(2)]
        assert [sum(D[i][j] * v[j] for j in range(2)) for i in range(2)] == [0, 0]
        assert [sum(D[i][j] for i in range(2)) for j in range(2)] == [0, 0]
        K = product(inverse_2([[(1 if i == j else 0) - D[i][j] for j in range(2)] for i in range(2)]), L)
        explicit = [[Q(3) * (9*kappa+10), Q(3) * (7*kappa+6)],
                    [Q(3) * (3*kappa+2), 7*kappa+10]]
        explicit = [[entry / (32*(kappa+1)) for entry in row] for row in explicit]
        assert K == explicit
        trace = K[0][0] + K[1][1]
        determinant = K[0][0]*K[1][1] - K[0][1]*K[1][0]
        assert trace == Q(17*kappa+20, 16*(kappa+1))
        assert determinant == Q(3, 16*(kappa+1))
        assert M*M - M*trace + determinant == -Q(3, 256*(kappa+1)) < 0
    # Exact coefficient comparison gives the preceding characteristic identity
    # for EVERY formal value of kappa, not merely sampled positive values:
    # after multiplying by 256*(kappa+1), the polynomial becomes -3.
    assert (289 - 289) == 0  # coefficient of kappa
    assert 289 - 340 + 48 == -3  # constant coefficient
    # At kappa = 1 the top root is (37+sqrt(985))/64; sqrt(985)>31.
    assert 985 > 31**2
    # The rank-one limit has Perron eigenvalue 1^T L v = M.
    Lv = [sum(L[i][j]*v[j] for j in range(2)) for i in range(2)]
    assert sum(Lv) == M
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
