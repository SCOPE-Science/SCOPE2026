#!/usr/bin/env python3
"""Polynomial/Beta and two-sided travelling-front checks.

Run: python verify_front.py. Requires NumPy and SciPy (see requirements.txt).
All computations use only the model and formulas specified in RESULT.md.
The collocation tests are finite numerical corroboration, not proofs.
"""
from fractions import Fraction
from math import sqrt, isclose
from scipy.integrate import solve_bvp
import numpy as np


def add(*ps):
    out = [Fraction(0)] * max(map(len, ps))
    for p in ps:
        for i, v in enumerate(p):
            out[i] += v
    return out


def times(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def scale(p, x):
    return [x * z for z in p]


def equal_poly(p, q):
    n = max(len(p), len(q))
    return p + [0] * (n-len(p)) == q + [0] * (n-len(q))


# Exact polynomial identity for E[q(U)(U-a)], U~Beta(1+2a,3-2a).
a = [Fraction(0), Fraction(1)]
p = [Fraction(1), Fraction(2)]
E1 = scale(p, Fraction(1, 4))
E2 = scale(times(p, add(p, [Fraction(1)])), Fraction(1, 20))
E3 = scale(times(times(p, add(p,[Fraction(1)])),add(p,[Fraction(2)])),Fraction(1,120))
computed = add(scale(E2, 2), scale(E3, -1), times(scale(a, -1), add(scale(E1,2),scale(E2,-1))))
expected = scale(times(p,[Fraction(9),Fraction(-17),Fraction(4)]),Fraction(1,60))
assert equal_poly(computed, expected), (computed, expected)
print('PASS: exact polynomial identity over rational coefficients')


def front_speed(allee, crowding, length=27.0):
    """Solve both tails with a midpoint phase and linearized Robin tail data."""
    z = np.linspace(0.0, length, 320)
    k = 1.0 / sqrt(2.0)
    upr = 1/(1+np.exp(k*z))
    upl = 1/(1+np.exp(-k*z))
    def diffusivity(u):
        return 1.0+crowding*u*(2.0-u)
    y0 = np.array((upr,-k*upr*(1-upr)*diffusivity(upr),
                   upl,-k*upl*(1-upl)*diffusivity(upl)))
    c0 = (1.0-2.0*allee)/sqrt(2.0)
    def ode(x, y, par):
        right,flux_right,left,flux_left=y
        c=par[0]
        return np.array((
            flux_right/diffusivity(right),
            -c*flux_right/diffusivity(right)-right*(1-right)*(right-allee),
            -flux_left/diffusivity(left),
            c*flux_left/diffusivity(left)+left*(1-left)*(left-allee)))
    def boundary(at0, atL, par):
        c=par[0]
        right,flux_right,left,flux_left=atL
        kright=(c+np.sqrt(c*c+4*allee))/2.0
        dleft=diffusivity(1.0)
        kleft=(-c+np.sqrt(c*c+4*dleft*(1-allee)))/(2*dleft)
        return np.array((at0[0]-.5,at0[2]-.5,at0[1]-at0[3],
                         flux_right+diffusivity(right)*kright*right,
                         flux_left+diffusivity(left)*kleft*(1-left)))
    solution=solve_bvp(ode,boundary,z,y0,p=[c0],tol=4e-9,max_nodes=5000)
    assert solution.status == 0, solution.message
    assert max(solution.rms_residuals) < 5e-9
    assert abs(solution.y[0,-1]) < 5e-7
    assert abs(1-solution.y[2,-1]) < 5e-7
    return float(solution.p[0])


# Numerical two-sided collocation test, separate from the adjoint evaluation.
for level in (0.20,0.50,0.80):
    epsilon=0.005
    plus=front_speed(level,epsilon)
    minus=front_speed(level,-epsilon)
    observed=(plus-minus)/(2*epsilon)
    pred=sqrt(2)*(2*level+1)*(4*level*level-17*level+9)/60
    assert abs(observed-pred) < 2.5e-5, (level,observed,pred)
    print(f'PASS: a={level:.2f}, symmetric BVP slope={observed:+.9f}, formula={pred:+.9f}')


# Balanced-area front must be stationary even at nonzero density-dependent motility.
for crowding in (-0.5,0.5):
    a_balance=(5+4*crowding)/(10+7*crowding)
    observed=front_speed(a_balance,crowding)
    assert abs(observed) < 2e-6, (crowding,a_balance,observed)
    print(f'PASS: Maxwell front b={crowding:+.2f}, a={a_balance:.9f}, c={observed:+.9g}')

threshold=(17-sqrt(145))/8
assert .5<threshold<.8
print(f'PASS: sharp response threshold a*={threshold:.12f}')
