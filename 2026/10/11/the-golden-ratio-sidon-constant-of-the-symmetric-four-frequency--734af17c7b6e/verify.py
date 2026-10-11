#!/usr/bin/env python3
from fractions import Fraction as F
import cmath, math, random

class Q5:
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q5) else Q5(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q5) else Q5(o)))
    def __rsub__(self,o): return Q5(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q5) else Q5(o)
        return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        den=self.a*self.a-5*self.b*self.b
        if den==0: raise ZeroDivisionError
        return Q5(self.a/den,-self.b/den)
    def __truediv__(self,o): return self*(o if isinstance(o,Q5) else Q5(o)).inv()
    def __eq__(self,o):
        o=o if isinstance(o,Q5) else Q5(o); return self.a==o.a and self.b==o.b
    def val(self): return float(self.a)+float(self.b)*math.sqrt(5)
    def __repr__(self): return f"Q5({self.a},{self.b})"

s=Q5(0,1)
one=Q5(1)
r=s-one
phi=(one+s)/2
phi2=phi*phi

# Witness identities.
r2=r*r
sstar=(s-one)/4
fstar=(one-sstar)*(r2+4*sstar)
sup2=4*fstar
assert sup2==(Q5(5)-s)*(Q5(5)-s)
assert (Q5(2)*s)/(Q5(5)-s)==phi
assert phi2==(Q5(3)+s)/2

# First profile F(r)=(1+r)^2/(1+r^2/2+r^4/16) at r=sqrt(5)-1.
Fprof=(one+r)*(one+r)/(one+r*r/2+(r*r*r*r)/16)
assert Fprof==phi2
# Second profile has exact maximum 7/3 at r=4/3; phi^2 is strictly larger.
r2b=F(4,3)
F2=F(1+r2b)**2/(F(1)+F(3,4)*r2b*r2b)
assert F2==F(7,3)
assert phi2.val()>float(F2)

# Corroborative random stress test on the final inequality.
random.seed(2705)
exps=(0,1,3,4)
N=4096
zs=[cmath.exp(2j*math.pi*k/N) for k in range(N)]
worst=0.0
for _ in range(400):
    c=[complex(random.gauss(0,1),random.gauss(0,1)) for _ in range(4)]
    l1=sum(abs(v) for v in c)
    M=max(abs(sum(cj*(z**e) for cj,e in zip(c,exps))) for z in zs)
    ratio=l1/M
    worst=max(worst,ratio)
    if ratio>phi.val()+2e-5:
        raise AssertionError((ratio,phi.val()))

print(f"VERIFY_OK exact_witness=1 exact_profiles=2 random_cases=400 worst_sample={worst:.12f} phi={phi.val():.12f}")
