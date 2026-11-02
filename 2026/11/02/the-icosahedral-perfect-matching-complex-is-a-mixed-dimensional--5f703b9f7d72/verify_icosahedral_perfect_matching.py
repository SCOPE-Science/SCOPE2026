"""Exact finite verification of an icosahedral perfect-matching complex.

Python 3 standard library only. All faces, matchings, signed Morse differentials,
integer unit-minor evidence, and an independent simplicial mod-two computation
are reconstructed directly from the twelve-vertex thirty-edge graph definition.
"""

from collections import Counter,deque
from functools import lru_cache
import hashlib, json

def edges():
 u=lambda i: 1+i%5
 v=lambda i: 6+i%5
 pairs=[]
 for i in range(5):
  pairs.extend([(0,u(i)),(11,v(i)),(u(i),u(i+1)),(v(i),v(i+1)),(u(i),v(i)),(u(i),v(i-1))])
 return sorted({tuple(sorted(p)) for p in pairs})
E=edges();assert len(E)==30;neighbors={i:[] for i in range(12)}
for k,(u,v) in enumerate(E):neighbors[u].append((v,k));neighbors[v].append((u,k))
assert all(len(x)==5 for x in neighbors.values())
# These are the two apex vertices and two staggered five-rings of the standard
# icosahedral graph. Its twenty triangles triangulate a closed sphere.
adj={v:{w for w,j in nbrs} for v,nbrs in neighbors.items()}
triangles=[(a,b,c) for a in range(12) for b in range(a+1,12)
           for c in range(b+1,12) if b in adj[a] and c in adj[a] and c in adj[b]]
assert len(triangles)==20
assert all(sum(u in t and v in t for t in triangles)==2 for u,v in E)
assert all(sum(1 for a in adj[v] for b in adj[v] if a<b and b in adj[a])==5
           for v in range(12))

def perfect(rem):
 if not rem:yield 0;return
 v=min(rem)
 for w,j in neighbors[v]:
  if w in rem:
   for f in perfect(rem-{v,w}):yield f|(1<<j)
P=sorted(set(perfect(frozenset(range(12)))));assert len(P)==125
faces={0}
for p in P:
 sub=p
 while sub:
  faces.add(sub)
  sub=(sub-1)&p
assert len(faces)==4056
counts=Counter(f.bit_count()-1 for f in faces if f)
assert [counts[i] for i in range(6)]==[30,315,1260,1575,750,125]
print('facets',len(P),'faces',len(faces),'f-vector',dict(counts))

remaining=faces.copy();pairs=[];order=[]
for iteration in range(30):
 options=[]
 for j in range(30):
  matches=[(f,f|(1<<j)) for f in remaining if not f&(1<<j) and (f|(1<<j)) in remaining]
  options.append(matches)
 j=max(range(30),key=lambda j:(len(options[j]),-j))
 if not options[j]:break
 order.append(j)
 for lo,hi in options[j]:
  pairs.append((lo,hi));remaining.remove(lo);remaining.remove(hi)
assert len(pairs)==1975
assert Counter(f.bit_count()-1 for f in remaining)==Counter({2:65,3:41})
print('pairs',len(pairs),'critical',Counter(f.bit_count()-1 for f in remaining),'order',order)

# Complete directed face-poset check, matched faces point upward.
upper_to_lower={hi:lo for lo,hi in pairs};lower_to_upper={lo:hi for lo,hi in pairs}
assert len(upper_to_lower)==len(lower_to_upper)==len(pairs)
indeg={f:0 for f in faces};arcs={f:[] for f in faces};nhasse=0
for hi in faces:
 if not hi:continue
 x=hi
 while x:
  b=x&-x;lo=hi^b;x-=b;nhasse+=1
  if upper_to_lower.get(hi)==lo: a,b2=lo,hi
  else:a,b2=hi,lo
  arcs[a].append(b2);indeg[b2]+=1
Q=deque(f for f in faces if indeg[f]==0);seen=0
while Q:
 f=Q.popleft();seen+=1
 for g in arcs[f]:
  indeg[g]-=1
  if indeg[g]==0:Q.append(g)
assert seen==4056
print('Hasse',nhasse,'acyclic',seen)

# Signed simplicial boundary (basis ordered by sorted graph-edge indexes).
def bd(face):
 j=0;out=[];x=face
 while x:
  b=x&-x;x-=b
  out.append((face^b,(-1)**j));j+=1
 return out
@lru_cache(None)
def projection(face):
 # Eliminated upper cells represent zero; critical cells represent themselves.
 if face in upper_to_lower:return {}
 if face not in lower_to_upper:return {face:1}
 higher=lower_to_upper[face]
 d=dict(bd(higher));sgn=d.pop(face)
 assert abs(sgn)==1
 o={}
 for ff,coef in d.items():
  for crit,value in projection(ff).items():o[crit]=o.get(crit,0)-sgn*coef*value
 return {c:v for c,v in o.items() if v}
crit2=sorted(f for f in remaining if f.bit_count()==3);crit3=sorted(f for f in remaining if f.bit_count()==4)
rowind={s:i for i,s in enumerate(crit2)}
B=[[0]*len(crit3) for _ in crit2]
for col,c in enumerate(crit3):
 for ff,coef in bd(c):
  for target,value in projection(ff).items():
   assert target in rowind
   B[rowind[target]][col]+=coef*value
print('boundary nonzero',sum(x!=0 for row in B for x in row),'max',max(abs(x) for row in B for x in row))

# Exact integer unimodular-pivot Schur elimination, simultaneously certifies
# rank and a maximal minor of determinant ±1 (remaining block identically zero).
R=[row[:] for row in B];rindex=list(range(len(R)));cindex=list(range(len(R[0])));pr=[];pc=[];pv=[]
while True:
 pivot=next(((i,j) for i,row in enumerate(R) for j,x in enumerate(row) if abs(x)==1),None)
 if pivot is None:break
 i,j=pivot;p=R[i][j];pr.append(rindex[i]);pc.append(cindex[j]);pv.append(p)
 R=[[R[k][l]-R[k][j]*R[i][l]*p for l in range(len(cindex)) if l!=j] for k in range(len(rindex)) if k!=i]
 rindex.pop(i);cindex.pop(j)
assert not any(x for row in R for x in row)
assert len(pr)==22
print('integral rank',len(pr))
assert (len(crit2)-len(pr),len(crit3)-len(pr))==(43,19)
print('Betti2',len(crit2)-len(pr),'Betti3',len(crit3)-len(pr))
# Independent fraction-free determinant of the selected maximal minor.
def bareiss_det(M):
    M=[r[:] for r in M]
    n=len(M)
    sign=1
    prev=1
    for k in range(n-1):
        if M[k][k]==0:
            t=next((i for i in range(k+1,n) if M[i][k]),None)
            if t is None:return 0
            M[k],M[t]=M[t],M[k]
            sign=-sign
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=M[i][j]*pivot-M[i][k]*M[k][j]
                assert numer%prev==0
                M[i][j]=numer//prev
        for i in range(k+1,n):M[i][k]=0
        prev=pivot
    return sign*M[n-1][n-1]
minor_det=bareiss_det([[B[i][j] for j in pc] for i in pr])
assert minor_det==-1
print('maximal minor determinant',minor_det)
print('pivot rows',pr)
print('pivot columns',pc)
print('matrixsha',hashlib.sha256(json.dumps(B,separators=(',',':')).encode()).hexdigest())
# Direct independent simplicial ranks over GF(2), rather than using the Morse matching.
cells={d:sorted(f for f in faces if f.bit_count()==d+1) for d in range(6)}
def mod2rank(cols):
 piv={}
 for bit in cols:
  while bit:
   p=bit.bit_length()-1
   if p not in piv:
    piv[p]=bit;break
   bit^=piv[p]
 return len(piv)
ranks=[]
for d in range(1,6):
 prev={f:i for i,f in enumerate(cells[d-1])}
 cols=[]
 for hi in cells[d]:
  v=0
  for lo,_ in bd(hi):v^=1<<prev[lo]
  cols.append(v)
 ranks.append(mod2rank(cols))
print('independent simplicial mod2 ranks',ranks)
assert ranks==[29,286,931,625,125]
print('ICOSAHEDRAL_PERFECT_MATCHING_43S2_19S3_EXACT_OK')
