"""Deterministic checks for Poisson-reset scaled-Brownian absolute-area extremes.

The asymptotic limit assertions require the accompanying analytic proof;
this program independently checks the explicit integral and saddle identities.
Only the Python standard library is required.
"""
import math

checks = 0

def near(a, b, tol=2e-10):
    global checks
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)
    checks += 1

def positive(value):
    global checks
    assert value > 0, value
    checks += 1


def coefficients(beta, kappa, r):
    m = beta + 2.0
    q = 2.0 / (m + 1.0)
    v = 4.0 * kappa / ((beta + 1.0) * (beta + 2.0))
    u = (m / (2.0 * v * r)) ** (1.0 / (m + 1.0))
    C = ((m + 1.0) / m) * r * u
    theta = m / (m + 1.0)
    return m, q, v, u, C, theta


def cost(u, m, v, r):
    return r * u + 1.0 / (2.0 * v * (u ** m))


def dimensionless_cost(z, a, m):
    return z + ((m ** m) / ((m + 1.0) ** (m + 1.0))) * a ** 2 / (z ** m)

for beta in (0.25, 0.75, 1.0, 1.5, 1.95):
    for kappa, r in ((0.4, 0.3), (1.0, 1.0), (1.7, 2.3)):
        m, q, v, u, C, theta = coefficients(beta, kappa, r)
        near(q * (m + 1.0), 2.0)
        near(r - m / (2.0 * v * (u ** (m + 1.0))), 0.0)
        near(cost(u, m, v, r), C)
        near(C ** (m + 1.0), (r ** m) * ((m + 1.0) ** (m + 1.0)) / (2.0 * v * (m ** m)))
        near(dimensionless_cost(theta, 1.0, m), 1.0)
        positive(dimensionless_cost(theta * 0.85, 1.0, m) - 1.0)
        positive(dimensionless_cost(theta * 1.15, 1.0, m) - 1.0)
        for a in (0.6, 0.9, 1.0, 1.1, 1.5):
            z = theta * (a ** q)
            near(dimensionless_cost(z, a, m), a ** q)
            near(1.0 - m * (m ** m) * a ** 2 / (((m + 1.0) ** (m + 1.0)) * (z ** (m + 1.0))), 0.0)
        # Numerical Riemann check of the covariance double integral, separate
        # from the analytic identity used in the proof.
        nodes = 160
        xs = [((j + .5) / nodes) ** beta for j in range(nodes)]
        double_integral = sum(min(a, b) for a in xs for b in xs) / nodes ** 2
        near(2.0 * kappa * double_integral, v, tol=3e-4)

m, q, v, u, C, theta = coefficients(1.0, 1.0, 1.0)
near(m, 3.0)
near(q, 0.5)
near(v, 2.0 / 3.0)
near(C * C, 8.0 / 3.0)
near(1.0 / (C * C), 3.0 / 8.0)
near(theta, 0.75)
print(f"PASS: {checks} deterministic coefficient/integral/optimization checks")
