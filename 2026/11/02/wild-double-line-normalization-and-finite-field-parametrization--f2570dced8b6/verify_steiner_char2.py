#!/usr/bin/env python3
"""Reproduce exact identities and small finite-field counts for the Roman quartic in characteristic two."""
import itertools
import sympy as sp

s,t,u=sp.symbols('s t u')
W=s*s+t*t+u*u; X=t*u; Y=s*u; Z=s*t
F=(X*Y)**2+(X*Z)**2+(Y*Z)**2+W*X*Y*Z
assert sp.Poly(F,s,t,u,modulus=2).is_zero
print('PARAMETRIZATION_IDENTITY_OK')

x,y,z,w=sp.symbols('x y z w')
f=x*x*y*y+x*x*z*z+y*y*z*z+w*x*y*z
for v,target in [(x,w*y*z),(y,w*x*z),(z,w*x*y),(w,x*y*z)]:
    assert sp.Poly(sp.diff(f,v)+target,x,y,z,w,modulus=2).is_zero
print('JACOBIAN_PARTIALS_OK')

# In affine chart X=1 of the surface, normalize by r=t/u !=0, a=s/u.
a,r=sp.symbols('a r')
normalized_y=a/r; normalized_z=a; normalized_w=(a*a+r*r+1)/r
M=sp.Matrix([[sp.diff(h,a),sp.diff(h,r)] for h in (normalized_y,normalized_z,normalized_w)])
for (i,j),target in [((0,1),a/r**2),((0,2),(a*a+r*r+1)/r**3),((1,2),(a*a+r*r+1)/r**2)]:
    v=sp.cancel(M.extract([i,j],[0,1]).det())
    assert sp.Poly(sp.together((v-target)*r**6),a,r,modulus=2).is_zero
# The determinantal ideal at a=0, r=1 is (a,(r+1)^2) in char 2.
assert sp.Poly((r+1)**2-(r*r+1),r,modulus=2).is_zero
print('DIFFERENTIAL_DEGENERACY: 3 length-two points; total length 6')

# B= k[y,z,w]/(f|X=1), A = k[a,r,r^-1], and r generates A as a B-module.
# r*y=z, r*z=w*z+(z^2+1)*y, r^2+w*r+z^2+1=0, r^-1=r+w+yz.
for expression in [
    r*normalized_y-normalized_z,
    r*normalized_z-normalized_w*normalized_z-(normalized_z**2+1)*normalized_y,
    r*r+normalized_w*r+normalized_z**2+1,
    r*(r+normalized_w+normalized_y*normalized_z)-1,
]:
    num=sp.together(expression).as_numer_denom()[0]
    assert sp.Poly(num,a,r,modulus=2).is_zero,expression
print('NORMALIZATION_MODULE_RELATIONS_OK')

# In char2, beta=(r+1)/w with w=r+1/r satisfies beta^2+beta=1/w.
branch_w=(r*r+1)/r
beta=(r+1)/branch_w
artin=sp.cancel((beta**2+beta+1/branch_w))
assert sp.Poly(sp.together(artin).as_numer_denom()[0],r,modulus=2).is_zero
print('ARTIN_SCHREIER_NORMAL_FORM_OK: v^2+v=1/w')

class GF:
    def __init__(self,m,poly): self.m=m;self.q=1<<m;self.poly=poly
    def mul(self,a,b):
        out=0
        while b:
            if b&1:out^=a
            b>>=1;a<<=1
            if a&self.q:a^=self.poly
        return out
    def power(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n>>=1
        return z
    def inv(self,a):
        assert a
        return self.power(a,self.q-2)
    def normalize(self,v):
        for x in v:
            if x:
                k=self.inv(x)
                return tuple(self.mul(q,k) for q in v)
        raise ValueError('zero vector')
    def proj(self,dim):
        for k in range(dim+1):
            for suffix in itertools.product(range(self.q),repeat=dim-k):
                yield (0,)*k+(1,)+suffix

for m,poly in [(1,0b11),(2,0b111),(3,0b1011),(4,0b10011)]:
    g=GF(m,poly);q=g.q;mul=g.mul
    pts=set()
    for ss,tt,uu in g.proj(2):
        ww=mul(ss,ss)^mul(tt,tt)^mul(uu,uu)
        xx=mul(tt,uu);yy=mul(ss,uu);zz=mul(ss,tt)
        P=g.normalize((ww,xx,yy,zz));pts.add(P)
        assert mul(mul(ww,xx),mul(yy,zz)) ^mul(mul(xx,xx),mul(yy,yy))^mul(mul(xx,xx),mul(zz,zz))^mul(mul(yy,yy),mul(zz,zz))==0
    surface=[]
    for ww,xx,yy,zz in g.proj(3):
        if mul(mul(ww,xx),mul(yy,zz)) ^mul(mul(xx,xx),mul(yy,yy))^mul(mul(xx,xx),mul(zz,zz))^mul(mul(yy,yy),mul(zz,zz))==0:
            surface.append((ww,xx,yy,zz))
    surface=set(surface)
    assert pts<=surface
    expected_surface=q*q+q+2
    expected_image=q*q-q//2+2
    assert len(surface)==expected_surface,(q,len(surface),expected_surface)
    assert len(pts)==expected_image,(q,len(pts),expected_image)
    missing=surface-pts
    assert len(missing)==3*q//2
    assert all(P[0] != 0 and sum(bool(v) for v in P[1:]) == 1 for P in missing)
    print(f'GF({q}): SURFACE={len(surface)}, PARAMETER_IMAGE={len(pts)}, MISSING={len(missing)}')
print('VERIFY_OK')
