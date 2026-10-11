"""Exact finite-class checks for signed-permutation class Fourier spectra.

Run: python artifacts/verify.py. Only Python's standard library is used.
The universal theorem is proved algebraically; finite tests are corroboration.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def signed_cycle_signature(perm, signs):
    n = len(perm)
    done = set()
    counts = defaultdict(int)
    for start in range(n):
        if start in done:
            continue
        j = start
        length = 0
        sign = 1
        while j not in done:
            done.add(j)
            length += 1
            sign *= signs[j]
            j = perm[j]
        counts[length, sign] += 1
    return tuple(sorted(counts.items()))


def energies(signature, n):
    counts = dict(signature)
    p1 = counts.get((1, 1), 0)
    m1 = counts.get((1, -1), 0)
    p2 = counts.get((2, 1), 0)
    m2 = counts.get((2, -1), 0)
    f = p1 + m1
    s = p1 - m1
    tau = p2 - m2
    return (Fraction(s * s, n), Fraction(f) - Fraction(s * s, n),
            Fraction(n - f, 2) + tau, Fraction(n - f, 2) - tau)


def matrices_by_class(n):
    result = defaultdict(list)
    for perm in permutations(range(n)):
        for signs in product((-1, 1), repeat=n):
            mat = [0] * (n * n)
            for col, row in enumerate(perm):
                mat[n * row + col] = signs[col]
            result[signed_cycle_signature(perm, signs)].append(mat)
    return result


def check(n):
    cls = matrices_by_class(n)
    assert sum(map(len, cls.values())) == (2 ** n) * factorial(n)
    dimensions = (1, n - 1, n * (n - 1) // 2, n * (n - 1) // 2)
    basis = []
    identity = [int(k // n == k % n) for k in range(n * n)]
    basis.append((0, identity))
    for i in range(1, n):
        d = [0] * (n * n)
        d[0] = 1
        d[n * i + i] = -1
        basis.append((1, d))
    for i in range(n):
        for j in range(i + 1, n):
            a = [0] * (n * n)
            a[i * n + j] = 1
            a[j * n + i] = 1
            basis.append((2, a))
            b = [0] * (n * n)
            b[i * n + j] = 1
            b[j * n + i] = -1
            basis.append((3, b))
    assert len(basis) == n * n
    # Schur orthogonality and coefficient normalization, checked as integers.
    coefficient_gram = [[0] * (n * n) for _ in range(n * n)]
    for matrices in cls.values():
        for mat in matrices:
            nz = [(i, x) for i, x in enumerate(mat) if x]
            for i, x in nz:
                for j, y in nz:
                    coefficient_gram[i][j] += x * y
    assert all(coefficient_gram[i][j] == ((2 ** n) * factorial(n) // n if i == j else 0)
               for i in range(n * n) for j in range(n * n))
    tight = injective = 0
    for signature, matrices in cls.items():
        e = energies(signature, n)
        assert sum(e) == n and all(t >= 0 for t in e)
        frame_lambda = [Fraction(len(matrices)) * e[j] / dimensions[j] for j in range(4)]
        is_tight = len(set(frame_lambda)) == 1
        has_full_rank = all(k > 0 for k in frame_lambda)
        p1 = dict(signature).get((1, 1), 0)
        m1 = dict(signature).get((1, -1), 0)
        p2 = dict(signature).get((2, 1), 0)
        m2 = dict(signature).get((2, -1), 0)
        f = p1 + m1
        s = p1 - m1
        tau = p2 - m2
        long_cycles = any(length >= 3 for (length, sign), count in signature if count > 0)
        assert is_tight == (f == 1 and tau == 0)
        assert has_full_rank == (s != 0 and (long_cycles or (p2 > 0 and m2 > 0)))
        tight += is_tight
        injective += has_full_rank
        for sector, a in basis:
            out = [0] * (n * n)
            for mat in matrices:
                coefficient = sum(x * y for x, y in zip(a, mat))
                if coefficient:
                    for z, entry in enumerate(mat):
                        out[z] += coefficient * entry
            mu = frame_lambda[sector]
            assert all(Fraction(v) == mu * a[z] for z, v in enumerate(out)), (n, signature, sector)
    return len(cls), tight, injective


if __name__ == '__main__':
    total = 0
    for n in (3, 4, 5):
        c, t, i = check(n)
        total += c
        print(f'n={n}: conjugacy_classes={c}, tight={t}, injective={i}, all_{n*n}_basis_vectors=PASS')
    print(f'VERIFY_OK conjugacy_classes={total} exact_full_class_orbit_operators=PASS coefficient_orthogonality=PASS')
