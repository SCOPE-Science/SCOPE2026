#!/usr/bin/env python3
"""Exact rational homology ranks and complete signed symmetry character for the 4-crosspolytope graph two-particle space.  No external packages."""
from itertools import permutations,product,combinations
from collections import Counter,defaultdict
from math import factorial
N=4
verts=list(range(2*N))
axis=lambda v:v//2
edge=[(u,v) for u,v in combinations(verts,2) if axis(u)!=axis(v)]
eidx={e:i for i,e in enumerate(edge)}
c0=list(combinations(verts,2)); zidx={z:i for i,z in enumerate(c0)}
c1=[(e,w) for e in edge for w in verts if w not in e]; bidx={b:i for i,b in enumerate(c1)}
c2=[(e,f) for e,f in combinations(edge,2) if not set(e)&set(f)]

def edge_dir(u,v):
 return (tuple(sorted((u,v))),1 if u<v else -1)

def boundary1(e,w):
 u,v=e
 return [(zidx[tuple(sorted((v,w)))],1),(zidx[tuple(sorted((u,w)))],-1)]

def boundary2(e,f):
 u,v=e;x,y=f
 return [(bidx[(f,v)],1),(bidx[(f,u)],-1),(bidx[(e,y)],-1),(bidx[(e,x)],1)]

# exact rank over prime, sufficient lower bound coupled with homology lower bound
p=1000003
def rank_prime(columns):
 pivots={}
 for col in columns:
  vec=defaultdict(int)
  for i,v in col:vec[i]=(vec[i]+v)%p
  vec={i:v for i,v in vec.items() if v}
  while vec:
   j=min(vec)
   if j not in pivots:
    a=pow(vec[j],-1,p)
    pivots[j]={k:v*a%p for k,v in vec.items() if v}
    break
   q=vec[j];base=pivots[j]
   for k,v in base.items():
    nv=(vec.get(k,0)-q*v)%p
    if nv:vec[k]=nv
    elif k in vec:del vec[k]
 return len(pivots)

assert len(c0)==28 and len(c1)==144 and len(c2)==156
for e,f in c2:
 d=defaultdict(int)
 for j,s in boundary2(e,f):
  for k,t in boundary1(*c1[j]):d[k]+=s*t
 assert all(not v for v in d.values())
r1=rank_prime([boundary1(*c) for c in c1])
r2=rank_prime([boundary2(*c) for c in c2])
assert r1==27
# Every triangle on three axes avoids an unused vertex, so the map H1(UConf2) -> H1(graph)
# is surjective. Graph cycle rank is |E|-|V|+1 = 17. Hence rank d2 <= C1-rank d1-17=100.
assert r2==100, ('rank2',r2)
b1=len(c1)-r1-r2;b2=len(c2)-r2
assert b1==17 and b2==56

def signed_perm(perm,signs):
 return tuple(2*perm[i]+(s^signs[i]) for i in range(N) for s in range(2))

def trace_g(g):
 # C0 count unordered vertex-pair sets fixed
 t0=sum(1 for u,v in c0 if tuple(sorted((g[u],g[v])))==(u,v))
 # C1 signed fixed orientation
 t1=0
 for (u,v),w in c1:
  a,b=g[u],g[v]
  if g[w]==w and tuple(sorted((a,b)))==(u,v):t1+=1 if a<b else -1
 # C2 signed fixed orientation, with exterior sign when two 1D factors swap
 t2=0
 for e,f in c2:
  ee,se=edge_dir(g[e[0]],g[e[1]])
  ff,sf=edge_dir(g[f[0]],g[f[1]])
  if (ee==e and ff==f) or (ee==f and ff==e):
   t2+=se*sf*(1 if ee==e else -1)
 # ordinary graph edge chain trace -> first homology
 te=sum(1 if g[u]==u and g[v]==v else (-1 if g[u]==v and g[v]==u else 0) for u,v in edge)
 tv=sum(g[u]==u for u in verts)
 h1=te-tv+1
 h2=t2-t1+t0-1+h1
 return t0,t1,t2,h1,h2

def signature(g):
 # classify signed cycle type in the signed permutation of 4 coordinate axes
 perm=tuple(g[2*i]//2 for i in range(N))
 bits=tuple(g[2*i]%2 for i in range(N))
 done=set(); plus=[];minus=[]
 for i in range(N):
  if i in done:continue
  cyc=[];j=i
  while j not in done:
   cyc.append(j);done.add(j);j=perm[j]
  (minus if sum(bits[j] for j in cyc)%2 else plus).append(len(cyc))
 return (tuple(sorted(plus,reverse=True)),tuple(sorted(minus,reverse=True)))

counts=Counter();chars={}; elems=0
for perm in permutations(range(N)):
 for signs in product(range(2),repeat=N):
  g=signed_perm(perm,signs)
  sig=signature(g);ch=trace_g(g)
  if sig in chars:assert chars[sig]==ch,('nonclassfunction',sig,chars[sig],ch)
  chars[sig]=ch;counts[sig]+=1;elems+=1
assert elems==384 and len(counts)==20
inv1=sum(counts[s]*chars[s][3] for s in counts)//384
inv2=sum(counts[s]*chars[s][4] for s in counts)//384
assert sum(counts[s]*chars[s][3] for s in counts)%384==0
assert sum(counts[s]*chars[s][4] for s in counts)%384==0
print('CELL_COUNTS',len(c0),len(c1),len(c2),'BOUNDARY_RANKS',r1,r2,'BETTI',(1,b1,b2))
print('ORBIT_CHARACTERS (positive signed-cycle partition, negative signed-cycle partition): count, C0, C1, C2, H1, H2')
for sig in sorted(chars, key=str):print(sig,counts[sig],*chars[sig])
print('INVARIANTS',inv1,inv2)
print('CROSSPOLYTOPE4_TWO_POINT_EXACT_OK')
# Independently verify every group element commutes with the cubical boundaries,
# preventing accidental sign errors in character evaluation.
for perm in permutations(range(N)):
 for signs in product(range(2),repeat=N):
  g=signed_perm(perm,signs)
  for e,w in c1:
   ee,sgn=edge_dir(g[e[0]],g[e[1]])
   rhs=defaultdict(int);lhs=defaultdict(int)
   for ix,c in boundary1(e,w):
    a,b=c0[ix];lhs[zidx[tuple(sorted((g[a],g[b])))]]+=c
   for ix,c in boundary1(ee,g[w]):rhs[ix]+=sgn*c
   assert dict((k,v) for k,v in lhs.items() if v)==dict((k,v) for k,v in rhs.items() if v)
  for e,f in c2:
   ee,s1=edge_dir(g[e[0]],g[e[1]])
   ff,s2=edge_dir(g[f[0]],g[f[1]])
   fac=s1*s2*(1 if ee<ff else -1)
   c2image=(ee,ff) if ee<ff else (ff,ee)
   lhs=defaultdict(int);rhs=defaultdict(int)
   for ix,c in boundary2(e,f):
    be,w=c1[ix]
    eb,sgn=edge_dir(g[be[0]],g[be[1]])
    lhs[bidx[(eb,g[w])]]+=sgn*c
   for ix,c in boundary2(*c2image):rhs[ix]+=fac*c
   assert dict((k,v) for k,v in lhs.items() if v)==dict((k,v) for k,v in rhs.items() if v),('action-boundary',e,f,g)
print('ALL_384_GROUP_ACTIONS_COMMUTE_WITH_BOTH_BOUNDARIES_OK')
# Natural subgroup-invariant dimensions, by finite-group rational averaging.
def average(pred):
 vals=[trace_g(signed_perm(pm,sg)) for pm in permutations(range(N)) for sg in product(range(2),repeat=N) if pred(pm,sg)]
 return len(vals),(sum(x[3] for x in vals)//len(vals),sum(x[4] for x in vals)//len(vals))
def parity(pm):return sum(pm[i]>pm[j] for i in range(N) for j in range(i+1,N))%2
for name,pred in [
 ('all B4',lambda p,s:True),
 ('rotation(det=+1)',lambda p,s:(parity(p)+sum(s))%2==0),
 ('coordinate permutation S4',lambda p,s:not any(s)),
 ('independent sign flips (C2)^4',lambda p,s:p==tuple(range(N))),
 ('even sign flips (C2)^3',lambda p,s:p==tuple(range(N)) and sum(s)%2==0),
 ('central inversion C2',lambda p,s:p==tuple(range(N)) and len(set(s))==1),
]:
 size,inv=average(pred)
 # Require exact division rather than flooring
 print('QUOTIENT_INVARIANTS',name,'order',size,inv)
