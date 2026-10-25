"""Supplementary exact-algebra and deterministic numerical checks for periodic Hardy shifts.

Run: python verify.py
Finite tests corroborate the analytic theorem; they cannot prove its universal quantifiers.
"""
from fractions import Fraction
from math import sqrt
from random import Random

class Q2:
    """Elements a+b sqrt(2), with exact rational coefficients."""
    def __init__(self,a=0,b=0): self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=coerce(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+-coerce(o)
    def __rsub__(self,o): return coerce(o)+-self
    def __mul__(self,o):
        o=coerce(o);return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o):
        o=coerce(o); return self.a==o.a and self.b==o.b
    def __truediv__(self,o):
        o=coerce(o);det=o.a*o.a-2*o.b*o.b
        return Q2((self.a*o.a-2*self.b*o.b)/det,(self.b*o.a-self.a*o.b)/det)
    def __float__(self):return float(self.a)+sqrt(2)*float(self.b)

def coerce(v):return v if isinstance(v,Q2) else Q2(v)

H=Q2(-1,1)
C=H*H
T=1-2*C
assert H*H+2*H==1
assert C==Q2(3,-2)
assert T==Q2(-5,4)
assert 2*C+H*(1+C)==1-C
assert T-C==H*(1+C)
assert T-(T+3)*C-C*C==0  # derivative of negative-branch profile
assert (1-T)/2==C
assert 2*C/(1+T)==H/2
assert float(3*C)<1

# Exact equality at the inside radius and at the boundary limit.
def f(a,b,r):return r*abs(a+b*r*r)/(1+r*r)
h=float(H); c=float(C);t=float(T)
assert abs(f(-t,1,h)-c)<1e-13
assert abs(abs(1-t)/2-c)<1e-13

# Exhaustive rational-grid check on a fixed finite mesh for both normalized ratios.
# This is a supplementary test, not an exhaustive test of all complex coefficients.
checks=0
for ar in range(-10,11):
 for ai in range(-10,11):
  a=complex(ar/10, ai/10)
  for br,bi in [(-1,0),(0,-1),(1,0),(0,1),(-.6,.8),(.8,.6),(.6,-.8)]:
   b=complex(br,bi)
   den=max(abs(a),abs(b))
   rad=max([f(a,b,k/2000) for k in range(2000)]+[abs(a+b)/2])
   # finite mesh is a lower bound, so allow small discretization error
   assert rad/den >= c-0.0005, (a,b,rad/den)
   assert rad/((abs(a)+abs(b))/2) >= h/2-0.0006, (a,b,rad)
   checks+=1

# Dense one-parameter scans of the extremal opposite-phase family.
for j in range(1001):
 r=j/1001
 assert f(-t,1,r)<=c+1e-13
 checks+=1

# Random complex phase tests with enough radial points to compare both bounds.
rng=Random(2077)
for j in range(500):
 a=complex(rng.uniform(-1,1),rng.uniform(-1,1))
 b=complex(rng.uniform(-1,1),rng.uniform(-1,1))
 norm=max(abs(a),abs(b))
 if norm==0:continue
 rad=max(f(a,b,h), f(a,b,.5),abs(a+b)/2)
 # The three witnesses suffice for norm sharpness.
 assert rad >= c*norm-1e-12
 checks+=1
print('PASS:',checks,'supplementary finite checks; exact Q(sqrt(2)) certificates passed')
