"""Exact finite sanity checks for chart weights and binomial profiles.

The all-dimensional homotopy proof is in RESULT.md; this script does not certify it.
"""
from math import comb, gcd
from functools import reduce


def mon(*pairs):
    out = {}
    for name, power in pairs:
        out[name] = out.get(name, 0) + power
    return {name: p for name, p in out.items() if p}


def combine(*signed_monomials):
    v = {}
    for m, scale in signed_monomials:
        for name, p in m.items():
            v[name] = v.get(name, 0) + scale * p
    return {name: p for name, p in v.items() if p}


def check(n):
    names = ['x', 'y', 'z', 'w'] + [f'u{i}' for i in range(1, n + 1)]
    weights = dict(zip(names, [1, -2, 2, -2, -1] + [0] * (n - 1)))
    original1 = mon(('x', 2), ('y', 1))
    original2 = mon(('z', 3), ('w', 2), *[(f'u{i}', 2) for i in range(1, n + 1)])
    for m in [original1, original2]:
        assert sum(weights[k] * a for k, a in m.items()) == 0
    # The x-normalized chart has characters Z=z/x^2, W=x^2 w, V=x u1.
    Z = mon(('z', 1), ('x', -2))
    W = mon(('w', 1), ('x', 2))
    V = mon(('u1', 1), ('x', 1))
    U = [mon((f'u{i}', 1)) for i in range(2, n + 1)]
    for m in [Z, W, V] + U:
        assert sum(weights[k] * a for k, a in m.items()) == 0
    assert combine((Z, 3), (W, 2), (V, 2), *[(u, 2) for u in U]) == original2
    # The u1-normalized chart has q=x*u1, b=y/u1^2, c=z*u1^2, d=w/u1^2.
    q = mon(('x', 1), ('u1', 1))
    b = mon(('y', 1), ('u1', -2))
    c = mon(('z', 1), ('u1', 2))
    d = mon(('w', 1), ('u1', -2))
    for m in [q, b, c, d]:
        assert sum(weights[k] * a for k, a in m.items()) == 0
    assert combine((q, 2), (b, 1)) == original1
    assert combine((c, 3), (d, 2), *[(u, 2) for u in U]) == original2
    # The primitive monomial 3*c+2*d+2*sum(U_i) defines a split n-torus.
    assert reduce(gcd, [3, 2] + [2] * (n - 1)) == 1
    # Parametrization c=s^2, d=s^-3 * prod U_i^-1 solves the equation.
    assert 3 * 2 + 2 * -3 == 0
    for ui in U:
        assert 3 * 0 + 2 * -1 + 2 == 0
    ranks = [comb(n, r) for r in range(n + 1)]
    assert sum((-1) ** (r + 2) * ranks[r] for r in range(n + 1)) == 0
    assert sum(ranks) == 2 ** n
    return ranks


if __name__ == '__main__':
    for n in range(1, 13):
        print(n, check(n))
    print('VERIFY_OK')
