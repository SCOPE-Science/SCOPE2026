#!/usr/bin/env python3
"""Numerical replay for the cubic grid-phase qubit endpoint law.
Uses only the Python standard library.
"""
import math


def rotate(v, u, delta, t):
    """Apply exp(t*(delta M_z + u M_x)) to a Bloch vector."""
    norm = math.hypot(u, delta)
    if norm == 0.0:
        return v
    ax, ay, az = u / norm, 0.0, delta / norm
    th = norm * t
    ct, st = math.cos(th), math.sin(th)
    x, y, z = v
    cx = ay*z - az*y
    cy = az*x - ax*z
    cz = ax*y - ay*x
    dot = ax*x + ay*y + az*z
    q = 1.0 - ct
    return (
        x*ct + cx*st + ax*dot*q,
        y*ct + cy*st + ay*dot*q,
        z*ct + cz*st + az*dot*q,
    )


def parameters(delta, n):
    omega = math.sqrt(1.0 + delta*delta)
    tau = 2.0 * math.pi / omega
    alpha = (math.pi - math.acos(delta*delta)) / (2.0 * math.pi)
    x = n * alpha
    k = math.floor(x)
    r = x - k
    return tau, alpha, k, r


def endpoint(delta, n, total_time, middle):
    tau, alpha, k, r = parameters(delta, n)
    step = total_time / n
    v = (0.0, 0.0, 1.0)
    v = rotate(v, -1.0, delta, k * step)
    v = rotate(v, middle, delta, step)
    v = rotate(v, +1.0, delta, (n-k-1) * step)
    return v


def solve_branch(delta, n):
    tau, alpha, k, r = parameters(delta, n)
    h = tau / n
    g = math.sqrt(1.0 - delta*delta)
    cpred = r * (1.0-r) / 3.0
    t = tau + cpred * h**3
    u = 1.0 - 2.0*r - delta*delta*r*(1.0-r)*h/g

    for _ in range(20):
        v = endpoint(delta, n, t, u)
        f0, f1 = v[0], v[1]
        if max(abs(f0), abs(f1)) < 2e-14:
            break
        et, eu = 1e-7, 1e-7
        vt = endpoint(delta, n, t+et, u)
        vu = endpoint(delta, n, t, u+eu)
        a = (vt[0]-f0)/et
        c = (vt[1]-f1)/et
        b = (vu[0]-f0)/eu
        d = (vu[1]-f1)/eu
        det = a*d-b*c
        if abs(det) < 1e-12:
            raise RuntimeError("singular Newton Jacobian")
        dt = (-f0*d+b*f1)/det
        du = (-a*f1+c*f0)/det
        t += dt
        u += du

    v = endpoint(delta, n, t, u)
    residual = math.sqrt(v[0]**2 + v[1]**2 + (v[2]+1.0)**2)
    cest = (t-tau)/h**3
    return r, cpred, cest, residual, u


def main():
    delta = 0.5
    # The coefficient estimate should approach r(1-r)/3 as N grows,
    # despite the phase r changing with N.
    for n in (40, 60, 80, 100, 150, 200):
        r, cpred, cest, residual, u = solve_branch(delta, n)
        if residual > 2e-12:
            raise AssertionError((n, "endpoint residual", residual))
        if not (-1.0-1e-10 <= u <= 1.0+1e-10):
            raise AssertionError((n, "middle amplitude", u))
        # Absolute convergence check is robust even when r is near 0 or 1.
        if abs(cest-cpred) > 1.0e-3:
            raise AssertionError((n, r, cpred, cest))

    # Exact grid alignment: delta^2=1/2 gives alpha=1/3.
    delta = 1.0 / math.sqrt(2.0)
    n = 60
    tau, alpha, k, r = parameters(delta, n)
    if abs(alpha-1.0/3.0) > 2e-15 or min(r, 1.0-r) > 2e-13:
        raise AssertionError((alpha, r))
    step = tau/n
    v = (0.0, 0.0, 1.0)
    v = rotate(v, -1.0, delta, k*step)
    v = rotate(v, +1.0, delta, (n-k)*step)
    residual = math.sqrt(v[0]**2 + v[1]**2 + (v[2]+1.0)**2)
    if residual > 2e-12:
        raise AssertionError(("aligned residual", residual))

    print("VERIFY_OK")


if __name__ == "__main__":
    main()
