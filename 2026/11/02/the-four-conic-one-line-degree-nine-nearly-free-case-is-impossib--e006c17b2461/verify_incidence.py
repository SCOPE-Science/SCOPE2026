#!/usr/bin/env python3
"""Exact combinatorial checks supporting the degree-nine exclusion.

The geometric common-tangent lemma and dual Bezout argument are proved in
RESULT.md; this script tests their arithmetic consequences, not geometry.
"""
from fractions import Fraction

m,k,d=9,4,1
admissible=[]
for r in range(0,10):
    if not (Fraction(2*m,3)-2 <= r <= Fraction(m,2)):
        continue
    if r!=4: continue
    tau=r*r-r*(m-1)+(m-1)**2-1
    for n2 in range(33):
        for t in range(17):
            for n3 in range(12):
                if n2+3*t+4*n3!=tau: continue
                if n2+2*t+3*n3!=4*(k*(k-1)//2)+2*k*d: continue
                if 8*k+n2+Fraction(3,4)*n3 < d+Fraction(5,2)*t:continue
                admissible.append((r,n2,t,n3))
assert admissible==[(4,0,13,2)],admissible
# A line meets each conic with degree 2. With no nodes and at most
# two triples on L, s must be 0 or 2. Case s=0: four line-conic
# tangencies, and every conic pair has <=1 tacnode by common-tangent
# obstruction. Case s=2: two line tangencies, and among six conic pairs
# the pair through both triples and the tangent pair each has <=1,
# leaving four pairs with <=2.
upper={0:4+6,2:2+1+1+4*2}
assert upper=={0:10,2:12}
assert max(upper.values())<13
print('DEGREE9_FOUR_CONICS_EXCLUSION_OK')
