#!/usr/bin/env python3
"""Exact association-scheme and seven-to-eight boundary checks.
Finite checks are auxiliary; see RESULT.md for the infinite proof.
"""
from math import comb
from fractions import Fraction

def params(k,j):
 n=3*k-2
 b=(-1)**j*comb(2*k-2-j,k-j)
 theta=(k-j)*(n-k-j)-j
 r=Fraction(theta-k*(k-2),k-1)
 return b,r

for k in range(3,31):
 n=3*k-2
 for j in range(1,k+1):
  b,r=params(k,j)
  # Independent binomial-inclusion sum for intersection-one adjacency.
  def beta(s):
   return comb(k-j,s-j)*comb(n-s-j,k-s) if j<=s else 0
  c=sum((-1)**(s-1)*s*beta(s) for s in range(j,k+1))
  assert c==b*r,(k,j,b,r,c)
  assert b==sum((-1)**s*beta(s) for s in range(j,k+1))

# Certified rational bounds via integer 100th powers.
TL=Fraction(1006955,1000000); TH=Fraction(1006956,1000000)
UL=Fraction(1011046,1000000); UH=Fraction(1011047,1000000)
assert TL**100<2<TH**100
assert UL**100<3<UH**100
# k=7: j=2 negative, j=3 positive at p=1/100.
L2_up=-TL+252*(Fraction(13,6)*(UH-TL)-(TL-1))
L3_lo=-TL+126*((TL-1)+(UL-TL)/3)
assert L2_up<0<L3_lo,(L2_up,L3_lo)
print('KNESER_NEGATIVE_TYPE_CHECK_OK', 'association_eigenvalues=',sum(range(3,31)),
      'boundary_j2_upper=',float(L2_up),'boundary_j3_lower=',float(L3_lo))
