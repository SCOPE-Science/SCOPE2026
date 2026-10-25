#!/usr/bin/env python3
"""Independent finite checks for a planar convex-hull vertex-count theorem.
Run with Python 3 and the standard library; no downloaded data needed.
Finite checks corroborate, but do not establish, the all-parameter proof.
"""
import math
import random

RNG = random.Random(20261018)


def hull_vertex_count(n, m, radius, phase):
    pi = math.pi
    pts = [(math.cos(2*pi*j/n), math.sin(2*pi*j/n), 0, j)
           for j in range(n)]
    pts += [(radius*math.cos(phase + 2*pi*j/m),
             radius*math.sin(phase + 2*pi*j/m), 1, j)
            for j in range(m)]
    points = sorted(pts)
    def cross(a, b, c):
        return ((b[0]-a[0])*(c[1]-a[1])
                -(b[1]-a[1])*(c[0]-a[0]))
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2],lower[-1],p) <= 1e-12:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2],upper[-1],p) <= 1e-12:
            upper.pop()
        upper.append(p)
    h = lower[:-1]+upper[:-1]
    return len(h), sum(p[2] == 1 for p in h)


def theo(n, m, radius):
    a = math.pi/n
    if radius <= math.cos(a):
        q = 0.0
    else:
        q = math.acos(min(1.,math.cos(a)/radius))/a
    g = math.gcd(n,m)
    k = m//g
    t = k*q
    j = math.floor(t)
    f = t - j
    return (q,g,k,j,f)


def angular_inner_count(n, m, radius, phase):
    a=math.pi/n
    if radius <= math.cos(a):return 0
    b=math.acos(math.cos(a)/radius)
    inner=[(phase+2*math.pi*j/m - a)%(2*a) for j in range(m)]
    return sum(x < b or x > 2*a-b for x in inner)


def check():
    total=0
    for _ in range(15000):
        n=RNG.randrange(3,61)
        m=RNG.randrange(3,n+1)
        r=RNG.uniform(.05, .99999)
        phase=RNG.uniform(0,2*math.pi)
        size, ni = hull_vertex_count(n,m,r,phase)
        assert size == n+ni, (n,m,r,phase,size,ni)
        ca = angular_inner_count(n,m,r,phase)
        assert ca == ni,(n,m,r,phase,ca,ni)
        q,g,k,j,f=theo(n,m,r)
        assert ni in (g*j,g*(j+1)),(n,m,r,ni,g,j,f)
        if f < 1e-12:assert ni == g*j
        total+=1
    print('INDEPENDENT_MONOTONE_CHAIN_ANGULAR_HULL_CASES_OK',total)

    thresholds=0
    for n in range(3,43):
        for m in range(3,n+1):
            g=math.gcd(n,m)
            k=m//g
            if k < 2:continue
            j=RNG.randrange(1,k)
            a=math.pi/n
            radius=math.cos(a)/math.cos(j*a/k)
            for _ in range(6):
                phase=RNG.uniform(0,2*math.pi)
                size,ni=hull_vertex_count(n,m,radius,phase)
                assert ni == g*j, (n,m,j,ni,phase)
                assert size==n+g*j
                thresholds+=1
    print('DETERMINISTIC_COPRIME_AND_NONCOPRIME_THRESHOLDS_OK',thresholds)

    quad=0
    for n,m,r in [(8,5,.985),(12,8,.99),(30,7,.997),(24,18,.999),
                  (10,3,.93),(3,3,.8),(6,6,.99),(11,4,.996)]:
        q,g,k,j,f=theo(n,m,r)
        hits=0
        phi_period=2*math.pi/n
        for s in range(2400):
            phase=(s+.482159)/2400*phi_period
            _size,ni=hull_vertex_count(n,m,r,phase)
            hits += (ni==g*(j+1))
        if f>0.005 and f<.995:
            assert abs(hits/2400-f)<.002,(n,m,r,hits/2400,f)
        quad+=2400
    print('FULL_ORIENTATION_GRID_TWO_ATOM_PROBABILITY_OK',quad)

    # Fixed inner order with different gcd subsequences: n coprime to six,
    # and n divisible by six; the near-circle limit depends on gcd.
    lam=3/8
    for n in (71,101,121,181,240,300,420,600):
        m=6
        a=math.pi/n
        q,g,k,j,f=theo(n,m,1-lam*a*a)
        assert abs(q-.5)<.0002,(n,q)
        assert abs(g*(j+f)-3)<.002,(n,g,j,f)
        if g==1:assert g*g*f*(1-f)<.003
        if g==6:assert abs(g*g*f*(1-f)-9)<.003
    print('ARITHMETIC_CRITICAL_WINDOW_VARIANCES_OK')
    print('ALL_PLANAR_ROTATION_HULL_CHECKS_OK')

if __name__=='__main__':check()
