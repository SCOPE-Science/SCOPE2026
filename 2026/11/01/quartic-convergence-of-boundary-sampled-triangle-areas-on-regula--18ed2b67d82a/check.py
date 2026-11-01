#!/usr/bin/env python3
"""Reproducibility checks for regular-polygon boundary triangle-area moments."""
import math
import random

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def point(a,b,t):
    return ((1-t)*a[0]+t*b[0],(1-t)*a[1]+t*b[1])

def triangle(a,b,c):
    return abs(cross((b[0]-a[0],b[1]-a[1]),(c[0]-a[0],c[1]-a[1])))/2

def analytic(m):
    z=math.pi/m; s=math.sin(z); c=math.cos(z)
    return ((1+1.5*(c/s)**2)/m**2,(1+2*c*c)**2/(24*m*m*s*s*c*c))

def independent_sum(m):
    th=math.pi/m; s=math.sin(th); c=math.cos(th)
    v=[(math.cos(2*math.pi*k/m),math.sin(2*math.pi*k/m)) for k in range(m)]
    middle=[point(v[k],v[(k+1)%m],0.5) for k in range(m)]
    distinct=sum(triangle(middle[i],middle[j],middle[k]) for i in range(m) for j in range(i+1,m) for k in range(j+1,m))*6/m**3
    repeated=0.0
    ell=2*s
    for i in range(m):
        for j in range(m):
            if i==j:
                continue
            h=c*(1-math.cos(2*math.pi*(j-i)/m))
            repeated += (3/m**3)*(ell*h/6)
    A=m*s*c
    return (distinct+repeated)/A

def independent_square_moment(m):
    # Direct integration of squared radial edge length then universal determinant identity.
    z=math.pi/m;s=math.sin(z);c=math.cos(z)
    v=(math.cos(2*z),math.sin(2*z))
    radius2=(1+1+v[0])/3
    sigma=radius2/2
    return 1.5*sigma*sigma/(m*s*c)**2

def simulation(m, rng, size=45000):
    v=[(math.cos(2*math.pi*k/m),math.sin(2*math.pi*k/m)) for k in range(m)]
    area=m*math.sin(math.pi/m)*math.cos(math.pi/m)
    total=0.0; total2=0.0
    for _ in range(size):
        p=[point(v[(i:=rng.randrange(m))],v[(i+1)%m],rng.random()) for _j in range(3)]
        a=triangle(*p)/area
        total+=a;total2+=a*a
    return total/size,total2/size

def main():
    for m in range(3,23):
        a,b=analytic(m)
        assert abs(a-independent_sum(m))<2e-12,(m,a,independent_sum(m))
        assert abs(b-independent_square_moment(m))<2e-12,m
        if m>3:assert a<analytic(m-1)[0]
    assert abs(analytic(3)[0]-1/6)<1e-14
    assert abs(analytic(4)[0]-5/32)<1e-14
    rng=random.Random(28042026)
    for m in (3,4,5,7,12):
        a,b=analytic(m);u,v=simulation(m,rng)
        assert abs(a-u)<0.003,(m,u,a)
        assert abs(b-v)<0.003,(m,v,b)
    for m in (300,600,1200):
        a,b=analytic(m)
        assert abs(m**4*(a-3/(2*math.pi**2))-math.pi**2/10)<0.0004,m
        assert abs(m**4*(b-3/(8*math.pi**2))-math.pi**2/15)<0.0004,m
    print('DISTINCT_AND_REPEATED_EDGE_EXACT_SUMS_PASSED 20')
    print('UNIVERSAL_COVARIANCE_SECOND_MOMENT_CHECKS_PASSED 20')
    print('INDEPENDENT_BOUNDARY_SIMULATION_CHECKS_PASSED 5')
    print('QUARTIC_RATE_DIAGNOSTICS_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
