#!/usr/bin/env python3
"""Standalone numerical cross-checks of the three-equal-Debye mode theorem.

All comparisons use the original loss derivative independently of the
hyperbolic-function reduction. This is evidence, not a substitute for proof.
"""
import math


def original_loss(t, a):
    return sum(math.exp(t+j*a)/(1+math.exp(2*(t+j*a))) for j in (-1, 0, 1))


def original_slope(t, a):
    result=0.0
    for j in (-1,0,1):
        u=t+j*a
        # stable sech and tanh expression for derivative of each Debye peak
        result-=0.5/math.cosh(u)*math.tanh(u)
    return result


def reduced_loss(t, c):
    z=math.cosh(t)
    return 0.5*(1/z + 2*c*z/(z*z+c*c-1))


def reduced_slope(t, c):
    z=math.cosh(t)
    h2=c*c-1
    return 0.5*math.sinh(t)*(-1/z**2+2*c*(h2-z*z)/(z*z+h2)**2)


def stationary(c):
    assert c>4
    h2=c*c-1
    d=math.sqrt(c*(c-4))
    ym=h2*(c-1-d)/(2*c+1)
    yp=h2*(c-1+d)/(2*c+1)
    return math.acosh(math.sqrt(ym)),math.acosh(math.sqrt(yp))


def bisect_slope(a,left,right):
    f=original_slope(left,a)
    g=original_slope(right,a)
    assert f*g<0
    for _ in range(75):
        middle=(left+right)/2
        fm=original_slope(middle,a)
        if f*fm>0:
            left=middle;f=fm
        else:
            right=middle;g=fm
    return (left+right)/2


def numeric_positive_roots(a,tmax):
    n=6000
    left=1e-6
    grid=[left+(tmax-left)*i/n for i in range(n+1)]
    roots=[]
    v=original_slope(grid[0],a)
    for i in range(1,n+1):
        u=original_slope(grid[i],a)
        if v*u<0:
            roots.append(bisect_slope(a,grid[i-1],grid[i]))
        v=u
    return roots


def check():
    count=0
    for c in (1.01,1.5,2.5,3.8,3.999,4.0,4.00001,4.01,4.5,5.0,7.0,12.0,30.0,70.0):
        a=math.acosh(c)
        for j in range(15):
            t=(j-7)*a/6
            assert abs(original_loss(t,a)-reduced_loss(t,c))<1e-11
            assert abs(original_slope(t,a)-reduced_slope(t,c))<1e-11
            count+=2
        roots=numeric_positive_roots(a,max(8,2*a+4))
        expected=[] if c<=4 else list(stationary(c))
        assert len(roots)==len(expected), (c,roots,expected)
        for x,y in zip(roots,expected):
            assert abs(x-y)<2e-9,(c,x,y)
            count+=1
        assert original_slope(min(1e-3,a/100),a)<0
        if c>4:
            tmin,tmax=expected
            assert tmin>0 and tmax>tmin
            assert original_slope((tmin+tmax)/2,a)>0
            assert original_slope(tmax+1,a)<0
            count+=3
        count+=2
    for r in (10**3,10**4,10**5,10**6):
        c=(r+1/r)/2
        a=math.log(r)
        vmin,vmax=stationary(c)
        assert abs(vmin-0.5*a)<0.09
        assert abs(vmax-a)<0.09
        ratio=original_loss(vmin,a)/(2/math.sqrt(r))
        assert abs(ratio-1)<0.13, (r,ratio)
        count+=3
    for d in (1e-5,1e-4,1e-3):
        t0=math.acosh(math.sqrt(5))
        tm,tp=stationary(4+d)
        predicted=math.sqrt(5)/6*math.sqrt(d)
        assert abs((tp-t0)/predicted-1)<0.15
        assert abs((t0-tm)/predicted-1)<0.15
        count+=2
    print('VERIFY_OK checks='+str(count))


if __name__=='__main__':
    check()
