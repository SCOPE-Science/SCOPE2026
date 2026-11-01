#!/usr/bin/env python3
"""Exact simplicial and signed fixed-face checks for Q4 independence topology."""
from itertools import permutations
from collections import defaultdict, Counter

N=16
E={tuple(sorted((v,v^(1<<j)))) for v in range(N) for j in range(4)}
faces=sorted((s for s in range(1<<N) if all(not ((s>>a&1) and (s>>b&1)) for a,b in E)), key=lambda s:(s.bit_count(),s))
by_size={k:[s for s in faces if s.bit_count()==k] for k in range(9)}
assert len(faces)==743 and len(E)==32
fvector=tuple(len(by_size[k]) for k in range(9))
assert fvector==(1,16,88,208,228,128,56,16,2),fvector

def binary_rank(cols):
 piv={}
 for x in cols:
  while x:
   p=x.bit_length()-1
   if p not in piv:
    piv[p]=x;break
   x^=piv[p]
 return len(piv)

ranks={0:1}
for k in range(2,9):
 rows={m:j for j,m in enumerate(by_size[k-1])}
 cols=[]
 for m in by_size[k]:
  col=0
  for j in range(N):
   if m>>j&1:
    col^=1<<rows[m^(1<<j)]
  cols.append(col)
 ranks[k-1]=binary_rank(cols)
ranks[8]=0
betti={k-1:len(by_size[k])-ranks[k-1]-ranks[k] for k in range(1,9)}
assert betti=={0:0,1:0,2:0,3:7,4:0,5:0,6:0,7:0},(ranks,betti)

def action(p,b):
 return tuple(b^sum(((v>>j)&1)<<p[j] for j in range(4)) for v in range(N))

def direct_face_trace(g):
 z=0
 for s in faces:
  verts=[v for v in range(N) if s>>v&1]
  img=[g[v] for v in verts]
  if set(verts)!=set(img):continue
  inv=sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))
  z+=(-1)**(len(verts)+inv)
 return z

def orbit_trace(g):
 seen=set(); orbit=[]
 for v in range(N):
  if v in seen:continue
  cyc=[];u=v
  while u not in seen:
   seen.add(u);cyc.append(u);u=g[u]
  s=sum(1<<j for j in cyc)
  if s in face_set: orbit.append(s)
 count=0
 for m in range(1<<len(orbit)):
  union=0
  for j,O in enumerate(orbit):
   if m>>j&1: union|=O
  if union in face_set:count+=(-1)**m.bit_count()
 return count

face_set=set(faces)
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
def predicted(p,b):
 fixed=[j for j in range(4) if p[j]==j]
 return sign(p)*(len(fixed)-1+sum((-1)**(b&~(1<<j)).bit_count() for j in fixed))

def type_of(p,b):
 out=[];seen=set()
 for i in range(4):
  if i in seen:continue
  cyc=[];j=i
  while j not in seen:
   cyc.append(j);seen.add(j);j=p[j]
  out.append((len(cyc),sum((b>>p[j])&1 for j in cyc)%2))
 return tuple(sorted(out))

classes=defaultdict(list)
for p in permutations(range(4)):
 for b in range(16):
  g=action(p,b)
  direct=direct_face_trace(g)
  orbit=orbit_trace(g)
  closed=predicted(p,b)
  assert direct==orbit==closed, (p,b,direct,orbit,closed)
  classes[type_of(p,b)].append(direct)
assert len(classes)==20
assert all(len(set(z))==1 for z in classes.values())

# Restriction to the 16-element translation subgroup and its character Fourier transform.
trans=[direct_face_trace(action(tuple(range(4)),b)) for b in range(16)]
assert [len([b for b in range(16) if b.bit_count()==k]) for k in range(5)]==[1,4,6,4,1]
assert [trans[2**k-1] for k in range(5)]==[7,1,3,5,-1]
mult={A:sum((-1)**(A&b).bit_count()*trans[b] for b in range(16))//16 for A in range(16)}
assert [mult[A] for A in range(16)]==[3 if A==0 else (1 if A.bit_count()==3 else 0) for A in range(16)]
for p in permutations(range(4)):
 t0=sum(direct_face_trace(action(p,b)) for b in range(16))//16
 assert t0==sign(p)*(sum(p[j]==j for j in range(4))-1)
 if p[3]==3:
  t3=sum((-1)**(b&7).bit_count()*direct_face_trace(action(p,b)) for b in range(16))//16
  assert t3==sign(p)

print('Q4_INDEPENDENCE_SYMMETRY_VERIFIED')
print('independence_faces_by_cardinality:',fvector)
print('augmented_boundary_ranks_mod2:',[ranks[i] for i in range(9)])
print('reduced_mod2_betti_by_degree:',[betti[i] for i in range(8)])
print('automorphisms: 384; signed classes:',len(classes),'all three character methods agree')
print('translation_trace_by_weight:',[trans[2**k-1] for k in range(5)])
print('translation_fourier_dimensions:',Counter((A.bit_count(),mult[A]) for A in range(16)))
print('signed_class_table: [(cycle_length, parity_bit) tuples, class_size, trace]')
for name,ls in sorted(classes.items()):
 print(name,len(ls),ls[0])
