"""Finite independent sanity tests of explicit dose-response identities.

This script does not prove the asymptotic or global existence statements.
Uses only the Python standard library.
"""
from math import exp, log


def cumulative(dose, horizon=3.0, initial_x=0.0, initial_y=2.0):
    """RK4 integrate y' = dose - (x0 exp(-t)+dose(1-exp(-t))) y."""
    n = max(12000, int(dose * horizon / 0.4) + 1)
    dt = horizon / n
    yy, area = initial_y, 0.0

    def rhs(tt, val):
        x = initial_x * exp(-tt) + dose * (1 - exp(-tt))
        return dose - x * val

    for j in range(n):
        t = j * dt
        k1 = rhs(t, yy)
        k2 = rhs(t + dt / 2, yy + dt * k1 / 2)
        k3 = rhs(t + dt / 2, yy + dt * k2 / 2)
        k4 = rhs(t + dt, yy + dt * k3)
        end = yy + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        area += dt * (yy + 2 * (yy + dt * k1 / 2) + 2 * (yy + dt * k2 / 2) + end) / 6
        yy = end
    return area


def main():
    t = 3.0
    p = t * t / 2
    q = p - t + 1 - exp(-t)
    slope = p - 2 * q
    assert 1.8 < p / q < 1.9
    assert abs(slope - (-0.5 + 2 * exp(-3))) < 1e-13
    assert slope < 0
    print("EXACT_INITIAL_SLOPE_AND_THRESHOLD_PASS", format(p/q, '.12f'), format(slope, '.12f'))

    c0 = cumulative(0)
    c1 = cumulative(1e-4)
    c2 = cumulative(1e-3)
    assert abs(c0 - 6) < 1e-9
    assert c1 < c0 and c2 < c1
    assert abs((c1 - c0) / 1e-4 - slope) < 0.001
    print("INDEPENDENT_INITIAL_DOSE_ODE_CHECK_PASS")

    # This finite calculation tests only large finite input, never the limit.
    vals = [cumulative(dose) for dose in (100.0, 1000.0, 10000.0)]
    assert vals[0] < vals[1] < vals[2]
    assert all(0.3 < v/log(d) < 1.5 for v, d in zip(vals, (100.0, 1000.0, 10000.0)))
    print("FINITE_HIGH_INPUT_TREND_PASS", *(format(v, '.9f') for v in vals))
    print("GLOBAL_NONMONOTONICITY_AND_LOGARITHMIC_LIMIT_REQUIRE_ANALYTICAL_PROOF")


if __name__ == "__main__":
    main()
