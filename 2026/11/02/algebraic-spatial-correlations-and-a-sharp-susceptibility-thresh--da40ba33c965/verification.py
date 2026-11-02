"""Numerical cross-checks of coalescing-walk and renewal-age formulas.

Requires NumPy and SciPy. Finite quadrature is not a proof of asymptotics.
"""
import math

from scipy.integrate import quad
from scipy.special import gammaln, ive

CHECKS = 0


def near(a, b, tol, label):
    global CHECKS
    assert math.isfinite(a) and math.isfinite(b), label
    assert abs(a - b) <= tol * max(1.0e-12, abs(b)), (
        label, a, b, abs(a - b) / max(1.0e-12, abs(b))
    )
    CHECKS += 1


def moment(n, b):
    assert n > b > 0
    logval = (math.log(2 * n) - math.log(n + b)
              + gammaln(2 * b) + gammaln(n - b)
              - gammaln(b) - gammaln(n + b))
    return math.exp(logval)


def moment_integral(n, b):
    # Independent inversion integral after s=2(cosh v-1).
    # Factor its exact integrable endpoint singularity v**(2*b-1).
    def regular(v):
        if v == 0.0:
            return 2.0 * math.exp(-gammaln(b))
        normalized_s = 2.0 * math.sinh(v/2) / v
        return (normalized_s**(2*b-2) * (2*math.sinh(v)/v)
                * math.exp(-n*v-gammaln(b)))
    return quad(regular, 0.0, 20.0, weight="alg",
                wvar=(2*b-1, 0), epsabs=2e-12,
                epsrel=5e-11, limit=400)[0]


def age_survival(t, alpha, tau):
    mu = alpha * tau / (alpha - 1)
    return (1 - t / mu) if t < tau else (tau / t)**(alpha - 1) / alpha


def covariance_over_initial_variance(n, alpha, tau):
    # The first-passage density is (n/t)e^{-2t} I_n(2t).
    # Using y=log(t), its Jacobian cancels n/t.
    def g(y):
        t = math.exp(y)
        return n * ive(n, 2 * t) * age_survival(t, alpha, tau)
    return quad(g, math.log(1e-3), math.log(5e8), points=[math.log(tau),
                    math.log(n*n)], epsabs=5e-12,
                    epsrel=3e-9, limit=350)[0]


def asymptotic_constant(alpha, tau):
    b = alpha - 1
    return math.exp(b * math.log(4*tau) + gammaln(b+0.5)
                    - gammaln(0.5)) / alpha


# Exact Mellin/Beta identity against an independently integrated kernel.
for n, b in [(4, 0.5), (8, 1.0), (10, 1.8), (14, 2.5),
             (6, 0.3), (12, 3.1)]:
    near(moment(n, b), moment_integral(n, b), 1e-8,
         f"negative Mellin moment n={n}, b={b}")

# Equilibrium age: continuity at cutoff; density integrates to one.
for alpha, tau in [(1.2, 1.), (1.5, 2.), (2., 1.), (3.5, 0.7)]:
    mu = alpha * tau / (alpha - 1)
    near(age_survival(tau, alpha, tau), 1/alpha, 5e-13,
         "age survival at cutoff")
    near(1-tau/mu, 1/alpha, 5e-13, "left age survival")
    def age_density(a):
        return (1/mu) if a < tau else ((tau/a)**alpha / mu)
    integral = quad(age_density, 0., tau)[0] + quad(
        age_density, tau, math.inf, epsabs=2e-11)[0]
    near(integral, 1., 3e-10, "equilibrium age normalization")

# An exact gamma-function upper bound for the stationary pair correlation;
# the cutoff correction becomes extremely small at large separation.
for alpha in [1.2, 1.5, 2.0, 2.7]:
    b = alpha-1
    k = asymptotic_constant(alpha, 1.)
    for n in [20, 50, 100]:
        c = covariance_over_initial_variance(n, alpha, 1.)
        upper = moment(n, b) / alpha
        assert c > 0, (alpha, n)
        CHECKS += 1
        near(min(c, upper), c, 0.002, "cutoff bound (numerical)")
        # At n=20 there are visible inverse-distance finite-size effects.
        near(c*n**(2*b), k, 0.022, "asymptotic constant")
        # A gamma-ratio check that does not involve Bessel quadrature.
        near(upper*n**(2*b), k, 0.022, "Mellin gamma asymptotic")

# Exact algebraic case b=1, n>1, fixes the walk's total jump rate.
for n in [2, 3, 7, 20, 50]:
    near(moment(n, 1), 2/(n*n-1), 2e-12,
         "integer-order exact identity")

print(f"PASS: {CHECKS} deterministic coefficient, age-law, Mellin, and Bessel checks")
