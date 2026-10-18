#!/usr/bin/env python3
"""Independent numerical consistency checks for an exact polygon circumradius theorem.

All checks use the Python standard library. This is supplementary evidence:
finite calculations do not establish the theorem for arbitrary convex polygons.
"""
import math
import random
from bisect import bisect_right


def f(theta):
    return (1.0 + math.cos(theta)) ** 2 / math.sin(theta)


def integrate_kernel(theta, n=30000):
    """Quadrature of the original integral after u=x/(1-x), 0<=x<=1."""
    q = math.cos(theta)
    h = 1.0 / n

    def z(x):
        if x >= 1:
            return 0.0
        d = 1.0 - x
        u = x / d
        return (u*u - 2.0*q*u + 1.0)**(-1.5) / (d*d)

    tot = z(0.0) + z(1.0)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * z(i*h)
    return tot*h/3


def corner_integral_checks():
    for theta in [math.pi/3, math.pi/2, 2*math.pi/3, 1.37, 2.4]:
        s = math.sin(theta)
        q = math.cos(theta)
        expected = (1+q)/(s*s)
        found = integrate_kernel(theta)
        assert abs(found-expected) < 3e-7, (theta, found, expected)
        # The triple integral factor is (8*sin(theta)^3/3)*expected**2.
        assert abs((8*s**3/3)*expected**2 - (8/3)*f(theta)) < 1e-10
    print('five one-dimensional corner integrals: PASS')


def sample_polygon(vertices, t, n=200000, seed=32):
    rng = random.Random(seed)
    edges = []
    lengths = []
    cum = []
    L = 0.0
    for i, v in enumerate(vertices):
        w = vertices[(i+1) % len(vertices)]
        e = (w[0]-v[0],w[1]-v[1])
        ell = math.hypot(*e)
        assert ell > 0
        L += ell
        lengths.append(ell)
        edges.append(e)
        cum.append(L)

    def pick():
        u = rng.random()*L
        j = bisect_right(cum,u)
        s = u-(cum[j-1] if j else 0.0)
        v=vertices[j]; e=edges[j]
        return (v[0]+e[0]*s/lengths[j], v[1]+e[1]*s/lengths[j])

    count = 0
    for _ in range(n):
        x,y,z=pick(),pick(),pick()
        ux,uy=y[0]-x[0],y[1]-x[1]
        vx,vy=z[0]-x[0],z[1]-x[1]
        cross=abs(ux*vy-uy*vx)
        if cross < 1e-12:
            continue
        ab=math.hypot(ux,uy)
        ac=math.hypot(vx,vy)
        bc=math.hypot(y[0]-z[0],y[1]-z[1])
        if ab*ac*bc <= 2*t*cross:
            count += 1

    terms=[]
    for i,v in enumerate(vertices):
        a=vertices[i-1]
        b=vertices[(i+1)%len(vertices)]
        u=(a[0]-v[0],a[1]-v[1])
        w=(b[0]-v[0],b[1]-v[1])
        cos=(u[0]*w[0]+u[1]*w[1])/(math.hypot(*u)*math.hypot(*w))
        th=math.acos(max(-1,min(1,cos)))
        terms.append(f(th))
    predicted=16*(t/L)**3*sum(terms)
    empirical=count/n
    se=math.sqrt(max(predicted*(1-predicted)/n,1e-30))
    z=abs(empirical-predicted)/se
    assert z<6, (vertices, empirical, predicted, z)
    print('boundary triangle:',len(vertices),'vertices; n=',n,'t=',t,
          'empirical=',round(empirical,7),'exact=',round(predicted,7),
          'standardized error=',round(z,3),'PASS')


def convexity_and_regular_checks():
    for m in range(3,81):
        x=math.pi/m
        theta=math.pi-2*x
        L=2*m*math.sin(x)
        c1=16*m*f(theta)/L**3
        c2=4/(m*m*math.cos(x))
        assert abs(c1-c2) < 1e-10
    rng=random.Random(1234)
    tested=0
    for m in range(3,11):
        for _ in range(150):
            v=[rng.expovariate(1) for i in range(m)]
            delta=[z*2*math.pi/sum(v) for z in v]
            if max(delta)>=math.pi:
                continue
            lhs=sum(f(math.pi-z) for z in delta)
            rhs=m*f(math.pi-2*math.pi/m)
            assert lhs>=rhs-1e-10
            tested+=1
    assert tested>=300
    print('78 regular-polygon identities and',tested,'angular Jensen instances: PASS')


if __name__=='__main__':
    corner_integral_checks()
    convexity_and_regular_checks()
    sample_polygon([(0,0),(1,0),(1,1),(0,1)],0.15)
    sample_polygon([(0,0),(1,0),(0.5,math.sqrt(3)/2)],0.15)
    sample_polygon([(0,0),(2,0),(0.3,0.8)],0.075)
    print('All numerical consistency checks passed; these are not infinite proofs.')
