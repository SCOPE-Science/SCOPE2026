#!/usr/bin/env python3
"""Reconstruct the Pappus noncover complex and verify its Morse matching and symmetries."""
from itertools import permutations, product
from collections import Counter, defaultdict, deque
N=9; FULL=(1<<N)-1
lines=[]
for axis in range(3):
 for value in range(3):
  t=0
  for x in range(3):
   for y in range(3):
    if ((x,y,(x+y)%3)[axis]==value):t|=1<<(3*x+y)
  lines.append(t)
assert len(set(lines))==9 and all(z.bit_count()==3 for z in lines)
line_set=set(lines)
facets=[FULL^z for z in lines]
faces={s for s in range(1,FULL+1) if any(s&~f==0 for f in facets)}
assert len(faces)==297
face_vec=tuple(sum(s.bit_count()==k for s in faces) for k in range(1,7))
assert face_vec==(9,36,81,108,54,9)
# Existence and exhaustive acyclicity of one explicit matching.
order=(1,3,0,6,8,5,2,7,4)
active=faces.copy(); pairs=[]
for v in order:
 for s in sorted(active,key=lambda z:(z.bit_count(),z)):
  t=s|(1<<v)
  if not(s&(1<<v)) and s in active and t in active:
   pairs.append((s,t));active.remove(s);active.remove(t)
assert len(pairs)==143
assert sorted(active)==[2,77,85,113,165,225,300,312,329,408,456]
assert Counter(s.bit_count()-1 for s in active)==Counter({3:10,0:1})
matched=set(pairs)
outs=defaultdict(list);indeg={s:0 for s in faces};cover_count=0
for t in faces:
 for v in range(N):
  bit=1<<v;s=t^bit
  if t&bit and s:
   a,b=(s,t) if (s,t) in matched else (t,s)
   outs[a].append(b);indeg[b]+=1;cover_count+=1
assert cover_count==1071
ready=deque(s for s in faces if indeg[s]==0);swept=0
while ready:
 a=ready.popleft();swept+=1
 for b in outs[a]:
  indeg[b]-=1
  if indeg[b]==0:ready.append(b)
assert swept==len(faces)
# Independently recover mod-2 boundary ranks from every face.
byk={k:sorted(s for s in faces if s.bit_count()==k) for k in range(1,7)}
def rank_binary(k):
 lut={a:i for i,a in enumerate(byk[k-1])};piv={}
 for upper in byk[k]:
  vec=0
  for v in range(N):
   if upper&(1<<v):vec^=1<<lut[upper^(1<<v)]
  while vec:
   i=vec.bit_length()-1
   if i not in piv:piv[i]=vec;break
   vec^=piv[i]
 return len(piv)
ranks=(0,)+tuple(rank_binary(k) for k in range(2,7))+(0,)
betti=tuple(len(byk[k])-ranks[k-1]-ranks[k] for k in range(1,7))
assert betti==(1,0,0,10,0,0)
# Exhaustively enumerate all 9! permutations and retain all automorphisms.
def image_mask(mask,p):
 return sum((1<<p[i]) for i in range(N) if mask&(1<<i))
automorphisms=[]
for p in permutations(range(N)):
 if {image_mask(l,p) for l in lines}==line_set:automorphisms.append(p)
assert len(automorphisms)==108
# Independent affine reconstruction of all 108 point-side automorphisms.
affine=[]
for a,b,c,d in product(range(3),repeat=4):
 if (a*d-b*c)%3==0:continue
 for u,v in product(range(3),repeat=2):
  p=tuple(3*((a*x+b*y+u)%3)+(c*x+d*y+v)%3 for x in range(3) for y in range(3))
  if {image_mask(l,p) for l in lines}==line_set:affine.append(p)
assert len(set(affine))==108 and set(affine)==set(automorphisms)
# Complete signed Lefschetz and orbit-cycle trace implementations.
def trace_direct(p):
 total=0
 for s in faces:
  ids=[i for i in range(N) if s&(1<<i)]
  js=[p[i] for i in ids]
  if set(js)!=set(ids):continue
  inv=sum(js[i]>js[j] for i in range(len(js)) for j in range(i+1,len(js)))
  total+=(-1)**(len(ids)-1+inv)
 return 1-total # only H_3 reduced, so L=1-trace(H_3)
def trace_orbits(p):
 seen=set();cycles=[]
 for i in range(N):
  if i in seen:continue
  j=i;mask=0
  while j not in seen:
   seen.add(j);mask|=1<<j;j=p[j]
  cycles.append(mask)
 total=0
 for subset in range(1<<len(cycles)):
  mask=0
  for i,c in enumerate(cycles):
   if subset&(1<<i):mask|=c
  if mask==0 or mask in faces:total+=(-1)**subset.bit_count()
 return total
character=[]
for p in automorphisms:
 v=trace_direct(p)
 assert v==trace_orbits(p)
 character.append(v)
assert Counter(character)==Counter({10:1,-2:21,-1:36,1:32,2:18})
assert sum(character)==0
assert sum(z*z for z in character)==324
print('VERIFY_OK')
print('nine_lines',len(lines),'nonempty_faces',len(faces),'fvector',face_vec)
print('matching_pairs',len(pairs),'critical_dimensions',{0:1,3:10})
print('directed_cover_incidences',cover_count,'acyclic_topological_sort',swept)
print('mod2_betti',betti)
print('point_automorphisms',len(automorphisms),'affine_reconstruction',len(affine))
print('character_histogram',sorted(Counter(character).items()))
print('invariant_dimension',sum(character)//108,'character_self_inner_product',sum(z*z for z in character)//108)
print('all_108_signed_lefschetz_and_cycle_orbit_traces_agree',True)
