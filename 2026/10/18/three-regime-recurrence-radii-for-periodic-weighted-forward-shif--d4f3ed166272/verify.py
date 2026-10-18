"""Finite diagnostics for the periodic weighted-shift recurrence-radius theorem.

Proof of the infinite-dimensional statement is analytic; these checks only test
explicit identities and an exact nonconvex witness.
"""
from fractions import Fraction as Q
from math import sqrt
import random


def squared_radius_critical(weights, coords):
    q = len(weights)
    product = 1.0
    for w in weights:
        product *= w
    assert abs(product - 1) < 1e-12
    c = [1.0]
    for w in weights[:-1]:
        c.append(c[-1] * w)
    base = sum(abs(z) ** 2 for z in coords)
    return base + min(
        sum(abs(z) ** 2 * (c[(j + r) % q] / c[j % q]) ** 2
            for j, z in enumerate(coords)) for r in range(q)
    )


def direct_sq_distance(weights, coords, n):
    q = len(weights)
    z = list(coords) + [0.0] * n
    image = [0.0] * n + list(coords)
    for j in range(len(coords)):
        multiplier = 1.0
        for k in range(n):
            multiplier *= weights[(j + k) % q]
        image[j + n] *= multiplier
    return sum(abs(a - b) ** 2 for a, b in zip(image, z))


def validate():
    # Exact algebraic inequalities using rational arithmetic and the bound sqrt(14)>13/4.
    a0, a1 = Q(4, 5), Q(1, 5)
    b0 = Q(3, 5)
    assert Q(5, 4)*a0*a0 + 5*a1*a1 == 1
    assert 2*(b0*b0 + Q(14, 100)) == 1
    assert 2*(a0*a0+a1*a1) == Q(34, 25)
    assert Q(5, 4)*b0*b0 + 5*Q(14, 100) == Q(23, 20)
    assert (Q(107, 100) + Q(2, 100)*Q(13, 4)) > 1
    assert (Q(67, 80) + Q(4, 80)*Q(13, 4)) == 1
    # The two strict midpoint inequalities use sqrt(14)>13/4, since 14>(13/4)^2.
    assert 14 > Q(13, 4)**2

    random.seed(731)
    diagnostics = 0
    for weights in ([0.5, 2.0], [0.8, 1.25], [0.5, 1.5, 4/3], [1.0]):
        q = len(weights)
        for _ in range(60):
            x = [random.uniform(-1, 1) for _ in range(8)]
            expected = squared_radius_critical(weights, x)
            # Take n beyond finite support so the weak cross term vanishes exactly.
            observed = min(direct_sq_distance(weights, x, n) for n in range(64, 64 + q))
            assert abs(expected - observed) < 1e-9, (weights, expected, observed)
            diagnostics += 1
    for weights, regime in [([0.4, 0.5], -1), ([0.5, 2.0], 0), ([2.0, 1.4], 1)]:
        product = weights[0]*weights[1]
        assert (product < 1) - (product > 1) == -regime
    assert abs(squared_radius_critical([0.5, 2.0], [0.8, 0.2]) - 1) < 1e-12
    b = [0.6, sqrt(14)/10]
    assert abs(squared_radius_critical([0.5, 2.0], b) - 1) < 1e-12
    m = [(0.8+b[0])/2, (0.2+b[1])/2]
    assert squared_radius_critical([0.5, 2.0], m) > 1.02
    print('PASS: exact witness inequalities; %d phase-iterate checks; growth-regime signs' % diagnostics)

if __name__ == '__main__':
    validate()
