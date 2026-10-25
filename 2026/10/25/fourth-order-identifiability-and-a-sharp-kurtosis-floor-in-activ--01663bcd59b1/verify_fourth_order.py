#!/usr/bin/env python3
"""Independent algebraic and covariance-operator checks for an OU-product velocity theorem."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad

count = 0

def check(condition, label):
    global count
    if not condition:
        raise AssertionError(label)
    count += 1

a, b, t, q, z = sp.symbols('a b t q z', positive=True)
# Independently expand the nine Wick pairing combinations at two times.
x, y = sp.symbols('x y', positive=True)
raw_4 = (1 + 2*x*x) * (1 + 2*y*y)
connected = sp.expand(raw_4 - 1 - 2*x*x*y*y)
check(sp.simplify(connected - 2*(x*x + y*y + x*x*y*y)) == 0,
      'connected Gaussian product fourth moment')

# Independently differentiate the free quadratic generating rate.
f = (a+b-sp.sqrt(a*a+b*b+2*sp.sqrt(a*a*b*b-4*a*b*q*z*z)))/2
k2 = sp.factor(sp.diff(f,z,2).subs(z,0))
k4 = sp.factor(sp.diff(sp.series(f,z,0,6).removeO(),z,4).subs(z,0))
check(sp.factor(k2 - 2*q/(a+b)) == 0,'second scaled cumulant')
check(sp.simplify(k4 - 24*q*q*(a*a+3*a*b+b*b)/(a*b*(a+b)**3)) == 0,
      'fourth scaled cumulant')

# Independently evaluate the Fourier integral of two squared OU spectra.
tr = 4*(a*a+3*a*b+b*b)/(a*b*(a+b)**3)
check(sp.simplify(6*q*q*tr-k4) == 0, 'trace/spectral cumulant agreement')

for av in (0.3,0.6,1.0,1.7,2.4):
 for bv in (0.4,0.8,1.0,1.3,3.1):
  for tv in (0.17,0.75,1.9):
   r = math.exp(-(av+bv)*tv)
   F = math.exp(-2*av*tv)+math.exp(-2*bv*tv)+r*r
   S = F-r*r
   discr = max(0.0,S*S-4*r*r)
   roots = sorted(((S-math.sqrt(discr))/2,(S+math.sqrt(discr))/2))
   expect = sorted((math.exp(-2*av*tv),math.exp(-2*bv*tv)))
   check(max(abs(roots[j]-expect[j]) for j in range(2)) < 4e-8,
         'single-lag inverse reconstruction')
   check(F>=3*r*r-1e-12, 'sharp fourth-order inequality')
   ratio = 6*(av*av+3*av*bv+bv*bv)/(av*bv*(av+bv))
   floor = 30/(av+bv)
   check(ratio>=floor-1e-10,'kurtosis floor under fixed persistence')

for av,bv in ((0.4,0.4),(0.6,1.7),(2.5,0.7),(0.9,3.1),(1.8,1.8)):
    # Direct spectral integral, independent of closed rational differentiation.
    fnum = lambda w: ((2*av/(av*av+w*w))**2)*((2*bv/(bv*bv+w*w))**2)
    integral = quad(fnum,0,math.inf,epsabs=5e-11,epsrel=5e-11)[0]/math.pi
    direct = 4*(av*av+3*av*bv+bv*bv)/(av*bv*(av+bv)**3)
    check(abs(integral/direct-1)<1e-9,'Fourier integral vs rational coefficient')

# Direct finite-interval matrix covariance traces, not using the generating rate.
for av,bv in ((0.6,1.8),(1.1,1.1),(2.2,0.5)):
    T=30.0
    n=240
    ts=(np.arange(n)+.5)*(T/n)
    distance=np.abs(ts[:,None]-ts[None,:])
    Ka=(T/n)*np.exp(-av*distance)
    Kb=(T/n)*np.exp(-bv*distance)
    P=Ka@Kb
    variance_discrete=np.trace(P)
    cumulant_discrete=6*np.trace(P@P)
    second_rate=2/(av+bv)
    fourth_rate=24*(av*av+3*av*bv+bv*bv)/(av*bv*(av+bv)**3)
    check(variance_discrete>0 and cumulant_discrete>0,'strict positivity')
    check(abs(variance_discrete/T/second_rate-1)<.09,'large-time variance rate')
    check(abs(cumulant_discrete/T/fourth_rate-1)<.15,'large-time fourth cumulant rate')

print(f'PASS: {count} symbolic and numerical assertions')
