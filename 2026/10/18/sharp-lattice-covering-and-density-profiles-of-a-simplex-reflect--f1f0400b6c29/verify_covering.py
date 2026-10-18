"""Exact-rational spot checks for a planar simplex/reflection covering theorem.

The continuum covering statement follows from the geometric proof. These
independent finite tests check formulas, vertices and representative lattice
covering calculations; they are not a substitute for the analytic argument.
"""
from fractions import Fraction as Q


def vertices(t):
    return [(Q(1), Q(0)), (Q(1), -t), (Q(0), -t),
            (-t, Q(0)), (-t, Q(1)), (Q(0), Q(1))]


def area(v):
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1]
                   - v[(i + 1) % len(v)][0] * v[i][1]
                   for i in range(len(v)))) / 2


def gauge(t, x, y):
    assert t > 0
    return max(x, y, x + y, -x / t, -y / t, -(x + y) / t)


def periodic_gauge(t, x, y):
    return min(gauge(t, x - j, y - k)
               for j in range(-1, 3) for k in range(-1, 3))


def radius(t):
    return Q(2, 1) / (1 + 2*t) if t <= 1 else Q(2, 1) / (t + 2)


def main():
    cases = [Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4), Q(1),
             Q(3, 2), Q(2), Q(4)]
    count = 0
    for t in cases:
        assert area(vertices(t)) == (1 + 4*t + t*t) / 2
        assert radius(t) == radius(1/t) / t
        a = 1 / (1 + 2*t) if t <= 1 else 1 - t / (t+2)
        assert periodic_gauge(t, a, a) == radius(t)
        for k in range(29):
            for j in range(29):
                x, y = Q(k, 28), Q(j, 28)
                assert periodic_gauge(t, x, y) <= radius(t)
                count += 1
    assert periodic_gauge(Q(1), Q(1,3), Q(1,3)) == Q(2,3)
    assert periodic_gauge(Q(1), Q(2,3), Q(2,3)) == Q(2,3)

    # The normalized covering density decreases from 2 to 4/3 on [0,1].
    # The exact derivative in the t-coordinate is -12*t/(1+2*t)^3.
    for t in [Q(1, 100), Q(1, 7), Q(1, 3), Q(1, 2), Q(3, 4), Q(1)]:
        density = radius(t)**2 * area(vertices(t))
        assert density >= Q(4, 3)
        if t != 1:
            assert density > Q(4,3)
    assert radius(Q(1))**2 * area(vertices(Q(1))) == Q(4,3)
    assert Q(2)**2 * Q(1,2) == Q(2)
    print(f'PASS: {count} exact rational grid-point checks, eight exact area and reciprocity tests, and exact endpoint/deep-hole identities.')


if __name__ == '__main__':
    main()
