#!/usr/bin/env python3
"""Numerical checks for the geometry of random orthogonal projections of fixed triangles.
All mathematical theorems are proved analytically in RESULT.md; finite checks are diagnostics.
No external packages or external data are required.
"""
import math
import random

PI=math.pi

def simpson(fun, n=4096):
    if n%2:raise ValueError('even subdivision count required')
    h=1.0/n
    total=fun(0.0)+fun(1.0)
    for j in range(1,n):total+=(4 if j%2 else 2)*fun(j*h)
    return total*h/3.0

def p_integral(angle):
    if not 0<angle<PI:raise ValueError('angle must be in (0, pi)')
    if angle>PI/2: return 1-p_integral(PI-angle)
    if angle==PI/2:return .5
    x=(1-math.cos(angle))/2
    return x*simpson(lambda t: math.cos(PI*t/2)**2/math.sqrt((1-x*math.sin(PI*t/2)**2)*(1-x*(1+math.sin(PI*t/2)**2))))

def p_polar(angle):
    if angle>PI/2:return 1-p_polar(PI-angle)
    if angle==PI/2:return .5
    x=(1-math.cos(angle))/2
    # A different surface-area integral with normal-axis polar coordinates.
    return 1-simpson(lambda t: math.sqrt((1-x-x*math.sin(PI*t/2)**2)/(1-x*math.sin(PI*t/2)**2)))*1.0

def p_from_normal(angle,n):
    co=math.cos(angle/2);si=math.sin(angle/2)
    u=(co,si,0.0);v=(co,-si,0.0)
    dot=math.cos(angle)-(sum(u[j]*n[j] for j in range(3)))*(sum(v[j]*n[j] for j in range(3)))
    return dot<0

def normal(rng):
    a,b,c=(rng.gauss(0,1) for j in range(3));q=math.sqrt(a*a+b*b+c*c)
    return (a/q,b/q,c/q)

def triangle_vertices(angles):
    # Fix A=(0,0), B=(1,0), C=t*(cos(A),sin(A)).
    A,B,C=angles
    t=math.sin(B)/math.sin(C)
    return ((0.0,0.0),(1.0,0.0),(t*math.cos(A),t*math.sin(A)))

def is_obtuse_projected(vertices,n):
    proj=[]
    for x,y in vertices:
        proj.append((x-n[0]*(n[0]*x+n[1]*y),y-n[1]*(n[0]*x+n[1]*y),-n[2]*(n[0]*x+n[1]*y)))
    for k in range(3):
        p=proj[k];u=proj[(k+1)%3];v=proj[(k+2)%3]
        if sum((u[j]-p[j])*(v[j]-p[j]) for j in range(3))<0:return True
    return False

if __name__=='__main__':
    nchecks=0
    for deg in range(5,90,5):
        a=math.radians(deg)
        assert abs(p_integral(a)-p_polar(a))<2e-6,(deg,p_integral(a),p_polar(a))
        nchecks+=1
    eq=3*p_integral(PI/3)
    assert abs(eq-0.47033962453623734)<0.000003
    assert eq<0.5
    print('Equilateral probability:',format(eq,'.12f'))
    rng=random.Random(2141277)
    for j in range(1000):
        # All angles acute, via rejection from a simple positive simplex law.
        while True:
            a=rng.uniform(0,PI/2);b=rng.uniform(0,PI/2);c=PI-a-b
            if 0<c<PI/2:break
        assert p_integral(a)+p_integral(b)+p_integral(c)>eq-3e-7
        nchecks+=1
    cases=[(60,60,60),(40,65,75),(20,80,80),(30,60,90),(20,40,120)]
    for degrees in cases:
        angles=tuple(math.radians(a) for a in degrees)
        verts=triangle_vertices(angles)
        theoretical=sum(p_integral(a) for a in angles)
        sample=25000
        count=sum(is_obtuse_projected(verts,normal(rng)) for _ in range(sample))
        estimated=count/sample
        # At least 6.5 Bernoulli standard deviations, plus discretization tolerance.
        assert abs(estimated-theoretical)<.025,(degrees,estimated,theoretical)
        nchecks+=1
        print('Triangle',degrees,'integral',format(theoretical,'.7f'),'simulation',format(estimated,'.7f'))
    for j in range(1,1001):
        w=j/1000
        assert (1+w/2)**2*(1-w/4)*(1-w/3)>=1-1e-13
        nchecks+=1
    print('PASS:',nchecks,'direct consistency/inequality checks; 125000 independent projected triangle trials')
