"""Build the explicit Q16 quasi-cyclic lifted-product CSS code and report parameters.
Shift matrix A (3x4, lift l=16, girth>=6 i.e. no 4-cycles):
  A = [[14,1,9,6],[12,10,6,0],[4,4,8,3]]
Symmetric lifted product with B=A:
  HX = [A (x) I | I (x) B], HZ = [I (x) B* | A* (x) I]  (* = negated shifts)
N = n1*n2*l + m1*m2*l = 256+144 = 400 qubits.
numpy + stdlib only. Deterministic.
"""
import numpy as np

A = [[14, 1, 9, 6], [12, 10, 6, 0], [4, 4, 8, 3]]
L = 16

def expand_QC(A, l):
    m, n = len(A), len(A[0])
    H = [[0] * (n * l) for _ in range(m * l)]
    for i in range(m):
        for j in range(n):
            s = A[i][j] % l
            for k in range(l):
                H[i * l + k][j * l + ((k + s) % l)] ^= 1
    return H

def expand_LP(A, B, l):
    m1, n1 = len(A), len(A[0])
    m2, n2 = len(B), len(B[0])
    Nqx = n1 * n2 * l + m1 * m2 * l
    Nrx, Nrz = m1 * n2 * l, n1 * m2 * l
    HX = [[0] * Nqx for _ in range(Nrx)]
    HZ = [[0] * Nqx for _ in range(Nrz)]
    for a in range(m1):
        for x in range(n2):
            for k in range(l):
                r = (a * n2 + x) * l + k
                for b in range(n1):
                    HX[r][(b * n2 + x) * l + ((k - A[a][b]) % l)] ^= 1
                for j in range(m2):
                    HX[r][n1 * n2 * l + (a * m2 + j) * l + ((k - B[j][x]) % l)] ^= 1
    for b in range(n1):
        for y in range(m2):
            for k in range(l):
                r = (b * m2 + y) * l + k
                for x in range(n2):
                    HZ[r][(b * n2 + x) * l + ((k + B[y][x]) % l)] ^= 1
                for a in range(m1):
                    HZ[r][n1 * n2 * l + (a * m2 + y) * l + ((k + A[a][b]) % l)] ^= 1
    return HX, HZ

def gf2_rank(mat):
    R = [row[:] for row in mat]
    m, n = len(R), len(R[0])
    r = 0
    for c in range(n):
        p = -1
        for i in range(r, m):
            if R[i][c]:
                p = i
                break
        if p < 0:
            continue
        R[r], R[p] = R[p], R[r]
        for i in range(m):
            if i != r and R[i][c]:
                for j in range(c, n):
                    R[i][j] ^= R[r][j]
        r += 1
    return r

def main():
    print("shift matrix A =", A, "lift =", L)
    HA = expand_QC(A, L)
    m, n = len(HA), len(HA[0])
    # 4-cycle check on protograph
    ncyc = 0
    for i1 in range(3):
        for i2 in range(i1 + 1, 3):
            for j1 in range(4):
                for j2 in range(j1 + 1, 4):
                    if (A[i1][j1] - A[i1][j2] - A[i2][j1] + A[i2][j2]) % L == 0:
                        ncyc += 1
    print(f"base QC: {m}x{n}, 4-cycle count = {ncyc}")
    HX, HZ = expand_LP(A, A, L)
    N = len(HX[0])
    rx, rz = gf2_rank(HX), gf2_rank(HZ)
    orth = 0
    for i in range(len(HX)):
        for j in range(len(HZ)):
            if sum(a & b for a, b in zip(HX[i], HZ[j])) % 2:
                orth += 1
    print(f"HX: {len(HX)}x{N} rank {rx} row-wt {sum(HX[0])}")
    print(f"HZ: {len(HZ)}x{N} rank {rz} row-wt {sum(HZ[0])}")
    print(f"CSS orthogonality violations: {orth}")
    print(f"n={N} k={N - rx - rz}")
    s = np.linalg.svd(np.array(HA, dtype=float), compute_uv=False)
    print("base singular values top3:", sorted(s, reverse=True)[:3])
    assert orth == 0 and N - rx - rz == 28
    print("BUILD_OK")

if __name__ == "__main__":
    main()
