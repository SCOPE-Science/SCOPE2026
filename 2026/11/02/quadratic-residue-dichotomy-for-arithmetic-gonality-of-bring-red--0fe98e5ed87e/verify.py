#!/usr/bin/env python3
"""Exact finite-field tests for the arithmetic gonality certificate of the symmetric genus-four complete intersection."""
from itertools import combinations,product
import sympy as S

def mul(x,y):
 a,b=divmod(x,3);c,d=divmod(y,3)
 # field F9 = F3[w]/(w^2+1), x=a*w+b
 return (((a*d+b*c)%3)*3 + (b*d+2*a*c)%3)
def add(x,y):return (((x//3+y//3)%3)*3+(x%3+y%3)%3)
def neg(x):return (((-x//3)%3)*3+(-(x%3))%3) if False else ((-x//3)%3)*3+(-(x%3))%3
# note negative quotient bug avoided by arithmetic explicit
neg=lambda x: ((-(x//3))%3)*3+(-(x%3))%3
one=1

def polys(u):
 e1=e2=e3=0
 for i in range(5):e1=add(e1,u[i])
 for ii in combinations(range(5),2):e2=add(e2,mul(u[ii[0]],u[ii[1]]))
 for ii in combinations(range(5),3):e3=add(e3,mul(mul(u[ii[0]],u[ii[1]]),u[ii[2]]))
 return (e1,e2,e3)

def power(x,n):
 r=1
 for _ in range(n):r=mul(r,x)
 return r

C=[]
# projective P3: [a:b:c:d:e] with sum=0, use four free a,b,c,d and e=-(a+b+c+d)
for k in range(4):
 # normalization first nonzero among a,b,c,d equals 1
 for tail in product(range(9),repeat=3-k):
  a=[0]*k+[one]+list(tail)
  e=0
  for t in a:e=add(e,t)
  u=tuple(a+[neg(e)])
  if polys(u)==(0,0,0):C.append(u)
print('F9 count',len(C))
F3=[p for p in C if all(power(x,3)==x for x in p)]
print('F3 count',len(F3))
print('F9 point',next((p for p in C if p not in F3),None))
print('Frobenius',tuple(power(x,3) for x in next(p for p in C if p not in F3)))
# determinant Hessian of quadric over Z before reduction
z=S.symbols('a b c d');vec=list(z)+[-sum(z)]
q=S.expand(sum(vec[i]*vec[j] for i in range(5) for j in range(i+1,5)))
print('Hessian determinant mod3',int(S.hessian(q,z).det())%3)
assert len(C)==30 and not F3 and int(S.hessian(q,z).det())%3==2
assert len({u for u in C})==len(C)
print('VERIFY_OK')
