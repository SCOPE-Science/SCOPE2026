"""Numerical checks of a Brownian distributed-resetting edge theorem.

Requires NumPy and SciPy. Finite numerical tests supplement, not replace, proof.
"""
import math
import numpy as np
from scipy.special import gammainc, gammaln
from scipy.optimize import minimize_scalar
from scipy.integrate import quad


def kernel(p, B, k):
    if k < 1e-6:
        return quad(lambda u: p*u**(p-1)*math.exp(-B*k*u), 0, 1,
                    epsabs=1e-11)[0]
    return math.exp(gammaln(p+1))*gammainc(p, B*k)/(B*k)**p


def mean(p, B, D, d, k):
    g = kernel(p, B, k)
    log_a = d*k-math.log(g)
    if log_a>650:
        return float("inf")
    return math.expm1(log_a)/(D*k*k)


def global_numeric_min(p, B, D, d):
    # Bracket candidates on a dense log grid before bounded minimization.
    grid = np.linspace(math.log(0.02/B), math.log(2e6/B), 700)
    vals = [mean(p, B, D, d, math.exp(v)) for v in grid]
    candidates = []
    for i in range(1, len(grid)-1):
        if vals[i] < min(vals[i-1], vals[i+1]):
            sol = minimize_scalar(lambda l: mean(p, B, D, d, math.exp(l)),
                                  bounds=(grid[i-1], grid[i+1]),
                                  method="bounded", options={"xatol": 1e-12})
            candidates.append((sol.fun, math.exp(sol.x)))
    if not candidates:
        raise AssertionError("No interior numerical candidate in scan")
    return min(candidates)


def run():
    B = D = 1.0
    for p in (0.5, 1.0, 1.5):
        a = 2-p
        constant = B**p * math.exp(a)/(D*math.gamma(p+1)*a**a)
        d = 1e-4
        tmin, k = global_numeric_min(p, B, D, d)
        print("subcritical", p, "d*k", d*k, "target", a,
              "scaled mean", tmin/d**a, "target", constant)
        assert abs(d*k/a-1)<.04
        assert abs(tmin/d**a/constant-1)<.04
        # Gamma(shape=p, rate=a) first moment is p/a.
        z=B*k
        ratio = p*gammainc(p+1,z)/gammainc(p,z)
        assert abs((ratio/(d*k))/(p/a)-1)<.05
    for p in (2.0, 2.5, 3.0):
        _, k0 = global_numeric_min(p, B, D, 0.0)
        _, k1 = global_numeric_min(p, B, D, 1e-3)
        print("critical/supercritical", p, "k0", k0, "k1", k1)
        assert k0<20 and k1<20
    for k in (0.5, 2.0, 6.0):
        g=kernel(2,B,k)
        explicit=2*(1-(1+B*k)*math.exp(-B*k))/(B*k)**2
        integral=quad(lambda u: 2*u*math.exp(-k*u),0,B)[0]
        assert abs(g-explicit)<1e-10
        assert abs(g-integral)<1e-10
    print("All finite-parameter checks passed.")


if __name__ == '__main__':
    run()
