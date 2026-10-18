#!/usr/bin/env python3
"""Standalone exact polynomial checks for a four-jump renewal envelope."""
from fractions import Fraction
from itertools import product

class Poly:
    def __init__(self, terms=None):
        self.t = {k: int(v) for k, v in (terms or {}).items() if v}
    @staticmethod
    def const(n):
        return Poly({(0, 0, 0): n})
    def __add__(self, other):
        if not isinstance(other, Poly): other=Poly.const(other)
        out=self.t.copy()
        for key,v in other.t.items(): out[key]=out.get(key,0)+v
        return Poly(out)
    __radd__=__add__
    def __neg__(self): return Poly({k:-v for k,v in self.t.items()})
    def __sub__(self, other): return self+-other if isinstance(other,Poly) else self+(-other)
    def __rsub__(self, other): return (-self)+other
    def __mul__(self, other):
        if not isinstance(other, Poly): other=Poly.const(other)
        out={}
        for k,v in self.t.items():
            for m,w in other.t.items():
                key=tuple(x+y for x,y in zip(k,m));out[key]=out.get(key,0)+v*w
        return Poly(out)
    __rmul__=__mul__
    def __pow__(self,n):
        assert type(n)==int and n>=0
        result=Poly.const(1)
        for _ in range(n):result=result*self
        return result
    def __eq__(self,other):
        if not isinstance(other,Poly):other=Poly.const(other)
        return self.t==other.t
    def degree(self): return max((sum(k) for k in self.t),default=-1)
    def compose(self, a, b, c):
        return sum((coef*a**k[0]*b**k[1]*c**k[2] for k,coef in self.t.items()),Poly.const(0))

one=Poly.const(1)
a=Poly({(1,0,0):1});b=Poly({(0,1,0):1});c=Poly({(0,0,1):1})
d=one-a-b-c
Q=a*(a+b)*(a+b+c)
P=Q+2*a*b*d
u1=a;u2=a*a+b;u3=a*a*a+2*a*b+c
assert P.degree()==3
assert P-Q==2*a*b*d
assert u1-P==a*(c+d*(one+a-b))
assert u2-P==b*b+b*c+d*(a*a+b*(one-a))
assert u3-P==a*b*(b+c)+c*(one-a*a)
# Under the cumulative coordinate substitution (a,b,c)->(s1,s2-s1,s3-s2),
# the successive terminal specializations have degrees 1, 2 and at most 3.
hat=P.compose(a,b-a,c-b)
assert hat==a*b*c+2*a*(b-a)*(one-c)
assert hat.compose(a,b,one)==a*b
assert hat.compose(a,one,one)==a
assert hat.degree()<=3

count=0
for denom in range(1,20):
    for ia in range(denom+1):
        for ib in range(denom-ia+1):
            for ic in range(denom-ia-ib+1):
                aa=Fraction(ia,denom);bb=Fraction(ib,denom)
                cc=Fraction(ic,denom);dd=1-aa-bb-cc
                qq=aa*(aa+bb)*(aa+bb+cc)
                pp=qq+2*aa*bb*dd
                rr=[aa,aa*aa+bb,aa**3+2*aa*bb+cc]
                assert 0<=qq<=pp<=min(rr)
                count+=1
# A coefficient greater than two fails on a family of small positive masses.
for alpha in [Fraction(201,100),Fraction(21,10),Fraction(3,1)]:
    t=min(Fraction(1,100), (alpha-2)/(4*(2*alpha-3)))
    aa=t; bb=t; cc=Fraction(0); dd=1-2*t
    excess=(aa*(aa+bb)*(aa+bb+cc)+alpha*aa*bb*dd) -(aa**3+2*aa*bb+cc)
    assert dd>0 and excess>0
print(f'VERIFY_OK symbolic_equalities=7 cumulative_specializations=3 simplex_grid_points={count} sharpness_examples=3')
