#!/usr/bin/env python3
"""Standalone exact checks for a low-degree Jacobi relative-extremum theorem.

Requires sympy.  Run: python verify.py
The paper proof, not this finite checker, proves the universal claims.
"""
import sympy as S

a,b,x=S.symbols('a b x', real=True)
P1=S.jacobi(1,a,b,x)
P2=S.jacobi(2,a,b,x)
P3=S.jacobi(3,a,b,x)
R=S.sqrt((a+3)*(b+3)/(a+b+5))
x2=(b-a)/(a+b+4)
x3=(b-a+2*R)/(a+b+6)
assert S.simplify(S.diff(P2,x).subs(x,x2))==0
assert S.simplify(S.diff(P3,x).subs(x,x3))==0
assert S.simplify(P2.subs(x,x2) + (a+2)*(b+2)/(2*(a+b+4)))==0
rem=-(a+3)*(b+3)*((a+b+4)*x+a-b)/(6*(a+b+6))
assert S.simplify(S.rem(P3,S.diff(P3,x),x)-rem)==0
M1=(b+1)/(a+1)
M2=(b+2)/((a+1)*(a+b+4))
M3=2*(b+3)*(a-b+(a+b+4)*R)/((a+1)*(a+2)*(a+b+6)**2)
assert S.simplify(-P3.subs(x,x3)/P3.subs(x,1)-M3)==0
assert S.simplify(-P2.subs(x,x2)/P2.subs(x,1)-M2)==0
assert S.simplify(-P1.subs(x,-1)/P1.subs(x,1)-M1)==0
U=2*(b+3)**3*S.sqrt(2*(b+3)*(b+4))
V=(b+4)*(2*(b+1)*(b+3)**2+(b+2)*(b+5)**2)
C=b**3+7*b**2+14*b+4
assert S.expand(U**2-V**2 + (b+2)*(b+4)*(b+5)**3*C)==0
L1=b+1
L2=(b+2)/(b+3)
L3=2*(b+3)*((b+3)*S.sqrt(2*(b+3)/(b+4))-(b+1))/(b+5)**2
assert S.simplify((L2-L1)+(b**2+3*b+1)/(b+3))==0
# Radical identity tested at exact rational beta values; its general validity
# follows algebraically by rationalizing the positive square root.
for bv in [-S.Rational(9,10),-S.Rational(1,2),-S.Rational(3,8),S.Rational(0),S.Rational(1),S.Rational(5,2)]:
    assert S.simplify(((L3-L2)*(b+3)*(b+4)*(b+5)**2-U+V).subs(b,bv))==0
beta1=(-3+S.sqrt(5))/2
assert S.simplify(C.subs(b,beta1)-beta1)==0
aw,bw=-S.Rational(19,20),-S.Rational(3,8)
assert M1.subs({a:aw,b:bw}) == S.Rational(25,2)
assert M2.subs({a:aw,b:bw}) == S.Rational(1300,107)
assert S.simplify(R**2).subs({a:aw,b:bw})==S.Rational(41,28)
rat=S.Rational(553037,457960)
assert S.simplify(R**2).subs({a:aw,b:bw})-rat**2 == S.Rational(8755992817,1468091531200)>0
assert M2.subs({a:aw,b:bw})<M1.subs({a:aw,b:bw})
assert bool((M3-M2).subs({a:aw,b:bw}).evalf(40)>0)
# A deterministic finite set of checks confirms the symbolic critical-value
# expressions against direct classical Jacobi evaluation.
count=0
for av in [-S.Rational(19,20),-S.Rational(2,3),S.Rational(0),S.Rational(1,3),S.Rational(2)]:
 for bv in [-S.Rational(3,8),-S.Rational(1,4),S.Rational(0),S.Rational(1),S.Rational(7,3)]:
  vals={a:av,b:bv}
  for idx,xx,poly,mm in [(2,x2,P2,M2),(3,x3,P3,M3)]:
   cv=S.N(xx.subs(vals),30)
   assert -1<cv<1
   direct=abs(S.N(poly.subs(vals).subs(x,cv)/poly.subs(vals).subs(x,1),30))
   expected=S.N(mm.subs(vals),30)
   assert abs(direct-expected)<S.Rational(1,10**23)
   count+=1
print('PASS: symbolic polynomial, boundary, witness, and',count,'finite-value checks')
