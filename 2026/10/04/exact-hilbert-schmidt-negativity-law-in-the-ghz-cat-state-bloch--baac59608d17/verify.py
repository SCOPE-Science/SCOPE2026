#!/usr/bin/env python3
import math


def simpson(f, a, b, n=200000):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a) + f(b)
    for k in range(1,n):
        s += (4 if k % 2 else 2) * f(a+k*h)
    return s*h/3


def density(e):
    if e < 0 or e > 0.5:
        return 0.0
    return 12.0*e*math.sqrt(max(0.0,1.0-4.0*e*e))


def cdf(e):
    if e <= 0:
        return 0.0
    if e >= 0.5:
        return 1.0
    return 1.0-(1.0-4.0*e*e)**1.5

norm = simpson(density,0.0,0.5)
mean = simpson(lambda e:e*density(e),0.0,0.5)
second = simpson(lambda e:e*e*density(e),0.0,0.5)
assert abs(norm-1.0) < 2e-8, norm
assert abs(mean-3.0*math.pi/32.0) < 2e-8, mean
assert abs(second-0.1) < 2e-8, second

for e in (0.03,0.11,0.23,0.37,0.47):
    h=1e-6
    deriv=(cdf(e+h)-cdf(e-h))/(2*h)
    assert abs(deriv-density(e)) < 2e-8, (e,deriv,density(e))

# Conditional-to-marginal identity. At fixed radius r, E has density
# 4e/(r^2 sqrt(1-4e^2/r^2)); the HS radius density is 3r^2.
for e in (0.02,0.08,0.17,0.31,0.44):
    lo=2*e
    if lo < 1.0:
        # substitute r=sqrt(lo^2+t^2), t in [0,sqrt(1-lo^2)]
        # which removes the integrable lower-end square-root singularity.
        top=math.sqrt(1-lo*lo)
        val=simpson(lambda t:12.0*e,0.0,top,20000)
        assert abs(val-density(e)) < 2e-8, (e,val,density(e))

# Check integer moments both directly and through independent radial/angular factors.
# E^q = 2^-q R^q (1-Z^2)^(q/2), R and Z independent,
# f_R(r)=3r^2 and Z uniform on [-1,1].
for q in range(1,9):
    direct=simpson(lambda e:(e**q)*density(e),0.0,0.5)
    er=3.0/(q+3.0)
    ez=simpson(lambda z:0.5*((1.0-z*z)**(q/2.0)),-1.0,1.0,100000)
    fact=(2.0**(-q))*er*ez
    assert abs(direct-fact) < 3e-8, (q,direct,fact)

print('VERIFY_OK norm=1 mean=3pi/32 second=1/10 derivative=5 conditional=5 moments=8')
