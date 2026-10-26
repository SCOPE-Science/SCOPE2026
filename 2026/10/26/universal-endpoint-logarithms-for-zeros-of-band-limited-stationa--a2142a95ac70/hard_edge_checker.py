#!/usr/bin/env python3
"""Reproducible numerical checks for finite-arc spectral masks.

Requires numpy and scipy. Numerical tests illustrate, but do not establish,
the asymptotic theorem or its uniform remainder.
"""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi


def angle_map(s, r):
    return 2.0 * math.atan2((1+r)*math.sin(s/2), (1-r)*math.cos(s/2))


def poisson(s, r):
    return (1-r*r)/(1-2*r*math.cos(s)+r*r)


def spectral_u(theta, r, arcs):
    return sum((angle_map(theta-a,r)-angle_map(theta-b,r))/(2*PI) for a,b in arcs)


def derivatives(theta,r,arcs):
    ur=0.0
    uth=0.0
    for a,b in arcs:
        x,y=theta-a,theta-b
        ur += (math.sin(x)/(1-2*r*math.cos(x)+r*r)
               -math.sin(y)/(1-2*r*math.cos(y)+r*r))/PI
        uth += (poisson(x,r)-poisson(y,r))/(2*PI)
    return ur,uth


def expected_n(t,arcs):
    r=1-t
    endpoints=sorted({z for pair in arcs for z in pair})
    pts=[0.0,2*PI]
    for e in endpoints:
        for m in (-100,-25,-1,0,1,25,100):
            z=e+m*t
            if 0<z<2*PI: pts.append(z)
    pts=sorted(set(pts))
    def integrand(th):
        return derivatives(th,r,arcs)[0]/spectral_u(th,r,arcs)
    m=sum(quad(integrand,a,b,epsabs=4e-8,epsrel=2e-8,limit=200)[0]
          for a,b in zip(pts,pts[1:]))/(2*PI)
    return r*r/(1-r*r)+.5*r*m


def normalized_density(theta,r,arcs):
    u=spectral_u(theta,r,arcs)
    ur,uth=derivatives(theta,r,arcs)
    return 1-(1-r*r)**2*(ur*ur+uth*uth/(r*r))/(4*u*u)


def run():
    tests=0
    def check(test,message):
        nonlocal tests
        assert test,message
        tests+=1
    cases=[[(PI/2,3*PI/2)],[(.3,1.2),(2.1,2.75)],[(.1,5.8)]]
    for arcs in cases:
        support=sum(b-a for a,b in arcs)/(2*PI)
        J=2*len(arcs)
        c=J/(4*PI*PI)
        v1=expected_n(1e-4,arcs)
        v2=expected_n(1e-5,arcs)
        d1=v1-support/(2e-4)
        d2=v2-support/(2e-5)
        estimate=(d2-d1)/math.log(10)
        check(abs(estimate-c)<.0004,(arcs,'coefficient',estimate,c))
        check(v1>0 and v2>v1,(arcs,'nonnegative zero count'))
        remainder1=d1-c*math.log(1e4)
        remainder2=d2-c*math.log(1e5)
        check(abs(remainder1-remainder2)<.001,(arcs,'bounded remainder',remainder1,remainder2))
        for r in (.25,.5,.8):
            for th in (.2,1.0,2.3,4.6):
                u=spectral_u(th,r,arcs)
                check(0<u<1,(arcs,'Poisson harmonic measure range'))
                # Independent integral of the Poisson kernel over the spectral arcs.
                v=sum(quad(lambda ph:poisson(th-ph,r),a,b,epsabs=2e-11)[0]
                      for a,b in arcs)/(2*PI)
                check(abs(v-u)<2e-12,(arcs,'Poisson convolution',u,v))
                h=1e-6
                ur,uth=derivatives(th,r,arcs)
                check(abs((spectral_u(th,r+h,arcs)-spectral_u(th,r-h,arcs))/(2*h)-ur)<4e-8,
                      (arcs,'radial derivative'))
                check(abs((spectral_u(th+h,r,arcs)-spectral_u(th-h,r,arcs))/(2*h)-uth)<4e-8,
                      (arcs,'angular derivative'))
    # Hard-edge intensity profile at the left endpoint, where the band begins.
    a=PI/2
    arcs=cases[0]
    for x in (-4,-2,-1,0,1,2,4):
        F=.5+math.atan(x)/PI
        target=1-1/(PI*PI*(1+x*x)*F*F)
        actual=normalized_density(a+1e-5*x,1-1e-5,arcs)
        check(abs(actual-target)<.002,(x,'edge profile',actual,target))
    # Independent finite Gaussian covariance geometric-series approximation.
    for r in (.35,.55,.7):
        for th in (0.8,2.,4.2):
            z=complex(r*math.cos(th),r*math.sin(th))
            def finite_gaf_variance(ph):
                w=z*complex(math.cos(-ph),math.sin(-ph))
                s=(1-w**61)/(1-w)
                return s.real*s.real+s.imag*s.imag
            v=quad(finite_gaf_variance,PI/2,3*PI/2,epsabs=2e-10,limit=200)[0]/(2*PI)
            exact=spectral_u(th,r,arcs)/(1-r*r)
            check(abs(v-exact)<2e-9,(r,th,'finite covariance check',v,exact))
    print(f'PASS: {tests} independent numeric assertions. Logs are not proofs.')

if __name__=='__main__':
    run()
