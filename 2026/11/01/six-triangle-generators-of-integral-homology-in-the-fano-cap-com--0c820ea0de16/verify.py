"""Reproducible exact check of six-triangle Fano cap cycles. Requires sympy."""
from itertools import combinations,product
from collections import Counter,defaultdict
from sympy import Matrix
V=list(range(1,8))
def xor(a,b):return a^b
lines=sorted(tuple(sorted((i,j,i^j))) for i,j in combinations(V,2) if i<j and i< i^j and j<i^j)
lines=sorted(set(lines)); print('lines',lines)
faces={k:[] for k in range(1,5)}
for k in range(1,5):
 for S in combinations(V,k):
  if not any(set(L)<=set(S) for L in lines):faces[k].append(S)
print('face_counts',{k:len(v) for k,v in faces.items()})
B={}
for k in range(2,5):
 lower={f:i for i,f in enumerate(faces[k-1])};B[k]=Matrix(len(lower),len(faces[k]),lambda i,j:0)
 for j,f in enumerate(faces[k]):
  for i in range(k): B[k][lower[f[:i]+f[i+1:]],j]=(-1)**i
print('ranks',{k: B[k].rank() for k in B})
# 3x3 GF2 matrices
G=[]
for rows in product(range(8),repeat=3):
 def apply(x):return sum(((int((r&x).bit_count()%2))<<i) for i,r in enumerate(rows))
 if len(set(apply(x) for x in range(8)))==8:
  G.append(tuple(apply(x) for x in range(8)))
print('group',len(G))
def sign_of_map(g,S):
 t=[g[x] for x in S];return (-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
def order(g):
 h=tuple(range(8))
 for i in range(1,100):
  h=tuple(g[x] for x in h)
  if h==tuple(range(8)):return i
for ord in sorted(set(map(order,G))):
 traces=Counter()
 for g in G:
  if order(g)!=ord:continue
  tr=-1 # reduced empty
  for k,Fs in faces.items():
   tr += (-1)**(k-1)*sum(sign_of_map(g,f) for f in Fs if set(g[x] for x in f)==set(f))
  traces[tr]+=1
 print(ord,traces)
# six triangle cycles
tri=faces[3]; eidx={e:i for i,e in enumerate(faces[2])}
mask=[]
for T in tri:
 m=0
 for e in combinations(T,2):m ^= 1<<eidx[e]
 mask.append(m)
sols=[]
for k in range(1,7):
 arr=[]
 for comb in combinations(range(len(tri)),k):
  b=0
  for i in comb:b ^= mask[i]
  if b==0:arr.append(comb)
 print('mod2_cycle_support',k,len(arr))
 if k==6: sols=arr
print('six example', [tri[i] for i in sols[0]])
# tetra boundary groups
caps=faces[4]
groups=[{tri.index(t) for t in combinations(Q,3)} for Q in caps]
print('blocks disjoint',len(set().union(*groups)),[len(x) for x in groups])
print('six 5 vertices?',Counter(len(set().union(*(tri[i] for i in s))) for s in sols))
# orbit of six cycles under group
ss={frozenset(s) for s in sols}
parent=sols[0]; orb=set()
for g in G:
 im=frozenset(tri.index(tuple(sorted(g[x] for x in tri[i]))) for i in parent)
 orb.add(im)
print('orbit length',len(orb),'all?',orb==ss)
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
Tpos={t:i for i,t in enumerate(tri)}
def v3_boundary(L):
 ret=[0]*len(tri)
 for i in range(4):
  face=L[:i]+L[i+1:]; sort=tuple(sorted(face)); sign=(-1)**i*(-1)**sum(face[a]>face[b] for a in range(3) for b in range(a+1,3))
  if sort in Tpos:ret[Tpos[sort]]+=sign
 return ret
cols=[]
for S in combinations(V,5):
 sublines=[l for l in lines if set(l)<=set(S)]
 assert len(sublines)==2
 for L in sublines:
  p,q=sorted(set(S)-set(L));u=v3_boundary((p,)+L);v=v3_boundary((q,)+L)
  c=[a-b for a,b in zip(u,v)]
  assert sum(int(x!=0) for x in c)==6
  assert B[3]*Matrix(c)==Matrix.zeros(21,1)
  cols.append(c)
Dcols=[v3_boundary(Q) for Q in faces[4]]
H=Matrix.hstack(*(Matrix(x) for x in cols+Dcols))
print('all 49 rank',H.rank())
D=smith_normal_form(H,domain=ZZ)
print('nonzero smith invariant', [int(D[i,i]) for i in range(min(D.shape)) if D[i,i]!=0])
print('sphere-only rank',Matrix.hstack(*(Matrix(x) for x in cols)).rank())
H6=Matrix.hstack(*(Matrix(x) for x in cols))
D6=smith_normal_form(H6,domain=ZZ)
print('sphere-only SNF nonzeros', [int(D6[i,i]) for i in range(min(D6.shape)) if D6[i,i]!=0])

# Final exact assertions; finite enumeration exhausts all subsets of at most six triangles.
assert len(lines)==7 and [len(faces[k]) for k in (1,2,3,4)]==[7,21,28,7]
assert B[2].rank()==6 and B[3].rank()==15 and B[4].rank()==7
assert [int(smith_normal_form(B[3],domain=ZZ)[i,i]) for i in range(15)]==[1]*15
assert len(G)==168 and len(sols)==42 and len(orb)==42 and orb==ss
assert len(set().union(*groups))==28 and all(len(x)==4 for x in groups)
assert len(cols)==42 and len({frozenset(i for i,z in enumerate(c) if z) for c in cols})==42
assert set(frozenset(i for i,z in enumerate(c) if z) for c in cols)==ss
assert all(B[3]*Matrix(c)==Matrix.zeros(21,1) for c in cols)
assert H6.rank()==13 and [int(D6[i,i]) for i in range(13)]==[1]*13
# Primitivity in homology: adding each sphere to the seven boundary cycles is saturated.
for c in cols:
    augmented=Matrix.hstack(*(Matrix(x) for x in Dcols+[c]))
    smith=smith_normal_form(augmented,domain=ZZ)
    assert augmented.rank()==8 and [abs(int(smith[i,i])) for i in range(8)]==[1]*8
assert B[3].cols-B[3].rank()==13
assert [int(D[i,i]) for i in range(13)]==[1]*13
print('boundary_2 Smith invariants: fifteen 1s; reduced H_1=0 integrally')
print('all 42 minimal sphere classes primitive modulo tetrahedral boundaries')
print('homology: reduced H_2 free rank 6; all others zero')
print('minimal nonboundary integral support: 6 triangles, 42 supports, one automorphism orbit')
print('all 42 oriented six-triangle sphere cycles span ker(boundary_2) over the integers')
print('VERIFY_OK')
