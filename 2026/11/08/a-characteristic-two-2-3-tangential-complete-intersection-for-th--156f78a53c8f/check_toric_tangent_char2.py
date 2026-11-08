#!/usr/bin/env python3
"""Exact, self-contained symbolic and finite-field checks of a toric tangent image.
Only corroborative calculations: the all-characteristic infinite statement uses a proof.
"""
import sympy as S
from itertools import product
A, Ap, B, Bp, C, Cp, Z, x,y,a,b = S.symbols('A Ap B Bp C Cp Z x y a b')
# Numerator-free reciprocal chart: at the torus, x,y invertible.
s,t = 1+a, 1+b
coords = {Z:1, A:s*x, Ap:s/x, B:t*y, Bp:t/y, C:(s+t+1)*x*y, Cp:(s+t+1)/(x*y)}
Q=Z**2+A*Ap+B*Bp+C*Cp
R=A*B*Cp+Ap*Bp*C
for title, poly in [('quadratic',Q),('cubic',R)]:
    value = S.cancel(poly.subs(coords, simultaneous=True))
    num = S.Poly(S.together(value).as_numer_denom()[0], a,b,x,y, modulus=2)
    assert num.is_zero, (title,num)
# Q after elimination by R has nonzero formal A-derivative in char 2:
F= A*Ap+B*Bp+(Ap*Bp*C*C)/(A*B)
dFdA = S.cancel(S.diff(F,A))
assert not S.Poly(S.together(dFdA).as_numer_denom()[0],A,Ap,B,Bp,C,modulus=2).is_zero
# Finite extension GF(4) with element alpha^2=alpha+1.
def mul(a,b):
    aa,bb=a,b; out=0
    while bb:
        if bb&1: out^=aa
        bb >>=1; aa <<=1
        if aa&4: aa ^= 0b111
    return out

def inv(a):
    assert a
    return next(b for b in (1,2,3) if mul(a,b)==1)

def div(a,b): return mul(a,inv(b))
def sq(a): return mul(a,a)

def tangent(x,y,a,b):
    s=1^a; t=1^b; u=s^t^1
    return (1,mul(s,x),div(s,x),mul(t,y),div(t,y),mul(mul(u,x),y),div(u,mul(x,y)))

def equations(p):
    z,A,Ap,B,Bp,C,Cp=p
    q=sq(z)^mul(A,Ap)^mul(B,Bp)^mul(C,Cp)
    r=mul(mul(A,B),Cp)^mul(mul(Ap,Bp),C)
    return q,r
for q in range(4):
    images=set()
    for x,y in product(range(1,4),repeat=2):
        for a,b in product(range(4),repeat=2):
            p=tangent(x,y,a,b)
            assert equations(p)==(0,0)
            images.add(p)
    # On the dense coordinate torus of the affine Z=1 patch, equality in F4.
    target={(1,*p) for p in product(range(1,4), repeat=6) if equations((1,*p))==(0,0)}
    actual={p for p in images if all(p[1:])}
    assert actual==target,(len(actual),len(target),len(target-actual))
    break
# Chern number for J1(H) on degree-six del Pezzo blow-up of P2 at 3 toric points
H2=6; KH=-6; c2X=6
c1J2=4*H2
c2J=c2X+2*KH+3*H2
Segre_degree=c1J2-c2J
assert (c1J2,c2J,Segre_degree)==(24,12,12)
assert Segre_degree//6==2 and Segre_degree%6==0
print('F4_dense_affine_torus_points=',len(target))
print('F4_tangent_image_dense_points=',len(actual))
print('tangent_segre_class_degree=',Segre_degree)
print('complete_intersection_degree=',2*3)
print('generic_tangent_incidence_degree=',Segre_degree//6)
print('ALL_CHECKS_PASSED')
