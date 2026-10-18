#!/usr/bin/env python3
"""Verify rational certificates for an ecological two-frequency mutation transition."""
from fractions import Fraction as F
from math import isfinite
import sympy as s
x,b=s.symbols('x b')
f= -x/2-s.Rational(3)/(1+x*x)-900*b/(900+x*x)
df=s.diff(f,x)
h=(((1+x*x)**2-12*x)*(900+x*x)**2)/(3600*x*(1+x*x)**2)
Q=x**8-297*x**6-897*x**4+14384*x**3-899*x*x-300
assert s.factor(s.diff(h,x)-(x*x+900)*Q/(1200*x*x*(1+x*x)**3))==0
assert s.factor(df.subs(b,h))==0
assert [s.sign(Q.subs(x,t)) for t in (0,s.Rational(1,2),4,20)]==[-1,1,-1,1]
assert [s.sign(df.subs({x:t,b:k})) for t,k in [(0,26),(s.Rational(1,5),26),(2,26),(3,26),(9,26),(13,26),(24,26),(28,26)]]==[-1,1,1,-1,-1,1,1,-1]
assert [s.sign(df.subs({x:t,b:27})) for t in (0,s.Rational(1,5),2,3,9,13,24,28)]==[-1,1,1,-1,-1,1,1,-1]
assert s.factor((x/2+s.Rational(23400)/(900+x*x)-s.Rational(277,10))*10*(900+x*x))==5*x**3-277*x*x+4500*x-15300
assert s.factor((x/2+3/(1+x*x)-3*x*x/100-s.Rational(36,25))*100*(1+x*x))==-3*x**4+50*x**3-147*x*x+50*x+156
assert f.subs({x:2,b:26})==-s.Rational(15529,565)
assert f.subs({x:26,b:27})==-s.Rational(7581551,266738)
assert f.subs({x:2,b:26})>-s.Rational(277,10)
assert f.subs({x:26,b:27})>-s.Rational(711,25)
assert s.factor((f.subs(x,2)-f.subs(x,0))-(s.Rational(7,5)+b/s.Rational(226)))==0
# Bisection to independently bracket the two internal maxima for fixed amplitude.
fval=s.lambdify((x,b),f,'math');dval=s.lambdify((x,b),df,'math')
def bisect(g,lo,hi):
    gl=g(lo)
    assert gl*g(hi)<0
    for _ in range(110):
        m=(lo+hi)/2
        gm=g(m)
        if gm==0: return m
        if gm*gl>0:lo,gl=m,gm
        else:hi=m
    return (lo+hi)/2
def gap(B):
    low=bisect(lambda y:dval(y,B),2,3)
    high=bisect(lambda y:dval(y,B),24,28)
    return fval(high,B)-fval(low,B),low,high
assert gap(26)[0]<-.37 and gap(27)[0]>.048
bstar=bisect(lambda B:gap(B)[0],26,27)
g,low,high=gap(bstar)
assert abs(g)<1e-11 and 26.88<bstar<26.90 and 2<low<3 and 24<high<28
print('PASS; B*=%.12f, low y=%.12f, high y=%.12f; D=%.12f and %.12f' %(bstar,low,high,(low/2)**2,(high/2)**2))
