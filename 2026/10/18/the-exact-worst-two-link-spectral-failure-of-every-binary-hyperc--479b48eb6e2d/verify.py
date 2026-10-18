#!/usr/bin/env python3
"""Exact finite identities for the hypercube two-edge consensus gap theorem.
Only Python's standard library is required. The general theorem uses a proof, not this finite check.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def ABC(d,x):
    A=sum((F(2,2**(d-1))*comb(d-1,j)/F(2*(j+1)-x) for j in range(d)),F(0))
    P=sum((F(1,2**(d-2))*comb(d-2,j)*(F(1,2*(j+1)-x)-F(1,2*(j+2)-x)) for j in range(d-1)),F(0))
    V=sum((F(1,2**(d-2))*comb(d-2,j)/F(2*(j+2)-x) for j in range(d-1)),F(0))
    W=sum((F(2,2**(d-2))*comb(d-2,j)/F(2*(j+1)-x) for j in range(d-1)),F(0))
    assert A+P==W
    return A,P,V,W
checks=0
wanted={3:(F(1,2),F(20,21),F(2,231)),4:(F(1),F(14,15),F(1,35)),5:(F(7,5),F(2980,3289),F(7230,141427))}
for d,(x,w,delta) in wanted.items():
    A,P,V,W=ABC(d,x)
    assert W==w and P-V==delta and 0<W<1
    checks+=4
for d in range(3,20):
    lo=F(0);hi=F(2)-F(1,2**40)
    for _ in range(40):
        m=(lo+hi)/2
        if ABC(d,m)[3]<1:lo=m
        else:hi=m
    assert ABC(d,lo)[3]<1<ABC(d,hi)[3]
    if d<=9:
        assert ABC(d,hi)[1]>ABC(d,hi)[2]
    checks+=3
# Every edge pair in 3- and 4-cubes: classify heat correlations with exact rational
# Walsh-mode resolvent. Finiteness is used only to check the proof's formulas.
for d in (3,4):
    n=1<<d
    edges=[(v,v^(1<<i),i) for i in range(d) for v in range(n) if not v&(1<<i)]
    x={3:F(3,5),4:F(6,5)}[d]
    A,P,V,W=ABC(d,x)
    assert W>1 and P>V
    def dot_edge_walsh(edge,s):
        u,v,_=edge
        return (-1)**((s&u).bit_count()%2)-(-1)**((s&v).bit_count()%2)
    for e,f in combinations(edges,2):
        c=sum((F(dot_edge_walsh(e,s)*dot_edge_walsh(f,s),n* (2*s.bit_count()-x)) for s in range(1,n)),F(0))
        assert abs(c)<=P
        same_square=(e[2]==f[2] and ((e[0]^f[0]).bit_count()==1))
        assert (abs(c)==P)==same_square
        checks+=2
print('VERIFY_OK',checks,'exact rational identities and all two-edge heat-resolvent correlations in cubes Q3 and Q4')
