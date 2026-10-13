#!/usr/bin/env python3
"""Numerical diagnostic for the sharp balanced 2-by-2 overrelaxed Sinkhorn theorem.

The accompanying mathematical proof, rather than these finite tests, establishes the
infinite-time statements. All kernels here are strictly positive.
"""
from math import cosh, exp, isclose, log
from random import Random


def z(k, x, y):
    return sum(k[i][j] * exp(((1 if i == 0 else -1) * x + (1 if j == 0 else -1) * y) / 2)
               for i in (0, 1) for j in (0, 1))


def potential(k, x, y):
    return log(z(k, x, y))


def row_target(k, y):
    return log((k[1][0] * exp(y / 2) + k[1][1] * exp(-y / 2)) /
               (k[0][0] * exp(y / 2) + k[0][1] * exp(-y / 2)))


def col_target(k, x):
    return log((k[0][1] * exp(x / 2) + k[1][1] * exp(-x / 2)) /
               (k[0][0] * exp(x / 2) + k[1][0] * exp(-x / 2)))


def sweep(k, x, y, omega):
    new_x = (1 - omega) * x + omega * row_target(k, y)
    new_y = (1 - omega) * y + omega * col_target(k, new_x)
    return new_x, new_y


def check_close(left, right, atol=2e-11):
    assert isclose(left, right, rel_tol=1e-10, abs_tol=atol), (left, right)


def test():
    rng = Random(16471851)
    cases = 400
    checks = 0
    for _ in range(cases):
        k = [[exp(rng.uniform(-2, 2)) for _ in range(2)] for _ in range(2)]
        x, y = rng.uniform(-3, 3), rng.uniform(-3, 3)
        w = rng.uniform(0.25, 1.8)
        new_x, new_y = sweep(k, x, y, w)

        # Recover the same update from the four original positive vector factors.
        s, t = rng.uniform(-2, 2), rng.uniform(-2, 2)
        u = [exp(s + x / 2), exp(s - x / 2)]
        v = [exp(t + y / 2), exp(t - y / 2)]
        row = [sum(k[i][j] * v[j] for j in range(2)) for i in range(2)]
        un = [u[i] ** (1-w) * (0.5 / row[i]) ** w for i in range(2)]
        col = [sum(k[i][j] * un[i] for i in range(2)) for j in range(2)]
        vn = [v[j] ** (1-w) * (0.5 / col[j]) ** w for j in range(2)]
        check_close(new_x, log(un[0]/un[1]))
        check_close(new_y, log(vn[0]/vn[1]))
        checks += 2

        d = x - row_target(k, y)
        delta = log(cosh((1-w)*d/2)) - log(cosh(d/2))
        check_close(potential(k, new_x, y) - potential(k, x, y), delta)
        assert potential(k, new_x, new_y) < potential(k, x, y) + 1e-10
        checks += 2

        # The unreduced scale must satisfy its own exact affine recurrence.
        avg_old = s + t
        avg_new = log(un[0]*un[1]*vn[0]*vn[1])/2
        aa1 = k[0][0]*exp(y/2)+k[0][1]*exp(-y/2)
        aa2 = k[1][0]*exp(y/2)+k[1][1]*exp(-y/2)
        bb1 = k[0][0]*exp(new_x/2)+k[1][0]*exp(-new_x/2)
        bb2 = k[0][1]*exp(new_x/2)+k[1][1]*exp(-new_x/2)
        c = log(2) + log(aa1*aa2)/2
        e = log(2) + log(bb1*bb2)/2
        check_close(avg_new, (1-w)**2*avg_old - w*(1-w)*c - w*e)
        checks += 1

        px, py = sweep(k, x, y, 2)
        check_close(potential(k, px, py), potential(k, x, y))
        px, py = sweep(k, x, y, 2.4)
        assert potential(k, px, py) >= potential(k, x, y) - 2e-11
        checks += 2

        # Projective convergence and local Schur inequalities.
        xx, yy = x, y
        for step in range(2500):
            xx, yy = sweep(k, xx, yy, w)
        assert abs(xx-row_target(k, yy)) < 3e-7
        assert abs(yy-col_target(k, xx)) < 3e-7
        # At optimum, the 2x2 balanced plan has the simple correlation form.
        cross = (k[0][0]*k[1][1]/(k[0][1]*k[1][0]))**0.5
        rho = (cross-1)/(cross+1)
        h=1-w
        trace=2*h+w*w*rho*rho
        determinant=h*h
        assert 1-determinant > 0
        assert 1-trace+determinant > 0
        assert 1+trace+determinant > 0
        checks += 5
    print(f'PASS: {cases} positive kernels; {checks} diagnostic identities and inequalities; no external dependencies')

if __name__ == '__main__':
    test()
