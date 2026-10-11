"""Finite numerical cross-checks for geometric corner limits and extreme tails.

All mathematical limits are proved analytically; these checks do not certify them.
Requires Python 3 standard library only.
"""
import math
import random


def integrate_unit_simpson(fun, steps=4000):
    assert steps > 0 and steps % 2 == 0
    h = 1.0 / steps
    total = fun(0.0) + fun(1.0)
    for k in range(1, steps):
        total += (4 if k % 2 else 2) * fun(k * h)
    return total * h / 3.0


def tail_ratio_integral(z):
    # X+Y has Gamma(2,1) law; X/(X+Y) is uniform independently.
    def f(u):
        if u == 0.0 or u == 1.0:
            return 0.0
        t = z / (u * (1.0-u))
        return math.exp(-t) * (1.0+t)
    return integrate_unit_simpson(f)


def tail_laplace_integral(z):
    # Conditional-X integral, now put x=z+z*exp(t).
    steps = 8000
    h = 24.0 / steps
    total=0.0
    for k in range(steps+1):
        t=-12.0+k*h
        u=z*math.exp(t)
        f=u*math.exp(-u-z*z/u)
        weight=1 if k in (0,steps) else (4 if k%2 else 2)
        total += weight*f
    return math.exp(-2*z)*h*total/3.0


def corner_distance(x,y,delta):
    q = x+y
    return x*y*math.sin(delta)/math.sqrt(q*q-4*x*y*math.sin(delta/2)**2)


def independent_segment_distance(x,y,delta):
    ax,ay=x,0.0
    bx,by=-y*math.cos(delta),y*math.sin(delta)
    dx,dy=bx-ax,by-ay
    t=-(ax*dx+ay*dy)/(dx*dx+dy*dy)
    t=max(0.0,min(1.0,t))
    return math.hypot(ax+t*dx,ay+t*dy)


def run():
    checks=0
    for z in (0.15,0.4,1.0,2.5,5.0):
        a=tail_ratio_integral(z)
        b=tail_laplace_integral(z)
        assert abs(a-b) < 3e-8, (z,a,b)
        checks+=1
    for z in (10.,20.,40.):
        ratio=tail_ratio_integral(z)/(math.sqrt(math.pi*z)*math.exp(-4*z))
        assert 0.98 < ratio < 1.04, (z,ratio)
        checks+=1
    rng=random.Random(772831)
    for m in (4,5,8,15,64,500):
        delta=2*math.pi/m
        for _ in range(240):
            x=rng.expovariate(1.0)
            y=rng.expovariate(1.0)
            z=x*y/(x+y)
            d=corner_distance(x,y,delta)
            geometric=independent_segment_distance(x,y,delta)
            assert math.isclose(d,geometric,rel_tol=2e-13,abs_tol=1e-13)
            assert math.sin(delta)*z-1e-12 <= d <= 2*math.sin(delta/2)*z+1e-12
            checks+=2
    for m in (10000,100000):
        b=.25*(math.log(m)+.5*math.log(math.log(m))+.5*math.log(math.pi)-math.log(2))
        for x in (-1.,0.,1.):
            z=b+x/4
            s=tail_ratio_integral(z)
            cdf=math.exp(m*math.log1p(-s))
            gumbel=math.exp(-math.exp(-x))
            assert abs(cdf-gumbel)<.06, (m,x,cdf,gumbel)
            checks+=1
    print(f'VERIFY_OK {checks} finite checks')


if __name__=='__main__':
    run()
