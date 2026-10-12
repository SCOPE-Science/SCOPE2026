#!/usr/bin/env python3
import math

def H(x):
    s=math.sqrt(5.0)
    return math.exp((3.0-s)*x)-math.exp((1.0-s)*x)-1.0-math.exp(-2.0*s*x)

def concurrence_x(x):
    z=2.0*math.exp(2*x)+2.0*math.exp(-2*x)
    l1=math.exp(2*x)/z
    l2=math.exp(-2*x)/z
    l3=math.exp(-2*x)/z
    l4=math.exp(2*x)/z
    return max(abs(l1-l4)-l2-l3,0.0)

def concurrence_y(x):
    s=math.sqrt(5.0)
    ws=[1.0, math.exp(2*x), math.exp((s-1)*x), math.exp(-(s+1)*x)]
    z=sum(ws)
    # Jx <= Jz branch: |lambda2-lambda3|-lambda1-lambda4
    return max(abs(ws[1]-ws[2])-ws[0]-ws[3],0.0)/z

for x in (0.1,0.5,1.0,2.0,7.0):
    assert concurrence_x(x) == 0.0

lo,hi=0.0,2.0
assert H(lo)<0.0 and H(hi)>0.0
for _ in range(100):
    mid=(lo+hi)/2.0
    if H(mid)>0.0: hi=mid
    else: lo=mid
root=(lo+hi)/2.0
assert 0.58258 < root < 0.58259
cy=concurrence_y(1.0)
assert cy > 0.2449 and cy < 0.2450
assert H(0.5)<0.0 and H(1.0)>0.0
print(f"VERIFY_OK root={root:.16f} Tc_over_a={1/root:.16f} Cx_at_x1={concurrence_x(1.0):.16f} Cy_at_x1={cy:.16f}")
