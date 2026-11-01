#!/usr/bin/env python3
"""Independent algebraic and numerical checks of a spherical brightness pushforward."""
from fractions import Fraction
from math import pi, log, asin, sqrt
import math
import random
from sympy import symbols, expand, Poly, Rational, rf, factor, simplify
from scipy.integrate import quad
from scipy.optimize import brentq

x,y,z=symbols('x y z')
Q=x*y+y*z+z*x-x*y*z

def dirichlet_expectation(poly):
    out=0
    for powers,c in Poly(expand(poly),x,y,z).terms():
        i,j,k=powers
        out+=c*rf(Rational(1,2),i)*rf(Rational(1,2),j)*rf(Rational(1,2),k)/rf(Rational(3,2),i+j+k)
    return factor(out)

assert dirichlet_expectation(Q)==Rational(4,21)
assert dirichlet_expectation(Q**2)==Rational(128,3003)
assert factor(dirichlet_expectation(Q**2)-dirichlet_expectation(Q)**2)==Rational(400,63063)

s=symbols('s', real=True)
A=s**2*(1-s**2)
B=(1-s**2)**3/4
T=(1-s**2)*(1+s**2)**2/4
assert simplify(A+B-T)==0
assert simplify(T.subs(s,1/sqrt(3))-Rational(8,27))==0
assert simplify(T.subs(s,0)-Rational(1,4))==0
assert simplify(A.subs(s,1/sqrt(2))-Rational(1,4))==0
assert simplify(simplify(T.diff(s,2).subs(s,0))/2-Rational(1,4))==0
# At an equatorial saddle near azimuth pi/4, quadratic Taylor = s²/4 - alpha².
# Six axis minima, twelve saddles, eight diagonal maxima yield endpoint slopes 3/2,9/2 and log residue 6/pi.

Afloat=lambda t:t*t*(1-t*t)
Tfloat=lambda t:(1-t*t)*(1+t*t)**2/4
Bfloat=lambda t:(1-t*t)**3/4

def density(v):
    assert 0<v<8/27 and abs(v-.25)>1e-12
    ends=[0.,1.,1/sqrt(2),1/sqrt(3)]
    grid=[i/300 for i in range(301)]
    for func in (Afloat,Tfloat):
        for a,b in zip(grid[:-1],grid[1:]):
            if (func(a)-v)*(func(b)-v)<0:
                ends.append(brentq(lambda r:func(r)-v,a,b))
    ends=sorted(set(round(t,14) for t in ends))
    result=0.
    for a,b in zip(ends[:-1],ends[1:]):
        mid=(a+b)/2
        if not (Afloat(mid)<v<Tfloat(mid)):continue
        def g(t):
            aa=Afloat(t);tt=Tfloat(t)
            if aa>=v or v>=tt:return 0.
            return 1/(pi*sqrt((v-aa)*(tt-v)))
        result+=quad(g,a,b,epsabs=2e-7,limit=200)[0]
    return result

fleft=density(.25-1e-4);fleft2=density(.25-1e-5)
fright=density(.25+1e-4);fright2=density(.25+1e-5)
pred=(6/pi)*log(10)
assert abs((fleft2-fleft)-pred)<.03,(fleft2-fleft,pred)
assert abs((fright2-fright)-pred)<.03,(fright2-fright,pred)
assert abs(density(1e-3)-1.5)<.05
assert abs(density(8/27-1e-3)-4.5)<.06

# The conditional beta-half law matches direct spherical samples in several bins.
rng=random.Random(431)
N=100000
counts=[0]*4
thresholds=[.04,.17,.24,.285]
for _ in range(N):
    zz=2*rng.random()-1
    phi=2*pi*rng.random()
    xx=(1-zz*zz)*math.cos(phi)**2
    yy=(1-zz*zz)*math.sin(phi)**2
    val=(1-xx)*(1-yy)*(1-zz*zz)
    for i,cutoff in enumerate(thresholds):
        if val<=cutoff:counts[i]+=1

def G(v):
    if v<=0:return 0.
    if v>=1:return 1.
    return 2/pi*asin(sqrt(v))
def cdf(t):
    return quad(lambda a:G((t-Afloat(a))/Bfloat(a)),0,1,epsabs=1e-8,limit=350)[0]
for cutoff,count in zip(thresholds,counts):
    assert abs(count/N-cdf(cutoff))<.012,(cutoff,count/N,cdf(cutoff))
print('VERIFY_OK: Dirichlet moments, conditional decomposition, saddle coefficient, endpoints and Haar sampling.')
print('mean=4/21, second moment=128/3003, variance=400/63063, saddle coefficient=6/pi')
