#!/usr/bin/env python3
"""Numerical example checks for an exact angular-return theorem.

The analytic theorem is proved separately; finite test cases are not its proof.
"""
import math

TWOPI = 2.0 * math.pi


def rk4_integrate(rhs, initial, n=24000):
    dt = TWOPI / n
    y = list(initial)
    s = 0.0
    for _ in range(n):
        k1 = rhs(s, y)
        y2 = [v + 0.5 * dt * w for v, w in zip(y, k1)]
        k2 = rhs(s + 0.5 * dt, y2)
        y3 = [v + 0.5 * dt * w for v, w in zip(y, k2)]
        k3 = rhs(s + 0.5 * dt, y3)
        y4 = [v + dt * w for v, w in zip(y, k3)]
        k4 = rhs(s + dt, y4)
        y = [v + dt * (a + 2 * b + 2 * c + d) / 6
             for v, a, b, c, d in zip(y, k1, k2, k3, k4)]
        s += dt
    return y


def close(a, b, tol=2e-8):
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)


def check_one(lam, a, eps, omega):
    assert lam > 0 and a > abs(eps) and omega > 0

    def affine_rhs(s, v):
        return [(2.0 / omega) *
                (lam - (a + eps * math.cos(2.0 * s)) * v[0])]

    B = rk4_integrate(affine_rhs, [0.0])[0]
    mapped_one = rk4_integrate(affine_rhs, [1.0])[0]
    rho_num = mapped_one - B
    rho = math.exp(-4.0 * math.pi * a / omega)
    close(rho_num, rho)
    fixed = B / (1.0 - rho)
    assert fixed > 0

    def period_rhs(s, v):
        rpow = v[0]
        assert rpow > 0
        dv = affine_rhs(s, [rpow])[0]
        return [dv, 1.0 / (omega * rpow)]

    v_end, measured_period = rk4_integrate(period_rhs, [fixed, 0.0])
    close(v_end, fixed)
    expected_period = TWOPI * a / (lam * omega)
    close(measured_period, expected_period)
    close(-math.log(rho) / expected_period, 2.0 * lam)
    test_v = fixed * 1.23
    close(rk4_integrate(affine_rhs, [test_v])[0],
          rho * test_v + B)
    return measured_period, rho


if __name__ == '__main__':
    first = check_one(1.0, 2.0, 0.8, 3.0)
    second = check_one(1.0, 2.0, -1.2, 3.0)
    close(first[0], second[0])
    close(first[1], second[1])
    check_one(1.7, 2.0, 0.4, 3.0)
    print('CHECK_OK')
