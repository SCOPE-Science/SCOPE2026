"""Exact rational checks for the trace-matched Lanczos covariance rank example.

Run with Python 3, standard library only. All arithmetic is rational.
"""
from fractions import Fraction as F


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return list(map(list, zip(*A)))


def invert(A):
    n = len(A)
    Q = [row[:] + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(A)]
    for j in range(n):
        k = next(i for i in range(j, n) if Q[i][j] != 0)
        Q[j], Q[k] = Q[k], Q[j]
        a = Q[j][j]
        Q[j] = [x / a for x in Q[j]]
        for i in range(n):
            if i != j:
                a = Q[i][j]
                Q[i] = [x - a * y for x, y in zip(Q[i], Q[j])]
    return [row[n:] for row in Q]


def determinant(A):
    if len(A) == 1:
        return A[0][0]
    return sum((-1) ** j * A[0][j] * determinant(
        [row[:j] + row[j+1:] for row in A[1:]])
        for j in range(len(A)))


def quadratic(A, v):
    return matmul([v], matmul(A, transpose([v])))[0][0]


def reconstruct(eps):
    # Lanczos q_1=e_1, m=1, beta_1=1, beta_2=eps.
    A = [[F(2), F(1), F(0)],
         [F(1), F(2), eps],
         [F(0), eps, F(2)]]
    S = [[F(3, 2), eps], [eps, F(2)]]
    B = invert(S)
    B2, B3 = matmul(B, B), matmul(matmul(B, B), B)
    p1, p2, p3 = B[0][0], B2[0][0], B3[0][0]
    sigma = p3 / p2
    omega = B[0][0] + B[1][1] - sigma
    v = [B[0][0], B[1][0]]
    Rhat = [[F(0)] * 3 for _ in range(3)]
    Rhat[0][0] = p1 / 4
    for j in range(2):
        Rhat[0][j+1] = Rhat[j+1][0] = -v[j] / 2
        for k in range(2):
            Rhat[j+1][k+1] = (omega * int(j == k)
                             + (sigma - omega) * v[j] * v[k] / p2)
    Rtrue = invert(A)
    Rtrue[0][0] -= F(1, 2)
    return A, Rtrue, Rhat, (p1, p2, p3, sigma, omega)


def main():
    A, R, H, p = reconstruct(F(1))
    assert p == (F(1), F(5, 4), F(27, 16), F(27, 20), F(2, 5))
    assert H == [[F(1, 4), -F(1, 2), F(1, 4)],
                 [-F(1, 2), F(29, 25), -F(19, 50)],
                 [F(1, 4), -F(19, 50), F(59, 100)]]
    assert determinant(R) == 0
    assert determinant(H) == F(1, 100)
    assert all(determinant([row[:k] for row in H[:k]]) > 0 for k in (1, 2, 3))
    observed = [F(2), F(1), F(0)]
    assert matmul(R, transpose([observed])) == [[0], [0], [0]]
    assert quadratic(H, observed) == F(4, 25)
    checks = 10
    # Additional exact-rational SPD Jacobi family, with nonterminating residual.
    for eps in (F(1, 40), F(1, 7), F(1, 2), F(1), F(6, 5)):
        A, R, H, p = reconstruct(eps)
        assert determinant(A) == F(2) * (F(3) - eps ** 2)
        assert determinant(R) == 0
        assert determinant(H) == eps**2 / (2 * (3-eps**2) * (4+eps**2)**2)
        assert all(determinant([row[:k] for row in H[:k]]) > 0 for k in (1, 2, 3))
        assert quadratic(H, [F(2), F(1), F(0)]) == 4*eps**2 / (eps**2 + 4)**2
        checks += 5
    print('PASS: exact-rational 3x3 certificate and five positive-definite cases')

if __name__ == '__main__':
    main()
