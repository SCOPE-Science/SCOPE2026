#!/usr/bin/env python3
"""Finite numerical cross-checks for regular-prism central-section vertex means.

Run with Python 3 standard library. Sampling is not an infinite proof.
"""
import math
import random

PI = math.pi


def exact_mean(n, h):
    assert isinstance(n, int) and n >= 5 and h > 0
    s = math.sin(PI / n)
    return 2*n / PI * (math.atan(h) + 2*math.asin(s / math.hypot(1.0, h)))


def direct_edge_angle_sum(n, h):
    v = [(math.cos(2*PI*j/n), math.sin(2*PI*j/n), zz)
         for zz in (-h, h) for j in range(n)]
    edges = [(j, n+j) for j in range(n)]
    edges += [(offset+j, offset+(j+1)%n)
              for offset in (0, n) for j in range(n)]
    total = 0.0
    for i, j in edges:
        vi, vj = v[i], v[j]
        cs = sum(a*b for a,b in zip(vi,vj)) / (math.sqrt(sum(a*a for a in vi))*math.sqrt(sum(b*b for b in vj)))
        total += math.acos(max(-1.0,min(1.0,cs))) / PI
    return total


def section_vertex_count(n, h, u):
    v = [(math.cos(2*PI*j/n), math.sin(2*PI*j/n), zz)
         for zz in (-h, h) for j in range(n)]
    dots = [sum(a*b for a,b in zip(x,u)) for x in v]
    # A generic plane cuts precisely the edges whose endpoints have opposing dot-product signs.
    return sum(dots[j]*dots[n+j] < 0 for j in range(n)) + sum(
        dots[base+j]*dots[base+(j+1)%n] < 0
        for base in (0,n) for j in range(n))


def derivative(n,h):
    s,c = math.sin(PI/n),math.cos(PI/n)
    return (2*n / (PI*(1+h*h)))*(1-2*s*h/math.hypot(h,c))


def main():
    tests=0
    for n in (5,6,7,9,12,30):
        for h in (.04,.2,.7,1.0,1.3090169943749475,2.0,12.0):
            x,y=exact_mean(n,h),direct_edge_angle_sum(n,h)
            assert abs(x-y) < 1e-12, (n,h,x,y)
            tests+=1
    hstar=(3+math.sqrt(5))/4
    assert abs(hstar - math.cos(PI/5)/math.sqrt(4*math.sin(PI/5)**2-1)) < 1e-14
    for h in (.01,.3,.9,hstar*0.99):
        assert derivative(5,h)>0
    for h in (hstar*1.01,3,10,100):
        assert derivative(5,h)<0
    assert abs(derivative(5,hstar))<1e-13
    for n in range(6,61):
        for h in (.01,.2,1.,10.,300.):
            assert derivative(n,h)>0
    tests+=4+4+1+55*5
    max5=exact_mean(5,hstar)
    assert max5 > 5.24 and max5 < 5.25
    for h in (60.,120.):
        crit=(6-exact_mean(6,h))*h**3
        assert abs(crit-3/(2*PI)) < 0.00035,crit
        for n in (7,8,10,20):
            lin=(n-exact_mean(n,h))*h
            target=(2*n/PI)*(1-2*math.sin(PI/n))
            assert abs(lin-target)<0.002,(n,h,lin,target)
        tests+=5
    rng=random.Random(260916195)
    trials=0
    worst=0.
    for n,h in [(5,.2),(5,hstar),(5,3.),(6,.2),(6,1.),(6,3.),(7,.6),(7,2.),(9,1.),(9,4.)]:
        m=26000
        total=0
        min_v,max_v=100,-1
        for k in range(m):
            u=(rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1))
            nv=section_vertex_count(n,h,u)
            total+=nv
            min_v=min(nv,min_v)
            max_v=max(nv,max_v)
        e=total/m
        error=abs(e-exact_mean(n,h))
        assert error < .045,(n,h,e,exact_mean(n,h),error)
        assert 3 <= min_v <= max_v <= n+2
        worst=max(worst,error)
        trials+=m
    print(f'VERIFY_OK formula_direct_angles={42} derivative_and_asymptotic_checks={tests-42} monte_carlo_normals={trials} max_absolute_sampling_error={worst:.6f}')
    print(f'golden_ratio_half_height={hstar:.15f}, pentagon_peak={max5:.15f}, n6_asymptotic_coefficient={3/(2*PI):.15f}')

if __name__=='__main__':
    main()
