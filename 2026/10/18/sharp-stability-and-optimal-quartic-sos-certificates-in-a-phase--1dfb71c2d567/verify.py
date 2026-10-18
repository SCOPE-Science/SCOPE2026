"""Reproduce exact algebra for a phase-locked homogeneous cubic flow.

Requires SymPy; the analytical proof and parameter quantifiers are in RESULT.md.
"""
import sympy as S

x,y,a,w,g=S.symbols('x y a w g',real=True)
r2=x*x+y*y
A=x*x-y*y
B=2*x*y
D=a*a+w*w
t=-g*w/D
P=(-a*x-w*y)*r2+g*(x**3-3*x*y*y)
R=(-a*y+w*x)*r2+g*(y**3-3*x*x*y)
V=r2**2+2*t*A*B
Q11=a-(g+t*w)
Q22=a+(g+t*w)
Q12=a*t
Qexpr=Q11*A*A+2*Q12*A*B+Q22*B*B
assert S.cancel(S.expand(S.diff(V,x)*P+S.diff(V,y)*R+4*r2*Qexpr))==0
assert S.cancel(Q11*Q22-Q12**2-a*a*(D-g*g)/D)==0
assert S.cancel(V-(S.Rational(1,2)*(1+t)*(A+B)**2+
                   S.Rational(1,2)*(1-t)*(A-B)**2))==0
assert S.cancel(Q11+Q22-2*a)==0
# A concrete phase-locked example: gamma=1, omega=a=4/5.
sub={a:S.Rational(4,5),w:S.Rational(4,5),g:S.Integer(1)}
assert t.subs(sub)==-S.Rational(5,8)
assert Q11.subs(sub)==S.Rational(3,10)
assert Q12.subs(sub)==-S.Rational(1,2)
assert Q22.subs(sub)==S.Rational(13,10)
assert (Q11*Q22-Q12**2).subs(sub)==S.Rational(7,50)
assert S.factor((-a+g).subs(sub))==S.Rational(1,5) # radial growth at angle 0
assert (a*a+w*w-g*g).subs(sub)==S.Rational(7,25)
# 120 exact sample substitutions; unlike the algebra above they are diagnostic only.
checks=0
for aa in (S.Rational(1,2), S.Rational(4,5), S.Integer(1), S.Integer(2)):
 for ww in (S.Rational(1,4), S.Rational(3,4), S.Integer(1)):
  for gg in (S.Rational(1,2),S.Integer(1)):
   for xx,yy in ((1,0),(1,1),(2,-1),(0,2),(-3,2)):
    eq=(S.diff(V,x)*P+S.diff(V,y)*R+4*r2*Qexpr).subs(
      {a:aa,w:ww,g:gg,x:xx,y:yy})
    assert S.cancel(eq)==0
    checks+=1
print(f'PASS: 4 symbolic identities, 8 exact boundary/Gram checks, {checks} rational instances')
