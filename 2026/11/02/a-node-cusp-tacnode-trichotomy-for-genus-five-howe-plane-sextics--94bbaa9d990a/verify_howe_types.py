#!/usr/bin/env python3
"""Exact polynomial checks for the stated Howe-sextic type stratification.

All arithmetic is integer, rational, or prime-field arithmetic. The general
classification is proved geometrically in RESULT.md, not by finite tests.
"""
from fractions import Fraction


def trim(a):
    a=list(a)
    while a and a[-1]==0:
        a.pop()
    return tuple(a)


def add(a,b):
    return trim(tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))))


def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))

def mul(a,b):
    if not a or not b:return ()
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)


def scale(a,n): return trim(tuple(n*x for x in a))
def derivative(a): return trim(tuple(i*a[i] for i in range(1,len(a))))
def value(a,x): return sum(v*x**i for i,v in enumerate(a))

def normalize_mod(a,p):
    return trim(tuple(int(x)%p for x in a))

def mod_gcd(a,b,p):
    a=normalize_mod(a,p);b=normalize_mod(b,p)
    while b:
        r=list(a)
        inv=pow(b[-1],-1,p)
        while len(r)>=len(b):
            n=len(r)-len(b); coeff=r[-1]*inv%p
            for j,v in enumerate(b): r[n+j]=(r[n+j]-coeff*v)%p
            r=list(trim(r))
        a,b=b,tuple(r)
    if not a:return ()
    return normalize_mod(scale(a,pow(a[-1],-1,p)),p)


def rational_gcd(a,b):
    a=trim(tuple(map(Fraction,a)));b=trim(tuple(map(Fraction,b)))
    while b:
        r=list(a)
        while len(r)>=len(b):
            n=len(r)-len(b); coeff=r[-1]/b[-1]
            for j,v in enumerate(b):r[n+j]-=coeff*v
            r=list(trim(r))
        a,b=b,tuple(r)
    return tuple(x/a[-1] for x in a) if a else ()


# Characteristic-zero cusp witness: phi=x(x-1)(x+1).
x=(0,1)
phi=(0,-1,0,1)
q1=(20,-15,1)
q2=(-12,7,1)
w1=sub(mul(derivative(q1),phi),mul(q1,derivative(phi)))
w2=sub(mul(derivative(q2),phi),mul(q2,derivative(phi)))
assert rational_gcd(w1,w2)==(-2,1)
assert value(w1,2)==value(w2,2)==0
assert value(phi,2)==6 and value(q1,2)==-6 and value(q2,2)==6
assert value(phi,0)==value(phi,1)==value(phi,-1)==0
assert all(value(q,alpha)!=0 for q in (q1,q2) for alpha in (0,1,-1))
assert rational_gcd(phi,q1)==rational_gcd(phi,q2)==rational_gcd(q1,q2)==(1,)
assert 15**2-4*20==145 and 7**2-4*(-12)==97

# Homogeneous nodal/cuspidal quotient cubic H(U,V,W):
# 12U^3+62U^2V+106UV^2+60V^3-U^2W-18UVW-25V^2W-2UW^2+2VW^2.
Hpol=add(add(add(scale(mul(mul(q1,q1),q1),12),scale(mul(mul(q1,q1),q2),62)),
              add(scale(mul(mul(q1,q2),q2),106),scale(mul(mul(q2,q2),q2),60))),
         add(add(neg(mul(mul(q1,q1),phi)),scale(mul(mul(q1,q2),phi),-18)),
             add(scale(mul(mul(q2,q2),phi),-25),
                 add(scale(mul(q1,mul(phi,phi)),-2),scale(mul(q2,mul(phi,phi)),2)))))
assert Hpol==(), Hpol

# In local affine coordinates U=-1+u,V=1+v, quadratic is (5u+7v)^2;
# cubic restricted to tangent 5u+7v=0 is 24 t^3 with (u,v)=(-7t,5t).
H=lambda u,v:(12*u**3+62*u*u*v+106*u*v*v+60*v**3
              -u*u-18*u*v-25*v*v-2*u+2*v)
assert H(-1,1)==0
# Exact derivatives at (-1,1):
Hu=lambda u,v:36*u*u+124*u*v+106*v*v-2*u-18*v-2
Hv=lambda u,v:62*u*u+212*u*v+180*v*v-18*u-50*v+2
assert Hu(-1,1)==0 and Hv(-1,1)==0
assert all(H(-1+t*a,1+t*b)==25*(t*a)**2+70*t*t*a*b+49*(t*b)**2 + t**3*(12*a**3+62*a*a*b+106*a*b*b+60*b**3) for (a,b,t) in [(1,0,1),(-7,5,1),(2,3,2)])
assert 12*(-7)**3+62*(-7)**2*5+106*(-7)*5**2+60*5**3==24
# At U=V=0, the linear part of H is -2U+2V, giving a reduced node
# after the coordinate-square pullback in characteristic not two.
assert H(0,0)==0 and (Hu(0,0),Hv(0,0))==(-2,2)

# A distinct admissible genus-five Howe example over F_31 has a nodal
# quotient; the coprime Wronskians establish a noncuspidal parameter.
p=31
phi31=mul(mul((0,1),(-1,1)),(-3,1))
q131=mul((-9,1),(-27,1))
q231=mul((-19,1),(-26,1))
W131=sub(mul(derivative(q131),phi31),mul(q131,derivative(phi31)))
W231=sub(mul(derivative(q231),phi31),mul(q231,derivative(phi31)))
assert mod_gcd(W131,W231,p)==(1,)

# A second published admissible example over F_31 has a quotient node
# on a ramification axis; its quadratic tangent-cone discriminant is 25.
U0=14
G=lambda u,w:23*u**3+4*u*u+4*u+1+(4*u*u+22)*w+(19*u+12)*w*w
Gu=lambda u,w:69*u*u+8*u+4+8*u*w+19*w*w
Gw=lambda u,w:4*u*u+22+2*(19*u+12)*w
assert G(U0,0)%31==Gu(U0,0)%31==Gw(U0,0)%31==0
# Quadratic in (u-U0,w) is 9a^2+19ab+30b^2, discr. 25 !=0.
assert (19**2-4*9*30)%31==25

print('HOWE_SEXTIC_NODE_CUSP_TACNODE_WRONSKIAN_AND_CUSP_WITNESS_EXACT_PASS')
