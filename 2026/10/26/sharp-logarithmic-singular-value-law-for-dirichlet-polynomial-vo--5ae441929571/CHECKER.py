"""Finite consistency checks for Dirichlet-polynomial Volterra coefficients.

Uses only the Python standard library. No finite check proves a singular-value asymptotic.
"""
from math import log, isclose
from itertools import combinations


def multiply(a, b):
    out = {}
    for n, x in a.items():
        for m, y in b.items():
            out[n * m] = out.get(n * m, 0j) + x * y
    return out


def volterra(g, f):
    out = {}
    for m, b in g.items():
        if m == 1:
            continue
        for n, a in f.items():
            out[n * m] = out.get(n * m, 0j) + a * b * log(m) / log(n * m)
    return out


def factorized(g, f):
    h = {m: b * log(m) for m, b in g.items() if m >= 2}
    return {k: v / log(k) for k, v in multiply(h, f).items()}


def agree(a, b, tol=1e-12):
    for k in set(a) | set(b):
        assert abs(a.get(k, 0) - b.get(k, 0)) < tol


def test():
    count = 0
    gs = [
        {2: 1 + 0j},
        {2: 1 + 1j, 3: -2 + 0.5j},
        {2: 1, 4: -3j, 6: 2.4, 9: -1},
    ]
    fs = [{1: 1}, {1: 2 - 3j, 2: 4, 7: -1.5j}, {5: 1, 10: 3, 12: -2}]
    for g in gs:
        for f in fs:
            agree(volterra(g, f), factorized(g, f))
            count += len(set(volterra(g, f)))

    # Monomial images have pairwise disjoint basis support and decreasing norms.
    for m in (2, 3, 6, 10):
        for n in range(1, 101):
            out = volterra({m: 1}, {n: 1})
            assert len(out) == 1 and m*n in out
            assert isclose(abs(out[m*n]), log(m) / log(m*n), abs_tol=1e-14)
            count += 1

    # Coprime-fiber orthogonality for a two-prime symbol and a polynomial in those primes.
    g = {2: 1 + 2j, 3: 3j, 6: -1}
    q = {1: 1, 2: -2, 3: 1j, 4: 0.3}
    rs = [5, 7, 11, 13, 17, 19, 23, 25, 29]
    for r, s in combinations(rs, 2):
        fr = {r*k: v for k, v in q.items()}
        fs_ = {s*k: v for k, v in q.items()}
        assert not (set(fr) & set(fs_))
        assert not (set(volterra(g, fr)) & set(volterra(g, fs_)))
        count += 2

    print(f'PASS: {count} finite coefficient/orthogonality assertions.')


if __name__ == '__main__':
    test()
