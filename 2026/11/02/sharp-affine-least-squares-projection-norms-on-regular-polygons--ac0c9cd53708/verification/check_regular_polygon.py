#!/usr/bin/env python3
"""Checks: sharp affine L2-projector L-infinity norm on regular polygons.

Python 3 standard library only. Independent computation integrates the absolute
kernel on origin-to-edge triangles by one-dimensional polynomial primitives.
Finite calculations test examples, not the all-n theorem or its asymptotic proof.
"""
import math


def norm_formula(n):
    if not isinstance(n, int) or n < 3:
        raise ValueError('n must be an integer >= 3')
    h = 2*math.pi/n
    s = (2+math.cos(h))/12
    j = math.ceil(math.acos(-s)/h - 1e-14)
    cj, sj = math.cos(j*h), math.sin(j*h)
    cprev, sprev = math.cos((j-1)*h), math.sin((j-1)*h)
    y = sprev + ((-s-cprev)/(cj-cprev))*(sj-sprev)
    cap_area = ((n-2*j)*math.sin(h)-2*s*sj-2*y*(cj+s))/2
    arc_cos_sum = -2*math.sin((j-.5)*h)/math.sin(h/2) -2*cj
    cap_moment = (math.sin(h)*arc_cos_sum
                  +2*(cj-s)*(-s*sj-y*cj)+4*s*s*y)/6
    area = n*math.sin(h)/2
    return 1-2*(cap_area+cap_moment/s)/area


def segment_triangle_average(la, lb):
    # Triangle with vertices (0,a,b), and affine integrand whose values
    # at those vertices are (1,la,lb).
    d = la-1.
    B = lb-1.
    roots = [0., 1.]
    for den, num in ((d,-1.), (la-lb,-lb)):
        if abs(den)>1e-13:
            t = num/den
            if 0<t<1: roots.append(t)
    roots = sorted(set(roots))
    if abs(B)<1e-13:
        def anti(u):return u+(d-1)*u*u/2-d*u*u*u/3
        return 2*sum((1 if 1+d*(u+v)/2 >=0 else -1)
                     *(anti(v)-anti(u)) for u,v in zip(roots,roots[1:]))
    result=0.
    for lo,hi in zip(roots,roots[1:]):
        A0,A1 = 1+d*lo,1+d*hi
        E0,E1 = lb+(la-lb)*lo,lb+(la-lb)*hi
        sa = 1 if A0+A1>=0 else -1
        se = 1 if E0+E1>=0 else -1
        aa=(A0*A0+A0*A1+A1*A1)/3
        ee=(E0*E0+E0*E1+E1*E1)/3
        result += (hi-lo)*(se*ee-sa*aa)/B
    return result


def independent_kernel_row(n, angle=0., radius=1.):
    h = 2*math.pi/n
    s = (2+math.cos(h))/12
    x = (radius*math.cos(angle),radius*math.sin(angle))
    return sum(segment_triangle_average(
        1+(x[0]*math.cos(k*h)+x[1]*math.sin(k*h))/s,
        1+(x[0]*math.cos((k+1)*h)+x[1]*math.sin((k+1)*h))/s)
        for k in range(n))/n


def run():
    max_error = 0
    checks = 0
    for n in range(3,81):
        prediction = norm_formula(n)
        independently = independent_kernel_row(n)
        err = abs(prediction-independently)
        max_error = max(max_error,err)
        assert err < 1e-10,(n,prediction,independently)
        checks+=1
    for n,value in [(3,19/8),(4,233/108),(6,361/180)]:
        assert abs(norm_formula(n)-value)<1e-11
    # Sample interior points only; the theorem establishes vertex maximality.
    for n in range(3,35):
        v=norm_formula(n)
        for radius in (0,.2,.5,.8,.99):
            for theta in (0., math.pi/(2*n), math.pi/n):
                assert independent_kernel_row(n,theta,radius*math.cos(math.pi/n))<=v+1e-10
                checks+=1
    disk=2/math.pi*(math.asin(.25)+11*math.sqrt(15)/16)
    coefficient=5*math.pi*math.sqrt(15)/12
    for n in (500,1000,2000):
        scaled=n*n*(norm_formula(n)-disk)
        assert abs(scaled-coefficient)<.02,(n,scaled,coefficient)
        checks+=1
    print('Independent exact polynomial-integral comparisons:',78)
    print('Interior row checks:',32*15)
    print('Asymptotic checks:',3)
    print('Total checked assertions:',checks+3)
    print('Max row error:',max_error)
    print('Sample n=3,4,6:',*[norm_formula(n) for n in (3,4,6)])
    print('Disk norm:',disk)
    print('Predicted leading coefficient:',coefficient)

if __name__=='__main__':run()
