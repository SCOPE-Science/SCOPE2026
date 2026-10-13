#!/usr/bin/env python3
"""Independently check exact Lee--Yang polynomial and sign certificates."""
import itertools
import sympy as sp
q,z,y=sp.symbols('q z y')

def direct(m):
    E=[(i,j) for i in range(2) for j in range(2,m+2)]
    ans=sp.Integer(0)
    for bits in itertools.product((0,1),repeat=m+2):
        cross=sum(bits[u] != bits[v] for u,v in E)
        ans += z**sum(bits)*q**cross
    return sp.expand(ans)

for m in (3,4):
    Q=direct(m)
    formula=(1+q**2*z)**m+2*q**m*z*(1+z)**m+z**2*(q**2+z)**m
    assert sp.expand(Q-formula)==0
    assert sp.expand(z**(m+2)*Q.subs(z,1/z)-Q)==0
    if m==3:
        F=y**2+(2*q**3+3*q**2-1)*y+q**6+3*q**4+4*q**3-3*q**2-1
        expr=(z+1)*z**2*F.subs(y,z+1/z)
        assert sp.factor(F.subs(y,-2))==(q-1)**2*(q+1)**2*(q**2+5)
        assert sp.expand(F.subs(y,-q**3-q**2)+(q-1)**2*(3*q**3+5*q**2+2*q+1))==0
    else:
        F=y**3+(2*q**4+4*q**2)*y**2+(q**8+14*q**4-3)*y+8*q**6+8*q**4-8*q**2
        expr=z**3*F.subs(y,z+1/z)
        assert sp.expand(F.subs(y,-2)+2*(q-1)**4*(q+1)**4)==0
        assert sp.expand(F.subs(y,2)-2*(q**8+4*q**6+22*q**4+4*q**2+1))==0
        assert sp.expand(F.subs(y,-q**4-q**2)-q**2*(q-1)**3*(q+1)**3*(4*q**2+5))==0
    assert sp.cancel(Q-expr)==0
    for Qvalue in (sp.Rational(6,5),sp.Rational(3,2),sp.Integer(2),sp.Integer(3)):
        fy=sp.Poly(F.subs(q,Qvalue),y)
        yr=sp.polys.polytools.intervals(fy,eps=sp.Rational(1,10**6))
        assert len(yr)==m-1 and all(mult==1 for _,mult in yr)
        yy=[(float(a)+float(b))/2 for (a,b),_ in yr]
        assert sum(t<-2 for t in yy)==2
        assert (sum(-2<t<2 for t in yy)==(m==4))
print('VERIFY_OK direct_spin_configs=96 exact_polynomial_identities=2 exact_sign_certificates=5 sample_root_censuses=8')
