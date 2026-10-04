#!/usr/bin/env python3
import math


def phi(r, p, c, b):
    return r ** (1.0 - p) * (r - c) / (c * (b - r))


def bisect_root(p, c, b, rho, lo=None, hi=None):
    if lo is None:
        lo = c * (1.0 + 1e-12)
    if hi is None:
        hi = b * (1.0 - 1e-12)
    f_lo = phi(lo, p, c, b) - rho
    f_hi = phi(hi, p, c, b) - rho
    if f_lo * f_hi > 0:
        raise ValueError("interval does not bracket a root")
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        f_mid = phi(mid, p, c, b) - rho
        if f_lo * f_mid <= 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return 0.5 * (lo + hi)


def check_geometry(gamma, phi1, phi2, p, m1, m2):
    v0 = (1.0, 0.0)
    v1 = (math.cos(gamma), math.sin(gamma))
    n1 = (math.cos(phi1), math.sin(phi1))
    n2 = (math.cos(phi2), math.sin(phi2))
    dot = lambda x, y: x[0] * y[0] + x[1] * y[1]
    c = dot(n2, v0) / dot(n1, v0)
    b = dot(n2, v1) / dot(n1, v1)
    delta = phi2 - phi1
    assert 0.0 < c < b
    rho = m2 / m1
    r = bisect_root(p, c, b, rho)
    if abs(p - 2.0) < 1e-12:
        return
    a1 = (m1 * math.sin(delta) / (b - r)) ** (1.0 / (2.0 - p))
    a2 = r * a1

    # Cartesian line intersection n_i dot x = a_i.
    det = n1[0] * n2[1] - n1[1] * n2[0]
    x = (a1 * n2[1] - a2 * n1[1]) / det
    y = (n1[0] * a2 - n2[0] * a1) / det

    # Endpoints of facet 1 on ray v1 and facet 2 on ray v0.
    t1 = a1 / dot(n1, v1)
    e1 = (t1 * v1[0], t1 * v1[1])
    t2 = a2 / dot(n2, v0)
    e2 = (t2, 0.0)
    L1_cart = math.hypot(x - e1[0], y - e1[1])
    L2_cart = math.hypot(x - e2[0], y - e2[1])
    L1 = a1 * (b - r) / math.sin(delta)
    L2 = a1 * (r - c) / (c * math.sin(delta))
    assert math.isclose(L1_cart, L1, rel_tol=1e-10, abs_tol=1e-10)
    assert math.isclose(L2_cart, L2, rel_tol=1e-10, abs_tol=1e-10)
    mm1 = a1 ** (1.0 - p) * L1
    mm2 = a2 ** (1.0 - p) * L2
    assert math.isclose(mm1, m1, rel_tol=1e-10, abs_tol=1e-10)
    assert math.isclose(mm2, m2, rel_tol=1e-10, abs_tol=1e-10)


def check_phase_diagram():
    gamma = math.pi / 2.0
    phi1 = math.radians(20.0)
    phi2 = math.radians(60.0)
    c = math.cos(phi2) / math.cos(phi1)
    b = math.sin(phi2) / math.sin(phi1)
    p_star = 2.0 * math.sqrt(b) / (math.sqrt(b) - math.sqrt(c))
    assert p_star > 2.0

    # For p=5>p_star there are two critical points and a three-root window.
    p = 5.0
    s = b + c - (b - c) / (p - 1.0)
    disc = s * s - 4.0 * b * c
    assert disc > 0.0
    r_minus = 0.5 * (s - math.sqrt(disc))
    r_plus = 0.5 * (s + math.sqrt(disc))
    assert c < r_minus < math.sqrt(b * c) < r_plus < b
    rho_max = phi(r_minus, p, c, b)
    rho_min = phi(r_plus, p, c, b)
    assert 0.0 < rho_min < rho_max
    rho = math.sqrt(rho_min * rho_max)
    roots = [
        bisect_root(p, c, b, rho, c * (1 + 1e-12), r_minus),
        bisect_root(p, c, b, rho, r_minus, r_plus),
        bisect_root(p, c, b, rho, r_plus, b * (1 - 1e-12)),
    ]
    assert roots[0] < roots[1] < roots[2]
    for r in roots:
        assert math.isclose(phi(r, p, c, b), rho, rel_tol=1e-10)

    # Critical roots have product bc.
    assert math.isclose(r_minus * r_plus, b * c, rel_tol=1e-12)


def check_p2():
    gamma = math.pi / 2.0
    phi1 = math.radians(25.0)
    phi2 = math.radians(55.0)
    c = math.cos(phi2) / math.cos(phi1)
    b = math.sin(phi2) / math.sin(phi1)
    delta = phi2 - phi1
    r = 0.5 * (c + b)
    m1 = (b - r) / math.sin(delta)
    m2 = (r - c) / (c * r * math.sin(delta))
    for a1 in (0.4, 1.0, 3.5):
        a2 = r * a1
        L1 = a1 * (b - r) / math.sin(delta)
        L2 = a1 * (r - c) / (c * math.sin(delta))
        assert math.isclose(a1 ** -1 * L1, m1, rel_tol=1e-12)
        assert math.isclose(a2 ** -1 * L2, m2, rel_tol=1e-12)


if __name__ == "__main__":
    check_geometry(1.3, -0.1, 0.45, 0.0, 1.7, 0.8)
    check_geometry(1.3, -0.1, 0.45, 1.0, 0.6, 2.2)
    check_geometry(1.4, 0.05, 0.65, 3.0, 1.1, 0.9)
    check_phase_diagram()
    check_p2()
    print("VERIFY_OK")
