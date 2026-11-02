"""Exact-rational consistency tests for a three-edge Markov heat sweep.

Runs with the Python 3 standard library only. These checks supplement the proof
of the analytic monotonicity and spectral classification; finite tests alone do
not establish assertions for every parameter.
"""
from fractions import Fraction as F
from math import exp, log, sqrt


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def det(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def edge(i, j, r):
    a = [[F(int(i == j)) for j in range(3)] for i in range(3)]
    v = [F(0)] * 3
    v[i], v[j] = F(1), F(-1)
    for k in range(3):
        for l in range(3):
            a[k][l] -= (1-r)*v[k]*v[l]/2
    return a


def sweep(r):
    return mm(mm(edge(0, 1, r), edge(1, 2, r)), edge(2, 0, r))


def trace_other(r):
    return -(r+1)*(r*r-10*r+1)/8


def discriminant(r):
    return (1-r)**4*(r*r-14*r+1)/64


n = 0
for i in range(0, 24):
    r = F(i, 23)
    a = sweep(r)
    tr = sum(a[k][k] for k in range(3))-1
    assert all(sum(row) == 1 for row in a)
    assert all(sum(a[k][j] for k in range(3)) == 1 for j in range(3))
    assert det(a) == r**3
    assert tr == trace_other(r)
    assert tr*tr-4*r**3 == discriminant(r)
    assert a[0][1] - a[1][0] == -(1-r)**2*(1+r)/8
    if 0 < r < 1:
        assert all(x > 0 for row in a for x in row)
    n += 1

rcrit = 7-4*sqrt(3)
tcrit = log(2+sqrt(3))
assert abs(exp(-2*tcrit)-rcrit) < 2e-15
rate = (2-sqrt(3))**3
assert abs(rate-(26-15*sqrt(3))) < 3e-15

def rate_at(r):
    tr = float(trace_other(r))
    disc = float(discriminant(r))
    if disc < 0:
        return r**1.5
    return (abs(tr)+sqrt(max(0, disc)))/2

for r in [0.001, 0.01, 0.03, 0.05, 0.07, 0.08, 0.1, 0.2, 0.5, 0.8, 0.95]:
    assert rate_at(r) > rate-1e-13
assert abs(rate_at(rcrit)-rate) < 1e-8
assert abs(rate_at(0)-0.125) < 1e-12
print(f"VERIFY_OK rational_sweeps={n} phase_boundaries=3 rate_tests=11")
