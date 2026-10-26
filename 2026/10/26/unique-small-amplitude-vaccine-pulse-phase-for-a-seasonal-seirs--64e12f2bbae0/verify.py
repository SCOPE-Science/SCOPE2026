"""Numerical consistency checks of the stated small-amplitude SEIRS Floquet theorem.
Requires numpy and scipy. This file is not an infinite proof.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp


def exponent(epsilon, eta, tau, *, alpha, gamma, b, delta, beta, p, period):
    w = 2 * math.pi / period
    k = b + delta
    s0 = (b * (1 - p) + delta) / k
    denom = 1 - (1 - eta) * math.exp(-k * period)
    def rhs(z, flat):
        s = s0 * (1 - eta * math.exp(-k * z) / denom)
        rate = beta * (1 + epsilon * math.cos(w * (z + tau))) * s
        a = np.array([[-(alpha + b), rate], [alpha, -(gamma + b)]])
        return (a @ flat.reshape(2, 2)).reshape(4)
    sol = solve_ivp(rhs, (0, period), np.eye(2).reshape(4),
                    method='DOP853', rtol=2e-12, atol=2e-14)
    assert sol.success
    eig = np.linalg.eigvals(sol.y[:, -1].reshape(2, 2))
    assert max(eig.real) > 0
    return math.log(max(eig.real)) / period


def test_case(alpha, gamma, b, delta, beta, p, period):
    w = 2 * math.pi / period
    k = b + delta
    s0 = (b * (1 - p) + delta) / k
    B = alpha * beta * s0
    gap = math.sqrt((alpha - gamma) ** 2 + 4 * B)
    theta = math.atan2(w, k)
    K = alpha * beta * s0 * (1 - 2 * B / (gap * gap + w * w)) / (
        gap * period * math.sqrt(k * k + w * w))
    assert K > 0
    kw = dict(alpha=alpha, gamma=gamma, b=b, delta=delta,
              beta=beta, p=p, period=period)
    z = 1e-4
    root = (-theta / w) % period
    base = exponent(0, 0, 0, **kw)
    for shift in (0, .25, .5, .75):
        tau = (root + shift * period) % period
        mixed = (exponent(z, z, tau, **kw) - exponent(z, 0, tau, **kw)
                 - exponent(0, z, tau, **kw) + base) / (z * z)
        prediction = -K * math.cos(w * tau + theta)
        assert abs(mixed - prediction) < .004 + .002 * K, (
            tau, mixed, prediction)
    eta = .004
    epsilon = .004
    t_other = (root + .5 * period) % period
    assert exponent(epsilon, eta, root, **kw) < exponent(
        epsilon, eta, t_other, **kw)
    print('PASS', 'phase=', root, 'mixed-coefficient=', K)


if __name__ == '__main__':
    test_case(2.0, 1.4, .07, .3, 3.2, .11, 1.0)
    test_case(1.5, 3.2, .03, 1.3, 4.5, 0.0, 2.0)
    test_case(100.0, 100.0, .02, .25, 270.0, 0.0, 1.0)
    print('All three Floquet parameter-family checks passed.')
