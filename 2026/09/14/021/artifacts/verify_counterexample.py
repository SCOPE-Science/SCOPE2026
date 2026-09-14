"""Verify the 2-patch SEIR bracketing-violation counterexample.

Model: infected states (E1,E2,I1,I2); F = [[0, D_beta],[0,0]];
V = [[V_E,0],[-D_sigma,V_I]]; V_E = diag(sigma+mu)+m*QE,
V_I = diag(gamma+mu)+m*QI; QE/QI Laplacian-type (zero column sums).
R0(m) = rho(K) = rho(H), H = D_beta V_I^{-1} D_sigma V_E^{-1}.

Counterexample: beta=(1,2), sigma=(3,1), mu=(2,2), gamma=(1,1),
CE=[[0,3],[0,0]] (E moves 2->1), CI=[[0,0],[3,0]] (I moves 1->2).
Isolated R0 = (1/5, 2/9); at m=1, rho(H) = (14/45+sqrt(106/2025))/2 > 2/9.
"""
from fractions import Fraction
import numpy as np

beta = (1, 2); sigma = (3, 1); mu = (2, 2); gamma = (1, 1)
CE = ((0, 3), (0, 0)); CI = ((0, 0), (3, 0))

def Qmat(C):
    n = 2
    Q = [[Fraction(0)] * n for _ in range(n)]
    for j in range(n):
        Q[j][j] = Fraction(C[0][j] + C[1][j])
        for i in range(n):
            if i != j:
                Q[i][j] = Fraction(-C[i][j])
    return Q

def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]

def inv2(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a * d - b * c
    assert det != 0
    return [[d / det, -b / det], [-c / det, a / det]]

def H_exact(m):
    m = Fraction(m)
    QE, QI = Qmat(CE), Qmat(CI)
    a = [sigma[i] + mu[i] for i in range(2)]
    b = [gamma[i] + mu[i] for i in range(2)]
    VE = mat_add([[Fraction(a[i] if i == j else 0) for j in range(2)]
                  for i in range(2)],
                 [[m * QE[i][j] for j in range(2)] for i in range(2)])
    VI = mat_add([[Fraction(b[i] if i == j else 0) for j in range(2)]
                  for i in range(2)],
                 [[m * QI[i][j] for j in range(2)] for i in range(2)])
    Db = [[Fraction(beta[0]), Fraction(0)], [Fraction(0), Fraction(beta[1])]]
    Ds = [[Fraction(sigma[0]), Fraction(0)], [Fraction(0), Fraction(sigma[1])]]
    return mat_mul(mat_mul(mat_mul(Db, inv2(VI)), Ds), inv2(VE))

def check():
    QE, QI = Qmat(CE), Qmat(CI)
    assert all(sum(Q[i][j] for i in range(2)) == 0 for Q in (QE, QI)
               for j in range(2)), "column sums must vanish"
    riso = [Fraction(beta[i] * sigma[i],
                     (sigma[i] + mu[i]) * (gamma[i] + mu[i]))
            for i in range(2)]
    assert riso == [Fraction(1, 5), Fraction(2, 9)], riso
    H0 = H_exact(0)
    assert H0[0][1] == 0 and H0[1][0] == 0
    assert H0[0][0] == riso[0] and H0[1][1] == riso[1]
    H1 = H_exact(1)
    assert H1 == [[Fraction(1, 10), Fraction(1, 20)],
                  [Fraction(1, 5), Fraction(19, 90)]], H1
    tr = H1[0][0] + H1[1][1]
    det = H1[0][0] * H1[1][1] - H1[0][1] * H1[1][0]
    assert (tr, det) == (Fraction(14, 45), Fraction(1, 90)), (tr, det)
    disc = tr * tr - 4 * det
    assert disc == Fraction(106, 2025), disc
    # rho > 2/9  <=>  sqrt(disc) > 2/15  <=>  106/2025 > 4/225 = 36/2025
    assert disc > Fraction(4, 225)
    rho = (float(tr) + float(disc) ** 0.5) / 2
    assert rho > float(max(riso)) * 1.05
    # float cross-check of the next-generation reduction
    def Qf(C):
        Q = np.zeros((2, 2))
        for j in range(2):
            Q[j, j] = C[0][j] + C[1][j]
            for i in range(2):
                if i != j:
                    Q[i, j] = -C[i][j]
        return Q
    bf = np.array(beta, float); sf = np.array(sigma, float)
    VE = np.diag(sf + mu) + Qf(np.array(CE, float))
    VI = np.diag(np.array(gamma, float) + mu) + Qf(np.array(CI, float))
    H = np.diag(bf) @ np.linalg.inv(VI) @ np.diag(sf) @ np.linalg.inv(VE)
    assert np.allclose(H, np.array([[0.1, 0.05], [0.2, 19 / 90]]))
    rho_f = float(max(abs(np.linalg.eigvals(H))))
    assert abs(rho_f - rho) < 1e-12
    print("R0^iso =", [float(x) for x in riso], " max =", float(max(riso)))
    print("H(1) =", [[float(x) for x in row] for row in H1])
    print("trace =", tr, " det =", det, " disc =", disc)
    print("R0(0) =", float(max(riso)), " R0(1) =", rho_f)
    print("VIOLATION CONFIRMED: R0(1) > max R0^iso")

if __name__ == "__main__":
    check()
