#!/usr/bin/env python3
"""Independent finite stress-tests of the analytic two-temperature Planck theorem.

The proofs of exactly three critical points and their asymptotics are analytic;
finite checks here are diagnostic only, not proof of the infinite claim.
"""
import math


def f(x):
    if x > 700:
        return 0.0
    return x*x*x / math.expm1(x)


def fp(x):
    # Stable derivative for both small and large arguments.
    if x >= 700:
        return 0.0
    if x < 0.0001:
        return 2*x - 1.5*x*x + x*x*x/3
    q = math.exp(-x)
    return x*x*q*((3-x)-3*q)/(1-q)**2


def F(x,R):
    return f(x)+R*f(x/R)


def deriv(x,R):
    return fp(x)+fp(x/R)


def bisect(g, left, right):
    gl=g(left)
    gr=g(right)
    assert gl*gr < 0, (left,right,gl,gr)
    for _ in range(150):
        mid=(left+right)/2
        gm=g(mid)
        if gm == 0 or mid in (left,right):
            return mid
        if gm*gl>0:
            left,gl=mid,gm
        else:
            right,gr=mid,gm
    return (left+right)/2


a = bisect(fp, 2., 3.)
assert 2.8 < a < 2.9
checks=0
for R in (100.,200.,500.,1000.,5000.):
    g=lambda x:deriv(x,R)
    x1=bisect(g,a,5)
    x2=bisect(g,5,R/2)
    x3=bisect(g,R*a-0.5,R*a+0.5)
    assert a < x1 < 5 < x2 < R/2 < x3 < R*a+0.5
    checks+=1
    # Independently sample across all exponentially separated scales.
    grid=[1e-7*(3*R/1e-7)**(k/12000) for k in range(12001)]
    signs=[1 if g(t)>0 else -1 for t in grid]
    transitions=sum(signs[k]!=signs[k-1] for k in range(1,len(signs)))
    assert transitions==3,(R,transitions)
    checks+=1
    for x,h,tag in ((x1,.0001,'cold'),(x2,.0001,'notch'),(x3,.01,'hot')):
        # Direct function values, not the derivative formula.
        curvature=(F(x+h,R)-2*F(x,R)+F(x-h,R))/(h*h)
        if tag=='notch':
            assert curvature>0,(R,tag,curvature)
        elif tag=='cold':
            assert curvature<0,(R,tag,curvature)
        # Hot peak curvature is ~1/R and small numerical differencing for R=5000 may be unstable.
        if tag=='hot':
            hh=max(1, R*.001)
            assert F(x,R)>F(x-hh,R) and F(x,R)>F(x+hh,R)
        checks+=1
    print(f'R={int(R):5d}: max1={x1:.10f}, min={x2:.10f}, max2/R={x3/R:.10f}, valley*R/log(R)^2={F(x2,R)*R/math.log(R)**2:.6f}, signs=3')
assert abs(f(a)-1.4214354727477367)<1e-10
assert abs((-2*a/(-0.4400301901492911))-12.8238445)<0.01
print(f'VERIFY_OK checks={checks} Wien_peak={a:.14f}')
