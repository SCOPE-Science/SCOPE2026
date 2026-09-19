"""Numerical checks for harmonic Schur-stability formulas of LC-UBU variants.

The variables are z = gamma*h and s = alpha*kappa*h**2 for one quadratic mode.
This script uses only NumPy and deterministic pseudo-random test points.
"""
import math
import numpy as np


def exact_matrix(z, s):
    q = math.exp(-z / 2.0)
    A = (1.0 - q) / z
    B = (1.0 - q*q) / z
    return np.array([
        [1.0 - s*A, B - s*A*A],
        [-s*q, q*q - s*q*A],
    ])


def taylor_matrix(z, s):
    A = (4.0 - z) / 8.0
    B = 1.0 - z / 2.0
    P = 1.0 - z + z*z / 2.0
    C = 1.0 - z / 2.0
    return np.array([
        [1.0 - s/2.0, B - (s/2.0)*A],
        [-s*C, P - s*C*A],
    ])


def pade_matrix(z, s):
    A = 2.0 / (4.0 + z)
    B = 2.0 / (2.0 + z)
    P = (2.0 - z) / (2.0 + z)
    C = 2.0 / (2.0 + z)
    return np.array([
        [1.0 - s/2.0, B - (s/2.0)*A],
        [-s*C, P - s*C*A],
    ])


def rho(M):
    return float(np.max(np.abs(np.linalg.eigvals(M))))


def S_exact(z):
    return 2.0*z / math.tanh(z/2.0)


def S_taylor(z):
    return 8.0*(z*z - 2.0*z + 4.0)/(z*z - 2.0*z + 8.0)


def S_pade(z):
    return 4.0*(z + 2.0)*(z + 4.0)/(z*z + 8.0*z + 8.0)


def predicted(kind, z, s):
    if kind == "exact":
        return s < S_exact(z)
    if kind == "taylor":
        return z < 2.0 and s < S_taylor(z)
    if kind == "pade":
        return s < S_pade(z)
    raise ValueError(kind)


def check_random():
    rng = np.random.default_rng(1729)
    methods = {
        "exact": exact_matrix,
        "taylor": taylor_matrix,
        "pade": pade_matrix,
    }
    mismatch = {k: 0 for k in methods}
    tested = {k: 0 for k in methods}
    for _ in range(30000):
        z = 10.0 ** rng.uniform(-2.0, 1.2)
        s = 10.0 ** rng.uniform(-3.0, 1.2)
        for kind, fun in methods.items():
            # Skip points extremely close to the exact boundary, where floating-point
            # eigenvalue classification is intentionally ill-conditioned.
            if kind == "exact":
                gap = abs(s - S_exact(z))
            elif kind == "taylor":
                gap = min(abs(z - 2.0), abs(s - S_taylor(z)))
            else:
                gap = abs(s - S_pade(z))
            if gap < 1e-9:
                continue
            observed = rho(fun(z, s)) < 1.0
            expected = predicted(kind, z, s)
            tested[kind] += 1
            mismatch[kind] += int(observed != expected)
    return tested, mismatch


def bisection_hmax(kind, gamma, lam=1.0):
    if kind == "exact":
        stable = lambda h: lam*h*h < S_exact(gamma*h)
        hi = max(4.0, 4.0*gamma/lam + 4.0)
    elif kind == "taylor":
        stable = lambda h: gamma*h < 2.0 and lam*h*h < S_taylor(gamma*h)
        hi = max(4.0, 4.0/gamma)
    elif kind == "pade":
        stable = lambda h: lam*h*h < S_pade(gamma*h)
        hi = 8.0/math.sqrt(lam)
    else:
        raise ValueError(kind)
    while stable(hi):
        hi *= 2.0
    lo = 0.0
    for _ in range(100):
        mid = (lo + hi)/2.0
        if stable(mid):
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2.0


def main():
    tested, mismatch = check_random()
    print("random Schur-classification checks")
    for kind in ("exact", "taylor", "pade"):
        print(f"{kind:6s}: tested={tested[kind]} mismatches={mismatch[kind]}")

    print("\nthreshold diagnostics")
    print(f"min S_T = {24/7:.15f}")
    print(f"min S_P = {2+math.sqrt(2):.15f}")
    for z in (0.15, 1.0, 2.0, 3.0, 10.0):
        st = S_taylor(z) if z < 2.0 else float('nan')
        print(f"z={z:5.2f}  S_E={S_exact(z):.12f}  S_T={st:.12f}  S_P={S_pade(z):.12f}")

    print("\nrepresentative point z=3, s=1")
    for kind, fun in (("exact", exact_matrix), ("taylor", taylor_matrix), ("pade", pade_matrix)):
        ev = np.linalg.eigvals(fun(3.0, 1.0))
        print(f"{kind:6s}: eig={ev.tolist()} rho={rho(fun(3.0,1.0)):.12f}")

    print("\nstiff-friction h_max diagnostics (lambda=1)")
    for gamma in (10.0, 30.0, 100.0):
        he = bisection_hmax("exact", gamma)
        ht = bisection_hmax("taylor", gamma)
        hp = bisection_hmax("pade", gamma)
        print(
            f"gamma={gamma:5.1f}: "
            f"exact hmax={he:.12f}, hmax/(2gamma)={he/(2*gamma):.12f}; "
            f"Taylor hmax={ht:.12f}, gamma*hmax/2={gamma*ht/2:.12f}; "
            f"Pade hmax={hp:.12f}, hmax/2={hp/2:.12f}"
        )


if __name__ == "__main__":
    main()
