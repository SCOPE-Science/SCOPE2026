#!/usr/bin/env python3
"""Symbolic and rational checks for the sticky-wall absorption allocation theorem.
Run with Python 3 and SymPy; no input files or remote access required.
"""
from sympy import symbols, Rational, simplify, factor, diff, together, solve, sqrt
from fractions import Fraction
import random

u,B,p,h,y = symbols('u B p h y', positive=True, finite=True)
Q = B*h + (p+1)*u*(B-u)
C = (u*(2+2*h+(p+1)*(B-u))-B)/Q
A0 = B*(h*(p+1)+p+Rational(1,2)) + 2*h*(h+1)
A1 = B*(p+1)/2 - p*(h+1)
S = (A0+A1*u-(p+1)*u**2/2)/Q
F = S + p*(C*y-y*y)
checks=0

def check(expr):
    global checks
    assert simplify(expr)==0, str(factor(expr))
    checks+=1

# Backward equations: t_+(x)=S+p(C*x-x*x)+(C-2*x)/2,
# t_-(x)=S+p(C*x-x*x)-(C-2*x)/2 on the unit interval.
x=symbols('x',real=True)
sx=S+p*(C*x-x*x); dx=C-2*x
plus=sx+dx/2;minus=sx-dx/2
check(diff(plus,x)+p*(minus-plus)+1)
check(-diff(minus,x)+p*(plus-minus)+1)
check(u*minus.subs(x,0)-h*(plus.subs(x,0)-minus.subs(x,0))-1)
check((B-u)*plus.subs(x,1)+h*(plus.subs(x,1)-minus.subs(x,1))-1)

# Independent 2023 mean-exit expression, with bulk flip rate p,
# boundary detachment h, and walls at distances y and 1-y.
R=Rational(1,2); Xc=R-y
ha=1+h; hb=ha
fa=2*h+u*(1+p); fb=2*h+(B-u)*(1+p)
angelani = R + p*(R**2-Xc**2) + (hb*fa+ha*fb)/((B-u)*fa+u*fb) + 2*p*Xc*((B-u)*ha-u*hb)/((B-u)*fa+u*fb)
check(F-angelani)

check(diff(F,u).subs(u,B/2) - 4*p*(h+1)*(2*y-1)/(B*(B*p+B+4*h)))
check(diff(F,u,2).subs({u:B/2,y:R}) - 16*(h+1)*(p+1)/(B**2*(B*p+B+4*h)))
check(diff(C,u) - (h+1)*((p+1)*(B**2-2*B*u+2*u*u)+2*B*h)/Q**2)
check(-p*diff(C,u).subs(u,B/2)/diff(F,u,2).subs({u:B/2,y:R})+B*p/(2*(p+1)))
check(F.subs({u:B/2,y:R})-(B*p+2*B+8*h+8)/(4*B))

# Endpoint derivative signs: each bracket has a fixed sign for 0<=y<=1.
H0 = (h+1)*(2*B*p*p*(y-1)+B*p*(2*y-3)-B+2*h*p*(2*y-3)-4*h)/(2*B*h*h)
HB = (h+1)*(2*B*p*p*y+B*p*(2*y+1)+B+2*h*p*(2*y+1)+4*h)/(2*B*h*h)
check(diff(F,u).subs(u,0)-H0)
check(diff(F,u).subs(u,B)-HB)

# Exact normalized example p=h=B=1, y=1/4.
ex=F.subs({B:1,p:1,h:1,y:Rational(1,4)})
check(ex-(22*u*u-6*u-115)/(16*(2*u*u-2*u-1)))
opt=(13-sqrt(141))/2
check(diff(ex,u).subs(u,opt))

# For multiple exact rational cases, prove numerical-sign witnesses without floating error.
for bb in [Rational(1,2),1,2,5]:
  for pp in [Rational(1,4),1,4]:
    for hh in [Rational(1,3),1,3]:
      for yy in [Rational(1,10),Rational(1,2),Rational(9,10)]:
        subs={B:bb,p:pp,h:hh,y:yy}
        assert diff(F,u).subs(subs).subs(u,0)<0
        assert diff(F,u).subs(subs).subs(u,bb)>0
        assert diff(C,u).subs(subs).subs(u,bb/3)>0
        checks+=3
print(f'PASS {checks} exact symbolic/rational checks')

# Orientation-biased initial conditions: m is mean signed initial velocity.
m = symbols('m',real=True)
Fdir = F + m*(C-2*y)/2
Bden = (p+1)*(B*B-2*B*u+2*u*u)+2*B*h
Theta = simplify(-diff(S,u)/diff(C,u))
check(diff(C,u)*(p*y+m/2-Theta)-diff(Fdir,u))
check(diff(Theta,u) + 2*(p+1)*(B*(p+1)+4*h)*Q/Bden**2)
check(Theta.subs(u,0)-(p+Rational(1,2)+h*(p+1)/(B*(p+1)+2*h)))
check(Theta.subs(u,B)-(-Rational(1,2)-h*(p+1)/(B*(p+1)+2*h)))
check(Theta.subs(u,B/2)-p/2)
# Orientation and initial location simply shift the common monotone threshold.
check(diff(Fdir,u).subs(u,B/2)- (p*(y-R)+m/2)*diff(C,u).subs(u,B/2))
check(diff(C,u).subs(u,B/2) - 8*(h+1)/(B*(B*(p+1)+4*h)))
check(-diff(C,u).subs(u,B/2)/(2*diff(Fdir,u,2).subs({u:B/2,y:R,m:0})) +B/(4*(p+1)))
# In all physically feasible cases, the endpoint signs are strict.
for bb in [Rational(1,2),1,2]:
  for pp in [Rational(1,4),1,4]:
    for hh in [Rational(1,3),1,3]:
      for yy in [0,Rational(1,4),Rational(3,4),1]:
        for mm in [-1,0,1]:
          z={B:bb,p:pp,h:hh,y:yy,m:mm}
          assert diff(Fdir,u).subs(z).subs(u,0)<0
          assert diff(Fdir,u).subs(z).subs(u,bb)>0
          checks+=2
print(f'PASS {checks} including all-direction boundary witnesses')
