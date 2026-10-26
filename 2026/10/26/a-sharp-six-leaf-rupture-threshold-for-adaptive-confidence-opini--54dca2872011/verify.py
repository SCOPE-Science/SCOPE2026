"""Exact finite checks supplementing the analytical star-network theorem.

Run with Python 3 standard library: python verify.py.
The finite checks do not replace the proof for all star degrees.
"""
from fractions import Fraction as Q
from itertools import product


def bmat(k):
    return [[(Q(1, 2) if i == j else Q(0)) - Q(1, k + 1)
             for j in range(k)] for i in range(k)]


def mm(a, b):
    return [[sum(a[i][z] * b[z][j] for z in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def norm_inf(a):
    return max(sum(abs(x) for x in row) for row in a)


def next_full(x):
    k = len(x) - 1
    return [sum(x) / (k + 1)] + [(x[0] + a) / 2 for a in x[1:]]


def next_actual(x, bounds, gamma, delta):
    k = len(x) - 1
    receptive = [abs(x[0] - x[i + 1]) < bounds[i] for i in range(k)]
    center_group = [x[0]] + [x[i + 1] for i in range(k) if receptive[i]]
    y = [sum(center_group) / len(center_group)]
    y += [(x[0] + x[i + 1]) / 2 if receptive[i] else x[i + 1]
          for i in range(k)]
    return y, [b + gamma * (1 - b) if receptive[i] else delta * b
               for i, b in enumerate(bounds)], receptive


checks = 0
for k in range(1, 26):
    b = bmat(k)
    kappa = Q(3 * (k - 1), 2 * (k + 1))
    assert norm_inf(b) == kappa
    checks += 1
    bb = mm(b, b)
    assert norm_inf(bb) == (Q(0) if k == 1 else Q(1, 4) + Q(k - 2, (k + 1)**2))
    checks += 1
    p = b
    for t in range(1, 10):
        assert norm_inf(p) <= (kappa if t == 1 else Q(1))
        checks += 1
        p = mm(p, b)
    c0 = Q(1, 4)
    threshold = max(Q(0), Q(k - 5, 2 * (k + 1)) * c0 / (1 - c0))
    if k >= 6:
        eta = Q(1, 100)
        x = [Q(1, 2), Q(1, 2) - c0 * (1 - eta)] + [Q(1, 2) + c0 * (1 - eta)] * (k - 1)
        assert all(abs(x[0] - z) < c0 for z in x[1:])
        x1, _, recept = next_actual(x, [c0] * k, Q(0), Q(1))
        assert all(recept)
        assert abs(x1[0] - x1[1]) > c0
        checks += 3
        # A strictly subcritical reinforcement can be chosen while preserving the rupture.
        g = threshold / 4
        x1, c1, _ = next_actual(x, [c0] * k, g, Q(1, 2))
        assert abs(x1[0] - x1[1]) >= c1[0]
        checks += 1
    if k <= 9:
        for sig in product((-1, 1), repeat=k):
            # Strictly-receptive data with both signs of hub-to-leaf gaps.
            c0 = Q(1, 4)
            x = [Q(1, 2)] + [Q(1, 2) - Q(99, 100)*c0*s for s in sig]
            g = max(Q(0), Q(k-5, 2*(k+1))*c0/(1-c0))
            bounds = [c0]*k
            for t in range(12):
                y, newbounds, recept = next_actual(x, bounds, g, Q(1, 3))
                assert all(recept)
                assert y == next_full(x)
                checks += 2
                x, bounds = y, newbounds
for k in range(1, 25):
    x = [Q(2, 5)] + [Q((3*i+1) % 11, 11) for i in range(k)]
    pi = [Q(k + 1, 3*k + 1)] + [Q(2, 3*k+1)]*k
    total = sum(pi[i]*x[i] for i in range(k+1))
    assert sum(pi) == 1
    assert total == sum(pi[i]*next_full(x)[i] for i in range(k+1))
    checks += 2
assert Q(3 * (6 - 1), 2*(6 + 1)) == Q(15, 14)
assert Q(6 - 5, 2*(6 + 1))*Q(1, 4)/(1-Q(1, 4)) == Q(1, 42)
print(f'PASS: {checks} exact-rational finite checks; sharp six-leaf witness and invariant checked')
