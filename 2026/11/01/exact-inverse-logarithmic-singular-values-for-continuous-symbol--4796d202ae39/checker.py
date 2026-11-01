#!/usr/bin/env python3
"""Finite cross-checks for the stated analytic weighted Bergman Hankel formulas.
Run with Python 3, NumPy, SciPy. These tests do not establish the infinite asymptotic theorem.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_genlaguerre, gammaln, polygamma, betaln

TESTS = 0

def near(x, y, tol=3.e-8):
    global TESTS
    assert np.isfinite(x) and np.isfinite(y), (x,y)
    assert abs(x-y) <= tol * (1 + abs(y)), (x,y)
    TESTS += 1

def beta_moment(n, alpha, j):
    return math.exp(gammaln(alpha+1+j)-gammaln(alpha+1)+gammaln(n+alpha+2)-gammaln(n+alpha+2+j))

def exact_quadrature(n, alpha, a):
    """Direct independent integration over the exact Beta density of S=1-U."""
    b = betaln(alpha+1,n+1)
    def density(s):
        return math.exp(alpha*math.log(s)+n*math.log1p(-s)-b) if 0<s<1 else 0.
    def h(s):
        return 1+math.log(math.e/s)**(-a)
    eh = quad(lambda s: density(s)*h(s), 0, 1,epsabs=2e-11,limit=300)[0]
    uh2 = quad(lambda s: density(s)*(1-s)*h(s)**2, 0, 1,epsabs=2e-11,limit=300)[0]
    return uh2-n/(n+alpha+1)*eh*eh

def gamma_rule_beta(n, alpha, a, order=180):
    """Independent positive Gauss-Laguerre representation of the exact Beta law."""
    x,w = roots_genlaguerre(order, alpha)
    x,w = x[x<n],w[x<n]/math.gamma(alpha+1)
    offset=gammaln(n+alpha+2)-gammaln(n+1)-(alpha+1)*math.log(n)
    ratio = np.exp(offset+x+n*np.log1p(-x/n))
    w=w*ratio
    # Renormalize only the numerical quadrature weights to remove roundoff.
    near(float(np.sum(w)),1,4e-5 if n<100 else 2e-7)
    w=w/np.sum(w)
    h = 1+(1+math.log(n)-np.log(x))**(-a)
    u=1-x/n
    eh=np.dot(w,h)
    center=h-eh
    intrinsic=(alpha+1)/((n+alpha+1)*(n+alpha+2))
    d2=intrinsic*eh*eh -2*eh*np.dot(w,(x/n)*center)+np.dot(w,u*center*center)
    assert d2>0, (n,alpha,a,d2)
    return d2

# Exact base-symbol formula and a polynomial perturbation, using Beta moments.
for alpha in [-0.5,0,1,2,3.25]:
    for n in range(1,18):
        c=n/(n+alpha+1)
        eu=1-beta_moment(n,alpha,1)
        near(eu-c,(alpha+1)/((n+alpha+1)*(n+alpha+2)))
        m1,m2,m3=[beta_moment(n,alpha,k) for k in [1,2,3]]
        d2poly = 1+m1-m2-m3-c*(1+m1)**2
        assert d2poly>0, (n,alpha)
        if n in [2,4,8,16] and alpha in [0,1,2]:
            # h(s)=1+s: direct beta integrals must match the moment identity.
            b=betaln(alpha+1,n+1)
            integ=quad(lambda s: (s**alpha)*(1-s)**n*(1-s)*(1+s)**2*math.exp(-b),0,1)[0]
            near(integ,1+m1-m2-m3)

# Independent evaluation of the logarithmic-symbol singular squares.
for alpha in [0,1,2]:
    for a in [0.5,1.0,2.0]:
        for n in [8,20,40,100,1000]:
            d_exact=exact_quadrature(n,alpha,a)
            d_lag=gamma_rule_beta(n,alpha,a)
            near(d_lag,d_exact, 1.2e-3 if n==8 else 1.5e-4)

# Tail patterns for genuinely exact Beta density (Laguerre with finite-n correction).
for alpha in [0,2]:
    for a in [0.5,1.,2.]:
        C=a*math.sqrt(float(polygamma(1,alpha+1)))
        ns=[10_000, 100_000, 1_000_000, 100_000_000]
        ratios=[]
        for n in ns:
            d2=gamma_rule_beta(n,alpha,a)
            ratio=math.sqrt(d2)*math.log(n)**(a+1)/C
            ratios.append(ratio)
            assert 0.5<ratio<1.2, (alpha,a,n,ratio)
            TESTS += 1
        assert ratios[-1]>ratios[0],(alpha,a,ratios)
        TESTS += 1
print('PASS',TESTS,'finite assertions; infinite limiting claims require analytic proof')
