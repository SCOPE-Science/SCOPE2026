#!/usr/bin/env python3
import math

def closed_I(m):
    if m == 1:
        return math.pi/2
    return 2*m/(m*m-1)/math.tan(math.pi/(2*m))

def anti(m, x):
    return math.sin((m-1)*x)/(2*(m-1)) - math.sin((m+1)*x)/(2*(m+1))

def partition_I(m):
    if m == 1:
        return math.pi/2
    s=0.0
    a=math.pi/m
    for k in range(m):
        s += ((-1)**k)*(anti(m,(k+1)*a)-anti(m,k*a))
    return s

def norm_formula(m):
    return (2*m/math.pi)*closed_I(m)

def midpoint_norm(m, steps=240000):
    h=math.pi/steps
    total=0.0
    for j in range(steps):
        x=(j+0.5)*h
        total += abs(math.sin(m*x))*math.sin(x)
    return (2*m/math.pi)*h*total

mx=0.0
for m in range(2,501):
    err=abs(partition_I(m)-closed_I(m))
    mx=max(mx,err)
    if err>2e-12:
        raise AssertionError((m,err))

quad_cases=(1,2,3,4,5,10,20,40)
qerr=0.0
for m in quad_cases:
    e=abs(midpoint_norm(m)-norm_formula(m))
    qerr=max(qerr,e)
    if e>3e-5:
        raise AssertionError((m,e))

ratio=norm_formula(2000)/2000
target=8/(math.pi**2)
if abs(ratio-target)>5e-7:
    raise AssertionError((ratio,target))
print(f"VERIFY_OK partition_m=2..500 max_partition_err={mx:.3e} quadrature_cases={len(quad_cases)} max_quad_err={qerr:.3e} ratio_m2000={ratio:.12f} target={target:.12f}")
