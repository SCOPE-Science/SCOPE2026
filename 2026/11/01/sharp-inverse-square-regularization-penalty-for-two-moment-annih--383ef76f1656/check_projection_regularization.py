#!/usr/bin/env python3
"""Independent numerical checks of the stated moment-projection formulas.

No finite list of tests proves the all-K asymptotic or operator claims.
Run: python3 check_projection_regularization.py
Only the Python standard library is required.
"""
import math


def p0(r):
    return r * math.asinh(1.0 / r)


def q0(r):
    return (1.0 + math.hypot(1.0, r) - r*r*math.asinh(1.0/r)) / 2.0


def phi(a, b):
    a, b = abs(a), abs(b)
    if a >= b:
        return a
    return (a*a+b*b)/(2.0*b)


def bisect_zero(fun, low, high, n=85):
    fl = fun(low)
    fh = fun(high)
    assert fl * fh < 0.0, (low, high, fl, fh)
    for _ in range(n):
        mid = (low+high)/2.0
        fm = fun(mid)
        if fm * fl > 0.0:
            low, fl = mid, fm
        else:
            high = mid
    return (low + high)/2.0


def cross(r, k):
    mass = 1.0/p0(r)
    return bisect_zero(
        lambda t:mass*(1.0+t/math.hypot(r,t))-k*t,
        0.0, 1.0)


def simpson(fun, a, b, n=512):
    assert n % 2 == 0
    dx = (b-a)/n
    s = fun(a)+fun(b)
    for j in range(1,n):
        s += (4 if j%2 else 2)*fun(a+j*dx)
    return dx*s/3.0


def deficit(r,k):
    mass=1.0/p0(r)
    t=cross(r,k)
    return (t*t/2.0
            + simpson(lambda x:x*x/math.hypot(r,x),0,t)
            - (k/mass)*t**3/3.0)


def r_for_k(k):
    return bisect_zero(lambda r:q0(r)-p0(r)-deficit(r,k),0.5,1.0)


def main():
    tested = 0
    def check(value, why):
        nonlocal tested
        assert value, why
        tested += 1

    rstar=bisect_zero(lambda r:p0(r)-q0(r),0.5,1.0)
    ell=1.0/p0(rstar)
    h=(1.0+rstar)*p0(rstar)
    coeff=ell**4/(6.0*(1.0+rstar))
    check(abs(rstar-0.7349935892425393)<1.e-13,'rstar')
    check(abs(ell-1.2204049171163608)<1.e-13,'ell')
    check(abs(coeff-0.21309176683523744)<1.e-13,'coefficient')
    check(abs(h-((1+rstar)/ell))<1.e-13,'H normalization')
    for k in [20,40,80,160,320,640]:
        r=r_for_k(k)
        mass=1.0/p0(r)
        a=lambda t:mass*r/math.hypot(r,t)
        b=lambda t: math.copysign(min(k*abs(t),mass*(1+abs(t)/math.hypot(r,abs(t)))),t)
        check(r<rstar,'root orientation')
        check(abs(mass*p0(r)-1.0)<2e-12,'zeroth moment')
        check(abs(mass*(q0(r)-deficit(r,k))-1.0)<2e-12,'first moment')
        check(abs(cross(r,k)-mass/k)<0.01,'boundary layer')
        check(abs(phi(a(0),b(0))-mass)<2e-13,'norm at origin')
        check((mass-ell)*h+1.e-12>=mass**3/(6.0*k*k),'lower bound')
        for j in range(-1250,1251):
            x=j/1250.0
            check(phi(a(x),b(x))<=mass+1e-12,'dual norm bound')
        for j in range(-1250,1250):
            x=j/1250.0
            y=(j+1)/1250.0
            check(abs(b(y)-b(x)) <= k*(y-x)+1.e-11,'Lipschitz bound')
        print('K={:4d} norm={:.12f} K^2 deficit={:.12f}'.format(k,1+mass,(mass-ell)*k*k))
    check(abs((1/p0(r_for_k(640))-ell)*640*640-coeff)<0.002,'K^-2 trend')
    # Verify the polar support identity on an independent mesh.
    for j in range(1,501):
        t=j/500.0
        u=rstar/math.hypot(rstar,t)
        v=1.0+t/math.hypot(rstar,t)
        check(abs(phi(u,v)-1)<2.e-12,'support norm')
        check(abs(rstar*u+t*v-(t+math.hypot(rstar,t)))<2.e-12,'support identity')
    print('r_star=', format(rstar,'.16g'))
    print('lambda=', format(1+ell,'.16g'))
    print('K^-2 coefficient=', format(coeff,'.16g'))
    print('Numerical assertions passed:',tested)


if __name__ == '__main__':
    main()
