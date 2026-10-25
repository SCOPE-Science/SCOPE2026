"""Exact symbolic and finite-field checks for the characteristic-two Roman quartic.

Run: python3 check.py (requires sympy).
Only finite-field point counts are experimental corroboration; the included
algebraic proof establishes the statements over an algebraic closure.
"""
from itertools import product
import sympy as sp

x,y,z,w,s,t,u=sp.symbols('x y z w s t u')
F=x*x*y*y+x*x*z*z+y*y*z*z+x*y*z*w
quadrics=(t*u,s*u,s*t,s*s+t*t+u*u)
subs=dict(zip((x,y,z,w), quadrics))
assert sp.Poly(sp.expand(F.subs(subs)),s,t,u,modulus=2).is_zero
partials=[sp.Poly(sp.diff(F,v),x,y,z,w,modulus=2).as_expr() for v in (x,y,z,w)]
assert partials==[y*z*w,x*z*w,x*y*w,x*y*z],partials
# Derive the projective intrinsic Jacobian ideal, including F itself,
# before dehomogenizing; degree four is divisible by characteristic two.
chart_poly=sp.Poly(F.subs({x:1}),y,z,w,modulus=2).as_expr()
local_gens=[chart_poly]+[sp.Poly(g.subs({x:1}),y,z,w,modulus=2).as_expr() for g in partials]
I=sp.groebner(local_gens,y,z,w,order='lex',modulus=2)
expected=sp.groebner((y*z,y*w,z*w,y*y+z*z),y,z,w,order='lex',modulus=2)
assert I.polys==expected.polys,(I,expected)
assert set(map(str,I.polys))==set(map(str,expected.polys))
E_gens=[sp.Poly(F.subs({w:1}),x,y,z,modulus=2).as_expr()]+[sp.Poly(g.subs({w:1}),x,y,z,modulus=2).as_expr() for g in partials]
E=sp.groebner(E_gens,x,y,z,order='lex',modulus=2)
E_expected=sp.groebner((x*y,x*z,y*z),x,y,z,order='lex',modulus=2)
assert E.polys==E_expected.polys
for mon in (y**3,z**3,w*y,w*z,y*z,y*y+z*z):
    assert sp.Poly(I.reduce(mon)[1],y,z,w,modulus=2).is_zero,mon
for mon in (y,z,y*y):
    assert not sp.Poly(I.reduce(mon)[1],y,z,w,modulus=2).is_zero,mon
# linear independence, by pairwise distinct Groebner normal monomials.
assert len({sp.expand(I.reduce(mon)[1]) for mon in (y,z,y*y)})==3
# Partial derivatives on chart w=1 are (yz,xz,xy), hence the
# reduced coordinate-axes singular scheme near the triple point.
assert all(sp.Poly(p.subs({w:1}),x,y,z,modulus=2).as_expr() in (y*z,x*z,x*y,x*y*z) for p in partials)

MODULI={1:0b11,2:0b111,3:0b1011}
def mul(a,b,m):
    mod=MODULI[m]; res=0
    while b:
        if b&1:res^=a
        b>>=1;a<<=1
        if a&(1<<m):a^=mod
    return res

def pw(a,n,m):
    r=1
    while n:
        if n&1:r=mul(r,a,m)
        n//=2;a=mul(a,a,m)
    return r

def canon(P,m):
    for v in P:
        if v:
            iv=pw(v,(1<<m)-2,m)
            return tuple(mul(q,iv,m) for q in P)
    raise ValueError('zero point')

def all_projective(n,m):
    q=1<<m; seen=set()
    for P in product(range(q),repeat=n):
        if any(P):seen.add(canon(P,m))
    return seen

def value(P,m):
    X,Y,Z,W=P
    mm=lambda a,b:mul(a,b,m)
    square=lambda a:mm(a,a)
    return mm(square(X),square(Y))^mm(square(X),square(Z))^mm(square(Y),square(Z))^mm(mm(mm(X,Y),Z),W)

def jac(P,m):
    X,Y,Z,W=P; mm=lambda a,b:mul(a,b,m)
    return (mm(mm(Y,Z),W),mm(mm(X,Z),W),mm(mm(X,Y),W),mm(mm(X,Y),Z))

for m in (1,2,3):
    q=1<<m
    P3=all_projective(4,m); P2=all_projective(3,m)
    Xpts={P for P in P3 if value(P,m)==0}
    singular={P for P in Xpts if jac(P,m)==(0,0,0,0)}
    expected={(X,Y,Z,W) for X,Y,Z,W in Xpts if sum(v!=0 for v in (X,Y,Z))<=1}
    assert singular==expected
    assert len(Xpts)==q*q+q+2,(q,len(Xpts))
    assert len(singular)==3*q+1,(q,len(singular))
    nimage={canon((mul(b,c,m),mul(a,c,m),mul(a,b,m),pw(a,2,m)^pw(b,2,m)^pw(c,2,m)),m) for a,b,c in P2}
    assert nimage.issubset(Xpts)
    print(f'GF({q}): P3={len(P3)} quartic={len(Xpts)} singular={len(singular)} normalization_image={len(nimage)}')
print('CHECK_OK: exact identity, characteristic-two Jacobian, local embedded torsion length three, GF(2), GF(4), GF(8) counts')
