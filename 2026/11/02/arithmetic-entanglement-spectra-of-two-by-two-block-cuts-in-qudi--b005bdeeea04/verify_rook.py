#!/usr/bin/env python3
"""Independent finite-field and small-state tests for rook-graph cuts.
Run: python3 verify_rook.py. Uses only the Python standard library.
"""
import cmath
import itertools
import random


def rank_mod_p(matrix, p):
    a = [list(map(lambda x: x % p, row)) for row in matrix]
    if not a:
        return 0
    n = len(a[0]); k = 0
    for col in range(n):
        pivot = next((i for i in range(k, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        inv = pow(a[k][col], -1, p)
        a[k] = [(x * inv) % p for x in a[k]]
        for i in range(k + 1, len(a)):
            coeff = a[i][col]
            if coeff:
                a[i] = [(x - coeff * y) % p for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def cut(a, b, c, d):
    A = [(i, j) for i in range(a + b) for j in range(c + d)
         if (i < a) == (j < c)]
    B = [(i, j) for i in range(a + b) for j in range(c + d)
         if (i < a) != (j < c)]
    return A, B


def physical_matrix(a, b, c, d):
    A, B = cut(a, b, c, d)
    # Build directly from the rook graph's two-coordinate adjacency.
    return [[int((i == k) != (j == l)) for k, l in B]
            for i, j in A]


def theoretical_rank(a, b, c, d, p):
    return a + b + c + d - 4 + rank_mod_p([[a, c], [d, b]], p)


def direct_purity(a, b, c, d, p):
    # Directly trace the physical graph-state amplitude over B, with no
    # stabilizer rank formula used to build the reduced density matrix.
    C = physical_matrix(a, b, c, d)
    n_A, n_B = len(C), len(C[0])
    xs = list(itertools.product(range(p), repeat=n_A))
    ys = list(itertools.product(range(p), repeat=n_B))
    omega = cmath.exp(2j * cmath.pi / p)
    amplitudes = []
    for x in xs:
        amplitudes.append([
            omega ** (sum(x[i] * C[i][j] * y[j]
                          for i in range(n_A) for j in range(n_B)) % p)
            for y in ys
        ])
    norm = p ** (n_A + n_B)
    rho = [[sum(v * w.conjugate() for v, w in zip(amplitudes[i], amplitudes[j])) / norm
            for j in range(len(xs))] for i in range(len(xs))]
    purity = sum((abs(x) ** 2 for row in rho for x in row)).real
    tr = sum(rho[i][i] for i in range(len(xs)))
    return tr, purity


def run():
    checked = 0
    for p in (2, 3, 5):
        for a, b, c, d in itertools.product(range(1, 5), repeat=4):
            actual = rank_mod_p(physical_matrix(a, b, c, d), p)
            expected = theoretical_rank(a, b, c, d, p)
            assert actual == expected, (p, a, b, c, d, actual, expected)
            checked += 1
    rng = random.Random(1729)
    for p in (2, 3, 5, 7):
        for _ in range(100):
            a, b, c, d = (rng.randint(1, 9) for _ in range(4))
            actual = rank_mod_p(physical_matrix(a, b, c, d), p)
            expected = theoretical_rank(a, b, c, d, p)
            assert actual == expected, (p, a, b, c, d, actual, expected)
            checked += 1
    print('GF_P_CUT_RANK_OK', checked)
    tested = 0
    for p, blocks in ((2, (1,1,1,1)), (3, (1,1,1,1)),
                      (2, (1,1,1,2)), (3, (1,1,1,2))):
        tr, purity = direct_purity(*blocks, p)
        rank = theoretical_rank(*blocks, p)
        assert abs(tr-1) < 2e-12, (p, blocks, tr)
        assert abs(purity - p**(-rank)) < 2e-12, (p, blocks, purity, rank)
        tested += 1
    print('DIRECT_QUANTUM_PURITY_OK', tested)
    for p, blocks, want in ((2,(2,2,2,2),4), (3,(2,2,2,2),5),
                            (2,(3,3,3,3),9), (3,(3,3,3,3),8)):
        actual=rank_mod_p(physical_matrix(*blocks),p)
        assert actual==want, (p,blocks,actual,want)
        print('EXAMPLE_OK p={} blocks={} entropy_dits={}'.format(p,blocks,want))
    print('VERIFICATION_OK')


if __name__ == '__main__':
    run()
