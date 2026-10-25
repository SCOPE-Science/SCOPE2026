"""Exact rational verification of the K_{2,m} polar Ehrhart calculation.

Uses only Python's standard library.  The infinite-parameter sign argument
in RESULT.md is mathematical; this program checks every remaining finite case.
"""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product


def bernoulli_at_one(order):
    """Return B_k(1), defined by t*exp(t)/(exp(t)-1)."""
    out = [Q(1)]
    for r in range(1, order + 1):
        out.append(Q(1) - sum(Q(comb(r + 1, j), r + 1) * out[j]
                                  for j in range(r)))
    return out


def coefficients_formula(m):
    B = bernoulli_at_one(m + 1)
    return ([Q(1)] +
            [Q(2 ** j * comb(m, j)) *
             (1 + 2 * B[m + 1 - j] / (m + 1 - j))
             for j in range(1, m + 1)] +
            [Q(2 ** (m + 2), m + 1)])


def count_lattice_points(m, n):
    """Fix one potential to zero and sum available choices for the others."""
    return sum((2 * n + 1 - abs(t)) ** m
               for t in range(-2 * n, 2 * n + 1))


def ordinary_coefficients_from_values(values):
    """Independent Newton interpolation in the binomial polynomial basis."""
    d = len(values) - 1
    differences = [Q(v) for v in values]
    delta = []
    while differences:
        delta.append(differences[0])
        differences = [differences[i + 1] - differences[i]
                       for i in range(len(differences) - 1)]
    ans = [Q(0)] * (d + 1)
    basis = [Q(1)]
    for k, a in enumerate(delta):
        for j, b in enumerate(basis):
            ans[j] += a * b / factorial(k)
        new = [Q(0)] * (len(basis) + 1)
        for j, b in enumerate(basis):
            new[j] -= k * b
            new[j + 1] += b
        basis = new
    return ans


def magic_coefficients(ordinary):
    d = len(ordinary) - 1
    return [sum(ordinary[j] * (-1) ** (i - j) * comb(d - j, i - j)
                for j in range(i + 1)) for i in range(d + 1)]


def direct_graph_count(m, n):
    """Small check independent of the closed summand: enumerate all potentials."""
    possible = range(-n, 3 * n + 1)
    total = 0
    for t in range(-2 * n, 2 * n + 1):
        for y in product(possible, repeat=m):
            if all(abs(z) <= n and abs(t - z) <= n for z in y):
                total += 1
    return total


def main():
    expected_centers = {
        9: Q(-144, 5), 10: Q(-598, 11), 11: Q(-892, 3),
        12: Q(-262324, 455), 13: Q(-106896, 35),
        14: Q(-31729, 5), 15: Q(-41178), 16: Q(-4767934, 51),
        17: Q(-7027360, 9), 18: Q(-774064682, 399),
        19: Q(-2120599388, 105),
    }
    for m in range(1, 21):
        ordinary = coefficients_formula(m)
        direct = ordinary_coefficients_from_values(
            [count_lattice_points(m, n) for n in range(m + 2)])
        assert ordinary == direct, (m, 'interpolation')
        magic = magic_coefficients(ordinary)
        if m <= 19:
            assert all(x > 0 for x in ordinary), (m, "ordinary positivity")
        assert magic == list(reversed(magic)), (m, 'symmetry')
        if m <= 8:
            assert all(c > 0 for c in magic), (m, 'positive magic')
        elif m <= 19:
            assert magic[(m + 1) // 2] == expected_centers[m]
            assert magic[(m + 1) // 2] < 0
        if m == 20:
            assert ordinary[1] == Q(-342622, 165)
    for m in range(1, 4):
        for n in range(0, 4):
            assert direct_graph_count(m, n) == count_lattice_points(m, n)
    assert bernoulli_at_one(20)[20] == Q(-174611, 330)
    print('EXACT_OK: direct graph enumeration, independent polynomial interpolation,')
    print('20 dimensions of coefficient identities, all finite magic signs,')
    print('and the Bernoulli index-20 infinite-family obstruction.')


if __name__ == '__main__':
    main()
