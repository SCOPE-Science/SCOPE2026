#!/usr/bin/env python3
"""Verify scalar algebra underlying the Chialvo zero-input recurrence identity."""
import math
import sympy as sp


def main():
    x, y, t, b, c = sp.symbols("x y t b c", positive=True, real=True)
    q = t + b
    xs = t / q
    cs = t * (1 + sp.log(q / t))
    xp = x**2 * sp.exp(y - x)
    yp = (1 - t) * y - b * x + c
    # x>0 allows log(xp)=2 log(x)+y-x, avoiding branch ambiguity.
    delta_v = (2 * sp.log(x) + y - x + yp / t) - (sp.log(x) + y / t)
    phi = x / xs - 1 - sp.log(x / xs)
    residual = sp.simplify(sp.expand_log(delta_v - ((c - cs) / t - phi), force=True))
    assert residual == 0, residual
    profile = q * x - t * sp.log(x)
    assert sp.simplify(sp.diff(profile, x).subs(x, xs)) == 0
    assert sp.simplify(sp.diff(profile, x, 2) - t / x**2) == 0
    assert sp.simplify(profile.subs(x, xs) - cs) == 0
    for a_value, b_value in [(0.89, 0.6), (0.89, 0.18), (0.5, 0.3)]:
        tv = 1 - a_value
        xstar = tv / (tv + b_value)
        cstar = tv * (1 + math.log((tv + b_value) / tv))
        for xv, yv in [(0.13, 0.9), (xstar, xstar - math.log(xstar)), (1.1, 2.3)]:
            for cv in [cstar - 0.01, cstar, cstar + 0.3]:
                xpval = xv**2 * math.exp(yv - xv)
                ypval = a_value * yv - b_value * xv + cv
                lhs = (math.log(xpval) + ypval / tv) - (math.log(xv) + yv / tv)
                u = xv / xstar
                rhs = (cv - cstar) / tv - (u - 1 - math.log(u))
                assert abs(lhs - rhs) < 1e-10, (lhs, rhs)
    for eta in [0.01, 0.15, 0.5, 0.9]:
        phi_left = -eta - math.log(1 - eta)
        phi_right = eta - math.log(1 + eta)
        assert phi_left > phi_right > 0
    print("Chialvo symbolic identity and scalar checks: PASS")


if __name__ == "__main__":
    main()
