#!/usr/bin/env python3
# Exact replay for the length-six polyphase base-energy certificate.
# Standard library only.

from fractions import Fraction

GRID=(-2,-1,0,1,2)

def A(u,v): return (1-u*u)*(1-v*v)+4*u*v

def D(u,v): return (1+u*u)**2*(1+v*v)**2

def z(u,v):
    z1=(u*u*v*v-3*u*u+4*u*v-3*v*v+5, 4*(u+v))
    z2=(-3*u*u*v*v+5*u*u-4*u*v+v*v-3, 4*u*(u*v-1))
    z3=(-3*u*u*v*v+u*u-4*u*v+5*v*v-3, 4*v*(u*v-1))
    z4=(5*u*u*v*v-3*u*u+4*u*v-3*v*v+1, -4*u*v*(u+v))
    return z1,z2,z3,z4

def dot(x,y): return x[0]*y[0]+x[1]*y[1]
def norm2(x): return dot(x,x)

def corner_numerators(u,v):
    # These are 2D*p_i after tangent-half-angle substitution.
    z1,z2,z3,z4=z(u,v)
    return tuple(norm2(w) for w in (z1,z2,z3,z4))

def direct_corner_numerators(u,v):
    # Expanded 2D*p_i polynomials, kept independently from z().
    p1=u**4*v**4-6*u**4*v**2+9*u**4+8*u**3*v**3-24*u**3*v-6*u**2*v**4+44*u**2*v**2-14*u**2-24*u*v**3+72*u*v+9*v**4-14*v**2+25
    p2=9*u**4*v**4-14*u**4*v**2+25*u**4+24*u**3*v**3-72*u**3*v-6*u**2*v**4+44*u**2*v**2-14*u**2-8*u*v**3+24*u*v+v**4-6*v**2+9
    p3=9*u**4*v**4-6*u**4*v**2+u**4+24*u**3*v**3-8*u**3*v-14*u**2*v**4+44*u**2*v**2-6*u**2-72*u*v**3+24*u*v+25*v**4-14*v**2+9
    p4=25*u**4*v**4-14*u**4*v**2+9*u**4+72*u**3*v**3-24*u**3*v-14*u**2*v**4+44*u**2*v**2-6*u**2-24*u*v**3+8*u*v+9*v**4-6*v**2+1
    return p1,p2,p3,p4

# Each difference below has degree at most 4 in u and at most 4 in v.
# Exact vanishing on a 5x5 Cartesian grid therefore certifies the identity.
for u in GRID:
    for v in GRID:
        assert corner_numerators(u,v)==direct_corner_numerators(u,v)
        z1,z2,z3,z4=z(u,v)
        # B=A/((1+u^2)(1+v^2)), so D*B=(1+u^2)(1+v^2)*A.
        DB=(1+u*u)*(1+v*v)*A(u,v)
        assert dot(z1,z4)-dot(z2,z3)==-4*DB

# Exact arithmetic in Z[zeta]/(zeta^2-zeta+1).
# Pair (a,b) represents a+b*zeta.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c+b*d)  # zeta^2=zeta-1

def conj(x):
    a,b=x
    return (a+b,-b)  # conjugate(zeta)=1-zeta

def n2(x):
    y=mul(x,conj(x))
    assert y[1]==0
    return y[0]

ONE=(1,0); Z=(0,1)
a=[ONE,ONE,Z,neg(ONE),ONE,neg(Z)]
ener=0
for k in range(1,6):
    c=(0,0)
    for j in range(0,6-k):
        c=add(c,mul(a[j+k],conj(a[j])))
    assert n2(c)==1
    ener+=n2(c)
assert ener==5
print('VERIFY_OK corner_sos=4 dot_identity=exact witness_energy=5')
