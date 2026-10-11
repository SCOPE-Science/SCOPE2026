"""Reconstruct and verify the ordinary 3-cut complex of the icosahedral graph.
Uses only the Python standard library; all faces and Hasse edges are enumerated.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations

N = 12
EDGES = ((0,1),(0,5),(0,7),(0,8),(0,11),
 (1,2),(1,5),(1,6),(1,8),(2,3),(2,6),(2,8),(2,9),
 (3,4),(3,6),(3,9),(3,10),(4,5),(4,6),(4,10),(4,11),
 (5,6),(5,11),(7,8),(7,9),(7,10),(7,11),(8,9),(9,10),(10,11))
ORDER = (7,9,5,1,2,4,3,11,10,0,6,8)
ADJ = [0]*N
for a,b in EDGES:
 assert 0 <= a < b < N
 ADJ[a] |= 1 << b; ADJ[b] |= 1 << a
assert len(EDGES)==30 and all(x.bit_count()==5 for x in ADJ)
# Every vertex link is an induced five-cycle, fixing the icosahedral combinatorics.
for v in range(N):
 neighbors=[u for u in range(N) if ADJ[v]>>u&1]
 assert len(neighbors)==5
 assert all(sum((ADJ[u]>>w)&1 for w in neighbors if w!=u)==2 for u in neighbors)
 assert len({tuple(sorted((u,w))) for u,w in combinations(neighbors,2) if ADJ[u]>>w&1})==5
assert sum(1 for a,b,c in combinations(range(N),3) if (ADJ[a]>>b)&1 and (ADJ[a]>>c)&1 and (ADJ[b]>>c)&1)==20

def connected3(t):
 a,b,c=t
 return ((ADJ[a]>>b)&1)+((ADJ[a]>>c)&1)+((ADJ[b]>>c)&1)>=2

bad = [sum(1<<v for v in t) for t in combinations(range(N),3) if not connected3(t)]
assert len(bad)==140
facets = [(1<<N)-1^b for b in bad]
faces=set()
for top in facets:
 s=top
 while s:
  faces.add(s);s=(s-1)&top
assert Counter(x.bit_count()-1 for x in faces)==dict(enumerate((12,66,220,495,792,924,792,465,140)))
assert len(faces)==3906

# Stage matching, with the face set remaining after each element toggle.
alive=set(faces); matched=[]
for v in ORDER:
 t=1<<v
 for x in sorted(alive):
  y=x|t
  if x&t==0 and y in alive:
   alive.remove(x);alive.remove(y);matched.append((x,y))
assert len(matched)==1949
assert Counter(x.bit_count()-1 for x in alive)=={0:1,7:1,8:6}
assert len(alive)==8

# Full directed Hasse diagram: unmatched covers oriented upward, matched downward.
paired=set(matched)
indeg={x:0 for x in faces}
out={x:[] for x in faces}
edges=0
for y in faces:
 for v in range(N):
  if (y>>v)&1 and (x:=y^(1<<v)):
   assert x in faces
   a,b=(y,x) if (x,y) in paired else (x,y)
   out[a].append(b);indeg[b]+=1;edges+=1
queue=deque(x for x in faces if indeg[x]==0)
seen=0
while queue:
 x=queue.popleft();seen+=1
 for y in out[x]:
  indeg[y]-=1
  if not indeg[y]:queue.append(y)
assert seen==len(faces)

# Alexander-dual complementary complex of vertex subsets all of whose triples
# induce connected subgraphs. Exhaustive at 12 vertices.
K=[]
for s in range(1,1<<N):
 if not any(s&b==b for b in bad):K.append(s)
assert len(K)==188
assert Counter(x.bit_count()-1 for x in K)=={0:12,1:66,2:80,3:30}
levels=[[x for x in K if x.bit_count()==j] for j in range(1,5)]

def rank_rational(matrix):
 # Sparse fractions, ordinary field elimination, with exact integers as input.
 bas={}
 for col in matrix:
  d={i:Fraction(t) for i,t in col.items()}
  while d:
   p=min(d)
   if p not in bas:
    a=d[p]
    bas[p]={j:v/a for j,v in d.items()}
    break
   coeff=d[p]
   for j,v in bas[p].items():
    z=d.get(j,0)-coeff*v
    if z:d[j]=z
    else:d.pop(j,None)
 return len(bas)

def boundary_rank(lo,hi):
 rows={x:i for i,x in enumerate(lo)}
 cols=[]
 for top in hi:
  c={}
  for pos,v in enumerate(a for a in range(N) if top&(1<<a)):
   c[rows[top^(1<<v)]]=1 if pos%2==0 else -1
  cols.append(c)
 return rank_rational(cols)

ranks=[boundary_rank(levels[i-1],levels[i]) for i in range(1,4)]
assert ranks==[11,49,30],ranks
# dual complex: reduced Betti 1 = 66 - rank_1 - rank_2 = 6.
assert 66-ranks[0]-ranks[1]==6
assert 80-ranks[1]-ranks[2]==1
# Duality implies rational Betti 8 = 6, so the 1x6 integral Morse boundary
# must be zero; it follows that each 8-cell has null attaching map to S^7.
print('VERIFY_OK', {'vertices':N,'graph_edges':len(EDGES),
 'disconnected_triples':len(bad), 'faces':len(faces),
 'hasse_covers':edges,'morse_pairs':len(matched),
 'critical':sorted(Counter(x.bit_count()-1 for x in alive).items()),
 'dual_face_count':len(K),'dual_boundary_ranks':ranks,
 'homotopy':'S^7 vee 6 S^8'})
