#!/usr/bin/env python3
"""Numerical diagnostics for the intrinsic inradius law of central octahedron sections.

Uses only Python standard library. This is not a replacement for the analytic proof.
"""
import math
import random

PI = math.pi
SQ3 = math.sqrt(3)
T_CRIT = 1 / SQ3


def tail_plus(t):
    if t >= 1:
        return 0.0
    return 6 / PI * (PI / 2 - PI * t / (3 * SQ3)
        - 2 * math.asin(1 / math.sqrt(3 - t*t))
        + 2 * t / SQ3 * math.atan(t / math.sqrt(3 * (2-t*t))))


def tail_minus(t):
    if t >= T_CRIT:
        return 0.0
    aa = (1 - t*t) / 2
    a = math.sqrt(aa)
    alpha = math.acos((1+t*t)/(3-t*t))
    c = (aa + 2*a*t - t*t/3) / (1-t*t/3)
    theta = math.acos(min(1.,max(-1., c)))
    return 2 / PI * (3*alpha-PI-SQ3*t*theta)


def cdf(r):
    if r <= 1 / SQ3:
        return 0.0
    if r >= 1 / math.sqrt(2):
        return 1.0
    t = math.sqrt(max(0,3-1/(r*r)))
    return 1 - tail_plus(t) - tail_minus(t)


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def norm(a):
    return math.sqrt(dot(a,a))


def planar_section_polygon_inradius(normal):
    """Independently construct the section polygon from all 12 octahedron edges."""
    v = [(s*(i==0),s*(i==1),s*(i==2)) for i in range(3) for s in (-1,1)]
    points=[]
    for i in range(6):
        for j in range(i+1,6):
            if i // 2 == j // 2:
                continue
            p,q=v[i],v[j]
            x,y=dot(normal,p),dot(normal,q)
            if x*y < 0:
                point=tuple((y*p[k]-x*q[k])/(y-x) for k in range(3))
                points.append(point)
    ref=(1.,0.,0.) if abs(normal[0]) < .9 else (0.,1.,0.)
    basis1=cross(normal,ref)
    nn=norm(basis1)
    basis1=tuple(z/nn for z in basis1)
    basis2=cross(normal,basis1)
    verts=sorted(((dot(p,basis1),dot(p,basis2)) for p in points),
                 key=lambda x:math.atan2(x[1],x[0]))
    assert len(verts) in (4,6), ('unexpected intersection vertices',len(verts))
    radii=[]
    for i,p in enumerate(verts):
        q=verts[(i+1)%len(verts)]
        dx,dy=q[0]-p[0],q[1]-p[1]
        radii.append(abs(p[0]*q[1]-p[1]*q[0])/math.hypot(dx,dy))
    return min(radii)


def predicted_inradius(normal):
    a,b,c=sorted(map(abs,normal),reverse=True)
    return (3-(a-b-c)**2)**(-.5)


def uniform_sphere(rng):
    z=2*rng.random()-1
    phi=2*PI*rng.random()
    xy=math.sqrt(1-z*z)
    return (xy*math.cos(phi),xy*math.sin(phi),z)


def integrate_simpson(f, lo, hi, n):
    assert n%2==0
    h=(hi-lo)/n
    s=f(lo)+f(hi)
    for j in range(1,n):
        s+=(4 if j%2 else 2)*f(lo+j*h)
    return s*h/3


def one_octant_plus_integrand(phi,t):
    b=math.cos(phi)+math.sin(phi)
    return 1-(t+b*math.sqrt(max(0,1+b*b-t*t)))/(1+b*b)


def run():
    rng=random.Random(482916)
    checks=0
    for _ in range(500):
        n=uniform_sphere(rng)
        actual=planar_section_polygon_inradius(n)
        predicted=predicted_inradius(n)
        assert abs(actual-predicted) < 5e-13, (n,actual,predicted)
        checks+=1
    for t in (0,.025,.1,.25,.4,.55,1/SQ3,.65,.78,.9,.99,1.):
        integral=6/PI*integrate_simpson(lambda ph:one_octant_plus_integrand(ph,t),0,PI/2,2000)
        assert abs(tail_plus(t)-integral)<1e-11,(t,integral,tail_plus(t))
        checks+=1
    assert abs(tail_plus(0)+tail_minus(0)-1)<1e-13
    checks+=1
    for t in (.01,.1,.3,.5,.55,1/SQ3,.7,.9,.99):
        r=1/math.sqrt(3-t*t)
        val=cdf(r)
        assert -1e-10<=val<=1+1e-10
        checks+=1
    n=150000
    qs=[]
    for _ in range(n):
        xyz=uniform_sphere(rng)
        a,b,c=sorted(map(abs,xyz),reverse=True)
        qs.append(abs(a-b-c))
    for t in (.03,.1,.2,.3,.4,.5,1/SQ3,.67,.8,.9,.97):
        empirical=sum(x<=t for x in qs)/n
        exact=1-tail_plus(t)-tail_minus(t)
        assert abs(empirical-exact)<.008,(t,empirical,exact)
        checks+=1
    print('PASS: independent edge-polygon inradii, quadrature, endpoints, and',n,'sphere samples;',checks,'diagnostic checks')

if __name__=='__main__':
    run()
