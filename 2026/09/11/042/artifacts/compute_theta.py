"""Unreduced Swiatkowski complex of minimal Theta_3 (essential vertices A,B;
edges e0,e1,e2), weights k=4,5.

S(A) = Z<empty_A, v_A, a0,a1,a2>, S(B) = Z<empty_B, v_B, b0,b1,b2>,
d(a_i) = e_i - v_A, d(b_j) = e_j - v_B.

C_2(k): m*a_i*b_j, m deg k-2                    (9*s2)
C_1(k): m*a_i*empty_B, m in M1                 (3*s1)
      + m*empty_A*b_j, m in M1                 (3*s1)
      + m*a_i*v_B, m in M2                     (3*s2)
      + m*v_A*b_j, m in M2                     (3*s2)
C_0(k): m*empty*empty, m in M0                 (s0)
      + m*v_A*empty, m in M1                   (s1)
      + m*empty*v_B, m in M1                   (s1)
      + m*v_A*v_B, m in M2                     (s2)
D3 = 0 structurally (one degree-1 slot per vertex, two vertices), so
H_2(weight k) = ker(D2) subset of a free group => free abelian.

Checks: entries in {-1,0,1}, D1*D2 = 0, H0 rank == 1 (connectivity).
"""
import datetime
from sympy import Matrix


def mons(d):
    out = []
    for a in range(d + 1):
        for b in range(d - a + 1):
            out.append((a, b, d - a - b))
    return out


def emul(m, i):
    L = list(m)
    L[i] += 1
    return tuple(L)


def build(k):
    M0, M1, M2 = mons(k), mons(k - 1), mons(k - 2)
    i0 = {m: n for n, m in enumerate(M0)}
    i1 = {m: n for n, m in enumerate(M1)}
    i2 = {m: n for n, m in enumerate(M2)}
    s0, s1, s2 = len(M0), len(M1), len(M2)
    nC0, nC1, nC2 = s0 + 2 * s1 + s2, 6 * s1 + 6 * s2, 9 * s2

    def AE(i, m):
        return i * s1 + i1[m]

    def BE(j, m):
        return 3 * s1 + j * s1 + i1[m]

    def AV(i, m):
        return 6 * s1 + i * s2 + i2[m]

    def BV(j, m):
        return 6 * s1 + 3 * s2 + j * s2 + i2[m]

    def EE(m):
        return i0[m]

    def VE(m):
        return s0 + i1[m]

    def EV(m):
        return s0 + s1 + i1[m]

    def VV(m):
        return s0 + 2 * s1 + i2[m]

    D2 = [[0] * nC2 for _ in range(nC1)]
    D1 = [[0] * nC1 for _ in range(nC0)]
    for i in range(3):
        for j in range(3):
            for m in M2:
                col = (i * 3 + j) * s2 + i2[m]
                D2[BE(j, emul(m, i))][col] += 1
                D2[BV(j, m)][col] -= 1
                D2[AE(i, emul(m, j))][col] -= 1
                D2[AV(i, m)][col] += 1
    for i in range(3):
        for m in M1:
            D1[EE(emul(m, i))][AE(i, m)] += 1
            D1[VE(m)][AE(i, m)] -= 1
    for j in range(3):
        for m in M1:
            D1[EE(emul(m, j))][BE(j, m)] += 1
            D1[EV(m)][BE(j, m)] -= 1
    for i in range(3):
        for m in M2:
            D1[EV(emul(m, i))][AV(i, m)] += 1
            D1[VV(m)][AV(i, m)] -= 1
    for j in range(3):
        for m in M2:
            D1[VE(emul(m, j))][BV(j, m)] += 1
            D1[VV(m)][BV(j, m)] -= 1
    return Matrix(D1), Matrix(D2), (nC0, nC1, nC2)


report = []
report.append("theta3 Swiatkowski verification " + datetime.datetime.now(datetime.timezone.utc).isoformat())
for k in (4, 5):
    D1, D2, dims = build(k)
    nC0, nC1, nC2 = dims
    assert all(v in (-1, 0, 1) for v in D1), "D1 entries"
    assert all(v in (-1, 0, 1) for v in D2), "D2 entries"
    assert (D1 * D2).is_zero_matrix, "D1*D2 == 0"
    r1 = D1.rank()
    r2 = D2.rank()
    h0 = nC0 - r1
    h1 = (nC1 - r1) - r2
    h2 = nC2 - r2
    assert h0 == 1, f"H0 rank sanity (got {h0})"
    line = (f"k={k}: C0={nC0} C1={nC1} C2={nC2} rankD1={r1} rankD2={r2} "
            f"H0rank={h0} H1rank={h1} H2rank={h2} D1D2=0 entries_pm1_OK")
    print(line, flush=True)
    report.append(line)
report.append("H_2(weight k) = ker D2 (D3 = 0): free abelian of rank above; no torsion in any weight.")
with open("output/artifacts/verify.log", "w") as f:
    f.write("\n".join(report) + "\n")
