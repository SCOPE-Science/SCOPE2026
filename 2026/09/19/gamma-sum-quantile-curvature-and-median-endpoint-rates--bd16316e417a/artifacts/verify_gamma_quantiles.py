import math
import scipy
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc, beta, gammainc, gamma


def gamma_cdf(shape, x):
    return 0.0 if x <= 0.0 else float(gammainc(shape, x))


def gamma_quantile(shape, q):
    hi = max(1.0, 2.0 * shape)
    while gamma_cdf(shape, hi) < q:
        hi *= 2.0
    return brentq(lambda x: gamma_cdf(shape, x) - q, 0.0, hi, xtol=2e-14, rtol=2e-14)


def positive_sum_cdf(r, alpha, z):
    norm = beta(r, r)
    def integrand(p):
        scale = alpha * p + (2.0 - alpha) * (1.0 - p)
        return (p ** (r - 1.0) * (1.0 - p) ** (r - 1.0) / norm) * gamma_cdf(2.0 * r, z / scale)
    return quad(integrand, 0.0, 1.0, epsabs=2e-11, epsrel=2e-11, limit=160)[0]


def positive_sum_quantile(r, alpha, q):
    center = gamma_quantile(2.0 * r, q)
    hi = max(1.0, 2.0 * center)
    while positive_sum_cdf(r, alpha, hi) < q:
        hi *= 2.0
    return brentq(lambda z: positive_sum_cdf(r, alpha, z) - q, 0.0, hi, xtol=2e-12, rtol=2e-12)


def difference_cdf(r, alpha, z):
    beta_coef = alpha - 2.0
    norm = gamma(r)
    def integrand(y):
        arg = (z + beta_coef * y) / alpha
        if arg <= 0.0:
            return 0.0
        return y ** (r - 1.0) * math.exp(-y) / norm * gamma_cdf(r, arg)
    return quad(integrand, 0.0, math.inf, epsabs=2e-10, epsrel=2e-10, limit=180)[0]


def difference_quantile(r, alpha, q):
    center = gamma_quantile(r, q)
    lo, hi = -max(1.0, 2.0 * center), max(1.0, 2.0 * center)
    while difference_cdf(r, alpha, lo) > q:
        lo *= 2.0
    while difference_cdf(r, alpha, hi) < q:
        hi *= 2.0
    return brentq(lambda z: difference_cdf(r, alpha, z) - q, lo, hi, xtol=2e-11, rtol=2e-11)


print('scipy', scipy.__version__)
r = 1.7
a = 2.0 * r
for q in (0.5, 0.9):
    z = gamma_quantile(a, q)
    theory = -z * (a + 1.0 - z) / (2.0 * (a + 1.0))
    eps = 0.04
    exact = positive_sum_quantile(r, 1.0 + eps, q)
    observed = (exact - z) / eps ** 2
    print(f'quadratic q={q:.1f} theory={theory:.12f} observed={observed:.12f} abs_err={abs(theory-observed):.3e}')

q_star = gamma_cdf(a, a + 1.0)
theory4 = (a + 1.0) / (2.0 * (a + 3.0))
for eps in (0.12, 0.08):
    exact = positive_sum_quantile(r, 1.0 + eps, q_star)
    observed = (exact - (a + 1.0)) / eps ** 4
    print(f'critical_quartic eps={eps:.2f} q_star={q_star:.12f} theory={theory4:.12f} observed={observed:.12f} abs_err={abs(theory4-observed):.3e}')

s = 1.7
g = gamma_quantile(s, 0.5)
for alpha in (0.03, 0.015):
    exact = positive_sum_quantile(s, alpha, 0.5)
    observed = (exact - 2.0 * g) / alpha
    theory = s - g
    print(f'left_endpoint alpha={alpha:.3f} theory={theory:.12f} observed={observed:.12f} abs_err={abs(theory-observed):.3e}')

for delta in (0.03, 0.015):
    exact = difference_quantile(s, 2.0 + delta, 0.5)
    observed = (exact - 2.0 * g) / delta
    theory = g - s
    print(f'right_endpoint delta={delta:.3f} theory={theory:.12f} observed={observed:.12f} abs_err={abs(theory-observed):.3e}')

phi = 0.8
g2 = gamma_quantile(2.0 * s, 0.5)
for c in (20.0, 50.0):
    alpha = 1.0 - 1.0 / c
    exact = phi * positive_sum_quantile(s, alpha, 0.5)
    coeff = phi * g2 * (2.0 * s + 1.0 - g2) / (2.0 * (2.0 * s + 1.0))
    approx = phi * g2 - coeff / c ** 2
    print(f'mckay_large_c c={c:.0f} exact={exact:.12f} approx={approx:.12f} abs_err={abs(exact-approx):.3e}')

theta = 0.8
for sigma in (0.2, 0.1):
    kappa = sigma ** 2 / theta ** 2
    alpha = 1.0 + math.sqrt(1.0 + kappa)
    exact = theta * difference_quantile(s, alpha, 0.5)
    approx = 2.0 * theta * g - (s - g) * sigma ** 2 / (2.0 * theta)
    print(f'vg_small_sigma sigma={sigma:.1f} exact={exact:.12f} approx={approx:.12f} abs_err={abs(exact-approx):.3e}')
