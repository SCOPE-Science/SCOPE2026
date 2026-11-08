"""Standalone numerical checks for a multivariate switched-trap stationary law.

Run: python verify.py (requires numpy, scipy, mpmath).
Analytical claims are established in RESULT.md; this checker is not a proof.
"""
from math import sqrt, log, pi, exp, gamma, isclose
import numpy as np
from scipy.integrate import quad
from scipy.special import kv, gammaln
import mpmath as mp

checks=0

def check(cond, description):
    global checks
    if not cond:
        raise AssertionError(description)
    checks+=1


def phi(s, alpha):
    return exp(-s/2)*(1+s/(2*alpha))*((1+s/alpha)**(-1-alpha/2))


def gamma_mix_phi(s, alpha):
    k=alpha/2
    z=1+s/alpha
    return exp(-s/2)*(.5*z**(-k)+.5*z**(-k-1))


def laplace_exp(s, alpha):
    k=alpha/2
    return (k+1)*np.log1p(s/alpha)-np.log1p(s/(2*alpha))


def laplace_from_levy(s, alpha):
    k=alpha/2
    # cancellation-free integrand for subordinator's positive Levy measure
    return quad(lambda t: -np.expm1(-s*t)*(k*np.exp(-alpha*t)+np.exp(-alpha*t)*(-np.expm1(-alpha*t)))/t,
                0,np.inf,epsabs=2e-10)[0]


def radial_log_kernel(r, alpha, d):
    nu=d/2
    a=sqrt(alpha)
    return 2/(2*pi)**nu*(a/r)**nu*kv(nu,a*r)


def selfdec_profile_derivative(r,alpha,d):
    nu=d/2
    a=sqrt(alpha); b=sqrt(2*alpha)
    g=lambda z: z**nu*kv(nu-1,z)
    return -(2/(2*pi)**nu)*((1+alpha/2)*a*g(a*r)-b*g(b*r))


def ou_driver_radial(r,alpha,d):
    return -selfdec_profile_derivative(r,alpha,d)/(r**(d-1))


for alpha in (.15,.6,.8,.83,1.0,1.5,2.,2.5,10.):
    for s in (0.,.03,.1,1.,5.,17.):
        check(abs(phi(s,alpha)-gamma_mix_phi(s,alpha)) < 3e-14,
              'gamma-mixture transform')
    for s in (.05,.5,3.,8.):
        check(abs(laplace_from_levy(s,alpha)-laplace_exp(s,alpha))<2e-9,
              'positive subordinator exponent')
    k=alpha/2
    ev=2+1/alpha
    ev2=4+6/alpha+4/alpha**2
    # Gamma-mixture moment reconstruction from the two exact Gamma shapes.
    eu=k+.5
    eu2=(k+1)**2
    check(abs(1+2*eu/alpha-ev)<1e-12,'second moment')
    check(abs(1+4*eu/alpha+4*eu2/alpha**2-ev2)<1e-12,'fourth moment')

alpha1=2*(sqrt(2)-1)
check(alpha1 < 2 and abs(alpha1-0.8284271247461901)<1e-14,'critical one-dimensional value')
for d in (1,2,3,4,5,6):
    for alpha in (2.,3.,6.):
        for r in (.0001,.005,.1,.5,1.,3.,8.):
            check(selfdec_profile_derivative(r,alpha,d)<0,'upper-region monotonicity')
            check(ou_driver_radial(r,alpha,d)>0,'positive OU driver density')

for alpha in (.3,.6,.8):
    check(selfdec_profile_derivative(1.e-4,alpha,1)>0,'1D lower-region obstruction')
for alpha in (1.,1.5,1.9):
    for d in (2,3,4,5,6):
        check(selfdec_profile_derivative(1.e-20,alpha,d)>0,
              'higher-dimensional small-radius obstruction')

# High-precision dimension-two Bessel K0 asymptotics resolve rates near alpha=2.
mp.mp.dps=90
for alpha in ('1.99','2.0','2.0001'):
    aa=mp.mpf(alpha); a=mp.sqrt(aa); b=mp.sqrt(2*aa); r=mp.mpf('1e-1000')
    ratio=(b/a)**2 * mp.besselk(0,b*r)/mp.besselk(0,a*r)
    # At finite r, ratio is slightly below 2, near its limiting value 2.
    check(ratio<2 and ratio>mp.mpf('1.999'), 'd=2 limiting derivative ratio')
    if aa < 2:
        check(ratio>1+aa/2, 'd=2 below-threshold near-zero derivative')
    else:
        check(ratio<1+aa/2, 'd=2 at/above-threshold derivative')

# Analytic intensity formula of the compound Poisson background driver,
# independently evaluated by radial numerical integration for dimensions 1-4.
for d in (1,2,3,4):
    sphere_area=2*pi**(d/2)/gamma(d/2)
    for alpha in (2.5,4.):
        f=lambda r: sphere_area*(r**(d-1))*ou_driver_radial(r,alpha,d)
        estimate=quad(f,0,np.inf,epsabs=1e-8,limit=180,points=None)[0]
        check(abs(estimate-alpha)<2e-6,'OU compound Poisson total jump rate')

print(f'PASS: {checks} computational diagnostic assertions')
print('Critical thresholds: d=1 =',alpha1,'; integer d>=2 = 2')
print('All assertions passed. These finite computations do not prove universal quantifiers.')
