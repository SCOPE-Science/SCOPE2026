from fractions import Fraction as F


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def autocorrelation(P, f, pi, k):
    Q = [[F(int(i == j)) for j in range(3)] for i in range(3)]
    for _ in range(k):
        Q = matmul(Q, P)
    Pf = matvec(Q, f)
    mean = sum(pi[i] * f[i] for i in range(3))
    var = sum(pi[i] * (f[i] - mean) ** 2 for i in range(3))
    cov = sum(pi[i] * (f[i] - mean) * (Pf[i] - mean) for i in range(3))
    return cov / var


def check(alpha):
    P = [
        [1 - alpha, alpha, F(0)],
        [F(0), 1 - alpha, alpha],
        [alpha, F(0), 1 - alpha],
    ]
    assert all(sum(row) == 1 for row in P)
    assert all(sum(P[i][j] for i in range(3)) == 1 for j in range(3))
    assert P[0][1] > 0 and P[1][0] == 0  # nonreversible
    assert all(P[i][i] > 0 for i in range(3))  # aperiodic
    f = [F(1), F(-1, 2), F(-1, 2)]
    pi = [F(1, 3)] * 3
    rho1 = autocorrelation(P, f, pi, 1)
    rho2 = autocorrelation(P, f, pi, 2)
    assert rho1 == 1 - F(3, 2) * alpha
    assert rho2 == 1 - 3 * alpha + F(3, 2) * alpha * alpha
    tau = (1 - alpha) / alpha
    bound = (4 - 3 * alpha) ** 2 / (6 * alpha * (2 - alpha))
    gap = (4 - 6 * alpha + 3 * alpha * alpha) / (6 * alpha * (2 - alpha))
    assert bound - tau == gap and gap > 0
    return rho1, rho2, tau, bound, gap


def main():
    for a in (F(1, 4), F(1, 2), F(3, 4), F(9, 10)):
        check(a)
    rho1, rho2, tau, bound, gap = check(F(1, 2))
    assert (rho1, rho2, tau, bound, gap) == (
        F(1, 4), F(-1, 8), F(1), F(25, 18), F(7, 18)
    )
    # The quadratic numerator is strictly positive: discriminant = -12.
    assert (-6) ** 2 - 4 * 3 * 4 == -12
    print("RATIONAL_MATRIX_CHECKS_PASS alpha=1/4,1/2,3/4,9/10")
    print("UNIVERSAL_GAP_POLYNOMIAL_PASS discriminant=-12")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
