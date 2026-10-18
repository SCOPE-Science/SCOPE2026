import json,sympy as s,collections,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
D=json.load(open(ROOT/'jet_data.json'))
mons=D['mons']; B=D['basis']; X=s.symbols('x y z')
free=[next(j for j in range(28) if B[i][j]==1 and sum(B[k][j]!=0 for k in range(15))==1) for i in range(15)]
assert all(B[i][free[i]]==1 for i in range(15))
monexp=[s.prod(X[k]**e for k,e in enumerate(mons[j])) for j in range(28)]
forms=[sum(B[i][j]*monexp[j] for j in range(28)) for i in range(15)]
subslist=[(X[1],X[0],X[2]),(X[0],X[2],X[1]),(2*X[0],X[1],X[2]),(X[0]+X[1],X[1],X[2])]
trans=[]
for new in subslist:
 m=[]
 for f in forms:
  e=s.Poly(s.expand(f.subs(dict(zip(X,new)),simultaneous=True)),*X,modulus=3)
  m.append([int(e.coeff_monomial(monexp[j]))%3 for j in free])
 trans.append(m)
print('generators constructed',flush=True)
def act(dig,m):return tuple(sum(dig[i]*m[i][j] for i in range(15))%3 for j in range(15))
def norm(a):
 t=next(v for v in a if v)
 return tuple((2 if t==2 else 1)*v%3 for v in a)
def classify(flex_target):
 candidates={norm(tuple(map(int,l.split()[0]))) for l in open(ROOT/'flex_masks_9_11.txt') if l.rstrip().endswith(' '+str(flex_target))}
 expected={9:101088,11:19656}[flex_target]
 assert len(candidates)==expected,(flex_target,len(candidates),expected)
 unseen=set(candidates);out=[]
 while unseen:
  seed=min(unseen);orbit={seed};todo=[seed]
  for v in todo:
   for m in trans:
    w=norm(act(v,m))
    assert w in candidates, (flex_target,'non-invariant',w)
    if w not in orbit:orbit.add(w);todo.append(w)
  out.append({'representative':list(seed),'size':len(orbit)})
  unseen-=orbit
 with open(ROOT/('orbits_'+str(flex_target)+'.json'),'w') as h:json.dump(out,h,indent=2)
 print('flex',flex_target,'orbit_sizes',[r['size'] for r in out],flush=True)
for target in (11,9):classify(target)
