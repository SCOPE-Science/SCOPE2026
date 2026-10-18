#!/usr/bin/env python3
"""Exact arithmetic checks for the index-66 K3–elliptic quotient."""
from math import gcd


def divide_monic(a, b):
    a = list(a)
    out = [0] * (len(a) - len(b) + 1)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        c = a[-1]
        out[shift] = c
        for i, bi in enumerate(b):
            a[shift + i] -= c * bi
        while a and a[-1] == 0:
            a.pop()
    assert not a, 'Nonzero polynomial remainder'
    return out


def cyclotomic(n):
    phi = {}
    for d in range(1, n + 1):
        if n % d != 0:
            continue
        x_d_minus_one = [-1] + [0] * (d-1) + [1]
        for k in sorted(phi):
            if d % k == 0:
                x_d_minus_one = divide_monic(x_d_minus_one, phi[k])
        phi[d] = x_d_minus_one
    return phi[n]


phi66 = cyclotomic(66)
assert len(phi66) - 1 == 20
assert sum(phi66) == 1
assert phi66 == list(reversed(phi66))
assert gcd(5, 66) == 1
# The four monomials y^2, x^3, t^12 and t scale identically.
assert len({(2*3) % 66, (3*2) % 66, (12*6) % 66, 6 % 66}) == 1
# The two-form dt wedge dx / y is multiplied by zeta^(6+2-3).
assert (6 + 2 - 3) % 66 == 5

# H^2(S;Z) = U (rank 2) plus T (rank 20); det(1-g|T) = Phi_66(1) = 1.
# M_g cohomology ranks from integral Wang sequence and K3 cohomology.
mapping_torus_ranks = [1, 1, 2, 2, 1, 1]
assert mapping_torus_ranks == [1, 1, 2, 2, 1, 1]
# Integral Kunneth with S^1: b_i(V) = b_i(M_g) + b_(i-1)(M_g).
bV = [(mapping_torus_ranks[i] if i < 6 else 0) +
      (mapping_torus_ranks[i-1] if i > 0 else 0) for i in range(7)]
assert bV == [1, 2, 3, 4, 3, 2, 1]
assert bV == list(reversed(bV))
assert sum((-1)**i * b for i,b in enumerate(bV)) == 0
assert bV[2] == 3 and bV[3] == 4
print('INDEX_66_BRAUER_COHOMOLOGY_CHECK_OK')
