"""Independent algebraic and numerical checks for the balanced collective-risk game.

Requirements: Python 3 with sympy, numpy, scipy. This file supplements, but does not
replace, the analytic proof in RESULT.md.
"""
from math import comb
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp, quad


def symbolic_checks():
    x, r, k, c, eps, a = sp.symbols("x r k c eps a", positive=True)
    s = x * (1 - x)
    lam = a * c / eps
    qlam = ((1 - r) / r) ** lam
    X = s * (k * s**a * r - c) / eps
    R = r * (1 - r) * (1 - 2*x)
    Hx = -a * qlam * (1 - 2*x) / s**(a + 1)
    Hr = a * qlam * (k*s**a*r-c) / (eps*s**a*r*(1-r))
    assert sp.simplify(Hx*X + Hr*R) == 0
    assert sp.simplify(sp.diff(Hx, r) - sp.diff(Hr, x)) == 0
    # Hessian of the first integral at E, expressed without evaluating an integral.
    rstar = c * 4**a / k
    Hxx = sp.simplify(sp.diff(Hx, x).subs({x: sp.Rational(1, 2), r:rstar}))
    Hrr = sp.simplify(sp.diff(Hr, r).subs({x: sp.Rational(1, 2), r:rstar}))
    Hxr = sp.simplify(sp.diff(Hx, r).subs({x: sp.Rational(1, 2), r:rstar}))
    assert sp.simplify(Hxx - 2*a * 4**(a+1) * ((1-rstar)/rstar)**lam)==0
    assert sp.simplify(Hrr - a*c*4**a*((1-rstar)/rstar)**lam/(eps*(1-rstar)*rstar**2))==0
    assert Hxr == 0
    return "Symbolic conservation and Hessian: passed"


def periodic_numerical_check(a):
    k = comb(2*a, a)
    b, c, eps = 1.0, 0.1, 0.1
    risk_equilibrium = 4**a*c/(k*b)
    assert 0 < risk_equilibrium < 1
    x_initial = 0.505

    def field(t, z):
        x, r = z
        return (x*(1-x)*(k*b*(x*(1-x))**a*r-c)/eps,
                r*(1-r)*(1-2*x))

    def crossing(t, z):
        return z[0]-x_initial
    crossing.direction = -1
    crossing.terminal = False

    solution = solve_ivp(field, (0, 30), (x_initial, risk_equilibrium),
                         events=crossing, rtol=2e-12, atol=1e-14,
                         max_step=0.025, dense_output=True)
    assert solution.success and len(solution.t_events[0]) >= 3
    period = solution.t_events[0][1]  # First full downward-crossing return.
    assert period > 0 and abs(solution.sol(period)[1]-risk_equilibrium) < 1e-8

    def average(function):
        return quad(lambda t: function(*solution.sol(t)), 0, period,
                    epsabs=2e-12, epsrel=2e-12)[0] / period

    mean_x = average(lambda x, r: x)
    mean_r = average(lambda x, r: r)
    mean_inverse_gain = average(lambda x, r: 1/(k*b*(x*(1-x))**a))
    variance = average(lambda x, r: (x-0.5)**2)
    assert abs(mean_x-0.5)<2e-9
    assert abs(mean_r-c*mean_inverse_gain)<2e-9
    assert mean_r > risk_equilibrium*(1+4*a*variance)
    return (f"a={a}, full physical period {period:.8f}, "
            f"mean risk {mean_r:.10f}, equilibrium risk {risk_equilibrium:.10f}, "
            f"variance {variance:.10f}: passed")


if __name__ == "__main__":
    print(symbolic_checks())
    for a in (1, 2, 3):
        print(periodic_numerical_check(a))
    print("All supplementary checks passed.")
