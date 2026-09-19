"""Numerical checks for endpoint-tail localization in Poisson--Laguerre extremes.

Requires Python 3 with SciPy. This script checks only mathematical formulas:
(1) the normalization effect of the +log(gamma) term in the d=3 Q2 shift;
(2) the Karamata/Laplace asymptotic and Gamma endpoint localization for a
    scaled Beta mark law.
"""
import math
from scipy.integrate import quad
from scipy.special import beta as beta_fn, gamma, gammainc

A = 1.7
gam = 0.4
v3 = 4.0 * math.pi / 3.0
c = 3.0 * (v3 * gam) ** (2.0 / 3.0)
EM2 = A * A / 2.0

print("d=3 Q2 normalization check")
print(f"A={A} gamma={gam} c={c:.15g}")
for L in (1e7, 1e10, 1e13):
    x_no_gamma = c * (A*A - EM2) * L ** (1.0/3.0) \
        - math.log(L) / 3.0 - math.log(c * A*A)
    x_with_gamma = x_no_gamma + math.log(gam)

    def log_G(x):
        q = c * (L + x) ** (1.0/3.0)
        log_Z = q*A*A + math.log1p(-math.exp(-q*A*A)) - math.log(A*A*q)
        return math.log(gam) - x - q*EM2 + log_Z

    print(
        f"L={L:.0e} "
        f"G_without_log_gamma={math.exp(log_G(x_no_gamma)):.12g} "
        f"G_with_log_gamma={math.exp(log_G(x_with_gamma)):.12g}"
    )

# Scaled-Beta example: M=A X, X~Beta(a,b).  Near A,
# P(A-M <= y) ~ C y^b with C=1/(b B(a,b) A^b).
a = 2.3
b = 1.5
B = beta_fn(a, b)
C = 1.0 / (b * B * A**b)
laplace_const = C * gamma(b + 1.0) / (2.0 * A) ** b

print("\nscaled-Beta endpoint check")
print(f"a={a} beta={b} C={C:.15g} laplace_const={laplace_const:.15g}")

def beta_density(x):
    return x ** (a - 1.0) * (1.0 - x) ** (b - 1.0) / B

def z_tilde(t):
    f = lambda x: math.exp(-t*A*A*(1.0-x*x)) * beta_density(x)
    return quad(f, 0.0, 1.0, epsabs=1e-13, epsrel=1e-12, limit=300)[0]

def tilted_scaled_cdf(t, y):
    # t(A-M)<=y iff X >= 1-y/(A t).
    lo = max(0.0, 1.0 - y/(A*t))
    den = z_tilde(t)
    f = lambda x: math.exp(-t*A*A*(1.0-x*x)) * beta_density(x)
    num = quad(f, lo, 1.0, epsabs=1e-13, epsrel=1e-12, limit=300)[0]
    return num / den

ys = (0.2, 0.5, 1.0, 2.0)
for t in (20.0, 100.0, 500.0):
    z = z_tilde(t)
    asym = laplace_const * t ** (-b)
    diffs = []
    for y in ys:
        target = gammainc(b, 2.0*A*y)  # Gamma(shape=b, rate=2A) CDF
        val = tilted_scaled_cdf(t, y)
        diffs.append(abs(val-target))
    print(f"t={t:6.1f} Z_over_asym={z/asym:.12g} max_grid_cdf_error={max(diffs):.12g}")
    for y in ys:
        target = gammainc(b, 2.0*A*y)
        val = tilted_scaled_cdf(t, y)
        print(f"  y={y:3.1f} tilted={val:.9f} gamma={target:.9f} diff={val-target:+.3e}")
