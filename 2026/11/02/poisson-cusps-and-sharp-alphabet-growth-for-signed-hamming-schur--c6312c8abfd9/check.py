"""Exact-arithmetic finite checks of signed Hamming Schur-multiplier formulas.

Run: python3 check.py. Requires Python standard library only.
All results for unbounded dimensions and parameters require the accompanying proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial


def spectrum_norm(d, q):
    N = q ** d
    top = N - 2 * d * (q - 1)
    assert top >= 0
    value = abs(top)
    for j in range(1, d + 1):
        multiplicity = comb(d, j) * (q - 1) ** j
        value += multiplicity * abs(2 * (q * j - d * (q - 1)))
    return Fraction(value, N)


def mass_norm(d, q):
    p = Fraction(1, q)
    k = d // q
    mass = comb(d - 1, k) * p ** k * (1 - p) ** (d - 1 - k)
    return 1 + 4 * d * (1 - p) * (mass - p ** (d - 1))


def abs_binomial_check(d, q):
    N = q ** d
    direct = Fraction(sum(comb(d, y) * (q - 1) ** (d - y)
                          * abs(d - q * y) for y in range(d + 1)), N)
    k = d // q
    boundary = (2 * d * Fraction(q - 1, q) * comb(d - 1, k)
                * Fraction(1, q) ** k
                * Fraction(q - 1, q) ** (d - 1 - k))
    assert direct == boundary, (d, q, direct, boundary)


def direct_tensor_eigencheck(d, q):
    verts = list(product(range(q), repeat=d))
    N = q ** d
    idx = {x: i for i, x in enumerate(verts)}
    neighbors = []
    for x in verts:
        adj = []
        for coord in range(d):
            for z in range(q):
                if z != x[coord]:
                    y = x[:coord] + (z,) + x[coord+1:]
                    adj.append(idx[y])
        neighbors.append(adj)
    for label in verts:
        level = sum(a > 0 for a in label)
        # Alphabet basis: all-one, and e_{a-1}-e_{q-1} for a=1..q-1.
        vec = []
        for x in verts:
            v = 1
            for a, z in zip(label, x):
                if a:
                    v *= (int(z == a - 1) - int(z == q - 1))
            vec.append(v)
        scalar = N - 2 * d * (q - 1) if level == 0 else 2 * (q * level - d * (q - 1))
        sum_v = sum(vec)
        for i in range(N):
            calc = sum_v - 2 * sum(vec[j] for j in neighbors[i])
            assert calc == scalar * vec[i], (d, q, label, verts[i], calc)
    return N


def main():
    comparisons = 0
    strict_pairs = 0
    for d in range(2, 66):
        prev = None
        for q in range(2, 55):
            a = spectrum_norm(d, q)
            b = mass_norm(d, q)
            assert a == b, (d, q, a, b)
            abs_binomial_check(d, q)
            if prev is not None:
                assert a > prev, (d, q, a, prev)
                strict_pairs += 1
            assert a < 1 + 4 * d
            prev = a
            comparisons += 1
    vertex_modes = 0
    for d, q in [(2, 2), (2, 3), (2, 4), (2, 5),
                 (3, 2), (3, 3), (3, 4), (4, 2), (4, 3),
                 (5, 2), (6, 2)]:
        vertex_modes += direct_tensor_eigencheck(d, q)
    assert mass_norm(2, 2) == 1
    assert mass_norm(2, 3) == Fraction(25, 9)
    assert mass_norm(3, 2) == Fraction(5, 2)
    assert mass_norm(2, 4) == 4
    print('SIGNED_HAMMING_SCHUR_CHECK_OK',
          'exact_spectrum_mass_pairs=', comparisons,
          'strict_alphabet_steps=', strict_pairs,
          'direct_tensor_eigenmodes=', vertex_modes,
          'small_exact_values=4')


if __name__ == '__main__':
    main()
