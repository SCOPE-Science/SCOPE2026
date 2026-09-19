"""Numerical consistency checks for the large-K harmonic Schwarz asymptotics.

Requires mpmath >= 1.3.0.  The loop counts are fixed.
"""

import mpmath as mp

mp.mp.dps = 50


def alpha_beta(tau):
    """Exact alpha(tau), beta(tau) from complete elliptic integrals."""
    parameter = 1 - tau * tau  # mpmath uses m=k^2
    Kc = mp.ellipk(parameter)
    Ec = mp.ellipe(parameter)
    alpha = 4 / mp.pi * (Ec - tau * tau * Kc) / (1 - tau * tau)
    beta = 4 * tau / mp.pi * (Kc - Ec) / (1 - tau * tau)
    return alpha, beta


def optimizer(K):
    """Bisection for alpha(tau)/beta(tau)=K."""
    lo = mp.mpf("1e-40")
    hi = mp.mpf(1)
    for _ in range(200):
        mid = (lo + hi) / 2
        alpha, beta = alpha_beta(mid)
        if alpha / beta > K:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


print("K  tau_ratio  deficit_ratio  boundary_ratio")
for K0 in (100, 1000, 10000):
    K = mp.mpf(K0)
    tau = optimizer(K)
    Y = -mp.lambertw(-mp.e / (4 * K), -1)
    tau_model = 1 / (K * Y)

    alpha, _ = alpha_beta(tau)
    exact_deficit = 4 / mp.pi - alpha
    two_term_deficit = 2 / (mp.pi * K * K * Y) * (1 - 1 / (2 * Y))

    exact_boundary_sq = (
        2 - 4 / mp.pi * mp.acos(tau) / mp.sqrt(1 - tau * tau)
    )
    leading_boundary_sq = 4 * tau / mp.pi

    print(
        K0,
        mp.nstr(tau / tau_model, 14),
        mp.nstr(exact_deficit / two_term_deficit, 14),
        mp.nstr(exact_boundary_sq / leading_boundary_sq, 14),
    )
