#!/usr/bin/env python3
"""Verification for exact contraction and Floquet identities in the trigonometric Nosé-Hoover flow."""

import numpy as np
import scipy
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def symbolic_checks():
    a, b, y, z = sp.symbols("a b y z", nonzero=True, real=True)
    zdot = b * (1 - 2 * sp.cos(y))
    div_v = -a * sp.cos(y) * sp.sin(z)
    dcosz_dt = -sp.sin(z) * zdot
    rhs = -sp.Rational(1, 2) * a * sp.sin(z) - a * dcosz_dt / (2 * b)
    contraction_residual = sp.simplify(div_v - rhs)

    theta = sp.symbols("theta", real=True)
    P = a * sp.sin(theta)
    # theta_dot = -b, hence P_dot = -a*b*cos(theta).
    Pdot = -a * b * sp.cos(theta)
    q_from_liouville = sp.expand_trig(sp.simplify(1 - Pdot / 2 - P**2 / 4))
    q_expected = 1 + a * b * sp.cos(theta) / 2 - a**2 * sp.sin(theta) ** 2 / 4
    hill_residual = sp.simplify(q_from_liouville - q_expected)

    assert contraction_residual == 0
    assert hill_residual == 0
    return contraction_residual, hill_residual


def monodromy_direct(a, b=0.5, z0=0.0, rtol=1e-12, atol=1e-14):
    T = 2 * np.pi / abs(b)

    def rhs(t, u):
        M = u.reshape(2, 2)
        theta = z0 - b * t
        A = np.array([[0.0, 1.0], [-1.0, -a * np.sin(theta)]])
        return (A @ M).ravel()

    sol = solve_ivp(
        rhs,
        (0.0, T),
        np.eye(2).ravel(),
        method="DOP853",
        rtol=rtol,
        atol=atol,
        max_step=T / 400,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1].reshape(2, 2)


def monodromy_hill(a, b=0.5, z0=0.0, rtol=1e-12, atol=1e-14):
    T = 2 * np.pi / abs(b)

    def rhs(t, u):
        M = u.reshape(2, 2)
        theta = z0 - b * t
        q = 1 + (a * b / 2) * np.cos(theta) - (a * a / 4) * np.sin(theta) ** 2
        A = np.array([[0.0, 1.0], [-q, 0.0]])
        return (A @ M).ravel()

    sol = solve_ivp(
        rhs,
        (0.0, T),
        np.eye(2).ravel(),
        method="DOP853",
        rtol=rtol,
        atol=atol,
        max_step=T / 400,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1].reshape(2, 2)


def finite_time_identity(a=2.0, b=0.5, T=100.0):
    # Integrate the flow plus the two observables entering the exact identity.
    u0 = np.array([1e-3, 1e-3, 0.0, 0.0, 0.0])

    def rhs(t, u):
        x, y, z, int_sinz, int_div = u
        sx, sy, sz = np.sin(x), np.sin(y), np.sin(z)
        cy = np.cos(y)
        return np.array([
            sy,
            -sx - a * sy * sz,
            b * (1 - 2 * cy),
            sz,
            -a * cy * sz,
        ])

    sol = solve_ivp(
        rhs,
        (0.0, T),
        u0,
        method="DOP853",
        rtol=1e-11,
        atol=1e-13,
        max_step=0.05,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    xT, yT, zT, int_sinz, int_div = sol.y[:, -1]
    predicted = -a * int_sinz / 2 - a * (np.cos(zT) - np.cos(u0[2])) / (2 * b)
    return int_div, predicted, int_div - predicted


def main():
    cres, hres = symbolic_checks()
    print(f"numpy={np.__version__}")
    print(f"scipy={scipy.__version__}")
    print(f"sympy={sp.__version__}")
    print(f"symbolic_contraction_residual={cres}")
    print(f"symbolic_hill_residual={hres}")

    b = 0.5
    root = brentq(lambda aa: np.trace(monodromy_direct(aa, b=b)) + 2.0, 1.58, 1.60, xtol=1e-13)
    Md = monodromy_direct(root, b=b)
    Mh = monodromy_hill(root, b=b)
    print(f"b={b:.16g}")
    print(f"first_trace_minus_two_root={root:.15f}")
    print(f"direct_trace={np.trace(Md):.15e}")
    print(f"direct_det={np.linalg.det(Md):.15e}")
    print(f"hill_trace={np.trace(Mh):.15e}")
    print(f"hill_det={np.linalg.det(Mh):.15e}")
    print("direct_monodromy=")
    print(Md)

    phases = [0.0, 0.3, 1.1]
    phase_traces = [np.trace(monodromy_direct(root, b=b, z0=z0)) for z0 in phases]
    print("phase_shift_traces=" + ",".join(f"{v:.15e}" for v in phase_traces))

    M_left = monodromy_direct(1.58, b=b)
    M_right = monodromy_direct(1.60, b=b)
    print(f"trace_at_1.58={np.trace(M_left):.15e}")
    print(f"trace_at_1.60={np.trace(M_right):.15e}")

    int_div, predicted, residual = finite_time_identity()
    print(f"finite_time_divergence_integral={int_div:.15e}")
    print(f"finite_time_predicted_integral={predicted:.15e}")
    print(f"finite_time_identity_residual={residual:.15e}")

    assert abs(np.linalg.det(Md) - 1.0) < 1e-10
    assert abs(np.trace(Md) + 2.0) < 1e-10
    assert abs(np.trace(Md) - np.trace(Mh)) < 1e-10
    assert max(abs(v + 2.0) for v in phase_traces) < 1e-9
    assert np.trace(M_left) > -2.0 and np.trace(M_right) < -2.0
    assert abs(residual) < 1e-9
    print("all_checks_passed=True")


if __name__ == "__main__":
    main()
