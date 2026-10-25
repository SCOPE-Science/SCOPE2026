"""Exact-rational replay for binary bilinear extragradient pairing.

This checker is a finite sanity test of identities; the stated universal
classification relies on the algebraic proof in RESULT.md.
Run: python3 CHECK.py
"""
from fractions import Fraction as F

checks = 0

def eq(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1


def normsquared(x):
    return x[0]*x[0] + x[1]*x[1]


def update(x, a, b, h):
    # F_a(x)=a*J*x, J(x,y)=(y,-x); extrapolate by a, correct by b.
    y = (x[0] - h*a*x[1], x[1] + h*a*x[0])
    return (x[0] - h*b*y[1], x[1] + h*b*y[0])


def factor(a, b, h):
    return (1-h*h*a*b)**2+h*h*b*b


def closed(a, b, h):
    t = h*h
    m2 = (a*a+b*b)/2
    m4 = (a**4+b**4)/2
    same = 1-m2*t+m4*t*t
    anti = 1+(m2-2*a*b)*t+(a*b)**2*t*t
    indep = 1-a*b*t+m2*m2*t*t
    return same, indep, anti


def paired(a, b, h, theta):
    p_same = (1+theta)/4
    p_cross = (1-theta)/4
    return (p_same*(factor(a,a,h)+factor(b,b,h))
            + p_cross*(factor(a,b,h)+factor(b,a,h)))

for a in [F(1,3),F(1),F(2),F(5)]:
    for b in [F(1,2),F(1),F(3),F(7)]:
        for h in [F(1,9), F(1,4), F(3,5), F(1), F(3,2)]:
            ss, ii, aa = closed(a,b,h)
            eq(paired(a,b,h,F(1)), ss)
            eq(paired(a,b,h,F(0)), ii)
            eq(paired(a,b,h,F(-1)), aa)
            eq(ii, (ss+aa)/2)
            eq(ss-aa, (a-b)**2*h*h*((a+b)**2*h*h/F(2)-1))
            for theta in [F(-1),F(-1,2),F(1,3),F(1,2),F(1)]:
                eq(paired(a,b,h,theta), (1+theta)*ss/2+(1-theta)*aa/2)
            for x in [(F(1), F(0)), (F(2), F(-3))]:
                for first in [a,b]:
                    for second in [a,b]:
                        eq(normsquared(update(x,first,second,h)),
                           factor(first,second,h)*normsquared(x))

rvals = [F(1,3),F(1,2),F(1),F(11,10),F(3,2),F(2),F(29,10),F(3),F(4)]
for r in rvals:
    P = r**4 - 2*r**3 -2*r*r -2*r +1
    tS = (1+r*r)/(1+r**4)
    tI = 4*r/(1+r*r)**2
    tA = (4*r-1-r*r)/(2*r*r)
    tc = F(2)/(1+r)**2
    eq(tA-tI,-(r-1)**2*P/(2*r*r*(1+r*r)**2))
    eq(tS-tI,(r-1)**2*P/((1+r*r)**2*(1+r**4)))
    eq(tS-tc,-P/((1+r)**2*(1+r**4)))
    eq(tA-tc,-P/(2*r*r*(1+r)**2))
    eq(P/(r*r),(r+1/r)**2-2*(r+1/r)-4)

ss, ii, aa = closed(F(1),F(2),F(3,5))
eq(ss,F(751,625)); eq(ii,F(109,100)); eq(aa,F(1223,1250))
assert ss > ii > 1 > aa
checks += 1
assert F(5,17)<F(8,25)<F(9,25)<F(3,8)
checks += 1
print('PASS: {} independent exact-rational assertions'.format(checks))
