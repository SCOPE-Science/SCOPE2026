"""Numerical checks for local spatial cusp coefficients in a two-dimensional inertial particle.

Requires Python 3, numpy, scipy.  Uses independent exact finite-time Gaussian
conditional covariances and linear-response differentiation, rather than the
asymptotic proof. No simulation is used as a substitute for that proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

M, R, W = 1.3, 1.4, 0.8
C = 2.0 / (3.0 * M*M)
A = R*gamma(2.0/3.0)/(3.0*math.pi*(2.0*C)**(1.0/3.0))
B0 = R*M/(4.0*math.pi)  # derivative of anisotropic cusp coefficient in activity
D = R/(2.0*math.sqrt(2.0*math.pi)*W)


def variance(t):
    x=t/M
    if x < 0.05:
        # Exact Taylor series through ninth order of twice the OU-integrated variance.
        poly=(x**3/3 - x**4/4 + 7*x**5/60 - x**6/24
              + 31*x**7/2520 - x**8/320 + 127*x**9/181440)
        return 2*M*poly
    return 2*(t + 2*M*math.expm1(-x) - 0.5*M*math.expm1(-2*x))


def inertial_transfer(t):
    return -M*math.expm1(-t/M)


def first_heading_response(t):
    """Exact E[integrated orientation forcing] per unit propulsion strength."""
    if t < 0.1:
        v=0.0
        for k in range(12):
            v += (-1)**k*t**(k+2)/math.factorial(k+2)*sum(M**(-j) for j in range(k+1))/M
        return v
    if abs(M-1.0) < 1e-12:
        return -math.expm1(-t)-t*math.exp(-t)
    return (-math.expm1(-t)
            - (math.exp(-t)-math.exp(-t/M))/(1.0/M-1.0))


def integrate_by_age(func, scale):
    # Split near the critical short-time scale so quadrature resolves the cusp.
    pts=sorted(set([0.,.1*scale,.5*scale,scale,3*scale,
                    12*scale,max(1.,80*scale),40.]))
    return sum(quad(func,l,r,epsabs=1e-9,epsrel=1e-10,limit=200)[0]
               for l,r in zip(pts[:-1],pts[1:]))


def passive_zero(s):
    def g(t):
        v=variance(t)
        if v<=0: return 0.0
        return R*math.exp(-R*t-s*s/(2*v))/(2*math.pi*v)
    return integrate_by_age(g,s**(2./3.))


def passive_maxwell(s):
    def g(t):
        v=variance(t)+W*W*inertial_transfer(t)**2
        if v<=0: return 0.0
        return R*math.exp(-R*t-s*s/(2*v))/(2*math.pi*v)
    return integrate_by_age(g,s)


def active_linear_response(s):
    # d/dPe f(s e1) evaluated at Pe=0, with rotational Brownian noise.
    # E[(cos theta_t,sin theta_t)]=(exp(-t),0) for dtheta=sqrt(2)dW.
    def g(t):
        v=variance(t)
        if v<=0: return 0.0
        return (R*math.exp(-R*t-s*s/(2*v))/(2*math.pi*v)
                *s*first_heading_response(t)/v)
    return integrate_by_age(g,s**(2./3.))


def main():
    print('parameters M,R,W=', M,R,W)
    print('analytic cusp coefficients:',A,B0,D)
    errors=[]
    for s in [0.01,0.003,0.001,0.0003,0.0001]:
        numA=passive_zero(s)*s**(4./3.)
        numB=active_linear_response(s)*s
        numD=passive_maxwell(s)*s
        errors.append([abs(numA/A-1),abs(numB/B0-1),abs(numD/D-1)])
        print(f's={s:.4g} zero={numA:.10f} response={numB:.10f} Maxwell={numD:.10f}')
    # All three normalized differences decrease monotonically along this test grid.
    for col in range(3):
        assert all(errors[k+1][col]<errors[k][col] for k in range(len(errors)-1))
        assert errors[-1][col]<0.012, (col,errors[-1][col])
    print('PASS: all three limiting coefficients approach their analytical values.')

if __name__=='__main__':
    main()
