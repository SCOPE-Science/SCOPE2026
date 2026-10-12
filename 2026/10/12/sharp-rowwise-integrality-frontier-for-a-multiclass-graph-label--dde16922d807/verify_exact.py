#!/usr/bin/env python3
"""Exact-rational spot checks for a graph-labeling penalty and two-node witness.

The accompanying proof, not finite testing, establishes the universal results.
"""
from fractions import Fraction as F
from itertools import product


def energy(rows, eps, weight, target, laplacian):
    n = len(rows)
    k = len(rows[0])
    assert all(sum(row) == 1 and min(row) >= 0 for row in rows)
    graph = sum(laplacian[i][j] * rows[i][z] * rows[j][z]
                for i in range(n) for j in range(n) for z in range(k)) / 2
    penalty = sum(1 - sum(x*x for x in row) for row in rows) / eps
    fidelity = sum(weight[i] * sum((rows[i][z]-target[i][z])**2
                      for z in range(k)) for i in range(n)) / 2
    return graph + penalty + fidelity


K = 3
L = ((F(1), F(-1)), (F(-1), F(1)))
W = (F(1), F(0))
T = ((F(1), F(0), F(0)), (F(0), F(0), F(0)))
unit = tuple(tuple(F(int(i == j)) for i in range(K)) for j in range(K))
xstar = (F(1, 2), F(1, 2), F(0))
ystar = unit[1]
Ustar = (xstar, ystar)


def coeff(eps):
    return tuple(1 / eps - (L[i][i] + W[i]) / 2 for i in range(2))


def gradient(rows, eps):
    n, k = len(rows), len(rows[0])
    return tuple(tuple(sum(L[i][j]*rows[j][z] for j in range(n))
                       + (1-2*rows[i][z])/eps
                       + W[i]*(rows[i][z]-T[i][z])
                       for z in range(k)) for i in range(n))


def expected_rounding(rows, eps):
    out = F(0)
    for a, b in product(range(K), repeat=2):
        p = rows[0][a] * rows[1][b]
        out += p * energy((unit[a], unit[b]), eps, W, T, L)
    return out


for eps in (F(1, 2), F(4, 5), F(1), F(3, 2), F(3)):
    for rows in (
        ((F(1, 3), F(1, 2), F(1, 6)), (F(1, 4), F(1, 4), F(1, 2))),
        Ustar,
        (unit[0], unit[1]),
    ):
        rhs = energy(rows, eps, W, T, L) - sum(
            coeff(eps)[i] * (1-sum(x*x for x in rows[i])) for i in range(2))
        assert expected_rounding(rows, eps) == rhs

for eps in (F(1), F(3, 2), F(7, 4)):
    assert energy(Ustar, eps, W, T, L) == F(1, 2) + F(1, 2) / eps
    assert min(energy((unit[a], unit[b]), eps, W, T, L)
               for a, b in product(range(K), repeat=2)) == 0

# At epsilon=3/2 the labeled row has positive restricted curvature,
# the unlabeled vertex has strict first-order gaps in both other classes.
eps = F(3, 2)
assert 2 - 2/eps == F(2, 3)
assert 2/eps - 1 == F(1, 3)
assert 2/eps - F(1, 2) == F(5, 6)
assert 1/eps == F(2, 3)  # row-1 inactive-class gap
g = gradient(Ustar, eps)
assert g[0][0] == g[0][1] == 0
assert g[0][2]-g[0][0] == F(2, 3)
assert g[1][0]-g[1][1] == F(1, 3)
assert g[1][2]-g[1][1] == F(5, 6)

# At epsilon=1 the labeled row has zero restricted curvature, and
# a continuum of local minima appears along the first two classes.
for p in (F(0), F(1, 5), F(1, 2), F(4, 5), F(1)):
    xx = (p, 1-p, F(0))
    assert energy((xx, ystar), F(1), W, T, L) == F(1)

# The new guarantee applies at epsilon=4/5 when the source's global
# Hessian remains indefinite, because det(L+W-2I/epsilon)<0.
eps = F(4, 5)
h11 = L[0][0] + W[0] - 2/eps
h22 = L[1][1] + W[1] - 2/eps
assert h11 < 0 and h22 < 0
assert h11*h22 - L[0][1]**2 == F(-1, 4)

print('VERIFY_OK: rounding identities, threshold margins, and witness energy')
