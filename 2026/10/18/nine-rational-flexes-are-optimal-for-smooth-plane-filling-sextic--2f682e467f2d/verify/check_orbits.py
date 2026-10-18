import json,sympy as s,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
D=json.load(open(ROOT/'jet_data.json'))
X=s.symbols('x y z');M=D['mons'];B=D['basis']
F=[sum(B[i][j]*s.prod(X[k]**e for k,e in enumerate(M[j])) for j in range(28)) for i in range(15)]
for target in (11,9):
 for ent in json.load(open(ROOT/('orbits_'+str(target)+'.json'))):
  dig=ent['representative'];f=s.Poly(sum(dig[i]*F[i] for i in range(15)),*X,modulus=3).as_expr()
  print('REPR', ''.join(map(str,dig)), 'projective orbit size',ent['size'],'f',f,flush=True)
  for ax in range(3):
   vs=[X[k] for k in range(3) if k!=ax];ff=s.Poly(f.subs(X[ax],1),*vs,modulus=3).as_expr()
   gg=s.groebner([ff]+[s.diff(ff,w) for w in vs],*vs,modulus=3)
   print('axis',ax,'smooth',list(gg)==[1],'GB',str(gg)[:300],flush=True)
