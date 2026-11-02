#!/usr/bin/env python3
"""Exact binary-word checks for the baker-map quantile discrepancy theorem.

Uses integer arithmetic and fractions; no external packages or numerical fitting.
"""
from fractions import Fraction
from itertools import product


def words(m):
    return [''.join(z) for z in product('01', repeat=m)]


def reverse_pairs(m):
    return [(w, w[::-1]) for w in words(m) if w < w[::-1]]


def basis(m):
    out = []
    for w, rw in reverse_pairs(m):
        out.append({z: (1 if z == w else -1 if z == rw else 0)
                    for z in words(m)})
    return out


def covariance(f, g, lag):
    m = len(next(iter(f)))
    assert m == len(next(iter(g)))
    s = sum(f[z[:m]] * g[z[lag:lag + m]]
            for z in words(m + lag))
    return Fraction(s, 2 ** (m + lag))


def green_kubo(f, g):
    m = len(next(iter(f)))
    return (covariance(f, g, 0) +
            sum((covariance(f, g, t) + covariance(g, f, t)
                 for t in range(1, m)), Fraction(0)))


def is_gradient(f):
    """Check existence of a potential on length-(m-1) binary states."""
    m = len(next(iter(f)))
    if m == 1:
        return all(x == 0 for x in f.values())
    V = {'0' * (m - 1): 0}
    for _ in range(2 ** (m - 1) + 1):
        changed = False
        for w in words(m):
            p, s = w[:-1], w[1:]
            if p in V and s not in V:
                V[s] = V[p] + f[w]
                changed = True
            elif s in V and p not in V:
                V[p] = V[s] - f[w]
                changed = True
        if not changed:
            break
    return len(V) == 2 ** (m - 1) and all(
        V[w[1:]] - V[w[:-1]] == f[w] for w in words(m))


def quantile_odd(m, k):
    def phi(w):
        return int(int(w, 2) < k)
    return {w: phi(w) - phi(w[::-1]) for w in words(m)}


def ell(f):
    return f['0010'] - f['0011'] + f['0101'] + f['1011']


def check_all():
    for m in (1, 2, 3):
        for f in basis(m):
            assert is_gradient(f), (m, f)
        for k in range(1, 2 ** m):
            assert is_gradient(quantile_odd(m, k)), (m, k)

    B = basis(4)
    pairs = reverse_pairs(4)
    expected_pairs = [('0001', '1000'), ('0010', '0100'),
                      ('0011', '1100'), ('0101', '1010'),
                      ('0111', '1110'), ('1011', '1101')]
    assert pairs == expected_pairs
    lv = [0, 1, -1, 1, 0, 1]
    for i in range(6):
        for j in range(6):
            assert green_kubo(B[i], B[j]) == Fraction(lv[i] * lv[j], 32)
    assert [covariance(B[1], B[1], n) for n in range(4)] == [
        Fraction(1, 8), Fraction(-1, 32), Fraction(-1, 64), Fraction(0)]

    # The five generators of ker(ell) are exact graph coboundaries.
    for i in (0, 4):
        assert is_gradient(B[i])
    for coeff in ((0, 1, 1, 0, 0, 0),
                  (0, -1, 0, 1, 0, 0),
                  (0, -1, 0, 0, 0, 1)):
        z = {w: sum(coeff[i] * B[i][w] for i in range(6))
             for w in words(4)}
        assert is_gradient(z)

    nonzero = {}
    for k in range(1, 16):
        z = quantile_odd(4, k)
        e = ell(z)
        assert green_kubo(z, z) == Fraction(e * e, 32)
        assert is_gradient(z) == (e == 0)
        if e:
            nonzero[k] = e
    assert nonzero == {3: 1, 5: -1, 11: -1, 13: 1}
    print('PASS: all reversal-odd blocks of length <=3 are gradients')
    print('PASS: rank-one six-by-six exact Green-Kubo matrix /32')
    print('PASS: all four-bit quantile thresholds; nonzero ell:', nonzero)
    print('PASS: full six-dimensional coboundary test on the binary de Bruijn graph')


if __name__ == '__main__':
    check_all()
