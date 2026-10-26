#!/usr/bin/env python3
"""Independent numerical corroboration for the positive spectral-jump zero law.

Dependencies: Python 3 and scipy. This script checks explicit two-arc spectral
models, not the infinite-dimensional theorem. Repeated with different jump
ratios, two boundary interfaces and three boundary scales.
"""
import math
import cmath
from scipy.integrate import quad

pi=math.pi

def field(r, theta, upper=1.0, lower=2.0):
    z=r*cmath.exp(1j*theta)
    contrast=upper-lower
    u=(upper+lower)/2 + contrast/pi*cmath.log((1+z)/(1-z)).imag
    du_dr=contrast/pi*(2*cmath.exp(1j*theta)/(1-z*z)).imag
    gradient2=4*contrast**2/(pi*pi*abs(1-z*z)**2)
    return u,du_dr,gradient2

def integrate_circle(func):
    bounds=[-pi,-pi/2,0,pi/2,pi]
    return sum(quad(func,a,b,epsabs=3e-9,epsrel=2e-9,limit=400)[0]
               for a,b in zip(bounds[:-1],bounds[1:]))

def checks(upper,lower):
    assert upper>0 and lower>0
    delta=upper-lower
    c=2*delta**2/(4*pi*pi*upper*lower)
    Ie=2*delta**2/(pi*upper*lower)
    # The contrast-free limit has zero correction.
    if delta == 0:
        for r in [0.12,0.78,0.995]:
            u,du,g2=field(r,0.4,upper,lower)
            assert abs(du)<1e-15 and abs(g2)<1e-15
        return 6
    ncheck=0
    for eps in [0.02,0.005,0.001]:
        r=1-eps
        E=integrate_circle(lambda t: field(r,t,upper,lower)[2]/field(r,t,upper,lower)[0]**2)
        assert abs(eps*E/Ie - 1) < 0.035
        ncheck+=1
        for x in [-2.,-0.3,0.,0.7,3.]:
            for theta0,wm,wp in [(0.,lower,upper),(pi,upper,lower)]:
                theta=theta0+eps*x
                u,_,g2=field(r,theta,upper,lower)
                calculated=1-(1-r*r)**2*g2/(4*u*u)
                W=wm+(wp-wm)*(0.5+math.atan(x)/pi)
                predicted=1-(wp-wm)**2/(pi*pi*(1+x*x)*W*W)
                assert abs(calculated-predicted)<0.045
                ncheck+=1
    # Integrated deficit: coefficient times log(1/epsilon), plus a bounded term.
    residuals=[]
    for eps in [0.03,0.01,0.003,0.001]:
        r=1-eps
        mean_deriv=integrate_circle(lambda t: field(r,t,upper,lower)[1]/field(r,t,upper,lower)[0])/(2*pi)
        deficit=(r/2)*mean_deriv
        residual=deficit+c*math.log(1/eps)
        residuals.append(residual)
        assert deficit<0
        ncheck+=1
    assert abs(residuals[-1]-residuals[-2])<0.003
    ncheck+=1
    return ncheck

if __name__=='__main__':
    total=0
    for upper,lower in [(1.,2.),(1.,4.),(3.,1.),(1.,1.)]:
        num=checks(upper,lower)
        total+=num
        print(f'w_upper={upper}, w_lower={lower}: {num} assertions passed')
    print(f'PASS: {total} numerical assertions (not an infinite proof)')
