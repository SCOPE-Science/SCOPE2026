#!/usr/bin/env python3
"""Numerical diagnostics for the cube critical-transition theorem.

Uses only the Python standard library. Numerical sampling is not proof of
Hausdorff convergence or a high-dimensional asymptotic theorem.
"""
import math
import random
from fractions import Fraction


def log_cosh(t):
    t = abs(t)
    return t + math.log1p(math.exp(-2 * t)) - math.log(2)


def integrate_simpson(f, a, b, steps=32768):
    assert steps % 2 == 0
    h = (b-a)/steps
    total = f(a)+f(b)
    for i in range(1,steps):
        total += (4 if i % 2 else 2)*f(a+i*h)
    return total*h/3


def cube_deficit_2d(p, y, steps=16384):
    a,b=y
    x0,x1=a/p,b/p
    assert max(abs(x0),abs(x1))<0.5
    def integrand(t):
        u,v=math.cos(t),math.sin(t)
        rho=.5/max(abs(u),abs(v))
        rhox=min((.5+math.copysign(x0,u))/abs(u) if abs(u)>1e-15 else math.inf,
                  (.5+math.copysign(x1,v))/abs(v) if abs(v)>1e-15 else math.inf)
        z=-p*math.log(rhox/rho)
        ell=math.log1p(math.exp(z))-math.log(2)
        diff=-math.expm1(-2*ell/p)
        return rho*rho*p*diff/2
    return integrate_simpson(integrand,0.0,2*math.pi,steps)


def orlicz_area_2d():
    xlim=math.acosh(math.e)
    def y_max(x):
        val=math.e/math.cosh(x)
        return math.acosh(max(1.0,val))
    return 4*integrate_simpson(y_max,0.0,xlim,32768)


def g(t):
    if t<1e-7:
        return 1+t/2+t*t/24
    return math.sqrt((2*t)/(-math.expm1(-2*t)))


def dirichlet_ratio_mc(n, count=18000, seed=314159):
    rand=random.Random(seed+n)
    total=0.0
    total_sq=0.0
    for _ in range(count):
        vals=[rand.gammavariate(.5,1) for i in range(n)]
        slack=rand.gammavariate(1,1)
        den=sum(vals)+slack
        weight=1.0
        for v in vals:
            weight*=g(v/den)
        total+=weight
        total_sq+=weight*weight
    mean=total/count
    error=math.sqrt(max(0.,total_sq/count-mean*mean)/count)
    return mean,error


def check_moments(n):
    alpha0=Fraction(n,2)+1
    slack=Fraction(1,1)/alpha0
    sqsum=Fraction(n,1)*Fraction(3,4)/(alpha0*(alpha0+1))
    assert slack==Fraction(2,n+2)
    assert sqsum==Fraction(3*n,(n+2)*(n+4))


def main():
    checks=0
    for n in range(1,501):
        check_moments(n)
        checks+=2
    expected=log_cosh(.8)+log_cosh(.25)
    vals=[cube_deficit_2d(p,(.8,.25)) for p in (100,250,800)]
    diffs=[abs(v-expected) for v in vals]
    assert diffs[2]<diffs[1]<diffs[0]<.04,(vals,expected,diffs)
    checks+=3
    area=orlicz_area_2d()
    ratio2=area/(2*math.pi)
    assert 1<ratio2<math.sqrt(math.e)
    checks+=1
    ratio1=math.acosh(math.e)/math.sqrt(2)
    assert abs(ratio1-1.171865) <.01
    checks+=1
    for n in [1,2,12,80,400]:
        sample,err=dirichlet_ratio_mc(n)
        assert 1<sample<math.sqrt(math.e)
        if n==1: assert abs(sample-ratio1)<6*err+.004
        if n==2: assert abs(sample-ratio2)<6*err+.004
        if n==400: assert abs(sample-math.sqrt(math.e)*(1-5/(4*n)))<6*err+.004
        checks+=2
        print('n=%d: MC ratio %.9f +/- %.9f'%(n,sample,err))
    print('2D critical convergence F_p=', vals, 'limiting=', expected)
    print('2D volume=',area,'ratio=',ratio2)
    print('verified diagnostics:',checks)

if __name__=='__main__':
    main()
