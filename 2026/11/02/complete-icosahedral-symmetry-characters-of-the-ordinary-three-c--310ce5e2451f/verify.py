#!/usr/bin/env python3
"""Exact finite checks for icosahedral ordinary three-cut homology characters.
Only Python standard library; independent of any external research package.
"""
import itertools
from collections import Counter, defaultdict
from fractions import Fraction

N=12
EDGES=((0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
(2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),
(4,5),(4,6),(4,10),(4,11),(5,6),(5,11),
(7,8),(7,9),(7,10),(7,11),(8,9),(9,10),(10,11))
V=tuple(range(N)); ADJ=[set() for _ in V]
for u,v in EDGES:ADJ[u].add(v);ADJ[v].add(u)
assert len(EDGES)==30 and all(len(x)==5 for x in ADJ)
assert all(sum(w in ADJ[u] for w in ADJ[v])==2 for v in V for u in ADJ[v])
assert len([t for t in itertools.combinations(V,3) if all(b in ADJ[a] for a,b in itertools.combinations(t,2))])==20

def bitmask(seq):return sum(1<<i for i in seq)
def is_connected_triple(t):
 a,b,c=t
 return (int(b in ADJ[a])+int(c in ADJ[a])+int(c in ADJ[b]))>=2
DIS=[bitmask(t) for t in itertools.combinations(V,3) if not is_connected_triple(t)]
assert len(DIS)==140
X=defaultdict(list);D=defaultdict(list)
for mask in range(1,1<<N):
 k=mask.bit_count()-1
 if any(mask & d == 0 for d in DIS):X[k].append(mask)
 if not any(mask & d==d for d in DIS):D[k].append(mask)
assert tuple(len(X[k]) for k in range(9)) == (12,66,220,495,792,924,792,465,140)
assert tuple(len(D[k]) for k in range(4)) == (12,66,80,30)
assert max(D)==3

def boundary(mask):
 vertices=[i for i in V if (mask>>i)&1]
 for q,u in enumerate(vertices): yield mask^(1<<u),(-1 if q%2 else 1)

def rat_rank(faces,k):
 if k==0:return 0
 ix={m:i for i,m in enumerate(faces[k-1])};basis={}
 for mask in faces[k]:
  col={ix[a]:Fraction(coef) for a,coef in boundary(mask)}
  while col:
   pv=max(col)
   if pv not in basis:
    factor=1/col[pv];basis[pv]={i:a*factor for i,a in col.items()}
    break
   factor=col[pv]
   for i,a in basis[pv].items():
    y=col.get(i,Fraction(0))-factor*a
    if y:col[i]=y
    else:col.pop(i,None)
 return len(basis)
assert (rat_rank(D,1),rat_rank(D,2),rat_rank(D,3))==(11,49,30)
# Combinatorial Alexander duality: reduced H_j(X;Q) = reduced H^(N-j-3)(D;Q).
assert (len(D[1])-11-49,len(D[2])-49-30)==(6,1)

P=1009
IDX={k:{s:j for j,s in enumerate(faces)} for k,faces in X.items()}
def sparse_subtract(x,factor,col):
 for j,a in col.items():
  z=(x.get(j,0)-factor*a)%P
  if z:x[j]=z
  else:x.pop(j,None)
def basis_add(basis,col):
 col={i:v%P for i,v in col.items() if v%P}
 while col:
  pv=max(col)
  if pv not in basis:
   z=pow(col[pv],-1,P)
   basis[pv]={i:a*z%P for i,a in col.items()}
   return True
  sparse_subtract(col,col[pv],basis[pv])
 return False

def reduce_by_basis(basis,col):
 col={i:v%P for i,v in col.items() if v%P}
 for pv in sorted(basis,reverse=True):
  if pv in col:sparse_subtract(col,col[pv],basis[pv])
 return col

B8={}
for s in X[8]:
 basis_add(B8,{IDX[7][t]:a for t,a in boundary(s)})
assert len(B8)==134
rank7={}
for s in X[7]:
 basis_add(rank7,{IDX[6][t]:a for t,a in boundary(s)})
assert len(rank7)==330
assert len(X[7])-len(rank7)-len(B8)==1

# Extract a cycle of degree 7 outside the degree-8 boundary image.
witness={};cycle=None
for j,s in enumerate(X[7]):
 col={IDX[6][t]:a%P for t,a in boundary(s)};comb={j:1}
 while col:
  pv=max(col)
  if pv not in witness:
   fac=pow(col[pv],-1,P)
   witness[pv]=({i:a*fac%P for i,a in col.items()},
                {i:a*fac%P for i,a in comb.items()})
   break
  fac=col[pv];boundary_column,combination=witness[pv]
  sparse_subtract(col,fac,boundary_column)
  sparse_subtract(comb,fac,combination)
 if not col and reduce_by_basis(B8,comb):
  cycle=comb
  break
assert cycle
zero_boundary={}
for j,coef in cycle.items():
 for target,sgn in boundary(X[7][j]):
  i=IDX[6][target]
  zero_boundary[i]=(zero_boundary.get(i,0)+coef*sgn)%P
assert all(v==0 for v in zero_boundary.values())
redcycle=reduce_by_basis(B8,cycle)

# Enumerate every automorphism by adjacency-preserving backtracking.
AUT=[];mapping={};used=set()
def enumerate_autos():
 if len(mapping)==N:
  AUT.append(tuple(mapping[i] for i in V));return
 unmapped=[i for i in V if i not in mapping]
 v=max(unmapped,key=lambda x:(len(ADJ[x]&mapping.keys()),-x))
 for candidate in V:
  if candidate in used:continue
  if any((u in ADJ[v]) != (mapping[u] in ADJ[candidate]) for u in mapping):continue
  mapping[v]=candidate;used.add(candidate)
  enumerate_autos()
  used.remove(candidate);del mapping[v]
enumerate_autos()
assert len(AUT)==120 and len(set(AUT))==120

def composition(a,b):return tuple(a[b[i]] for i in V)
def order(p):
 cur=tuple(V)
 for j in range(1,121):
  cur=composition(p,cur)
  if cur==V:return j
 raise AssertionError

def actmask(mask,p):
 vs=[p[i] for i in V if mask>>i&1]
 inversions=sum(vs[i]>vs[j] for i in range(len(vs)) for j in range(i+1,len(vs)))
 return bitmask(vs),(-1 if inversions%2 else 1)

def actcycle(p):
 target={}
 for j,a in cycle.items():
  newmask,sgn=actmask(X[7][j],p)
  ij=IDX[7][newmask]
  target[ij]=(target.get(ij,0)+a*sgn)%P
 return reduce_by_basis(B8,target)

def lef(p):
 return sum(((-1)**k)*sgn for k,f in X.items() for mask in f
            for tgt,sgn in [actmask(mask,p)] if tgt==mask)-1

# The icosahedral rotation group is generated by all odd-order automorphisms.
rotset={V};old=None
odds=[a for a in AUT if order(a)%2]
while len(rotset)!=old:
 old=len(rotset)
 for p in list(rotset):
  for g in odds:rotset.add(composition(p,g))
assert len(rotset)==60
assert Counter(order(p) for p in rotset)=={1:1,2:15,3:20,5:24}
assert Counter(order(p) for p in AUT if p not in rotset)=={2:16,6:20,10:24}
# Opposite vertices are the unique graph-distance-three points.
opp=[]
for i in V:
 dist={i:0};q=[i]
 for u in q:
  for w in ADJ[u]:
   if w not in dist:dist[w]=dist[u]+1;q.append(w)
 o=[j for j,d in dist.items() if d==3]
 assert len(o)==1
 opp.append(o[0])
opp=tuple(opp)
assert opp in AUT and opp not in rotset and order(opp)==2
assert all(composition(opp,g)==composition(g,opp) for g in AUT)

# Verify the generator transforms by +1 for rotations and -1 for inversion coset.
for p in AUT:
 tgt=actcycle(p)
 multiplier=1 if p in rotset else P-1
 assert tgt=={i:a*multiplier%P for i,a in redcycle.items()}

# All 120 signed fixed-simplex Lefschetz numbers, then degree-eight character.
TABLE=Counter()
for p in AUT:
 orientation=1 if p in rotset else -1
 chi7=orientation
 chi8=lef(p)+chi7
 TABLE[(orientation,order(p),chi7,chi8,lef(p))]+=1
EXPECTED={
 (1,1,1,6,5):1,(1,2,1,-2,-3):15,(1,3,1,0,-1):20,(1,5,1,1,0):24,
 (-1,2,-1,-6,-5):1,(-1,2,-1,2,3):15,(-1,6,-1,0,1):20,(-1,10,-1,-1,0):24
}
assert TABLE==EXPECTED,(TABLE,EXPECTED)
# The rotation character (6,-2,0,1,1) is the sum of the two 3-dimensional A5 characters.
# It contains no trivial constituent: weighted character average is zero.
assert (6+15*(-2)+20*0+24*1)==0
print('ICOSAHEDRAL_THREE_CUT_FULL_EQUIVARIANT_EXACT_OK')
print('face counts', [len(X[k]) for k in range(9)], 'Alexander dual',[len(D[k]) for k in range(4)])
print('ranks dual Q',(11,49,30),'ranks d7/d8 mod1009',(330,134),'aut',len(AUT))
print('H7 cycle support',len(cycle),'H7 sign checked on all',len(AUT),'automorphisms')
for key,count in sorted(TABLE.items()):print(count,key)
