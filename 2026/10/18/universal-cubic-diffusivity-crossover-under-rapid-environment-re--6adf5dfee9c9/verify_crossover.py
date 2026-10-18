#!/usr/bin/env python3
"""Exact symbolic certificate for the high-refresh diffusivity crossover.

Requirements: Python 3 and SymPy. Run: python verify_crossover.py
This program checks all 2^m path histories for 1 <= m <= 4, derives
annealed static-walk moments from independent site probabilities, and
reconstructs the first four Taylor coefficients of the regenerative
speed and diffusivity. Analytic convergence and uniform error bounds
are proved separately in RESULT.md.
"""
from itertools import product
import sympy as sp

a, b, r, d, v = sp.symbols('a b r d v')


def departure_moment(right, left):
    """E[omega**right*(1-omega)**left] for <=2 departures."""
    assert right >= 0 and left >= 0 and right + left <= 2
    return {
        (0, 0): sp.Integer(1),
        (1, 0): a,
        (0, 1): 1-a,
        (2, 0): b,
        (1, 1): a-b,
        (0, 2): 1-2*a+b,
    }[(right, left)]


def path_moments(m):
    E = sp.Integer(0)
    E2 = sp.Integer(0)
    mass = sp.Integer(0)
    paths = 0
    for steps in product((-1, 1), repeat=m):
        x = 0
        departures = {}
        for step in steps:
            right, left = departures.get(x, (0, 0))
            departures[x] = (right + (step == 1), left + (step == -1))
            x += step
        path_probability = sp.prod(departure_moment(*counts) for counts in departures.values())
        mass += path_probability
        E += x * path_probability
        E2 += x*x * path_probability
        paths += 1
    assert paths == 2**m
    assert sp.expand(mass-1) == 0
    return sp.expand(E), sp.expand(E2)


means, seconds = {}, {}
for m in range(1, 5):
    means[m], seconds[m] = path_moments(m)

expected_means = {
    1: d,
    2: 2*d,
    3: d*(3-2*v),
    4: 4*d*(1-v),
}
expected_seconds = {
    1: sp.Integer(1),
    2: 2*(1+d*d),
    3: 3*(1+2*d*d),
    4: 4*(1+3*d*d-2*d*d*v-2*v*v),
}


def to_d_v(expr):
    return sp.factor(expr.subs(b, v+a*a).subs(a, (1+d)/2))


checked = 0
for m in range(1, 5):
    assert sp.simplify(to_d_v(means[m])-expected_means[m]) == 0
    assert sp.simplify(to_d_v(seconds[m])-expected_seconds[m]) == 0
    checked += 2

# The regenerative mean speed and CLT diffusivity are
# (1-r)^2 sum_{m>=1} r^(m-1) E[Z_m] and
# (1-r)^2 sum_{m>=1} r^(m-1) E[(Z_m-m*speed)^2], respectively.
# Only m<=4 influence coefficients of degrees <=3.
speed = sp.series((1-r)**2 * sum(means[m]*r**(m-1) for m in range(1,5)), r, 0, 4).removeO()
speed = sp.Poly(sp.expand(speed), r)
assert [sp.simplify(to_d_v(speed.nth(i))-z)==0 for i,z in enumerate([d,0,-2*d*v,0])].count(True) == 4
checked += 4

A = sum(
    (seconds[m] - 2*m*speed.as_expr()*means[m] + m*m*speed.as_expr()**2) * r**(m-1)
    for m in range(1,5)
)
diffusion = sp.Poly(sp.series((1-r)**2*A, r, 0, 4).removeO(), r)
expected_diffusion = [1-d*d, 0, 12*d*d*v, -8*v*v]
for i in range(4):
    assert sp.simplify(to_d_v(diffusion.nth(i))-expected_diffusion[i]) == 0
    checked += 1

# Verify the leading sharp crossover coefficient for triangular laws.
kappa = sp.symbols('kappa', real=True)
assert sp.simplify((12*d*d*v*r*r-8*v*v*r**3).subs(d,kappa*sp.sqrt(r))/r**3 - 4*v*(3*kappa**2-2*v)) == 0
checked += 1

print(f'PASS: {checked} exact symbolic identities, {2+4+8+16} enumerated directed histories')
print('diffusivity high-refresh coefficients:', [str(z) for z in expected_diffusion])
