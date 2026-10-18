#!/usr/bin/env python3
"""Independent, standard-library numerical checks for the right equilateral prism theorem.
Scientific notation, no external data or services. Run: python check_prism.py
"""
from math import acos, atan, cos, pi, sin, sqrt
from random import Random


def j(x):
    assert x > 0
    r = sqrt(1.0 + x*x)
    b = pi/2 - 2*atan(x/(sqrt(3)*r))
    return pi/2 - atan(2*x/sqrt(3)) + pi*x/6 - r*b


def jprime(x):
    r = sqrt(1+x*x)
    b = pi/2 - 2*atan(x/(sqrt(3)*r))
    return pi/6 - x*b/r


def p5_formula(x):
    return 12*j(x)/(pi*(3+2*x))


def p_exact(x):
    v=p5_formula(x)
    return {3:2*x/(3+2*x)+v,4:3/(3+2*x)-2*v,5:v}


def p5_direct_quadrature(x, mphi=360, mq=600):
    """Independent orientation-offset integration, NOT the arctangent primitive.
    Fix the side length to 1, hence the planar circumradius to 1/sqrt(3).
    Offset pentagon interval is computed as intersection of five face ranges.
    """
    h=x
    r=1/sqrt(3)
    totalL=totalW=0.0
    for i in range(mphi):
        phi=(i+.5)*2*pi/mphi
        levels=[r*cos(phi-2*pi*j/3) for j in range(3)]
        levels.sort()
        for k in range(mq):
            z=(k+.5)/mq
            rho=sqrt(1-z*z)
            low=[rho*v-h*z/2 for v in levels]
            high=[rho*v+h*z/2 for v in levels]
            w=max(high)-min(low)
            bases_low=levels[0]*rho+h*z/2
            bases_high=levels[2]*rho-h*z/2
            side_low=levels[1]*rho-h*z/2
            side_high=levels[1]*rho+h*z/2
            L=max(0.0,min(bases_high,side_high)-max(bases_low,side_low))
            totalL+=L
            totalW+=w
    return totalL/totalW


def mc_sections(x, n=90000, seed=14813):
    """Independent random-normal/offset edge-counting, width importance weighting."""
    h=x
    r=1/sqrt(3)
    verts=[(r*cos(2*pi*j/3),r*sin(2*pi*j/3),z*h/2)
           for z in (-1,1) for j in range(3)]
    edges=[(3*z+j,3*z+(j+1)%3) for z in range(2) for j in range(3)]
    edges += [(j,j+3) for j in range(3)]
    gen=Random(seed)
    counts={3:0.,4:0.,5:0.}
    mass=0.
    for _ in range(n):
        az=2*pi*gen.random()
        z=2*gen.random()-1
        rho=sqrt(1-z*z)
        ux,uy,uz=rho*cos(az),rho*sin(az),z
        dots=[ux*a+uy*b+uz*c for a,b,c in verts]
        w=max(dots)-min(dots)
        off=min(dots)+w*gen.random()
        nv=sum(1 for i,k in edges if (dots[i]-off)*(dots[k]-off)<0)
        assert nv in counts, ('unexpected generic section',nv)
        counts[nv]+=w
        mass+=w
    return {k:v/mass for k,v in counts.items()}


def verify():
    for x in (0.08,0.18,0.47,0.85,1.5,3.0):
        p=p_exact(x)
        assert abs(sum(p.values())-1)<1e-13
        assert all(0<p[k]<1 for k in (3,4,5))
        direct=p5_direct_quadrature(x)
        assert abs(direct-p[5])<3.0e-5, (x,direct,p[5])
        step=1e-5
        nd=(j(x+step)-j(x-step))/(2*step)
        assert abs(nd-jprime(x))<1e-8, (x,nd,jprime(x))
    a,b=0.05,1.0
    def d(x):return (3+2*x)*jprime(x)-2*j(x)
    assert d(a)>0>d(b)
    for i in range(80):
        m=(a+b)/2
        if d(m)>0:a=m
        else:b=m
    peak=(a+b)/2
    assert abs(peak-0.47287604788115)<3e-11
    assert abs(p5_formula(peak)-0.11265019621095)<3e-11
    assert all(p5_formula(t)<p5_formula(peak) for t in
               (0.001,0.02,0.1,0.25,0.4,0.6,1.,2.,4.,10.,100.))
    for x in (0.35,0.9,1.5):
        got=mc_sections(x)
        expected=p_exact(x)
        assert all(abs(got[k]-expected[k])<0.012 for k in (3,4,5)), (x,got,expected)
    print('PASS: independent offset-orientation quadrature at six ratios;')
    print('PASS: independent weighted edge counts for three ratios;')
    print('PASS: derivative identities, normalization, positivity, and optimizer bracket.')
    print(f'height/side optimum = {peak:.14f}; maximal pentagon probability = {p5_formula(peak):.14f}')

if __name__=='__main__':verify()
