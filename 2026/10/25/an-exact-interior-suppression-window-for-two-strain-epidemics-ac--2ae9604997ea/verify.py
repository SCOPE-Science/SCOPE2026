#!/usr/bin/env python3
"""Independent finite checks of the two-type layer-allocation identities.
The symbolic argument is in RESULT.md. No sampled test proves its universal scope.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
from math import sqrt
import random

checks = 0

def check(value):
    global checks
    assert value
    checks += 1

# Exact polynomial det(I - R[[c(1-t), at], [bt, d(1-t)]])
a = b = c = F(1)
d = F(1, 4)
R = F(11, 10)
# diagonal factors: 1-Rc+Rc t; 1-Rd+Rd t; subtract R^2 ab t^2
coefs = ((1-R*c)*(1-R*d), R*c*(1-R*d)+R*d*(1-R*c), R*R*(c*d-a*b))
check(coefs == (F(-29,400), F(308,400), F(-363,400)))
check(coefs[0] < 0 and sum(coefs) < 0)
check(coefs[0] + coefs[1]*F(1,2) + coefs[2]*F(1,4) > 0)
# Algebraic roots are of shape (14 + k sqrt(109))/33, k=+-1.
# Substitute t=(14+k u)/33, u^2=109, and reduce to A+B u.
for sign in (-1,1):
    u0 = F(14,33)
    u1 = F(sign,33)
    A = coefs[0] + coefs[1]*u0 + coefs[2]*(u0*u0 + F(109)*u1*u1)
    B = coefs[1]*u1 + coefs[2]*(2*u0*u1)
    check(A == 0 and B == 0)
getcontext().prec = 55
r1 = (Decimal(14)-Decimal(109).sqrt())/Decimal(33)
r2 = (Decimal(14)+Decimal(109).sqrt())/Decimal(33)
check(Decimal(0)<r1<Decimal('0.5')<r2<Decimal(1))
check(Decimal(11)*(Decimal(5)+Decimal(73).sqrt())/Decimal(160)<1)
# Derive a high-precision eigenvalue independently via the matrix trace/discriminant.
def rho(tt, aa, bb, cc, dd, rr):
    p=rr*cc*(1-tt); r=rr*dd*(1-tt); off=rr*rr*aa*bb*tt*tt
    return (p+r+sqrt((p-r)**2+4*off))/2
check(abs(rho(0,1,1,1,.25,1.1)-1.1)<1e-12)
check(abs(rho(1,1,1,1,.25,1.1)-1.1)<1e-12)
check(rho(.5,1,1,1,.25,1.1)<1)
for tt in (0.02, float(r1)-1e-5, (float(r1)+float(r2))/2, float(r2)+1e-5, .95):
    expected = (float(r1)<tt<float(r2))
    check((rho(tt,1,1,1,.25,1.1)<1) == expected)

rng = random.Random(923023)
for j in range(1700):
    aa=rng.uniform(.05,1); bb=rng.uniform(.05,1)
    cc=rng.uniform(.05,1); dd=rng.uniform(.05,1)
    s=(cc+dd)/2; h=abs(cc-dd)/2; q=sqrt(aa*bb)
    fun=lambda t: s*(1-t)+sqrt(h*h*(1-t)**2+q*q*t*t)
    if q>s and h>1e-6:
        z=sqrt(q*q-cc*dd)
        L=q*(s*q+h*z)/(q*q+h*h)
        t=(s*L-cc*dd)/(q*q-cc*dd)
        check(0<t<1)
        check(abs(fun(t)-L)<1e-9)
        check(fun(t)<min(fun(0),fun(1)))
        for x in (0,.13,.31,.47,.68,.83,1):
            check(fun(t)<=fun(x)+1e-10)
    else:
        # When h>0 and q<=s, optimal endpoint 1; h nearly zero handled by affine comparison.
        if h>1e-6:
            for x in (0,.15,.4,.6,.81,1):
                check(fun(1)<=fun(x)+1e-11)
    for x in (.13,.29,.51,.76):
        lhs=fun(x)
        rhs=(fun(x-.00001)+fun(x+.00001))/2
        check(lhs<=rhs+1e-9)
    # Formula must match full eigenvalue for a nontrivial matrix.
    tt=rng.uniform(.05,.95)
    check(abs(rho(tt,aa,bb,cc,dd,1)-fun(tt))<1e-12)
print(f'PASSED {checks} finite and exact arithmetic assertions')
