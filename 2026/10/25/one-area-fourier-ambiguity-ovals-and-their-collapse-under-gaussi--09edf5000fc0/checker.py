"""Independent quadrature and geometry checks for a two-Gaussian ambiguity formula.

Run with: python checker.py  (requires scipy and numpy).
The mathematical proof, including the all-parameter area identity, is analytical.
"""
import math
import numpy as np
from scipy.integrate import quad


def gaussian(t, a, r, sigma):
    return math.exp(-((t - a) / sigma) ** 2 / 2) + r * math.exp(-((t + a) / sigma) ** 2 / 2)


def closed_form(T, nu, a, r, sigma):
    z = 2 * math.pi * a * nu
    u = a * T / sigma**2
    c = math.exp(-a*a/sigma**2)
    pref = math.sqrt(math.pi)*sigma*math.exp(-T*T/(4*sigma**2)-math.pi**2*sigma**2*nu**2)
    return pref * (complex(math.cos(z), -math.sin(z))
                    + r*r*complex(math.cos(z), math.sin(z))
                    + 2*r*c*math.cosh(u))


def integral(T, nu, a, r, sigma):
    xmax = a + abs(T)/2 + 14*sigma
    def value(x):
        return gaussian(x+T/2,a,r,sigma)*gaussian(x-T/2,a,r,sigma)
    re = quad(lambda x: value(x)*math.cos(2*math.pi*nu*x),-xmax,xmax,epsabs=2e-12,epsrel=2e-12,limit=400)[0]
    im = quad(lambda x: -value(x)*math.sin(2*math.pi*nu*x),-xmax,xmax,epsabs=2e-12,epsrel=2e-12,limit=400)[0]
    return complex(re,im)


def lobe_area(a,sigma):
    c = math.exp(-a*a/sigma**2)
    U = math.acosh(1/c)
    def f(u):
        return math.acos(min(1.0, c*math.cosh(u)))
    uv_area = 4 * quad(f,0,U,epsabs=2e-12,limit=300)[0]
    return uv_area*sigma**2/(2*math.pi*a*a)


# Independent quadrature comparison away from zeros.
cases = [
    (0.2,0.14,0.8,1.0,1.0),
    (-0.5,0.39,1.2,2.0,0.9),
    (0.7,-0.12,0.7,0.5,1.3),
    (1.1,0.52,0.5,1.8,0.8),
    (0.1,0.71,1.0,0.3,1.2),
    (1.0,0.2,0.6,1.1,1.5),
    (-0.4,0.11,0.9,2.5,0.7),
    (0.9,-0.41,1.1,0.9,1.1),
]
max_abs_diff = 0
for args in cases:
    v1=integral(*args)
    v2=closed_form(*args)
    d=abs(v1-v2)
    max_abs_diff=max(d,max_abs_diff)
    assert d < 2e-10,(args,v1,v2,d)
print('independent_gaussian_integrals',len(cases),'max_abs_diff',f'{max_abs_diff:.3e}')

# Equal-weight lobe area: phase-space coordinates are (delay, cycles-frequency).
max_area_err=0
for a,sigma in [(0.25,0.8),(0.6,1),(0.9,1.4),(1.3,0.8),(1.8,1.5),(2.3,1.0),(3.4,1.2)]:
    S=lobe_area(a,sigma)
    err=abs(S-1)
    max_area_err=max(max_area_err,err)
    assert err<2e-10, (a,sigma,S)
print('balanced_loop_areas',7,'max_error_from_one',f'{max_area_err:.3e}')

# Amplitude imbalance: two regular isolated zeros at each odd frequency line.
zero_cases=[(0.5,1.5,1.0),(0.75,2.0,0.9),(1.0,0.65,1.1),(1.35,2.3,1.25)]
max_zero_resid=0
for a,r,sigma in zero_cases:
    U=math.acosh(math.exp(a*a/sigma**2)*(r+1/r)/2)
    for sign in [-1,1]:
        T=sign*sigma**2*U/a
        for k in [-1,0,1]:
            nu=(2*k+1)/(2*a)
            z=closed_form(T,nu,a,r,sigma)
            direct=integral(T,nu,a,r,sigma)
            max_zero_resid=max(max_zero_resid,abs(z),abs(direct))
            assert abs(z)<3e-14,(a,r,sigma,k,sign,z)
            assert abs(direct)<3e-10,(a,r,sigma,k,sign,direct)
            # The exact real-imag Jacobian has opposite signs at the two tips.
            J=-4*math.pi*r*math.exp(-a*a/sigma**2)*(a*a/sigma**2)*(r*r-1)*math.sinh(sign*U)
            assert J !=0
            assert (J>0)==((-sign*(r*r-1))>0)
print('imbalanced_isolated_zeros',len(zero_cases)*2*3,'max_abs_residual',f'{max_zero_resid:.3e}')

# Nonzeros near the isolated zeros, including in the complex direction.
a,r,sigma=1.0,1.7,1.0
U=math.acosh(math.exp(a*a)*(r+1/r)/2)
T=U/a; nu=1/(2*a)
for deltaT,deltaNu in [(0.03,0),(0,-0.02),(-0.02,0.01)]:
    assert abs(closed_form(T+deltaT,nu+deltaNu,a,r,sigma))>1e-6
print('neighbor_nonzero_cases',3)
print('CHECKS PASSED')
