#!/usr/bin/env python3
"""Exact arithmetic checks for the two-step residual-weighted Kaczmarz example.

Requires only the Python standard library. The symbolic two-row inequality
is proved separately in RESULT.md; finite checks here are consistency tests.
"""
from fractions import Fraction as Q
from itertools import product

V = ((0, 1, 1), (2, 1, 0), (1, -1, 0))
NORMS2 = tuple(sum(t*t for t in r) for r in V)
TARGET = (Q(2), Q(0), Q(2))
ZERO = (Q(0), Q(0), Q(0))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def shrink(y, lam):
    return tuple(max(abs(t)-lam, 0) * (1 if t >= 0 else -1) for t in y)


def update(y, row, lam):
    x = shrink(y, lam)
    residual_unscaled = dot(V[row], tuple(x[j]-TARGET[j] for j in range(3)))
    coeff = residual_unscaled / NORMS2[row]
    return tuple(y[j]-coeff*V[row][j] for j in range(3))


def residuals2(y, lam):
    e = tuple(shrink(y, lam)[j]-TARGET[j] for j in range(3))
    return tuple(dot(v, e)**2 / n for v, n in zip(V, NORMS2))


def sqerror(y, lam):
    e = tuple(shrink(y, lam)[j]-TARGET[j] for j in range(3))
    return dot(e, e)


def probabilities(y, lam, power):
    if power == 0:
        return (Q(1, 3),) * 3
    assert power % 2 == 0 and power >= 2
    weights = [r**(power//2) for r in residuals2(y, lam)]
    normalizer = sum(weights)
    return tuple(w/normalizer for w in weights)


def expected_error(lam, power, horizon):
    states = [(Q(1), ZERO)]
    for _ in range(horizon):
        nxt = []
        for prob, y in states:
            for row, w in enumerate(probabilities(y, lam, power)):
                nxt.append((prob*w, update(y, row, lam)))
        states = nxt
    return sum(prob*sqerror(y, lam) for prob, y in states)


def test():
    assert NORMS2 == (2, 5, 2)
    assert residuals2(ZERO, Q(1, 2)) == (Q(2), Q(16, 5), Q(2))
    first_2 = update(ZERO, 1, Q(1, 2))
    assert first_2 == (Q(8, 5), Q(4, 5), Q(0))
    assert shrink(first_2, Q(1, 2)) == (Q(11, 10), Q(3, 10), Q(0))
    assert residuals2(first_2, Q(1, 2)) == (Q(289, 200), Q(90, 200), Q(144, 200))
    second_21 = update(first_2, 0, Q(1, 2))
    assert shrink(second_21, Q(1, 2)) == (Q(11, 10), Q(23, 20), Q(7, 20))
    assert sqerror(second_21, Q(1, 2)) == Q(971, 200)
    nine = [[sqerror(update(update(ZERO, i, Q(1, 2)), j, Q(1, 2)), Q(1, 2)) for j in range(3)] for i in range(3)]
    assert nine == [
        [Q(6), Q(49, 10), Q(61, 16)],
        [Q(971, 200), Q(89, 20), Q(409, 100)],
        [Q(61, 16), Q(401, 100), Q(6)],
    ], nine
    assert expected_error(Q(1, 2), 0, 1) == Q(179, 30)
    assert expected_error(Q(1, 2), 0, 2) == Q(4193, 900)
    assert expected_error(Q(1, 2), 24, 1) < Q(179, 30)
    assert expected_error(Q(1, 2), 24, 2) > Q(4193, 900)
    bound = Q(971, 200) * Q(100, 101) * Q(2048, 2049)
    assert Q(5, 8)**12 < Q(1, 200)
    assert Q(90, 289) < Q(1, 2) and Q(144, 289) < Q(1, 2)
    assert bound > Q(4193, 900)
    assert expected_error(Q(1, 2), 24, 2) > bound
    # The same row geometry has a smaller reversal for orthogonal projection.
    assert expected_error(Q(0), 0, 2) == Q(101, 25)
    assert sqerror(update(update(ZERO, 1, Q(0)), 0, Q(0)), Q(0)) == Q(102, 25)
    assert sqerror(update(update(ZERO, 1, Q(0)), 2, Q(0)), Q(0)) == Q(102, 25)
    assert expected_error(Q(0), 24, 2) > Q(101, 25)
    # Recheck algebraic identity for a two-row unsparsified problem on a grid.
    checks = 0
    for c_num, u_num, v_num in product(range(-3, 4), repeat=3):
        c, u, v = Q(c_num, 3), Q(u_num), Q(v_num)
        if abs(u) < abs(v):
            u, v = v, u
        lhs = (1+3*c*c)*u*u+(1-c*c)*v*v-4*c*u*v
        rhs = (1+c*c)*(u*u-v*v)+2*(c*u-v)**2
        assert lhs == rhs and rhs >= 0
        checks += 1
    print("verified: 7 path/normalization checks; p=0,24 exact expectations; all-real-p bound;")
    print(f"two-row identity {checks} rational instances; uniform risk 4193/900; bound={bound}")


if __name__ == '__main__':
    test()
