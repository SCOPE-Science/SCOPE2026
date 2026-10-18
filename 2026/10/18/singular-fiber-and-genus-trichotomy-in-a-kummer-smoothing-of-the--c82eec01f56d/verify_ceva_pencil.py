#!/usr/bin/env python3
"""Exact symbolic and finite-field checks for a Kummer-Ceva smoothing of Fermat/Ceva lines.
Requires Python 3 and SymPy for the characteristic-zero identities.
"""
import sympy as S
x,y,l = S.symbols('x y l')
v = (x-y)*(y-1)*(1-x)
f = S.expand(v-l*x*y)
assert S.factor(S.together(S.diff(v/(x*y),x) + (x*x-y)*(y-1)/(x*x*y))) == 0
assert S.factor(S.together(S.diff(v/(x*y),y) + (x-1)*(x-y*y)/(x*y*y))) == 0
# At the two nodal parameter values l*l+27=0, the critical points are explicit.
a=-(l+3)/6
b=(l-3)/6
for E in [f,S.diff(f,x),S.diff(f,y)]:
    t=S.cancel(E.subs({x:a,y:b}))
    assert S.rem(S.together(t),l*l+27,l)==0
assert S.rem(S.det(S.hessian(f,[x,y])).subs({x:a,y:b}),l*l+27,l)==-9
# Check that the finite-parameter singular cubic is exactly at l=0 or l*l+27=0.
G = S.groebner([f,S.diff(f,x),S.diff(f,y)],x,y,l,order='lex')
assert any(p.as_expr()==l**3+27*l for p in G.polys)
# Exhaust finite-field projective singular sets; compare independently computed prediction.
q=13
inv=lambda t:pow(t%q,q-2,q)
points=[(a,b,1) for a in range(q) for b in range(q)] + [(a,1,0) for a in range(q)] + [(1,0,0)]
for m in (2,3):
  for lam in (0,1,5,8):
    predicted={(1,0,0),(0,1,0),(0,0,1)}
    if lam==0:
      predicted.update((a,b,1) for a in range(q) for b in range(q) if a*b%q and pow(a,m,q)==pow(b,m,q)==1)
    elif lam in (5,8):
      X=(-(lam+3)*inv(6))%q;Y=((lam-3)*inv(6))%q
      predicted.update((a,b,1) for a in range(q) for b in range(q) if pow(a,m,q)==X and pow(b,m,q)==Y)
    X,Y,Z = S.symbols('X Y Z')
    F=S.expand((X**m-Y**m)*(Y**m-Z**m)*(Z**m-X**m)-lam*(X*Y*Z)**m)
    fun=[S.lambdify((X,Y,Z),g,'math') for g in (F,S.diff(F,X),S.diff(F,Y),S.diff(F,Z))]
    found={p for p in points if all(int(v(*p))%q==0 for v in fun)}
    if found!=predicted: raise AssertionError((m,lam,len(found),len(predicted),found^predicted))
print('VERIFY_OK: rational-critical identities, nodal Hessian, elimination, and GF(13) projective singular strata for m=2,3')
