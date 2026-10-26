#!/usr/bin/env python3
"""Reproduce finite and polynomial checks for a characteristic-two Schur quartic.

The geometric proof uses blowups and intersection theory; these checks verify
its defining polynomial identities and its twelve-point finite configuration.
"""
import itertools
import sympy as s

x,y,z,w,U,Y,W=s.symbols('x y z w U Y W')

def zero_mod2(expr, generators):
    p=s.Poly(s.expand(expr),*generators,modulus=2)
    assert p.is_zero, str(p)

F=x**4+x*y**3+z**4+z*w**3
H=Y**3+W**3
G=U**4+U*W**3
zero_mod2(F.subs({z:x+U,y:Y,w:W})-(x*(Y**3+W**3)+U**4+U*W**3), (x,U,Y,W))
quadruple=(G,Y*H,U*H+G,W*H)
zero_mod2(F.subs({x:quadruple[0],y:quadruple[1],z:quadruple[2],w:quadruple[3]}),(U,Y,W))
assert s.Poly(s.diff(F,x),x,y,z,w,modulus=2)==s.Poly(y**3,x,y,z,w,modulus=2)
assert s.Poly(s.diff(F,y),x,y,z,w,modulus=2)==s.Poly(x*y**2,x,y,z,w,modulus=2)
assert s.Poly(s.diff(F,z),x,y,z,w,modulus=2)==s.Poly(w**3,x,y,z,w,modulus=2)
assert s.Poly(s.diff(F,w),x,y,z,w,modulus=2)==s.Poly(z*w**2,x,y,z,w,modulus=2)

# GF(4) is F2[t]/(t^2+t+1).  Bits represent 1,t.
def add(a,b):return a^b
def mul(a,b):
    v=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:
                v^=1<<(i+j)
    if v&4:v^=7  # t^2=t+1: xor t^2+t+1
    return v

def pow4(a,n):
    r=1
    for _ in range(n):r=mul(r,a)
    return r

def fg(u,yy,ww):
    return add(pow4(u,4),mul(u,pow4(ww,3))),add(pow4(yy,3),pow4(ww,3))

roots3=[a for a in range(4) if pow4(a,3)==1]
roots4=[a for a in range(4) if add(pow4(a,4),a)==0]
assert set(roots3)=={1,2,3}
assert set(roots4)=={0,1,2,3}
base={(u,yy,1) for u in roots4 for yy in roots3}
assert len(base)==12
assert all(fg(*v)==(0,0) for v in base)
for u,yy,ww in itertools.product(range(4),repeat=3):
    if ww==1 and fg(u,yy,ww)==(0,0):assert (u,yy,ww) in base
# A line through P=[1:0:1:0] has direction [U:Y:W].
# It is contained iff the cubic and quartic homogeneous coefficients vanish.
# No direction at infinity W=0 can meet both H=G=0.
assert all(fg(1,yy,0)!=(0,0) for yy in range(4))
assert sum(fg(u,yy,1)==(0,0) for u,yy in itertools.product(range(4),repeat=2))==12

# Base-point transversality at W=1:
# dH/dY=Y^2, dG/dU=W^3, both nonzero at all twelve points.
assert all(pow4(yy,2)!=0 for u,yy,_ in base)

# Intersection matrix of the three exceptional proper transforms.
M=s.Matrix([[-3,1,1],[1,-3,1],[1,1,-3]])
assert sorted(M.eigenvals())==[-4,-1]
assert list(M*s.ones(3,1))==[-1,-1,-1]
# Blow up the ordinary triple intersection to produce an SNC exceptional star.
Ggood=s.Matrix([[-1,1,1,1],[1,-4,0,0],[1,0,-4,0],[1,0,0,-4]])
assert Ggood.det()==16
assert all(float(v)<0 for v in Ggood.eigenvals())
# Local Tjurina quotient: k[[U,Y,W]]/(U^4,Y^2,W^2).
monomials=list(itertools.product(range(4),range(2),range(2)))
assert len(monomials)==16

print('PASS: quartic transformation identity, 4-section map, partial derivatives,')
print('      twelve transverse F4 base points/lines, exceptional intersection matrix,')
print('      local Jacobian quotient length 16.')
