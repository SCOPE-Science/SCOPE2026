#!/usr/bin/env python3
"""Reproduce finite consistency checks for disk advection under the cubic Hopf flow.

Python 3 standard library only. Proofs of the universal assertions are in RESULT.md.
"""
import math

PI = math.pi


def point(a, R, theta, t):
    x = a + R * math.cos(theta)
    y = R * math.sin(theta)
    s = math.expm1(2.0 * t)
    f = math.exp(t) / math.sqrt(1.0 + s * (x*x+y*y))
    return (f*x, f*y)


def exact_area(a, R, t):
    if t == 0:
        return PI*R*R
    s = math.expm1(2*t)
    k2 = math.exp(2*t)
    d = math.sqrt((1+s*(a+R)**2)*(1+s*(a-R)**2))
    return PI*k2/(2*s)*(1-(1+s*(a*a-R*R))/d)


def simpson(f, lo, hi, n=16000):
    assert n % 2 == 0
    h=(hi-lo)/n
    total=f(lo)+f(hi)
    for j in range(1,n):
        total+=(4 if j%2 else 2)*f(lo+j*h)
    return total*h/3


def area_flux(a,R,t,n=16000):
    s=math.expm1(2*t); k2=math.exp(2*t)
    return simpson(lambda th:k2*R*(R+a*math.cos(th)) /
                   (2*(1+s*(a*a+R*R+2*a*R*math.cos(th)))),0,2*PI,n)


def perimeter(a,R,t,n=16000):
    s=math.expm1(2*t);k=math.exp(t)
    def speed(th):
        x=a+R*math.cos(th);y=R*math.sin(th)
        xp=-R*math.sin(th);yp=R*math.cos(th)
        rr=x*x+y*y
        d=1+s*rr
        dot=x*xp+y*yp
        vx=k/math.sqrt(d)*(xp-s*dot*x/d)
        vy=k/math.sqrt(d)*(yp-s*dot*y/d)
        return math.hypot(vx,vy)
    return simpson(speed,0,2*PI,n)


def main():
    checks=0
    cases=((.3,.9),(.6,.6),(1.4,.8),(0.,1.))
    for a,R in cases:
        for t in (.5,1.5,3.5,5.):
            exact=exact_area(a,R,t)
            independent=area_flux(a,R,t)
            assert abs(exact-independent)<3e-8,(a,R,t,exact,independent)
            checks+=1
        target=2*PI if a<R else (PI+2 if a==R else 4*math.asin(R/a))
        p3=perimeter(a,R,3.0)
        p5=perimeter(a,R,5.0)
        assert abs(p5-target)<abs(p3-target)+2e-6,(a,R,p3,p5,target)
        assert abs(p5-target)<0.12,(a,R,p5,target)
        checks+=2
        if a<R:
            coeff=PI*(1-R*R/(R*R-a*a)**2)
            asym=PI+coeff*math.exp(-10)
            assert abs(exact_area(a,R,5)-asym)<.005,(a,R,asym)
        elif a==R:
            asym=PI/2-PI/(4*a)*math.exp(-5)
            assert abs(exact_area(a,R,5)-asym)<.003,(a,R,asym)
        else:
            asym=PI*R*R/(a*a-R*R)**2*math.exp(-10)
            assert abs(exact_area(a,R,5)-asym)<.005,(a,R,asym)
        checks+=1
    # Boundary layer: nontrivial interior points on the latent diameter.
    for u in (-2.,-.75,0.,1.5,3.):
        z=point(.6,.6,PI+u*math.exp(-7),7)
        expected=-.6*u / math.sqrt(1+.36*u*u)
        assert abs(z[0])<.006,(u,z)
        assert abs(z[1]-expected)<.006,(u,z,expected)
        checks+=2
    # Exact polar flow and radial differential signs in sampled regimes.
    for t in (.1,.7,3.,5.):
        s=math.expm1(2*t)
        for r in (.01,.2,.7,1.5,3.):
            f=math.exp(t)*r/math.sqrt(1+s*r*r)
            derivative=math.exp(t)/(1+s*r*r)**1.5
            assert f>0 and derivative>0
            assert abs(derivative*f/r-math.exp(2*t)/(1+s*r*r)**2)<1e-12
            checks+=2
    print(f'PASS: {checks} independent finite consistency assertions; standard-library Python')

if __name__=='__main__':
    main()
