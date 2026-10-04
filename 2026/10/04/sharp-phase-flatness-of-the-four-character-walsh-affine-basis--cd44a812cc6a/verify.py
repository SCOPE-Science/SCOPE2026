#!/usr/bin/env python3
import cmath, itertools, math, random

SQRT2 = math.sqrt(2.0)
target_hi = 4.0 + 2.0 * SQRT2
target_lo = 4.0 - 2.0 * SQRT2

# Exact Q(sqrt(2)) arithmetic as pairs a+b*sqrt(2).
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def neg(x): return (-x[0],-x[1])
def eq(x,y): return x==y

# Coefficients are represented by real/imaginary Q(sqrt(2)) pairs.
# 1, exp(i*pi/4), i, exp(3i*pi/4).
zero=(0,0); one=(1,0); halfroot=(0,1/2)
cs=[
    (one,zero),
    (halfroot,halfroot),
    (zero,one),
    (neg(halfroot),halfroot),
]

def cadd(z,w): return (add(z[0],w[0]),add(z[1],w[1]))
def cscale(s,z): return (z[0] if s==1 else neg(z[0]), z[1] if s==1 else neg(z[1]))
def norm2(z): return add(mul(z[0],z[0]),mul(z[1],z[1]))

levels=[]
for eps in itertools.product((-1,1), repeat=3):
    z=cs[0]
    for e,c in zip(eps,cs[1:]): z=cadd(z,cscale(e,c))
    levels.append(norm2(z))
hi=(4,2); lo=(4,-2)
assert sum(eq(v,hi) for v in levels)==4
assert sum(eq(v,lo) for v in levels)==4
assert all(eq(v,hi) or eq(v,lo) for v in levels)

# sin^2(pi/8)=(2-sqrt(2))/4; multiply by 4+2sqrt(2) and get 1.
sin2=(1/2,-1/4)
assert eq(mul(sin2,hi),one)

# Deterministic corroborative stress only.
rng=random.Random(27061)
worst=float('inf')
for _ in range(5000):
    phases=[rng.random()*2*math.pi for _ in range(4)]
    coeff=[cmath.exp(1j*t) for t in phases]
    m=0.0
    for eps in itertools.product((-1,1), repeat=3):
        z=coeff[0]+sum(e*c for e,c in zip(eps,coeff[1:]))
        m=max(m,abs(z)**2)
    worst=min(worst,m)
    assert m >= target_hi - 1e-10
print('VERIFY_OK exact_levels=8 multiplicities=4,4 random_stress=5000 min_seen=%.12f target=%.12f' % (worst,target_hi))
