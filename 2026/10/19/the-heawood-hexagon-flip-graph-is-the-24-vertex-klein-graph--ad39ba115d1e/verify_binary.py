#!/usr/bin/env python3
"""Independent exact computation using binary-vector Fano incidences."""
from collections import Counter, deque
from itertools import combinations

P=range(1,8)  # nonzero vectors in the 3-dimensional binary vector space
F=range(1,8)  # nonzero binary linear forms, representing Fano lines

def dot(a,x):
 t=a&x
 return t.bit_count()%2

options={x:[a for a in F if dot(a,x)==0] for x in P}
assert all(len(z)==3 for z in options.values())
assert len({tuple(a for a in F if dot(a,x)==0) for x in P})==7
matchings=[]
def extend(x,used,chosen):
 if x==8:
  matchings.append(tuple(chosen));return
 for a in options[x]:
  if a not in used:
   extend(x+1,used|{a},chosen+[a])
extend(1,set(),[])
assert len(matchings)==24

# Independent legal-move definition: permute the line partners of exactly
# three point vertices in a cycle. Every assigned incidence must survive.
index={p:i for i,p in enumerate(matchings)}
adj=[set() for _ in matchings]
for i,m in enumerate(matchings):
 for selected in combinations(range(7),3):
  a,b,c=selected
  for assignment in ((m[b],m[c],m[a]), (m[c],m[a],m[b])):
   if all(dot(assignment[t],P[selected[t]])==0 for t in range(3)):
    arr=list(m)
    for t,z in enumerate(selected):arr[z]=assignment[t]
    j=index[tuple(arr)]
    assert i!=j
    adj[i].add(j)
assert len({(min(i,j),max(i,j)) for i in range(24) for j in adj[i]})==84
assert all(len(x)==7 for x in adj)
assert all(i in adj[j] for i in range(24) for j in adj[i])

def distances(i):
 d={i:0};todo=deque([i])
 while todo:
  u=todo.popleft()
  for v in adj[u]:
   if v not in d:
    d[v]=d[u]+1;todo.append(v)
 return d

D=[distances(i) for i in range(24)]
classes=[]
for i in range(24):
 d=D[i]
 assert len(d)==24 and Counter(d.values())==Counter({0:1,1:7,2:14,3:2})
 for j,h in d.items():
  if h==0:continue
  a=sum(d[z]==h for z in adj[j])
  b=sum(d[z]==h+1 for z in adj[j])
  c=sum(d[z]==h-1 for z in adj[j])
  assert (a,b,c)=={1:(2,4,1),2:(4,1,2),3:(0,0,7)}[h]
  common=len(set(enumerate(matchings[i]))&set(enumerate(matchings[j])))
  assert h=={4:1,2:2,1:2,0:3}[common]
 C=frozenset(j for j,h in d.items() if h in (0,3))
 if C not in classes:classes.append(C)
assert len(classes)==8 and all(len(C)==3 for C in classes)
for C in classes:
 for p,q in combinations(C,2):
  assert set(enumerate(matchings[p])).isdisjoint(enumerate(matchings[q]))
 for u in C:
  assert all(len(adj[u]&other)==1 for other in classes if other!=C)

print('VERIFY_OK: binary-plane 24 perfect matchings and 84 3-cycle flips')
print('VERIFY_OK: 24 distance arrays, intersection (7,4,1;1,2,7)')
print('VERIFY_OK: 8 triple 1-factorization classes and antipodal K8 quotient')
