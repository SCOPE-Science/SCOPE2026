#!/usr/bin/env python3
"""Finite checks for a harmonic Abel family; analytic proof is in RESULT.md."""
import math

PI=math.pi


def setup(g,v,w,s,k):
    def vals(t):
        G=g+v*math.cos(t)
        S=w+s*math.sin(t)
        gp=-v*math.sin(t)
        sp=s*math.cos(t)
        A=G*S*(S+k)*gp
        B=-G*sp-(2*S+k)*gp
        return G,S,gp,sp,A,B
    return vals


def simpson(f,a,b,n=6000):
    assert n%2==0
    h=(b-a)/n
    sm=f(a)+f(b)
    for j in range(1,n):
        sm+=(4 if j%2 else 2)*f(a+j*h)
    return sm*h/3


def rk4(f,u,N=2000):
    h=2*PI/N
    x=u
    for j in range(N):
        t=j*h
        z1=f(t,x)
        z2=f(t+h/2,x+h*z1/2)
        z3=f(t+h/2,x+h*z2/2)
        z4=f(t+h,x+h*z3)
        x+=h*(z1+2*z2+2*z3+z4)/6
        assert math.isfinite(x) and abs(x)<100000
    return x


def check(g,v,w,s,k):
    vals=setup(g,v,w,s,k)
    def rhs(t,x):
        G,S,gp,sp,A,B=vals(t)
        return A*x**3+B*x**2
    def curve(t,q):
        G,S,gp,sp,A,B=vals(t)
        P=G*(S+q)
        xp=-(gp*(S+q)+G*sp)/P**2
        return 1/P,xp
    for q in (0,k):
        for j in range(48):
            t=2*PI*j/48
            x,xp=curve(t,q)
            assert abs(rhs(t,x)-xp)<1e-11
        u=curve(0,q)[0]
        assert abs(rk4(rhs,u)-u)<2e-9
    def J(c):
        return simpson(lambda t:2*s*v*math.sin(t)**2/((g+v*math.cos(t))*(c*c-s*s*math.sin(t)**2)),0,PI)
    for q,c,sgn in ((0,w,1),(k,w+k,-1)):
        exponent=simpson(lambda t:(3*vals(t)[4]*curve(t,q)[0]**2+2*vals(t)[5]*curve(t,q)[0]),0,2*PI)
        assert abs(exponent-sgn*k*J(c))<2e-9
        assert exponent*sgn>0
    assert abs(simpson(lambda t:vals(t)[5],0,2*PI)-PI*v*s)<1e-9
    # Selected intervals: origin -- attracting rational -- repelling rational.
    lo=curve(0,k)[0]
    hi=curve(0,0)[0]
    mid=(lo+hi)/2
    assert 0<lo<mid<hi
    assert rk4(rhs,lo*0.50)-lo*0.50>0
    assert rk4(rhs,mid)-mid<0
    assert rk4(rhs,hi*1.02)-hi*1.02>0
    return (round(-k*J(w+k),12),round(k*J(w),12))


if __name__=='__main__':
    a=check(3,1,2,0.5,1)
    assert abs(a[0]+0.061154868707)<1e-8
    assert abs(a[1]-0.141350491003)<1e-8
    b=check(4,0.8,2.4,0.4,0.6)
    c=check(2.7,0.2,1.8,0.15,0.7)
    print('CHECK_OK',a,b,c)
