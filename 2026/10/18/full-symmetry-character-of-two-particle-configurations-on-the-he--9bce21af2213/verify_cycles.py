"""Independent combinatorial checks for two-particle Heawood configurations."""
from itertools import combinations
import collections
lines=[frozenset((i+j)%7 for j in (0,1,3)) for i in range(7)]
n=14
edges=sorted((p,7+j) for j,L in enumerate(lines) for p in L)
idx={e:i for i,e in enumerate(edges)}
N=[set() for _ in range(n)]
for a,b in edges:N[a].add(b);N[b].add(a)
assert all(len(s)==3 for s in N)
assert len(edges)==21

def connected_without(removed):
 allowed=set(range(n))-set(removed)
 if not allowed: return True
 seen={next(iter(allowed))};q=list(seen)
 for v in q:
  for w in N[v]&allowed-seen:
   seen.add(w);q.append(w)
 return seen==allowed
assert all(connected_without(S) for k in range(3) for S in combinations(range(n),k))
print('VERTEX_CONNECTIVITY_AT_LEAST_3 true')
cycles=set()
for a in range(n):
 def walk(seq):
  if len(seq)==6:
   if a in N[seq[-1]]:
    t=tuple(seq); variants=[tuple(t[i:]+t[:i]) for i in range(6)]
    s=list(reversed(t));variants += [tuple(s[i:]+s[:i]) for i in range(6)]
    cycles.add(min(variants))
   return
  for b in N[seq[-1]]:
   if b not in seq: walk(seq+[b])
 walk([a])
assert len(cycles)==28
print('SIX_CYCLES',len(cycles))

def rank_mod3(vectors):
 piv={}
 for v in vectors:
  a=dict((i,x%3) for i,x in enumerate(v) if x%3)
  while a:
   i=min(a)
   if i not in piv:
    z=pow(a[i],-1,3);piv[i]={j:(x*z)%3 for j,x in a.items()};break
   fac=a[i]
   for j,x in piv[i].items():
    w=(a.get(j,0)-fac*x)%3
    if w:a[j]=w
    else:a.pop(j,None)
 return len(piv)
vecs=[]
for c in cycles:
 v=[0]*len(edges)
 for a,b in zip(c,c[1:]+c[:1]):
  e=tuple(sorted((a,b)));v[idx[e]]+=1 if a<b else -1
 vecs.append(v)
assert rank_mod3(vecs)==8
print('SIX_CYCLE_SPAN_RANK_MOD_3',8)
# No simple cycles of length <6: a 4-cycle would be two Fano points on two different lines.
assert all(len(lines[j]&lines[k])==1 for j,k in combinations(range(7),2))
print('GIRTH_AT_LEAST_6 true')
print('GRAPH_CYCLE_RANK',21-14+1)
print('PLANAR_GIRTH6_BOUND','21 > 3*(14-2)/2 = 18',flush=True)
