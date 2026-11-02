"""Numerical cross-checks for logarithmic Gaussian correlation-mixture tails.

Requires Python 3, NumPy, SciPy. The analytic proof is in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.stats import norm, multivariate_normal
from scipy.special import gamma, kv

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def profile(a, w1, w2):
    d = abs(math.log(w1 / w2))
    if d == 0:
        return math.sqrt(w1*w2) * (2.0**a)*gamma(a + 0.5)/math.sqrt(math.pi)
    nu = a + 0.5
    return math.sqrt(w1*w2)*2*(d/2)**nu*kv(nu,d/2)/math.sqrt(2*math.pi)


def finite_normalized(a, L, w1, w2):
    """Exact mixture via Plackett integral for Pr(R>1-s)=s**a."""
    u = math.exp(-L)
    q1, q2 = -norm.ppf(u*w1), -norm.ppf(u*w2)
    def integrand(t):
        if t <= 0 or t >= L:
            return 0.0
        r = 1.0-t/L
        log_density = (-math.log(2*math.pi)-0.5*math.log(1-r*r)
                       -(q1-q2)**2/(4*(1-r))
                       -(q1+q2)**2/(4*(1+r)))
        return math.exp(log_density + L + a*math.log(t/L) + (a-1)*math.log(L))
    z = quad(integrand, 0, L, epsabs=1e-11, epsrel=1e-10, limit=350)[0]
    return u*w1*w2*L**a + z


# Analytic profile: Gamma diagonal, Bessel quadrature, and a=1 elementary law.
for a in [0.25, 0.5, 1.0, 1.75, 2.0]:
    for w1,w2 in [(1,1),(.5,2),(1,4),(.1,7)]:
        d = math.log(w1/w2)
        expected = math.sqrt(w1*w2)/math.sqrt(2*math.pi) * quad(
            lambda t: t**(a-0.5)*math.exp(-t/2-d*d/(8*t)),
            0, 180, epsabs=1e-11, epsrel=1e-10, limit=350)[0]
        got = profile(a,w1,w2)
        check(math.isclose(got,expected,rel_tol=3e-8,abs_tol=1e-9), 'Bessel profile')
        check(math.isclose(got,profile(a,w2,w1),rel_tol=1e-13), 'symmetry')
        check(math.isclose(profile(a,2*w1,2*w2),2*got,rel_tol=1e-13), 'homogeneity')
        if a==1:
            elementary = min(w1,w2)*(1+abs(d)/2)
            check(math.isclose(got,elementary,rel_tol=2e-12), 'elementary case')

# Finite-u comparison for an explicit family of mixing distributions.
for a in [0.5, 1., 2.]:
    for w1,w2 in [(1,1),(.5,2),(1,4)]:
        truth = profile(a,w1,w2)
        f80=finite_normalized(a,80,w1,w2)
        f200=finite_normalized(a,200,w1,w2)
        check(abs(f200/truth-1)<0.07, 'finite-scale 200 relative error')
        check(abs(f200/truth-1)<abs(f80/truth-1)+0.02, 'convergence trend')
        check(f200>0, 'positivity')

# Independent finite-dimensional Plackett derivative check.
for r in [0.1,0.4,0.75]:
    for x,y in [(-1.3,-0.6),(-2,-1.2),(-0.6,-1.5)]:
        h=0.0002
        c_plus=multivariate_normal.cdf([x,y],mean=[0,0],cov=[[1,r+h],[r+h,1]])
        c_minus=multivariate_normal.cdf([x,y],mean=[0,0],cov=[[1,r-h],[r-h,1]])
        derivative=(c_plus-c_minus)/(2*h)
        density=math.exp(-(x*x-2*r*x*y+y*y)/(2*(1-r*r)))/(2*math.pi*math.sqrt(1-r*r))
        check(abs(derivative-density)<5e-7, 'Plackett derivative')

print(f'PASS: {checks} independent finite numerical checks')
print('a=1, weights=(1,1): limit=%.12f, normalized at L=200: %.12f' %
      (profile(1,1,1), finite_normalized(1,200,1,1)))
print('a=1, weights=(0.5,2): limit=%.12f, normalized at L=200: %.12f' %
      (profile(1,.5,2), finite_normalized(1,200,.5,2)))
print('a=0.5, weights=(1,1): limit=%.12f' % profile(.5,1,1))
print('a=2, weights=(1,1): limit=%.12f' % profile(2,1,1))
