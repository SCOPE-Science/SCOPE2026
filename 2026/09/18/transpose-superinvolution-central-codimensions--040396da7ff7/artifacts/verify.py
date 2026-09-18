"""Exact checks for the codimension identities in RESULT.md."""
from math import comb
from fractions import Fraction


def source_full(n):
    s = sum(Fraction(comb(n, j) * comb(j, j // 2), 2**j) for j in range(n + 1))
    return 2**n * (2 * s - 1)


def closed_full(n):
    return comb(2 * n + 2, n + 1) - 2**n


def central_layer_by_compositions(n):
    first = sum(comb(n, n2) for n2 in range(0, n + 1, 2))
    second = 0
    for k in range(1, n // 2 + 1):
        r = n - 2 * k
        second += comb(n, 2 * k) * comb(2 * k, k) * 2**r
    return first + second


def closed_layer(n):
    return comb(2 * n, n) - 2 ** (n - 1)


for n in range(1, 101):
    assert source_full(n) == closed_full(n)
    assert central_layer_by_compositions(n) == closed_layer(n)
    central_codim = closed_full(n) - closed_layer(n)
    assert central_codim == Fraction(3 * n + 1, n + 1) * comb(2 * n, n) - 2 ** (n - 1)

print("verified n=1..100")
