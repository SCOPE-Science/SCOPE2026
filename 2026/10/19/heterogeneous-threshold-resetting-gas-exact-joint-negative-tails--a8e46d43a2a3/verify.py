#!/usr/bin/env python3
"""Independent quadrature diagnostics for heterogeneous first-passage-triggered resets.

Finite evaluations corroborate constants and convergence; the infinite limit is
proved analytically in RESULT.md and is not established by this script.
Requires scipy and numpy. Run: python verify.py
"""
import math
from scipy.integrate import quad
from scipy.special import erf, gamma


def survival(t, D, L):
    return erf(L / math.sqrt(4 * D * t))


def left_prob(z, t, D, L):
    # The interval integral is cancellation-free even when z is large.
    # Use the short interval variable u in [0,1].
    from scipy.special import roots_legendre
    a, w = roots_legendre(64)
    ys = z + L * (a + 1)
    return (L / math.sqrt(4 * math.pi * D * t)) * sum(
        wi * math.exp(-yi * yi / (4 * D * t)) for yi, wi in zip(ys, w)
    )


def run_case(D, L, subset, cs=None, R_values=(12, 24, 48, 96)):
    n = len(D)
    assert n >= 3 and len(L) == n
    if cs is None:
        cs = [1.0] * len(subset)
    mu = quad(lambda t: math.prod(survival(t, di, li)
                                  for di, li in zip(D, L)),
              0, math.inf, epsabs=2e-10, epsrel=2e-10)[0]
    A = math.prod(li / math.sqrt(math.pi * di) for di, li in zip(D, L))
    nu = n / 2 - 1
    Q = sum(c * c / D[i] for i, c in zip(subset, cs))
    K = (A / mu) * gamma(nu) * (4 / Q)**nu
    out = []
    for R in R_values:
        mapping = dict(zip(subset, cs))
        def integrand(s):
            t = (R * R) * s
            return math.prod(left_prob(R * mapping[i], t, di, li)
                             if i in mapping else survival(t, di, li)
                             for i, (di, li) in enumerate(zip(D, L)))
        prob = R * R / mu * quad(integrand, 0, math.inf,
                                  epsabs=5e-13, epsrel=5e-10, limit=200)[0]
        ratio = prob * R**(n - 2) / K
        assert 0.0 < ratio < 1.05, (D, L, subset, R, ratio)
        out.append(ratio)
    assert out[-1] > 0.94, (D, L, subset, out)
    print('n=', n, 'subset=', subset, 'mu=', round(mu, 11),
          'K=', round(K, 11), 'ratios=', [round(v, 5) for v in out])
    return K


def main():
    D = (1.0, 0.5, 2.0, 1.5)
    L = (1.0, 1.5, 0.7, 1.2)
    k1 = run_case(D, L, (0,))
    k2 = run_case(D, L, (0, 1))
    assert abs(k2 / k1 - (D[1] / (D[0] + D[1]))**(len(D)/2-1)) < 1e-12
    run_case(D, L, (0, 1, 2))
    run_case(D, L, (0, 1, 2, 3))
    k1b = run_case(D, (2.0, 0.5, 1.8, 0.8), (0,))
    k2b = run_case(D, (2.0, 0.5, 1.8, 0.8), (0, 1))
    assert abs(k2b/k1b - k2/k1) < 1e-12
    D5 = (1.1, 0.8, 1.7, 1.2, 0.6)
    L5 = (0.8, 1.0, 1.3, 0.9, 1.4)
    k5a = run_case(D5, L5, (1,), R_values=(24, 48, 96))
    k5b = run_case(D5, L5, (1, 3), R_values=(24, 48, 96))
    assert abs(k5b / k5a - (D5[3] / (D5[1] + D5[3]))**(len(D5)/2-1)) < 1e-12
    print('PASS: three sets of diffusivities/thresholds, seven joint-tail integrals,'
          ' asymptotic coefficients and conditional-ratio invariance; finite checks only.')


if __name__ == '__main__':
    main()
