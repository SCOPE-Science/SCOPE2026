#!/usr/bin/env python3
"""Exact checks of the random-coordinate momentum covariance identity."""
from fractions import Fraction as F

def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def mat(q,b,s):
    return [[1-2*q*s+q*s*s,2*q*b*s*(s-1),q*b*b*s*s],
            [1-q*s,b*(1-2*q*s),-q*b*b*s],
            [1,2*b,b*b]]

def moments_of(A):
    # For y' = c*x+d*y, x'=a*x+b*y, transform E[x^2],E[x*y],E[y^2].
    (a,b),(c,d)=A
    return [[a*a,2*a*b,b*b], [a*c,a*d+b*c,b*d], [c*c,2*c*d,d*d]]

checks=0
for q in map(F,range(4)):
 for beta in map(F,range(7)):
  for s in map(F,range(5)):
   M=mat(q,beta,s)
   assert determinant3([[int(i==j)-M[i][j] for j in range(3)] for i in range(3)]) == q*s*(2*(1-beta*beta)-(1+beta-2*beta*q)*s)
   checks+=1
   A0=[[F(1),F(0)],[F(1),beta]]
   A1=[[1-s,-s*beta],[F(1),beta]]
   M0=moments_of(A0); M1=moments_of(A1)
   for i in range(3):
    for j in range(3):
     assert M[i][j] == (1-q)*M0[i][j]+q*M1[i][j]
     checks+=1
# Exact threshold instances and deterministic comparison.
for (q,b,s_star) in [(F(2,3),F(1,2),F(9,5)),(F(1,1),F(1,2),F(3)),(F(1,2),F(3,4),F(7,8))]:
 assert s_star == 2*(1-b*b)/(1+b-2*b*q)
 checks+=1
print('VERIFY_OK exact assertions:',checks)
