#!/usr/bin/env python3
"""Independent construction via the line graph of once-subdivided K4.
Enumerates matchings recursively; independently computes mod-2 Betti ranks.
"""
import itertools,collections
# Each edge {u,v} of K4 is subdivided, with new vertex named ('s',u,v).
sub=[]
for u,v in itertools.combinations(range(4),2):
 middle=('s',u,v)
 sub.extend([(u,middle),(v,middle)])
assert len(sub)==12
# The truncated tetrahedron is the line graph of this subdivided K4.
GE=[]
for i,j in itertools.combinations(range(12),2):
 if set(sub[i])&set(sub[j]):GE.append((i,j))
assert len(GE)==18
# All faces of the matching complex, from a recursion disjointness filter.
def matching_faces(edge_indices):
 E=[GE[i] for i in edge_indices]
 faces=[]
 def rec(j,used,selection):
  if j==len(E):
   faces.append(tuple(selection));return
  rec(j+1,used,selection)
  a,b=E[j]
  if not ((used>>a)&1 or (used>>b)&1):
   selection.append(edge_indices[j]);rec(j+1,used|1<<a|1<<b,selection);selection.pop()
 rec(0,0,[])
 return {tuple(sorted(face)) for face in faces}

def ranks_betti(faces):
 by_dim={j:sorted(face for face in faces if len(face)==j+1) for j in range(-1,6)}
 ranks={}
 for dim in range(1,6):
  upper=by_dim[dim];lower=by_dim[dim-1]
  idx={s:i for i,s in enumerate(lower)};basis={}
  for face in upper:
   bits=0
   for k in range(len(face)):
    bits^=1<<idx[face[:k]+face[k+1:]]
   while bits:
    leading=bits.bit_length()-1
    if leading in basis:bits^=basis[leading]
    else:basis[leading]=bits;break
  ranks[dim]=len(basis)
 # Euler chain boundary in dimension zero has rank #vertices-1 if connected.
 n0=len(by_dim[0])
 betti={}
 for i in range(6):
  n=len(by_dim[i]);rdown=0 if i==0 else ranks.get(i,0)
  rup=ranks.get(i+1,0)
  val=n-rdown-rup-(1 if i==0 else 0)
  if val:betti[i]=val
 return betti,{str(i):len(by_dim[i]) for i in range(6) if by_dim[i]}

allidx=list(range(len(GE)))
full=matching_faces(allidx)
res=[]
for kind,faces in [('full',full)]:res.append((kind,*ranks_betti(faces)))
for kind,edge in [('triangular',next(i for i,(a,b) in enumerate(GE) if len(set(sub[a])&set(sub[b]))==1 and any(isinstance(x,int) for x in set(sub[a])&set(sub[b])))),('reversal',next(i for i,(a,b) in enumerate(GE) if any(isinstance(x,tuple) for x in set(sub[a])&set(sub[b]))))]:
 E=set(range(len(GE)))
 D=matching_faces(sorted(E-{edge}))
 L={tuple(sorted(s-{edge})) for f in full if edge in f for s in [set(f)]}
 res.append((kind+' edge deletion',*ranks_betti(D)))
 res.append((kind+' endpoint deletion',*ranks_betti(L)))
expected={'full':{3:22},'triangular edge deletion':{3:14},'triangular endpoint deletion':{2:8},'reversal edge deletion':{3:20},'reversal endpoint deletion':{2:2}}
for k,b,f in res:
 print(k,'mod2 reduced Betti',b,'face vector',f)
 assert b==expected[k],(k,b,expected[k])
print('INDEPENDENT_VERIFY_OK')
