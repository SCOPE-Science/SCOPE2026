#!/usr/bin/env python3
"""Exact-rational finite witness for the vaccinated-fomite sharp extinction law.

This checks one admissible parameter point, not the general dynamical proof.
"""
from fractions import Fraction as F

zero = F(0)
one = F(1)


def dot(x, y):
    return sum((a*b for a,b in zip(x,y)), zero)


def mul2(A,v):
    return [dot(row,v) for row in A]


def mul3(A,v):
    return [dot(row,v) for row in A]


def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


def solve2(A, b):
    d = det2(A)
    assert d != 0
    return [(b[0]*A[1][1]-A[0][1]*b[1])/d,
            (A[0][0]*b[1]-A[1][0]*b[0])/d]


Lam=F(7,2); mu=xi=gam=d=sigma=eta=kappa=phi=omega=one
p=F(1,2); beta1=F(3,2); beta2=F(1,2); alpha1=one; alpha2=F(1,2)
a=xi+mu
b=gam+d+mu
D=mu*(eta+mu)+sigma*(mu+p*eta)
S0=Lam*(eta+mu)/D
V0=Lam*sigma/D
assert (S0,V0)==(F(2),one)
h=phi/(kappa*omega)
H=alpha1*S0+alpha2*V0
B=beta1*S0+beta2*V0
Rc=xi*(B+h*H)/(a*b)
Jc=(Lam/mu)*(xi/(a*b))*(beta1+alpha1*h)
assert Rc==one and Jc==F(35,24)>one
A=[[-(sigma+mu),(one-p)*eta],[sigma,-(eta+mu)]]
assert det2(A)>zero
q=[beta1+alpha1*h,beta2+alpha2*h]
T=solve2(A,[S0*q[0],V0*q[1]])
assert T==[F(-3),F(-2)]
assert mul2(A,T)==[S0*q[0],V0*q[1]]
B0=[[-a,B,H/kappa],[xi,-b,zero],[zero,phi,-omega]]
r=[b/xi,one,phi/omega]
ell=[one,a/xi,H/(kappa*omega)]
assert mul3(B0,r)==[zero]*3
assert [dot(ell,[B0[i][j] for i in range(3)]) for j in range(3)]==[zero]*3
P=dot(ell,r)
K=(-dot(q,T)+H*h*h)/P
assert P==F(15,2) and K==F(8,5)
assert K>zero
# Independent expansion of the nonlinear Perron mass derivative along
# the true critical *tangent* (not a claim that the tangent is invariant).
# For small epsilon, S=S0+T0*epsilon, V=V0+T1*epsilon,
# I=epsilon and C=(phi/omega)*epsilon.
# The coefficient of epsilon^2 is the sum of the direct-incidence
# demographic-tangent term and the two environmental terms:
#   (beta*T)*I + (alpha*T)*g(C) - H*g'' term.
quadratic=beta1*T[0]+beta2*T[1] + h*(alpha1*T[0]+alpha2*T[1])-H*h*h
assert quadratic==F(-12)
assert quadratic == -K*P
assert [v/K for v in r]==[F(15,8),F(5,8),F(5,8)]
assert [v/K for v in T]==[F(-15,8),F(-5,4)]
print('PASS: exact rational DFE, thresholds, nullvectors, tangent, curvature, and profile')
