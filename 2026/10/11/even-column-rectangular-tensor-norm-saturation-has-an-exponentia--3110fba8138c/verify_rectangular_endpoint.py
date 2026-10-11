"""Exact finite diagnostics for a rectangular tensor-norm endpoint theorem.

Not a replacement for the dimension-uniform analytic proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def signs(n):
    return list(product((-1, 1), repeat=n))


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def endpoint_ratio(rows):
    n = len(rows[0]); eps = signs(n)
    total = sum(sum(abs(v) for v in row) for row in rows)
    denom = max(sum(abs(dot(row, s)) for row in rows) for s in eps)
    return Fraction(total, denom)


for n in (2, 4, 6, 8):
    eps = signs(n)
    reps = [(1,) + tail for tail in product((-1, 1), repeat=n - 1)]
    exact = Fraction(2**n, comb(n, n//2))
    assert endpoint_ratio(reps) == exact, (n, 'ratio')
    mu = Fraction(sum(abs(sum(e)) for e in eps), len(eps))
    assert mu == Fraction(n * comb(n, n//2), 2**n), (n, 'binomial mean')
    for sz in range(2, n + 1, 2):
        for subset in combinations(range(n), sz):
            coeff = Fraction(sum(abs(sum(e)) * __import__('math').prod(e[j] for j in subset)
                                 for e in eps), len(eps))
            assert coeff != 0, (n, subset, 'nonzero Walsh coefficient')
    varied = (2,) + (1,) * (n - 1)
    f_varied = Fraction(sum(abs(dot(varied, e)) for e in eps), len(eps))
    assert f_varied > Fraction(mu * sum(varied), n), (n, 'strict convexity')
    assert endpoint_ratio(reps[:-1]) < exact, (n, 'missing sign class')
    print('n=', n, 'minimal_rows=', len(reps), 'sharp_ratio=', exact,
          'all_even_Fourier_nonzero=OK')
print('RECTANGULAR_ENDPOINT_FINITE_CHECK_OK')
