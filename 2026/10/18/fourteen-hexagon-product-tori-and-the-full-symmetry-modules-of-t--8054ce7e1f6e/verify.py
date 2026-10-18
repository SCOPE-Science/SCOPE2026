#!/usr/bin/env python3
"""Reproduce the Heawood two-particle homology and symmetry calculations.
Requires Python 3, numpy and sympy. Run alongside CERTIFICATE.json.
"""
from collections import Counter,defaultdict
from itertools import combinations,permutations
from math import lcm
from pathlib import Path
import json
import numpy as np
from sympy import Matrix

K=json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text(encoding='utf-8'))
V=list(range(14))
E=sorted((p,7+j) for j in range(7) for p in {(j+d)%7 for d in (0,1,3)})
EID={e:i for i,e in enumerate(E)}
C0=list(combinations(V,2)); C0id={z:i for i,z in enumerate(C0)}
C1=[(i,w) for i,(a,b) in enumerate(E) for w in V if w not in (a,b)]
C1id={z:i for i,z in enumerate(C1)}
C2=[(i,j) for i,(a,b) in enumerate(E) for j in range(i+1,len(E)) if not {a,b}.intersection(E[j])]
C2id={z:i for i,z in enumerate(C2)}
assert (len(C0),len(C1),len(C2))==(91,252,168)
d1=[]
for i,w in C1:
 a,b=E[i]
 d1.append({C0id[tuple(sorted((b,w)))]:1,C0id[tuple(sorted((a,w)))]:-1})
d2=[]
for i,j in C2:
 a,b=E[i];c,d=E[j]
 d2.append({C1id[(j,b)]:1,C1id[(j,a)]:-1,C1id[(i,d)]:-1,C1id[(i,c)]:1})
for column in d2:
 total=defaultdict(int)
 for r,x in column.items():
  for z,y in d1[r].items():total[z]+=x*y
 assert all(y==0 for y in total.values())

# Tree-reduced integer boundary, using only non-tree 1-cells as cycle coordinates.
uf=list(range(len(C0)))
def root(x):
 while x!=uf[x]:uf[x]=uf[uf[x]];x=uf[x]
 return x
tree=set()
for j,col in enumerate(d1):
 a,b=col
 ra,rb=root(a),root(b)
 if ra!=rb:uf[ra]=rb;tree.add(j)
assert len(tree)==90
non_tree=[j for j in range(len(C1)) if j not in tree]
assert len(non_tree)==162
index={j:i for i,j in enumerate(non_tree)}
B=np.zeros((162,168),dtype=np.int64)
for j,col in enumerate(d2):
 for row,coeff in col.items():
  if row in index:B[index[row],j]=coeff
assert np.count_nonzero(B)==430

# A nonzero 154-by-154 integer minor of determinant 2, plus mod-two rank 153.
rr=K['boundary_minor_rows'];cc=K['boundary_minor_cols']
assert len(rr)==len(cc)==154 and len(set(rr))==len(set(cc))==154
det=int(Matrix(B[np.ix_(rr,cc)].tolist()).det(method='domain-ge'))
assert det==2,('determinant',det)
def rank_sparse_mod2(columns):
 basis={}
 for col in columns:
  v=sum(1<<int(r) for r in col if col[r]%2)
  while v:
   bit=v.bit_length()-1
   if bit not in basis:basis[bit]=v;break
   v^=basis[bit]
 return len(basis)
rank2=rank_sparse_mod2([{i:int(B[i,j]) for i in np.flatnonzero(B[:,j])} for j in range(168)])
assert rank2==153,rank2

# Distinct 6-cycles bound disjoint embedded Cartesian-product tori.
def signed_cycle(seq):
 assert len(seq)==6 and len(set(seq))==6
 edges={}
 for a,b in zip(seq,seq[1:]+seq[:1]):
  e=tuple(sorted((a,b)))
  assert e in EID,(seq,e)
  i=EID[e]
  edges[i]=edges.get(i,0)+(1 if a<b else -1)
 assert len(edges)==6
 return edges
M=np.zeros((168,14),dtype=np.int64)
for j,(a,b) in enumerate(K['torus_cycles']):
 assert set(a).isdisjoint(b)
 aa=signed_cycle(a);bb=signed_cycle(b)
 for e,sgn in aa.items():
  for f,tgn in bb.items():
   ii,jj=sorted((e,f))
   M[C2id[(ii,jj)],j]+=sgn*tgn*(1 if e<f else -1)
 for row in range(len(C1)):
  assert sum(int(M[k,j])*d2[k].get(row,0) for k in np.flatnonzero(M[:,j]))==0
minorrows=K['torus_minor_rows']
assert len(minorrows)==14 and len(set(minorrows))==14
mdet=int(Matrix(M[minorrows,:].tolist()).det(method='domain-ge'))
assert abs(mdet)==1,mdet
# The unit minor and the rank-154 boundary minor imply a full integral basis of H2.
# The determinant-2 minor and mod-two rank drop force H1 torsion Z/2 exactly.

# All 336 graph automorphisms; 168 Fano collineations and 168 dualities.
lines=[frozenset((j+d)%7 for d in (0,1,3)) for j in range(7)]
lineindex={ln:i for i,ln in enumerate(lines)}
good=[]
for pp in permutations(range(7)):
 if all(frozenset(pp[k] for k in ln) in lineindex for ln in lines):
  lperm=tuple(7+lineindex[frozenset(pp[k] for k in ln)] for ln in lines)
  good.append(pp+lperm)
assert len(good)==168
polarity=tuple(7+(-p)%7 for p in range(7))+tuple((-j)%7 for j in range(7))
G=good+[tuple(g[polarity[k]] for k in V) for g in good]
assert len(G)==len(set(G))==336

def trace(g):
 vfix=sum(g[v]==v for v in V)
 pointpairs=sum(tuple(sorted((g[a],g[b])))==(a,b) for a,b in C0)
 edgeimgs=[]
 for (a,b) in E:
  x,y=g[a],g[b]
  edgeimgs.append((EID[tuple(sorted((x,y)))],1 if x<y else -1))
 tgraph1=sum(sign for i,(j,sign) in enumerate(edgeimgs) if i==j)
 tcell1=sum(sign for i,w in C1 for (j,sign) in [edgeimgs[i]] if i==j and g[w]==w)
 tcell2=0
 for i,j in C2:
  ii,si=edgeimgs[i]; jj,sj=edgeimgs[j]
  if {ii,jj}=={i,j}:tcell2+=si*sj*(1 if ii<jj else -1)
 h1=tgraph1-vfix+1
 h2=pointpairs-tcell1+tcell2-1+h1
 return h1,h2

def order(g):
 seen=set();lens=[]
 for v in V:
  if v not in seen:
   w=v;k=0
   while w not in seen:seen.add(w);k+=1;w=g[w]
   lens.append(k)
 return lcm(*lens)

class_counts=defaultdict(int)
inner8=inner6=innercross=0
for g in G:
 a,b=trace(g)
 c=b-a
 key=(order(g),int(g[0]>=7),a,b,c)
 class_counts[key]+=1
 inner8+=a*a; inner6+=c*c; innercross+=a*c
actual=sorted([[ord_,swap,count,a,b,c] for (ord_,swap,a,b,c),count in class_counts.items()])
assert actual==sorted(K['expected_character_classes']),(actual,K['expected_character_classes'])
assert (inner8,inner6,innercross)==(336,336,0)
assert sum(count*a for (_,_,a,b,c),count in class_counts.items())==0
assert sum(count*b for (_,_,a,b,c),count in class_counts.items())==0
print('PASS',{'cells':[len(C0),len(C1),len(C2)],'rank_d1':90,'rank_d2_Q':154,
 'rank_d2_F2':rank2,'boundary_minor_det':det,'H1':'Z^8 + Z/2',
 'H2':'Z^14','embedded_tori':14,'torus_minor_det':mdet,
 'automorphisms':len(G),'classes':actual,'character_norms':(inner8,inner6,innercross)})
