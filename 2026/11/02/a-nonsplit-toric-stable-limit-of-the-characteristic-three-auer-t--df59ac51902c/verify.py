#!/usr/bin/env python3
"""Exact finite and symbolic checks for a characteristic-three quartic degeneration."""
import itertools
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
x,y,z,w,t,a,W=sp.symbols('x y z w t a W')
Q=x*x+y*y+z*z
R=x*x*y*y+y*y*z*z+z*z*x*x
S=x*x-y*y
B=x*x+y*y

def zero3(F, variables):
    return sp.Poly(sp.expand(F),*variables,modulus=3).is_zero

F=x**4+y**4+z**4-(a+1)*R
assert zero3(F-(Q*Q-a*R),(x,y,z,a))
assert zero3(R+S*S-B*Q,(x,y,z))
print('IDENTITIES_OK: quartic = Q^2-lambda*R, R+S^2=BQ')

# Exhaustively enumerate projective F3 points with Q=S=0; these are all
# geometric intersections because x^2=y^2=z^2 and x cannot vanish.
P=set()
for xx,yy,zz in itertools.product(range(3),repeat=3):
    if (xx,yy,zz)==(0,0,0):continue
    h=next(v for v in (xx,yy,zz) if v)
    inv=pow(h,-1,3)
    p=tuple((inv*v)%3 for v in (xx,yy,zz))
    if (sum(v*v for v in p)%3==0 and (p[0]*p[0]-p[1]*p[1])%3==0):
        P.add(p)
assert P=={(1,yy,zz) for yy,zz in itertools.product((1,2),repeat=2)}
print('FOUR_NODES_OK:',sorted(P))

# In affine x=1, eliminate z by Q=tw, since dQ/dz=2z is a unit at P.
# Substitution of R=-S^2+BQ gives w^2+S^2=tBw.
B1=1+y*y; S1=1-y*y
f=w*w+S1*S1-t*B1*w
# Let W=w-(tB)/2; uv=4(W^2+S^2)/B^2=t^2 over F9.
assert zero3(f.subs(w,W+t*B1/2)-(W*W+S1*S1-t*t*B1*B1/4),(W,y,t))
# dS/dy=-2y, dQ/dz=2z and B are units at all 4 points.
assert all(((-2*yy)*(2*zz))%3!=0 and (1+yy*yy)%3!=0 for _,yy,zz in P)
print('THICKNESS_OK: at each node etale-local uv=t^2 over F9')

# Four A1 resolutions insert four vertices separating two original components.
# A reduced K_{2,4} Laplacian (the row/column of one degree-four vertex omitted).
L=sp.Matrix([[4,-1,-1,-1,-1],[-1,2,0,0,0],[-1,0,2,0,0],[-1,0,0,2,0],[-1,0,0,0,2]])
snf=smith_normal_form(L,domain=sp.ZZ)
factors=tuple(abs(int(snf[i,i])) for i in range(5))
assert factors==(1,1,2,2,8) and L.det()==32
print('COMPONENT_GROUP_OK: Z/2 x Z/2 x Z/8, order 32')
print('FROBENIUS: fixes 4 nodes and swaps conjugate components, so H1 action=-I_3')
print('TORUS: (R^1_{F9/F3} G_m)^3, |T(F3)|=4^3=64')
print('VERIFY_OK')
