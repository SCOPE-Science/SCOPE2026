#!/usr/bin/env python3
"""Reproduce exact two-zone probabilistic retail choice calculations.

Pure Python 3 standard library; run with: python verify.py
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import random

checks = 0

def check(c, label=""):
    global checks
    checks += 1
    if not c:
        raise AssertionError(label or 'check failed')


def capture(w, u, t):
    return w * t * u / (1 + t * u)


def diff(t, p1, p2, u1, v1, u2, v2):
    return (capture(p1,u1,t)-capture(p1,v1,t)
            +capture(p2,u2,t)-capture(p2,v2,t))


def q(u, v, t):
    return (1+u*t)*(1+v*t)


def coeffs(p1,p2,u1,v1,u2,v2):
    a = p1*(u1-v1)
    b = p2*(v2-u2)
    return (a-b, a*(u2+v2)-b*(u1+v1), a*u2*v2-b*u1*v1)


def polynomial(t, c):
    return c[0]+c[1]*t+c[2]*t*t

# Two-zone phase diagram and Euclidean realizability example.
p1,p2,u1,v1,u2,v2 = F(1), F(5), F(9), F(1), F(2), F(3)
c=coeffs(p1,p2,u1,v1,u2,v2)
check(c==(F(3),F(-10),F(3)), 'quadratic coefficients')
check(c[0]*c[2]>0 and c[1]*c[2]<0 and c[1]**2>4*c[0]*c[2], 'two crossings')
for t in (F(1,3),F(3)):
    check(diff(t,p1,p2,u1,v1,u2,v2)==0, 'exact crossovers')
for t,expected in [(F(1,6),F(17,420)),(F(1),F(-1,60)),(F(6),F(306,95095))]:
    check(diff(t,p1,p2,u1,v1,u2,v2)==expected, ('example gap',t))
for t in (F(1,6),F(1,3),F(1),F(3),F(6)):
    check(diff(t,p1,p2,u1,v1,u2,v2)==t*polynomial(t,c)/(q(u1,v1,t)*q(u2,v2,t)), 'rational identity')

# Each rational instance satisfies the exact signed numerator identity.
rng=random.Random(20261029)
for k in range(6000):
    vals=[F(rng.randint(1,27),rng.randint(1,20)) for _ in range(7)]
    p1,p2,u1,v1,u2,v2,t=vals
    a=p1*(u1-v1)
    b=p2*(v2-u2)
    c=coeffs(p1,p2,u1,v1,u2,v2)
    numerator=a*q(u2,v2,t)-b*q(u1,v1,t)
    expected=t*numerator/(q(u1,v1,t)*q(u2,v2,t))
    check(diff(t,p1,p2,u1,v1,u2,v2)==expected, 'cross multiplication')
    check(numerator==polynomial(t,c), 'quadratic coefficients')
    if c[2]!=0 and c[0]!=0 and c[1]**2>4*c[0]*c[2]:
        two_positive=(c[0]*c[2]>0 and c[1]*c[2]<0)
        # Algebraic Vieta test under two real unequal roots.
        check(two_positive == ((c[0]/c[2]>0) and (-c[1]/c[2]>0)), 'Vieta')

# Exact squared distances to prospective entrants A=(0,0), B=(1,0).
# z1=(1/18,sqrt(35)/18), z2=(7/12,sqrt(23)/12).
check(F(1,18)**2+F(35,18**2)==F(1,9), 'z1-A')
check((F(1,18)-1)**2+F(35,18**2)==F(1), 'z1-B')
check(F(7,12)**2+F(23,12**2)==F(1,2), 'z2-A')
check((F(7,12)-1)**2+F(23,12**2)==F(1,3), 'z2-B')
with localcontext() as ctx:
    ctx.prec=60
    x1,y1=Decimal(1)/18,Decimal(35).sqrt()/18
    x2,y2=Decimal(7)/12,Decimal(23).sqrt()/12
    ex,ey=(x1+x2)/2,(y1+y2)/2
    d1=(x1-ex)**2+(y1-ey)**2
    d2=(x2-ex)**2+(y2-ey)**2
    check(abs(d1-d2)<Decimal('1e-55'), 'incumbent equal distances')
    check(abs(d1-(Decimal(59)-Decimal(805).sqrt())/432)<Decimal('1e-55'), 'incumbent quality')

print(f'PASS: {checks} exact-rational, structural, and high-precision geometry checks')
