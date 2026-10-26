#!/usr/bin/env python3
"""Finite numerical checks for the exact event-trigger equations."""
import math


def event_step(h, rho, sigma):
    """Find the first small positive root of the exact trigger equation."""
    c = sigma / (2.0 * rho**3)
    lo, hi = 0.0, 2.0 * c * h

    def values(tau):
        z = h * tau / 2.0
        ez = math.exp(z)
        # Stable form of 1 + exp(h*tau) - 2 exp(h*tau/2) cos(tau).
        e2 = math.expm1(z)**2 + 4.0 * ez * math.sin(tau / 2.0)**2
        error = math.sqrt((1.0 - h) * e2)
        h_next = -math.expm1(math.log1p(-h) + h * tau)
        residual = 2.0 * rho**3 * error - sigma * h_next
        return residual, h_next, error

    assert values(lo)[0] < 0.0
    assert values(hi)[0] > 0.0
    for _ in range(64):
        mid = (lo + hi) / 2.0
        if values(mid)[0] > 0.0:
            hi = mid
        else:
            lo = mid
    tau = (lo + hi) / 2.0
    residual, h_next, error = values(tau)
    assert 0.0 < h_next < h
    assert abs(residual) <= 1e-10 * h_next
    return tau, h_next


def main():
    rho, sigma, h = 1.2, 0.4, 1e-2
    total_time = 0.0
    last_tau = None
    for _ in range(2000):
        tau, h_next = event_step(h, rho, sigma)
        total_time += tau
        h = h_next
        last_tau = tau
    assert h > 0.0 and last_tau > 0.0 and total_time > 0.0
    # These are finite sanity checks only; the asymptotic limits are proved analytically.
    assert h < 1e-2
    assert last_tau < 2e-3
    print("VERIFY_OK: 2000 exact-flow/trigger updates; positive decreasing barrier margin;")
    print("finite checks only; asymptotic limits follow from the analytic proof")


if __name__ == '__main__':
    main()
