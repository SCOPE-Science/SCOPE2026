#!/usr/bin/env python3
"""Consistency replay for the six-spike cap-body theorem.

This script is not a proof of the quantified theorem; RESULT.md contains the analytic proof.
"""
import math

SQ2 = math.sqrt(2.0)

def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm2(a):
    return dot(a,a)

def run_one(r):
    c=math.sqrt(1.0-r**-2)
    lo=max(c, 0.59)
    x=(lo+1.0/SQ2)/2.0
    if abs(x-1.0/math.sqrt(3.0)) < 1e-6:
        x=(2*lo+1.0/SQ2)/3.0
    assert c < x < 1.0/SQ2
    assert abs(x-1.0/math.sqrt(3.0)) > 1e-10
    s=math.sqrt(1.0-2*x*x)
    u1=(x,x,s)
    u2=(-x,s,x)
    u3=(s,-x,-x)
    u4=(-1/math.sqrt(3.0),)*3
    us=(u1,u2,u3,u4)
    for u in us:
        assert abs(norm2(u)-1.0) < 1e-12
    rel=tuple(u1[i]+u2[i]+u3[i]+math.sqrt(3.0)*s*u4[i] for i in range(3))
    assert max(abs(z) for z in rel) < 1e-12
    d=det3(u1,u2,u3)
    assert abs(d - s*(3*x*x-1.0)) < 1e-12
    assert abs(d) > 1e-10
    # +e1,-e1,+e2,-e2,+e3,-e3 witnesses: u2,u1,u3,u1,u3,u2
    signed=(-u2[0], u1[0], -u3[1], u1[1], -u3[2], u2[2])
    # Each entry is the positive magnitude x; corresponding signed coordinate is -x<-c.
    for mag in signed:
        assert mag > c

for r in (1.001,1.05,1.2,1.35,1.4,math.sqrt(2.0)-1e-6):
    run_one(r)

c_end=math.sqrt(1.0-(math.sqrt(2.0))**-2)
assert abs(c_end-1.0/math.sqrt(2.0)) < 1e-15
# Strictly exceeding c_end in two coordinates would force norm^2 > 2*c_end^2 = 1.
assert abs(2*c_end*c_end-1.0) < 1e-15
print('VERIFY_OK six-spike octahedral cap-body phase transition')
