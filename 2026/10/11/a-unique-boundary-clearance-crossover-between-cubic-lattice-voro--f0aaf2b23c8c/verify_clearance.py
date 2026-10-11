#!/usr/bin/env python3
"""Exact-rational algebra and deterministic diagnostics for Voronoi clearance laws.
Only Python's standard library is required.  This checks specified identities,
not an exhaustive mathematical proof of the associated geometric lemmas.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import random

# All tests here are exact integer/rational comparisons.
s3lo=F(173205,100000);s3hi=F(173206,100000)
s2lo=F(14142,10000);s2hi=F(14143,10000)
qlo=F(8908,10000);qhi=F(8909,10000)
assert s3lo**2 < 3 < s3hi**2
assert s2lo**2 < 2 < s2hi**2
assert qlo**6 < F(1,2) < qhi**6
A_lower=3/qhi-F(3,2)*s3hi-F(3,4)
C_lower=-10+5*s3lo+s2lo
assert A_lower > 0 and C_lower > 0
Tupper=(1+s3hi)/4
bTupper=(3-s3lo)/4
fbase_lower=1-Tupper/qlo
assert fbase_lower>0 and bTupper/F(144,100)<fbase_lower
assert s3hi/2<qlo
assert qlo/4 > (17*s3hi-1)/128

# Pure rational quadratic extension a+b*sqrt(3).
class R3:
    def __init__(self,a=0,b=0):self.a=F(a);self.b=F(b)
    @staticmethod
    def make(z):return z if isinstance(z,R3) else R3(z)
    def __add__(self,z):
        z=self.make(z);return R3(self.a+z.a,self.b+z.b)
    __radd__=__add__
    def __neg__(self):return R3(-self.a,-self.b)
    def __sub__(self,z):return self+-self.make(z)
    def __rsub__(self,z):return self.make(z)+-self
    def __mul__(self,z):
        z=self.make(z);return R3(self.a*z.a+3*self.b*z.b,self.a*z.b+self.b*z.a)
    __rmul__=__mul__
    def __truediv__(self,z):
        z=self.make(z);den=z.a*z.a-3*z.b*z.b
        return self*R3(z.a/den,-z.b/den)
    def __pow__(self,k):
        out=R3(1)
        for i in range(k):out=out*self
        return out
    def __eq__(self,z):
        z=self.make(z);return self.a==z.a and self.b==z.b
    def __repr__(self):return f'R3({self.a},{self.b})'

zero=R3();one=R3(1);sqrt3=R3(0,1)
def addpoly(a,b):return [a[i] if i>=len(b) else b[i] if i>=len(a) else a[i]+b[i] for i in range(max(len(a),len(b)))]
def mulpoly(a,b):
    c=[zero for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=c[i+j]+x*y
    return c
def scale(a,z):return [x*z for x in a]
def cube(a):return mulpoly(mulpoly(a,a),a)
def integrate_poly(a,upper):return sum((x*upper**(k+1)/(k+1) for k,x in enumerate(a)),zero)

T=(one+sqrt3)/4
radius=sqrt3/2
b=[R3(F(3,2)),-sqrt3]
c=[R3(F(1,2)),one-sqrt3]
Vearly=addpoly(scale(cube(b),F(4,3)),scale(cube(c),-4))
Vlate=scale(cube(b),F(4,3))
# Exact integrals of the interior-parallel volume and survival first moment.
area_int=integrate_poly(Vearly,T)+integrate_poly(Vlate,radius)-integrate_poly(Vlate,T)
assert area_int/4 == (17*sqrt3-one)/128
v0=sum((x*R3(0)**k if k else x for k,x in enumerate(Vearly)),zero)
assert v0==4
# Second moment 2 * integral t*survival(t) dt.
Vearly_times_t=[zero]+Vearly
Vlate_times_t=[zero]+Vlate
second_int=integrate_poly(Vearly_times_t,T)+integrate_poly(Vlate_times_t,radius)-integrate_poly(Vlate_times_t,T)
assert second_int/2 == R3(F(13,160),F(-1,640))

# Deterministic random-direction independent interior membership checks.
# These are finite numerical diagnostics, NOT proofs of the universal statement.
with localcontext() as ctx:
    ctx.prec=60
    root3=Decimal(3).sqrt()
    q=(Decimal(1)/Decimal(2))**(Decimal(1)/Decimal(6))
    tcrit=(1+root3)/4
    rB=root3/2
    def sb(t):
        if t>=rB:return Decimal(0)
        a=Decimal(1)-t
        b=Decimal('1.5')-root3*t
        v=Decimal(4)/3*b**3
        if t<tcrit:v-=4*(b-a)**3
        return v/4
    def sf(t):return max(Decimal(0),1-t/q)**3
    def diff(t):return sb(t)-sf(t)
    left=Decimal('0.3');right=Decimal('0.4')
    assert diff(left)>0 and diff(right)<0
    for i in range(220):
        mid=(left+right)/2
        if diff(mid)>0:left=mid
        else:right=mid
    crossing=(left+right)/2
    assert abs(crossing-Decimal('0.3250593'))<Decimal('0.0000001')
    EB=(17*root3-1)/128
    EF=q/4
    assert EF>EB
    rng=random.Random(103)
    n=240000
    threshold=[Decimal('0.10'),Decimal('0.30'),Decimal('0.50'),Decimal('0.70')]
    counts=[0]*len(threshold)
    for _ in range(n):
        x,y,z=(2*rng.random()-1 for __ in range(3))
        if abs(x)+abs(y)+abs(z)>1.5:continue
        dd=min(1-max(abs(x),abs(y),abs(z)),(1.5-abs(x)-abs(y)-abs(z))/float(root3))
        for i,t in enumerate(threshold):counts[i]+=dd>float(t)
    # Rejection sampling in cube gives P(point in cell) = 4/8=1/2.
    for t,k in zip(threshold,counts):
        empirical=Decimal(k)*2/Decimal(n)
        assert abs(empirical-sb(t))<Decimal('0.012'),(t,empirical,sb(t))
    print('VERIFY_OK')
    print('exact identity: volume4, mean=(17sqrt3-1)/128, second moment=(52-sqrt3)/640')
    print('rational certificates: initial slope, convex crossing quadratic, phase endpoint, FCC higher mean')
    print('clearance crossover:',format(crossing,'.16f'))
    print('mean BCC:',format(EB,'.16f'),'mean FCC:',format(EF,'.16f'))
    print('deterministic rejection diagnostics:',[(str(t),k) for t,k in zip(threshold,counts)])
