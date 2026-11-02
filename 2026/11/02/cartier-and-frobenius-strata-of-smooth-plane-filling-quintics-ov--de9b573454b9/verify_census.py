import itertools,collections,time
import sympy as sp
start=time.time()
d=5
exps=[(a,b,d-a-b) for a in range(d,-1,-1) for b in range(d-a,-1,-1)]
assert len(exps)==21
inds={e:i for i,e in enumerate(exps)}
pts=[p for p in itertools.product((0,1),repeat=3) if any(p)]
def dot(e,p): return int(all(not (x and not y) for x,y in zip(e,p)))
E=[sum(dot(e,p)<<i for i,e in enumerate(exps)) for p in pts]
def parity(n):return n.bit_count()&1
# nullspace basis F2 rref
rows=E[:]; piv=[];r=0
for col in range(21):
 k=next((i for i in range(r,7) if rows[i]>>col&1),None)
 if k is None:continue
 rows[r],rows[k]=rows[k],rows[r]
 for i in range(7):
  if i!=r and rows[i]>>col&1:rows[i]^=rows[r]
 piv.append(col);r+=1
assert r==7
basis=[]
for f in range(21):
 if f in piv:continue
 v=1<<f
 for i,p in enumerate(piv):
  if rows[i]>>f&1:v^=1<<p
 assert all(not parity(e&v) for e in E)
 basis.append(v)
assert len(basis)==14
valid=[0]
for b in basis:valid.extend([x^b for x in valid])
assert len(set(valid))==16384
# gradients at rational pts
grad=[]
for p in pts:
 grad.append([sum((((e[k]&1)*dot(tuple(e[j]-(j==k) for j in range(3)),p))<<i) for i,e in enumerate(exps) if e[k]&1) for k in range(3)])
def tangent(mask,pi):
 g=tuple(parity(mask&b) for b in grad[pi])
 return g
covers=[{q for q in pts if parity(sum((a*b)<<i for i,(a,b) in enumerate(zip(g,q))))==0} for g in pts]
counts=collections.Counter(); covers_by_size=collections.Counter();nonzero=[]
for mask in valid[1:]:
 gs=[tangent(mask,pi) for pi in range(7)]
 if any(g==(0,0,0) for g in gs):continue
 lines=set(gs)
 u=set().union(*(covers[pts.index(g)] for g in lines))
 covers_by_size[len(u)]+=1
 counts[(len(u),len(lines))]+=1
 nonzero.append(mask)
print('all tangent-smooth rational curves',len(nonzero),'coverage stats',covers_by_size,'coverage,line stats',counts,'elapsed',time.time()-start,flush=True)
# group generators projective coordinate change represented images of X,Y,Z
trans=[[(0,1,0),(1,0,0),(0,0,1)],[(0,1,0),(0,0,1),(1,0,0)],[(1,1,0),(0,1,0),(0,0,1)]]
def multiply(A,B):
 C={}
 for x,a in A.items():
  for y,b in B.items():
   z=tuple(x[i]+y[i] for i in range(3));C[z]=C.get(z,0)^(a&b)
 return {x:v for x,v in C.items() if v}
gens=[]
for subst in trans:
  # precompute degree <= 5 powers directly
 def mon_sub(e):
  p={(0,0,0):1}
  for k in range(3):
   for _ in range(e[k]):
    p=multiply(p,{tuple(int(i==j) for i in range(3)):1 for j,v in enumerate(subst[k]) if v})
  return sum(1<<inds[e1] for e1 in p)
 gens.append([mon_sub(e) for e in exps])
def transform(mask,g):
 z=0
 while mask:
  bit=mask&-mask;i=bit.bit_length()-1
  z^=g[i];mask^=bit
 return z
unseen=set(nonzero);orbs=[]
while unseen:
 rep=min(unseen);orb={rep};todo=[rep]
 while todo:
  m=todo.pop()
  for g in gens:
   v=transform(m,g)
   if v not in orb:orb.add(v);todo.append(v)
 if not orb<=set(nonzero):raise ValueError('not invariant')
 unseen.difference_update(orb)
 orbs.append((rep,len(orb)))
print('pointwise smooth orbits',len(orbs),collections.Counter(x[1] for x in orbs),'elapsed',time.time()-start,flush=True)
S,T,U=sp.symbols('S T U');monoms=[S**a*T**b*U**c for a,b,c in exps]
def smooth(mask):
 F=sum(monoms[i] for i in range(21) if mask>>i&1)
 for a in (S,T,U):
  vars=[x for x in (S,T,U) if x!=a]
  f=F.subs(a,1)
  gb=sp.groebner([f]+[sp.diff(f,v) for v in vars],*vars,modulus=2)
  if list(gb)!=[1]:return False
 return True
smooth_orbs=[]
for rep,sz in orbs:
 if smooth(rep):
  gs=[tangent(rep,i) for i in range(7)]
  lines=set(gs);u=set().union(*(covers[pts.index(g)] for g in lines))
  smooth_orbs.append((rep,sz,len(lines),len(u)))
print('smooth orbits',len(smooth_orbs),'curves',sum(s for _,s,_,_ in smooth_orbs),'strata',collections.Counter((ll,cv) for _,sz,ll,cv in smooth_orbs for _ in range(sz)),'reps',smooth_orbs,'elapsed',time.time()-start,flush=True)
# Independently evaluate the Cartier/Manin matrices from degree-five coefficients.
indices=[(i,j) for i in range(3) for j in range(3-i)]
def gf2_rank(rows):
 rows=list(rows);p=0
 for col in range(6):
  idx=next((v for v in range(p,6) if (rows[v]>>col)&1),None)
  if idx is None:continue
  rows[idx],rows[p]=rows[p],rows[idx]
  for v in range(6):
   if v!=p and ((rows[v]>>col)&1):rows[v]^=rows[p]
  p+=1
 return p
def product(A,B):
 out=[]
 for row in A:
  accum=0
  for k in range(6):
   if row>>k&1:accum^=B[k]
  out.append(accum)
 return out
rank_info=[]
for mask,orbit,tangent_lines,coverage in smooth_orbs:
 monomial_set={e for i,e in enumerate(exps) if mask>>i&1}
 H=[]
 for i,j in indices:
  r=0
  for col,(k,l) in enumerate(indices):
   a=2*k-i+1;b=2*l-j+1;c=5-a-b
   if (a,b,c) in monomial_set:r|=1<<col
  H.append(r)
 P=H
 for _ in range(5):P=product(P,H)
 a=6-gf2_rank(H);p=gf2_rank(P)
 rank_info.append((mask,orbit,tangent_lines,p,a))
print('RANK_INFO',rank_info,flush=True)
assert rank_info==[
(213034,168,5,2,3),(213150,84,6,6,0),(213334,168,4,6,0),
(213658,168,6,6,0),(213756,168,6,6,0),(215182,168,5,5,1),
(215210,168,5,2,1),(215310,168,5,6,0),(215482,84,5,2,1),
(221388,168,5,5,1)]
strata=collections.Counter()
for mask,orbit,tangent_lines,p,a in rank_info:strata[(p,a)]+=orbit
assert strata=={(2,3):168,(2,1):252,(5,1):336,(6,0):756}
print('CENSUS_CARTIER_VERIFY_OK',strata)
