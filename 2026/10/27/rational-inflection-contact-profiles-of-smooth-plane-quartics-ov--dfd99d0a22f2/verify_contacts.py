#!/usr/bin/env python3
"""Second direct line-restriction check of all smooth orbit representatives."""
import sympy as S,itertools,json,collections
from pathlib import Path
X,Y,Z,T=S.symbols('X Y Z T')
var=(X,Y,Z)
monomials=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
points=[p for p in itertools.product([0,1],repeat=3) if any(p)]
D=json.load(open(Path(__file__).resolve().parent/'flex_quartics_data.json'))
counts=collections.Counter()
for row in D['representatives']:
 mask=row['mask']
 F=sum(X**a*Y**b*Z**c for i,(a,b,c) in enumerate(monomials) if (mask>>i)&1)
 grad=[S.diff(F,u) for u in var]
 contacts=collections.Counter()
 for p in points:
  subs=dict(zip(var,p))
  if int(F.subs(subs))%2!=0:continue
  g=[int(v.subs(subs))%2 for v in grad]
  assert any(g)
  q=next(q for q in points if q!=p and sum(g[i]*q[i] for i in range(3))%2==0)
  # Direct independent polynomial expansion, without Hasse binomial formula.
  pol=S.Poly(S.expand(F.subs({var[i]:p[i]+T*q[i] for i in range(3)}, simultaneous=True)),T,modulus=2)
  coeff={int(k[0]):int(v)%2 for k,v in pol.terms()}
  assert coeff.get(0,0)==0 and coeff.get(1,0)==0
  contact=next(j for j in (2,3,4) if coeff.get(j,0))
  contacts[contact]+=1
 assert row['contacts']==[contacts[j] for j in (2,3,4)]
 assert row['N']==sum(contacts.values())
 counts[(row['N'],*row['contacts'])]+=row['orbit_size']
expected={(p['N'],p['ordinary'],p['flex'],p['hyperflex']):p['forms'] for p in D['profiles']}
assert counts==expected
assert sum(counts.values())==10920 and len(counts)==34 and len(D['representatives'])==78
print('PASS: all 78 smooth orbit representatives checked by a second polynomial-restriction implementation; 34 exact profiles, 10920 equations.')
for s,v in sorted(counts.items()):print(*s,v)
