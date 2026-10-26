#!/usr/bin/env python3
"""Reproduce the critical-decay example in a two-population impulsive competition system.

Requires Python 3.9+; no third-party dependencies. Numerical checks supplement,
but do not replace, the mathematical proof in RESULT.md.
"""
import math

PERIOD = 1.0
BETA_Y = 0.5
PULSE_Y = 0.25
A = D = 1.0
B, C, E, F = 2.0, 1.0, 1.0, 1.0
Q = C / F
KAPPA = B - Q * E


def logistic(y, duration):
    z = math.exp(duration)
    return y * z / (1.0 + y * (z - 1.0))


def resident_origin():
    # Reciprocal logistic map over a period with a pulse at t=1/4:
    # u(1) = 1 + exp(-3/4) + 2 exp(-1) (u(0)-1).
    return 1.0 / (1.0 + math.exp(-0.75) / (1.0 - 2.0 / math.e))


def exact_predictions():
    y0 = resident_origin()
    before = logistic(y0, 0.25)
    after = BETA_Y * before
    middle_area = math.log(1 + after * (math.exp(0.5) - 1))
    total_area = 1.0 + math.log(BETA_Y)
    return y0, total_area, middle_area, y0 / (KAPPA * total_area), y0 / (KAPPA * (total_area + middle_area))


def f(state, multiplier):
    x, y, integral = state
    return (x * (A - B*x - C*y), y * (D - E*x - F*y), multiplier * (y**Q))


def rk4(state, dt, multiplier):
    k1 = f(state, multiplier)
    k2 = f(tuple(state[i] + dt*k1[i]/2 for i in range(3)), multiplier)
    k3 = f(tuple(state[i] + dt*k2[i]/2 for i in range(3)), multiplier)
    k4 = f(tuple(state[i] + dt*k3[i] for i in range(3)), multiplier)
    return tuple(state[i] + dt*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6 for i in range(3))


def simulate(x_pulse, periods=3000, mesh=200):
    state = (0.4, 0.29, 0.0)
    for k in range(1, periods + 1):
        segments = sorted(set((PULSE_Y, x_pulse, PERIOD)))
        start = 0.0
        # The normalized ratio multiplier Psi is piecewise constant here,
        # because the continuous growth-rate difference A-Q*D vanishes.
        multiplier = 1.0
        for end in segments:
            n = round((end - start)*mesh)
            assert n > 0 and abs(n/mesh - (end-start)) < 1e-14
            for _ in range(n):
                state = rk4(state, 1.0/mesh, multiplier)
            x, y, i = state
            if end == PULSE_Y:
                y *= BETA_Y
                multiplier *= BETA_Y ** (-Q)
            if end == x_pulse:
                x *= 0.5
                multiplier *= 0.5
            state = (x, y, i)
            start = end
        # Both pulse products cancel over each period on the critical line.
        assert abs(multiplier - 1.0) < 1e-14
        if k in (1, 10, 100, 1000, periods):
            x, y, i = state
            ratio = x/(y**Q)
            independent_formula = 1.0/(1.0/(0.4/(0.29**Q)) + KAPPA*i)
            assert abs(ratio - independent_formula) <= 1e-6*max(ratio, independent_formula)
    return periods*state[0], state[1], state[2]


def main():
    assert A*PERIOD+math.log(0.5) == D*PERIOD+math.log(0.5)
    assert KAPPA > 0
    y0, area, middle, coincident, staggered = exact_predictions()
    assert area > 0 and middle > 0
    assert staggered < coincident
    same, y_same, _ = simulate(0.25)
    late, y_late, _ = simulate(0.75)
    assert abs(y_same-y0) < 0.001 and abs(y_late-y0) < 0.001
    assert abs(same/coincident-1) < 0.01, (same, coincident)
    assert abs(late/staggered-1) < 0.01, (late, staggered)
    print('PASS: exact reciprocal-logistic resident map')
    print('PASS: exact normalized-ratio identity along numerical trajectories')
    print('PASS: critical 1/k law at 3000 periods (within 1% numerical error)')
    print('PASS: identical invasion threshold and distinct pulse-phase amplitudes')
    print('resident y*(0) = %.12f; total resident area = %.12f' % (y0,area))
    print('additional middle-interval area = %.12f' % middle)
    print('same-phase limit %.12f, numerical %.12f' % (coincident,same))
    print('staggered limit  %.12f, numerical %.12f' % (staggered,late))

if __name__ == '__main__':
    main()
