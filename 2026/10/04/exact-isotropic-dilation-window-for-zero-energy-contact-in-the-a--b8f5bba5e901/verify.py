#!/usr/bin/env python3
import math


def thresholds(A,B,C):
    x,y,z=1.0/A,1.0/B,1.0/C
    M=max(x,y,z)
    sp2=4.0*(x*y+x*z+y*z)
    if x+y+z <= 2.0*M + 1e-14:
        sm2=4.0*x*y*z/M
        regime="nontriangle"
    else:
        sm2=2.0*(x*y+x*z+y*z)-(x*x+y*y+z*z)
        regime="triangle"
    return math.sqrt(sm2),math.sqrt(sp2),regime


def F(k,t1,t2,a,b,c):
    return ((3*k**4+1)*math.sin(a*k)*math.sin(b*k)*math.sin(c*k)
        +2*k*k*(k*k-1)*(math.sin(b*k)*math.cos(t2)+math.sin(c*k)*math.cos(t1)+math.sin(a*k)*math.cos(t2-t1))
        -2*k*k*(k*k+1)*(math.cos(a*k)*math.cos(b*k)*math.sin(c*k)+math.cos(b*k)*math.cos(c*k)*math.sin(a*k)+math.cos(c*k)*math.cos(a*k)*math.sin(b*k)))


def minimizing_phase(a,b,c):
    X,Y,Z=1.0/a,1.0/b,1.0/c
    if X+Y+Z >= 2.0*max(X,Y,Z)-1e-13:
        v=(Y*Y-X*X-Z*Z)/(2.0*X*Z)
        w=(Z*Z-X*X-Y*Y)/(2.0*X*Y)
        v=max(-1.0,min(1.0,v)); w=max(-1.0,min(1.0,w))
        return math.acos(w),-math.acos(v)
    j=min(range(3),key=lambda i:(a,b,c)[i])
    return [(math.pi,math.pi),(math.pi,0.0),(0.0,math.pi)][j]

# Exact special-case checks.
sm,sp,reg=thresholds(1.0,1.0,1.0)
assert reg=="triangle"
assert abs(sm-math.sqrt(3.0))<1e-12
assert abs(sp-2.0*math.sqrt(3.0))<1e-12
assert abs(sp/sm-2.0)<1e-12

# Representative reciprocal-nontriangle shape.
sm,sp,reg=thresholds(0.4,1.0,1.0)
assert reg=="nontriangle"
assert sp/sm >= math.sqrt(5.0)-1e-12

# Determinant endpoint signs. The lower minimizing phase is positive at order k^5
# while a nonminimizing phase is negative; the upper maximizing phase is positive.
# These numerical evaluations are corroborative only.
for A,B,C in [(1.0,1.0,1.0),(0.4,1.0,1.0),(1.0,1.5,2.0)]:
    sm,sp,_=thresholds(A,B,C)
    a,b,c=sm*A,sm*B,sm*C
    t1,t2=minimizing_phase(a,b,c)
    k=0.02
    assert F(k,t1,t2,a,b,c) > 0.0
    assert F(k,0.0,0.0,a,b,c) < 0.0
    a,b,c=sp*A,sp*B,sp*C
    assert F(k,0.0,0.0,a,b,c) > 0.0

# Deterministic shape grid checks of the width theorem.
checked=0
for A in [0.4,0.6,1.0,1.7,2.5]:
    for B in [0.5,0.9,1.4,2.2]:
        for C in [0.7,1.1,1.9,3.0]:
            sm,sp,reg=thresholds(A,B,C)
            assert sp/sm >= 2.0-1e-12
            if reg=="nontriangle":
                assert sp/sm >= math.sqrt(5.0)-1e-12
            checked += 1
print(f"VERIFY_OK shapes={checked} equilateral_window=[sqrt(3),2sqrt(3)) endpoint_cases=3 width_bound=2")
