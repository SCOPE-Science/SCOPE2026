#!/usr/bin/env python3
"""Independent symbolic smoothness and orbit calculation (requires sympy>=1.12)."""
from sympy import symbols,Poly,groebner
from itertools import combinations
from collections import Counter
import json
X,Y,Z=symbols('X Y Z')
V=(X,Y,Z)
MON=(X**2*Y,X**2*Z,X*Y**2,Y**2*Z,X*Z**2,Y*Z**2,X*Y*Z,Z**3)
F={m:sum(MON[i] for i in range(8) if m>>i&1) for m in range(1,256)}

def independent_smooth(f):
    grads=[f.diff(t) for t in V]
    for subs,rem in [({X:1},(Y,Z)),({X:0,Y:1},(Z,)),({X:0,Y:0,Z:1},())]:
        gs=[g.subs(subs) for g in grads]
        if not rem:
            if all(g==0 for g in gs):return False
        else:
            I=groebner(gs,*rem,modulus=2)
            if len(I.polys)!=1 or I.polys[0].as_expr()!=1:
                return False
    return True

sm={m for m in F if independent_smooth(F[m])}
assert len(sm)==60
pens={tuple(sorted((a,b,a^b))) for a,b in combinations(sorted(sm),2) if a^b in sm}
assert len(pens)==104
GROUP=[]
for swap in (0,1):
 for a in (0,1):
  for b in (0,1):
   M=((0,1,a),(1,0,b),(0,0,1)) if swap else ((1,0,a),(0,1,b),(0,0,1))
   sub={V[i]:sum(M[i][j]*V[j] for j in range(3)) for i in range(3)}
   action={}
   for m,f in F.items():
    p=Poly(f.subs(sub, simultaneous=True),X,Y,Z,modulus=2)
    t=sum((1<<i) for i,v in enumerate(MON) if p.coeff_monomial(v))
    assert Poly(F[t]-p.as_expr(),X,Y,Z,modulus=2).is_zero
    action[m]=t
   GROUP.append(action)
unseen=set(pens);orbit_reps=[]
while unseen:
 r=min(unseen)
 o={tuple(sorted(g[m] for m in r)) for g in GROUP}
 assert o<=unseen
 orbit_reps.append((r,len(o)));unseen-=o
assert len(orbit_reps)==13 and all(v==8 for r,v in orbit_reps)
P2=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
def val(f,point):return int(f.subs(dict(zip(V,point))))%2
r_counts=Counter(sum(not val(F[p[0]],v) and not val(F[p[1]],v) for v in P2) for p in pens)
assert r_counts=={2:56,3:48}
print(json.dumps({'smooth_count':len(sm),'pencil_count':len(pens),
                  'orbit_reps':orbit_reps,'orbit_count':len(orbit_reps),
                  'rational_base_distribution':dict(r_counts)},indent=2))
