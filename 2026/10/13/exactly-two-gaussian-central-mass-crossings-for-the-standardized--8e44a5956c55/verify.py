#!/usr/bin/env python3
import math

SQRT2 = math.sqrt(2.0)
SQRT2PI = math.sqrt(2.0*math.pi)

def Phi(x):
    return 0.5*(1.0 + math.erf(x/SQRT2))

def phi(x):
    return math.exp(-0.5*x*x)/SQRT2PI

def D(c):
    if c <= 1.0:
        return 2.0*math.sinh(c)/math.e - (2.0*Phi(c)-1.0)
    return 2.0*(1.0-Phi(c)) - math.exp(-1.0-c)

def bisect(a,b,n=100):
    fa=D(a)
    fb=D(b)
    assert fa*fb < 0.0
    for _ in range(n):
        m=(a+b)/2.0
        fm=D(m)
        if fa*fm <= 0.0:
            b=m
            fb=fm
        else:
            a=m
            fa=fm
    return (a+b)/2.0

cminus=bisect(0.1,0.9)
cplus=bisect(1.1,3.0)

assert 0.49616854 < cminus < 0.49616856
assert 1.93298728 < cplus < 1.93298730
assert D(0.49616854) < 0.0 < D(0.49616856)
assert D(1.93298728) > 0.0 > D(1.93298730)

# Source-highlighted and structural representative points.
assert D(0.25) < 0.0
assert D(0.5) > 0.0
assert D(1.0) > 0.0
assert D(1.5) > 0.0
assert D(2.0) < 0.0
assert D(3.0) < 0.0

# Deterministic grid replay of the proved sign regions.
for i in range(1,2000):
    c=3.0*i/2000.0
    val=D(c)
    if c < cminus-1e-6:
        assert val < 0.0
    elif cminus+1e-6 < c < cplus-1e-6:
        assert val > 0.0
    elif c > cplus+1e-6:
        assert val < 0.0

# Numerical replay of monotonic derivative-control ratios.
prev=math.exp(-1.0)/phi(0.0)
for i in range(1,1001):
    c=i/1000.0
    cur=math.exp(-1.0)*math.cosh(c)/phi(c)
    assert cur > prev
    prev=cur

prev=math.exp(-2.000001)/(2.0*phi(1.000001))
for i in range(1,1001):
    c=1.000001 + 4.0*i/1000.0
    cur=math.exp(-1.0-c)/(2.0*phi(c))
    assert cur > prev
    prev=cur

print(f"VERIFY_OK c_minus={cminus:.12f} c_plus={cplus:.12f} D1={D(1.0):.12f}")
