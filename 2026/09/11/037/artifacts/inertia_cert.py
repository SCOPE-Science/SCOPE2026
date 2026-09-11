"""Rigorous interval certificate: second singular value of the 48x64 base QC matrix <= 2.73.
Method (exact, stdlib only): M = HA*HA^T is an exact 48x48 integer matrix.
T = 2.73^2 = 74529/10000. Exact Fraction symmetric LDL (congruence) of (T*I - M)
gives inertia (pos,neg,zero); neg = #{eigenvalues of M above T} by Sylvester.
Result pos=47, neg=1, zero=0 with no pivoting failures: exactly one eigenvalue of M
above T. The all-ones vector is an exact eigenvector with eigenvalue 12 (biregular
row/col structure, checked exactly), so that one is the trivial Perron value and
every other eigenvalue of M is <= T, i.e. every nontrivial singular value of HA
is <= 2.73. In particular lambda2(Tanner) <= 2.73 < sqrt(12) ~= 3.4641.
"""
from fractions import Fraction
from itertools import combinations

A = [[14, 1, 9, 6], [12, 10, 6, 0], [4, 4, 8, 3]]
L = 16
M_DIM = 48

def base_cols():
    cols = []
    for j in range(4):
        for t in range(16):
            mask = 0
            for i in range(3):
                mask |= 1 << (i * 16 + ((t + A[i][j]) % 16))
            cols.append(mask)
    return cols

def main():
    cols = base_cols()
    # M[i][j] = overlap of checks i,j = #(common neighboring vars)
    M = [[0] * M_DIM for _ in range(M_DIM)]
    for c in cols:
        vs = []
        b = c
        while b:
            lsb = b & (-b)
            vs.append(lsb.bit_length() - 1)
            b ^= lsb
        for a in vs:
            for d in vs:
                M[a][d] += 1
    assert all(M[i][j] == M[j][i] for i in range(M_DIM) for j in range(M_DIM))
    # exact Perron check: every row sums to 12
    assert all(sum(M[i]) == 12 for i in range(M_DIM)), "Perron value must be 12"
    T = Fraction(74529, 10000)  # 2.73^2
    B = [[(T - M[i][j] if i == j else Fraction(-M[i][j])) for j in range(M_DIM)]
         for i in range(M_DIM)]
    pos = neg = zero = 0
    blocks2 = 0
    k = 0
    while k < M_DIM:
        if B[k][k] != 0:
            piv = B[k][k]
            if piv > 0:
                pos += 1
            else:
                neg += 1
            for i in range(k + 1, M_DIM):
                f = B[i][k] / piv
                if f != 0:
                    rowk = B[k]
                    rowi = B[i]
                    for j in range(k + 1, M_DIM):
                        rowi[j] -= f * rowk[j]
            k += 1
        else:
            j = next((jj for jj in range(k + 1, M_DIM) if B[jj][k] != 0), None)
            if j is None:
                zero += 1
                k += 1
                continue
            B[k + 1], B[j] = B[j], B[k + 1]
            for i in range(M_DIM):
                B[i][k + 1], B[i][j] = B[j], B[i][k + 1]
            pos += 1
            neg += 1
            blocks2 += 1
            b = B[k][k + 1]
            E11 = B[k + 1][k + 1]
            i00 = -E11 / (b * b)
            i01 = Fraction(1) / b
            for i in range(k + 2, M_DIM):
                u0, u1 = B[i][k], B[i][k + 1]
                if u0 == 0 and u1 == 0:
                    continue
                for j2 in range(k + 2, M_DIM):
                    v0, v1 = B[k][j2], B[k + 1][j2]
                    B[i][j2] -= u0 * (i00 * v0 + i01 * v1) + u1 * (i01 * v0)
            k += 2
    print(f"inertia of (2.73^2 I - M): pos={pos} neg={neg} zero={zero} 2x2blocks={blocks2}")
    assert blocks2 == 0 and zero == 0
    assert neg == 1, "exactly the trivial eigenvalue 12 lies above 2.73^2"
    print("LAMBDA2_CERT_OK: second singular value of base Tanner matrix <= 2.73")

if __name__ == "__main__":
    main()
