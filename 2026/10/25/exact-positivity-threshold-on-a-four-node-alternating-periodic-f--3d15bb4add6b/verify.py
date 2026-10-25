from fractions import Fraction as F


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def inverse(A):
    n = len(A)
    W = [list(row) + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(A)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if W[r][col] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        W[col], W[pivot] = W[pivot], W[col]
        p = W[col][col]
        W[col] = [v / p for v in W[col]]
        for r in range(n):
            if r != col:
                f = W[r][col]
                W[r] = [W[r][j] - f * W[col][j] for j in range(2 * n)]
    return [row[n:] for row in W]


def build(a, b, tau):
    z = F(0)
    m0 = (a + b) / 3
    ma, mb = a / 6, b / 6
    k0 = 1 / a + 1 / b
    M = [
        [m0, ma, z, mb],
        [ma, m0, mb, z],
        [z, mb, m0, ma],
        [mb, z, ma, m0],
    ]
    K = [
        [k0, -1 / a, z, -1 / b],
        [-1 / a, k0, -1 / b, z],
        [z, -1 / b, k0, -1 / a],
        [-1 / b, z, -1 / a, k0],
    ]
    A = [[M[i][j] + tau * K[i][j] for j in range(4)] for i in range(4)]
    P = matmul(inverse(A), M)

    den = ((a * b + 12 * tau) * (a * a + 3 * a * b + 12 * tau)
           * (3 * a * b + b * b + 12 * tau))
    nd = (3 * a**4 * b**2 + 10 * a**3 * b**3 + 3 * a**2 * b**4
          + 36 * a**3 * b * tau + 144 * a**2 * b**2 * tau
          + 36 * a * b**3 * tau + 72 * (a**2 + b**2) * tau**2
          + 504 * a * b * tau**2 + 432 * tau**3)
    na = 6 * tau * (a**3 * b + 5 * a**2 * b**2 + 2 * a * b**3
                    + 36 * a * b * tau + 12 * b**2 * tau + 72 * tau**2)
    nb = 6 * tau * (2 * a**3 * b + 5 * a**2 * b**2 + a * b**3
                    + 12 * a**2 * tau + 36 * a * b * tau + 72 * tau**2)
    q = 72 * tau**2 + 12 * a * b * tau - a * b * (a + b)**2
    opp = 6 * tau * q
    expected = [
        [nd / den, na / den, opp / den, nb / den],
        [na / den, nd / den, nb / den, opp / den],
        [opp / den, nb / den, nd / den, na / den],
        [nb / den, opp / den, na / den, nd / den],
    ]
    assert P == expected, "displayed transition entries do not match exact matrix product"
    assert all(sum(row) == 1 for row in P), "row sums must equal one"
    return P, q


def main():
    cases = [
        (F(1), F(1), F(0)),
        (F(1), F(1), F(1, 12)),
        (F(1), F(1), F(1, 4)),
        (F(2), F(1), F(1, 4)),
        (F(2), F(1), F(1, 2)),
        (F(3, 2), F(1), F(1, 4)),
        (F(3, 2), F(1), F(1, 3)),
    ]
    for a, b, tau in cases:
        P, q = build(a, b, tau)
        if tau == 0:
            assert P == [[F(int(i == j)) for j in range(4)] for i in range(4)]
        else:
            assert (min(min(row) for row in P) >= 0) == (q >= 0)
    print("RATIONAL_SPOT_CHECKS_OK")


if __name__ == "__main__":
    main()
