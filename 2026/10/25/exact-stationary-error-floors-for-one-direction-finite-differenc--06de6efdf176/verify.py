#!/usr/bin/env python3
"""Reproduce exact planar finite-difference subspace Newton checks.

Requires only Python 3 standard library. Run: python verify.py
This is a numerical cross-check, not a substitute for the analytical proof.
"""
import math
import random
from fractions import Fraction

CHECKS = 0


def near(a, b, tol=1e-9):
    global CHECKS
    CHECKS += 1
    if abs(a-b)>tol * max(1.0,abs(a),abs(b)):
        raise AssertionError((a,b,tol))


def f(x, a,b):
    return (a*x[0]*x[0]+b*x[1]*x[1])/2.0


def step_fd(x,u,a,b,h):
    fu=f(x,a,b)
    f1=f((x[0]+h*u[0],x[1]+h*u[1]),a,b)
    f2=f((x[0]+2*h*u[0],x[1]+2*h*u[1]),a,b)
    g=(f1-fu)/h
    H=(f2-2*f1+fu)/(h*h)
    return (x[0]-g*u[0]/H,x[1]-g*u[1]/H)


def step_formula(x,u,a,b,h):
    D=a*u[0]*u[0]+b*u[1]*u[1]
    delta=(a*u[0]*x[0]+b*u[1]*x[1])/D+h/2
    return (x[0]-delta*u[0],x[1]-delta*u[1])


def solve3(A,b):
    M=[list(map(float,A[i]))+[float(b[i])] for i in range(3)]
    for k in range(3):
        p=max(range(k,3),key=lambda i:abs(M[i][k]))
        M[p],M[k]=M[k],M[p]
        t=M[k][k]
        assert abs(t)>1e-14
        M[k]=[x/t for x in M[k]]
        for i in range(3):
            if i!=k:
                t=M[i][k]
                M[i]=[M[i][j]-t*M[k][j] for j in range(4)]
    return [M[i][3] for i in range(3)]


def quadrature_covariance(a,b,h,N=8192):
    # Independent brute-force angular quadrature for the complete covariance map.
    # Symmetric covariance coordinates are C11,C12,C22.
    T=[[0.0]*3 for _ in range(3)]
    forcing=[0.0]*3
    first=[0.0,0.0]
    beta=0.0
    for j in range(N):
        th=2*math.pi*(j+0.5)/N
        c=math.cos(th);s=math.sin(th)
        z1=math.sqrt(a)*c;z2=math.sqrt(b)*s
        d=z1*z1+z2*z2
        v1=z1/math.sqrt(d);v2=z2/math.sqrt(d)
        P11=1-v1*v1;P12=-v1*v2;P22=1-v2*v2
        X=v1*v1
        first[0]+=X/N
        beta+=X*(1-X)/N
        # Full 2x2 conjugation, without assuming diagonal stationarity.
        T[0][0]+=P11**2/N
        T[0][1]+=2*P11*P12/N
        T[0][2]+=P12**2/N
        T[1][0]+=P11*P12/N
        T[1][1]+=(P11*P22+P12*P12)/N
        T[1][2]+=P12*P22/N
        T[2][0]+=P12**2/N
        T[2][1]+=2*P12*P22/N
        T[2][2]+=P22**2/N
        forcing[0]+=(h*h/4)*(z1*z1)/N
        forcing[1]+=(h*h/4)*(z1*z2)/N
        forcing[2]+=(h*h/4)*(z2*z2)/N
    return solve3([[(1 if i==j else 0)-T[i][j] for j in range(3)] for i in range(3)],forcing),first[0],beta


def exact_cov(a,b,h):
    g=math.sqrt(a*b)
    return (h*h*(3*a+b+2*g)/24,0.0,h*h*(a+3*b+2*g)/24)


def exact_fraction_comparison(a,b,h):
    # Rational-square curvature pairs give independent exact comparisons.
    ra=Fraction(a);rb=Fraction(b);rh=Fraction(h)
    sqroot=math.isqrt(a*b)
    assert sqroot*sqroot==a*b
    haar=rh*rh*(ra+rb+sqroot)/12
    coordinate=rh*rh*(ra+rb)/8
    difference=rh*rh*(math.isqrt(a)-math.isqrt(b))**2/24
    assert coordinate-haar==difference
    return haar,coordinate,difference


def run():
    rng=random.Random(8812401)
    for a,b,h in [(1,1,.2),(1,4,.3),(4,1,.7),(9,16,.12),(.5,8,.4),(2,3,.25),(100,1,.1)]:
        true=exact_cov(a,b,h)
        C,m,beta=quadrature_covariance(a,b,h)
        for i in range(3): near(C[i],true[i],tol=2e-9)
        near(m,math.sqrt(a)/(math.sqrt(a)+math.sqrt(b)),2e-9)
        near(beta,math.sqrt(a*b)/(2*(math.sqrt(a)+math.sqrt(b))**2),2e-9)
        near((C[0]+C[2])/2,h*h*(a+b+math.sqrt(a*b))/12,2e-9)
        for j in range(100):
            ang=rng.random()*2*math.pi
            u=(math.cos(ang),math.sin(ang))
            x=(rng.uniform(-2,2),rng.uniform(-2,2))
            x1=step_fd(x,u,a,b,h)
            x2=step_formula(x,u,a,b,h)
            near(x1[0],x2[0],tol=2e-8)
            near(x1[1],x2[1],tol=2e-8)
    for a,b,h in [(1,4,Fraction(1,3)),(1,9,Fraction(2,5)),(4,16,Fraction(5,7)),(9,9,Fraction(2,3))]:
        haar,coord,difference=exact_fraction_comparison(a,b,h)
        near(float(coord-haar),float(difference),1e-14)
    # Stationary simulation, independently implementing the geometry formula.
    for a,b,h in [(1,1,.2),(1,4,.3),(9,1,.15),(100,1,.12)]:
        m=1800
        x1=[0.0]*m;x2=[0.0]*m
        for it in range(210):
            for k in range(m):
                angle=2*math.pi*rng.random()
                u=math.cos(angle);v=math.sin(angle)
                D=a*u*u+b*v*v
                t=(a*u*x1[k]+b*v*x2[k])/D+h/2
                x1[k]-=t*u;x2[k]-=t*v
        value=sum((a*x1[k]**2+b*x2[k]**2)/2 for k in range(m))/m
        target=h*h*(a+b+math.sqrt(a*b))/12
        near(value,target,tol=.13)
    print('PASS',CHECKS,'standalone numerical and exact-rational checks')

if __name__=='__main__':
    run()
