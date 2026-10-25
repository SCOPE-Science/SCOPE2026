"""Numerical corroboration of the exact seasonal two-patch Perron formula.

The analytical theorem is proved separately; these checks do not establish the
inequalities for infinitely many parameter values.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def exact_growth(a, b, m, T):
    k = a + b + m
    return (a-b-m)/2 + (2/T)*math.asinh((m/k)*math.sinh(k*T/4))


def direct_growth(a, b, m, T):
    B1 = np.array([[a, m], [0, -b-m]], dtype=float)
    B2 = np.array([[-b-m, 0], [m, a]], dtype=float)
    mat = expm(B2*T/2) @ expm(B1*T/2)
    eigs = np.linalg.eigvals(mat)
    return math.log(float(np.max(np.abs(eigs))))/T


def root_period(a, b, m):
    lo, hi = 0.001, 50.0
    assert exact_growth(a, b, m, lo) < 0
    assert exact_growth(a, b, m, hi) > 0
    return brentq(lambda t: exact_growth(a, b, m, t), lo, hi, xtol=1e-13)


def run():
    count = 0
    for a in [0.15, 0.5, 1.0, 2.3]:
        for b in [a+0.25, a+2.0]:
            for m in [0.15, 1.0, 2.7, 8.0]:
                for T in [0.2, 0.7, 2.3, 5.0]:
                    x = exact_growth(a, b, m, T)
                    y = direct_growth(a, b, m, T)
                    assert abs(x-y) < 3e-10, (a,b,m,T,x,y)
                    count += 1
                    if T<5.0:
                        assert exact_growth(a,b,m,T) < exact_growth(a,b,m,T+0.1)
                    if m<8.0:
                        assert exact_growth(a,b,m,T) < exact_growth(a,b,m+0.1,T)
    y=(3+math.sqrt(13))/4
    t=2*math.acosh(y)
    assert abs(exact_growth(1,3,2,t)) < 5e-14
    assert exact_growth(1,3,2,1) < 0 < exact_growth(1,3,2,3)
    for m in [0.1,0.5,1.0,2.0,5.0,12.0]:
        tc=root_period(1,3,m)
        assert exact_growth(1,3,m,tc*0.99)<0<exact_growth(1,3,m,tc*1.01)
    print(f'CHECK_OK matrix exponential identities: {count}; monotonic examples and critical period exact example verified')

if __name__ == '__main__':
    run()
