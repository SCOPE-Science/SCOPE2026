"""Exact inertia check at T=2.70^2=729/100: demonstrates the fallback bar FAILS (stdlib only).

Same exact Fraction symmetric-LDL congruence as inertia_cert.py, only T differs.
Expected result: pos=39, neg=9, zero=0, 2x2blocks=0 -- nine eigenvalues of
M = HA*HA^T exceed 2.70^2 (the trivial 12 plus four pairs around 2.70-2.73),
so in particular the bound lambda2 <= 2.70 is FALSE for the logged matrices
and no honest interval script can certify it. Compare inertia_cert.py which
gives (47,1,0) at T=2.73^2 (only the trivial 12 above).
Numerically the top singular values are
  3.464102, 2.728007(x2), 2.704774(x2), 2.701280(x2), 2.700122(x2), ...
i.e. 9 singular values above 2.70, 1 above 2.73 -- consistent with neg=9/neg=1.
"""
from fractions import Fraction

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


def inertia_at(T):
    cols = base_cols()
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
    assert all(sum(M[i]) == 12 for i in range(M_DIM)), "Perron value must be 12"
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
    return pos, neg, zero, blocks2


def main():
    T = Fraction(729, 100)  # 2.70^2
    pos, neg, zero, blocks2 = inertia_at(T)
    print(f"inertia of (2.70^2 I - M): pos={pos} neg={neg} zero={zero} 2x2blocks={blocks2}")
    assert blocks2 == 0 and zero == 0
    assert neg == 9, f"expect 9 eigenvalues above 2.70^2, got neg={neg}"
    print("CHECK270_OK: bound lambda2 <= 2.70 is FALSE for the logged matrices "
          "(9 eigenvalues above 2.70^2); fallback bar correctly FAILS")


if __name__ == "__main__":
    main()
