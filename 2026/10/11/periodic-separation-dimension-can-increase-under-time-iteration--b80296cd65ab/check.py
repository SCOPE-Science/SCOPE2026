"""Finite exact-rational diagnostics for a compact periodic-orbit system.

No finite diagnostic is used to establish the infinite critical exponents.
"""
from fractions import Fraction
from itertools import combinations


def harmonic(m):
    return sum((Fraction(1, j) for j in range(1, m + 1)), Fraction(0))


def level(q, m):
    r = 1 / harmonic(m)
    eps = Fraction(1, 100 * q * m * m * (2 ** (m*m)))
    pts = [(r * Fraction(j, m), Fraction(1, m) + h * eps)
           for j in range(m) for h in range(q)]
    return r, eps, pts


def dist2(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


def orbit_indices(q, m, power, start):
    cur = start
    indices = []
    while cur not in indices:
        indices.append(cur)
        j, h = divmod(cur, q)
        cur = ((j * q + h + power) % (m * q))
    assert cur == start
    return indices


def check():
    checks = 0
    for q in range(2, 7):
        for m in range(2, 13):
            r, eps, pts = level(q, m)
            assert eps < r / m
            assert len(set(pts)) == m * q
            full = orbit_indices(q, m, 1, 0)
            assert len(full) == m * q
            delta2 = min(dist2(pts[a], pts[b]) for a, b in combinations(full, 2))
            assert delta2 == eps * eps, (q, m, delta2, eps*eps)
            checks += 1
            for h in range(q):
                reduced = orbit_indices(q, m, q, h)
                assert len(reduced) == m
                assert len(set(reduced)) == m
                d2 = min(dist2(pts[a], pts[b]) for a, b in combinations(reduced, 2))
                assert d2 == (r / m) ** 2, (q, m, h, d2, (r/m)**2)
                checks += 1
        for m in range(2, 31):
            _, eps, _ = level(q, m)
            _, eps_next, _ = level(q, m + 1)
            assert Fraction(1, m+1) + (q-1)*eps_next < Fraction(1, m)
            assert Fraction(1, m) + (q-1)*eps < Fraction(1, m-1)
            checks += 1
    print('PASS', checks, 'exact rational diagnostics')

if __name__ == '__main__':
    check()
