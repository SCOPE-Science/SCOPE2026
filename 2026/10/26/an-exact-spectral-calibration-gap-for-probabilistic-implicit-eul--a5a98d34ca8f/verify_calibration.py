#!/usr/bin/env python3
"""Reproduce the constrained two-mode implicit-Euler calibration frontier."""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import cosh, exp, log, sqrt
getcontext().prec=65
checks=0

def tick(cond, what='check'):
    global checks
    if not cond:
        raise AssertionError(what)
    checks+=1

def parameters(rate, N):
    """Exact rational data for terminal time T=1, h=1/N."""
    h=Fraction(1,N)
    rate=Fraction(rate,1)
    q=1/(1+rate*h)
    q2=1/(1+rate*h/2)
    E=q**N-q2**(2*N)
    a=h**3*q**2*(1-q**(2*N))/(1-q**2)
    r=E*E/a
    return q,E,a,r

for N in range(1,65):
    for rate in (1,2,4,10):
        q,E,a,r=parameters(rate,N)
        tick(E>0 and a>0 and r>0,'positivity')
        h=Fraction(1,N)
        vv=Fraction(0)
        for k in range(N):
            vv=q*q*(vv+h**3)
        tick(vv==a,'exact covariance recursion')
        tick(a==h*h*(1-q**(2*N))/(2*rate+rate*rate*h),'geometric simplification')
        if N<=12:
            # deterministic two timescale refinements verify equivalent recurrences.
            x=Fraction(1)
            for _ in range(N): x=q*x
            tick(x==q**N,'mean recurrence')

def D(s,r):
    return 0.5*log(cosh(0.5*log(s/r)))
for N in (1,2,3,4,8,16,32,64):
    r1=float(parameters(1,N)[3]);r2=float(parameters(10,N)[3])
    s=sqrt(r1*r2)
    value=D(s,r1)+D(s,r2)
    formula=log(cosh(0.25*log(r1/r2)))
    tick(abs(value-formula)<1e-12,'Bhattacharyya exact objective')
    for z in (0.01,0.1,0.4,1,4,10,100):
        tick(D(s*z,r1)+D(s*z,r2)>=value-1e-12,'minimum global')

D1=Decimal(1);D10=Decimal(10);T=Decimal(1)
rf=lambda ell:ell**5*T*T/(Decimal(8)*((Decimal(2)*ell*T).exp()-1))
r1=rf(D1);r10=rf(D10)
s=(r1*r10).sqrt()
x=((r1/r10).ln()/Decimal(4))
gap=((x.exp()+(-x).exp())/2).ln()
tick(gap>1,'strict example gap')
# Check convergence of rational terminal scales and gaps to closed asymptotics.
for N in (64,128,256):
    h=Decimal(1)/N
    def asympcalc(ell):
        q=Decimal(1)/(1+ell*h)
        qhalf=Decimal(1)/(1+ell*h/2)
        E=q**N-qhalf**(2*N)
        a=h*h*(1-q**(2*N))/(2*ell+ell*ell*h)
        return (E*E/a)
    rr1=asympcalc(D1);rr10=asympcalc(D10)
    tick(rr1>0 and rr10>0)
    tick(abs(rr1-r1)<(Decimal(50)/N))
    tick(abs(rr10-r10)<(Decimal(50)/N))
# Unique positive critical point for r(lambda,T), by monotonicity of derivative function.
def F(x):return Decimal(5)*(1-(-Decimal(2)*x).exp())-Decimal(2)*x
lo=Decimal(1);hi=Decimal(4)
for _ in range(250):
    mid=(lo+hi)/2
    if F(mid)>0:lo=mid
    else:hi=mid
peak=(lo+hi)/2
tick(Decimal('2.4825')<peak<Decimal('2.4826'),'peak interval')
# At each subcritical x the identical calibration coefficient recurs on the upper branch.
for val in (Decimal('0.5'),Decimal('1'),Decimal('2')):
    target=rf(val)
    lo=peak;hi=Decimal(30)
    for _ in range(250):
        mid=(lo+hi)/2
        if rf(mid)>target:lo=mid
        else:hi=mid
    twin=(lo+hi)/2
    tick(twin>peak and abs(rf(twin)/target-1)<Decimal('1e-50'),'matched partner')
print('VERIFY_OK',checks)
print('critical_lambdaT=',str(peak))
print('asymptotic_r_1=',str(r1))
print('asymptotic_r_10=',str(r10))
print('asymptotic_sigma_squared=',str(s))
print('minimum_terminal_Bhattacharyya=',str(gap))
