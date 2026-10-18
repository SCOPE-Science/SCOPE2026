"""Direct line-contact and geometric-smoothness check on orbit representatives."""
import json
from pathlib import Path
import sympy as sp
R=Path(__file__).resolve().parent
D=json.loads((R/'jet_data.json').read_text())
x,y,z=sp.symbols('x y z'); t=sp.Symbol('t'); X=[x,y,z]
mon=[sp.prod(X[k]**a for k,a in enumerate(ex)) for ex in D['mons']]
basis=[sum(int(c)*mon[j] for j,c in enumerate(row)) for row in D['basis']]
pts=D['pts']
def witness_f(dig):return sp.Poly(sum(int(dig[i])*basis[i] for i in range(15)),*X,modulus=3).as_expr()
def contact(F,P):
 grad=[int(sp.diff(F,X[k]).subs(dict(zip(X,P))))%3 for k in range(3)]
 assert any(grad)
 options=[]
 for aa in range(3):
  for bb in range(3):
   for cc in range(3):
    V=(aa,bb,cc)
    if V==(0,0,0) or sum(grad[i]*V[i] for i in range(3))%3:continue
    if any(all((V[i]-c*P[i])%3==0 for i in range(3)) for c in range(3)):continue
    options.append(V)
 assert options
 V=options[0]
 pol=sp.Poly(sp.expand(F.subs({X[i]:P[i]+t*V[i] for i in range(3)},simultaneous=True)),t,modulus=3)
 if pol.is_zero:return 100
 return min(k[0] for k,c in pol.terms())

results={}
for target,expected_orbits,expected_smooth in [(11,4,0),(9,20,3)]:
 O=json.loads((R/f'orbits_{target}.json').read_text())
 assert len(O)==expected_orbits
 data=[]
 for ent in O:
  dig=ent['representative'];F=witness_f(dig)
  assert all(int(F.subs(dict(zip(X,P))))%3==0 for P in pts)
  mult=[contact(F,P) for P in pts]
  assert sum(m>=3 for m in mult)==target and sum(m==2 for m in mult)==13-target,(dig,mult)
  charts=[]
  for fixed in range(3):
   vs=[X[j] for j in range(3) if j!=fixed]
   p=sp.Poly(F.subs(X[fixed],1),*vs,modulus=3).as_expr()
   G=sp.groebner([p,sp.diff(p,vs[0]),sp.diff(p,vs[1])],*vs,modulus=3)
   charts.append(list(G)==[1])
  if all(charts):assert set(mult)=={2,3}
  data.append(dict(representative=''.join(map(str,dig)),projective_orbit=ent['size'],smooth=all(charts),chart_unit_ideals=charts,nonflex_points=[pts[k] for k,m in enumerate(mult) if m==2]))
 assert sum(item['smooth'] for item in data)==expected_smooth
 assert sum(item['projective_orbit'] for item in data if item['smooth']) == (16848 if target==9 else 0)
 results[str(target)]=data
 print('target',target,'orbits',len(data),'smooth',expected_smooth)
(R/'independent_report.json').write_text(json.dumps(results,indent=2)+'\n')
