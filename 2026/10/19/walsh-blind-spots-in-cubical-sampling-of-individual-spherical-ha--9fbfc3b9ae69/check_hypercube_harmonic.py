"""Exact rational Walsh-eigenvalue checks for spherical-harmonic samples on cubical vertices.

Usage: python check_hypercube_harmonic.py
Requires Python 3 with SymPy. No network or external data.
"""
from math import comb
import sympy as sp

x = sp.Symbol('x')


def krawtchouk_weight(d, j, h):
    return sum((-1) ** q * comb(j, q) * comb(d-j, h-q)
               for q in range(max(0, h-(d-j)), min(j, h)+1))


def cubical_walsh_eigenvalue(d, ell, j):
    kernel = sp.Poly(sp.gegenbauer(ell, sp.Rational(d-2, 2), x), x)
    return sp.factor(sum(
        krawtchouk_weight(d, j, h) * kernel.eval(sp.Rational(d-2*h, d))
        for h in range(d+1)))


def expected_levels(d, ell):
    levels = {j for j in range(min(d, ell)+1) if (j-ell) % 2 == 0}
    if ell == 2:
        levels.discard(0)
    if ell == d+2:
        levels.discard(d)
    return levels


def main():
    pairs = 0
    for d in range(6, 11):
        for ell in range(d+3):
            expected = expected_levels(d, ell)
            actual = set()
            for j in range(d+1):
                e = cubical_walsh_eigenvalue(d, ell, j)
                if e != 0:
                    if not (e > 0):
                        raise AssertionError((d, ell, j, 'negative', e))
                    actual.add(j)
                pairs += 1
            assert actual == expected, (d, ell, actual, expected)
            r = sum(comb(d, j) for j in actual)
            closed = sum(comb(d, j) for j in range(min(d, ell)+1)
                         if (j-ell) % 2 == 0) - (ell == 2) - (ell == d+2)
            assert r == closed
        print('d=', d, 'all degrees 0..', d+2, 'passed')
    t = sp.symbols('t')
    assert sp.legendre(6, t).subs(t, 1/sp.sqrt(3)) == sp.Rational(2, 9)
    print('PASS:', pairs, 'exact rational spherical-kernel Walsh eigenvalue tests')

if __name__ == '__main__':
    main()
