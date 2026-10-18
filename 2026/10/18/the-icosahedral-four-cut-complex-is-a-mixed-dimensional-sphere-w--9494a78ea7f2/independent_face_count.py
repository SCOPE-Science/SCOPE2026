from itertools import combinations
from collections import defaultdict
from math import comb
V=list(range(12))
E=set()
for j in range(5):
 a=1+j;b=6+j
 for u,v in [(0,a),(11,b),(a,1+(j+1)%5),(b,6+(j+1)%5),(a,b),(a,6+(j-1)%5)]:E.add(tuple(sorted((u,v))))
assert len(E)==30

def connected(vertices):
 unseen=set(vertices);q=[unseen.pop()];seen={q[0]}
 for u in q:
  for v in list(unseen):
   if tuple(sorted((u,v))) in E:
    unseen.remove(v);seen.add(v);q.append(v)
 return len(seen)==len(vertices)
invalid=[]
for s in combinations(V,4):
 if not connected(s):invalid.append(frozenset(s))
faces=[{} for i in range(9)]
for chosen in combinations(V,4):
 if frozenset(chosen) not in invalid:continue
 allowed=set(V)-set(chosen)
 for size in range(1,9):
  for s in combinations(sorted(allowed),size):faces[size][s]=True
counts=tuple(len(f) for f in faces[1:])
print('disconnected four-subsets',len(invalid),'face counts',counts,'total',sum(counts))
assert len(invalid)==285 and sum(counts)==3502
# Euler checks: reduced chi should 5 - 20 = -15 because S6 positive, S7 negative.
euler=sum((-1)**(i-1)*len(faces[i]) for i in range(1,9))
print('Euler',euler,'reduced Euler',euler-1)
assert euler-1 == -15
