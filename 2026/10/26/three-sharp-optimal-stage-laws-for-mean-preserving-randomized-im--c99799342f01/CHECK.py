#!/usr/bin/env python3
"""Exact identities and independent rational sampling checks for a scalar randomized implicit stage method."""
from fractions import Fraction
from itertools import combinations
import sympy as S

s,t=S.symbols('s t', positive=True)
r=(1-s+s*t)/(1+s*t)
g=S.cancel(r*r)
a=S.factor((2*s*s+s-2)/(s*(s+2)))
sc=(S.sqrt(17)-1)/4
sd=2/S.sqrt(3)
ch=(1-t)*g.subs(t,0)+t*g.subs(t,1)
fac_small=(s**3*t*(t-1)*(s*(s*s-2)*t+2*s*s+s-2))/((s+1)**2*(1+s*t)**2)
assert S.factor(g-ch-fac_small)==0
ell=S.factor(g.subs(t,a)+S.diff(g,t).subs(t,a)*(t-a))
fac_mid=s*(1-t)*(s*(s+2)*(t-a))**2/(4*(s+1)**3*(1+s*t)**2)
assert S.factor(g-ell-fac_mid)==0
mid=S.Rational(1,2)
mtan=S.factor(g.subs(t,mid)+S.diff(g,t).subs(t,mid)*(t-mid))
fac_high=s**3*(2*t-1)**2*(2*s*s*t+s*s-4*s*t+4*s-4)/((s+2)**3*(1+s*t)**2)
assert S.factor(g-mtan-fac_high)==0
pa=1/(2*(1-a));p1=(mid-a)/(1-a)
assert S.factor(pa+p1-1)==0
assert S.factor(pa*a+p1-mid)==0
Msmall=(s**4-2*s*s+2)/(2*(s+1)**2)
Mmid=(-s**3-4*s*s+4*s+8)/(8*(s+1)**3)
Mbig=(2-s)**2/(s+2)**2
assert S.factor(ch.subs(t,mid)-Msmall)==0
assert S.factor((pa*g.subs(t,a)+p1*g.subs(t,1))-Mmid)==0
assert S.factor(g.subs(t,mid)-Mbig)==0
assert S.simplify(Msmall.subs(s,sc)-Mmid.subs(s,sc))==0
assert S.simplify(Mmid.subs(s,sd)-Mbig.subs(s,sd))==0
assert S.factor(S.diff(g,t,2)+2*s**3*(2*s*t-3*s+2)/(1+s*t)**4)==0
assert S.factor(g.subs(t,S.Rational(1,3)).subs(s,1)-S.Rational(1,16))==0
assert S.factor(Mmid.subs(s,1)-S.Rational(7,64))==0
assert S.factor(Msmall.subs(s,S.Rational(1,2))-S.Rational(25,72))==0
assert S.factor(Mbig.subs(s,S.Rational(6,5))-S.Rational(1,16))==0
print('All 16 structural symbolic identities and boundary tests passed.')

def val(q,x):
    return (1-q+q*x)**2/(1+q*x)**2

def opt(q):
    c=(S.sqrt(17)-1)/4
    d=2/S.sqrt(3)
    if S.Rational(q)<=c:
        return (val(q,Fraction(0))+val(q,Fraction(1)))/2
    if S.Rational(q)<d:
        aa=(2*q*q+q-2)/(q*(q+2))
        p=Fraction(1,2)/(1-aa)
        return p*val(q,aa)+(1-p)*val(q,Fraction(1))
    return val(q,Fraction(1,2))

checks=0
for q in [Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(4,5),Fraction(1),Fraction(11,10),Fraction(6,5),Fraction(2),Fraction(4)]:
    best=opt(q)
    # All one-point mean-half laws and all two-point mean-half laws on a 21-node grid.
    assert val(q,Fraction(1,2))>=best;checks+=1
    nodes=[Fraction(i,20) for i in range(21)]
    for u,v in combinations(nodes,2):
        if u<=Fraction(1,2)<=v:
            p=(v-Fraction(1,2))/(v-u)
            avg=p*val(q,u)+(1-p)*val(q,v)
            assert avg>=best, (q,u,v,avg,best)
            checks+=1
    # Convex lower bound of g at arbitrary grid points, using the optimal supporting line.
    for x in nodes:
        if q<=Fraction(3,4):
            bound=(1-x)*val(q,0)+x*val(q,1)
        elif q<=Fraction(11,10):
            aa=(2*q*q+q-2)/(q*(q+2))
            bound=val(q,aa) + (x-aa)*(S.Rational(q)*(q+2)**2/(4*(q+1)**3))
        else:
            slope=2*q*q*(1-q+q*Fraction(1,2))/(1+q*Fraction(1,2))**3
            bound=val(q,Fraction(1,2))+(x-Fraction(1,2))*slope
        assert val(q,x)>=bound,(q,x)
        checks+=1
print(f'All {checks} exact-rational grid inequalities passed; grid tests are illustrative, not the universal proof.')
