"""Numerical cross-checks for reciprocal Gaussian-product modal geometry.

Run with NumPy and SciPy installed. The analytic proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import loggamma, kv, zeta

EULER = 0.5772156649015328606065120900824
MU = (math.log(2) - EULER) / 2
CONST = 3 * float(zeta(3, 1)) / math.pi**2


def log_rayleigh_fourier_derivative(n, s):
    """Derivative of density of sum of n independent log-Rayleigh variables."""
    # The exact transform is exp(n*(i*t*log(2)/2 + logGamma(1+i*t/2))).
    def f(t):
        phase = n * (.5j*t*math.log(2) + loggamma(1+.5j*t)) - 1j*t*s
        return (-1j*t*np.exp(phase)).real
    return quad(f, 0, min(150.0, 40/math.sqrt(n) + 20),
                epsabs=1.e-12, epsrel=1.e-10, limit=200)[0] / math.pi


def log_rayleigh_fourier_density(n, s):
    def f(t):
        phase = n * (.5j*t*math.log(2) + loggamma(1+.5j*t)) - 1j*t*s
        return np.exp(phase).real
    return quad(f, 0, min(150.0, 40/math.sqrt(n) + 20),
                epsabs=1.e-12, epsrel=1.e-10, limit=200)[0] / math.pi


def exact_mode(n):
    return brentq(lambda s: log_rayleigh_fourier_derivative(n, s),
                  n*MU - 1.0, n*MU + 2.0, xtol=1.e-11)


def main():
    assert abs(exact_mode(1) - math.log(2)/2) < 1.e-9
    t2 = brentq(lambda t: t*kv(1,t)-2*kv(0,t), 0.2, 5)
    assert abs(math.exp(exact_mode(2)) - t2) < 1.e-9
    records = []
    for n in [1,2,3,4,5,10,20,50,100]:
        u = exact_mode(n)
        h = log_rayleigh_fourier_density(n, u)
        assert h > 0
        assert log_rayleigh_fourier_derivative(n,u-.2) > 0
        assert log_rayleigh_fourier_derivative(n,u+.2) < 0
        records.append((n, u, u-n*MU, 1/math.exp(u)))
        print(f'n={n:3d}, log_Rayleigh_mode={u:.12f}, offset={u-n*MU:.12f}, Gaussian_reciprocal_mode={math.exp(-u):.12g}')
    for n,u,offset,mode in records[-3:]:
        assert abs(offset-CONST) < .2/n
    rng = np.random.default_rng(517)
    g = rng.standard_normal(120000)
    observed = -np.log(np.abs(g)).mean()
    predicted = (EULER + math.log(2))/2
    assert abs(observed-predicted) < .02
    print('closed-form n=1 and Bessel n=2 agree; derivative brackets and high-n offset checked')
    print(f'LLN: empirical log reciprocal factor mean={observed:.6f}, predicted={predicted:.6f}')
    print('PASS (numerical corroboration, not a proof)')

if __name__ == '__main__':
    main()
