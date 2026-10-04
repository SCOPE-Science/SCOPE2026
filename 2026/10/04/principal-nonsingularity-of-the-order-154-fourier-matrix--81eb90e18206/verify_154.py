#!/usr/bin/env python3
"""Exact finite-field verification for the order-154 Fourier principal-minor claim.

The calculation is entirely over K = F_11[a]/(a^3+a+4), with elements encoded
as c0 + c1*a + c2*a^2.  It verifies that a has multiplicative order 1330,
sets zeta=a^95 (order 14), forms the 14x14 Fourier matrix (zeta^(ij)), and
checks every nonempty principal determinant by exact Gaussian elimination.
"""
from itertools import combinations

P = 11
Q = P**3
GROUP_ORDER = Q - 1  # 1330
N = 14


def enc(c0, c1=0, c2=0):
    return (c0 % P) + P * (c1 % P) + P * P * (c2 % P)


def dec(x):
    return (x % P, (x // P) % P, (x // (P * P)) % P)


def add(x, y):
    a = dec(x); b = dec(y)
    return enc(a[0] + b[0], a[1] + b[1], a[2] + b[2])


def neg(x):
    a = dec(x)
    return enc(-a[0], -a[1], -a[2])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    a = dec(x); b = dec(y)
    c = [0] * 5
    for i in range(3):
        for j in range(3):
            c[i + j] = (c[i + j] + a[i] * b[j]) % P
    # Reduce by a^3 + a + 4 = 0, so a^d = -a^(d-2)-4a^(d-3), d>=3.
    for d in (4, 3):
        t = c[d] % P
        c[d] = 0
        c[d - 2] = (c[d - 2] - t) % P
        c[d - 3] = (c[d - 3] - 4 * t) % P
    return enc(c[0], c[1], c[2])


def fpow(x, e):
    r = 1
    while e:
        if e & 1:
            r = mul(r, x)
        x = mul(x, x)
        e >>= 1
    return r


def inv(x):
    if x == 0:
        raise ZeroDivisionError
    return fpow(x, Q - 2)


def det_principal(F, idx):
    m = len(idx)
    A = [[F[i][j] for j in idx] for i in idx]
    det = 1
    for col in range(m):
        pivot = next((r for r in range(col, m) if A[r][col] != 0), None)
        if pivot is None:
            return 0
        if pivot != col:
            A[col], A[pivot] = A[pivot], A[col]
            det = neg(det)
        pv = A[col][col]
        det = mul(det, pv)
        ip = inv(pv)
        for r in range(col + 1, m):
            if A[r][col] == 0:
                continue
            factor = mul(A[r][col], ip)
            for c in range(col, m):
                A[r][c] = sub(A[r][c], mul(factor, A[col][c]))
    return det


def main():
    # Cubic irreducibility: a cubic over a field is irreducible iff it has no root.
    roots = [x for x in range(P) if (x**3 + x + 4) % P == 0]
    assert roots == [], roots

    alpha = enc(0, 1, 0)
    assert fpow(alpha, GROUP_ORDER) == 1
    prime_divisors = (2, 5, 7, 19)
    primitive_tests = {q: fpow(alpha, GROUP_ORDER // q) for q in prime_divisors}
    assert all(v != 1 for v in primitive_tests.values())

    zeta = fpow(alpha, GROUP_ORDER // N)  # alpha^95
    assert fpow(zeta, N) == 1
    assert fpow(zeta, 7) != 1 and fpow(zeta, 2) != 1

    primitive_exponents = (1, 3)
    counts = {k: 0 for k in range(1, N + 1)}
    zero_counts = {e: {k: 0 for k in range(1, N + 1)} for e in primitive_exponents}
    checksum = 0
    MOD64 = 1 << 64
    total = 0
    per_root = (1 << N) - 1
    for e in primitive_exponents:
        ze = fpow(zeta, e)
        powers = [fpow(ze, j) for j in range(N)]
        F = [[powers[(i * j) % N] for j in range(N)] for i in range(N)]
        for k in range(1, N + 1):
            for idx in combinations(range(N), k):
                d = det_principal(F, idx)
                if e == primitive_exponents[0]:
                    counts[k] += 1
                total += 1
                if d == 0:
                    zero_counts[e][k] += 1
                # Deterministic smoke checksum; nonvanishing is established by zero_counts.
                mask = sum(1 << i for i in idx)
                checksum = (checksum * 1000003 + e * 65537 + mask * 4099 + d) % MOD64

    assert sum(counts.values()) == per_root
    assert total == len(primitive_exponents) * per_root
    assert all(v == 0 for table in zero_counts.values() for v in table.values())

    print("VERIFY_OK")
    print(f"field=GF({P}^3) modulus=x^3+x+4 elements={Q}")
    print(f"alpha_order={GROUP_ORDER} primitive_tests={primitive_tests}")
    print(f"zeta_encoded={zeta} zeta_order={N}")
    print(f"primitive_14th_root_orbit_representatives_checked={len(primitive_exponents)} exponents={primitive_exponents}")
    print(f"principal_subsets_per_root={per_root} total_determinants_checked={total}")
    print("counts_by_size_per_root=" + repr(counts))
    print("zero_counts_by_root_and_size=" + repr(zero_counts))
    print(f"checksum64={checksum}")


if __name__ == "__main__":
    main()
