#!/usr/bin/env python3
"""Exact rational interval certificate for a three-cycle in a sine-coupled triangle.

No floating-point comparison enters an assertion. Run with Python >=3.10:
    python verify_triangle_cycle.py
"""
from fractions import Fraction as Q
from math import factorial

class I:
    def __init__(self, lo, hi=None):
        self.lo = Q(lo)
        self.hi = Q(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, rhs):
        rhs = rhs if isinstance(rhs, I) else I(rhs)
        return I(self.lo+rhs.lo, self.hi+rhs.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self,rhs):
        return self + (-rhs if isinstance(rhs,I) else -I(rhs))
    def __rsub__(self,rhs):
        return I(rhs) - self
    def __mul__(self,rhs):
        rhs = rhs if isinstance(rhs,I) else I(rhs)
        vals=(self.lo*rhs.lo,self.lo*rhs.hi,self.hi*rhs.lo,self.hi*rhs.hi)
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def absmax(self):
        return max(abs(self.lo),abs(self.hi))
    def widen(self,eps):
        return I(self.lo-eps,self.hi+eps)

# Alternating arctangent series and the exact Machin identity for pi.
def atan_interval(inv,n):
    val=sum(((-1)**k * Q(1, (2*k+1)*inv**(2*k+1)) for k in range(n)),Q(0))
    eps=Q(1,(2*n+1)*inv**(2*n+1))
    return I(val-eps,val+eps)
pi = 16*atan_interval(5,24)-4*atan_interval(239,8)
assert pi.lo > Q('3.141592653589793238462643383')
assert pi.hi < Q('3.141592653589793238462643384')

# Polynomial Taylor bounds on [-3,3].  Remainders follow from the
# Taylor/Lagrange theorem and the bound |sin|, |cos| <= 1.
def sc(x):
    assert abs(x) < 3
    s=sum((Q((-1)**k)*x**(2*k+1)/factorial(2*k+1) for k in range(15)),Q(0))
    c=sum((Q((-1)**k)*x**(2*k)/factorial(2*k) for k in range(16)),Q(0))
    return I(s).widen(Q(3**31,factorial(31))), I(c).widen(Q(3**32,factorial(32)))

h=Q(57,50)
a=Q('1.514991066322')
b=Q('0.512312470864')
c=-a-b
r=Q(1,10**8)
sa,ca=sc(a)
sb,cb=sc(b)
sc_,cc=sc(c)
R=[I(2*a+b)+h*(2*sa-sb-sc_)-2*pi,
   I(b-a)+h*(2*sb-sa-sc_)]
J=[[I(2)+h*(2*ca+cc),I(1)+h*(-cb+cc)],
   [I(-1)+h*(-ca+cc),I(1)+h*(2*cb+cc)]]
M=[[Q('0.762247899'),Q('0.152210095')],
   [Q('0.480438085'),Q('0.498391907')]]
assert M[0][0]*M[1][1]-M[0][1]*M[1][0] != 0
normM=max(sum(abs(v) for v in row) for row in M)
correction=max(sum(abs(M[i][j])*R[j].absmax() for j in range(2)) for i in range(2))
linear=max(sum((I(int(i==k))-sum((M[i][j]*J[j][k] for j in range(2)),I(0))).absmax() for k in range(2)) for i in range(2))
# At all points of the closed radius-r box, the Jacobian's two row
# sums deviate from J(a,b) by at most 7*h*r (cos is 1-Lipschitz).
lipschitz=linear+normM*7*h*r
assert correction < Q(1,10**9)
assert lipschitz < Q(1,10**5)
assert correction+lipschitz*r < r

# Derivative of the co-rotating map P^{-1}F on E (a,b,-a-b).
# Each cosine at a true root differs from its center value by
# at most (r,r,2r) respectively.
Ca,Cb,Cc=ca.widen(r),cb.widen(r),cc.widen(2*r)
B=[[h*(-Ca+Cc),I(1)+h*(2*Cb+Cc)],
   [I(-1)+h*(-2*Cc-Ca),I(-1)+h*(-2*Cc-Cb)]]
trace=B[0][0]+B[1][1]
det=B[0][0]*B[1][1]-B[0][1]*B[1][0]
assert I(Q(-156,100)).hi < trace.lo and trace.hi < Q(-155,100)
assert Q(70,100) < det.lo and det.hi < Q(71,100)
assert (I(1)+trace+det).lo>0
assert (I(1)-trace+det).lo>0
assert (I(1)-det).lo>0
# Strictly distinct, nonzero a,b,c in (-pi,pi), so cyclic shifts
# form a prime period-three orbit, distinct from its sign reflection.
assert c < -2 and Q(1)<a<Q(2) and Q(0)<b<Q(1)
assert (-3<c<0 and 0<b<a<3 and c!= -a and c!=-b and a!=-b)

print('PASS: exact rational interval Newton contraction and unique fixed point in box')
print('center defect upper bound: %.4g' % float(correction))
print('contraction bound: %.4g' % float(lipschitz))
print('trace enclosure: [%.12f, %.12f]' % (float(trace.lo),float(trace.hi)))
print('determinant enclosure: [%.12f, %.12f]' % (float(det.lo),float(det.hi)))
print('PASS: all three strict quadratic Schur inequalities')
