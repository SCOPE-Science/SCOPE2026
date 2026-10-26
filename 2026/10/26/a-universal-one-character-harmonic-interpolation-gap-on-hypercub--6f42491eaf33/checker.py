"""Exact finite-dimensional checks supporting the cube harmonic sampling theorem.

Requires Python 3 and sympy. The all-dimension proof is analytic, not a finite census.
"""
from math import comb
import sympy as sp

u,v,w=sp.symbols('u v w')
R2=u*u+v*v+w*w
h4=u**4-6*u*u*v*v+v**4
h6=(231*u**6-315*u**4*R2+105*u*u*R2**2-5*R2**3)/16
h7=(429*u**7-693*u**5*R2+315*u**3*R2**2-35*u*R2**3)/16
assert sp.expand(sp.diff(h4,u,2)+sp.diff(h4,v,2))==0
for h in (h6,h7):
    assert sp.expand(sum(sp.diff(h,z,2) for z in (u,v,w)))==0
assert h4.subs({u:1,v:1})==-4
assert h6.subs({u:1,v:1,w:1})==6
assert h7.subs({u:1,v:1,w:1})==15
assert sp.expand((1+sp.I)**6)==-8*sp.I

x=sp.symbols('x')
for d in range(3,11):
    a=sp.Rational(d-2,2)
    P=[sp.Integer(1),x]
    Lmax=d+4
    for ell in range(1,Lmax):
        P.append(sp.expand((2*(ell+a)*x*P[-1]-ell*P[-2])/(ell+2*a)))
    for ell in (d,d+2,d+4):
        values=[P[ell].subs(x,sp.Rational(d-2*k,d)) for k in range(d+1)]
        rank=0
        vanished=[]
        for j in range(d+1):
            ev=sp.factor(sum(values[k]*sum((-1)**t*comb(j,t)*comb(d-j,k-t)
                for t in range(max(0,k-d+j),min(j,k)+1)) for k in range(d+1)))
            if ev:
                rank+=comb(d,j)
            else:
                vanished.append(j)
        expected=2**(d-1)-(ell==d+2)
        assert rank==expected,(d,ell,rank,expected)
        assert vanished==[j for j in range(d+1) if j%2 != ell%2] + ([d] if ell==d+2 else []), (d,ell,vanished)
        print('dimension',d,'degree',ell,'rank',rank,'target',expected)
print('All exact finite tests passed; all-dimension proof is independent of the tests.')
