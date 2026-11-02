"""Independent colouring-partition and Hamming-bucket verification (stdlib only)."""
from collections import Counter, defaultdict
from itertools import combinations
E=[(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
# Independently enumerate named four-way partitions into independent vertex sets.
N=12;FULL=(1<<N)-1
ind=set(mask for mask in range(1<<N) if all(not((mask>>u)&1 and (mask>>v)&1) for u,v in E))
C=[]
def visit(rest,parts):
 if len(parts)==3:
  if rest in ind:
   parts=parts+[rest]
   c=[next(j for j,mask in enumerate(parts) if (mask>>i)&1) for i in range(N)]
   C.append(tuple(c))
  return
 sub=rest
 while sub:
  if sub in ind:visit(rest^sub,parts+[sub])
  sub=(sub-1)&rest
visit(FULL,[])
assert len(C)==18024 and len(set(C))==18024
idx={c:i for i,c in enumerate(C)}
NBR=[set() for _ in C]
for v in range(12):
 buckets=defaultdict(list)
 for i,c in enumerate(C):buckets[c[:v]+c[v+1:]].append(i)
 for b in buckets.values():
  for i,j in combinations(b,2):NBR[i].add(j);NBR[j].add(i)
assert sum(map(len,NBR))==128640
component=[-1]*len(C);sizes=[]
for i in range(len(C)):
 if component[i]!=-1:continue
 label=len(sizes);component[i]=label;todo=[i];size=0
 while todo:
  z=todo.pop();size+=1
  for j in NBR[z]:
   if component[j]==-1:component[j]=label;todo.append(j)
 sizes.append(size)
assert sorted(sizes)==[9012,9012]
# Enumerate every Hamming-distance-two pair across the disconnected sectors.
# Each cross-component pair is an available *single simultaneous* change of exactly two vertices.
across=set();cross_vertex=Counter()
for i,c in enumerate(C):
 for u,v in combinations(range(12),2):
  for a in range(4):
   if a==c[u]:continue
   for b in range(4):
    if b==c[v]:continue
    x=list(c);x[u]=a;x[v]=b
    j=idx.get(tuple(x))
    if j is not None and component[i]!=component[j] and j>i:
     across.add((i,j));cross_vertex[(u,v)]+=1
assert len(across)==11616,len(across)
assert len(cross_vertex)==20 and all(edge in E for edge in cross_vertex)
assert set(E)-set(cross_vertex)=={(2,3),(6,11),(7,8),(9,10)}
# Since each of the two one-vertex components is connected, one cross-sector edge makes the <=2-change graph connected.
print('B_PASS independent 4-way independent-set partition 18024 proper colourings')
print('B_PASS Hamming-one edges=64320 components=(9012,9012)')
print('B_PASS Hamming-two cross-sector pairs=11616 supported on 20 of 24 adjacent vertex pairs')
print('B_PASS one two-vertex simultaneous change joins the two sectors')

wi,wj=min(across)
print("B_WITNESS two-vertex crossing",C[wi],C[wj],"changed",tuple(t for t in range(12) if C[wi][t]!=C[wj][t]))
