"""Exact Chvatal graph four-colouring move graph, independently replayable (stdlib)."""
from collections import Counter, deque
from itertools import permutations
E=[(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
Q=[((0,1,2,6),1),((0,1,5,4),-1),((0,4,3,9),-1),((0,6,11,9),1),((1,2,3,7),1),((1,5,11,7),-1),((2,3,4,8),1),((2,6,10,8),-1),((3,7,11,9),-1),((4,5,10,8),1),((5,10,6,11),1)]
AUT=[(0,1,2,3,4,5,6,7,8,9,10,11),(0,4,3,2,1,5,9,8,7,6,11,10),(1,0,6,11,5,4,2,9,10,7,8,3),(4,0,9,10,5,1,3,6,11,8,7,2),(1,5,11,6,0,4,7,10,9,2,3,8),(4,5,10,9,0,1,8,11,6,3,2,7),(5,1,7,8,4,0,11,2,3,10,9,6),(5,4,8,7,1,0,10,3,2,11,6,9)]
assert len(E)==24 and len(set(E))==24
assert all(tuple(sorted((q[i],q[(i+1)%4]))) in E for q,_ in Q for i in range(4))
assert len(set(AUT))==8 and all({tuple(sorted((a[x],a[y]))) for x,y in E}==set(E) for a in AUT)
assert {tuple(a[b[i]] for i in range(12)) for a in AUT for b in AUT}==set(AUT)
A=[set() for _ in range(12)]
for u,v in E:A[u].add(v);A[v].add(u)
assert all(len(a)==4 for a in A)
C=[];work=[0]*12

def rec(v):
 if v==12:C.append(tuple(work));return
 used={work[w] for w in A[v] if w<v}
 for k in range(4):
  if k not in used:work[v]=k;rec(v+1)
rec(0);assert len(C)==18024
# The same exhaustive extension recursion rejects every proper three-colouring.
def three(v,assign):
 if v==12:return 1
 forbidden={assign[w] for w in A[v] if w<v}
 return sum(three(v+1,assign+[k]) for k in range(3) if k not in forbidden)
assert three(0,[])==0
idx={c:i for i,c in enumerate(C)};assert len(idx)==len(C)
N=[[] for _ in C]
for i,c in enumerate(C):
 for v in range(12):
  used={c[w] for w in A[v]}
  for k in range(4):
   if k==c[v] or k in used:continue
   d=list(c);d[v]=k;N[i].append(idx[tuple(d)])
assert sum(map(len,N))==2*64320 and all(i in N[j] for i,adj in enumerate(N) for j in adj)

def signword(p):
 if len(set(p))<4:return 0
 return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def invariant(c):return sum(coef*signword(tuple(c[v] for v in q)) for q,coef in Q)
I=[invariant(c) for c in C]
assert Counter(I)=={-3:9012,3:9012}
assert all(I[i]==I[j] for i,adj in enumerate(N) for j in adj)
lab=[-1]*len(C);components=[]
for i in range(len(C)):
 if lab[i]>=0:continue
 lab[i]=len(components);stack=[i];comp=[]
 while stack:
  z=stack.pop();comp.append(z)
  for y in N[z]:
   if lab[y]==-1:lab[y]=lab[i];stack.append(y)
 components.append(comp)
assert len(components)==2 and sorted(map(len,components))==[9012,9012]
assert len({I[i] for i in components[0]})==len({I[i] for i in components[1]})==1 and I[components[0][0]]!=I[components[1][0]]
assert Counter(map(len,N))=={4:288,5:1344,6:4224,7:4416,8:5352,9:2304,10:96}
# Every orbit under the eight graph automorphisms and 24 colour-name permutations has the same eccentricity.
P=list(permutations(range(4)));seen=set();ecc=Counter();orbs=0
for i,c in enumerate(C):
 if i in seen:continue
 orbit=set()
 for a in AUT:
  d=[None]*12
  for v in range(12):d[a[v]]=c[v]
  for p in P:orbit.add(idx[tuple(p[x] for x in d)])
 assert orbit.isdisjoint(seen)
 seen.update(orbit);orbs+=1
 dist={i:0};q=deque([i])
 while q:
  z=q.popleft()
  for j in N[z]:
   if j not in dist:dist[j]=dist[z]+1;q.append(j)
 assert len(dist)==9012
 ecc[max(dist.values())]+=len(orbit)
assert len(seen)==18024
assert ecc=={16:192,17:9024,18:8424,19:336,20:48},ecc
print('A_PASS vertices=18024 edges=64320 components=(9012,9012) I=(+3,-3) with invariant proof by exhaustive edges')
print('A_PASS 8 automorphisms, orbits=',orbs,'eccentricities=',dict(ecc),'radius=16 diameter=20')
