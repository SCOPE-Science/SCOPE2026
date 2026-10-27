"""Exact finite checks of the path phase-map winding threshold formulas.

The infinite-family theorem is proved analytically; these are independent
rational tests of lattice residues, saturation and multiplicity.
"""
from fractions import Fraction
from itertools import product
from math import gcd, prod


def least_odd_prime(m):
    for q in range(3, m + 1, 2):
        if m % q == 0 and all(q % j for j in range(2, int(q**0.5) + 1)):
            return q
    return None


def totient(n):
    return sum(gcd(j, n) == 1 for j in range(1, n + 1))


def expected(m):
    n = m - 1
    p = least_odd_prime(m)
    if p is not None:
        t = Fraction(p - 1, 2 * p)
        return t, (p - 1) * 2 ** (n - 2 * (m // p)), (p - 1) * 2 ** n
    return (Fraction(1, 2), (m - 1) * 2 ** n,
            2 ** n * sum(totient(d) * 2 ** (m // d)
                         for d in range(2, m + 1) if m % d == 0))


def least_representatives(k, m):
    """Enumerate minimax-residue representatives of the cyclic class k."""
    positions = []
    for i in range(1, m):
        r = Fraction((i * k) % m, m)
        if r < Fraction(1, 2):
            positions.append((r,))
        elif r > Fraction(1, 2):
            positions.append((r - 1,))
        else:
            positions.append((Fraction(-1, 2), Fraction(1, 2)))
    return product(*positions)


def check(m):
    n = m - 1
    t, boundary_pred, near_pred = expected(m)
    seen = set()
    boundary = near = 0
    min_norm = None
    for k in range(1, m):
        for u in least_representatives(k, m):
            # Every candidate is an integer-lattice inverse: K u = w.
            w = tuple(2 * u[i] - (u[i - 1] if i else 0)
                      - (u[i + 1] if i + 1 < n else 0) for i in range(n))
            assert all(x.denominator == 1 for x in w)
            assert any(w)
            assert w not in seen
            seen.add(w)
            norm = max(abs(v) for v in u)
            if min_norm is None or norm < min_norm:
                min_norm = norm
            if norm == t:
                saturated = sum(abs(v) == t for v in u)
                boundary += 2 ** (n - saturated)
                near += 2 ** n
    assert min_norm == t, (m, min_norm, t)
    assert boundary == boundary_pred, (m, boundary, boundary_pred)
    assert near == near_pred, (m, near, near_pred)
    print(f'm={m:2d}: t={t}, at-threshold new fixed={boundary}, '
          f'just-above new fixed={near}: exact checks PASS')


if __name__ == '__main__':
    for length in range(2, 17):
        check(length)
    print('ALL_EXACT_WINDING_CHECKS_PASS')
