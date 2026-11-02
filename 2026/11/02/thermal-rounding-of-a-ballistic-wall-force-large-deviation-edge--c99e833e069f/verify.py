#!/usr/bin/env python3
"""Reproduce exact force-imbalance identities and the thermal ballistic-edge law.

No external Python packages. Analytic theorems are given in RESULT.md; finite checks
exercise formulas and event-driven trajectories, not an infinite-domain certificate.
"""
import math
import random


def scgf(q, rate, speed, diffusivity):
    return diffusivity*q*q-rate+math.hypot(rate, speed*q)


def grad(q, rate, speed, diffusivity):
    return 2*diffusivity*q + speed*speed*q/math.hypot(rate,speed*q)


def current_rate(j, rate, speed, diffusivity):
    if diffusivity == 0:
        if abs(j) > speed:
            return math.inf
        return rate*(1-math.sqrt(max(0., 1-(j/speed)**2)))
    if j == 0:
        return 0.
    sign=1 if j>=0 else -1
    j=abs(j)
    lo=0.
    hi=1.
    while grad(hi,rate,speed,diffusivity)<j:
        hi*=2
        assert hi<1e100
    for _ in range(180):
        mid=(lo+hi)/2
        if grad(mid,rate,speed,diffusivity)<j:lo=mid
        else:hi=mid
    q=sign*(lo+hi)/2
    return q*(sign*j)-scgf(q,rate,speed,diffusivity)


def edge_scale(rate, speed, diffusivity):
    return ((rate**4*diffusivity)/(speed**2))**(1/3), ((rate**2*diffusivity**2)/speed)**(1/3)


def edge_profile(s):
    # Unique positive root of 2z - 1/(2z^2) = s.
    lo=0.
    hi=max(1.,abs(s)+2.)
    for _ in range(150):
        mid=(lo+hi)/2
        if 2*mid-1/(2*mid*mid)<s:lo=mid
        else:hi=mid
    z=(lo+hi)/2
    return s*z-z*z-1/(2*z)


def exact_reflection_path(width, speed, rate, horizon, rng):
    x0=width*rng.random()
    x=x0
    orientation=1 if rng.random()<0.5 else -1
    lower=upper=total=0.
    t=0.
    while t<horizon:
        remaining=-math.log1p(-rng.random())/rate
        dt=min(remaining,horizon-t)
        unreflected_step=speed*orientation*dt
        total+=unreflected_step
        candidate=x+unreflected_step
        if candidate>width:
            upper+=candidate-width
            x=width
        elif candidate<0:
            lower-=candidate
            x=0.
        else:x=candidate
        t+=dt
        orientation=-orientation
    # The identity is stronger than any asymptotic theorem.
    assert abs((upper-lower)-total+(x-x0)) < 1e-9*(1+abs(total))
    return upper-lower,total,x-x0


def main():
    checked=0
    rng=random.Random(724399)
    for rate,speed in [(1.,1.),(2.,3.),(0.7,1.9)]:
        for d in [0.,0.01,0.2,2.]:
            for q in [-9.,-3.,-0.1,0.,0.2,3.,12.]:
                # The spectrum of the tilted two-state generator is explicit.
                eig_plus=-rate+math.hypot(rate,speed*q)+d*q*q
                assert abs(eig_plus-scgf(q,rate,speed,d))<1e-12*(1+abs(eig_plus))
                if d>0:
                    eps=1e-5*(1+abs(q))
                    numerical=(scgf(q+eps,rate,speed,d)-scgf(q-eps,rate,speed,d))/(2*eps)
                    assert abs(grad(q,rate,speed,d)-numerical)<2e-7*(1+abs(grad(q,rate,speed,d)))
                    checked+=1
                checked+=1
            for jj in [-0.8*speed,-0.23*speed,0.,0.63*speed,0.98*speed,1.2*speed]:
                val=current_rate(jj,rate,speed,d)
                assert val>=-1e-11
                if d>0:
                    assert abs(val-current_rate(-jj,rate,speed,d))<1e-10*(1+val)
                    checked+=1
                checked+=1
        for d in [1e-4,1e-5,1e-6]:
            E,delta=edge_scale(rate,speed,d)
            assert abs((current_rate(speed,rate,speed,d)-rate)/E+3/(2**(4/3)))<0.12
            checked+=1
            for s in [-2.,-0.5,0.,1.,3.]:
                target=rate+E*edge_profile(s)
                actual=current_rate(speed+s*delta,rate,speed,d)
                assert abs(actual-target) < 0.13*E
                checked+=1
    # Exact event-driven simulation of outward-sticking telegraph reflection.
    for width in [0.25,1.,7.,19.]:
        for _ in range(320):
            s,free,dx=exact_reflection_path(width,2.,1.3,5.+rng.random()*35.,rng)
            assert abs(s-free)<=width+1e-9
            checked+=1
    print('PASS:',checked,'deterministic numerical and exact-path consistency checks')
    for d in [1e-3,1e-4,1e-5,1e-6]:
        E,delta=edge_scale(1.,1.,d)
        ratio=(current_rate(1.,1.,1.,d)-1.)/E
        print('D',d,'edge scaled deficit',round(ratio,9),'limit',round(-3/2**(4/3),9),'window',delta)
    print('Finite tests corroborate; the proof is analytical.')

if __name__=='__main__':main()
