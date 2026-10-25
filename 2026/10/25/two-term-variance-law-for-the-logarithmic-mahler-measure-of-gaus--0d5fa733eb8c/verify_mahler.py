"""Reproducible checks for the logarithmic Gaussian polynomial circle-average variance.

Numerical tests corroborate; the proof of the asymptotic statement is analytical.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import spence


def sinc2(x):
    z = x / 2.0
    if abs(z) < 1e-10:
        return 1.0
    return (math.sin(z) / z)**2


def dilog_real(z):
    return float(spence(1.0 - z))


def finite_variance(n):
    def integrand(x):
        h = x / 2.0
        if abs(h) < 1e-10:
            return math.pi**2 / 6.0
        p = math.sin(n*h) / (n*math.sin(h))
        return dilog_real(min(1.0, max(0.0, p*p)))
    val = quad(integrand, 0, math.pi, epsabs=1e-10, limit=500)[0]
    return val / (4 * math.pi)


def exact_series(n, K=24):
    poly = [1]
    acc = 0.0
    for k in range(1, K + 1):
        poly2 = [0] * (len(poly) + n - 1)
        for j, a in enumerate(poly):
            for i in range(n):
                poly2[j+i] += a
        poly = poly2
        norm2 = sum(c*c for c in poly)
        acc += (norm2 / n**(2*k)) / (4*k*k)
    return acc


def H(s):
    return dilog_real(s) - s


def A_integrand(x):
    s = sinc2(x)
    if s == 1.0:
        return 0.0
    return x*x*(-math.log1p(-s)-s)


def coefficients(R=350):
    C = 0.25 + (2*quad(lambda x: H(sinc2(x)), 0, R, epsabs=1e-10, limit=1000)[0])/(8*math.pi)
    A = (2*quad(A_integrand, 0, R, epsabs=1e-8, limit=1000)[0])/(96*math.pi)
    return C,A


def run():
    checks=0
    assert abs(finite_variance(1)-math.pi**2/24)<1e-11; checks+=1
    assert abs(finite_variance(2)-(math.pi**2/24-math.log(2)**2/2))<1e-11; checks+=1
    for n in (2,3,5,7):
        assert 0 < finite_variance(n)-exact_series(n, K=45) < 1/(4*45)
        checks+=1
    for n in (16,32,64,128,256,512):
        v=finite_variance(n)
        assert v>0
        print('n=',n,'var=',f'{v:.15f}','nV=',f'{n*v:.15f}')
        checks+=1
    C,A=coefficients(350)
    assert 0.330 < C < 0.333
    assert .03 < A < .05
    checks+=2
    assert abs(finite_variance(128)*128-C)<1e-5; checks+=1
    assert abs(finite_variance(512)*512-C)<1e-6; checks+=1
    # Elementary cardinal B-spline checks: k=1,2,3, at zero, and second derivative.
    from math import comb,factorial
    def B(k):
        return sum((-1)**j*comb(2*k,j)*(k-j)**(2*k-1) for j in range(k))/factorial(2*k-1)
    def D(k):
        return -sum((-1)**j*comb(2*k,j)*(k-j)**(2*k-3) for j in range(k))/factorial(2*k-3)
    assert abs(B(1)-1)<1e-12 and abs(B(2)-2/3)<1e-12 and abs(B(3)-11/20)<1e-12; checks+=3
    assert D(2)==2 and D(3)==1; checks+=2
    print('C truncated',C,'A truncated',A,'total_checks',checks)

if __name__=='__main__':
    run()
