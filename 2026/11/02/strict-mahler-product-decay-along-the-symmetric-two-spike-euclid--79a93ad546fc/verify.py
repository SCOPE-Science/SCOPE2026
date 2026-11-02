"""Reproduce finite tests for the exact symmetric axial-spike Mahler law.

Usage: python verify.py   (Python standard library only)
Finite tests complement, and do not replace, the analytic proof.
"""
from fractions import Fraction
from math import pi, gamma, sqrt


def ball_vol(k):
    return pi ** (k / 2) / gamma(1 + k / 2)


def simpson(fun, upper, panels=3000):
    assert panels % 2 == 0
    h = upper / panels
    return (fun(0) + fun(upper) + 4 * sum(fun(j * h) for j in range(1, panels, 2))
            + 2 * sum(fun(j * h) for j in range(2, panels, 2))) * h / 3


def law(d, a):
    t = 1 / a
    f = lambda x: max(0, 1-x*x) ** ((d - 1)/2)
    I = simpson(f, t)
    H = (1-t*t) ** ((d+1)/2)/(d*t)
    return 4 * ball_vol(d-1) ** 2 * I * (I+H)


def independent_shell(d, a):
    t = 1/a
    f = lambda z: max(0, 1-z*z) ** ((d-1)/2)
    v0 = simpson(f,t)
    v1 = simpson(lambda q: ((1-t*(t+q*(a-t)))/sqrt(1-t*t))**(d-1), 1) * (a-t)
    vp = 2*ball_vol(d-1) * simpson(f,t)
    v = 2*ball_vol(d-1) *(v0+v1)
    return v*vp


def check():
    count=0
    for d in (2, 3, 4, 5, 8):
        prev = ball_vol(d)**2
        lower = 4*ball_vol(d-1)**2/d
        for a in (1.01, 1.1, 1.7, 2.5, 4, 9, 30):
            actual=law(d,a)
            assert lower < actual < prev, (d,a,actual,lower,prev)
            count+=1
            alternate=independent_shell(d,a)
            assert abs(actual-alternate)/actual < 4e-9, (d,a,actual,alternate)
            count+=1
            if d==3:
                exact=4*pi*pi/9*(3+2/a**2-1/a**4)
                assert abs(actual-exact)<2e-10, (d,a,actual,exact)
                count+=1
            prev=actual
        assert abs(law(d,1000)/lower -1-(d-1)/(3*1000**2))<2e-9
        count+=1
    # Exact rational algebra for the n=3 formula and its derivative.
    for denominator in (3, 4, 7, 13, 29):
        t=Fraction(1,denominator)
        I=t-t**3/3
        H=(1-t*t)**2/(3*t)
        assert I*(I+H)==(3+2*t*t-t**4)/9
        count+=1
        J=t**3/3-t**5/5
        S=I-Fraction(5,3)*J/t**2
        assert S==Fraction(4,9)*t, (t,S)
        count+=1
    return count

if __name__=='__main__':
    print('PASS',check(),'finite assertions; analytical proof is required for all dimensions.')
