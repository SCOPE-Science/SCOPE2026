"""Exhaustive integer discrete-Morse certificates for two Johnson-neighborhood complexes.
Run with Python 3; requires no third-party libraries.
All computations are exact and use the graph's open neighborhoods.
"""
from itertools import combinations
from collections import defaultdict
from math import comb
import sys,time

def jd(n,k):
 v=list(combinations(range(n),k)); d={tuple(x):i for i,x in enumerate(v)}
 neighbors=[]
 for a in v:
  set_a=set(a)
  neighbors.append([j for j,b in enumerate(v) if len(set_a.intersection(b))==k-1])
 return v,neighbors

def complex_faces(n,k):
 vs,N=jd(n,k)
 faces=[set() for i in range(k*(n-k))]
 for ni in N:
  for s in range(1,1<<len(ni)):
   m=0
   for j,a in enumerate(ni):
    if s>>j&1: m|=1<<a
   faces[m.bit_count()-1].add(m)
 return vs,N,faces


from collections import Counter,deque
from itertools import combinations
import time,sys,math

ORD6=[4,1,2,3,0]+list(range(5,20))

def faces_and_pairs(n):
 vs,N,levels=complex_faces(n,3)
 faces=set.union(*levels)
 order=ORD6 if n==6 else list(range(len(vs)))
 remaining=set(faces); pairs={}
 for v in order:
  b=1<<v
  for x in list(remaining):
   if not x&b and (x|b) in remaining:
    remaining.remove(x);remaining.remove(x|b);pairs[x]=x|b
 return vs,N,levels,remaining,pairs

def check(n):
 t=time.time()
 vs,N,levels,crit,pairs=faces_and_pairs(n)
 cells=set.union(*levels)
 print('n',n,'verts',len(vs),'face_count',len(cells),'pairs',len(pairs),'crit',Counter(x.bit_count()-1 for x in crit),flush=True)
 id_of={c:i for i,c in enumerate(cells)}
 dag=[[] for _ in cells];indeg=[0]*len(cells);covers=0
 for d in range(1,len(levels)):
  for big in levels[d]:
   b_id=id_of[big];bb=big
   while bb:
    bt=bb&-bb;bb-=bt;sm=big^bt;small_id=id_of[sm]
    if pairs.get(sm)==big: src,dst=small_id,b_id
    else: src,dst=b_id,small_id
    dag[src].append(dst);indeg[dst]+=1;covers+=1
 del id_of
 queue=deque(i for i,x in enumerate(indeg) if x==0);seen=0
 while queue:
  u=queue.popleft();seen+=1
  for v in dag[u]:
   indeg[v]-=1
   if indeg[v]==0:queue.append(v)
 print('acyclic_check',seen,'/',len(cells),'cover_count',covers,'seconds',round(time.time()-t,2),flush=True)
 assert seen==len(cells)
 del dag,indeg
 # Compute integer Morse differential crit3 to crit2 using triangular elimination of matched dim2-dim3 pairs.
 pairs23={a:b for a,b in pairs.items() if a.bit_count()==3}
 def boundary(face):
  out={}; bits=[1<<i for i in range(face.bit_length()) if face>>i&1]
  for j,b in enumerate(bits):out[face^b]=(-1)**j
  return out
 boundaries={a:boundary(b) for a,b in pairs23.items()}
 coeff={a:d[a] for a,d in boundaries.items()}
 reverse={}
 for a,d in boundaries.items():
  reverse[a]=set(d).intersection(pairs23.keys())-{a}
 indeg2={a:0 for a in pairs23}
 for a,subs in reverse.items():
  for b in subs: indeg2[b]+=1
 queue=deque(a for a,j in indeg2.items() if j==0)
 order=[]
 while queue:
  a=queue.popleft();order.append(a)
  for b in reverse[a]:
   indeg2[b]-=1
   if indeg2[b]==0:queue.append(b)
 print('2-3 DAG',len(order),len(pairs23),flush=True)
 assert len(order)==len(pairs23)
 crit2={a for a in crit if a.bit_count()==3}
 crit3={a for a in crit if a.bit_count()==4}
 d3vals=[]
 for z in crit3:
  bd=boundary(z)
  for a in order:
   x=bd.pop(a,0)
   if not x:continue
   tsgn=x//coeff[a]
   for sm,sg in boundaries[a].items():
    if sm==a:continue
    v=bd.get(sm,0)-tsgn*sg
    if v:bd[sm]=v
    else:bd.pop(sm,None)
  d3vals.append({a:bd.get(a,0) for a in crit2 if bd.get(a,0)})
  # Keep every coefficient for gcd and exact integral Smith invariant
 vals=[val for row in d3vals for val in row.values()]
 print('morse_d3 coefficients',Counter(vals),'nonzero columns',sum(bool(c) for c in d3vals),'gcd',math.gcd(*vals) if vals else 0,'/',len(crit3),'time',round(time.time()-t,2),flush=True)
 assert len(d3vals)==len(crit3) and len(crit2)==1 and math.gcd(*vals)==2
 return (len(cells),len(pairs),len(crit2),len(crit3),covers)



def main():
 for n, expected in [(6,(8620,4238,1,142,41940)),(7,(136220,67723,1,772,839580))]:
  observed=check(n)
  assert observed==expected, (n,observed,expected)
 # At n=5, the complement symmetry makes J(5,3) a triangular graph;
 # the same acyclic matching has one critical point and 11 critical 3-cells.
 vs, neighborhood, cells, crit, pairs=faces_and_pairs(5)
 assert len(vs)==10
 assert Counter(x.bit_count()-1 for x in crit)=={0:1,3:11}
 # Independent acyclicity for the preceding rank-three Johnson case.
 full=set.union(*cells); idx={f:i for i,f in enumerate(full)}
 indeg=[0]*len(full); arrows=[[] for _ in full]
 for d in range(1,len(cells)):
  for big in cells[d]:
   bb=big
   while bb:
    b=bb&-bb;bb-=b; small=big^b
    a,z=(idx[small],idx[big]) if pairs.get(small)==big else (idx[big],idx[small])
    arrows[a].append(z); indeg[z]+=1
 q=deque(i for i,j in enumerate(indeg) if not j); visited=0
 while q:
  i=q.popleft();visited+=1
  for j in arrows[i]:
   indeg[j]-=1
   if not indeg[j]:q.append(j)
 assert visited==len(full), (visited,len(full))
 print('VERIFY_OK n=6,7 integral Morse homotopy certificates; n=5 boundary check')

if __name__ == '__main__':
 main()
