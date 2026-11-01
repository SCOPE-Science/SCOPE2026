#!/usr/bin/env python3
"""Numerical checks of boundary-point near-diameter asymptotics on ellipses.
Run with python3 check_ellipse.py. Only SciPy and NumPy are required.
"""
from math import pi, sqrt, acos, sin, cos, asin
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipe, ellipk


def model_tail(delta, epsilon, a=1.):
    # Semi-minor axis b=a*sqrt(1-delta), and epsilon is an absolute distance deficit.
    assert 0<=delta<1 and 0<epsilon<.5*a
    b=a*sqrt(1-delta)
    perimeter=4*a*ellipe(delta)
    h=epsilon/a
    # At a phase phi, the exact distance is 2a*cos(v/2)*sqrt(1-delta*sin(phi)^2).
    # Integrate only phi near the rightmost / leftmost major-axis poles when needed.
    cutoff=(h-h*h/4)/delta if delta else 2.
    phi_max=pi/2 if cutoff>=1 else asin(sqrt(cutoff))
    def gauss_integrate(phi):
        z=sqrt(max(0.,1-delta*sin(phi)**2))
        if z<=1-h/2: return 0.
        vmax=2*acos(min(1.,(1-h/2)/z))
        def w(v):
            speed1=a*sqrt(1-delta*cos(phi-v/2)**2)
            speed2=a*sqrt(1-delta*cos(phi+v/2)**2)
            return speed1*speed2
        return quad(w, -vmax, vmax, epsabs=4e-12)[0]
    # 4 symmetric intervals of length phi_max, overall phi in [0,2pi].
    num=4*quad(gauss_integrate, 0, phi_max, epsabs=1e-11,epsrel=1e-10,limit=120)[0]
    return num/perimeter**2

def crossover(lam):
    if lam==0: return 2/pi
    if lam <= 1: return 4*ellipe(lam)/pi**2
    m=1/lam
    return 4*sqrt(lam)*(ellipe(m)-(1-m)*ellipk(m))/pi**2

def tail_coefficient(delta,a=1.):
    b=a*sqrt(1-delta)
    P=4*a*ellipe(delta)
    return 4*pi*b*b/(a*P**2*sqrt(delta))

def main():
    count=0
    for lam in (0.,.2,.5,.9,1.,1.1,1.5,3.,10.):
        eps=2.e-5
        f=model_tail(lam*eps,eps)/sqrt(eps)
        g=crossover(lam)
        relative=abs(f/g-1)
        assert relative < 2.5e-4, (lam,f,g,relative)
        print('CROSS',lam,f,g,'relative_error',relative)
        count+=1
    for delta in (.1,.36,.75):
        eps=3e-6
        f=model_tail(delta,eps)/eps
        g=tail_coefficient(delta)
        relative=abs(f/g-1)
        assert relative < 4e-4,(delta,f,g,relative)
        print('FIXED',delta,f,g,'relative_error',relative)
        count+=1
    for h in (1e-3,1e-4,1e-5):
        true=crossover(1+h)*pi**2
        approx=4+h*np.log(h)+(1-np.log(16))*h
        relative=abs(true-approx)
        assert relative < 1.0*h*h*abs(np.log(h)),(h,true,approx,relative)
        print('CUSP',h,true,approx,'error',relative)
        count+=1
    print('VERIFY_OK cases=',count)

if __name__=='__main__': main()
