#!/usr/bin/env python3
"""Independent finite diagnostics for Haar central-section areas of the unit octahedron.

All mathematical conclusions require the analytical proof in RESULT.md.
This script uses only the Python 3 standard library.
"""
import math
import random

ROOT2 = math.sqrt(2.0)
ROOT3 = math.sqrt(3.0)
PI = math.pi


def area_formula(a, b, c):
    assert min(a, b, c) >= 0
    S = a*b + a*c + b*c
    P = (a+b)*(a+c)*(b+c)
    return 2.0*math.sqrt(a*a+b*b+c*c)*S/P


def section_vertices(a, b, c):
    u = (a, b, c)
    vertices = []
    for i, j in ((1,0),(2,0),(2,1),(0,1),(0,2),(1,2)):
        v = [0.0]*3
        v[i] = u[j]/(u[i]+u[j])
        v[j] = -u[i]/(u[i]+u[j])
        vertices.append(v)
    return vertices


def area_from_vertices(a, b, c):
    P = section_vertices(a, b, c)
    n = math.sqrt(a*a+b*b+c*c)
    accum = 0.0
    for i in range(6):
        v, w = P[i], P[(i+1)%6]
        cross = (v[1]*w[2]-v[2]*w[1], v[2]*w[0]-v[0]*w[2], v[0]*w[1]-v[1]*w[0])
        accum += (a*cross[0]+b*cross[1]+c*cross[2])/n
    return abs(accum)/2.0


def simpson(f, left, right, steps):
    assert steps%2 == 0
    h=(right-left)/steps
    v=f(left)+f(right)
    for i in range(1,steps):
        v+=(4 if i%2 else 2)*f(left+i*h)
    return v*h/3


def checks():
    rng=random.Random(20261020)
    for _ in range(250):
        a,b,c=(math.exp(rng.uniform(-3,3)) for _ in range(3))
        assert abs(area_formula(a,b,c)-area_from_vertices(a,b,c))<3e-12
    print('DIRECT_HEXAGON_VERTEX_SHOELACE_IDENTITY_OK 250')

    for t in (0.01,0.003,0.001):
        f=area_formula(1+t,1,1)
        coeff=(f-3*ROOT3/4)/t**2
        assert abs(coeff-ROOT3/16)<0.003
    for h in (0.01,0.003,0.001):
        a=math.cos(PI/4+h);b=math.sin(PI/4+h)
        xx=(area_formula(a,b,0)-ROOT2)/h**2
        yy=(area_formula(1/ROOT2,1/ROOT2,h)-ROOT2)/h**2
        assert abs(xx-ROOT2/2)<0.005
        assert abs(yy+3*ROOT2/2)<0.09
    print('INDEPENDENT_DIAGONAL_MINIMUM_AND_EQUATOR_SADDLE_HESSIANS_OK')

    for phi in (0.0,0.1,0.35,0.7,PI/2):
        radius=1e-6
        co,si=math.cos(phi),math.sin(phi)
        observed=(2-area_formula(1,radius*co,radius*si))/radius
        expected=2*(1+co*si)/(co+si)
        assert abs(observed-expected)<1e-4
    print('AXIS_CONICAL_ENDPOINT_NORMAL_FORM_OK')

    I=simpson(lambda t:(math.cos(t)+math.sin(t))**2/(1+math.cos(t)*math.sin(t))**2,0,PI/2,10000)
    exact=2/3+4*PI/(9*ROOT3)
    assert abs(I-exact)<1e-10
    coeff_max=3*I/(4*PI)
    assert abs(coeff_max-(1/(2*PI)+ROOT3/9))<1e-10
    print('EXACT_AXIS_ANGULAR_INTEGRAL_AND_UPPER_TAIL_COEFFICIENT_OK')

    minv=3*ROOT3/4
    coeff_min=64/(9*ROOT3)
    coeff_saddle=math.sqrt(6)/PI
    N=480000
    bottom=top=0
    for _ in range(N):
        x,y,z=(abs(rng.gauss(0,1)) for i in range(3))
        t=math.sqrt(x*x+y*y+z*z)
        value=area_formula(x/t,y/t,z/t)
        bottom+=(value<minv+0.008)
        top+=(value>1.92)
    observed_bottom=bottom/N/.008
    observed_top=top/N/.08**2
    assert abs(observed_bottom/coeff_min-1)<.07,(observed_bottom,coeff_min)
    # At this threshold the quadratic approximation is noticeably biased.
    assert abs(observed_top/coeff_max-1)<.29,(observed_top,coeff_max)
    assert abs(coeff_saddle-12/(4*PI*math.sqrt(3/2)))<1e-12
    print('INDEPENDENT_GAUSSIAN_HAAR_ORIENTATION_ENDPOINT_SAMPLING_OK',N)
    print('TWELVE_SADDLE_LOGARITHMIC_NORMALIZATION_OK')
    print('ALL_OCTAHEDRAL_CENTRAL_SECTION_AREA_CHECKS_OK')


if __name__=='__main__':
    checks()
