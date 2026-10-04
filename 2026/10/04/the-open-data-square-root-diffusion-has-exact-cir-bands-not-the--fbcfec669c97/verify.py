#!/usr/bin/env python3
import math

# Source benchmark parameters.
alphaG = 0.6
alphaE = 0.6
K0 = 5.0
delta = 0.1
betaG = 2.0
betaE = 2.0
r = 0.9
muG = 0.5
muE = 0.5
tau = 0.5
lam = 10.0
omega = 0.6
sigma = 0.4

XN = omega * lam * (muG * (r + delta) + tau * alphaG) / (betaG * (r + delta))
YN = (1.0 - omega) * lam * (muE * (r + delta) + tau * alphaE) / (betaE * (r + delta))
A = alphaG * XN + alphaE * YN

assert abs(XN - 2.4) < 1e-14
assert abs(YN - 1.6) < 1e-14
assert abs(A - 2.4) < 1e-14

shape = 2.0 * A / (sigma * sigma)
scale = sigma * sigma / (2.0 * delta)
mean = shape * scale
var = shape * scale * scale
sd = math.sqrt(var)

assert abs(shape - 30.0) < 1e-12
assert abs(scale - 0.8) < 1e-12
assert abs(mean - 24.0) < 1e-12
assert abs(var - 19.2) < 1e-12

# Regularized lower incomplete gamma P(a,x), Numerical-Recipes style.
def gammainc_P(a, x):
    if x < 0.0 or a <= 0.0:
        raise ValueError
    if x == 0.0:
        return 0.0
    gln = math.lgamma(a)
    eps = 2e-15
    itmax = 10000
    fpmin = 1e-300
    if x < a + 1.0:
        ap = a
        summ = 1.0 / a
        term = summ
        for _ in range(itmax):
            ap += 1.0
            term *= x / ap
            summ += term
            if abs(term) < abs(summ) * eps:
                return summ * math.exp(-x + a * math.log(x) - gln)
        raise RuntimeError("series did not converge")
    b = x + 1.0 - a
    c = 1.0 / fpmin
    d = 1.0 / b
    h = d
    for i in range(1, itmax + 1):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < fpmin:
            d = fpmin
        c = b + an / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        fac = d * c
        h *= fac
        if abs(fac - 1.0) < eps:
            q = math.exp(-x + a * math.log(x) - gln) * h
            return 1.0 - q
    raise RuntimeError("continued fraction did not converge")

def gamma_cdf(x, a, scale):
    if x <= 0.0:
        return 0.0
    return gammainc_P(a, x / scale)

def gamma_ppf(p, a, scale):
    lo = 0.0
    hi = max(a * scale, scale)
    while gamma_cdf(hi, a, scale) < p:
        hi *= 2.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if gamma_cdf(mid, a, scale) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0

q025 = gamma_ppf(0.025, shape, scale)
q975 = gamma_ppf(0.975, shape, scale)

source_lo = mean - 1.96 * var
source_hi = mean + 1.96 * var
gauss_lo = mean - 1.96 * sd
gauss_hi = mean + 1.96 * sd

source_cov = gamma_cdf(source_hi, shape, scale) - gamma_cdf(source_lo, shape, scale)
gauss_cov = gamma_cdf(gauss_hi, shape, scale) - gamma_cdf(gauss_lo, shape, scale)

assert abs(q025 - 16.1926992196) < 1e-8
assert abs(q975 - 33.3190699457) < 1e-8
assert abs(source_lo + 13.632) < 1e-12
assert abs(source_hi - 61.632) < 1e-12
assert abs(source_cov - 0.999999999676259) < 2e-12
assert abs(gauss_cov - 0.951947224026146) < 2e-10

print("VERIFY_OK")
print("XN", repr(XN))
print("YN", repr(YN))
print("A", repr(A))
print("shape", repr(shape))
print("scale", repr(scale))
print("mean", repr(mean))
print("variance", repr(var))
print("sd", repr(sd))
print("exact_95", repr(q025), repr(q975))
print("source_band", repr(source_lo), repr(source_hi))
print("source_exact_coverage", repr(source_cov))
print("gaussian_sd_band", repr(gauss_lo), repr(gauss_hi))
print("gaussian_sd_exact_coverage", repr(gauss_cov))
