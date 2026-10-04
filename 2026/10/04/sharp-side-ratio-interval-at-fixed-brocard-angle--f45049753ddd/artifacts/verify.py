#!/usr/bin/env python3
import math

def bounds(q):
    lo=(1+math.sqrt(2)*q)/(1-q/math.sqrt(2))
    hi=(1+q*q+q*math.sqrt(3*(2-q*q)))/(1-2*q*q)
    return lo,hi

max_low=0.0
max_high=0.0
max_qerr=0.0
max_constraint=0.0
min_triangle=1e9
checks=0
qs=[0.0]+[0.705*k/140 for k in range(1,141)]
for q in qs:
    lo,hi=bounds(q)
    # endpoint classes
    x=(1+math.sqrt(2)*q)/3
    y=z=(1-q/math.sqrt(2))/3
    max_low=max(max_low,abs(x/z-lo))
    s=(2-q*q)/3
    xm=(s+q*math.sqrt(s))/2
    zm=(s-q*math.sqrt(s))/2
    ym=(1+q*q)/3
    max_high=max(max_high,abs(xm/zm-hi))
    # Brocard conversion round trip
    tanw=math.sqrt(max(0.0,(1-2*q*q)/3))
    q2=math.sqrt(max(0.0,(1-3*tanw*tanw)/2))
    max_qerr=max(max_qerr,abs(q-q2))
    A=math.sqrt(2)*q/3
    for k in range(1440):
        th=2*math.pi*k/1440
        vals=[1/3+A*math.cos(th),1/3+A*math.cos(th-2*math.pi/3),1/3+A*math.cos(th+2*math.pi/3)]
        vals.sort(reverse=True)
        X,Y,Z=vals
        max_constraint=max(max_constraint,abs(X+Y+Z-1),abs((X-Y)**2+(Y-Z)**2+(Z-X)**2-q*q))
        ratio=X/Z
        if ratio < lo-5e-12 or ratio > hi+5e-10:
            raise AssertionError((q,ratio,lo,hi))
        a,b,c=map(math.sqrt,vals)
        min_triangle=min(min_triangle,b+c-a)
        if b+c <= a:
            raise AssertionError(('triangle',q,vals))
        checks += 1
print('VERIFY_OK')
print('checks',checks)
print('max_lower_endpoint_error',f'{max_low:.3e}')
print('max_upper_endpoint_error',f'{max_high:.3e}')
print('max_q_roundtrip_error',f'{max_qerr:.3e}')
print('max_constraint_error',f'{max_constraint:.3e}')
print('minimum_sampled_triangle_margin',f'{min_triangle:.3e}')
