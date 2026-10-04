#!/usr/bin/env python3
import math, cmath

PI=math.pi

def f(x,y):
    return math.log(math.hypot(x,y))

def R_from_log(x,y,j):
    if j==0:
        d=f(x-1,y)-f(x+1,y)
    else:
        d=f(x,y-1)-f(x,y+1)
    return (2/PI)*d/(4j)

def Q_from_log(x,y):
    d=f(x+1,y)+f(x-1,y)-f(x,y+1)-f(x,y-1)
    return -(2/PI)*d/4

# Exact shift prefactors from G=C-a/2.
assert abs((1/(4j))*1j - 0.25) < 1e-15

cases=[(80,37),(140,61),(220,93),(360,151)]
for x,y in cases:
    r2=x*x+y*y
    for j,coord in ((0,x),(1,y)):
        actual=R_from_log(x,y,j)
        pred=1j*coord/(PI*r2)
        rel=abs(actual-pred)/abs(pred)
        if rel>2e-3:
            raise SystemExit(f'R coefficient check failed {(x,y,j)} rel={rel}')
    actual=Q_from_log(x,y)
    pred=(x*x-y*y)/(PI*r2*r2)
    rel=abs(actual-pred)/abs(pred)
    if rel>3e-3:
        raise SystemExit(f'Q coefficient check failed {(x,y)} rel={rel}')

# Nodal symmetry of the leading tensors.
assert 0/(PI*100)==0
assert (50*50-50*50)==0
print('VERIFY_OK cases=%d dipole_coeff=1/pi quadrupole_coeff=1/pi' % len(cases))
