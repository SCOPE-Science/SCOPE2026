#!/usr/bin/env python3
"""Numerical diagnostics for the centroidal right-rectangular-pyramid section theorem.
The mathematical proof is analytic; these checks test independent implementations.
"""
from math import pi, asin, cos, sin, sqrt, atan, isclose
from random import Random


def law(a, b, c):
    assert a > 0 and b > 0 and c > 0
    z = sqrt(a*a+b*b+c*c)
    return 4/pi*(asin(a/z)+asin(b/z)-asin(sqrt(a*a+b*b)/z))


def integral_law(a,b,c,steps=20000):
    assert steps%2 == 0
    def fn(phi):
        f = a*cos(phi)+b*sin(phi)
        g = abs(a*cos(phi)-b*sin(phi))
        return f/sqrt(c*c+f*f)-g/sqrt(c*c+g*g)
    delta = (pi/2)/steps
    s=fn(0)+fn(pi/2)
    for j in range(1,steps):
        s+=(4 if j%2 else 2)*fn(delta*j)
    return 2/pi*delta*s/3


def edge_count(a,b,c,xyz):
    x,y,z=xyz
    vals=[-a*x-b*y-c*z,-a*x+b*y-c*z,a*x-b*y-c*z,a*x+b*y-c*z,3*c*z]
    edges=((0,1),(1,3),(3,2),(2,0),(0,4),(1,4),(2,4),(3,4))
    return sum((vals[i]>0)!=(vals[j]>0) for i,j in edges)


def simulate(a,b,c,n,seed):
    r=Random(seed)
    count=0
    for _ in range(n):
        xyz=(r.gauss(0,1),r.gauss(0,1),r.gauss(0,1))
        k=edge_count(a,b,c,xyz)
        assert k in (4,5)
        count += (k==5)
    return count/n


def derivative_height(a,b,c):
    total=a*a+b*b+c*c
    return 4/(pi*total)*(sqrt(a*a+b*b)-c*(a/sqrt(b*b+c*c)+b/sqrt(a*a+c*c)))


def params(theta,z):
    return sqrt(2)*cos(theta),sqrt(2)*sin(theta),z


def main():
    cases=((1.,1.,.2),(1.,1.,1.),(1.,1.,4.),(2.,.5,.7),(.5,2.,3.),(1.1,1.7,1.3))
    for i,(a,b,c) in enumerate(cases):
        closed=law(a,b,c)
        integrated=integral_law(a,b,c)
        assert abs(closed-integrated)<5e-9, (a,b,c,closed,integrated)
        mc=simulate(a,b,c,100000,20261025+i)
        assert abs(closed-mc)<.012, (a,b,c,closed,mc)
        step=1e-5*max(1.,c)
        difference=(law(a,b,c+step)-law(a,b,c-step))/(2*step)
        assert abs(difference-derivative_height(a,b,c))<5e-8
        print('case',i,'analytic',round(closed,9),'integral',round(integrated,9),'simulation',round(mc,6))
    optimum=law(1,1,1)
    assert abs(optimum-(2/pi)*(3*__import__('math').acos(1/3)-pi))<1e-14
    r=Random(20261125)
    for _ in range(3000):
        a=10**r.uniform(-2,2);b=10**r.uniform(-2,2);c=10**r.uniform(-2,2)
        assert law(a,b,c)<=optimum+3e-14
        L=sqrt(a*a+b*b)
        assert law(a,b,c)<=law(L/sqrt(2),L/sqrt(2),c)+3e-14
    eps=0.0005
    def pp(theta,z):
        return law(*params(theta,z))
    pi4=pi/4
    d2_theta=(pp(pi4+eps,1)-2*pp(pi4,1)+pp(pi4-eps,1))/eps**2
    d2_height=(pp(pi4,1+eps)-2*pp(pi4,1)+pp(pi4,1-eps))/eps**2
    d2_mix=(pp(pi4+eps,1+eps)-pp(pi4+eps,1-eps)-pp(pi4-eps,1+eps)+pp(pi4-eps,1-eps))/(4*eps*eps)
    assert abs(d2_theta+2*sqrt(2)/pi)<2e-6
    assert abs(d2_height+2*sqrt(2)/(3*pi))<2e-6
    assert abs(d2_mix)<2e-7
    print('sharp maximum',repr(optimum))
    print('quadratic curvature',repr(d2_theta),repr(d2_height),repr(d2_mix))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
