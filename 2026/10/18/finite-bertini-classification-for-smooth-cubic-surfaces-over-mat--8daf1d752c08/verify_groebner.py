#!/usr/bin/env python3
"""Independent symbolic smoothness checks over the algebraic closure.

Run after verify_census.py; requires SymPy and orbit_representatives.tsv.
For every projective representative, the gradient ideal is checked on every
affine chart. Euler's identity for degree 3 gives the singularity criterion.
"""
"""Independent exact algebraic-closure singularity test for enumerated representatives."""
import sympy as s,collections
x=s.symbols('x y z w'); u=s.symbols('u v t')

def monoms(n,d):
 if n==1:return [(d,)]
 return [(a,)+b for a in range(d,-1,-1) for b in monoms(n-1,d-a)]

m4=monoms(4,3)

def poly(mask,mons,vars):
 return sum(s.prod(t**a for t,a in zip(vars,ex)) for k,ex in enumerate(mons) if mask>>k&1)

def smooth(mask,mons,vars):
 F=poly(mask,mons,vars)
 dF=[s.diff(F,v) for v in vars]
 for j,v in enumerate(vars):
  others=[vv for i,vv in enumerate(vars) if i!=j]
  G=s.groebner([s.expand(q.subs(v,1)) for q in dF],*others,order='lex',modulus=2)
  if not (len(G.polys)==1 and G.polys[0].is_one):
   return False
 return True

reps=[tuple(map(int,line.split())) for line in list(open('orbit_representatives.tsv',encoding='utf8'))[1:]]
sec_restrict=[]
for normal in range(1,16):
 vs=[v for v in range(1,16) if (v&normal).bit_count()%2==0]
 basis=[];span={0}
 for z in vs:
  if z not in span:
   basis.append(z);span|={v^z for v in list(span)}
  if len(basis)==3:break
 assert len(span)==8
 subs={x[j]:sum(u[i] for i in range(3) if (basis[i]>>j)&1) for j in range(4)}
 sec_restrict.append(subs)

discrepancies=[]
for F,size,rank_smooth,count,rational_points in reps:
 truth=smooth(F,m4,x)
 if int(truth)!=rank_smooth:discrepancies.append((F,'surface',rank_smooth,truth))
print('surface Groebner verification',len(reps),'discrepancies',discrepancies,flush=True)
D=collections.Counter();errors=[]
for F,size,rank_smooth,count,rational_points in reps:
 if not rank_smooth:continue
 P=poly(F,m4,x); k=0
 for subs in sec_restrict:
  ps=s.Poly(s.expand(P.subs(subs, simultaneous=True)),*u,modulus=2)
  eq=sum(int(coef)%2*s.prod(z**a for z,a in zip(u,ex)) for ex,coef in ps.terms())
  assert s.Poly(eq,*u).total_degree()==3
  grad=[s.diff(eq,z) for z in u]
  ok=True
  for j,z in enumerate(u):
   others=[w for i,w in enumerate(u) if i!=j]
   G=s.groebner([s.expand(g.subs(z,1)) for g in grad],*others,order='lex',modulus=2)
   if not (len(G.polys)==1 and G.polys[0].is_one):ok=False;break
  k+=int(ok)
 if k!=count:errors.append((F,count,k))
 D[k]+=size
print('section Groebner verifier',len([r for r in reps if r[2]]),'discrepancies',errors,'weighted',dict(sorted(D.items())),flush=True)
assert not discrepancies and not errors
print('PASS independent exact Groebner checks',flush=True)
