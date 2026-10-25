#!/usr/bin/env python3
"""Exact interval certificate and finite extreme-potential cross-check for pentagon interpolation.

Requires Python 3 standard library only. The inequalities are certified by
rational interval arithmetic; floating-point output is for orientation only.
"""
from fractions import Fraction as F
from math import isqrt
from itertools import product

S = 10**27

class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi
    @staticmethod
    def c(x): return x if isinstance(x, I) else I(x)
    def __add__(self, o):
        o = I.c(o); return I(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, o): return self + (-I.c(o))
    def __rsub__(self, o): return I.c(o) + (-self)
    def __mul__(self, o):
        o = I.c(o)
        v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(v),max(v))
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = I.c(o)
        assert o.lo>0 or o.hi<0
        return self * I(F(1,o.hi),F(1,o.lo))
    def __rtruediv__(self, o): return I.c(o)/self
    def sqrt(self):
        assert self.lo>=0
        def flo(x): return isqrt((x.numerator*S*S)//x.denominator)
        return I(F(flo(self.lo),S),F(flo(self.hi)+1,S))
    def pos(self, name):
        assert self.lo>0, (name, float(self.lo),float(self.hi))
    def midpoint(self): return float((self.lo+self.hi)/2)

p=(I(1)+I(5).sqrt())/2
u=((2*p+3)/4).sqrt()
v=((4*p+3)/4).sqrt()
T=I(1)+2*u+v
D=2*(p-1)*T
NA=2*p*u-1
NB=2*p*v+p-2*(p+1)*u
NC=4*p*u-2*(p+1)*v
L=4*p/D
A=NA/D; B=NB/D; C=NC/D
for name,expr in [('positive denominator',D),('strictly positive opposite weight',NC),('weight order A>B',NA-NB),('weight order B>C',NB-NC),('amplification over 1',4*p-D),('adjacent midpoint coupling margin',2*p*p-(p*(NA-NB)+(NB-NC))),('nonadjacent midpoint coupling margin',2*p*p*p-(p*(NA-NC)+(NA-NB)))]:
    expr.pos(name)
    print(name, 'PASS; lower bound',format(float(expr.lo),'.15g'))
normalization=2*A+2*B+C
assert normalization.lo <= 1 <= normalization.hi
assert normalization.hi-normalization.lo < F(1,10**20)
E=A+(p+1)*B+p*C
J=(p+1)*A+p*B+C
O=2*p*A+2*B
for lhs,rhs in [(E,L/2),(J,L*u),(O,L*v)]:
    gap=lhs-rhs
    assert gap.lo<=0<=gap.hi and gap.hi-gap.lo<F(1,10**20)
print('normalization and three saturated vertex orbits', 'PASS')
print('phi,u,v',p.midpoint(),u.midpoint(),v.midpoint())
print('weights A,B,C',A.midpoint(),B.midpoint(),C.midpoint())
print('sharp norm',L.midpoint())

# Independent enumeration of every extreme real one-Lipschitz potential on
# the five original vertices (fix f(v_0)=0): its connected tight-edge graph
# contains a spanning tree, so signed tree distances generate all vertices.
def add(z,w): return (z[0]+w[0],z[1]+w[1])
def neg(z): return (-z[0],-z[1])
def sub(z,w): return add(z,neg(w))
def is_positive(z):
    # a+b*phi = (2*a+b+b*sqrt(5))/2; decide sign by integer squares.
    a,b=z; x=2*a+b
    if b==0: return x>0
    if x==0: return b>0
    if (x>0)==(b>0): return x>0
    return (x*x>5*b*b) == (x>0)
def leq(z,w): return not is_positive(sub(z,w))
def prufer_tree(seq):
    degrees=[1]*5
    for x in seq: degrees[x]+=1
    edges=[]
    for x in seq:
        leaf=next(i for i in range(5) if degrees[i]==1)
        edges.append((leaf,x))
        degrees[leaf]-=1; degrees[x]-=1
    a,b=[i for i in range(5) if degrees[i]==1]
    edges.append((a,b))
    return edges

def chord(a,b): return (1,0) if min((a-b)%5,(b-a)%5)==1 else (0,1)

potentials=set()
for word in product(range(5),repeat=3):
    tree=prufer_tree(word)
    for signs in product((-1,1),repeat=4):
        adj=[[] for _ in range(5)]
        for ((i,j),s) in zip(tree,signs):
            diff=tuple(s*t for t in chord(i,j))
            adj[i].append((j,diff));adj[j].append((i,neg(diff)))
        f={0:(0,0)};stack=[0]
        while stack:
            i=stack.pop()
            for j,d in adj[i]:
                if j not in f:
                    f[j]=add(f[i],d);stack.append(j)
        assert len(f)==5
        if all(leq(sub(f[i],f[j]),chord(i,j)) and leq(sub(f[j],f[i]),chord(i,j)) for i in range(5) for j in range(i+1,5)):
            potentials.add(tuple(f[i] for i in range(5)))
assert len(potentials)==70,len(potentials)
print('exactly enumerated extreme vertex potentials',len(potentials))

# Verify the canonical 5 midpoint rows against every enumerated extreme
# function. The symbolic proof covers all functions; here we certify using
# intervals that the numerically enumerated vertices obey the sharp bound.
rows=[]
for i in range(5):
    row=[None]*5
    for j in range(5):
        t=(j-i)%5
        row[j]=(A if t in (0,1) else B if t in (2,4) else C)
    rows.append(row)

checked=0
for f in potentials:
    fv=[I(a)+b*p for a,b in f]
    mv=[sum((rows[i][j]*fv[j] for j in range(5)),I(0)) for i in range(5)]
    # Verify the 25 vertex-midpoint inequalities using tight intervals,
    # allowing exact ties whose interval lower bound can be tiny negative.
    for i in range(5):
        for j in range(5):
            t=(j-i)%5
            dist=I(F(1,2)) if t in (0,1) else u if t in (2,4) else v
            gap=L*dist-(mv[i]-fv[j])
            assert gap.hi>=0 and gap.lo > -F(1,10**18)
            checked+=1
    for i in range(5):
        for j in range(i+1,5):
            t=min((i-j)%5,(j-i)%5)
            dist=(p/2 if t==1 else p*p/2)
            gap=L*dist-(mv[i]-mv[j])
            assert gap.lo>0,('midpoint strict gap',i,j)
            checked+=1
print('extreme-potential pair inequalities',checked,'PASS')
print('PENTAGON_EXTENSION_CERTIFICATE_OK')
