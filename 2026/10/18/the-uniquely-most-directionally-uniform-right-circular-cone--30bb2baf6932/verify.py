"""Reproducibility checks for the directional-width cone minimizer.

Run with: python3 verify.py
Python standard library only. Analytic inequalities are proved in RESULT.md;
finite checks here do not replace the proof.
"""

import math
from fractions import Fraction


def width(z, t):
    a = math.sqrt(max(0.0, 1.0 - z*z))
    return a + max(a, t*z)


def first(t):
    return (math.pi + t - math.atan(t)) / 2.0


def second(t):
    q = 1.0 + t*t
    return (t*t + 2.0 + 2.0*(t*t + 3.0)/math.sqrt(q)) / 3.0


def cv_squared(t):
    mean = first(t)
    return second(t)/(mean*mean) - 1.0


def t_function(t):
    q = 1.0 + t*t
    a = q**1.5 + t*t - 1.0
    b = t*(t*t+2.0)*math.sqrt(q) + 2.0*t*(t*t+3.0)
    return math.atan(t) + b/a - t


def t_derivative(t):
    y = t*t
    q = 1.0 + y
    a = q**1.5 + y - 1.0
    p = y**3 - 6*y*y - 15*y - 4
    r = 9*y**3 + 16*y*y + 3*y - 4
    return (math.sqrt(q)*p - r)/(q**1.5*a*a)


def simpson(f, n=8192):
    assert n%2 == 0
    h = 1.0/n
    total = f(0.0) + f(1.0)
    for i in range(1, n):
        total += (4 if i%2 else 2)*f(i*h)
    return total*h/3.0


def root_bisect():
    low, high = 1.0, 3.0
    assert t_function(low) > math.pi > t_function(high)
    for _ in range(110):
        mid = (low+high)/2
        if t_function(mid) > math.pi:
            low = mid
        else:
            high = mid
    return (low+high)/2


def check():
    total = 0
    for t in [0.001,0.1,0.5,1.0,1.1,1.25,1.5,
              1.65,1.7090130666055156,math.sqrt(3),1.9,2.0,3.0,5.0,12.0,100.0]:
        mu1 = simpson(lambda z: width(z,t))
        mu2 = simpson(lambda z: width(z,t)**2)
        assert abs(mu1 - first(t)) < 1.0e-6 * max(1.0,mu1)
        assert abs(mu2 - second(t)) < 1.0e-6 * max(1.0,mu2)
        total += 2
    for i in range(1,500):
        t = 0.015 + i*(2.985/500)
        h = 1e-5
        fd = (t_function(t+h) - t_function(t-h))/(2*h)
        assert abs(fd - t_derivative(t)) < 2e-5 * max(1.0,abs(fd))
        assert t_derivative(t) < 0
        total += 2
    # Rigorously check the two polynomial-dominance expressions
    # used in the proof; the proof itself holds for every real y>0.
    for i in range(1,100):
        y = Fraction(9*i,100)
        p = y**3-6*y*y-15*y-4
        r = 9*y**3+16*y*y+3*y-4
        if p <= 0:
            assert p-r < 0
        else:
            assert 4*p-r < 0
        total += 1
    opt = root_bisect()
    assert abs(opt - 1.7090130666055156) < 3e-13
    assert 1.0 < opt < math.sqrt(3)
    assert abs(cv_squared(opt)-0.001686966078316204) < 1e-12
    assert cv_squared(opt) < cv_squared(math.sqrt(3))
    total += 4
    # Verify that the derivative of the normalized variance has the
    # algebraic sign predicted by the exact stationarity reduction.
    for i in range(1,401):
        t = 0.1 + i*0.022
        h = 1e-5
        diff = (cv_squared(t+h)-cv_squared(t-h))/(2*h)
        q = 1.0+t*t
        a = math.pi+t-math.atan(t)
        aa = q**1.5+t*t-1.0
        analytic = (8*t*aa/(3*a**3*q**1.5))*(math.pi-t_function(t))
        assert abs(diff-analytic) < 2e-8 * max(1.0,abs(analytic))
        total += 1
    print('VERIFY_OK',total)
    print('optimal_height_radius_ratio',format(opt,'.16f'))
    print('minimal_squared_relative_width_variance',format(cv_squared(opt),'.16f'))
    print('minimal_coefficient_of_variation',format(math.sqrt(cv_squared(opt)),'.16f'))
    print('worst_case_width_ratio_minimizer',format(math.sqrt(3),'.16f'))


if __name__ == '__main__':
    check()
