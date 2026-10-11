#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt, sqrt, atan, pi
import sympy as sp

# Exact symbolic derivative identity.  Put x=t/sqrt(1+t^2),
# m=pi+t-atan(t), q^2=m^2-4s, s=1+sqrt(1+t^2).
m,q,x=sp.symbols('m q x', real=True)
s=(m*m-q*q)/4
Aprime=3*m*m*x*x-6*(x*x*s+m*x)+8
Bprime=3*q*(m*x*x-2*x)
assert sp.expand(Aprime+Bprime-(2+sp.Rational(3,2)*(x*(m+q)-2)**2))==0
assert sp.expand(Aprime-Bprime-(2+sp.Rational(3,2)*(x*(m-q)-2)**2))==0

# Exact rational interval arithmetic for four sign certificates.
def I(a,b=None):
    return (Fraction(a), Fraction(a if b is None else b))
def add(a,b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[1],-a[0])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    vals=[a[i]*b[j] for i in (0,1) for j in (0,1)]
    return (min(vals),max(vals))
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def sq(a):
    if a[0]>=0: return (a[0]*a[0],a[1]*a[1])
    if a[1]<=0: return (a[1]*a[1],a[0]*a[0])
    return (Fraction(0),max(a[0]*a[0],a[1]*a[1]))
def cube(a): return mul(sq(a),a)
def sqrt_frac_interval(y,D=10**12):
    assert y>=0
    if y==0: return (Fraction(0),Fraction(0))
    n=(y.numerator*D*D)//y.denominator
    r=isqrt(n)
    lo=Fraction(r,D); hi=Fraction(r+1,D)
    assert lo*lo<=y<hi*hi
    return lo,hi
def sqrtI(a,D=10**12):
    assert a[0]>=0
    lo=sqrt_frac_interval(a[0],D)[0]
    hi=sqrt_frac_interval(a[1],D)[1]
    return lo,hi

PI=(Fraction(333,106),Fraction(355,113))
SQ2=(Fraction(1414213,10**6),Fraction(1414214,10**6))
SQ3=(Fraction(1732050,10**6),Fraction(1732051,10**6))
SQ5=(Fraction(2236067,10**6),Fraction(2236068,10**6))

def psi_interval(t,r,alpha,which):
    # m=pi+t-alpha, s=1+r, q=sqrt(m^2-4s)
    mm=add(add(PI,t),neg(alpha))
    ss=add(I(1),r)
    qq=sqrtI(sub(sq(mm),mul(I(4),ss)))
    A=add(sub(cube(mm),mul(I(6),mul(mm,ss))),mul(I(8),t))
    B=cube(qq)
    return add(A,B) if which=='+' else sub(A,B)

# Type-2 transition: Psi_+(1)<0<Psi_+(sqrt(3)).
p1=psi_interval(I(1),SQ2,div(PI,I(4)),'+')
p2=psi_interval(SQ3,I(2),div(PI,I(3)),'+')
assert p1[1]<0 and p2[0]>0

# Type-1 transition: use tan(2pi/5)=sqrt(5+2sqrt(5)) and
# tan(5pi/12)=2+sqrt(3), both giving algebraic secants.
tan72=sqrtI(add(I(5),mul(I(2),SQ5)))
sec72=add(I(1),SQ5)
p3=psi_interval(tan72,sec72,div(mul(I(2),PI),I(5)),'-')
sq6=mul(SQ2,SQ3)
tan75=add(I(2),SQ3)
sec75=add(sq6,SQ2)
p4=psi_interval(tan75,sec75,div(mul(I(5),PI),I(12)),'-')
assert p3[1]<0 and p4[0]>0

# Supplemental numerical bisection.  These decimals are not used in the proof.
def psi_float(t,which):
    r=sqrt(1+t*t)
    mm=pi+t-atan(t)
    ss=1+r
    qq=sqrt(mm*mm-4*ss)
    A=mm**3-6*mm*ss+8*t
    return A+(qq**3 if which=='+' else -qq**3)
def bisect(a,b,which):
    fa=psi_float(a,which); fb=psi_float(b,which)
    assert fa<0<fb
    for _ in range(100):
        c=(a+b)/2
        fc=psi_float(c,which)
        if fc<0: a=c
        else: b=c
    return (a+b)/2
h2=bisect(1.0,sqrt(3.0),'+')
h1=bisect(sqrt(5+2*sqrt(5)),2+sqrt(3),'-')

print('VERIFY_OK')
print('Psi_plus(1) upper <',float(p1[1]))
print('Psi_plus(sqrt(3)) lower >',float(p2[0]))
print('Psi_minus(tan(2pi/5)) upper <',float(p3[1]))
print('Psi_minus(tan(5pi/12)) lower >',float(p4[0]))
print('h_Type2 = %.15f' % h2)
print('h_Type1 = %.15f' % h1)
