#!/usr/bin/env python3
"""Exact arithmetic checks for a fastest-mixing problem on binary 1/3-flip graphs.

Standard-library only. This checks formulas and finite instances; the universal
optimization proof and all-dimensional Krawtchouk bound are in RESULT.md.
"""
from fractions import Fraction as F
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def k3(d, j):
    return sum((-1)**i * choose(j, i) * choose(d-j, 3-i)
               for i in range(4))


def vals(d, a, b):
    c = comb(d, 3)
    return [F(1) - 2*j*a - (c-k3(d, j))*b for j in range(1, d+1)]


def candidate(d):
    if d == 3:
        return F(1, 6), F(1, 6), F(1, 3)
    if d == 4:
        return F(1, 12), F(1, 12), F(1, 3)
    if d == 5:
        return F(1, 22), F(1, 22), F(4, 11)
    if d == 6:
        return F(1, 52), F(3, 104), F(5, 13)
    return F(0), F(6, (d+3)*(d-1)*(d-2)), F(d-3, d+3)


# Exact analytic linear dual certificates for dimensions five and six.
for d, indices, weights in [
    (5, (1, 3, 5), (F(5, 22), F(5, 11), F(7, 22))),
    (6, (1, 4, 6), (F(4, 13), F(5, 13), F(4, 13))),
]:
    p, q, r = weights
    i, j, k = indices
    assert p + q + r == 1 and min(weights) > 0
    assert 2*i*p + 2*j*q == 2*k*r
    assert (comb(d, 3)-k3(d, i))*p + (comb(d, 3)-k3(d, j))*q == (comb(d, 3)-k3(d, k))*r
    assert p + q - r == candidate(d)[2]

# Check the algebraic Krawtchouk factor identity in broad exact integer ranges.
factor_checks = 0
for d in range(7, 129):
    assert k3(d, 1) == (d-1)*(d-2)*(d-6)//6
    for j in range(1, d+1):
        Q = 4*j*j + (4-6*d)*j + 3*d*d-9*d+6
        assert 3*(k3(d, 1)-k3(d, j)) == (j-1)*Q
        if d == 7:
            assert Q >= 0  # for integer j; equality at j=5
        else:
            assert 4*Q >= 3*d*d-24*d+20 > 0
        factor_checks += 1

# Exact candidate feasibility and all Fourier-mode bounds, for 3..128.
mode_checks = 0
for d in range(3, 129):
    a, b, mu = candidate(d)
    assert a >= 0 and b >= 0
    assert d*a + comb(d, 3)*b <= 1
    theta = vals(d, a, b)
    assert max(map(abs, theta)) == mu
    for value in theta:
        assert abs(value) <= mu
        mode_checks += 1
    if d >= 7:
        assert a == 0 and b > 0
        assert d*a + comb(d, 3)*b == F(d, d+3)
        assert theta[0] == mu and theta[-1] == -mu
        assert k3(d, d) == -comb(d, 3)
    if d == 7:
        assert theta[4] == mu  # the extra sharp upper spectral contact

# Independent row enumeration: derive character eigenvalues directly from the
# graph's transition probabilities without using Krawtchouk polynomials.
row_checks = 0
for d in range(3, 10):
    a, b, mu = candidate(d)
    n = 1 << d
    hold = 1 - d*a - comb(d, 3)*b
    row = []
    for delta in range(n):
        h = delta.bit_count()
        row.append(hold if h == 0 else a if h == 1 else b if h == 3 else F(0))
    assert sum(row) == 1
    for mask in range(1, n):
        eig = sum(w if (mask & delta).bit_count() % 2 == 0 else -w
                  for delta, w in enumerate(row))
        assert eig == vals(d, a, b)[mask.bit_count()-1]
        row_checks += 1

# Equality/mode certificates that force unique invariant candidates at 5,6.
for d, active in [(5, [1, 3, 5]), (6, [1, 4, 6])]:
    a, b, mu = candidate(d)
    th = vals(d, a, b)
    assert th[active[0]-1] == mu
    assert th[active[1]-1] == mu
    assert th[active[2]-1] == -mu

print(f'VERIFY_OK dual_certificates=2 krawtchouk_factor_cases={factor_checks} '
      f'finite_mode_checks={mode_checks} independent_character_row_checks={row_checks}')
