#!/usr/bin/env python3
"""Exact monomial-Cartier verification for the stated Serre-type family.

Finite instances test the formula, its regular-differential domain,
all monomial images, the nilpotency index, and the explicit terminal witness.
No numerical experiment is offered as an infinite proof.
"""
from functools import lru_cache


def instance(p, t, n):
    q = p ** t
    Q = q * q
    assert n >= 3 and n % 2 == 1
    assert (q ** n + 1) % (q + 1) == 0
    m = (q ** n + 1) // (q + 1)
    b = (q ** (n - 1) - 1) // (q + 1)
    assert (q ** (n - 1) - 1) % (q + 1) == 0
    assert m % p == 1 and b % p == p - 1
    genus = (Q - 1) * (m - 1) // 2
    top = 2 * genus - 2
    basis = {(i, j) for j in range(Q)
             for i in range((top - m * j) // Q + 1)
             if top - m * j >= 0}
    assert len(basis) == genus

    def cartier(monomial):
        i, j = monomial
        i0, j0 = i % p, j % p
        if i0 + j0 < p - 1:
            return None
        nu = i0 + j0 - (p - 1)
        S = (i + m * (j0 - nu) - (p - 1)) // p
        E = j // p + (Q // p) * nu
        assert 0 <= nu <= j0
        assert (S, E) in basis
        # A selected binomial coefficient is nonzero in the prime field.
        from math import comb
        coefficient = (-1 if (j0 - nu) % 2 else 1) * comb(j0, nu)
        assert coefficient % p != 0
        return (S, E), coefficient % p

    @lru_cache(None)
    def steps(v):
        arrow = cartier(v)
        return 0 if arrow is None else 1 + steps(arrow[0])

    assert all(steps(v) <= t * n - 1 for v in basis)
    assert max(steps(v) for v in basis) == t * n - 1
    w = (p ** (t - 1) * b - 1, p ** (t - 1))
    assert w in basis
    v, scalar = w, 1
    for index in range(t * n - 1):
        arrow = cartier(v)
        assert arrow is not None, (p, t, n, index, v)
        v, a = arrow
        scalar = (scalar * a) % p
    assert v == (0, 0), (p, t, n, v)
    assert scalar == (-1) % p, (p, t, n, scalar)
    assert cartier(v) is None
    assert steps(w) == t * n - 1
    return q, n, genus, t * n


def main():
    trials = ((2, 1, 3), (2, 1, 5), (2, 1, 7),
              (2, 2, 3), (2, 2, 5),
              (3, 1, 3), (3, 1, 5), (3, 1, 7), (3, 2, 3),
              (5, 1, 3), (5, 1, 5), (7, 1, 3))
    for p, t, n in trials:
        q, nn, g, order = instance(p, t, n)
        print('checked q=%d n=%d genus=%d index=%d' % (q, nn, g, order))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
