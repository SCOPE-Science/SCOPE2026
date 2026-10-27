#!/usr/bin/env python3
"""Independent numerical spot checks for a derived Toeplitz limit-body formula.

These tests evaluate only finite samples. The uniform-in-parameter convergence,
convex-hull identity, and uniqueness of the limiting maximizer are analytical.
"""
from math import cosh, sinh, tanh, sqrt, isclose


def ellipse(p, v):
    assert p > 1 and p != 2 and v >= 0
    d = abs(p-2)/p
    return (2*cosh(d*v)/cosh(v),
            2*sinh(d*v)/(abs(p-2)*cosh(v)))


def limiting_ellipse(v):
    return 2/cosh(v), v/cosh(v)


def support_exact(p, a, b, steps=30000, vmax=20):
    out = 0
    for k in range(steps+1):
        v = vmax*k/steps
        x,y=ellipse(p,v)
        out=max(out, sqrt((a*x)**2+(b*y)**2))
    return out


def support_limit(a,b,steps=30000,vmax=20):
    out = 0
    v_at=0
    for k in range(steps+1):
        v=vmax*k/steps
        x,y=limiting_ellipse(v)
        h=sqrt((a*x)**2+(b*y)**2)
        if h>out:
            out=h;v_at=v
    return out,v_at


def root_bisect(f,lo,hi):
    assert f(lo)*f(hi)<0
    for _ in range(120):
        m=(lo+hi)/2
        if f(lo)*f(m)<=0:hi=m
        else:lo=m
    return (lo+hi)/2


def test():
    count=0
    for p in (1.9,1.99,1.999,2.001,2.01,2.1):
        for v in (0.0,0.1,0.4,1.0,2.0,3.5,7):
            ax,ay=ellipse(p,v)
            # Directly evaluate source ellipse via r^p+s^p=1.
            r=__import__('math').exp(v/p)/(2*cosh(v))**(1/p)
            s=__import__('math').exp(-v/p)/(2*cosh(v))**(1/p)
            assert isclose(r**p+s**p,1.0,abs_tol=1e-12)
            direct_a=2*(r*s**(p-1)+s*r**(p-1))
            direct_b=2*abs(r*s**(p-1)-s*r**(p-1))/abs(p-2)
            assert isclose(ax,direct_a,abs_tol=3e-12,rel_tol=3e-12)
            assert isclose(ay,direct_b,abs_tol=3e-12,rel_tol=3e-12)
            count+=3
    for a,b in ((1,0),(1,0.8),(1,1.5),(1,2),(1,2.001),(1,3),(0,1),(0.1,1)):
        h,v=support_limit(a,b)
        if abs(b) <= 2*abs(a):
            assert abs(h-2*abs(a)) < 1e-8
            assert v==0
        else:
            assert v>0 and h>2*abs(a)
        count+=2
    # Sharp finite-exponent supporting-normal threshold for the point (2,0).
    # A norming vector (a,b) has maximum exactly 2|a| iff
    # |b| <= 2 |a| sqrt(1 - delta**2), delta = |1-2/p|.
    for p in (1.2,1.5,1.8,1.95,2.05,2.5,3,5,10):
        delta=abs(1-2/p)
        critical=2*sqrt(1-delta**2)
        for ratio in (0.0,critical*0.99,critical,critical*1.01,critical*1.3):
            # A tiny quadratic gain above threshold can escape coarse grids;
            # optimize continuously by golden-section search on [0,10].
            def fun(v):
                x,y=2*cosh(delta*v)/cosh(v),sinh(delta*v)/(delta*cosh(v))
                return sqrt(x*x+ratio*ratio*y*y)
            lo,hi=0.0,10.0
            for _ in range(160):
                a0=lo+0.381966011250105*(hi-lo)
                b0=hi-0.381966011250105*(hi-lo)
                if fun(a0)>fun(b0):hi=b0
                else:lo=a0
            peak=max(2.0,fun((lo+hi)/2))
            if ratio<=critical:
                assert abs(peak-2)<3e-12, (p,ratio,peak)
            else:
                assert peak>2+1e-10, (p,ratio,peak)
            count+=1
    z0=root_bisect(lambda z:z*tanh(z)-1,0.1,5.0)
    c=z0/cosh(z0)
    assert abs(z0-1.199678640257734)<1e-13
    assert abs(c-0.6627434193491816)<3e-14
    for p in (1.99,1.999,2.001,2.01):
        for a,b in ((1,0.5),(1,2),(1,2.5),(0,1)):
            ex=support_exact(p,a,b,steps=5000)
            li,_=support_limit(a,b,steps=5000)
            assert abs(ex-li)<0.045
            count+=1
    print('PASS',count,'finite numerical checks; critical root',format(z0,'.15f'), 'height',format(c,'.15f'))


if __name__=='__main__':
    test()
