"""Exact finite certificate for the Franklin-graph perfect-matching complex.

Requires Python 3 standard library only. Each assertion is a finite identity.
"""
import itertools, collections, heapq
EDGES=[(0,1),(0,5),(0,11),(1,2),(1,8),(2,3),(2,7),(3,4),(3,10),(4,5),(4,9),(5,6),(6,7),(6,11),(7,8),(8,9),(9,10),(10,11)]
ORDER=[16,5,17,14,7,8,6,0,12,10,15,11,2,1,9,3,13,4]
assert len(EDGES)==18 and len(set(EDGES))==18
assert len(ORDER)==18 and set(ORDER)==set(range(18))
cycle_edges={tuple(sorted((i,(i+1)%12))) for i in range(12)}
chord_edges={tuple(sorted((i,(i+(5 if i%2==0 else -5))%12))) for i in range(12)}
assert set(EDGES)==cycle_edges|chord_edges
assert len(cycle_edges)==12 and len(chord_edges)==6
nbr={x:[] for x in range(12)}
for ix,(u,v) in enumerate(EDGES):nbr[u].append((v,ix));nbr[v].append((u,ix))
MS=[]
def gen(left,bits):
 if not left:
  MS.append(bits);return
 u=min(left)
 for v,j in nbr[u]:
  if v in left:gen(left-{u,v},bits|(1<<j))
gen(set(range(12)),0)
assert len(MS)==17 and len(set(MS))==17
F={0}
for M in MS:
 subset=M
 while True:
  F.add(subset)
  if subset==0:break
  subset=(subset-1)&M
assert len(F)==762
# Exhaustive independent check of the ordinary matching complex:
# inspect all 2^18 graph-edge subsets and require disjoint endpoints.
ordinary={0}
for mask in range(1,1<<18):
 used=0
 for j,(u,v) in enumerate(EDGES):
  if mask>>j&1:
   endpoints=(1<<u)|(1<<v)
   if used&endpoints:break
   used|=endpoints
 else:ordinary.add(mask)
assert collections.Counter(s.bit_count() for s in ordinary)=={0:1,1:18,2:117,3:336,4:417,5:186,6:17}
assert F<=ordinary
assert sum(1 for s in ordinary-F if s.bit_count()==3)==72
assert not any(s.bit_count()<=2 for s in ordinary-F)
assert collections.Counter(x.bit_count() for x in F)=={0:1,1:18,2:117,3:264,4:243,5:102,6:17}
unmatched=F-{0}; P=[]
for v in ORDER:
 b=1<<v
 pairs=[(s,s|b) for s in unmatched if not (s&b) and (s|b) in unmatched]
 for a,z in pairs:
  unmatched.remove(a);unmatched.remove(z)
 P+=pairs
assert len(P)==377
assert collections.Counter(s.bit_count()-1 for s in unmatched)=={0:1,2:6}
matched=set(P)
faces=F-{0};indegree={s:0 for s in faces};graph={s:[] for s in faces}
incidences=0
for s in faces:
 for i in range(18):
  b=1<<i
  if not s&b:continue
  t=s^b
  if not t:continue
  if (t,s) in matched:u,v=t,s
  else:u,v=s,t
  graph[u].append(v);indegree[v]+=1
  incidences+=1
q=[s for s in faces if indegree[s]==0];heapq.heapify(q); count=0
while q:
 u=heapq.heappop(q);count+=1
 for v in graph[u]:
  indegree[v]-=1
  if indegree[v]==0:heapq.heappush(q,v)
assert count==len(faces),(count,len(faces))
print('perfect matching count',len(MS));print('ordinary faces',len(ordinary)-1, 'nonextendible triples',72); print('simplices by dimension',dict(sorted(collections.Counter(s.bit_count()-1 for s in faces).items())))
print('pairs',len(P),'critical',dict(sorted(collections.Counter(s.bit_count()-1 for s in unmatched).items())))
print('incidences',incidences,'acyclic',count==len(faces))
print('critical faces',sorted(tuple(i for i in range(18) if s>>i&1) for s in unmatched))
print('VERIFY_OK')
