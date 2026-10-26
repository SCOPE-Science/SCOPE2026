#!/usr/bin/env python3
"""Exact-rational check for the explicit three-agent model witness."""
from fractions import Fraction as Q

W = [[Q(0), Q(1, 2), Q(1, 2)],
     [Q(1, 2), Q(0), Q(1, 2)],
     [Q(1, 2), Q(1, 2), Q(0)]]
gam = [Q(5), Q(1, 5), Q(1)]
x = [Q(3, 4), Q(1, 4), Q(1, 2)]


def matvec(w, v):
    return [sum(w[i][j] * v[j] for j in range(3)) for i in range(3)]


def scalar_response(z, g):
    return g * z / (1 + (g - 1) * z)


def transform(v, g):
    u = matvec(W, v)
    return [scalar_response(u[i], g[i]) for i in range(3)]


def positive_pf_certificate(g, a):
    linear = [g[i] * v for i, v in enumerate(matvec(W, a))]
    assert all(linear[i] > a[i] > 0 for i in range(3))
    return [linear[i] - a[i] for i in range(3)]


assert [sum(row) for row in W] == [1, 1, 1]
assert matvec(W, x) == [Q(3, 8), Q(5, 8), Q(1, 2)]
assert transform(x, gam) == x
for g in (Q(1, 5), Q(1), Q(5), Q(4, 3)):
    for s in (Q(1, 7), Q(1, 3), Q(7, 9)):
        assert 1 - scalar_response(s, g) == scalar_response(1 - s, 1 / g)
assert positive_pf_certificate(gam, [Q(4), Q(1, 5), Q(3, 2)]) == [Q(1, 4), Q(7, 20), Q(3, 5)]
assert positive_pf_certificate([1 / g for g in gam], [Q(1, 5), Q(4), Q(3, 2)]) == [Q(7, 20), Q(1, 4), Q(3, 5)]
assert transform([1 - v for v in x], [1 / g for g in gam]) == [1 - v for v in x]
print('PASS: exact rational witness and spectral certificates')
