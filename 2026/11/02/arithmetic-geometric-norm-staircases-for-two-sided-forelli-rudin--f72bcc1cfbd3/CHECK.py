#!/usr/bin/env python3
"""Self-contained checks for the two-sided disk-kernel singular-value theorem."""
import cmath
import math
from fractions import Fraction

CHECKS = 0

def check(x, name=''):
    global CHECKS
    assert x, name
    CHECKS += 1

def sv(n, a, b, c):
    A, B = 2*a+2, 2*b+2
    logsv = (math.lgamma(n+c)-math.lgamma(c)
             +0.5*(math.lgamma(A-1)+math.lgamma(B-1)
                   -math.lgamma(n+A)-math.lgamma(n+B)))
    return math.exp(logsv)

# Coefficient-by-coefficient exact verification of the ratio sign identity.
for A in [Fraction(11,10),Fraction(2),Fraction(5,2),Fraction(4),Fraction(9)]:
    for B in [Fraction(7,5),Fraction(3),Fraction(8),Fraction(11)]:
        for c in [Fraction(1,2),Fraction(2),Fraction(29,10),Fraction(7)]:
            for n in [0,1,2,5,19]:
                lhs = (n+c)**2-(n+A)*(n+B)
                rhs = (2*c-A-B)*n+c*c-A*B
                check(lhs == rhs, 'ratio numerator')

# Gamma simplification and direct exact special family a=0,b=1,c=3.
for n in range(100):
    value=sv(n,0,1,3)
    check(abs(value**2 - (n+2)/(2*(n+3)))<2e-12,'critical asymmetric example')
    check(value < 1/math.sqrt(2),'critical norm nonattainment')
    check(abs(sv(n,0,0,2)-1)<2e-12,'critical symmetric projection')

# In the compact asymmetric example c=2.9 the unique maximizing order is 3.
vals=[sv(n,0,1,2.9) for n in range(150)]
check(max(range(150), key=vals.__getitem__)==3,'finite norm staircase')
check(all(vals[i] > vals[i+1] for i in range(3,149)),'postmaximum decay')
check(vals[0]<vals[1]<vals[2]<vals[3],'premmaximum growth')

# Exact finite-difference positivity of staircase thresholds c_n.
for A,B in [(2.,4.),(1.3,8.),(1.1,1.5),(4.,10.)]:
    thresholds=[math.sqrt((n+A)*(n+B))-n for n in range(300)]
    check(all(x<y for x,y in zip(thresholds,thresholds[1:])), 'strict staircase')
    check(thresholds[-1]<(A+B)/2,'critical accumulation from below')

# Independent polar midpoint quadrature of the integral kernel on input
# f(w)=w^n(1-|w|^2)^b; the predicted output is one analytic monomial.
a,b,c = 0.25,0.5,2.4
z = 0.25+0.10j
nx,nt=400,180
for n in range(4):
    accum=0j
    for k in range(nx):
        x=(k+0.5)/nx
        r=math.sqrt(x)
        rad=(1-x)**(2*b)
        for l in range(nt):
            theta=2*math.pi*(l+0.5)/nt
            w=r*cmath.exp(1j*theta)
            accum += (w**n)*rad/(1-z*w.conjugate())**c
    value = (1-abs(z)**2)**a * accum/(nx*nt)
    coeff=math.gamma(n+c)/(math.gamma(c)*math.gamma(n+1))
    beta=math.gamma(n+1)*math.gamma(2*b+1)/math.gamma(n+2*b+2)
    expected=(1-abs(z)**2)**a*coeff*beta*(z**n)
    check(abs(value-expected)<2e-5, 'polar integration')

# The ordering rule follows from the exact ratio and its unique sign crossing.
for c in [2.50,math.sqrt(8),2.85,2.90,2.93,2.99]:
    A,B=2.,4.
    vals=[sv(n,0,1,c) for n in range(600)]
    predicted = 0 if c < math.sqrt(A*B) else (
        math.ceil((c*c-A*B)/(A+B-2*c)) if c<3 else 599)
    # At exact arithmetic transition c=sqrt(AB), modes 0 and 1 tie.
    if c < math.sqrt(A*B):
        check(vals[0] == max(vals),'base mode')
    elif c == math.sqrt(A*B):
        check(abs(vals[0]-vals[1])<1e-12,'double extremizer')
    else:
        check(predicted==max(range(600),key=vals.__getitem__),'staircase index')

print('CHECK_OK',CHECKS)
