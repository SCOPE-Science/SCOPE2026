import sympy as s
from itertools import product
X,Y,Z,W=s.symbols('X Y Z W');u,v,t=s.symbols('u v t')
for eps in [0,1]:
 F=X*W*(X+W)+Y*Z*(Y+Z)+eps*Y*Z*W
 good=[];bad=[]
 for bits in product([0,1],repeat=4):
  if not any(bits):continue
  ker=[p for p in product([0,1],repeat=4) if any(p) and (sum(b*c for b,c in zip(bits,p))%2==0)]
  basis=[]; span={(0,0,0,0)}
  for p in ker:
   if p not in span:
    basis.append(p); span=span|{tuple(a^b for a,b in zip(q,p)) for q in span}
    if len(basis)==3:break
  assert len(basis)==3
  subs={q:sum(basis[j][i]*[u,v,t][j] for j in range(3)) for i,q in enumerate((X,Y,Z,W))}
  cubic=s.Poly(F.subs(subs,simultaneous=True),u,v,t,modulus=2).as_expr()
  deriv=[s.diff(cubic,q) for q in (u,v,t)]
  singular=False
  for q in (u,v,t):
   ds=[s.Poly(g.subs(q,1),*[vv for vv in (u,v,t) if vv!=q],modulus=2).as_expr() for g in deriv]
   G=s.groebner(ds,*[vv for vv in (u,v,t) if vv!=q],modulus=2)
   if not G.is_zero_dimensional or G!=s.groebner([1],*[vv for vv in (u,v,t) if vv!=q],modulus=2):
    # non-unit ideal, even when zero-dimensional empty test direct is_one property
    if not (len(G.polys)==1 and G.polys[0].as_expr()==1):singular=True;break
  (bad if singular else good).append(bits)
 print('eps',eps,'smooth sections',len(good),'singular sections',len(bad),'all normals',len(good)+len(bad))
 assert not good
