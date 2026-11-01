#!/usr/bin/env python3
"""Independent finite checks for a one-site 90/150 hybrid on a cyclic ring.
No external dependencies beyond Python stdlib and optional sympy for determinant checks.
"""

def step(state, n, defect=True):
    full = (1 << n) - 1
    left = ((state << 1) & full) | (state >> (n - 1))
    right = (state >> 1) | ((state & 1) << (n - 1))
    return (left ^ right ^ ((state & 1) if defect else 0)) & full

def rows(n, defect=True):
    return [((1 << ((i - 1) % n)) ^ (1 << ((i + 1) % n)) ^ ((1 << i) if (defect and i == 0) else 0)) for i in range(n)]

def matmul(a, b):
    out = []
    for row in a:
        val = 0
        while row:
            bit = row & -row
            val ^= b[bit.bit_length() - 1]
            row -= bit
        out.append(val)
    return out

def rank(rows_, n):
    a = rows_[:]
    piv = 0
    for col in range(n):
        q = next((i for i in range(piv, n) if (a[i] >> col) & 1), None)
        if q is None:
            continue
        a[q], a[piv] = a[piv], a[q]
        for i in range(piv + 1, n):
            if (a[i] >> col) & 1:
                a[i] ^= a[piv]
        piv += 1
    return piv

def v2(n):
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    return s

def powers_ranks(n, defect):
    a = rows(n, defect)
    p = [1 << i for i in range(n)]
    vals = []
    for t in range(n + 1):
        vals.append(rank(p, n))
        p = matmul(a, p)
    return vals

def brute_entry_distribution(n):
    counts = {}
    for state in range(1 << n):
        seen = {}
        v = state
        t = 0
        while v not in seen:
            seen[v] = t
            v = step(v, n)
            t += 1
            assert t <= (1 << n)
        preperiod = seen[v]
        counts[preperiod] = counts.get(preperiod, 0) + 1
    return counts

def main():
    for n in range(3, 81):
        q = (1 << v2(n)) - 1
        values = powers_ranks(n, True)
        expected = [n - min(t, q) for t in range(n + 1)]
        assert values == expected, (n, values, expected)
        old = powers_ranks(n, False)
        s = v2(n)
        old_q = (1 << s)
        blocks = 2 if s else 1
        length = (1 << (s - 1)) if s else 1
        expected_old = [n - min(t, length) * blocks for t in range(n + 1)]
        assert old == expected_old, (n, old, expected_old)
    print('POWER_RANK_PROFILES_OK lengths=3..80')

    for n in range(3, 12):
        q = (1 << v2(n)) - 1
        direct = brute_entry_distribution(n)
        predicted = {0: 1 << (n - q)}
        for t in range(1, q + 1):
            predicted[t] = 1 << (n - q + t - 1)
        assert direct == predicted, (n, direct, predicted)
    print('FULL_MICROSCOPIC_ORBITS_OK lengths=3..11 configurations=4088')

    try:
        import sympy as sp
    except ImportError:
        print('CHARPOLY_CHECK_SKIPPED sympy_unavailable')
    else:
        z = sp.symbols('z')
        p = [sp.Poly(1, z, modulus=2), sp.Poly(z, z, modulus=2)]
        for k in range(2, 18):
            p.append(sp.Poly(z * p[k-1].as_expr() + p[k-2].as_expr(), z, modulus=2))
        for n in range(3, 18):
            mat = sp.zeros(n)
            for i in range(n):
                mat[i, (i - 1) % n] = 1
                mat[i, (i + 1) % n] = 1
            mat[0, 0] = 1
            char = sp.Poly(mat.charpoly(z).as_expr(), z, modulus=2)
            expect = sp.Poly((z+1)*p[n-1].as_expr(), z, modulus=2)
            assert char == expect, (n, char, expect)
        print('CHARACTERISTIC_POLYNOMIALS_OK lengths=3..17')

    print('ONE_DEFECT_RING_VERIFY_OK')

if __name__ == '__main__':
    main()
