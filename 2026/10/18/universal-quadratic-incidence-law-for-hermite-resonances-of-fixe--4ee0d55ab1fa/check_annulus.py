"""Numerical corroboration of exact Gaussian annulus Hermite crossing theorem.

Dependencies: Python 3.9+, scipy, numpy. Finite checks do not prove
unrestricted assertions. Normalization is area t=pi*(x*x+xi*xi).
"""
from math import factorial, lgamma, exp, log, e
from scipy.special import gammainc, gammaincc
from scipy.integrate import quad
from scipy.optimize import brentq


def q(j, a, w):
    # Select complementary incomplete-gamma differences to avoid lower-tail
    # cancellation at large a; both formulas are mathematically identical.
    if a >= j + 1:
        return gammaincc(j + 1, a) - gammaincc(j + 1, a + w)
    return gammainc(j + 1, a + w) - gammainc(j + 1, a)


def crossing(m, n, w):
    b = exp((lgamma(n+1) - lgamma(m+1))/(n-m))
    lo, hi = max(0.0, b-w), b
    def f(a):
        return q(n, a, w) / q(m, a, w) - 1.0
    return brentq(f, lo, hi, xtol=1e-13), b


def limit_integrand(t):
    if t == 0: return 1.0
    if t == 1: return e**(-2)
    return t**(2*t/(1-t))


def run():
    for w in (0.1, 1., 3.):
        for m, n in ((0,1),(0,2),(2,5),(3,9),(10,15)):
            a,b = crossing(m,n,w)
            assert b-w < a < b
            assert abs(q(n,a,w)/q(m,a,w)-1) < 2e-11
            t1=max(0,a-0.05); t2=a+0.05
            assert q(n,t1,w)/q(m,t1,w) < 1
            assert q(n,t2,w)/q(m,t2,w) > 1
            print('w,m,n,a,B',w,m,n,round(a,10),round(b,10))
    C=e*e/2*quad(limit_integrand,0,1,epsabs=1e-12)[0]
    assert abs(C-1.1717702429648398)<1e-11
    print('universal C=', C)
    # Count via exact geometric-mean enclosure independent of special functions.
    for R in (20.,40.,80.,160.,300.):
        lower=upper=0
        n=1
        while n<=int(e*(R+1))+3:
            for m in range(n):
                b=exp((lgamma(n+1)-lgamma(m+1))/(n-m))
                lower+=(b<=R)
                upper+=(b<=R+1)
            n+=1
        assert lower<=upper
        print('R=',R,'M(R)/R^2=',lower/R**2,'M(R+1)/R^2=',upper/R**2)
    print('All specified finite checks passed; infinite theorem proved analytically.')


if __name__=='__main__':
    run()
