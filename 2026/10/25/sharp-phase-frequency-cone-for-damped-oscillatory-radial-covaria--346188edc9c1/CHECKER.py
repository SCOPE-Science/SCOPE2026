"""Reproducibility cross-check of a complex Fourier transform and its spectral signs.

Requires numpy and scipy. This finite test does NOT prove positive definiteness
for the continuum; the analytic phase argument supplies that proof.
"""
from math import pi, atan, tan
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, jv


def analytic_spectrum(d, alpha, omega, beta, rho):
    z = complex(alpha, -omega)
    c = 2**d * pi**((d - 1)/2) * gamma((d + 1)/2)
    return float(c * (((1 - 1j * beta) * z) / ((z*z + rho*rho)**((d+1)/2))).real)


def direct_radial_quadrature(d, alpha, omega, beta, rho):
    def covariance(r):
        return np.exp(-alpha*r)*(np.cos(omega*r)+beta*np.sin(omega*r))
    if d == 1:
        return 2*quad(lambda r: covariance(r)*np.cos(rho*r), 0, 100, epsabs=1e-11)[0]
    return (2*pi)**(d/2)*rho**(1-d/2)*quad(
        lambda r:r**(d/2)*covariance(r)*jv(d/2-1,rho*r),
        0,100, epsabs=1e-10, limit=1000)[0]


def run():
    alpha, omega = 1.3, 0.51
    phi = atan(omega/alpha)
    max_error = 0.0
    for d in (1, 2, 3, 5):
        lower, upper = -1/tan(d*phi), alpha/omega
        beta = (lower+upper)/2
        for rho in (0.1, 1.0, 3.0):
            exact = analytic_spectrum(d,alpha,omega,beta,rho)
            independent = direct_radial_quadrature(d,alpha,omega,beta,rho)
            error = abs(exact-independent)
            max_error = max(max_error,error)
            assert error < 2e-9*(1+abs(exact)), (d,rho,error)
        assert analytic_spectrum(d,alpha,omega,lower-0.15,0) < 0
        assert analytic_spectrum(d,alpha,omega,upper+0.15,100) < 0
        for b in (lower, beta, upper):
            for rho in (0.1, 1., 3., 20.):
                assert analytic_spectrum(d,alpha,omega,b,rho) > 0
    for rho in (0.,0.1,1.,3.,10.):
        exact = analytic_spectrum(3,1.,1.,1.,rho)
        rational = 64*pi*rho*rho/(rho**4+4)**2
        assert abs(exact-rational)<1e-12*(1+abs(rational))
    print('PASS; dimensions 1,2,3,5; quadrature frequencies .1,1,3; coefficient endpoints checked')
    print('max absolute direct-quadrature discrepancy:',max_error)
    print('dimension-3 rational special case checked exactly to rounding error')

if __name__ == '__main__':
    run()
