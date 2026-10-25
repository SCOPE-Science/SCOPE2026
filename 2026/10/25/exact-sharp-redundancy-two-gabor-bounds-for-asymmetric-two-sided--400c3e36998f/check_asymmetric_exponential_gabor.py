"""Supplementary numerical and rational-identity checks for the stated Gabor formula.

The analytic proof, not these finite tests, establishes the all-parameter theorem.
Run with Python 3 and the standard library.
"""
from fractions import Fraction
from math import exp, log, sqrt, pi, isclose
import cmath


def analytic(a, b):
    r, s = exp(-a), exp(-b)
    d = 1 / (1 + r * r)
    e = 1 / (1 + s * s)
    h = (r + s) / ((1 + r * r) * (1 + s * s))
    t = ((b - a) * h + sqrt((b - a)**2 * h*h + 4*a*b*d*e)) / (2*b*e)
    x = log(t / s) / (a + b)
    u, v = exp(-a*x), exp(-b*(1-x))
    lower = 2*(d*u*u + e*v*v - 2*h*u*v)
    upper = (1/(1-r)+s/(1-s))**2 + (1/(1+r)-s/(1+s))**2
    return lower, upper, x


def symbol(a, b, x, omega):
    r, s = exp(-a), exp(-b)
    def zak(freq):
        z = cmath.exp(2j*pi*freq)
        return exp(-a*x)/(1-r/z) + exp(-b*(1-x))*z/(1-s*z)
    return abs(zak(omega))**2 + abs(zak(omega+0.5))**2


for ir in range(1,9):
    for js in range(1,9):
        a = 0.08 + ir*0.37
        b = 0.11 + js*0.29
        low, up, xstar = analytic(a,b)
        assert 0 < xstar < 1 and 0 < low < up
        assert isclose(low, symbol(a,b,xstar,0.25), rel_tol=4e-13, abs_tol=1e-13)
        assert isclose(up, symbol(a,b,0.,0.), rel_tol=4e-13, abs_tol=1e-13)
        assert isclose(up, symbol(a,b,1.,0.), rel_tol=4e-13, abs_tol=1e-13)
        assert isclose(symbol(a,b,0.,0.25),symbol(a,b,1.,0.25),rel_tol=4e-13,abs_tol=1e-13)
        # These grids sample all Zak phases and a range of spatial fibers.
        for k in range(21):
            x = k/20
            for ell in range(41):
                omega = ell/80
                val = symbol(a,b,x,omega)
                assert low-5e-10 <= val <= up+5e-10, (a,b,x,omega,val,low,up)

# Exact rational identities for the two end fibers and the Gram determinant.
for i in range(2,9):
    for j in range(2,9):
        r, s = Fraction(1,i), Fraction(1,j)
        d = 1/(1+r*r); e=1/(1+s*s)
        h=(r+s)/((1+r*r)*(1+s*s))
        assert d*e-h*h == (1-r*s)**2/((1+r*r)**2*(1+s*s)**2)
        f0=2*(d+e*s*s-2*h*s)
        f1=2*(d*r*r+e-2*h*r)
        assert f0 == f1 == 2*(1-r*s)**2/((1+r*r)*(1+s*s))
        z0=(1/(1-r)+s/(1-s))**2+(1/(1+r)-s/(1+s))**2
        z1=(r/(1-r)+1/(1-s))**2+(r/(1+r)-1/(1+s))**2
        assert z0 == z1

print('CHECK_OK: 64 two-parameter grids; 49 exact rational determinant/end-fiber checks')
