#!/usr/bin/env python3
"""Reproduce stationary transport edge and reset-origin singularity diagnostics.

Requires numpy and scipy. Finite checks are not a proof of the limiting claims.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp


def evaluate(kind, amplitude, flip, reset):
    if kind == 'tan':
        g = np.tan
        edge = math.atan(amplitude)
        k_edge = 1 + amplitude * amplitude
    elif kind == 'tanh':
        g = np.tanh
        edge = math.atanh(amplitude)
        k_edge = 1 - amplitude * amplitude
    else:
        raise ValueError(kind)
    k_origin = 1.0
    a = flip + reset
    exponent = a / k_edge
    eps = 2e-6
    def rhs(v, y):
        u, w = y
        f = amplitude - g(v)
        b = amplitude + g(v)
        return [-a*u/f + flip*w/b, a*w/b - flip*u/f]
    init = eps ** exponent
    sol = solve_ivp(rhs, (edge-eps, 0.0),
                    [init, (flip/a)*init], method='DOP853',
                    rtol=4e-12, atol=1e-14, dense_output=True,
                    max_step=0.004)
    assert sol.success, sol.message
    u0,w0 = sol.sol(0.0)
    assert u0 > w0 > 0, (kind, amplitude, flip, reset, u0, w0)
    factor = (reset/2.0)/(u0-w0)
    def prob(v):
        u,w=sol.sol(v)*factor
        return u/(amplitude-g(v))+w/(amplitude+g(v))
    expected_slope = reset*(k_origin-2*flip-reset)/(2*amplitude**2)
    h=1e-4
    derivative=(-3*prob(0)+4*prob(h)-prob(2*h))/(2*h)
    # The finite difference has O(h^2) truncation. Its agreement probes the
    # stationary transport solution, independent of the symbolic derivation.
    assert abs(derivative-expected_slope) < 0.004 + 0.015*abs(expected_slope), (
        kind, flip, reset, derivative, expected_slope)
    # Logarithmic boundary power from two well-separated interior distances.
    ds = [0.009,0.004,0.0012]
    ds = [d*min(edge,1.0) for d in ds]
    vals = [prob(edge-d) for d in ds]
    log_slope=math.log(vals[-1]/vals[0])/math.log(ds[-1]/ds[0])
    assert abs(log_slope-(exponent-1)) < 0.065, (kind, log_slope, exponent-1)
    # Ratio of outward and inward positive probability currents at the edge.
    d=0.0005*min(edge,1.0)
    u,w=sol.sol(edge-d)
    assert abs(w/u-flip/a) < 0.025, (kind,w/u,flip/a)
    return (kind,amplitude,flip,reset,round(derivative,7),
            round(expected_slope,7),round(log_slope,5),
            round(exponent-1,5),round(w/u,6))


def main():
    cases=[('tan',3.0,.2,.3), ('tan',3.0,.9,.15),
           ('tan',3.0,4.0,2.0), ('tanh',.6,.15,.3),
           ('tanh',.6,.5,.3), ('tanh',.6,.6,.02), ('tanh',.4,1.2,.8)]
    for args in cases:
        print(evaluate(*args))
    print('PASS: 7 stationary origin/edge/inward-flux checks (21 comparisons)')

if __name__=='__main__':
    main()
