#!/usr/bin/env python3
"""Independent finite response checks for the polynomial spectral construction.

Only standard-library modules are needed. This script is corroborative, not a
substitute for the infinite-dimensional resolvent proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import cos, pi, sin


def multiply(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def det3(a):
    return (a[0][0] * (a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1] * (a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2] * (a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def characteristic3(a):
    tr = sum(a[j][j] for j in range(3))
    two = sum(a[i][i]*a[j][j]-a[i][j]*a[j][i]
              for i, j in ((0, 1), (0, 2), (1, 2)))
    return [Q(1), -tr, two, -det3(a)]


def do_case(coefficients):
    assert len(coefficients) == 3
    matrix = [[Q(0) for _ in range(3)] for _ in range(3)]
    for j, c in enumerate(coefficients):
        matrix[j][0] = -c
    for k in range(1, 3):
        matrix[k-1][k] = Q(1)
    assert characteristic3(matrix) == [Q(1)] + coefficients

    # Numerical derivative of the exact pushforward integral, computed
    # independently of the transfer-operator formula or companion matrix.
    n = 8192
    epsilon = 2e-6
    total_error = 0.0
    for k in range(3):
        obs_accumulators = [0.0, 0.0, 0.0]
        for i in range(n):
            y = i / n
            ek = 2.0 * cos(2*pi*(2**k)*y)
            coupling_m = epsilon if k == 0 else 0.0
            force = sum(float(c)/(pi*2**j)*sin(2*pi*(2**(j+1))*y)
                        for j, c in enumerate(coefficients))
            fp = 2*y + coupling_m*force
            fm = 2*y - coupling_m*force
            for l in range(3):
                positive = 2*cos(2*pi*(2**l)*fp)
                negative = 2*cos(2*pi*(2**l)*fm)
                # Basis test has L2 norm squared 2.
                obs_accumulators[l] += (
                    positive*(1+epsilon*ek)-negative*(1-epsilon*ek)
                ) / (4*epsilon*n)
        for l in range(3):
            error = abs(obs_accumulators[l] - float(matrix[l][k]))
            total_error = max(error, total_error)
            assert error < 1e-6, (k, l, error)
    return total_error


# The first characteristic polynomial has three real roots.
p1 = multiply(multiply([-Q(6, 5), Q(1)], [Q(4, 5), Q(1)]),
              [-Q(3, 4), Q(1)])
# The second has one real root and a conjugate imaginary pair.
p2 = multiply([-Q(6, 5), Q(1)], [Q(9, 16), Q(0), Q(1)])
assert p1[-1] == p2[-1] == 1
errors = [do_case(list(reversed(p[:-1]))) for p in (p1, p2)]
print('VERIFY_OK polynomials=2 derivative_entries=18 nodes_per_integral=8192')
print('MAX_ENTRY_ERROR', max(errors))
