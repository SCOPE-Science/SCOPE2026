# Independent verification via invariant-subspace enumeration before orbit decomposition.
from itertools import product
from collections import Counter,defaultdict
from sympy import symbols,Poly,groebner
from time import monotonic
start=monotonic()
x,y,z=symbols('x y z'); vars=(x,y,z)
mons=[(4-a-b,a,b) for b in range(5) for a in range(5-b)]
idx={e:i for i,e in enumerate(mons)}
B=[x**e[0]*y**e[1]*z**e[2] for e in mons]
pts=list(range(1,8))
def inner(p,q):return (p&q).bit_count()%2
def im(m,p):return sum(inner(m[i],p)<<i for i in range(3))
GL=[m for m in product(pts,repeat=3) if set(im(m,p) for p in pts)==set(pts)]
assert len(GL)==168
identity=(1,2,4)
elations={p:[] for p in pts}
for p in pts:
 for w in pts:
  if inner(p,w)!=0:continue
  mat=tuple((1<<i) ^ (w if ((p>>i)&1) else 0) for i in range(3))
  assert mat in GL and mat!=identity
  elations[p].append(mat)
 assert len(elations[p])==3

def columns(m):
 substitution=dict(zip(vars, [sum(vars[j] for j in range(3) if (row>>j)&1) for row in m]))
 cols=[]
 for b in B:
  expr=Poly(b.subs(substitution, simultaneous=True),vars,modulus=2)
  v=0
  for e,c in expr.terms():
   if int(c)%2:v|=1<<idx[e]
  cols.append(v)
 return cols
act={m:columns(m) for m in GL}
def replace(m,bits):
 out=0
 for i in range(15):
  if bits>>i &1:out ^= act[m][i]
 return out
# Using only central elations, find all forms admitting some rational arithmetic fiberwise symmetry.
trans={m for l in elations.values() for m in l}
assert len(trans)==21
candidates=set()
for t in trans:
 for f in range(1,1<<15):
  if replace(t,f)==f:candidates.add(f)
print('invariant candidates',len(candidates),'in',round(monotonic()-start,1),'s',flush=True)

def val(f,p):return sum(1 for i,e in enumerate(mons) if f>>i&1 and all((not exp) or (p>>j&1) for j,exp in enumerate(e)))%2

def smooth(f):
 f0=sum(B[i] for i in range(15) if f>>i&1)
 for k in range(3):
  others=[vars[i] for i in range(3) if i!=k]
  ff=Poly(f0.subs(vars[k],1),others,modulus=2).as_expr()
  g=groebner([ff,ff.diff(others[0]),ff.diff(others[1])],*others,order='lex',modulus=2)
  if len(g.polys)!=1 or g.polys[0].as_expr()!=1:return False
 return True

# A smooth transvection-invariant quartic cannot pass through its center; prefilter impossibilities.
possible=[f for f in candidates if all(val(f,p) for p in pts if any(replace(t,f)==f for t in elations[p]))]
print('possible',len(possible),'in',round(monotonic()-start,1),'s',flush=True)
S={f for f in possible if smooth(f)}
print('smooth candidate equations',len(S),'in',round(monotonic()-start,1),'s',flush=True)
assert len(S)==1184
# All candidate orbits are entirely contained in S, by coordinate invariance.
remaining=S.copy();orb=[];counts=Counter();galois=Counter();Ncounts=Counter()
while remaining:
 f=min(remaining)
 orbit={replace(g,f) for g in GL}
 assert orbit<=S
 remaining-=orbit
 qcounts=[sum(replace(t,f)==f for t in elations[p]) for p in pts]
 n2=qcounts.count(1)
 n4=qcounts.count(3)
 assert all(q in (0,1,3) for q in qcounts)
 N=sum(1-val(f,p) for p in pts)
 counts[(n2,n4)]+=1
 Ncounts[(n2,n4,N)]+=1
 galois[n4]+=1
 orb.append((f,len(orbit),n2,n4,N))
print('orbits',len(orb),'by (C2 centers,V4 centers)',sorted(counts.items()))
print('galois center counts classes',sorted(galois.items()))
print('full table',sorted(Ncounts.items()))
print('overall',len(S),sum(x[1] for x in orb),'time',round(monotonic()-start,1))
import json
json.dump({'orbit_representatives':sorted(orb),'class_profiles':[(list(k),v) for k,v in sorted(Ncounts.items())], 'equations':len(S), 'classes':len(orb),'fixed_subspaces':len(candidates)},open('independent.json','w'),indent=2)
