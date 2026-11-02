"""Exact finite cross-check of the hypercube exact-degree harmonic rank formula.

No third-party dependencies. The infinite-dimensional theorem is established by
explicit harmonic witnesses, not inferred from these tests.
"""
from fractions import Fraction as Q
from math import comb


def krawtchouk(d, h, j):
    return sum((-1) ** a * comb(j, a) * comb(d - j, h - a)
               for a in range(max(0, h - (d - j)), min(h, j) + 1))


def exact_kernel_values(d, max_k):
    alpha = Q(d - 2, 2)
    t = [Q(d - 2 * h, d) for h in range(d + 1)]
    prev = [Q(1)] * (d + 1)
    cur = [2 * alpha * x for x in t]
    yield 0, prev
    yield 1, cur
    for k in range(2, max_k + 1):
        nxt = [(2 * (k + alpha - 1) * t[h] * cur[h]
                - (k + 2 * alpha - 2) * prev[h]) / k
               for h in range(d + 1)]
        yield k, nxt
        prev, cur = cur, nxt


def predicted_levels(d, k):
    return {j for j in range(d + 1)
            if j <= k and j % 2 == k % 2
            and not (k == 2 and j == 0)
            and not (k == d + 2 and j == d)}


def check():
    checked = 0
    for d in range(3, 13):
        for k, values in exact_kernel_values(d, d + 2):
            lambdas = [sum(krawtchouk(d, h, j) * values[h]
                           for h in range(d + 1))
                       for j in range(d + 1)]
            observed = {j for j, v in enumerate(lambdas) if v > 0}
            assert observed == predicted_levels(d, k), (d, k, observed, predicted_levels(d, k))
            assert all(v >= 0 for v in lambdas), (d, k)
            rank = sum(comb(d, j) for j in observed)
            assert rank == sum(comb(d, j) for j in predicted_levels(d, k))
            if k in (d, d + 1):
                assert rank == 2 ** (d - 1)
            if k == d + 2:
                assert rank == 2 ** (d - 1) - 1 and lambdas[d] == 0
            checked += len(lambdas)
    # Explicit nonzero witnesses for the lower Walsh levels and constants.
    for s in range(30):
        im = sum((-1) ** ((r - 1) // 2) * comb(2 * s + 1, r)
                 for r in range(1, 2 * s + 2, 2))
        assert abs(im) == 2 ** s
    for k in range(4, 80, 2):
        if k % 4 == 0:
            assert (-1) ** (k // 4) * 2 ** (k // 2) != 0
        else:
            assert k >= 6
            coeff = Q(k * (k - 2), 2) * (-1) ** ((k - 2) // 4) * 2 ** ((k - 2) // 2)
            assert coeff != 0
    print('CUBE_EXACT_DEGREE_RANK_OK', checked, 'exact Krawtchouk spectral checks; 10 dimensions')


if __name__ == '__main__':
    check()
