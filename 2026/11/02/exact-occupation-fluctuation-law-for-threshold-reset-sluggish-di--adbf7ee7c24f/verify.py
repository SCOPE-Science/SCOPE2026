"""Reproduce the threshold-reset occupation-fluctuation identities.

Python >=3.10, standard library only. Tests exact rational Green-kernel
integration, independent of the advertised closed variance formula.
This tests algebra; an analytic proof establishes the time-limit theorem.
"""
from fractions import Fraction as F
from math import isclose


def variance_from_green(a, x):
    """Exact integrated 2G f (-L)^(-1)f, L=1, integer a>=0.

    The positive- and negative-half Green moments are integrated
    independently, without using the closed covariance formula.
    """
    h = (a + 1) * (a + 2)
    d = (1-x) / (2 * (1 - x**(a+2)))
    th = 1-d
    c = F(1,2)-th
    def ip(n):
        return ((1+x)-2*x**(n+2)) / ((n+1)*(n+2))
    def im(n):
        return (1-x) / ((n+1)*(n+2))
    value = (
        d*(c*ip(a)+ip(a+1)/2-d*ip(2*a+2))
        - th*(c*im(a)-im(a+1)/2+th*im(2*a+2))
    )/h
    return value


def exact_second_moment(a,x):
    return 3*(1-x*x)/(4*(a+2)**2*(a+3)*(2*a+3))


def clt_variance(a,x):
    return (3*(a+1)*(1-x*x) /
            (4*(a+2)*(a+3)*(2*a+3)*(1-x**(a+2))))

checks=0
for a in [0,1,2,3,4,5,7]:
    for x in [F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
        second=variance_from_green(a,x)
        assert second == exact_second_moment(a,x), (a,x,second)
        checks+=1
        mean_tau=(1-x**(a+2))/((a+1)*(a+2))
        assert second/mean_tau == clt_variance(a,x)
        checks+=1
        assert clt_variance(a,x)>0
        checks+=1
        if a == 0:
            assert clt_variance(a,x)==F(1,24)
            checks+=1
    if a>0:
        vals=[clt_variance(a,x) for x in [F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]]
        assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
        checks+=1

# Tests the exact half-line moment integrations against direct composite
# Simpson quadrature, for noninteger sluggishness values. This checks the
# power-integral reduction by an independent quadrature.
def simpson(fun, lo, hi, n=2000):
    if hi==lo: return 0.0
    h=(hi-lo)/n
    return h/3*(fun(lo)+fun(hi)+4*sum(fun(lo+(2*j-1)*h) for j in range(1,n//2+1))+2*sum(fun(lo+2*j*h) for j in range(1,n//2)))

for a in [0.25,0.5,1.5,2.5,3.75]:
    for x in [0,0.2,0.5,0.8]:
        h=(a+1)*(a+2)
        theta=1-(1-x)/(2*(1-x**(a+2)))
        def g(y):
            if y>=0:
                return (0.5-theta+y/2-(1-theta)*y**(a+2))/h
            return (0.5-theta+y/2+theta*(-y)**(a+2))/h
        def density(y):
            gg=((1+x)*(1-y)/2 if y>=x else (1-x)*(1+y)/2)
            return 2*gg*abs(y)**a*((1-theta) if y>0 else (-theta))*g(y)
        # A power-map smooths the fractional cusp at the origin.
        pwr=8
        neg=simpson(lambda z: density(-z**pwr)*pwr*z**(pwr-1),0,1)
        pos0=simpson(lambda z: density(x*z**pwr)*x*pwr*z**(pwr-1),0,1) if x>0 else 0
        pos1=simpson(lambda z: density(x+(1-x)*z**pwr)*(1-x)*pwr*z**(pwr-1),0,1)
        numerical=neg+pos0+pos1
        exact=exact_second_moment(a,x)
        assert isclose(numerical,exact,rel_tol=1e-7,abs_tol=1e-9),(a,x,numerical,exact)
        checks+=1
print(f'PASS: {checks} exact identities, sign inequalities, and independent quadrature comparisons')
