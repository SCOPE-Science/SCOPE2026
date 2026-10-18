#!/usr/bin/env python3
"""Finite exact monomial-semigroup tests for a tangent-deleted Veronese family.

The infinite-family statements require the separate symbolic proof.
"""
from math import comb


def weak_compositions(length, total):
    if length == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for tail in weak_compositions(length - 1, total - a):
            yield (a,) + tail


def chart_monomials(n, d, i=0):
    return {tuple(v[j] for j in range(n) if j != i)
            for v in weak_compositions(n, d)
            if max(v) != d - 1 and v[i] != d}


def test_chart(n, d, bound=9):
    r = n - 1
    generators = chart_monomials(n, d)
    degree_2_or_3 = {v for degree in (2, 3)
                     for v in weak_compositions(r, degree)}
    assert degree_2_or_3 <= generators
    assert all(sum(v) >= 2 for v in generators)
    reachable = {(0,) * r}
    for degree in range(1, bound + 1):
        for v in weak_compositions(r, degree):
            if any(all(v[j] >= g[j] for j in range(r))
                   and tuple(v[j] - g[j] for j in range(r)) in reachable
                   for g in generators):
                reachable.add(v)
        actual = {v for v in reachable if sum(v) == degree}
        expected = set(weak_compositions(r, degree)) if degree >= 2 else set()
        assert actual == expected, (n, d, degree)
    for q in range(0, 5):
        # Length of (k+m^2)/m^(2q+2) for a polynomial ring in r variables.
        from_monomials = 1 + sum(comb(r + degree - 1, r - 1)
                                 for degree in range(2, 2 * (q + 1)))
        predicted = comb(r + 2 * q + 1, r) - r
        assert from_monomials == predicted
    print(f'PASS n={n}, d={d}, checked_total_degree={bound}')


if __name__ == '__main__':
    for n, d in [(3, 5), (3, 6), (4, 5), (4, 6), (5, 5)]:
        test_chart(n, d)
    print('VERIFY_OK')
