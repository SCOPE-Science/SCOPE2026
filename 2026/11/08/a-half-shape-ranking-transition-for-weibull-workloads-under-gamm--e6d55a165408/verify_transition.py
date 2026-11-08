#!/usr/bin/env python3
"""Finite and numerical checks for Weibull workload/Gamma service rank transition.
All experiments support the proof but do not certify asymptotic assertions.
"""
import math, random


def norm_tail(x):
    return .5*math.erfc(x/math.sqrt(2))


def exact_A(g):
    return math.exp(.125-g/2)*norm_tail(g-.5)-norm_tail(g)


def simpson(f, a, b, steps):
    h=(b-a)/steps
    return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,steps,2))
                +2*sum(f(a+i*h) for i in range(2,steps,2)))


def critical_probability():
    return simpson(lambda g: math.exp(-g*g/2)/math.sqrt(2*math.pi)/(1+exact_A(g)), -11,11,4000)


def verify():
    checks=0
    # Compare the equivalent integral and closed expression for A(g).
    for g in [-4,-2,-.7,0,.5,2,4]:
        # Make the exponentially small Gaussian tail integrable over [0, 12].
        v=simpson(lambda x: math.exp(x)*norm_tail(g+2*x),0,12,2000)
        assert abs(v-exact_A(g))<3e-7, (g,v,exact_A(g))
        checks+=1
    # Gamma upper-tail Chernoff rate comparison (deterministic calculus check).
    for k in range(1,51):
        for j in range(1,61):
            t=k*(1+j/15)
            rate=t-k-k*math.log(t/k)
            assert rate+1e-12 >= (t-k)**2/(2*t)
            checks+=1
    p=critical_probability()
    assert .74440<p<.74443,p
    checks+=1
    # The exact asymptotic critical PPP formula is also sampled independently.
    rng=random.Random(175367)
    agreements=0
    runs=18000
    for _ in range(runs):
        # PPP on z >= -5: N~Poisson(e^5) by inverse gap construction
        z=-5.0
        top_z=(-1e10,-1e10)
        top_s=(-1e10,-1e10)
        # transform PPP intensity e^-z dz into homogeneous Poisson in u=e^-z;
        # point coordinates in u in (0,e^5), sampled by Poisson spacings.
        u=0.0
        best_z=None
        best_s=None
        imax_z=None
        imax_s=None
        i=0
        while True:
            u += rng.expovariate(1.0)
            if u>math.exp(5):
                break
            z=-math.log(u)
            score=z+.5*rng.gauss(0,1)
            if best_z is None or z>best_z:
                best_z=z; imax_z=i
            if best_s is None or score>best_s:
                best_s=score; imax_s=i
            i+=1
        agreements+=(imax_z==imax_s)
    empirical=agreements/runs
    assert abs(empirical-p)<.022,(empirical,p)
    checks+=1
    print(f"FINITE_CHECKS_OK={checks} integral_p={p:.12f} PPP_sim={empirical:.5f}")


if __name__=='__main__':
    verify()
