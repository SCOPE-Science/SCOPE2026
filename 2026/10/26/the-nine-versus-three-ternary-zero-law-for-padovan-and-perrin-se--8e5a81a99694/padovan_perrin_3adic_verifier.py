"""Standalone exact-integer checks for Padovan/Perrin ternary zero-class theorem.

Run with Python 3: python padovan_perrin_3adic_verifier.py
All calculations are deterministic; finite checks support, not replace, the proof.
"""

M = ((0, 1, 0), (0, 0, 1), (1, 1, 0))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
B = ((2, 4, 3), (3, 5, 4), (4, 7, 5))
SEEDS = {"Padovan": (1, 1, 1), "Perrin": (3, 0, 2)}
EXPECTED_ROWS = {
    "Padovan": {5: (3, 37, 465, 5842), 9: (9, 114, 1432, 17991),
                10: (12, 151, 1897, 23833), 12: (21, 265, 3329, 41824)},
    "Perrin": {0: (3, 12, 158, 1983), 1: (0, 17, 209, 2627),
               3: (3, 29, 367, 4610), 9: (12, 158, 1983, 24914)},
}


def matmul(A, D, mod=None):
    E = tuple(tuple(sum(A[i][z] * D[z][j] for z in range(3)) for j in range(3))
              for i in range(3))
    return E if mod is None else tuple(tuple(x % mod for x in row) for row in E)


def matpow(A, n, mod=None):
    out = I
    while n:
        if n & 1:
            out = matmul(out, A, mod)
        A = matmul(A, A, mod)
        n //= 2
    return out


def matvec(A, v, mod=None):
    z = tuple(sum(A[i][j] * v[j] for j in range(3)) for i in range(3))
    return z if mod is None else tuple(x % mod for x in z)


def matadd(A, D):
    return tuple(tuple(A[i][j] + D[i][j] for j in range(3)) for i in range(3))


def matscale(A, c):
    return tuple(tuple(c * x for x in row) for row in A)


def subseq(name, k):
    modulus = 3 ** k
    L = 13 * 3 ** (k - 1)
    v = tuple(x % modulus for x in SEEDS[name])
    start = v
    zeros = []
    for n in range(L):
        if v[0] == 0:
            zeros.append(n)
        v = matvec(M, v, modulus)
        if n < L - 1:
            assert v != start, (name, k, n)
    assert v == start
    return zeros


def main():
    U = matpow(M, 13)
    assert U == matadd(I, matscale(B, 3)), (U, B)
    assert matpow(M, 13, 3) == I
    for seed in SEEDS.values():
        assert matvec(M, seed, 3) != tuple(x % 3 for x in seed)
        assert any(x % 3 for x in matvec(B, seed))
    for name, seed in SEEDS.items():
        for r in range(13):
            row = matpow(M, r)
            vals = []
            w = seed
            for _ in range(4):
                vals.append(matvec(row, w)[0])
                w = matvec(B, w)
            if r in EXPECTED_ROWS[name]:
                assert tuple(vals) == EXPECTED_ROWS[name][r], (name, r, vals)
            else:
                assert vals[0] % 3 != 0, (name, r)
    # The exceptional branch uses C_m=(U^(3^m)-I)/3^(m+1).
    C1 = matadd(matadd(B, matscale(matmul(B, B), 3)),
                matscale(matmul(matmul(B, B), B), 3))
    assert matpow(U, 3) == matadd(I, matscale(C1, 9))
    for m in range(1, 7):
        mod = 9 * 3 ** (m + 1)
        W = matpow(U, 3 ** m, mod)
        Cm = tuple(tuple(((W[i][j] - I[i][j]) % mod) // (3 ** (m + 1))
                         for j in range(3)) for i in range(3))
        assert all((Cm[i][j] - C1[i][j]) % 9 == 0
                   for i in range(3) for j in range(3)), m
    # Check exceptional Hensel increments directly using exact residues.
    seed = SEEDS["Padovan"]
    for m in range(1, 6):
        mod = 3 ** (m + 3)
        for t in range(35):
            def f(x):
                return matvec(matpow(M, 9 + 13 * x, mod), seed, mod)[0] % mod
            z = (f(t + 3 ** m) - f(t)) % mod
            assert z % 9 == 0
            assert ((z // 9) - (3 ** m) * t) % (3 ** (m + 1)) == 0, (m, t, z)
    # Independently enumerate complete periods and compare root counts.
    for k in range(1, 11):
        pz = subseq("Padovan", k)
        rz = subseq("Perrin", k)
        expected_p = 4 if k == 1 else (6 if k == 2 else 9)
        expected_r = 4 if k == 1 else 3
        assert len(pz) == expected_p and len(rz) == expected_r, (k, pz, rz)
        if k >= 3:
            assert sum(n % 13 == 9 for n in pz) == 6
            assert sorted(n % 13 for n in pz if n % 13 != 9) == [5, 10, 12]
        print('k=%d period=%d Padovan_zero_count=%d Perrin_zero_count=%d'
              % (k, 13 * 3 ** (k - 1), len(pz), len(rz)))
    print('PASS: exact matrix, branch, lifting and complete-period tests')


if __name__ == '__main__':
    main()
