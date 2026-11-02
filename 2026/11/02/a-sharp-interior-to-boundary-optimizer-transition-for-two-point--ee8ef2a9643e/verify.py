#!/usr/bin/env python3
"""Finite exact support checks for the explicitly proved coefficient-sign argument.
No finite test is substituted for the analytic infinite-index inequality.
"""
from fractions import Fraction as F
from math import factorial, sqrt
import sympy as S
p=S.symbols('p',real=True)
a=lambda n:S.Rational(2)*(1+(5**(n+2)-1)*p)/((1+24*p)*S.factorial(n+2))
expected={2:-(16576*p*p-952*p+1)/(36*(1+24*p)**2),3:-(80976*p*p-2852*p+1)/(45*(1+24*p)**2),4:-(2796032*p*p-61664*p+7)/(720*(1+24*p)**2)}
checks=0
for n in (2,3,4):
 b=(n-1)*a(n)-sum(a(i)*a(n-i) for i in range(1,n))
 assert S.simplify(b-expected[n])==0;checks+=1
p4=(S.Rational(1927)+575*S.sqrt(11))/174752
pc=S.Rational(17,592)+S.Rational(25,4144)*S.sqrt(21)
for expr in [p4-S.Rational(1,50),pc-p4,1-pc,pc-S.Rational(1,20)]:
 assert expr.evalf(60)>0;checks+=1
assert S.simplify((2796032*p*p-61664*p+7).subs(p,p4))==0;checks+=1
assert S.simplify((16576*p*p-952*p+1).subs(p,pc))==0;checks+=1
n=S.symbols('n',integer=True,positive=True)
g=(337*n*n-2799*n+9704)/5550
assert S.simplify(g.subs(n,5)-S.Rational(689,925))==0;checks+=1
assert S.simplify(g.subs(n,n+1)-g-(337*n-1231)/2775)==0;checks+=1
for nn in range(5,81):
 assert g.subs(n,nn)>0;checks+=1
for pp in [F(1,40),F(3,100),F(1,20),F(1,10),F(1,2),F(1,1)]:
 for nn in range(5,35):
  A=lambda k:F(2*(1+(5**(k+2)-1)*pp),1+24*pp)/factorial(k+2)
  b=(nn-1)*A(nn)-sum(A(i)*A(nn-i) for i in range(1,nn))
  assert b<0;checks+=1
print('PASSED',checks,'exact/symbolic assertions')
