#!/usr/bin/env python3
"""Independent quadrature checks for stationary fitness integrals and edge laws.
Requires Python >=3.10 and SciPy >=1.9. These are finite checks, not proofs.
"""
import math
from scipy.integrate import quad

C = 0.4
BETA = 0.1


def kernel(s, theta, log_inverse_zeta, *, background=False):
    # Exact substitution u = exp(-s) for q(l)=2(1-l),
    # r(1-u) = C*u*(1+log(1/u))**theta, zeta=exp(-L).
    x = s - log_inverse_zeta
    z = math.exp(x) if x < 680 else float('inf')
    d = 1 + C * (1 + s) ** theta + z
    numerator = 2 * math.exp(-s) if background else -math.expm1(-s)
    return numerator / d


def integrate(theta, L, *, background=False, a=0.0, b=None):
    if b is None:
        b = L + 32
    if b <= a:
        return 0.0
    knots = [a, b]
    # Intermediate decades stabilize tail integration and endpoint resolution.
    knots.extend(10.0 ** k for k in range(-1, 13) if a < 10.0 ** k < b)
    knots.extend(x for x in (L / 4, L / 2, L - 20, L - 2, L, L + 2) if a < x < b)
    knots = sorted(set(knots))
    ans = 0.0
    for low, high in zip(knots, knots[1:]):
        val, _ = quad(lambda s: kernel(s, theta, L, background=background),
                      low, high, epsabs=3e-11, epsrel=1e-10, limit=150)
        ans += val
    return ans


def test():
    checks = 0
    def close(x, y, tol):
        nonlocal checks
        assert math.isfinite(x) and abs(x-y) <= tol, (x, y, tol)
        checks += 1
    # Exact elementary integrals for constant marginal factor theta=0.
    for L in (1.0, 4.0, 9.0, 18.0, 34.0):
        z = math.exp(-L)
        a = 1 + C
        h = math.log1p(a/z)
        exact_I = (1 / a + z / a**2) * h - 1 / a
        exact_J = 2 / a - 2*z/a**2 * h
        num_I = integrate(0.0, L)
        num_J = integrate(0.0, L, background=True)
        close(num_I, exact_I, 3e-9)
        close(num_J, exact_J, 3e-9)
        rho = num_I / (1 - BETA*num_J)
        origin_mass = num_I / rho
        background_mass = BETA * num_J
        close(origin_mass + background_mass, 1.0, 1e-12)
        assert rho > 0 and 0 < origin_mass < 1
        checks += 2

    # Sharp leading density asymptotics for the 4 divergent regimes.
    L = 1e7
    observed = {
        -0.5: integrate(-0.5, L),
        0.0: integrate(0.0, L),
        0.5: integrate(0.5, L),
        1.0: integrate(1.0, L),
    }
    targets = {
        -0.5: L,
        0.0: L/(1 + C),
        0.5: math.sqrt(L) * 2 / C,
        1.0: math.log(L) / C,
    }
    for theta in observed:
        close(observed[theta]/targets[theta], 1.0, 0.16)

    # Condensate's logarithmic-gap profile for theta<=0 and 0<theta<1.
    for theta in (-0.5, 0.0, 0.5):
        I = observed[theta]
        for t in (0.2, 0.5, 0.8):
            fraction = integrate(theta, L, b=t*L) / I
            expected = t**(1-theta) if theta > 0 else t
            close(fraction, expected, 0.065)

    # At theta=1 ordinary log coordinate collapses; double-log stays uniform.
    L = 1e8
    I = integrate(1.0, L)
    for t in (0.2, 0.5, 0.8):
        double_log_cutoff = math.expm1(t * math.log1p(L))
        fraction = integrate(1.0, L, b=double_log_cutoff)/I
        close(fraction, t, 0.09)
    close(integrate(1.0, L, b=.1*L)/I, 1.0, 0.16)

    # For theta>1 I converges and no condensate survives at the endpoint.
    for theta in (1.5, 2.0):
        I1, I2 = integrate(theta, 1e6), integrate(theta, 1e8)
        assert 0 < I1 < I2 and I2 - I1 < (0.1 if theta == 1.5 else 0.001)
        checks += 2
    print(f"PASS: {checks} deterministic analytical-formula and quadrature checks")

if __name__ == '__main__':
    test()
