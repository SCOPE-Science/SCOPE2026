"""Exact algebra and finite diagnostic checks for the order-eight Fourier five-band theorem.
Run with Python 3; uses only the standard library.
"""
from fractions import Fraction
import cmath
import math
import random


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def add(*polys):
    n=max(map(len,polys)); c=[0]*n
    for p in polys:
        for i,v in enumerate(p): c[i]+=v
    return c


def scale(a,c): return [c*x for x in a]

# Let w=u^2=A/B, A=2(v^4+3v^3+6v+2), B=3(v^2+4v+2).
A=[4,12,0,6,2]
B=[6,12,3]
P=[-2,-7,0,4,1]
Q=[20,48,12,24,7]
# Numerator of the v-stationarity equation after putting w=A/B.
left=add(mul([6,3],mul(A,A)),mul([6,0,-9,-2],mul(A,B)),mul([0,2,0,-2],mul(B,B)))
right=scale(mul(P,Q),-6)
assert left[:len(right)]==right and not any(left[len(right):]),(left,right)
# Rational localization, uniqueness follows from Descartes' one sign change.
def p(v): return v**4+4*v**3-7*v-2
lo=Fraction(1274598,1000000);hi=Fraction(1274600,1000000)
assert p(lo)<0<p(hi)
for _ in range(100):
    mid=(lo+hi)/2
    if p(mid)<0:lo=mid
    else:hi=mid
v=float((lo+hi)/2)
u2=2*(v**4+3*v**3+6*v+2)/(3*(v*v+4*v+2))
u=math.sqrt(u2)
K=(6*u**4+12*u*u*v*v+24*u*u*v+24*u*u+v**4+12*v*v+8)/(2+2*u*u+v*v)**2
assert 3.52790<K<3.52791 and 1.18<u<1.20

def mom_convolution(c):
    v=[0j]*8
    for i,x in enumerate(c):
        for j,y in enumerate(c):v[(i+j)%8]+=x*y
    return sum(abs(x)**2 for x in v)

def mom_direct(c):
    return sum(abs(sum(c[j]*cmath.exp(2j*math.pi*j*k/8) for j in range(5)))**4 for k in range(8))/8

# Exact convolution-energy polynomial for symmetric real inputs.
for x in range(1,4):
    for y in range(0,4):
        for z in range(0,4):
            c=[x,y,z,y,x]
            expected=(6*y**4+12*y*y*z*z+24*x*y*y*z+24*x*x*y*y+z**4+12*x*x*z*z+8*x**4)
            assert mom_convolution(c)==expected, (c,mom_convolution(c),expected)

rng=random.Random(178403)
for _ in range(3000):
    c=[complex(rng.randint(-4,4),rng.randint(-4,4)) for _ in range(5)]
    direct=mom_direct(c); conv=mom_convolution(c)
    assert abs(direct-conv)<1e-7*(1+conv)
    energy=sum(abs(x)**2 for x in c)
    assert conv<=K*energy**2+1e-7*(1+conv)

# Eight projective maximizers: phase rotations by characters, not all real rotations.
for k in range(8):
    c=[(1 if j in (0,4) else u if j in (1,3) else v)*cmath.exp(2j*math.pi*k*j/8) for j in range(5)]
    energy=sum(abs(x)**2 for x in c)
    assert abs(mom_convolution(c)/energy**2-K)<1e-11

# Confirm strict sampled-to-continuous discrepancy at the optimizer.
assert 3.5279<K<3.528
print('VERIFY_OK',format(v,'.15f'),format(u,'.15f'),format(K,'.15f'),'checks',3000+8+48)
