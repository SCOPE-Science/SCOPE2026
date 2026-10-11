#!/usr/bin/env python3
"""Symbolically verify the integrable zero-coupling Pehlivan--Wei flow."""
import sympy as s
x,y,z,u,H,K,a,t=s.symbols('x y z u H K a t',real=True)
f=s.Matrix([y*(1-z),y*(1+z)-a*x,a-x*y-y*y])
U=x+y
HH=z+U**2/4
KK=2*y-(1+HH)*U+U**3/12
B=s.Matrix([U,HH,KK])
L=s.Matrix([s.expand(s.diff(w,x)*f[0]+s.diff(w,y)*f[1]+s.diff(w,z)*f[2]) for w in B])
print('Lie(U),Lie(H),Lie(K) at a=0:',[s.simplify(v.subs(a,0)) for v in L]);assert s.simplify(L[1].subs(a,0))==0;assert s.simplify(L[2].subs(a,0))==0
inv=s.Matrix([u-(K+(1+H)*u-u**3/12)/2,(K+(1+H)*u-u**3/12)/2,H-u**2/4]);print('Inverse composing:',[s.factor(B[i].subs({x:inv[0],y:inv[1],z:inv[2]},simultaneous=True)-v) for i,v in enumerate([u,H,K])]);assert all(s.simplify(B[i].subs({x:inv[0],y:inv[1],z:inv[2]},simultaneous=True)-v)==0 for i,v in enumerate([u,H,K]));assert s.factor(B.jacobian([x,y,z]).det())==-2
P=K+(1+H)*u-u**3/12
assert s.factor((L[0].subs(a,0)).subs({x:inv[0],y:inv[1],z:inv[2]},simultaneous=True)-P)==0
q=s.symbols('q',positive=True);r=s.symbols('r',real=True,nonzero=True)
D=s.discriminant(-12*P,u); print('discriminant:',s.factor(D)); assert s.factor(D-432*(16*(1+H)**3-9*K**2))==0
print('fold positive:',s.factor((P.subs({H:q-1,K:-s.Rational(4,3)*q**s.Rational(3,2)}))));print('fold negative:',s.factor((P.subs({H:q-1,K:s.Rational(4,3)*q**s.Rational(3,2)}))))
assert s.factor(P.subs({H:q-1,K:-s.Rational(4,3)*q**s.Rational(3,2)})+(u-2*s.sqrt(q))**2*(u+4*s.sqrt(q))/12)==0
assert s.factor(P.subs({H:q-1,K:s.Rational(4,3)*q**s.Rational(3,2)})+(u+2*s.sqrt(q))**2*(u-4*s.sqrt(q))/12)==0
G=K*u+(1+H)*u*u/2-u**4/48
assert s.simplify(s.diff(G,u)-P)==0
print('cusp explicit u(t):',s.simplify(s.diff(u/s.sqrt(1+u*u*t/6),t)+(u/s.sqrt(1+u*u*t/6))**3/12)); assert s.simplify(s.diff(u/s.sqrt(1+u*u*t/6),t)+(u/s.sqrt(1+u*u*t/6))**3/12)==0
for hh,kk in [(0,0),(3,0),(3,5),(3,-5),(-3,1)]:
 print('leaf',hh,kk,'roots:',s.nroots(P.subs({H:hh,K:kk})))
print('ALL EXACT ALGEBRAIC CHECKS PASSED')
