#!/usr/bin/env python3
"""Exact finite-generator checks for a three-site resetting exclusion process.

Dependency: sympy; run with `python check.py`.
"""
import itertools
import sympy as sp


def generator(length, injection, extraction, reset):
    configurations = list(itertools.product((0, 1), repeat=length))
    positions = {v: i for i, v in enumerate(configurations)}
    G = sp.zeros(len(configurations))
    for i, state in enumerate(configurations):
        events = []
        if not state[0]:
            new = list(state)
            new[0] = 1
            events.append((tuple(new), injection))
        if state[-1]:
            new = list(state)
            new[-1] = 0
            events.append((tuple(new), extraction))
        for k in range(length - 1):
            if state[k] and not state[k + 1]:
                new = list(state)
                new[k], new[k + 1] = 0, 1
                events.append((tuple(new), sp.Integer(1)))
        if not state[0]:
            for k in range(1, length):
                if state[k]:
                    new = list(state)
                    new[k], new[0] = 0, 1
                    events.append((tuple(new), reset))
        for target, rate in events:
            j = positions[target]
            G[i, j] += rate
            G[i, i] -= rate
    return configurations, G


def assert_zero(expr, label):
    if sp.cancel(expr) != 0:
        raise AssertionError(f"{label}: {sp.factor(expr)}")

r = sp.symbols('r', nonnegative=True)
A, B = sp.symbols('A B', positive=True)
checks = 0

# General two-site exact probability and covariance laws.
states2, G2 = generator(2, A, B, r)
T = B / A + A / B + A + B + r + 1
p2 = sp.Matrix([B / A, 1, A + B + r, A / B]) / T
for i, residual in enumerate(G2.T * p2):
    assert_zero(residual, f'two-site stationarity {i}')
    checks += 1
assert_zero(sum(p2) - 1, 'two-site normalization'); checks += 1
m1 = sum(z * u[0] for z, u in zip(p2, states2))
m2 = sum(z * u[1] for z, u in zip(p2, states2))
m12 = sum(z * u[0] * u[1] for z, u in zip(p2, states2))
assert_zero(m12 - m1 * m2 - (1 - A - B - r) / T**2, 'two-site covariance')
checks += 1

# Three-site exact stationary solution at injection=1, extraction=1/10.
states3, G3 = generator(3, sp.Integer(1), sp.Rational(1, 10), r)
D = 200*r**3 + 4230*r**2 + 21471*r + 28455
numerators = [
    20*r + 21,
    10*(20*r + 21),
    (10*r + 11)*(20*r + 21),
    100*(10*r + 21),
    200*r**3 + 830*r**2 + 991*r + 252,
    10*(10*r + 21)*(20*r + 11),
    1200*r**2 + 3530*r + 2331,
    1000*(10*r + 21),
]
p3 = sp.Matrix(numerators) / D
for i, residual in enumerate(G3.T * p3):
    assert_zero(residual, f'three-site stationarity {i}')
    checks += 1
assert_zero(sum(p3) - 1, 'three-site normalization'); checks += 1
mean2 = sum(z * u[1] for z, u in zip(p3, states3))
mean3 = sum(z * u[2] for z, u in zip(p3, states3))
mean23 = sum(z * u[1] * u[2] for z, u in zip(p3, states3))
assert_zero(mean2 - 2*(700*r**2 + 7480*r + 12831)/D, 'site-two mean'); checks += 1
assert_zero(mean3 - 20*(100*r**2 + 825*r + 1281)/D, 'site-three mean'); checks += 1
assert_zero(mean23 - 1100*(10*r + 21)/D, 'joint moment'); checks += 1
Q = 30000*r**4 + 93500*r**3 + 6900*r**2 - 114345*r + 7497
covariance = -20*Q/D**2
assert_zero(mean23 - mean2*mean3 - covariance, 'stationary covariance polynomial')
checks += 1

for rr, sign in [(sp.Integer(0), -1), (sp.Rational(1,4), 1), (sp.Integer(1), -1)]:
    val = sp.factor(covariance.subs(r, rr))
    assert sign*val > 0, f'wrong covariance sign at rate {rr}'
    checks += 1

assert sp.Poly(Q, r).all_coeffs() == [30000, 93500, 6900, -114345, 7497]
checks += 1
positive = sorted(float(sp.re(z)) for z in sp.nroots(Q, maxsteps=500) if abs(float(sp.im(z))) < 1.e-10 and float(sp.re(z)) > 0)
assert len(positive) == 2 and 0 < positive[0] < .25 < positive[1] < 1
checks += 1
print(f'PASS: {checks} exact stationary, polynomial, and sign assertions')
print('two-site covariance = (1 - injection - extraction - reset) / T^2')
print('three-site covariance = -20*Q(r)/D(r)^2')
print('two positive threshold roots:', ', '.join(f'{x:.15f}' for x in positive))
for rr in (sp.Integer(0), sp.Rational(1,4), sp.Integer(1)):
    print(f'r={rr}: covariance={sp.factor(covariance.subs(r,rr))}')
print('Descartes upper bound: two positive roots counted with multiplicities.')
print('Sign alternation: two distinct positive roots, both simple; no others.')
