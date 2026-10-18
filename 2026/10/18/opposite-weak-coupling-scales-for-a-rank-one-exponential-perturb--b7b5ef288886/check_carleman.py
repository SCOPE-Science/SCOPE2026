#!/usr/bin/env python3
"""Numerical cross-checks for exact rank-one Carleman secular formulas.

Only Python standard-library modules are needed. The mathematical theorem is
proved analytically; numerical sampling is not used to certify uniqueness.
"""
import math

PI = math.pi
checks = 0

def test(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def F(z):
    if z > PI:
        return (4 / (PI * math.sqrt((z - PI)*(z + PI)))
                * math.atan(math.sqrt((z + PI)/(z - PI))))
    if z >= 0:
        raise ValueError('Exterior real spectral parameter only')
    a = -z
    if a < PI:
        r = math.sqrt((PI - a)/(PI + a))
        # Stable artanh expression: avoids subtraction of nearly equal numbers.
        lr = math.log((PI+a)*(1+r)**2/(2*a))
        return -2*lr/(PI*math.sqrt((PI-a)*(PI+a)))
    if a == PI:
        return -2/PI**2
    return (-4/(PI*math.sqrt((a-PI)*(a+PI)))
            * math.atan(math.sqrt((a-PI)/(a+PI))))

def simpson(f, a, b, n=12000):
    assert n % 2 == 0
    h = (b-a)/n
    acc = f(a)+f(b)
    for j in range(1,n):
        acc += (4 if j % 2 else 2)*f(a+j*h)
    return acc*h/3

def direct(z):
    return simpson(lambda t: 1/(z - PI*math.cos(t)),
                   -PI/2, PI/2)/PI

# Independent angular quadrature at both spectral ends, away from singularities.
for z in [PI+.15,PI+.5,PI+1,PI+3,PI+7,2*PI,6*PI,
          -.03,-.07,-.2,-.8,-1.7,-PI,-5,-10,-40]:
    test(abs(F(z)-direct(z)) < 1e-8, 'Closed form versus quadrature')
    test(F(z)*(1 if z>0 else -1)>0, 'Exterior resolvent sign')

# Simple signed Stieltjes monotonicity is tested, not inferred from sampling.
for za,zb in [(PI+.001,PI+.1),(PI+.1,PI+3),(PI+3,PI+50),
              (-50,-10),(-10,-PI),(-PI,-.1),(-.1,-.001)]:
    test(F(za)>F(zb), 'Exterior resolvent is decreasing')

test(abs((3*PI*math.sqrt(3)/4)*F(2*PI)-1)<2e-14,
     'Positive exact coupling landmark')
test(abs((-PI**2/2)*F(-PI)-1)<2e-14,
     'Negative exact coupling landmark')

# Implicit-function inversion with bisection (not a proof of existence).
def solve(gamma):
    assert gamma != 0
    if gamma > 0:
        lo,hi = PI+1e-11, max(2*PI, gamma+2*PI)
        while gamma*F(hi)>1:
            hi *= 2
    else:
        lo,hi = -max(2*PI,-gamma+2*PI),-1e-11
        while gamma*F(lo)>1:
            lo*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if (gamma*F(mid)>1) == (gamma>0):
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

for gamma in [.1,.2,.4,.7,1,2,5,10,100,-.3,-.6,-1,-2,-5,-10,-100]:
    z=solve(gamma)
    test((z>PI) if gamma>0 else (z<0), 'Eigenvalue on correct side')
    test(abs(gamma*F(z)-1)<2e-8, 'Secular equation residual')

# Recover leading two-edge scales from the closed resolvent formula.
for delta in [1e-3,1e-4,1e-5]:
    gam=1/F(PI+delta)
    test(abs(delta/gam**2-2/PI)<.025, 'Quadratic upper edge')
for a in [math.exp(-9), math.exp(-13), math.exp(-17)]:
    kap=-1/F(-a)
    a0=2*PI*math.exp(-PI*PI/(2*kap))
    test(abs(a/a0-1)<1e-4, 'Exponential lower edge')

# First resolvent moment and strong-coupling shift.
wint=simpson(lambda x: 1/math.cosh(PI*x),-8,8,n=12000)
moment=simpson(lambda x: PI/(math.cosh(PI*x)**2),-8,8,n=12000)
test(abs(wint-1)<1e-9,'Spectral-vector normalization')
test(abs(moment-2)<1e-9,'First Carleman moment')
for gam in [1000,-1000]:
    test(abs(solve(gam)-gam-2)<.01, 'Strong coupling first moment')

print('PASS: %d independent finite numerical consistency assertions' % checks)
