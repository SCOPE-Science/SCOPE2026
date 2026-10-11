#!/usr/bin/env python3
import math
import random
import sympy as sp

t = sp.symbols("t", positive=True)
q = t/4
s = sp.sqrt(1-2*t)
r = (1-s)/2
g = sp.symbols("g", positive=True)

I1 = sp.integrate((1-g)/2-q/g, (g, r, sp.sqrt(q)))
I2 = sp.integrate((1-g)/2-g, (g, sp.sqrt(q), sp.Rational(1,3)))
Fint = sp.simplify(12*(I1+I2))
F = sp.Rational(3,2)*s-sp.Rational(1,2) + sp.Rational(3,2)*t*sp.log(2*(1-s)/(1+s))

Falt = sp.Rational(3,2)*s-sp.Rational(1,2) + sp.Rational(3,2)*t*(2*sp.log(1-s)-sp.log(t))
assert sp.simplify(Fint-Falt) == 0
# On 0<t<4/9 all arguments are positive, and the two logarithm
# forms agree because t=(1-s)(1+s)/2.
assert sp.simplify(2*(1-s)/(1+s) - (1-s)**2/t) == 0
assert sp.simplify(sp.limit(F, t, sp.Rational(4,9), dir="-")) == 0
assert sp.simplify(sp.limit(F, t, 0, dir="+")) == 1

series = sp.series(F, t, 0, 3)
expected = 1 + sp.Rational(3,2)*t*sp.log(t) - sp.Rational(3,2)*t + sp.Rational(3,4)*t**2
assert sp.simplify(series.removeO()-expected) == 0

def formula(x):
    ss=math.sqrt(1-2*x)
    return 1.5*ss-0.5+1.5*x*math.log(2*(1-ss)/(1+ss))

random.seed(2068)
N=400000
levels=[0.02,0.10,0.20,0.30,0.40]
counts=[0]*len(levels)
for _ in range(N):
    e=[-math.log(max(random.random(),1e-300)) for _ in range(3)]
    z=sum(e)
    a,b,c=[v/z for v in e]
    depth=4*min(a*b,b*c,c*a)
    for j,lev in enumerate(levels):
        if depth >= lev:
            counts[j]+=1

for lev,cnt in zip(levels,counts):
    empirical=cnt/N
    exact=formula(lev)
    assert abs(empirical-exact) < 0.0045, (lev,empirical,exact)

print("VERIFY_OK")
print("symbolic_integral_identity = passed")
print("endpoint_and_series = passed")
print("monte_carlo_points =", N)
for lev,cnt in zip(levels,counts):
    print("level", lev, "empirical", cnt/N, "exact", formula(lev))
