#!/usr/bin/env python3
"""Exact rational sign certificate for a four-dimensional Steiner polynomial.

Uses Python's standard-library rational arithmetic for all inequalities.
SymPy is used only to reproduce the symbolic quartic discriminant.
"""
from fractions import Fraction as F
from math import comb
import sympy as sp


def atan_partial(reciprocal, degree):
    return sum(((-1)**k * F(1, (2*k+1)*reciprocal**(2*k+1)) for k in range(degree+1)), F(0))

# Alternating Taylor bounds, with Machin's identity for pi.
pi_lower_machin = 16*atan_partial(5,17)-4*atan_partial(239,18)
pi_upper_machin = 16*atan_partial(5,18)-4*atan_partial(239,17)
p_lo, p_hi = F(3141592653589793238,10**18),F(3141592653589793239,10**18)
assert p_lo < pi_lower_machin < pi_upper_machin < p_hi

class Interval:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,other):
        other=other if isinstance(other,Interval) else Interval(other)
        return Interval(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,other):return self+-other if isinstance(other,Interval) else self+(-F(other))
    def __mul__(self,other):
        other=other if isinstance(other,Interval) else Interval(other)
        a=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return Interval(min(a),max(a))
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=Interval(1)
        for _ in range(n):out=out*self
        return out

p=Interval(p_lo,p_hi)
# Discriminant = (8/27) q^2 G(q), where G has the five coefficients below.
c=[27*p**4-204*p**3+384*p**2,
   216*p**3-2664*p**2+11328*p-16384,
   540*p**2-4536*p+9528,
   432*p-1776,Interval(108)]

def eval_poly(coef,q):
    v=Interval(0)
    for a in coef[::-1]:v=v*q+a
    return v

assert eval_poly(c,0).lo>0
assert eval_poly(c,1).hi<0
for x,sign in [(F(87,100),1),(F(9,10),-1),(F(8766744,10**7),1),(F(8766745,10**7),-1)]:
    v=eval_poly(c,x)
    assert (v.lo>0 if sign>0 else v.hi<0),(x,v.lo,v.hi)

# Check strict G' negativity with Bernstein positivity on four subintervals.
# A cubic on [0,1] is a convex combination of its Bernstein coefficients.
d=[(i+1)*c[i+1] for i in range(4)]
intervals=[(F(0),F(1,2)),(F(1,2),F(3,4)),(F(3,4),F(7,8)),(F(7,8),F(1))]
for a,b in intervals:
    power=[sum((d[k]*F(comb(k,j))*a**(k-j)*(b-a)**j for k in range(j,4)),Interval(0)) for j in range(4)]
    bern=[sum((power[j]*F(comb(i,j),comb(3,j)) for j in range(i+1)),Interval(0)) for i in range(4)]
    upper_bound={F(0):-F(44), F(1,2):-F(4), F(3,4):-F(1), F(7,8):-F(3,4)}[a]
    assert all(v.hi<upper_bound for v in bern),(a,b,[float(v.hi) for v in bern])
    print('Gprime Bernstein',str(a),str(b),*[f'{float(v.hi):.9f}' for v in bern])

# The regular m-gon's quotient q_m=pi/(m*tan(pi/m)).
# tan(pi/5)=sqrt(5-2sqrt(5)); sqrt(5)<22361/10000, pi<22/7.
assert F(22361,10000)**2>5
assert F(22,7)**2 < F(87,100)**2*25*(5-2*F(22361,10000))
# For the regular hexagon q_6=pi*sqrt(3)/6>9/10.
assert F(173,100)**2<3
assert F(314,100)*F(173,100)/6>F(9,10)
assert p_lo>F(314,100) and p_hi<F(22,7)

# Independent symbolic calculation of the discriminant and coefficient scaling.
z,q,s,A,P,L=sp.symbols('z q s A P L')
pi=sp.symbols('pi')
quartic=z**4/sp.Integer(2)+sp.Rational(8,3)*z**3+(pi+2*q)*z**2+4*q*z+q**2
G=27*pi**4-204*pi**3+384*pi**2+q*(216*pi**3-2664*pi**2+11328*pi-16384)+q**2*(540*pi**2-4536*pi+9528)+q**3*(432*pi-1776)+108*q**4
assert sp.simplify(sp.discriminant(quartic,z)-sp.Rational(8,27)*q**2*G)==0
raw=A**2+2*A*P*s+(2*sp.pi*A+sp.pi*P**2/4)*s**2+sp.Rational(4,3)*sp.pi*P*s**3+sp.pi**2*s**4/2
normalized=sp.expand(raw.subs({A:q*sp.pi*L**2,P:2*sp.pi*L,s:z*L})/(sp.pi**2*L**4))
assert sp.simplify(normalized-quartic.subs(pi,sp.pi))==0
print('PASS: rational pi, four-interval strict monotonicity, root brackets, polygon cutoff, discriminant, Steiner coefficients')
