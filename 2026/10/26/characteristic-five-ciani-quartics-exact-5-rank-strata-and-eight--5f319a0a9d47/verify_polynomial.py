#!/usr/bin/env python3
"""Formal polynomial coefficient checker in characteristic 5; stdlib only.
Expands all six terms of the Ciani quartic to the fourth power and
compares the three required Hasse-Witt coefficients symbolically.
"""
from itertools import product
from math import factorial
M=[((4,0,0),(0,0,0)),((0,4,0),(0,0,0)),((0,0,4),(0,0,0)),((2,2,0),(1,0,0)),((0,2,2),(0,1,0)),((2,0,2),(0,0,1))]
def norm(d):return {k:v%5 for k,v in d.items() if v%5}
def pol(*terms):
 d={}
 for k,v in terms:d[k]=(d.get(k,0)+v)%5
 return norm(d)
def add(*parts):
 d={}
 for part in parts:
  for k,v in part.items():d[k]=(d.get(k,0)+v)%5
 return norm(d)
def scale(a,p):return norm({k:(a*v)%5 for k,v in p.items()})
def difference(a,b):return add(a,scale(-1,b))
def multiply(a,b):
 d={}
 for x,u in a.items():
  for y,v in b.items():
   k=tuple(i+j for i,j in zip(x,y));d[k]=(d.get(k,0)+u*v)%5
 return norm(d)
R={(1,0,0):1};S={(0,1,0):1};T={(0,0,1):1};ONE={(0,0,0):1}
def sq(a):return multiply(a,a)
def expcoeff(target):
 d={}
 for c in product(range(5),repeat=6):
  if sum(c)!=4:continue
  dg=tuple(sum(c[i]*M[i][0][j] for i in range(6)) for j in range(3))
  if dg!=target:continue
  v=factorial(4)//__import__('math').prod(factorial(n) for n in c)
  e=tuple(sum(c[i]*M[i][1][j] for i in range(6)) for j in range(3))
  d[e]=(d.get(e,0)+v)%5
 return norm(d)
R2=sq(R);S2=sq(S);T2=sq(T);RST=multiply(multiply(R,S),T)
expected=[
 add(multiply(R2,T2),scale(2,R2),scale(-1,RST),S2,scale(2,T2),scale(2,ONE)),
 add(multiply(R2,S2),scale(2,R2),scale(-1,RST),scale(2,S2),T2,scale(2,ONE)),
 add(R2,scale(-1,RST),multiply(S2,T2),scale(2,S2),scale(2,T2),scale(2,ONE))]
actual=[expcoeff(tgt) for tgt in [(8,4,4),(4,8,4),(4,4,8)]]
assert actual==expected,(actual,expected)
# Factor comparisons: H1-H2=(t²-s²)(r²+1), etc.
assert difference(actual[0],actual[1])==multiply(difference(T2,S2),add(R2,ONE))
assert difference(actual[1],actual[2])==multiply(difference(R2,T2),add(S2,ONE))
assert difference(actual[2],actual[0])==multiply(difference(S2,R2),add(ONE,T2))
print('POLYNOMIAL_VERIFY_OK',len(actual))
