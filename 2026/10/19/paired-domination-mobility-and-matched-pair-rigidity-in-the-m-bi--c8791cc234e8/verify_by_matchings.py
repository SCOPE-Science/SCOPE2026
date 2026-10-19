#!/usr/bin/env python3
"""Enumerate all small edge matchings; their endpoint sets generate every paired-dominating set."""
import itertools,collections,collections.abc,hashlib,json,sys,functools

N=8
V=2*N
EDGES=sorted({tuple(sorted(e)) for i in range(N) for e in ((i,(i+1)%N),(i,N+i),(N+i,N+(i+3)%N))})
A=[0]*V
for u,v in EDGES:A[u]|=1<<v;A[v]|=1<<u
closed=[A[i]|(1<<i) for i in range(V)]; FULL=(1<<V)-1

def covered(m):
 r=0
 for i in range(V):
  if m&(1<<i):r|=closed[i]
 return r==FULL

def enumerate_pd(matching_size):
 # This is genuinely different from direct vertex-subset enumeration: every
 # possible disjoint family of edges of the required size is constructed.
 ans=set()
 def rec(start, chosen_mask, remaining):
  if not remaining:
   if covered(chosen_mask):ans.add(chosen_mask)
   return
  for ei in range(start,len(EDGES)):
   u,v=EDGES[ei]; pair=(1<<u)|(1<<v)
   if chosen_mask&pair:continue
   rec(ei+1,chosen_mask|pair,remaining-1)
 rec(0,0,matching_size)
 return sorted(ans)

sizes={2*t:enumerate_pd(t) for t in range(1,5)}
assert [len(sizes[k]) for k in (2,4,6,8)]==[0,0,0,684]
ms=sizes[8];at={m:i for i,m in enumerate(ms)}
J=set();P=set();STRICT=set()
@functools.lru_cache(None)
def has_remaining_matching(m):
 if not m:return True
 u=(m&-m).bit_length()-1
 return any((m>>v&1) and (A[u]>>v&1) and has_remaining_matching(m^(1<<u)^(1<<v)) for v in range(V))
for i,a in enumerate(ms):
 for u in range(V):
  if not a&(1<<u):continue
  for v in range(V):
   if a&(1<<v):continue
   tar=(a^(1<<u))|(1<<v)
   j=at.get(tar)
   if j is not None and i<j:J.add((i,j))
 # Paired-edge relocation: delete one selected adjacent pair, insert one unselected adjacent pair.
 for u,v in EDGES:
  old=(1<<u)|(1<<v)
  if (a&old)!=old:continue
  for x,y in EDGES:
   new=(1<<x)|(1<<y)
   if a&new:continue
   j=at.get((a^old)|new)
   if j is not None and i<j:
    P.add((i,j))
    if has_remaining_matching(a^old):STRICT.add((i,j))
J=sorted(J);P=sorted(P);STRICT=sorted(STRICT)

def distances(E):
 adj=[[] for _ in ms]
 for a,b in E: adj[a].append(b);adj[b].append(a)
 eccentric=[];components=[]
 seen=set()
 for start in range(len(ms)):
  if start in seen:continue
  stack=[start];seen.add(start);C=[]
  for u in stack:
   C.append(u)
   for v in adj[u]:
    if v not in seen:seen.add(v);stack.append(v)
  components.append(sorted(C))
 for s in range(len(ms)):
  ds={s:0};q=[s]
  for x in q:
   for y in adj[x]:
    if y not in ds:ds[y]=ds[x]+1;q.append(y)
  eccentric.append(max(ds.values()) if len(ds)>1 else -1)
 return components,eccentric
JC,JE=distances(J);PC,PE=distances(P);SC,SE=distances(STRICT)
induced=[sum(1 for u,v in EDGES if (m&(1<<u)) and (m&(1<<v))) for m in ms]
# All size-eight paired-dominating sets necessarily meet each colour class in four vertices.
colour=[None]*V
colour[0]=0
q=[0]
for i in q:
 for j in range(V):
  if (A[i]>>j)&1:
   if colour[j] is None:colour[j]=1-colour[i];q.append(j)
   else:assert colour[j]!=colour[i]
assert len(q)==16 and all(sum(colour[j] for j in range(V) if m>>j&1)==4 for m in ms)
assert len(J)==3504 and len(JC)==1 and collections.Counter(JE)=={6:216,7:432,8:36}
assert len(P)==2016 and sorted(map(len,PC))==[1]*54+[630]
assert len(STRICT)==1392 and sorted(map(len,SC))==[1]*54+[30,168,432]
assert collections.Counter(SE)=={-1:54,4:30,9:288,10:312}
assert all((sum(1 for u,v in EDGES if (ms[k]&(1<<u)) and (ms[k]&(1<<v)))==8) for C in SC if len(C)==30 for k in C)
assert collections.Counter(PE)=={-1:54,6:630}
assert {i for i,e in enumerate(induced) if e==4}=={C[0] for C in PC if len(C)==1}
assert {i for i,e in enumerate(induced) if e==4}=={C[0] for C in SC if len(C)==1}
assert {len(C):dict(collections.Counter(SE[i] for i in C)) for C in SC if len(C)>1}=={432:{9:192,10:240},168:{9:96,10:72},30:{4:30}}
# No adjacent-vertex single token slide is possible.
assert all(not (A[u]>>v&1) for i,j in J for u in range(V) if ms[i]>>u&1 and not ms[j]>>u&1 for v in range(V) if ms[j]>>v&1 and not ms[i]>>v&1)
cert={
 'object':'Mobius-Kantor graph GP(8,3), vertices 0..15',
 'edges':[list(e) for e in EDGES],
 'minimal_paired_dominating_sets':[[i for i in range(V) if m>>i&1] for m in ms],
 'token_jumping_edges':[list(e) for e in J],
 'paired_edge_relocation_edges':[list(e) for e in P],
 'partner_preserving_relocation_edges':[list(e) for e in STRICT],
 'token_jumping_eccentricity':JE,
 'paired_edge_relocation_eccentricity':PE,
 'partner_preserving_relocation_eccentricity':SE,
 'partner_preserving_component_profiles':{str(len(C)):{str(k):v for k,v in sorted(collections.Counter(SE[i] for i in C).items())} for C in SC if len(C)>1},
 'induced_edge_count':induced,
}
summary={
 'n':V,'m':len(EDGES),'paired_dominating_counts_by_size':{str(k):len(sizes[k]) for k in (2,4,6,8)},
 'optimal_partition_profile':{'4+4':len(ms)},
 'token_jumping':{'vertices':len(ms),'edges':len(J),'components':list(sorted(map(len,JC),reverse=True)),'eccentricity_counts':dict(sorted(collections.Counter(JE).items()))},
 'token_sliding':{'vertices':len(ms),'edges':0,'components':len(ms)},
 'paired_edge_relocation':{'vertices':len(ms),'edges':len(P),'components':list(sorted(map(len,PC),reverse=True)),'eccentricity_counts':dict(sorted(collections.Counter(PE).items()))},
 'partner_preserving_relocation':{'vertices':len(ms),'edges':len(STRICT),'components':list(sorted(map(len,SC),reverse=True)),'eccentricity_counts':dict(sorted(collections.Counter(SE).items()))},
 'partner_preserving_component_profiles':{str(len(C)):{str(k):v for k,v in sorted(collections.Counter(SE[i] for i in C).items())} for C in SC if len(C)>1},
 'isolates_equivalent_to_four_induced_edges':True,
}
print(json.dumps(summary,sort_keys=True,indent=2))
if len(sys.argv)>1:
 with open(sys.argv[1],'w',encoding='utf8') as f:json.dump(cert,f,sort_keys=True,separators=(',',':'),ensure_ascii=False);f.write('\n')
