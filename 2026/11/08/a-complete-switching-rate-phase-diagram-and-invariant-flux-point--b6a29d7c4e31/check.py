#!/usr/bin/env python3
"""Independent exact checks for the two-state spectral-diffusion intensity theorem.
This is a standalone mathematical verification aid, not an infinite proof.
"""
import sympy as S
import random
T,X,V=S.symbols('t x v',real=True)
I=S.I
A=1-I*X
U=1+T-I*X
Z=A*U+V**2
expected=S.cancel(U/Z)
M=S.Matrix([[1+T/2-I*(X-V),-T/2],[-T/2,1+T/2-I*(X+V)]])
b=S.Matrix([S.Rational(1,2),S.Rational(1,2)])
from_generator=S.cancel((S.ones(1,2)*M.inv()*b)[0]); assert S.simplify(from_generator-expected)==0
p=1+T+V**2-X**2
q=X*(2+T)
R=((1+T)*(1+T+V**2)+X**2)/(p*p+q*q)
assert S.simplify(S.re(S.expand_complex(expected))-R)==0
assert S.factor(S.diff(R,T)-V**2*(p*p-q*q)/(p*p+q*q)**2)==0
minus=(1-X)*T+1+V**2-X**2-2*X
plus=(1+X)*T+1+V**2-X**2+2*X
assert S.expand(minus*plus-(p*p-q*q))==0
assert S.factor(R.subs({X:1,V:S.sqrt(2)})-S.Rational(1,2))==0
assert S.factor(S.diff(R,T).subs({X:1,V:S.sqrt(2)}))==0
flat_amp=S.factor(expected.subs({X:1,V:S.sqrt(2)}))
assert S.simplify(flat_amp-(S.Rational(1,2)+I*T/(2*(T+2))))==0
flat_el=S.simplify((flat_amp*S.conjugate(flat_amp)).expand(complex=True))
assert S.simplify(flat_el-(S.Rational(1,4)+T*T/(4*(T+2)**2)))==0
assert S.simplify(S.Rational(1,2)-flat_el-(T+1)/(T+2)**2)==0
assert S.simplify(S.diff(flat_el,T)-T/(T+2)**3)==0
assert S.simplify(S.diff(S.Rational(1,2)-flat_el,T)+T/(T+2)**3)==0
# Unit/zero splitting recovery.
assert S.factor(R.subs(V,0)-1/(1+X*X))==0
assert S.factor(S.limit(R,T,S.oo)-1/(1+X*X))==0
# Differentiation sign and extremal positions checked against exact rational samples.
examples=[
 (S.Rational(7,2), S.Integer(1), S.Rational(13,18),'max_small'),
 (S.Rational(7,2), S.Integer(8), None,'decrease'),
 (S.Rational(7,2), S.Integer(24), S.Rational(23,10),'max_large'),
 (S.Rational(7,10), S.Rational(1,4), S.Rational(32,15),'min'),
 (S.Integer(0), S.Integer(2), None,'increase'),
 (S.Integer(1),S.Integer(2),None,'flat')]
for x,s2,star,regime in examples:
 f=S.factor(R.subs({X:x,V:S.sqrt(s2)}))
 der=S.factor(S.diff(f,T))
 if star is not None:
  assert S.simplify(der.subs(T,star))==0,(regime,star,der)
  assert S.sign(S.diff(f,T,2).subs(T,star)) == (1 if regime=='min' else -1)
 else:
  samples=[S.Rational(1,10),S.Integer(1),S.Integer(10)]
  if regime=='flat':assert all(S.simplify(der.subs(T,z))==0 for z in samples)
  else:assert all(S.sign(der.subs(T,z))== (1 if regime=='increase' else -1) for z in samples)
# exact independent two-component resolvent vs rational formula on deterministic grid
checks=0
for x in [S.Rational(0),S.Rational(1,3),S.Rational(7,10),S.Integer(1),S.Rational(3,2),S.Rational(5,2),S.Rational(7,2)]:
 for v in [S.Rational(1,3),S.Rational(1),S.sqrt(2),S.Integer(3),S.Integer(5)]:
  for t in [S.Integer(0),S.Rational(1,2),S.Integer(1),S.Integer(4),S.Integer(13)]:
   mat=M.subs({X:x,V:v,T:t})
   val=S.simplify(S.re((S.ones(1,2)*mat.inv()*b)[0]))
   assert S.simplify(val-R.subs({X:x,V:v,T:t}))==0,(x,v,t)
   checks+=1
# additional sign-region test without trusting root formulas
random.seed(271828)
for _ in range(300):
 x=S.Rational(random.randint(0,100),20)
 s2=S.Rational(random.randint(1,200),20)
 t=S.Rational(random.randint(1,200),20)
 derived=S.factor(S.diff(R,T)).subs({X:x,V:S.sqrt(s2),T:t})
 direct=S.re(S.diff(expected,T).subs({X:x,V:S.sqrt(s2),T:t}))
 assert S.simplify(derived-direct)==0
 checks+=1
print('PASS',checks,'independent rational resolvent and derivative comparisons; six phase witnesses; exact symbolic identities')
print('Witnesses:')
for x,s2,star,regime in examples:
 f=R.subs({X:x,V:S.sqrt(s2)})
 print(regime,'x=',x,'v2=',s2,'critical_t=',star,'R(0)=',S.factor(f.subs(T,0)),'R(infty)=',S.factor(S.limit(f,T,S.oo)),'R(tcrit)=',S.factor(f.subs(T,star)) if star else '')
