#!/usr/bin/env python3
"""Finite regression checks for curvature paths of planar outer parallel bodies.

No finite experiment is used as a proof of the statements for all convex bodies.
This file uses only the Python standard library.
"""
import math
import random

PI = math.pi

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def mul(c, p):
    return (c*p[0], c*p[1])

def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]

def norm(v):
    return math.hypot(*v)

def close(a, b, tolerance=3e-10):
    assert norm(sub(a,b)) <= tolerance*(1+norm(a)+norm(b)), (a,b)

def polygon_data(vertices):
    """Area/edge/boundary/angle data for CCW strictly convex polygons."""
    n=len(vertices)
    a=0.0; moment=(0.,0.)
    for i in range(n):
        p,q=vertices[i],vertices[(i+1)%n]
        d=cross(p,q)
        a+=d/2
        moment=add(moment,mul(d/6,add(p,q)))
    assert a>0
    G=mul(1/a,moment)
    L=0.; perimeter_moment=(0.,0.); sector_s=(0.,0.); extras=[]
    for i in range(n):
        p=vertices[i];q=vertices[(i+1)%n]
        e=sub(q,p);le=norm(e)
        nn=(e[1]/le,-e[0]/le)
        L+=le
        perimeter_moment=add(perimeter_moment,mul(le/2,add(p,q)))
        extras.append((le,p,q,nn))
    angles=[]
    for i in range(n):
        edge_prev=sub(vertices[i],vertices[(i-1)%n])
        edge_next=sub(vertices[(i+1)%n],vertices[i])
        theta=math.atan2(cross(edge_prev,edge_next),edge_prev[0]*edge_next[0]+edge_prev[1]*edge_next[1])
        assert 0<theta<PI
        angles.append(theta)
        sector_s=add(sector_s,mul(theta,vertices[i]))
    assert abs(sum(angles)-2*PI)<1e-9
    H=mul(1/L,perimeter_moment)
    S=mul(1/(2*PI),sector_s)
    return a,L,G,H,S,angles,extras

def expansion_mass_from_disjoint_pieces(vertices, t):
    """Independent exact geometry: central polygon + edge strips + sectors."""
    a,L,G,H,S,angles,extras=polygon_data(vertices)
    mass=a+L*t+PI*t*t
    total_moment=mul(a,G)
    for le,p,q,nn in extras:
        # Centroid of outward rectangle on edge.
        center=add(mul(0.5,add(p,q)),mul(t/2,nn))
        total_moment=add(total_moment,mul(le*t,center))
    n=len(vertices)
    for i in range(n):
        nnprev=extras[(i-1)%n][3]
        alpha0=math.atan2(nnprev[1],nnprev[0]);theta=angles[i]
        radial=(math.sin(alpha0+theta)-math.sin(alpha0),
                math.cos(alpha0)-math.cos(alpha0+theta))
        total_moment=add(total_moment,add(mul(t*t*theta/2,vertices[i]),mul(t**3/3,radial)))
    return mass,mul(1/mass,total_moment)

def curve(a,L,G,H,S,t):
    q=a+L*t+PI*t*t
    return mul(1/q,add(add(mul(a,G),mul(L*t,H)),mul(PI*t*t,S)))

def acceleration_det(a,L,G,H,S,t):
    q=a+L*t+PI*t*t
    dq=L+2*PI*t
    up=L*(a-PI*t*t)/q**2
    vp=PI*t*(2*a+L*t)/q**2
    upp=L*(-2*PI*t*q-2*(a-PI*t*t)*dq)/q**3
    vpp=PI*((2*a+2*L*t)*q-2*t*(2*a+L*t)*dq)/q**3
    return cross(sub(H,G),sub(S,G))*(up*vpp-vp*upp)

def analytic_det(a,L,G,H,S,t):
    return 2*a*L*PI*cross(sub(H,G),sub(S,G))/(a+L*t+PI*t*t)**3

def triangle(apex_angle):
    # Apex at (0,cos(theta/2)), equal legs length 1; CCW.
    s=math.sin(apex_angle/2);c=math.cos(apex_angle/2)
    return [(-s,0.),(s,0.),(0.,c)]

def check():
    rng=random.Random(730141)
    ncheck=0
    # Convex polygons from angularly sampled points on mildly perturbed circle.
    for n in [3,4,5,6,9]:
        for j in range(35):
            ts=sorted(2*PI*(i+rng.uniform(-.08,.08))/n for i in range(n))
            shift=(rng.uniform(-.3,.3), rng.uniform(-.3,.3))
            vertices=[add(shift,(math.cos(x),math.sin(x))) for x in ts]
            a,L,G,H,S,ang,_=polygon_data(vertices)
            for t in [0,.125,.51,1.75,4.5]:
                mass,c_direct=expansion_mass_from_disjoint_pieces(vertices,t)
                assert abs(mass-(a+L*t+PI*t*t))<1e-9
                close(c_direct,curve(a,L,G,H,S,t))
                assert abs(acceleration_det(a,L,G,H,S,t)-analytic_det(a,L,G,H,S,t))<1e-9
                ncheck+=1
    # Strictly scalene triangles have noncollinear curvature centers.
    scalene=0
    for j in range(350):
        # Uniform random angles all in (0,pi), summed to pi.
        x,y=sorted((rng.random(),rng.random()))
        angles=[x*PI,(y-x)*PI,(1-y)*PI]
        if min(angles)<.10 or min(abs(angles[i]-angles[j]) for i in range(3) for j in range(i+1,3))<.035:
            continue
        # Triangle from side lengths proportional to sines; rotate to standard base.
        a,b,c=map(math.sin,angles)
        base=c
        xx=(b*b+base*base-a*a)/(2*base)
        yy2=b*b-xx*xx
        if yy2<0:continue
        vertices=[(0.,0.),(base,0.),(xx,math.sqrt(yy2))]
        area,L,G,H,S,_,_=polygon_data(vertices)
        assert abs(cross(sub(H,G),sub(S,G)))>1e-10
        scalene+=1
    # Isosceles: three centers collinear; except equilateral strict ordering and monotonic.
    for theta in [.15,.5,.9,1.05,1.35,1.8,2.5,2.95]:
        vertices=triangle(theta)
        area,L,G,H,S,_,_=polygon_data(vertices)
        assert abs(cross(sub(H,G),sub(S,G)))<1e-12
        if abs(theta-PI/3)>.002:
            series=[curve(area,L,G,H,S,t)[1] for t in (0,.15,.8,2.0,5.0,20.,5000.)]
            assert all(series[i+1]>series[i] for i in range(len(series)-1)) if theta<PI/3 else all(series[i+1]<series[i] for i in range(len(series)-1))
    print('PASS: independent polygon area-moment expansion, 875 offset cases; 350 attempted scalene cases with',scalene,'nondegenerate witnesses; 8 isosceles paths')

if __name__=='__main__':
    check()
