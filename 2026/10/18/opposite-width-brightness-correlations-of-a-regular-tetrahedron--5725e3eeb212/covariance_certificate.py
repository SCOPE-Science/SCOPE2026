"""Exact rational interval certificate for spherical width--brightness covariance.

Only Python's standard library is needed. Fractions and integer square roots are exact.
"""
from fractions import Fraction as F
from math import isqrt

PREC=10**16

def sqrt_bounds(n):
    r=isqrt(n*PREC**2)
    return (F(r,PREC),F(r+1,PREC))

def add(a,b):
    return a[0]+b[0],a[1]+b[1]
def neg(a):
    return (-a[1],-a[0])
def sub(a,b):
    return add(a,neg(b))
def mul(a,b):
    products=[x*y for x in a for y in b]
    return min(products),max(products)
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def const(x):
    x=F(x)
    return x,x
def atan_bounds_positive(t,n=28):
    # Leibniz alternating series for arctan, bracketed by even and odd truncations.
    assert 0<=t[0]<=t[1]<1
    def series(x):
        acc=F(0)
        for k in range(n):
            acc+=(-1)**k*x**(2*k+1)/F(2*k+1)
        return acc
    # n even -> lower; odd n+1 -> upper
    assert n%2==0
    return series(t[0]),series(t[1])+t[1]**(2*n+1)/F(2*n+1)

sqrt2=sqrt_bounds(2)
sqrt3=sqrt_bounds(3)
sqrt6=sqrt_bounds(6)
pi=sub(mul(const(16),atan_bounds_positive(const(F(1,5)),28)),mul(const(4),atan_bounds_positive(const(F(1,239)),28)))
z=sub(sqrt3,sqrt2)
theta=mul(const(2),atan_bounds_positive(z,28))
omegaden=add(add(add(const(3),mul(const(2),sqrt2)),sqrt6),mul(const(2),sqrt3))
omega=mul(const(2),atan_bounds_positive(div(const(1),omegaden),28))

# O = conv{±e1,±e2,±e3}; T = conv{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)}.
# U Haar-uniform on S^2. W = directional width, B = orthogonal projection area.
# E[Wo Bo] = 2/3 + (4 sqrt(2) +8 omega)/pi
# E[Wo] = 6 sqrt(2) theta/pi, E[Bo] = sqrt(3).
# E[Wt Bt] = 8/3 +8 sqrt(6)/pi.
# E[Wt] = 6 sqrt(2)(pi/2-theta)/pi, E[Bt] =2sqrt(3).
e_wobo=add(const(F(2,3)),div(add(mul(const(4),sqrt2),mul(const(8),omega)),pi))
e_wo=div(mul(mul(const(6),sqrt2),theta),pi)
cov_o=sub(e_wobo,mul(sqrt3,e_wo))
e_wtbt=add(const(F(8,3)),div(mul(const(8),sqrt6),pi))
e_wt=div(mul(mul(const(6),sqrt2),sub(div(pi,const(2)),theta)),pi)
cov_t=sub(e_wtbt,mul(mul(const(2),sqrt3),e_wt))

# Numerical bounds strictly enclose correct exact values, computed using rational endpoints only.
assert F(1,50)<cov_o[0] and cov_o[1]<F(3,100)
assert -F(4,100)<cov_t[0] and cov_t[1]<-F(3,100)
for k,x in [('theta',theta),('omega',omega),('cov_oct',cov_o),('cov_tet',cov_t)]:
    print(k,'%.14f'%float(x[0]),'%.14f'%float(x[1]),'width<','%.2g'%float(x[1]-x[0]))
print('PASS: exact rational interval proof: covariance of octahedron > 1/50; tetrahedron < -3/100.')
