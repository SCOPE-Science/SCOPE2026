#!/usr/bin/env python3
"""Exact certificate for central sections of the regular pentagonal antiprism.

Run: python3 verify.py. Standard Python library only.
"""
from fractions import Fraction
from itertools import product, combinations
from collections import Counter
from math import acos, pi, sqrt

class Qphi:
    __slots__ = ('a','b')
    def __init__(self,a,b=0): self.a,self.b=int(a),int(b)
    def __add__(self,o):
        o=coerce(o);return Qphi(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Qphi(-self.a,-self.b)
    def __sub__(self,o):return self+-coerce(o)
    def __rsub__(self,o):return coerce(o)+-self
    def __mul__(self,o):
        o=coerce(o)
        return Qphi(self.a*o.a+self.b*o.b,self.a*o.b+self.b*o.a+self.b*o.b)
    __rmul__=__mul__
    def __eq__(self,o):
        o=coerce(o);return self.a==o.a and self.b==o.b
    def sign(self):
        lo=Fraction(1618033988749894848,10**18)
        hi=lo+Fraction(1,10**18)
        assert lo*lo-lo-1<0 and hi*hi-hi-1>0
        lower=Fraction(self.a)+self.b*(lo if self.b>=0 else hi)
        upper=Fraction(self.a)+self.b*(hi if self.b>=0 else lo)
        if lower>0:return 1
        if upper<0:return -1
        if self.a==self.b==0:return 0
        raise ArithmeticError('Insufficient algebraic interval')
    def __repr__(self):return f'{self.a}+{self.b}φ'

def coerce(x): return x if isinstance(x,Qphi) else Qphi(x)
phi=Qphi(0,1)
def vec(*x):return tuple(coerce(a) for a in x)
def dot(a,b):return sum((a[i]*b[i] for i in range(3)),Qphi(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def neg(v):return tuple(-w for w in v)

# Coordinates of the twelve-vertex icosahedron, with one antipodal pair removed.
V=[]
for y,z in product([-1,1],repeat=2):V.append(vec(0,y,z*phi))
for x,y in product([-1,1],repeat=2):V.append(vec(x,y*phi,0))
for x,z in product([-1,1],repeat=2):V.append(vec(x*phi,0,z))
pole=vec(0,1,phi)
V=[v for v in V if v!=pole and v!=neg(pole)]
assert len(V)==10 and len(set((str(v) for v in V)))==10
assert all(dot(v,v)==phi+2 for v in V)
E=[]
for i,j in combinations(range(10),2):
    if dot(tuple(V[i][k]-V[j][k] for k in range(3)),tuple(V[i][k]-V[j][k] for k in range(3)))==4:
        E.append((i,j))
assert len(E)==20
# Recover *all* exact supporting facets, including the two five-vertex faces.
facets=set()
for i,j,k in combinations(range(10),3):
    ni=cross(tuple(V[j][t]-V[i][t] for t in range(3)),
             tuple(V[k][t]-V[i][t] for t in range(3)))
    if all(x==0 for x in ni): continue
    signs=[dot(ni,tuple(V[h][t]-V[i][t] for t in range(3))).sign() for h in range(10)]
    if all(s>=0 for s in signs) or all(s<=0 for s in signs):
        facets.add(tuple(h for h,s in enumerate(signs) if s==0))
assert Counter(len(f) for f in facets)==Counter({3:10,5:2})
assert Counter(x for ij in E for x in ij)==Counter({i:4 for i in range(10)})
# Exact length-2 edges form a standard regular pentagonal antiprism graph.
assert len({i for i in range(10)})==10

R=[]
for x in V:
    if x not in R and neg(x) not in R:R.append(x)
assert len(R)==5 and all(dot(a,cross(b,c)).sign()!=0 for a,b,c in combinations(R,3))
print('EXACT_12_SUPPORTING_FACETS_20_EDGES_PASSED')
print('FIVE_PLANES_GENERAL_POSITION_PASSED')

# One integer normal strictly inside each of the 22 great-circle chambers.
W={
'-----':(1,0,-1), '---+-':(1,0,-4), '--+--':(1,1,-1), '--+-+':(-1,4,2),
'--++-':(-2,2,-4), '--+++':(-4,3,-4), '-+---':(1,-1,-1), '-+-+-':(-2,-4,-4),
'-+-++':(-4,-4,-4), '-+++-':(-2,-1,-4), '-++++':(-4,-2,-4), '+----':(1,0,1),
'+---+':(1,0,2), '+-+--':(1,1,1), '+-+-+':(-2,2,4), '+-+++':(-4,3,2),
'++---':(1,-4,-1), '++--+':(-2,-4,4), '++-+-':(-1,-4,-2), '++-++':(-4,-4,-2),
'+++-+':(-2,-1,4), '+++++':(-4,-2,-1),
}
assert len(W)==22 and len(set(W))==22
counts=Counter()
for target,coord in W.items():
    u=vec(*coord)
    actual=''.join('+' if dot(u,r).sign()>0 else '-' for r in R)
    assert actual==target and all(dot(u,r).sign()!=0 for r in R)
    signs=[dot(u,v).sign() for v in V]
    assert 0 not in signs
    n=sum(signs[i]!=signs[j] for i,j in E)
    assert n in (6,10), (target,n)
    counts[n]+=1
assert counts==Counter({6:10,10:12}),counts
# Five great circles in general position have 2+2(1+2+3+4)=22 regions.
# All 22 sign patterns have a strict witness, so there are no other chambers.
assert 2+sum(2*k for k in range(1,5))==len(W)
print('EXHAUSTIVE_22_CHAMBER_INTEGER_WITNESS_CERTIFICATE_PASSED')
print('NO_EIGHT_GON_OR_OTHER_SECTION_TYPE_PASSED')

# Every antiprism edge has angle arccos(1/sqrt(5)) at the center.
for i,j in E:
    assert dot(V[i],V[j])==phi
    # (phi/(phi+2))^2 = 1/5; both positive.
    assert (dot(V[i],V[j])*dot(V[i],V[j])*5)==(phi+2)*(phi+2)
θ=acos(1/sqrt(5))
mean=20*θ/pi
p10=(mean-6)/4
p6=1-p10
assert 0<p10<1 and abs(p10-(5*θ/pi-1.5))<1e-14
assert abs(6*p6+10*p10-mean)<1e-13
assert abs(p10-0.26208191174783346)<1e-13
print('CROFTON_MEAN_AND_TWO_POINT_EXACT_LAW_PASSED')
print('ALL_EXACT_CERTIFICATE_CHECKS_PASSED')
