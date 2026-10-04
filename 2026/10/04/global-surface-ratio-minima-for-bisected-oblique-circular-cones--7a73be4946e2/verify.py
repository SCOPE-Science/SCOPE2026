#!/usr/bin/env python3
import math

def bisect(f, lo, hi, n=200):
    flo=f(lo); fhi=f(hi)
    assert flo < 0 < fhi
    for _ in range(n):
        mid=(lo+hi)/2
        fm=f(mid)
        if fm < 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

pi=math.pi
xL=bisect(lambda x: 2*x-pi*math.cos(x), 0.0, pi/2)
xT=bisect(lambda x: 2*x-2*pi*math.cos(x)+pi, 0.0, pi/2)
aL=1/math.sin(xL)
aT=1/math.sin(xT)

RLx=lambda x:(4*math.cos(x)+4*x*math.sin(x)-pi*math.sin(x)-2)/(pi*math.sin(x)+2)
RTx=lambda x:(-1+2*math.cos(x)+2*x*math.sin(x))/(1+pi*math.sin(x))
ROx=lambda x:(2*math.cos(x)+2*x*math.sin(x))/(pi*math.sin(x)+2)

def arcsec(a): return math.acos(1/a)
def arccsc(a): return math.asin(1/a)
def RLa(a): return (pi-2*a+4*math.sqrt(a*a-1)-4*arcsec(a))/(pi+2*a)
def RTa(a): return (-a+2*math.sqrt(a*a-1)+2*arccsc(a))/(pi+a)
def ROa(a): return (2*math.sqrt(a*a-1)+2*arccsc(a))/(pi+2*a)

mL=4*xL/pi-1
mT=2*xT/pi
mO=2*xL/pi
assert abs(RLx(xL)-mL) < 2e-15
assert abs(RTx(xT)-mT) < 2e-15
assert abs(ROx(xL)-mO) < 2e-15
assert abs(RLa(aL)-mL) < 2e-14
assert abs(RTa(aT)-mT) < 2e-14
assert abs(ROa(aL)-mO) < 2e-14
assert abs(aL-1.2437608987462040) < 2e-15
assert abs(aT-1.4782960807222794) < 2e-15
assert abs(mL-0.18922328811367117) < 2e-15
assert abs(mT-0.47296889648303337) < 2e-15
assert abs(mO-0.59461164405683558) < 2e-15
print('x_L = %.17g' % xL)
print('a_L = %.17g' % aL)
print('inf lateral = %.17g' % mL)
print('inf overlap = %.17g' % mO)
print('x_T = %.17g' % xT)
print('a_T = %.17g' % aT)
print('inf total = %.17g' % mT)
print('VERIFY_OK')
