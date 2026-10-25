#!/usr/bin/env python3
"""Exact checks for the three-by-three Hankel permanent singular-scheme calculation.

Uses Python 3 and SymPy. This verifies polynomial identities and finite-field
point support; the proof of all-characteristic scheme structure is in RESULT.md.
"""
import itertools
import sympy as sp

a,b,c,d,e,t,U,V,W=sp.symbols('a b c d e t U V W')
F=a*c*e+a*d**2+b*b*e+2*b*c*d+c**3
P=sp.expand(F.subs(a,1))
u=c+b*b
w=d+b*c
v=e+u**2-4*b*b*u+5*b**4
assert sp.expand(P-(w**2+u*v-2*b**6))==0
inv={c:U-t*t, d:W-t*(U-t*t), e:V-U**2+4*t*t*U-5*t**4}
assert sp.expand(P.subs({b:t,c:U-t*t,d:W-t*(U-t*t),e:V-U**2+4*t*t*U-5*t**4})-(W**2+U*V-2*t**6))==0
# The involution reversing the five coordinates preserves the permanent.
assert sp.expand(F-F.xreplace({a:e,e:a,b:d,d:b}))==0
partials=[sp.diff(F,x) for x in [a,b,c,d,e]]
assert partials==[c*e+d**2,2*b*e+2*c*d,a*e+2*b*d+3*c**2,2*a*d+2*b*c,a*c+b**2]
# Mod-p Jacobian normal forms, checked by Groebner normal forms.
G=W**2+U*V-2*t**6
for p in [2,3,5,7,11]:
    generators=[G]+[sp.diff(G,z) for z in [t,U,V,W]]
    basis=sp.groebner(generators, V,U,W,t,modulus=p)
    if p==2: expected=[U,V,W**2]
    elif p==3: expected=[U,V,W,t**6]
    else: expected=[U,V,W,t**5]
    for q in expected:
        assert basis.reduce(q)[1]==0,(p,q)
    eb=sp.groebner(expected,V,U,W,t,modulus=p)
    for q in basis.polys:
        assert eb.reduce(q.as_expr())[1]==0,(p,q)
# A characteristic-three polar curve and its off-hypersurface point.
S,T=sp.symbols('S T')
param={a:S**4,b:S**3*T,c:-S**2*T**2,d:S*T**3,e:T**4}
assert sp.expand(F.subs(param)+2*S**6*T**6)==0
for h in partials:
    hparam=sp.expand(h.subs(param))
    assert all(int(coeff)%3==0 for coeff in sp.Poly(hparam,S,T).coeffs())
# Exhaustive rational point support (not a proof of geometric support).
for p in [2,3,5]:
    xs=list(itertools.product(range(p),repeat=5))
    projective=[v for v in xs if next((z for z in v if z),None)==1]
    # ensure unique points by normalizing first nonzero coordinate
    projective=[]
    for z in xs:
        nz=next((val for val in z if val),None)
        if nz is None: continue
        zz=tuple(val*pow(nz,-1,p)%p for val in z)
        if zz not in projective: projective.append(zz)
    found=set()
    poly=sp.Poly(F,a,b,c,d,e)
    pps=[sp.Poly(f,a,b,c,d,e) for f in partials]
    for z in projective:
        sub=dict(zip((a,b,c,d,e),z))
        if int(poly.eval(sub))%p==0 and all(int(h.eval(sub))%p==0 for h in pps):
            found.add(z)
    if p==2:
        expected={(1,0,0,0,0),(1,1,1,1,1),(0,0,0,0,1)}
    else: expected={(1,0,0,0,0),(0,0,0,0,1)}
    assert found==expected,(p,found,expected)
# The polar base over F_3 consists of four rational points of the quartic plus Q.
p=3
polar=set()
for vals in itertools.product(range(p),repeat=5):
    fst=next((u for u in vals if u),None)
    if fst is None:continue
    z=tuple(v*pow(fst,-1,p)%p for v in vals)
    sub=dict(zip((a,b,c,d,e),z))
    if all(int(h.eval(sub))%p==0 for h in pps):polar.add(z)
expected={(0,0,0,0,1),(0,0,1,0,0)}
expected.update({(1,z,-z*z%3,z**3%3,z**4%3) for z in range(3)})
assert polar==expected,(polar,expected)
print('VERIFY_OK: exact transformation, Jacobian normal forms p=2,3,5,7,11; exhaustive F2/F3/F5 support; F3 polar base')
