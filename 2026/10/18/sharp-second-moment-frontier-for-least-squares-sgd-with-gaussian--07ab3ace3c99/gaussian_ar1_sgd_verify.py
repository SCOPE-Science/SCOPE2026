"""Reproducible finite checks for Gaussian AR(1) least-squares SGD moments.

Analytic theorems are proved separately; quadrature and finite simulations are checks.
Run: python gaussian_ar1_sgd_verify.py
"""
import numpy as np
from scipy.special import roots_hermitenorm
from scipy.optimize import brentq


def transfer_growth(step, correlation, order=100):
    x, w = roots_hermitenorm(order)
    w = w / np.sqrt(2 * np.pi)
    r = correlation
    z = x[:, None] ** 2 + x[None, :] ** 2
    kernel = np.exp((2 * r * np.outer(x, x) - r*r*z)/(2*(1-r*r))) / np.sqrt(1-r*r)
    v = np.sqrt(w) * np.abs(1 - step*x*x)
    matrix = (v[:, None] * kernel) * v[None, :]
    return np.linalg.eigvalsh(matrix)[-1]


def two_step_moments(step, correlation, order=45):
    # Independent standard normals U,V; design coordinates X0=U, X1=rU+sqrt(1-r^2)V.
    z, w = roots_hermitenorm(order)
    w = w / np.sqrt(2*np.pi)
    X0 = z[:, None]
    X1 = correlation*X0 + np.sqrt(1-correlation**2)*z[None, :]
    M0 = (1-step*X0**2)**2
    M1 = (1-step*X1**2)**2
    weights = w[:, None] * w[None, :]
    return float(np.sum(weights * M0 * M1)), float(np.sum(weights * X0**2 * M1))


def check():
    checks = 0
    for s in [0.07, 1/3, 0.43, 0.61, 2/3, 0.9]:
        mu = 1-2*s+3*s*s
        v0 = transfer_growth(s,0)
        assert abs(v0-mu)<2e-11
        checks+=1
        for rho in (0.01,0.04,0.12,0.35,0.6):
            lam=transfer_growth(s,rho)
            assert lam>=v0-5e-9
            checks+=1
            c2,d1=two_step_moments(s,rho)
            ec2=mu**2+8*s*s*(3*s-1)**2*rho**2+24*s**4*rho**4
            ed1=mu+4*s*(3*s-1)*rho**2
            assert abs(c2-ec2)<2e-10,(c2,ec2)
            assert abs(d1-ed1)<2e-10,(d1,ed1)
            checks+=2
    for rho in (0.02,0.04,0.08,0.12,0.2):
        roots=[brentq(lambda a: transfer_growth(a,rho,order)-1,.45,.7,xtol=1e-11)
               for order in (50,80,120)]
        assert max(roots)-min(roots)<1e-7
        prediction=2/3-16*rho*rho/9
        print(f'rho={rho:.2f}: critical step={roots[-1]:.10f}; local series={prediction:.10f}')
        checks+=2
    print('PASSED',checks,'deterministic quadrature/threshold checks')

if __name__=='__main__':
    check()
