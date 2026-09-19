import math
import scipy
from scipy.integrate import quad
from scipy.optimize import brentq

# Numerical checks for the critical alpha=1 power-log family
#   f_k(x) = Z_k^{-1}(1-x^2) / log(e/(1-x^2))^k, |x|<1,
# and exact checks for the standard Laplace distribution.


def normalizer(k):
    f = lambda x: (1.0 - x*x) / math.log(math.e / (1.0 - x*x))**k
    return quad(f, -1.0, 1.0, epsabs=1e-13, epsrel=1e-13, limit=500)[0]


_norm_cache = {}


def c_norm(k):
    if k not in _norm_cache:
        _norm_cache[k] = 1.0 / normalizer(k)
    return _norm_cache[k]


def density(x, k):
    if abs(x) >= 1.0:
        return 0.0
    s = 1.0 - x*x
    return c_norm(k) * s / math.log(math.e / s)**k


def hellinger2(r, k):
    # Convention: H^2 = (1/2) integral (sqrt(f)-sqrt(g))^2.
    d = 2.0 * r

    def integrand(x):
        return 0.5 * (math.sqrt(density(x, k)) - math.sqrt(density(x-d, k)))**2

    cuts = [-1.0, -1.0+d, 0.0, d, 1.0, 1.0+d]
    total = 0.0
    for left, right in zip(cuts[:-1], cuts[1:]):
        if right > left:
            total += quad(integrand, left, right,
                          epsabs=1e-18, epsrel=2e-10, limit=500)[0]
    return total


def endpoint_mass(s, k):
    c = c_norm(k)

    def integrand(t):
        w = 2.0*t - t*t
        return c * w / math.log(math.e / w)**k

    return quad(integrand, 0.0, s, epsabs=1e-16, epsrel=2e-11, limit=500)[0]


def endpoint_s(u, k):
    return brentq(lambda s: endpoint_mass(s, k) - u,
                  max(1e-16, u/10.0), 1.0,
                  xtol=1e-14, rtol=1e-14, maxiter=200)


def delta_functional(p, k):
    jmax = int(math.floor(math.log2(1.0 / (4.0*p))))
    energy = 0.0
    for j in range(jmax + 1):
        u = (2.0**j) * p
        gap = endpoint_s(2.0*u, k) - endpoint_s(u, k)
        energy += (2.0**j) / (gap*gap)
    return energy**(-0.5)


def h_asymptotic(r, k):
    a = 2.0 * c_norm(k)
    L = math.log(1.0 / r)
    if k < 1.0:
        return a * r*r * L**(1.0-k) / (1.0-k)
    if k == 1.0:
        return a * r*r * math.log(L)
    raise ValueError("displayed boundary asymptotic check is for k<=1")


def delta_asymptotic(p, k):
    a = 2.0 * c_norm(k)
    L = math.log(1.0 / p)
    q = math.sqrt(2.0) - 1.0
    if k < 1.0:
        coeff = q * math.sqrt(2.0**(1.0-k) * (1.0-k) * math.log(2.0) / a)
        return coeff * math.sqrt(p) * L**(-(1.0-k)/2.0)
    if k == 1.0:
        coeff = q * math.sqrt(math.log(2.0) / a)
        return coeff * math.sqrt(p / math.log(L))
    raise ValueError("displayed dyadic asymptotic check is for k<=1")


print("scipy_version", scipy.__version__)
print("universal_ratio_Delta_over_omega",
      (math.sqrt(2.0)-1.0) * math.sqrt(math.log(2.0)))

print("\nHellinger ratios: exact numerical H^2 / stated leading term")
for k, radii in [
    (0.0, [1e-3, 1e-4, 1e-5, 1e-6]),
    (0.5, [1e-3, 1e-4, 1e-5, 1e-6]),
    (1.0, [1e-4, 1e-6, 1e-8]),
]:
    print("k=", k, "normalizing_inverse=", c_norm(k))
    for r in radii:
        print(" r=", r, "ratio=", hellinger2(r, k) / h_asymptotic(r, k))

print("\nDyadic-functional ratios: exact numerical Delta / stated leading term")
for k in [0.0, 0.5, 1.0]:
    print("k=", k, "normalizing_inverse=", c_norm(k))
    for p in [1e-4, 1e-6, 1e-8, 1e-10]:
        print(" p=", p, "ratio=", delta_functional(p, k) / delta_asymptotic(p, k))

# Exact regular-model obstruction: standard Laplace f(x)=exp(-|x|)/2.
ln2 = math.log(2.0)
print("\nLaplace exact dyadic phase constants")
print("subseq_Delta_over_sqrt_p_interval", math.sqrt(2.0)*ln2, 2.0*ln2)
print("subseq_Delta_over_omega_interval", ln2, math.sqrt(2.0)*ln2)
for m in [10, 20, 30]:
    p = 2.0**(-m-2)  # phase z=1/4, so jmax=m
    jmax = int(math.floor(math.log2(1.0 / (4.0*p))))
    delta = ln2 / math.sqrt(2.0**(jmax+1) - 1.0)
    print("m=", m, "jmax=", jmax,
          "Delta/sqrt(p)=", delta / math.sqrt(p),
          "Delta/sqrt(2p)=", delta / math.sqrt(2.0*p))
