#!/usr/bin/env python3
"""Exact verification for the degree-23 M_2(F_2) word-sum counterexample."""

# A 2x2 matrix over F_2 is encoded by four row-major bits:
# bit 0=a00, bit 1=a01, bit 2=a10, bit 3=a11.

I2 = 0b1001

def mm(a, b):
    a00, a01, a10, a11 = (a >> 0) & 1, (a >> 1) & 1, (a >> 2) & 1, (a >> 3) & 1
    b00, b01, b10, b11 = (b >> 0) & 1, (b >> 1) & 1, (b >> 2) & 1, (b >> 3) & 1
    c00 = (a00 & b00) ^ (a01 & b10)
    c01 = (a00 & b01) ^ (a01 & b11)
    c10 = (a10 & b00) ^ (a11 & b10)
    c11 = (a10 & b01) ^ (a11 & b11)
    return c00 | (c01 << 1) | (c10 << 2) | (c11 << 3)

def shuffle_table(max_total=23):
    # P[a][b] is the sum of all words with a copies of A and b copies of B.
    total_sum = [[0] * (max_total + 1) for _ in range(max_total + 1)]
    for A in range(16):
        for B in range(16):
            P = [[0] * (max_total + 1) for _ in range(max_total + 1)]
            P[0][0] = I2
            for total in range(1, max_total + 1):
                for a in range(total + 1):
                    b = total - a
                    v = 0
                    if a:
                        v ^= mm(P[a - 1][b], A)
                    if b:
                        v ^= mm(P[a][b - 1], B)
                    P[a][b] = v
                    total_sum[a][b] ^= v
    return total_sum

def poly_mul(p, q, limit=23):
    # Polynomials over F_2 are encoded as coefficient bitsets.
    r = 0
    while q:
        if q & 1:
            r ^= p
        q >>= 1
        p <<= 1
    return r & ((1 << (limit + 1)) - 1)

def pmat_mul(X, Y, limit=23):
    Z = [0] * 4
    for i in range(2):
        for j in range(2):
            s = 0
            for k in range(2):
                s ^= poly_mul(X[2 * i + k], Y[2 * k + j], limit)
            Z[2 * i + j] = s
    return tuple(Z)

def pmat_pow_tA_plus_B(A, B, exponent=23):
    M = tuple(((B >> j) & 1) | (((A >> j) & 1) << 1) for j in range(4))
    R = (1, 0, 0, 1)
    e = exponent
    while e:
        if e & 1:
            R = pmat_mul(R, M, exponent)
        M = pmat_mul(M, M, exponent)
        e >>= 1
    return R

def aggregate_polynomial_23():
    S = [0, 0, 0, 0]
    for A in range(16):
        for B in range(16):
            R = pmat_pow_tA_plus_B(A, B, 23)
            for j in range(4):
                S[j] ^= R[j]
    return tuple(S)

def factor_polynomial_bitset():
    # t^5 (t+1)^5 (t^2+t+1) (t^3+t+1) (t^3+t^2+1)
    factors = [
        1 << 5,
        0b11, 0b11, 0b11, 0b11, 0b11,
        0b111,
        (1 << 3) | (1 << 1) | 1,
        (1 << 3) | (1 << 2) | 1,
    ]
    f = 1
    for g in factors:
        f = poly_mul(f, g, 23)
    return f

def main():
    T = shuffle_table(23)
    failures = []
    for total in range(2, 24):
        for a in range(1, total):
            b = total - a
            if T[a][b]:
                failures.append((total, a, b, T[a][b]))

    first_total = min(t for t, _, _, _ in failures)
    degree23 = [(a, b, v) for t, a, b, v in failures if t == 23]
    support = [a for a, b, v in degree23 if v == I2]

    S = aggregate_polynomial_23()
    f = factor_polynomial_bitset()

    assert first_total == 23
    assert all(v == I2 for _, _, v in degree23)
    assert support == [5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18]
    assert S == (f, 0, 0, f)
    assert ((S[0] >> 5) & 1) == 1

    print("first nonzero total degree for r=2:", first_total)
    print("degree-23 nonzero a-values:", support)
    print("T_(5,18) = I_2:", hex(T[5][18]) == hex(I2))
    print("polynomial identity verified:", S == (f, 0, 0, f))

if __name__ == "__main__":
    main()
