"""Check cyclic collapse templates and sphere-bundle local data.

Usage: python3 verify_cycle3.py
Only Python's standard library is required.
Finite tests corroborate the local combinatorial proof in RESULT.md.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

CORE = [(0,1,2,6),(0,1,5,6),(0,2,3,4),(0,2,4,5),(0,2,5,6)]
# (free face, unique coface); all translations applied in listed order.
OPS = [
 ((0,1,2,4,5),(0,1,2,4,5,6)),
 ((0,1,2,4),(0,1,2,4,6)),
 ((0,1,2,5),(0,1,2,5,6)),
 ((0,1,3,4),(0,1,3,4,5)),
 ((0,1,2,-3),(0,1,2,-4,-3)),
 ((0,1,2,-4),(0,1,2,-4,-2)),
 ((0,1,3),(0,1,3,5)),
 ((0,2,-3),(0,2,-4,-3)),
 ((0,1,4),(0,1,4,5)),
 ((0,2,-4),(0,2,-4,-2))
]

def cyc(s,n,i=0):
 return tuple(sorted((x+i)%n for x in s))

def faces(n):
 result=[set() for _ in range(6)]
 for c in range(n):
  N=cyc((-3,-2,-1,1,2,3),n,c)
  for k in range(1,7):
   result[k-1].update(combinations(N,k))
 return result

def check(n):
 F=faces(n)
 for sig,tau in OPS:
  d=len(tau)-1
  S=[cyc(sig,n,i) for i in range(n)]
  T=[cyc(tau,n,i) for i in range(n)]
  assert len(set(S))==n and len(set(T))==n
  ct=Counter(face for z in F[d] for face in combinations(z,len(z)-1))
  for s,t in zip(S,T):
   assert s in F[d-1] and t in F[d] and set(s).issubset(t)
   assert ct[s]==1,(n,s,t,ct[s])
   assert all(s not in z for dd in range(d+1,6) for z in F[dd])
  F[d-1].difference_update(S)
  F[d].difference_update(T)
 assert [len(a) for a in F]==[n,6*n,10*n,5*n,0,0]
 coreset={cyc(P,n,i) for P in CORE for i in range(n)}
 assert F[3]==coreset
 for f in F[3]:
  for q in combinations(f,3):assert q in F[2]
 for f in F[2]:
  assert sum(f in set(t) or set(f).issubset(t) for t in F[3])==2
 for v in range(n):
  link={tuple(x for x in t if x!=v) for t in F[3] if v in t}
  ee=Counter(e for t in link for e in combinations(t,2))
  assert len(link)==20 and len(ee)==30 and all(d==2 for d in ee.values())
  assert len({x for t in link for x in t})==12
  assert is_connected_triangles(link)
 return F

def is_connected_triangles(tris):
 t=list(tris);reach={0};queue=[0]
 while queue:
  a=queue.pop()
  for b in range(len(t)):
   if b not in reach and len(set(t[a])&set(t[b]))==2:
    reach.add(b);queue.append(b)
 return len(reach)==len(t)

def lift_check():
 T={tuple(x+i for x in P):(i,j) for i in range(-18,19) for j,P in enumerate(CORE)}
 # The vertex link at 0 has icosahedral f-vector (12,30,20).
 link={tuple(x for x in f if x!=0) for f in T if 0 in f}
 E={e for tri in link for e in combinations(tri,2)}
 assert (len({v for f in link for v in f}),len(E),len(link))==(12,30,20)
 for sign in [-1,1]:
  half={f for f in link if all(v*sign>0 for v in f)}
  edge=Counter(e for f in half for e in combinations(f,2))
  assert (len({v for f in half for v in f}),len(edge),len(half))==(6,10,5)
  assert sum(x==1 for x in edge.values())==5
  assert all(x in (1,2) for x in edge.values())
  assert is_connected_triangles(half)
 # A half-integral height level cuts 27 tetrahedra into triangles or quads.
 crossing=[f for f in T if min(f)<.5<max(f)]
 V={(a,b) for f in crossing for a,b in combinations(f,2) if a<=0<b}
 E=set()
 polygons=[]
 for f in crossing:
  vertices={(a,b) for a,b in combinations(f,2) if a<=0<b}
  assert len(vertices) in (3,4)
  polygons.append(vertices)
  for tri in combinations(f,3):
   ee=frozenset((a,b) for a,b in combinations(tri,2) if a<=0<b)
   if len(ee)==2:E.add(ee)
 assert (len(V),len(E),len(polygons))==(21,46,27)
 assert len(V)-len(E)+len(polygons)==2
 seen={0}; queue=[0]
 while queue:
  x=queue.pop()
  for j in range(len(polygons)):
   if j not in seen and len(polygons[x]&polygons[j])==2:
    seen.add(j);queue.append(j)
 assert len(seen)==len(polygons)
 # The oriented tetrahedra in the infinite cover have signs
 # (-1)^i*(1,-1,1,1,1) for the five templates.
 incidence=defaultdict(list)
 for f,(i,j) in T.items():
  orient=(-1 if i%2 else 1)*(1,-1,1,1,1)[j]
  for k in range(4):
   incidence[f[:k]+f[k+1:]].append((f,orient*(-1 if k%2 else 1)))
 for face,occurrences in incidence.items():
  if len(occurrences)==2:
   assert occurrences[0][1]+occurrences[1][1]==0,(face,occurrences)
 assert (1,-1,1,1,1)!=(-1,1,-1,-1,-1)

if __name__=='__main__':
 for n in range(13,37):check(n)
 lift_check()
 print('VERIFY_OK sizes=13..36 collapse_orbits=10 final_f=(n,6n,10n,5n)')
 print('VERIFY_OK vertex_links=icosahedral level=(21,46,27) orientation_shift=-1')
