"""Finite-column diagnostics for the Gaussian lazy-shift asymptotic law.

Requires numpy, scipy. All assertions are finite numerical checks only.
"""
import math
import numpy as np
from scipy.stats import binom
from scipy.integrate import quad
from scipy.optimize import minimize_scalar


def columns(n, alpha, delta):
    mu, sigma = n*delta, math.sqrt(n*delta*(1-delta))
    jlo, jhi = max(1, int(mu-6*sigma)), min(n+1+int(10*sigma), int(mu+10*sigma)+2)
    k = np.arange(n+2)
    p = binom.pmf(k, n, delta)
    d = np.diff(np.r_[0., p])
    out0, out1 = 0., 0.
    for j in range(jlo, jhi):
        ix = np.arange(min(n+2, j))
        weight = (j/(j-ix))**alpha
        out0 = max(out0, float(np.dot(p[ix], weight)))
        out1 = max(out1, float(delta*np.dot(np.abs(d[ix]), weight)))
    return out0, out1


def gaussian_max(alpha, derivative):
    def f(s):
        def kernel(z):
            u = s-z
            return z**(-alpha)*math.exp(-u*u/2)/math.sqrt(2*math.pi)*(abs(u) if derivative else 1)
        return quad(kernel, 0, np.inf, epsabs=1e-8, limit=200)[0]
    return -minimize_scalar(lambda s:-f(s), method='bounded', bounds=(-5,10)).fun


def main():
    for alpha, delta in [(0.2,0.5),(0.5,0.5),(0.7,0.4)]:
        lim0 = (delta/(1-delta))**(alpha/2)*gaussian_max(alpha,False)
        lim1 = (delta/(1-delta))**((alpha+1)/2)*gaussian_max(alpha,True)
        n = 2500
        a,b = columns(n, alpha, delta)
        scaled0 = n**(-alpha/2)*a
        scaled1 = n**((1-alpha)/2)*b
        # Both converge slowly due to fractional singularity; use loose finite diagnostic margins.
        assert abs(scaled0/lim0-1) < 0.25, (alpha,scaled0,lim0)
        assert abs(scaled1/lim1-1) < 0.35, (alpha,scaled1,lim1)
        print(alpha,delta, 'scaled-power',scaled0,'limit',lim0, 'scaled-difference',scaled1,'limit',lim1)
    print('finite diagnostics passed; analytic proof is separate')


if __name__ == '__main__':
    main()
