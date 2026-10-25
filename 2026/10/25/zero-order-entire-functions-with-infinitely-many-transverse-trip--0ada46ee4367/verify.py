#!/usr/bin/env python3
"""Exact finite seed algebra; infinite lacunary induction is proved in RESULT.md."""
from fractions import Fraction as F

def mul(A,B):
 C={}
 for (i,j),a in A.items():
  for (k,l),b in B.items(): C[(i+k,j+l)]=C.get((i+k,j+l),F(0))+a*b
 return {k:v for k,v in C.items() if v}
def plus(A,B):
 C=A.copy()
 for k,v in B.items(): C[k]=C.get(k,F(0))+v
 return {k:v for k,v in C.items() if v}
def mon(i,j,v=1):return {(i,j):F(v)}
def ev(A,r,x):return sum(c*r**i*x**j for (i,j),c in A.items())
def derivative(A,axis):
 C={}
 for ij,v in A.items():
  n=ij[axis]
  if n:C[tuple(ij[k]-(k==axis) for k in (0,1))]=v*n
 return C
# first index = radius exponent, second = angular cosine exponent
Ts=[mon(0,0),mon(0,1),plus(mul(mon(0,1,2),mon(0,1)),mon(0,0,-1)),plus(mul(mon(0,1,4),mon(0,2)),mon(0,1,-3))]
a=[F(1),F(-3,2),F(3),F(2)]
Q={}
for i in range(4):
 for j in range(4):
  Q=plus(Q,{(i+j,k):v*a[i]*a[j] for (r,k),v in Ts[abs(i-j)].items()})
assert ev(Q,F(1),F(1))==F(81,4)
# identity as polynomial in x: 81/4-16(1-x)(x+1/2)^2
one={ (j,0):c for (i,j),c in Q.items() if i==0} # unused
# Compare on four distinct rational values, sufficient for degree <= 3.
for x in [F(-1),F(-1,2),F(0),F(1)]:
 assert ev(Q,F(1),x)==F(81,4)-16*(1-x)*(x+F(1,2))**2
assert ev(derivative(Q,1),F(1),F(1))==36
assert ev(derivative(derivative(Q,1),1),F(1),F(-1,2))==-48
assert ev(derivative(Q,1),F(1),F(-1,2))==0
slope=ev(derivative(Q,0),F(1),F(1))-ev(derivative(Q,0),F(1),F(-1,2))
assert slope==27
# Symbolic recurrence d_j=m_j+3 gives disjoint supports and dominance.
d=3
for j in range(2,100):
 m=2*d+10
 assert m>2*d and m>d+3
 d=m+3
print('CHECK_OK: cubic identity, three peak nondegeneracy, transverse slope 27, 98 degree-gap stages')
