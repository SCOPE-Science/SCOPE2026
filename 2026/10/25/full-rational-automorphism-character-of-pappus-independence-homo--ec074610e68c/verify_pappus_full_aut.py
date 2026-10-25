#!/usr/bin/env python3
"""Exact integral-valued character computation for the Pappus independence complex.
Requires Python 3.10+ standard library only. Verifies every automorphism and every face.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations

N=18
LCF=(5,7,-7,7,-7,-5)*3
ADJ=[0]*N
for i in range(N):
 for j in ((i+1)%N,(i+LCF[i])%N):
  ADJ[i]|=1<<j;ADJ[j]|=1<<i
assert all(a.bit_count()==3 for a in ADJ) and sum(a.bit_count() for a in ADJ)==54

def auts():
 p=[-1]*N;used=0;ans=[]
 def walk(k):
  nonlocal used
  if k==N:
   ans.append(tuple(p));return
  avail=[x for x in range(N) if p[x]<0]
  x=max(avail,key=lambda x:(sum(p[y]>=0 for y in range(N) if ADJ[x]>>y&1),-x))
  mapped=[z for z in range(N) if p[z]>=0]
  for y in range(N):
   if used>>y&1:continue
   if any(((ADJ[x]>>z)&1)!=((ADJ[y]>>p[z])&1) for z in mapped):continue
   p[x]=y;used^=1<<y;walk(k+1);used^=1<<y;p[x]=-1
 walk(0)
 return sorted(ans)
PERMS=auts()
assert len(PERMS)==216 and len(set(PERMS))==216
KEY={p:i for i,p in enumerate(PERMS)}
ID=tuple(range(N));assert ID in KEY

def compose(p,q):return tuple(p[q[i]] for i in range(N))
def inverse(p):
 q=[0]*N
 for i,j in enumerate(p):q[j]=i
 return tuple(q)

def orbit_blocks(p):
 unseen=set(range(N)); blocks=[]
 while unseen:
  v=min(unseen);b=[];u=v
  while u in unseen:
   unseen.remove(u);b.append(u);u=p[u]
  assert u==v
  blocks.append(tuple(b))
 return blocks

def signed_lefschetz(p):
 # Sum signed simplicial traces, including augmented degree -1.
 blocks=[b for b in orbit_blocks(p) if all(not (ADJ[x]>>y&1) for x,y in combinations(b,2))]
 m=len(blocks);conflict=[0]*m
 for i in range(m):
  for j in range(i+1,m):
   if any((ADJ[x]>>y)&1 for x in blocks[i] for y in blocks[j]):
    conflict[i]|=1<<j;conflict[j]|=1<<i
 memo={0:1}
 def f(rem):
  if rem in memo:return memo[rem]
  bit=rem&-rem;i=bit.bit_length()-1
  memo[rem]=f(rem^bit)-f((rem^bit)&~conflict[i])
  return memo[rem]
 return -f((1<<m)-1)

# Indep faces; boundary ranks of augmented chain complex over F_2.
faces=[0]
for v in range(N):faces += [s|(1<<v) for s in list(faces) if not(s&ADJ[v])]
assert len(faces)==2598
by=defaultdict(list)
for s in faces:by[s.bit_count()].append(s)
assert [len(by[k]) for k in range(10)]==[1,18,126,438,801,756,348,90,18,2]
R={}
for k in range(1,10):
 lookup={s:i for i,s in enumerate(by[k-1])};piv={}
 for s in by[k]:
  t=s;col=0
  while t:
   b=t&-t;t-=b;col^=1<<lookup[s^b]
  while col:
   idx=col.bit_length()-1
   if idx not in piv:piv[idx]=col;break
   col^=piv[idx]
 R[k]=len(piv)
assert [R[k] for k in range(1,10)]==[1,17,109,329,472,274,74,16,2]
assert {k-1:len(by[k])-R.get(k,0)-R.get(k+1,0) for k in range(10) if len(by[k])-R.get(k,0)-R.get(k+1,0)}=={4:10}

# Full group conjugacy classes and character.
CHI={p:signed_lefschetz(p) for p in PERMS}
assert CHI[ID]==10
unseen=set(PERMS);classes=[]
while unseen:
 g=min(unseen)
 C={compose(compose(h,g),inverse(h)) for h in PERMS}
 assert len({CHI[h] for h in C})==1
 classes.append(C);unseen.difference_update(C)
assert len(classes)==13 and not unseen
classes.sort(key=lambda C:(min(C)==ID, min(C)))
# Identify conjugacy classes using size, order, bipartition swap, and representative.
assert sum(len(C) for C in classes)==216
CC={x:i for i,C in enumerate(classes) for x in C}
REP=[min(C) for C in classes]

# Claimed irreducible character constituents by conjugacy signature.
# Their evaluations are given by a table indexed by:
# (class size, order, bipartition swap, Pappus Lefschetz trace, vertex cycle type).
SIG=[]
def order(p):
 t=ID
 for k in range(1,217):
  t=compose(p,t)
  if t==ID:return k
 raise AssertionError('order > 216')
for C,r in zip(classes,REP):
 cy=tuple(sorted(Counter(len(b) for b in orbit_blocks(r)).items()))
 SIG.append((len(C),order(r),r[0]%2,CHI[r],cy))
# Distinct signatures except the two order-12 classes: both have the same character values.
BASE={
 (18,2,0,2,((1,4),(2,7))):(2,0),
 (9,2,0,-2,((1,6),(2,6))):(0,-2),
 (1,1,0,10,((1,18),)):(4,6),
 (36,6,0,-1,((1,1),(2,1),(3,1),(6,2))):(-1,0),
 (12,3,0,1,((1,3),(3,5))):(1,0),
 (18,4,1,2,((2,3),(4,3))):(0,2),
 (18,2,1,0,((2,9),)):(0,0),
 (18,12,1,-1,((6,1),(12,1))):(0,-1),
 (36,6,1,0,((6,3),)):(0,0),
 (18,6,0,1,((3,2),(6,2))):(0,1),
 (12,3,0,-2,((3,6),)):(-2,0),
 (2,3,0,1,((3,6),)):(4,-3),
}
assert all(sig in BASE for sig in SIG),(SIG,BASE)
assert len(SIG)==13
psi4=[BASE[s][0] for s in SIG]
psi6=[BASE[s][1] for s in SIG]
assert all(psi4[k]+psi6[k]==CHI[REP[k]] for k in range(13))
for degree,psi in [(4,psi4),(6,psi6)]:
 assert psi[SIG.index((1,1,0,10,((1,18),)))]==degree
 assert sum(len(C)*psi[k] for k,C in enumerate(classes))==0
 assert sum(len(C)*psi[k]**2 for k,C in enumerate(classes))==216
# Finite class-algebra multiplication checks: the 2 functions define
# irreducible central characters (center of Q[G]), not fitted curves.
for degree,psi in [(4,psi4),(6,psi6)]:
 lamb=[Fraction(len(classes[k])*psi[k],degree) for k in range(13)]
 for i,C in enumerate(classes):
  for j,D in enumerate(classes):
   count=Counter(CC[compose(a,b)] for a in C for b in D)
   rhs=sum(Fraction(count[k],len(classes[k]))*lamb[k] for k in count)
   assert rhs==lamb[i]*lamb[j]
# Completeness and augmentation.
assert sum(len(C)*CHI[REP[i]] for i,C in enumerate(classes))==0
assert sum(len(C)*CHI[REP[i]]**2 for i,C in enumerate(classes))==432
print('PAPPUS_FULL_216_AUTOMORPHISM_CHARACTER_VERIFIED')
print('vertices=18 edges=27 nonempty_faces=2597 conjugacy_classes=13')
print('mod2_reduced_betti={4:10} rational_character=4_plus_6_irreducible')
for i in range(13):
 print('class',i+1,'signature',SIG[i],'psi4',psi4[i],'psi6',psi6[i])

# Independent direct oriented-face trace check, not using cycle-orbit reductions.
# Every setwise fixed simplex contributes its induced orientation sign.
def direct_character(p):
 total=0
 for face in faces:
  mapped=0; arr=[]
  for v in range(N):
   if face>>v&1:
    mapped|=1<<p[v];arr.append(p[v])
  if mapped!=face:continue
  inv=sum(a>b for i,a in enumerate(arr) for b in arr[i+1:])
  total+=(-1 if len(arr)%2==0 else 1)*(-1 if inv%2 else 1)
 return total
assert all(direct_character(g)==CHI[g] for g in PERMS)
print('PAPPUS_DIRECT_SIGNED_TRACE_ALL_216_VERIFIED')
