#!/usr/bin/env python3
import math

# Coefficient-level check of
# (1+h^2)(1+y^2) - (h+y)^2 == (hy-1)^2.
# Monomials are keyed by (power_h, power_y).
left = {(0,0):1,(2,0):1,(0,2):1,(2,2):1}
sub  = {(2,0):-1,(1,1):-2,(0,2):-1}
for k,v in sub.items(): left[k]=left.get(k,0)+v
left={k:v for k,v in left.items() if v}
right={(2,2):1,(1,1):-2,(0,0):1}
assert left == right, (left,right)

def defect(h,x,y):
    s=math.sqrt(1+h*h)
    t=h-y
    R1=math.hypot(x,t)
    R2=math.hypot(x+1,y)
    R3=math.hypot(x-1,y)
    r23=2*t/s
    return (R2+R3)/r23 - 2*y/R1 - 1

def lower(h,y):
    s=math.sqrt(1+h*h)
    return (h*y-1)**2/((h-y)*(s*math.sqrt(1+y*y)+h+y))

# Deterministic stress grid spanning thin, balanced, and tall isosceles triangles.
for h in [0.15,0.3,0.6,1.0,1.2,2.0,5.0,12.0]:
    for j in range(1,40):
        y=h*j/40.0
        lim=(h-y)/h
        for k in range(-19,20):
            x=lim*k/20.0
            d=defect(h,x,y)
            L=lower(h,y)
            assert d >= -2e-12, (h,x,y,d)
            assert d+2e-12 >= L, (h,x,y,d,L)
        # exact-altitude numerical equality of the derived lower profile
        assert abs(defect(h,0.0,y)-lower(h,y)) < 2e-12

# Equality candidates: interior only for h>1 at y=1/h.
for h in [1.2,2.0,5.0]:
    y=1/h
    assert y < h
    assert abs(defect(h,0.0,y)) < 2e-12
for h in [0.2,0.7,1.0]:
    assert 1/h >= h

print('VERIFY_OK')
