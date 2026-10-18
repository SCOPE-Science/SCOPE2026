"""Exact-rational checks for homogeneous higher-order SIS equilibria.

Run with Python 3.9+; no external packages are required.
The analytic proof for arbitrary interaction order is in RESULT.md.
"""
from fractions import Fraction as F


def multiply(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return c


def evaluate(a, x):
    result = F(0)
    for a_i in reversed(a):
        result = result * x + a_i
    return result


def witness(m):
    assert isinstance(m, int) and m >= 1
    roots = [F(j, m * (m + 1)) for j in range(1, m + 1)]
    assert sum(roots) == F(1, 2)
    R = [F(1)]
    for r in roots:
        R = multiply(R, [-r, F(1)])
    C = evaluate(R, F(1))
    assert C > 0

    # Divide (1 - R(y)/C) exactly by (1-y), with constant-first coefficients.
    numerator = [-a / C for a in R]
    numerator[0] += 1
    Q = [F(0)] * m
    Q[0] = numerator[0]
    for k in range(1, m):
        Q[k] = numerator[k] + Q[k - 1]
    assert numerator[m] == -Q[-1]
    assert all(b > 0 for b in Q)
    assert multiply([F(1), F(-1)], Q) == numerator

    # Confirm the entire polynomial identity coefficient by coefficient.
    field = multiply([F(0), F(1)], multiply([F(1), F(-1)], Q))
    field[1] -= 1
    expected = [-F(0)] + [-a / C for a in R]
    assert field == expected

    for j, r in enumerate(roots, 1):
        assert evaluate(field, r) == 0
        derivative = F(1)
        for k, other in enumerate(roots, 1):
            if j != k:
                derivative *= (r - other)
        derivative = -r * derivative / C
        assert derivative != 0
        assert (derivative < 0) == ((m - j) % 2 == 0)
    assert sum((m - j) % 2 == 0 for j in range(1, m + 1)) == (m + 1) // 2
    return roots, C, Q


for M in range(1, 19):
    witness(M)

roots, C, rates = witness(5)
assert roots == [F(1, 30), F(1, 15), F(1, 10), F(2, 15), F(1, 6)]
assert C == F(2639, 4500)
assert rates == [F(118756, 118755), F(5275, 5278), F(2675, 2639),
                 F(2250, 2639), F(4500, 2639)]
assert rates[0] > 1
print('VERIFY_OK: exact polynomial identities and hyperbolic stability, M=1,...,18')
print('M=5 roots:', ', '.join(str(x) for x in roots))
print('M=5 positive rates:', ', '.join(str(x) for x in rates))
print('M=5 stable endemic fractions: 1/30, 1/10, 1/6')
