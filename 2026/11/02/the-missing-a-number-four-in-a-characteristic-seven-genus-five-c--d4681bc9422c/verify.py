#!/usr/bin/env python3
"""Exact characteristic-seven Cartier-stratification certificate.
Requires sympy (tested with 1.13 or later). No network or external files.
All polynomial reductions and ideal calculations are over GF(7).
"""
from collections import Counter
import sympy as S
x,s,v,z,L=S.symbols('x s v z L')
p=7

def red(expr, *gens):
    return S.Poly(S.expand(expr),*gens,modulus=p).as_expr()

G=S.Poly((x-1)**2*(x*x-s*x+v),x)
A0=red((S.Poly((x-1)**3*(x*x-s*x+v),x)).nth(3),s,v)
A1=red((S.Poly((x-1)**3*(x*x-s*x+v),x)).nth(2),s,v)
B0=red((G**5).nth(10),s,v)
B1=red((G**5).nth(17),s,v)
assert A0==3*s+v+3
assert A1==-3*s-3*v-1
assert B0==3*s**3*v**2+3*s**3+2*s**2*v**3+2*s**2+s*v**4-s*v**3-s*v+s+v**5+v**4+v+1
assert B1==-3*s**3-2*s**2+s*v-s-v-1
# Cartier images from the 5-differential basis.  The x variable here is w^2.
# The three coefficients of C(dw/z) are [x^3,x^10,x^17]G^5,
# with relation c0+c2+c4=0; this is the holomorphy constraint.
assert red((G**5).nth(3)+(G**5).nth(10)+(G**5).nth(17),s,v)==0
# (w^2-1)F^3 central Cartier block, where F(w)=G(w^2).
Ccenter=red((S.Poly((x-1),x)*G**3).nth(10),s,v)
Leg_center=red(S.Poly((x*x-s*x+v)**3,x).nth(3),s,v)
assert red(Ccenter-Leg_center,s,v)==0
# Characteristic seven Hasse invariant, roots 2,4,6.
H=red(sum(S.binomial(3,j)**2*L**j for j in range(4)),L)
assert red(H-(L-2)*(L-4)*(L-6),L)==0
# A pair vanishes precisely at (s,v)=(1,1).
assert S.groebner([A0,A1],s,v,modulus=p)==S.groebner([s-1,v-1],s,v,modulus=p)
assert red(B0.subs({s:1,v:1}),s,v)==0 and red(B1.subs({s:1,v:1}),s,v)==0
# Complete algebraic-closure certificate: exclude singular parameter locus
# v(v-s+1)(s^2-4v)=0 by localization. Lex Groebner basis exactly as below.
ideal=S.groebner([B0,B1,z*v*(v-s+1)*(s*s-4*v)-1],z,s,v,order='lex',modulus=p)
expected=S.groebner([z-2,s-1,v-1],z,s,v,order='lex',modulus=p)
assert ideal==expected, (ideal, expected)
# By directly substituting 7-element-field values, cross-check 20 smooth
# ordered presentations, including both superspecial points.
frequency=Counter()
for t in range(2,7):
  for u in range(2,7):
    if t==u:continue
    sv={(s):(t+u)%p,(v):(t*u)%p}
    aval=[int(a.subs(sv))%p for a in (A0,A1)]
    bval=[int(b.subs(sv))%p for b in (B0,B1)]
    center=int(Ccenter.subs(sv))%p
    # rank(Cartier): two off-diagonal blocks and the central 1x1.
    rank=int(any(aval))+int(any(bval))+int(center!=0)
    exact_a=5-rank
    desired=2+int(((u*pow(t,-1,p))%p) in (2,4,6))+2*int((t+u)%p==1 and (t*u)%p==1)
    assert exact_a==desired,(t,u,exact_a,desired)
    frequency[exact_a]+=1
assert dict(frequency)=={2:8,3:10,5:2},frequency
print('VERIFY_OK')
