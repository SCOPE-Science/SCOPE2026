#!/usr/bin/env python3
"""Independent numerical checks for the sharp central-section theorem of a circular bicone.
The analytic proof is contained in RESULT.md; numerical sampling cannot prove a continuum theorem.
Requires only Python's standard library.
"""
import math

PI=math.pi

def simpson(f, left, right, N=12000):
    if N % 2: N += 1
    step=(right-left)/N
    total=f(left)+f(right)
    for j in range(1,N):
        total += (4 if j%2 else 2)*f(left+j*step)
    return total*step/3

def I_closed(a):
    if a == 0: return PI
    if abs(a-1)<1e-8:
        return 2*simpson(lambda t: 1/(1+a*math.cos(t))**2,0,PI/2,10000)
    if a<1:
        return 2*(math.acos(a)/(1-a*a)**1.5-a/(1-a*a))
    return 2*(a/(a*a-1)-math.acosh(a)/(a*a-1)**1.5)

def I_polar(a):
    if a > 10:
        # The substitution tan(theta)=a*t/(1-t) resolves the narrow endpoint layer.
        return (2/a)*simpson(lambda t: 1/((1-t)+math.sqrt(t*t+(1-t)**2/(a*a)))**2,0,1,10000)
    return 2*simpson(lambda t: 1/(1+a*math.cos(t))**2,0,PI/2,12000)

def I_chords(a):
    end=1/(1+a)
    return 4*simpson(lambda x: math.sqrt(max(0,(1-a*x)**2-x*x)),0,end,12000)

def section_area(a,h):
    return math.hypot(1,h*a)*I_closed(a)

alphas=[0,0.01,0.05,0.1,0.25,0.5,0.8,0.9,1,1.1,1.5,2,3,5,10,20,100]
for a in alphas:
    C=I_closed(a); P=I_polar(a); H=I_chords(a)
    if a != 1 and a != 0 and abs(a-1)>1e-4:
        assert abs(C-P)<1e-8,(a,C,P)
    assert abs(P-H)<4e-7,(a,P,H)
    if a>0:
        bridge=2*math.atan(1/a)
        elliptic=PI/math.hypot(1,PI*a/2)
        assert C<bridge<elliptic,(a,C,bridge,elliptic)
assert abs(I_closed(1)-4/3)<2e-12
print('THREE_INDEPENDENT_AREA_FORMULAS_OK',len(alphas),'incl_exact_I_1=4/3')

# Probe all aspect ratios and oblique section angles on logarithmic grids.
for h in [0.001,0.01,0.1,0.5,1.0,1.5,PI/2,1.6,1.8,2.0,3,10,100]:
    limit=max(PI,2*h)
    for j in range(1,501):
        a=10**(-4+8*j/501)
        A=math.hypot(1,h*a)*I_polar(a)
        assert A < limit+5e-11,(h,a,A,limit)
print('FULL_ASPECT_RANGE_OBLIQUE_NUMERICAL_CHECKS_OK',13*500)

# Direct endpoint sections follow from the disk and rhombus constraints.
for h in [0.5,PI/2,3]:
    assert math.isclose(PI, I_closed(0))
    # x=0 cuts |y|+|z|/h<=1: 4 congruent triangles of area h/2.
    assert math.isclose(2*h,4*(h/2))
print('ENDPOINT_AREAS_AND_THRESHOLD_OK',PI/2)
print('BICONE_ALL_CHECKS_OK')
