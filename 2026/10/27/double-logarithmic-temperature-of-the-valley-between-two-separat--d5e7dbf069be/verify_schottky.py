"""Reproduce numerical diagnostics of the two-scale Schottky valley.

Only Python standard library is required. The analytic asymptotic proof is
in RESULT.md; finite checks do not certify limits at infinite gap ratio.
"""
import math


def f(y):
    return y * y / (4 * math.cosh(y / 2) ** 2)


def fp(y):
    return f(y) * (2 / y - math.tanh(y / 2))


def derivative(r, y):
    return fp(y / r) + r * fp(y)


def root(r):
    L = math.log(r)
    a, b = L, 3 * L
    assert derivative(r, a) < 0 < derivative(r, b)
    for _ in range(90):
        m = (a + b) / 2
        if derivative(r, m) > 0:
            b = m
        else:
            a = m
    return (a + b) / 2


def main():
    checks = 0
    prev_height = float('inf')
    for r in (30, 50, 100, 300, 1000, 3000, 10000):
        y = root(r)
        L = math.log(r)
        for diff, sign in ((-0.0001, -1), (+0.0001, 1)):
            assert sign * derivative(r, y + diff) > 0
            checks += 1
        asym = 2 * L + math.log(L) + math.log(4)
        assert abs(y - asym) < 0.2
        checks += 1
        height = f(y / r) + f(y)
        assert height < prev_height
        prev_height = height
        checks += 1
        assert 1 < height * r * r / (L * L) < 2.5
        checks += 1
        assert abs(derivative(r, y)) < 1e-10
        checks += 1
    print(f'PASS: {checks} finite diagnostic checks across 7 gap ratios.')


if __name__ == '__main__':
    main()
