#!/usr/bin/env python3
"""Independent finite-field checks of characteristic-two derivation-rank formulas.
Run with Python 3; no third-party packages are used.
"""
from collections import Counter
from itertools import product
import random


def mul(a, b, q):
    """GF(2^f), irreducible polynomials x, x^2+x+1, x^3+x+1."""
    f = q.bit_length() - 1
    modulus = {2: 0b11, 4: 0b111, 8: 0b1011}[q]
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= modulus
    return z


def inv(a, q):
    if not a:
        raise ZeroDivisionError()
    return next(b for b in range(1, q) if mul(a, b, q) == 1)


def bracket(x, y, q):
    """Model filiform alternating bracket in basis e_1,...,e_n."""
    n = len(x)
    z = [0] * n
    for j in range(1, n - 1):
        z[j + 1] = mul(x[0], y[j], q) ^ mul(y[0], x[j], q)
    return z


def d_matrix(a, v, w, q):
    """Build columns recursively from the defining derivation identity."""
    n = len(w) + 1
    cols = [[a] + list(v), [0] + list(w)]
    for j in range(2, n):
        unit = [int(i == j - 1) for i in range(n)]
        e1 = [int(i == 0) for i in range(n)]
        c1 = bracket(cols[0], unit, q)
        c2 = bracket(e1, cols[j - 1], q)
        cols.append([x ^ y for x, y in zip(c1, c2)])
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def rank(M, q):
    A = [row[:] for row in M]
    h = len(A)
    w = len(A[0])
    r = 0
    for j in range(w):
        pivot = next((i for i in range(r, h) if A[i][j]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        t = inv(A[r][j], q)
        A[r] = [mul(t, x, q) for x in A[r]]
        for i in range(h):
            if i != r and A[i][j]:
                t = A[i][j]
                A[i] = [x ^ mul(t, y, q) for x, y in zip(A[i], A[r])]
        r += 1
    return r


def predicted(q, n):
    d = n - 1
    C = Counter()
    C[0] += 1
    C[1] += q ** d - 1
    for r in range(1, d + 1):
        number_w = (q - 1) * q ** (r - 1)
        C[r] += number_w * q ** r
        C[r + 1] += number_w * (q ** d - q ** r)
    C[n] += (q - 1) * (q - 2) * q ** (2 * d - 1)
    for ell in ((d + 1) // 2, d // 2):
        for j in range(1, ell + 1):
            v = ((q - 1) * q ** (d - 1 - j) if j < ell else q ** (d - ell))
            C[n - j] += (q - 1) * q ** d * v
    C += Counter()
    assert sum(C.values()) == q ** (2 * n - 1)
    return C


def identity_check(M, q):
    n = len(M)
    cols = [list(col) for col in zip(*M)]
    basis = [[int(i == j) for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            xy = bracket(basis[i], basis[j], q)
            lhs = [0] * n
            for t in range(n):
                if xy[t]:
                    lhs = [a ^ mul(xy[t], b, q) for a, b in zip(lhs, cols[t])]
            rhs1 = bracket(cols[i], basis[j], q)
            rhs2 = bracket(basis[i], cols[j], q)
            assert lhs == [a ^ b for a, b in zip(rhs1, rhs2)]


def derivation_test(q, n, exhaustive=True, sample_size=1500):
    d = n - 1
    obs = Counter()
    rand = random.Random(47 + q * 100 + n)
    if exhaustive:
        source = product(range(q), repeat=2 * d + 1)
    else:
        source = ([rand.randrange(q) for _ in range(2 * d + 1)] for _ in range(sample_size))
    first = True
    for values in source:
        a = values[0]
        v = values[1:1 + d]
        w = values[1 + d:]
        D = d_matrix(a, v, w, q)
        if first or rand.randrange(512) == 0:
            identity_check(D, q)
        first = False
        obs[rank(D, q)] += 1
    if exhaustive:
        assert obs == predicted(q, n), (q, n, obs, predicted(q, n))
        return 'EXHAUSTIVE', sum(obs.values()), sorted(obs.items())
    assert all(predicted(q, n)[k] > 0 for k in obs)
    return 'SAMPLED', sum(obs.values()), sorted(obs.items())


def all_linear_maps_n4_binary():
    q, n = 2, 4
    obs = Counter()
    for bits in range(1 << (n * n)):
        M = [[(bits >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        cols = list(map(list, zip(*M)))
        ok = True
        for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)):
            lhs = [0] * n
            if i == 0 and j < 3:
                lhs = cols[j + 1]
            ei = [int(z == i) for z in range(n)]
            ej = [int(z == j) for z in range(n)]
            rhs1 = bracket(cols[i], ej, q)
            rhs2 = bracket(ei, cols[j], q)
            if lhs != [a ^ b for a, b in zip(rhs1, rhs2)]:
                ok = False
                break
        if ok:
            obs[rank(M, q)] += 1
    assert obs == predicted(q, n), (obs, predicted(q, n))
    return sum(obs.values())



def gauge_normal_form_test():
    """Check the characteristic-two conjugating-unit equation independently."""
    rng = random.Random(2026)
    trials = 0
    for q in (2, 4, 8):
        for d in range(4, 12):
            even_len = (d + 1) // 2
            odd_len = d // 2
            for _ in range(40):
                f = [rng.randrange(q) for _ in range(d)]
                odd = f[1::2]
                even = f[0::2]
                z = [0] * even_len
                for k in range(even_len):
                    value = odd[k] if k < odd_len else 0
                    for j in range(odd_len):
                        for r in range(k):
                            if j + 2 * r == k - 1:
                                value ^= mul(odd[j], mul(z[r], z[r], q), q)
                    z[k] = value
                h = even[:]
                for k in range(1, even_len):
                    for j in range(odd_len):
                        r = k - 1 - j
                        if 0 <= r < even_len:
                            h[k] ^= mul(odd[j], z[r], q)
                u = [0] * d
                u[0] = 1
                for r in range(odd_len):
                    u[2 * r + 1] = z[r]
                lhs = [(j & 1) * u[j] for j in range(d)]
                rhs = [0] * d
                for i in range(d):
                    for j in range(d - i):
                        lhs[i + j] ^= mul(f[i], u[j], q)
                for i in range(even_len):
                    for j in range(d - 2*i):
                        rhs[2*i + j] ^= mul(h[i], u[j], q)
                assert lhs == rhs, (q,d,f,z,h,lhs,rhs)
                trials += 1
    return trials


def main():
    checks = []
    for q, n in [(2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
                 (4, 4), (4, 5)]:
        mode, number, histogram = derivation_test(q, n)
        checks.append((q, n, mode, number))
        print('CHECK', q, n, mode, number, histogram)
    for q, n in [(4, 6), (8, 4), (8, 5)]:
        mode, number, histogram = derivation_test(q, n, False)
        checks.append((q, n, mode, number))
        print('CHECK', q, n, mode, number, histogram)
    print('ALL_LINEAR_MAPS_BINARY_N4', all_linear_maps_n4_binary())
    print('GAUGE_CONJUGATION_TESTS', gauge_normal_form_test())
    print('VERIFY_OK_FILIFORM_DERIVATION_RANKS', len(checks), 'configurations')

if __name__ == '__main__':
    main()
