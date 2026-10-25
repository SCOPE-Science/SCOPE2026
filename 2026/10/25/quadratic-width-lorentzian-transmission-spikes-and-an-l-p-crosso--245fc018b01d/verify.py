"""Reproducibility checks for the two-pendant transmission boundary layer.

Requires Python 3, NumPy and SciPy. All frequencies are dimensionless with
pendant length ell=1 and Robin ratio alpha/beta=1. The asymptotic proof is
analytic; these finite-resolution checks do not certify infinite limits.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma

PI = math.pi


def transmit(x, phase):
    sin1 = math.sin(x-phase)
    cos1 = math.cos(x-phase)
    sin3 = math.sin(3*x-phase)
    a = sin1**4
    b = 4*cos1*cos1*sin3*sin3
    return a/(a+b) if a+b > 1e-30 else 0.0


def derivative(x):
    s, c = math.sin(x), math.cos(x)
    y = s*s
    den = y + 4*c*c*(3-4*y)**2
    return 8*s*c*(3-4*y)*(6*y-5)/den**2


def regular_constant(p):
    return quad(lambda x: abs(derivative(x))**p,
                -PI/2, PI/2, epsabs=2e-12, limit=200)[0]


def spike_constant(p):
    return (2/27)*math.sqrt(PI)*gamma(p-0.5)/gamma(p)


def data(n):
    kappa = (n+0.5)*PI
    delta = math.atan(1/kappa)
    phase = lambda x: math.atan(1/(kappa+x))
    center = brentq(lambda x: 3*x-phase(x), 0, 0.6*delta)
    half_width = 2*delta*delta/27
    return delta, phase, center, half_width


def error_integral(n, p):
    delta, phase, center, w = data(n)
    def integrand(x):
        return abs(transmit(x,phase(x))-transmit(x,0.0))**p
    points = [-PI/2, -1., -0.5, -0.1, 0., 0.1, 0.5, 1., PI/2]
    for scale in [-100, -10, -1, 0, 1, 10, 100]:
        points.append(center+scale*w)
    points = sorted(x for x in set(points) if -PI/2 <= x <= PI/2)
    return sum(quad(integrand, left, right, epsabs=1e-14,
                    epsrel=2e-9, limit=250)[0]
               for left,right in zip(points,points[1:]))


def threshold_width(n, eps):
    delta, phase, center, w = data(n)
    def signal(x):
        return transmit(x,phase(x))-transmit(x,0)-eps
    left = brentq(signal, center-20*w, center)
    right = brentq(signal, center, center+20*w)
    return right-left


def main():
    for x in [-1.2,-0.7,-0.1,0.1,0.6,1.2]:
        h=1e-6
        num=(transmit(x,h)-transmit(x,-h))/(2*h)
        assert abs(num-derivative(x))<4e-8, (x,num,derivative(x))
    checks=6
    for n in [20,100,400]:
        delta, phase, center, w = data(n)
        assert abs(3*center-phase(center))<1e-12
        assert abs(transmit(center,phase(center))-1)<1e-11
        for u in [-3,-1,0,1,3]:
            x=center+w*u
            near=transmit(x,phase(x))
            assert abs(near-1/(1+u*u))<0.08, (n,u,near)
            checks+=1
        for eps in [0.25,0.5,0.75]:
            measured=threshold_width(n,eps)
            expected=2*w*math.sqrt(1/eps-1)
            assert abs(measured/expected-1)<0.004, (n,eps,measured,expected)
            checks+=1
        for p in [1,2,4]:
            integral=error_integral(n,p)
            predicted=regular_constant(p)*delta**p + spike_constant(p)*delta**2
            assert abs(integral/predicted-1)<0.004, (n,p,integral,predicted)
            checks+=1
    print(f"PASS: {checks} derivative, resonance, Lorentzian, threshold and norm checks")
    print("Illustrative regular G_2 and Lorentzian L_2:",
          regular_constant(2),spike_constant(2))

if __name__=='__main__':
    main()
