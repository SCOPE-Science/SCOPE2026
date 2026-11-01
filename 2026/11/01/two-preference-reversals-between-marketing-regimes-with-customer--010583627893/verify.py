#!/usr/bin/env python3
"""Reproducible exact algebra and independent numerical checks for two marketing regimes.

Standard library only. The numerical integration supplements an exact proof.
"""
from fractions import Fraction as F
from math import log, exp, sqrt, isclose
import random

A=((40,12),(14,62))
B=((34,4),(30,32))

def mul(U,V):
    return tuple(tuple(sum(U[i][k]*V[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def mob(M,x):
    return (M[0][0]*x+M[0][1])/(M[1][0]*x+M[1][1])

def poly_cross(P,Q):
    (a,b),(c,d)=P
    (u,v),(w,z)=Q
    return (a*w-u*c, a*z+b*w-u*d-v*c,b*z-v*d)

P,Q=mul(B,A),mul(A,B)
assert P==((1416,656),(1648,2344))
assert Q==((1720,544),(2336,2040))
assert poly_cross(P,Q)==(128*3697,-128*3962,128*493)

# Exact sign-change witnesses within the physical adopter interval.
coefs=poly_cross(P,Q)
def numerator(x):
    aa,bb,cc=coefs
    return aa*x*x+bb*x+cc
assert numerator(F(0))>0
assert numerator(F(1,2))<0
assert numerator(F(1))>0
rminus=(1981-2*sqrt(525435))/3697
rplus=(1981+2*sqrt(525435))/3697
assert 0<rminus<F(1,2)<rplus<1
assert abs(float(numerator(rminus)))<1e-7
assert abs(float(numerator(rplus)))<1e-7
assert rminus != rplus

# The projective flow lift is proportional to the two exact matrices.
def lift(p,q,r,T):
    beta=q-p-r
    s=sqrt(beta*beta+4*p*q)
    from math import cosh,sinh
    t=s*T/2
    C=cosh(t)
    S=sinh(t)/s
    return ((C+beta*S,2*p*S),(2*q*S,C-beta*S))
for (p,q,r,T),K in [((6,7,12,log(2)/17),A),((2,15,12,log(2)/11),B)]:
    M=lift(p,q,r,T)
    factor=M[0][0]/K[0][0]
    assert all(isclose(M[i][j],factor*K[i][j],rel_tol=2e-14,abs_tol=2e-14)
               for i in range(2) for j in range(2))
    eq=((q-p-r)+sqrt((q-p-r)**2+4*p*q))/(2*q)
    assert 0<eq<1
    assert isclose(mob(K,eq),eq,rel_tol=1e-13,abs_tol=1e-13)

# Independent fixed-step RK4, not derived from the projective lift.
def integrate(x,p,q,r,T,steps=400):
    h=T/steps
    def field(y): return (p+q*y)*(1-y)-r*y
    for _ in range(steps):
        k1=field(x)
        k2=field(x+h*k1/2)
        k3=field(x+h*k2/2)
        k4=field(x+h*k3)
        x+=h*(k1+2*k2+2*k3+k4)/6
    return x
random.seed(45)
for _ in range(200):
    x=random.random()
    y1=integrate(x,6,7,12,log(2)/17)
    y2=integrate(x,2,15,12,log(2)/11)
    assert abs(y1-mob(A,x))<1e-11
    assert abs(y2-mob(B,x))<1e-11
    assert abs(mob(P,x)-mob(B,mob(A,x)))<2e-15
    assert abs(mob(Q,x)-mob(A,mob(B,x)))<2e-15
    first=integrate(y1,2,15,12,log(2)/11)
    reverse=integrate(y2,6,7,12,log(2)/17)
    assert abs(first-mob(P,x))<1e-11
    assert abs(reverse-mob(Q,x))<1e-11
    diff=mob(P,x)-mob(Q,x)
    assert (diff>0)==(numerator(x)>0)
print('PASS: exact matrices/cross-quadratic, two interior simple roots,')
print('exact stationary equilibria and 200 independent two-period RK4 comparisons.')
