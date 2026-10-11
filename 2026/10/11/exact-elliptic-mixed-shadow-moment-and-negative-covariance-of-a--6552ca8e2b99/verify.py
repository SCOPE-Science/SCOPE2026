#!/usr/bin/env python3
"""Reproduce exact mixed-shadow moment's sign certificate and geometry checks."""
from fractions import Fraction as F
from math import isqrt, comb, sqrt, hypot, pi, sin, cos
from random import Random

class Interval:
    def __init__(self, low, high=None):
        self.lo = F(low)
        self.hi = F(low if high is None else high)
        assert self.lo <= self.hi
    def __add__(self, other):
        other = interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self):
        return Interval(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + -interval(other)
    def __rsub__(self, other):
        return interval(other) + -self
    def __mul__(self, other):
        other = interval(other)
        v = [x*y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return Interval(min(v), max(v))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = interval(other)
        assert other.lo > 0 or other.hi < 0
        return self * Interval(1/other.hi, 1/other.lo)
    def __rtruediv__(self, other):
        return interval(other) / self

def interval(x):
    return x if isinstance(x, Interval) else Interval(x)

def rational_sqrt(x, digits=45):
    """Outward rational enclosure: no floating-point rounding assumed."""
    x = F(x)
    d = 10**digits
    q = isqrt(x.numerator * d*d // x.denominator)
    return Interval(F(q,d), F(q+1,d))

def atan_rational(x, K=25):
    """Alternating-series enclosure for arctangent of rational 0<x<1."""
    x = F(x)
    assert 0 < x < 1
    p = sum(((-1)**k)*x**(2*k+1)/F(2*k+1) for k in range(K+1))
    tail = x**(2*K+3)/F(2*K+3)
    return Interval(p-tail,p) if K%2==0 else Interval(p,p+tail)

def atan_enclosure(x):
    assert 0 < x.lo and x.hi < 1
    return Interval(atan_rational(x.lo).lo, atan_rational(x.hi).hi)

def certify_covariance():
    sqrt2 = rational_sqrt(2)
    sqrt3 = rational_sqrt(3)
    PI = 16*atan_rational(F(1,5)) - 4*atan_rational(F(1,239))
    theta = PI/4 + atan_enclosure(3-2*sqrt2)
    assert 0 < theta.lo and theta.hi < 1

    N = 14
    # S_n = integral from zero to theta of sin(x)^(2n) dx.
    # sin(theta)*cos(theta)=sqrt(2)/3; sin(theta)^2=2/3.
    S = [theta]
    for n in range(1, N+2):
        S.append(F(2*n-1,2*n)*S[-1] - sqrt2*F(1,3)*F(2,3)**(n-1)/F(2*n))

    partial = interval(0)
    for n in range(N+1):
        coefficient = F((-1)**n * comb(2*n,n), 8**n)
        partial += coefficient * (S[n] + S[n+1])
    # (2 + sin(x)^2)^(-1/2) = (1/sqrt(2)) sum (-1)^n a_n sin(x)^(2n)/2^n.
    # Alternating remainder is at most (sin(theta)^2/2)^(N+1) <= 3^(-N-1).
    # theta<1 and 1+sin(theta)^2<=5/3 imply |error|<=5/3^(N+2).
    remainder = F(5, 3**(N+2))
    J = partial / sqrt2 + Interval(-remainder,remainder)
    mixed = 4*sqrt3/(3*PI) + 2*J/PI
    mean_product = 3*sqrt3*theta/4
    covariance = mixed - mean_product
    assert F(-4,10000) < covariance.lo
    assert covariance.hi < F(-3,10000)
    print('CERTIFIED_COVARIANCE_INTERVAL', float(covariance.lo), float(covariance.hi))
    print('CERTIFIED_MIXED_MOMENT_INTERVAL', float(mixed.lo), float(mixed.hi))
    return (float(mixed.lo)+float(mixed.hi))/2

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def unit(v):
    d=sqrt(dot(v,v))
    return tuple(x/d for x in v)

def hull(points):
    """Monotone chain polygon of at most four planar points."""
    pts=sorted(points)
    def det(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in pts:
        while len(lower)>=2 and det(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    upper=[]
    for p in pts[::-1]:
        while len(upper)>=2 and det(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def test_geometry():
    c=1/sqrt(3); s=sqrt(2/3)
    normals=[(c,s,0),(c,-s,0),(-c,0,s),(-c,0,-s)]
    verts=[tuple(-sqrt(6)/4*v for v in n) for n in normals]
    r=Random(20261009)
    max_area=max_perim=0.0
    for _ in range(400):
        u=unit(tuple(r.gauss(0,1) for i in range(3)))
        e=unit(cross(u,(0,0,1))) if abs(u[2])<.95 else unit(cross(u,(0,1,0)))
        f=cross(u,e)
        poly=hull([(dot(v,e),dot(v,f)) for v in verts])
        ar=abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])))/2
        pe=sum(hypot(a[0]-b[0],a[1]-b[1]) for a,b in zip(poly,poly[1:]+poly[:1]))
        exact_ar=sqrt(3)/8*sum(abs(dot(n,u)) for n in normals)
        exact_pe=0
        for i in range(4):
            for j in range(i+1,4):
                if dot(normals[i],u)*dot(normals[j],u)<0:
                    edge=unit(cross(normals[i],normals[j]))
                    exact_pe += sqrt(max(0,1-dot(edge,u)**2))
        max_area=max(max_area,abs(ar-exact_ar))
        max_perim=max(max_perim,abs(pe-exact_pe))
    assert max_area<1e-12 and max_perim<1e-12
    print('INDEPENDENT_POLYGON_TESTS',400, max_area, max_perim)

def test_elliptic_integral(mixed):
    # Midpoint quadrature of the analytic one-variable integral (diagnostic only).
    theta=__import__('math').atan(sqrt(2))
    count=200000
    step=theta/count
    J=step*sum((1+sin((i+.5)*step)**2)/sqrt(2+sin((i+.5)*step)**2) for i in range(count))
    numerical=4*sqrt(3)/(3*pi)+2*J/pi
    assert abs(numerical-mixed)<1e-7
    print('ONE_DIMENSIONAL_QUADRATURE', numerical)

if __name__=='__main__':
    mid=certify_covariance()
    test_geometry()
    test_elliptic_integral(mid)
    print('VERIFY_OK')
