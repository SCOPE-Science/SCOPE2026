#!/usr/bin/env python3
"""Deterministic numerical checks for the normal-operator degree-two minimax theorem."""
import math
import platform
import numpy as np
from scipy.optimize import minimize

SEED = 20260921
rng = np.random.default_rng(SEED)

def p(z, b, c):
    return 1.0 - b*z + c*z*z

def boundary(d, n=20001):
    th = np.linspace(-math.acos(d), math.acos(d), n)
    arc = np.exp(1j*th)
    y = np.linspace(-math.sqrt(max(0.0, 1.0-d*d)), math.sqrt(max(0.0, 1.0-d*d)), n)
    chord = d + 1j*y
    return np.concatenate([arc, chord])

def hard_matrix(d):
    s = math.sqrt(max(0.0, 1.0-d*d))
    return np.array([[d, 0.0, 0.0], [0.0, d, -s], [0.0, s, d]])

print("python", platform.python_version())
print("numpy", np.__version__)
import scipy
print("scipy", scipy.__version__)
print("seed", SEED)

max_main_error = 0.0
max_same_error = 0.0
min_random_margin = float("inf")
for d in [0.02, 0.1, 0.25, 0.5, 0.8, 0.95, 0.999]:
    z = boundary(d)
    q = 1.0-d
    bstar, cstar = 1.0+d, 1.0
    observed = float(np.max(np.abs(p(z, bstar, cstar))))
    max_main_error = max(max_main_error, abs(observed-q))

    # Fixed 3x3 real-normal witness containing d and d +/- i sqrt(1-d^2).
    A = hard_matrix(d)
    P = np.eye(3) - bstar*A + cstar*(A@A)
    opnorm = float(np.linalg.norm(P, 2))
    max_main_error = max(max_main_error, abs(opnorm-q))

    # Convex lower certificate at the two active spectral locations.
    z0 = complex(d, 0.0)
    z1 = complex(d, math.sqrt(max(0.0, 1.0-d*d)))
    for _ in range(20000):
        b = rng.uniform(-4.0, 5.0)
        c = rng.uniform(-4.0, 5.0)
        witness = max(abs(p(z0,b,c)), abs(p(z1,b,c)))
        min_random_margin = min(min_random_margin, witness-q)
        if witness < q - 5e-13:
            raise AssertionError((d,b,c,witness,q))

    # Numerical minimization of the sampled boundary sup norm.
    def objective(x):
        return float(np.max(np.abs(p(z, x[0], x[1]))))
    res = minimize(objective, np.array([bstar, cstar]), method="Nelder-Mead",
                   options={"maxiter": 3000, "xatol": 1e-11, "fatol": 1e-11})
    if res.fun < q - 5e-7:
        raise AssertionError(("sample optimizer below theorem", d, res.fun, q))

    # Standard same-step extragradient benchmark.
    t = 1.0/(1.0+d)
    qsame = (1.0+d+d*d)/(1.0+d)**2
    same_observed = float(np.max(np.abs(p(z, t, t*t))))
    max_same_error = max(max_same_error, abs(same_observed-qsame))

    # Direct endpoint minimax scan over nonnegative common steps.
    grid = np.linspace(0.0, 2.0, 200001)
    vals = np.maximum(np.abs(1-grid*d+(grid*d)**2), np.abs(1-grid+grid**2))
    grid_min = float(vals.min())
    if abs(grid_min-qsame) > 2e-5:
        raise AssertionError(("same-step grid", d, grid_min, qsame))

    print(f"d={d:.3f} main={observed:.15g} target={q:.15g} "
          f"hard3x3={opnorm:.15g} same={same_observed:.15g} same_target={qsame:.15g} "
          f"sample_min={res.fun:.15g}")

print("max_main_abs_error", f"{max_main_error:.3e}")
print("max_same_abs_error", f"{max_same_error:.3e}")
print("min_random_lower_certificate_margin", f"{min_random_margin:.3e}")
print("status PASS")
