from itertools import combinations
import sympy as s
from collections import defaultdict,Counter
N=7
F={tuple(sorted((i+j)%N for j in (0,1,3))) for i in range(N)}|{tuple(sorted((i+j)%N for j in (0,1,5))) for i in range(N)}
print('Facets:',sorted(F))
E=Counter(x for f in F for x in combinations(f,2));print('f',N,len(E),len(F),'edge degrees',set(E.values()))

def each_subsets():
 for k in range(3,N+1):
  for I in combinations(range(N),k): yield I
class HH:
 def __init__(self,I):
  self.I=I; self.root=I[0];self.edges=list(combinations(I[1:],2));self.edidx={e:j for j,e in enumerate(self.edges)}
  self.tfaces=[f for f in F if set(f)<=set(I)]
  self.boundaries=s.zeros(len(self.edges),len(self.tfaces))
  for col,f in enumerate(self.tfaces):
   for ix in range(3):
    e=tuple(t for j,t in enumerate(f) if j!=ix)
    if self.root not in e:self.boundaries[self.edidx[e],col]+=(-1)**ix
  # pivot columns of B; quotient basis selected coordinate nonpivots via left nullspace of B.T
  self.quot=s.Matrix.hstack(*self.boundaries.T.nullspace()) if len(self.edges) and self.boundaries.T.nullspace() else s.zeros(len(self.edges),0)
  # basis of cycles at domain mapped to coordinate in quotient via quotient.T (not necessarily integral)
  self.rank=self.quot.cols
  self.smith_partial = (self.boundaries.rows,self.boundaries.cols,self.boundaries.rank())
 def cycle_to_coords(self,chain):
  # a 1-cycle as dict edge->signed integer; fundamental cycles are nonstar edge coordinate directly
  v=s.zeros(len(self.edges),1)
  for e,c in chain.items():
   if self.root not in e:v[self.edidx[e]]=c
  return v
 def basis_cycle(self,i):
  a,b=self.edges[i]
  return {tuple(sorted((self.root,a))):1,(a,b):1,tuple(sorted((self.root,b))):-1} # root smaller all
 def inclusion(self,other):
  # map on dual space H1(source) -> H1(target), representation in Q.T coordinates, choose source image vectors of fundamental edge cycles, quotient by boundary relations
  # compute Qtarget.T on source cycles, express source via Qsource.T
  A=s.zeros(other.rank,len(self.edges))
  for i in range(len(self.edges)):
   v=other.cycle_to_coords(self.basis_cycle(i))
   A[:,i]=other.quot.T*v
  # find linear T such that T Qsource.T=A (which holds provided source boundaries killed); use independent columns from Qsource.T
  if self.rank==0:return s.zeros(other.rank,0)
  Q=self.quot.T
  _,piv=Q.rref();inds=list(piv)[:self.rank]; X=Q[:,inds]
  T=s.simplify(A[:,inds]*X.inv())
  assert T*Q==A, ('inclusion_mismatch',self.I,other.I)
  assert all(z.q==1 for z in T if hasattr(z,'q')), ('nonintegral',self.I,other.I)
  return T

objs={I:HH(I) for I in each_subsets()}
for k in range(3,8):
 print('k=',k,'ranks',Counter(x.rank for I,x in objs.items() if len(I)==k),'total',sum(x.rank for I,x in objs.items() if len(I)==k))

for k in range(3,7):
 src=[I for I,x in objs.items() if len(I)==k and x.rank>0]
 tgt=[I for I,x in objs.items() if len(I)==k+1 and x.rank>0]
 soi={I:sum(objs[J].rank for J in src[:ix]) for ix,I in enumerate(src)}
 toi={I:sum(objs[J].rank for J in tgt[:ix]) for ix,I in enumerate(tgt)}
 D=s.zeros(sum(objs[I].rank for I in tgt),sum(objs[I].rank for I in src))
 for I in src:
  for j in range(N):
   if j in I:continue
   J=tuple(sorted((*I,j)))
   if objs[J].rank==0:continue
   T=objs[I].inclusion(objs[J])
   eps=(-1)**sum(i<j for i in I)
   D[toi[J]:toi[J]+objs[J].rank,soi[I]:soi[I]+objs[I].rank]=eps*T
 print('d',k,'shape',D.shape,'rank',D.rank(),'max coefficient',max([abs(q) for q in D] or [0]))
 if k==3: D3=D
 if k==4: D4=D
 if k==5: D5=D
 if k==6: D6=D
dims=[sum(x.rank for I,x in objs.items() if len(I)==k)-(0 if k==3 else [D3,D4,D5,D6][k-4].rank())-(0 if k==7 else [D3,D4,D5,D6][k-3].rank()) for k in range(3,8)]
assert dims==[1,0,1,0,0], dims
assert D4*D3==s.zeros(D4.rows,D3.cols) and D5*D4==s.zeros(D5.rows,D4.cols) and D6*D5==s.zeros(D6.rows,D5.cols)
print('HH1 dims:',dims)

from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
for nm,M in [('D3',D3),('D4',D4),('D5',D5),('D6',D6)]:
 S=smith_normal_form(M,domain=ZZ)
 diag=[S[i,i] for i in range(min(S.shape)) if S[i,i]!=0]
 assert all(abs(x)==1 for x in diag), (nm,diag)
 print(nm,'smith',Counter(abs(x) for x in diag),'rank',len(diag))
for I,x in objs.items():
 if not x.boundaries.cols: continue
 S=smith_normal_form(x.boundaries,domain=ZZ)
 diag=[S[i,i] for i in range(min(S.shape)) if S[i,i]!=0]
 assert all(abs(q)==1 for q in diag), (I,diag)
# dim H1 first few groups as q-basis saturation; Q.T Smith all 1
for I,x in objs.items():
 if x.rank:
  S=smith_normal_form(x.quot.T,domain=ZZ)
  diag=[S[i,i] for i in range(min(S.shape)) if S[i,i]!=0]
  assert all(abs(q)==1 for q in diag), (I,diag)
# Check vertex links are six-cycles, so this connected closed surface is a torus.
for v in range(N):
 links=[tuple(t for t in f if t!=v) for f in F if v in f]
 assert len(links)==6
 edge_links=Counter(u for e in links for u in e)
 assert len(edge_links)==6 and set(edge_links.values())=={2}
 # A 2-regular six-vertex graph could be two triangles; also check connectivity.
 reached={links[0][0]}
 while True:
  extended=reached|{b for a,b in links if a in reached}|{a for a,b in links if b in reached}
  if extended==reached:break
  reached=extended
 assert len(reached)==6, ('disconnected_link',v)
assert all(x==2 for x in E.values()) and len(E)==21 and len(F)==14
assert objs[tuple(range(N))].boundaries.rank()==13
print('All integral, chain, and surface checks complete')
