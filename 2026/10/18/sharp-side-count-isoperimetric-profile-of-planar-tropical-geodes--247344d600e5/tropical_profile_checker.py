"""Reproduce exact arithmetic checks for tropical polygon isoperimetry.

No finite test is used as proof of the infinite assertions; those follow from
normal forms and sum-of-squares identities given in RESULT.md.
"""
from fractions import Fraction as F
import random
import sympy as sp

a, b, u = sp.symbols('a b u', real=True)
s=a+b
P=2*s-u
A=a*b-u*u/2
assert sp.simplify(P**2-14*A-sp.Rational(7,2)*(a-b)**2-8*(u-s/4)**2)==0
assert sp.simplify((2*a+b)**2-16*(a*b-b*b/2)-(2*a-3*b)**2)==0
assert sp.simplify((2*(a+b))**2-16*a*b-4*(a-b)**2)==0

def N(v):
    x,y=v
    return max(abs(x),abs(y),abs(x-y))

def area_poly(vertices):
    return abs(sum(x*v-y*w for (x,y),(w,v) in zip(vertices, vertices[1:]+vertices[:1])))/2

def per_poly(vertices):
    return sum(N((w-x,v-y)) for (x,y),(w,v) in zip(vertices, vertices[1:]+vertices[:1]))

def cut_rect(a,b,u):
    verts=[(F(0),F(0)),(a-u,F(0)),(a,u),(a,b),(F(0),b)]
    result=[]
    for v in verts:
        if v not in result: result.append(v)
    return result

rng=random.Random(2060315)
for _ in range(2000):
    a=F(rng.randint(2,100),rng.randint(1,40))
    b=F(rng.randint(2,100),rng.randint(1,40))
    u=min(a,b)*F(rng.randint(1,49),50)
    vertices=cut_rect(a,b,u)
    assert len(vertices)==5
    assert area_poly(vertices)==a*b-u*u/2
    assert per_poly(vertices)==2*(a+b)-u
    assert per_poly(vertices)**2>=14*area_poly(vertices)

for _ in range(1000):
    b=F(rng.randint(1,100),rng.randint(1,30))
    a=b+F(rng.randint(1,100),rng.randint(1,30))
    vertices=cut_rect(a,b,b)
    assert len(vertices)==4
    assert area_poly(vertices)==a*b-b*b/2
    assert per_poly(vertices)==2*a+b
    assert per_poly(vertices)**2>=16*area_poly(vertices)

for _ in range(1000):
    a=F(rng.randint(1,100),rng.randint(1,30))
    b=F(rng.randint(1,100),rng.randint(1,30))
    vertices=[(F(0),F(0)),(a,F(0)),(a,b),(F(0),b)]
    assert area_poly(vertices)==a*b
    assert per_poly(vertices)==2*(a+b)
    assert per_poly(vertices)**2>=16*area_poly(vertices)

for _ in range(100):
    a=F(rng.randint(1,100),rng.randint(1,30))
    tri=cut_rect(a,a,a)
    assert len(tri)==3
    assert per_poly(tri)**2==18*area_poly(tri)

assert (lambda v: per_poly(v)**2==12*area_poly(v))([(F(-1),F(-1)),(F(-1),F(0)),(F(0),F(1)),(F(1),F(1)),(F(1),F(0)),(F(0),F(-1))])
assert per_poly(cut_rect(F(1),F(1),F(1,2)))**2==14*area_poly(cut_rect(F(1),F(1),F(1,2)))
assert per_poly(cut_rect(F(3,2),F(1),F(1)))**2==16*area_poly(cut_rect(F(3,2),F(1),F(1)))
print('VERIFY_OK: 4103 exact polygon cases and 3 symbolic identities')
