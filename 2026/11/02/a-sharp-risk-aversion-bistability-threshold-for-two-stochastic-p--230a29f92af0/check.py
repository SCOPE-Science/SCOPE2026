#!/usr/bin/env python3
"""Exact symbolic and rational verification of two-route Bernoulli mean-variance routing."""
from random import Random
import sympy as S

y,g=S.symbols('y g',real=True)
u,H,s,t,d,c=S.symbols('u H s t d c',real=True)
count=0

def check(v):
    global count
    assert bool(v)
    count+=1

def same(a,b):
    check(S.simplify(a-b)==0)

A=c+d*(1-y)
B0=u+s*y
B1=u+H+t*y
mean=S.expand((B0+B1)/2)
variance=S.expand(((B0-mean)**2+(B1-mean)**2)/2)
delta=s-t
v=(s+t)/2
costgap=S.expand(mean+g*variance-A)
formula=u+H/2-c-d+(v+d)*y+g*(H-delta*y)**2/4
same(mean,u+H/2+v*y)
same(variance,(H-delta*y)**2/4)
same(costgap,formula)
same(S.diff(costgap,y,2),g*delta**2/2)
same((costgap.subs(y,0)-costgap.subs(y,1)),g*delta*(2*H-delta)/4-(v+d))
critical=4*(v+d)/(delta*(2*H-delta))
lower=u+H/2+v+g*(H-delta)**2/4
upper=u+H/2-d+g*H**2/4
same(upper-lower,(g-critical)*delta*(2*H-delta)/4)

F=S.expand(costgap.subs({u:0,H:4,s:3,t:1,d:1,c:S.Rational(27,5)}))
same(F,g*(y-2)**2+3*y-S.Rational(22,5))
same(F.subs(y,0),4*g-S.Rational(22,5))
same(F.subs(y,1),g-S.Rational(7,5))
same(S.discriminant(F,y),9-S.Rational(32,5)*g)
same(F.subs(g,S.Rational(11,10)),y*(11*y-14)/10)
same(F.subs(g,S.Rational(7,5)),(y-1)*(7*y-6)/5)
same(F.subs(g,S.Rational(45,32)),(15*y-14)**2/160)
same(F.subs(g,S.Rational(6,5)),(6*y*y-9*y+2)/5)
same(critical.subs({H:4,s:3,t:1,d:1}), S.Rational(1))
# General parameter sharp threshold is distinct from the chosen fixed-c bifurcation.
rootminus=(4*g-3-S.sqrt(9-S.Rational(32,5)*g))/(2*g)
rootplus=(4*g-3+S.sqrt(9-S.Rational(32,5)*g))/(2*g)
same(F.subs(y,rootminus),0)
same(F.subs(y,rootplus),0)
same(rootminus.subs(g,S.Rational(7,5)),S.Rational(6,7))
same(rootplus.subs(g,S.Rational(7,5)),1)
same(rootminus.subs(g,S.Rational(45,32)),S.Rational(14,15))
same(rootplus.subs(g,S.Rational(45,32)),S.Rational(14,15))
same(rootminus.subs(g,S.Rational(6,5)),(9-S.sqrt(33))/12)
same(rootplus.subs(g,S.Rational(6,5)),(9+S.sqrt(33))/12)

# Independent boundary and interior checks at all five transitions; count_roots counts endpoint roots.
for gamma,interior,end0,end1 in [
    (S.Rational(0),0,False,True),
    (S.Rational(1),0,False,True),
    (S.Rational(11,10),0,True,True),
    (S.Rational(6,5),1,True,True),
    (S.Rational(7,5),1,True,True),
    (S.Rational(281,200),2,True,False),
    (S.Rational(45,32),1,True,False),
    (S.Rational(3,2),0,True,False),
]:
    ff=S.Poly(F.subs(g,gamma),y)
    check(ff.count_roots(S.Rational(1,100000),S.Rational(99999,100000))==interior)
    check((ff.eval(0)>=0)==end0)
    check((ff.eval(1)<=0)==end1)

# Continuous intervals tested by many exact rationals, with root count independent of explicit formula.
rand=Random(42107)
for lo,hi,numroots,end0,end1 in [
    (S.Rational(0),S.Rational(11,10),0,False,True),
    (S.Rational(11,10),S.Rational(7,5),1,True,True),
    (S.Rational(7,5),S.Rational(45,32),2,True,False),
    (S.Rational(45,32),S.Rational(2),0,True,False),
]:
    for _ in range(40):
        a=S.Rational(rand.randrange(1,10000),10000)
        gamma=lo+(hi-lo)*a
        ff=S.Poly(F.subs(g,gamma),y)
        check(ff.count_roots(S.Rational(0),S.Rational(1))==numroots)
        check((ff.eval(0)>0)==end0)
        check((ff.eval(1)<0)==end1)

# Direct Bernoulli enumeration and exact sharp c interval for random admissible slope/intercept tuples.
for _ in range(120):
    uu=S.Rational(rand.randrange(0,10),5)
    ss=S.Rational(rand.randrange(3,15),4)
    tt=ss*S.Rational(rand.randrange(1,9),10)
    HH=(ss-tt)+S.Rational(rand.randrange(1,9),5)
    dd=S.Rational(rand.randrange(1,7),4)
    vvv=(ss+tt)/2
    deltaa=ss-tt
    gc=4*(vvv+dd)/(deltaa*(2*HH-deltaa))
    gg=gc+S.Rational(rand.randrange(1,11),10)
    c_lo=uu+HH/2+vvv+gg*(HH-deltaa)**2/4
    c_hi=uu+HH/2-dd+gg*HH**2/4
    cc=(c_lo+c_hi)/2
    check(c_hi>c_lo>0)
    f0=uu+HH/2-cc-dd+gg*HH**2/4
    f1=uu+HH/2+vvv-cc+gg*(HH-deltaa)**2/4
    check(f0>0 and f1<0)
    check(S.Poly(f0+(vvv+dd-gg*HH*deltaa/2)*y+gg*deltaa**2*y*y/4,y).count_roots(0,1)==1)
    gglo=gc-S.Rational(rand.randrange(1,11),10)*gc/S.Integer(20)
    check(gglo>0)
    width=gglo*deltaa*(2*HH-deltaa)/4-(vvv+dd)
    check(width<0)

print('Exact symbolic/rational assertions passed:',count)
