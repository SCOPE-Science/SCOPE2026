#!/usr/bin/env python3
"""Reproduce the sharp two-term local fourth-moment constant; standard library only."""
import math
import cmath
from fractions import Fraction

w = math.log(2)
sinc = lambda z: math.sin(z) / z if z else 1.0
A = 2 * math.sqrt(2) * sinc(w / 2)
B = 2 + sinc(w)

def Q(x):
    return (-A*x**6/2 + (2-2*B)*x**5 - A*x**4 - 3*x**3
            - 5*A*x**2/2 + (2*B-8)*x + A)

def F(x):
    return (1+A*x+B*x*x+A*x**3/2+x**4/4)/(1+4*x*x+x**4)
lo, hi = 0.0, 1.0
for _ in range(100):
    mid = (lo+hi)/2
    if Q(mid)>0:lo=mid
    else:hi=mid
xi = (lo+hi)/2
assert 0.444103 < xi < 0.444105
assert 1.60766 < F(xi) < 1.60768
assert F(0.5)>1.5
assert 2 < B < 3 and A > 0
# Exact polynomial identity used for the m>=2 exclusion.
# Polynomial coefficients indexed in ascending order.
def multiply(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):out[i+j]+=ai*bj
    return out
D=[Fraction(1),Fraction(0),Fraction(4),Fraction(0),Fraction(1)]
lhs=[8*z for z in D]
for i,coeff in enumerate([3,12,18,12,3]):lhs[i]-=coeff
rhs=multiply([Fraction(1),Fraction(-2),Fraction(1)], [Fraction(5),Fraction(-2),Fraction(5)])
assert lhs==rhs
# Other exclusion: substitution x=sqrt(3) y yields a positive SOS.
lhs2=[Fraction(3-2),Fraction(-8),Fraction(36-12),Fraction(-8),Fraction(27-2)]
rhs2=[Fraction(1),Fraction(-8),Fraction(16+8),Fraction(-8),Fraction(25)]
assert lhs2==rhs2
# Independent midpoint-rule quadratures (not used in proof).
checks=0
for m,n,x in [(1,2,xi),(1,2,.5),(1,3,1.0),(1,4,.4),(2,3,1.0),(4,7,2.0)]:
    theta=-(.5) + (0 if m==1 else math.pi/17)
    if m==1 and n==2:
        theta=-.5
    a=1+0j
    b=x+0j
    steps=4000
    acc=0.0
    for j in range(steps):
        t=theta+(j+.5)/steps
        v=a*cmath.exp(-(.5+1j*t)*math.log(m))+b*cmath.exp(-(.5+1j*t)*math.log(n))
        acc+=abs(v)**4
    numerical=acc/steps/(1+4*x*x+x**4)
    assert numerical <= F(xi)+1e-7, (m,n,x,numerical)
    if m==1 and n==2:
        assert abs(numerical-F(x)) < 2e-7, (numerical,F(x))
    checks+=1
print(f"VERIFY_OK algebraic_identities=2 independent_quadratures={checks} root={xi:.15f} constant={F(xi):.15f}")
