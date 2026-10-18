"""Independent 3-vertex forbidden-pattern enumeration and mod-2 boundary computation."""
from collections import defaultdict
from itertools import combinations

E={(min(a,b),max(a,b)) for a,b in (
(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))}
assert len(E)==18
assert all(sum(v in e for e in E)==3 for v in range(12))

# Check the standard Frucht LCF presentation against a label isomorphism.
J=[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]
LCF={(min(i,(i+1)%12),max(i,(i+1)%12)) for i in range(12)}
LCF|={(min(i,(i+j)%12),max(i,(i+j)%12)) for i,j in enumerate(J)}
perm={4:0,3:1,2:2,1:3,7:4,0:5,6:6,5:7,10:8,11:9,8:10,9:11}
assert len(LCF)==18 and set(perm)==set(range(12)) and set(perm.values())==set(range(12))
assert {(min(perm[u],perm[v]),max(perm[u],perm[v])) for u,v in E}==LCF

# Every connected induced graph of order >=3 contains a connected induced triple.
# The forbidden triples are precisely triples spanning at least two edges.
BAD=[]
for t in combinations(range(12),3):
 if sum((min(a,b),max(a,b)) in E for a,b in combinations(t,2))>=2:
  BAD.append(sum(1<<v for v in t))
F={mask for mask in range(1,1<<12) if not any(mask&t==t for t in BAD)}
assert len(F)==824
assert [sum(f.bit_count()==k for f in F) for k in range(1,8)]==[12,66,190,293,209,53,1]

def reduced_betti(K):
 K=set(K)-{0}
 levels=defaultdict(list)
 for f in K:levels[f.bit_count()].append(f)
 if not levels:return {}
 ranks={1:0}
 for k in range(2,max(levels)+1):
  idx={f:i for i,f in enumerate(levels[k-1])}
  pivots={};rank=0
  for f in levels[k]:
   vec=0
   for v in range(12):
    if f&(1<<v): vec ^= 1 <<idx[f^(1<<v)]
   while vec:
    i=vec.bit_length()-1
    if i not in pivots:
     pivots[i]=vec;rank+=1;break
    vec ^= pivots[i]
  ranks[k]=rank
 out={k-1:len(levels[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in levels}
 out[0]-=1
 return {k:v for k,v in out.items() if v}

assert reduced_betti(F)=={3:1}
DEL=[2,2,2,1,2,2,1,3,1,2,2,4]
LINK=[{2:1,3:2},{3:1},{3:1},{},{3:1},{3:1},{2:1,3:1},{3:2},{2:1,3:1},{2:1,3:2},{3:1},{3:3}]
for v in range(12):
 d={f for f in F if not(f&(1<<v))}
 l={f^(1<<v) for f in F if f&(1<<v)}
 assert reduced_betti(d)=={3:DEL[v]},(v,'del',reduced_betti(d))
 assert reduced_betti(l)==LINK[v],(v,'link',reduced_betti(l))
 print(v,len(d),len(l)-1,reduced_betti(d),reduced_betti(l))
print('INDEPENDENT_ALL_25_OK')
