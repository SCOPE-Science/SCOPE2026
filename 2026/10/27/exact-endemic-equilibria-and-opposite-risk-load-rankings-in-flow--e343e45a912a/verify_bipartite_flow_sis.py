"""Reproduce equilibrium tests for the load-coupled SIS system on bicliques.

Run with Python 3 (standard library only). All exact cases use rational arithmetic.
"""

from fractions import Fraction
from math import sqrt


def analytic(m, n, recovery, mass, root):
    """Return infections and rates for a supercritical equilibrium."""
    z = (mass * root(m * n) / recovery - m - n) / (
        m * root(m) + n * root(n)
    )
    assert z > 0
    xl = z * root(n) / (1 + z * root(n))
    xr = z * root(m) / (1 + z * root(m))
    bl = recovery * (1 + z * root(m)) / root(m * n)
    br = recovery * (1 + z * root(n)) / root(m * n)
    return [xl] * m + [xr] * n, [bl] * m + [br] * n


def original_system_rhs(m, n, recovery, infection, load):
    """Direct full vertex-by-vertex implementation, with no class reduction."""
    count = m + n
    dx, db = [0] * count, [0] * count
    for i in range(count):
        for j in range(count):
            if (i < m) == (j < m):
                continue
            dx[i] += load[i] * (1 - infection[i]) * infection[j]
            db[i] -= load[i] * (1 - infection[j])
            db[i] += load[j] * (1 - infection[i])
        dx[i] -= recovery * infection[i]
    return dx, db


def exact_tests():
    total = 0
    for m in (1, 4, 9, 16):
        for n in (1, 4, 9, 16):
            sq = lambda v: Fraction(__import__('math').isqrt(v))
            for gamma in (Fraction(1), Fraction(2, 3)):
                critical = gamma * Fraction(m + n, sq(m * n))
                for multiplier in (Fraction(1001, 1000), Fraction(5, 4),
                                   Fraction(2), Fraction(13, 2)):
                    B = critical * multiplier
                    x, beta = analytic(m, n, gamma, B, sq)
                    dx, db = original_system_rhs(m, n, gamma, x, beta)
                    assert all(v == 0 for v in dx + db)
                    assert sum(beta) == B
                    assert all(Fraction(0) < t < Fraction(1) for t in x)
                    assert all(t > 0 for t in beta)
                    if m < n:
                        assert x[0] > x[-1] and beta[0] < beta[-1]
                    elif m > n:
                        assert x[0] < x[-1] and beta[0] > beta[-1]
                    else:
                        assert x[0] == x[-1] and beta[0] == beta[-1]
                    total += 1
    return total


def floating_tests():
    total, maxres = 0, 0.
    for m in range(1, 10):
        for n in range(1, 10):
            for gamma in (0.3, 1., 1.7):
                critical = gamma * (m + n) / sqrt(m * n)
                for multiplier in (1.000001, 1.05, 1.75, 12.):
                    B = critical * multiplier
                    x, beta = analytic(m, n, gamma, B, sqrt)
                    dx, db = original_system_rhs(m, n, gamma, x, beta)
                    residual = max(abs(q) for q in dx + db)
                    maxres = max(maxres, residual)
                    assert residual < 5.e-12, (m, n, gamma, B, residual)
                    assert abs(sum(beta) - B) < 1.e-12
                    total += 1
    return total, maxres


def zero_tests():
    total = 0
    for m in range(1, 12):
        for n in range(1, 12):
            for scale in (.1, 1., 1.9):
                gamma = 1.2
                B = scale * gamma * (m + n) / sqrt(m*n)
                v = B/(m+n)
                x = [0.] * (m+n)
                beta = [v] * (m+n)
                dx, db = original_system_rhs(m, n, gamma, x, beta)
                assert all(q == 0 for q in dx+db)
                total += 1
    return total


if __name__ == '__main__':
    a = exact_tests()
    b, err = floating_tests()
    c = zero_tests()
    print('Exact supercritical cases:', a)
    print('Floating supercritical cases:', b, '; max residual:', format(err, '.4g'))
    print('Disease-free cases:', c)
    print('All direct full-state residual tests passed.')
