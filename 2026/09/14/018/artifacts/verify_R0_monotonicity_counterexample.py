"""Exact integer-arithmetic verification of the 2-patch R0-monotonicity counterexample.

No floating point is used for any proof step; all certificates are Fraction
objects or integer square comparisons.
"""
from fractions import Fraction


def main():
    # Parameters
    beta = [Fraction(8), Fraction(4)]
    sigma = [Fraction(1), Fraction(1)]
    gamma = [Fraction(1), Fraction(1)]
    mu = [Fraction(1), Fraction(1)]
    Lambda = [Fraction(1), Fraction(1)]
    # MS = C = [[-1,1],[1,-1]]
    MS = [[Fraction(-1), Fraction(1)], [Fraction(1), Fraction(-1)]]
    C = [row[:] for row in MS]

    # 1. C / MS checks: zero column sums, off-diagonal >= 0, irreducible (1<->2)
    for j in range(2):
        assert MS[0][j] + MS[1][j] == 0, "column sum"
        assert C[0][j] + C[1][j] == 0, "column sum"
    assert MS[0][1] > 0 and MS[1][0] > 0, "irreducible 2-node digraph"
    assert C[0][1] > 0 and C[1][0] > 0
    assert MS[0][0] < 0 and MS[1][1] < 0

    # 2. DFE uniqueness: (mu*I - MS) S0 = Lambda; det = 3 != 0; S0 = (1,1)
    # mu*I - MS = [[2,-1],[-1,2]]
    detM = Fraction(2) * Fraction(2) - Fraction(1) * Fraction(1)
    assert detM == 3, detM
    S0 = [Fraction(1), Fraction(1)]
    # verify equation
    for i in range(2):
        lhs = mu[i] * S0[i] - (MS[i][0] * S0[0] + MS[i][1] * S0[1])
        assert lhs == Lambda[i], (i, lhs)
    N0 = S0[:]
    print("DFE S0 =", S0, "det(muI-MS) =", detM)

    # 3. Isolated patch risks r_i = beta_i*(S0/N0)*sigma/((sigma+mu)(gamma+mu))
    r = []
    for i in range(2):
        num = beta[i] * (S0[i] / N0[i]) * sigma[i]
        den = (sigma[i] + mu[i]) * (gamma[i] + mu[i])
        r.append(num / den)
    print("isolated risks =", r)
    assert r[0] == 2 and r[1] == 1, r
    assert r[0] != r[1], "heterogeneous"

    # 4. NGM reduction quantities: D = diag(beta*S0/N0*sigma/(gamma+mu)), P = sigma+mu
    D = [beta[i] * (S0[i] / N0[i]) * sigma[i] / (gamma[i] + mu[i]) for i in range(2)]
    P = [sigma[i] + mu[i] for i in range(2)]
    print("D =", D, "P =", P)
    assert D == [Fraction(4), Fraction(2)], D
    assert P == [Fraction(2), Fraction(2)], P

    def H_of(m):
        m = Fraction(m)
        A = [[P[0] + m, -m], [-m, P[1] + m]]  # P*I - m*C since C=[[-1,1],[1,-1]]
        detA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        assert detA > 0, detA
        invA = [[A[1][1] / detA, -A[0][1] / detA],
                [-A[1][0] / detA, A[0][0] / detA]]
        H = [[D[0] * invA[0][0], D[0] * invA[0][1]],
             [D[1] * invA[1][0], D[1] * invA[1][1]]]
        T = H[0][0] + H[1][1]
        Det = H[0][0] * H[1][1] - H[0][1] * H[1][0]
        return H, T, Det, detA

    # m1 = 0
    H0, T0, Det0, detA0 = H_of(0)
    print("m=0: H =", H0, "T =", T0, "Det =", Det0, "detA =", detA0)
    assert H0 == [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(1)]]
    assert T0 == 3 and Det0 == 2
    R0_m1 = Fraction(2)  # eigenvalues 2, 1
    # characteristic at lambda=2: 4 - 3*2 + 2 = 0
    assert R0_m1 * R0_m1 - T0 * R0_m1 + Det0 == 0
    print("R0(0) = 2 exactly")

    # m2 = 1
    H1, T1, Det1, detA1 = H_of(1)
    print("m=1: H =", H1, "T =", T1, "Det =", Det1, "detA =", detA1)
    assert detA1 == 8
    assert H1 == [[Fraction(3, 2), Fraction(1, 2)],
                  [Fraction(1, 4), Fraction(3, 4)]]
    assert T1 == Fraction(9, 4) and Det1 == 1
    Disc = T1 * T1 - 4 * Det1
    print("discriminant =", Disc)
    assert Disc == Fraction(17, 16)
    assert Disc > 0  # real distinct roots
    # Larger root is (T + sqrt(Disc))/2 = (9 + sqrt(17))/8.
    # Certificate sqrt(17) < 5 via 17 < 25 (integer arithmetic).
    assert 17 < 25
    # Hence R0(1) = (9+sqrt17)/8 < (9+5)/8 = 7/4 < 2 = R0(0).
    assert Fraction(7, 4) < R0_m1
    print("R0(1) = (9+sqrt(17))/8 < 7/4 < 2 = R0(0)")
    print("m1=0 < m2=1 but R0(m1) > R0(m2): strict-increase claim FALSE")

    # Extra interior point (not needed for proof, consistency check)
    Hh, Th, Deth, _ = H_of(Fraction(1, 10))
    print("m=0.1: H =", Hh, "T =", Th, "Det =", Deth)

    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
