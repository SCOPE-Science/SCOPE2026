"""Standalone exact certificate for cut complexes of the Petersen graph."""
from itertools import combinations
from collections import Counter,deque
from math import comb

V=list(combinations(range(5),2));N=len(V);assert N==10
adj=[0]*N
for i,a in enumerate(V):
 for j,b in enumerate(V):
  if i!=j and not set(a)&set(b):adj[i]|=1<<j

def connected(T):
 if not T:return False
 reach=(T & -T)
 while True:
  nxt=reach;z=reach
  while z:
   b=z&-z;z-=b
   nxt|=adj[b.bit_length()-1]&T
  if nxt==reach:break
  reach=nxt
 return reach==T

def complex_for(k):
 full=(1<<N)-1
 facet=[full^t for t in range(1<<N) if t.bit_count()==k and not connected(t)]
 faces={0}
 for s in facet:
  x=s
  while x:
   faces.add(x)
   x=(x-1)&s
 return facet,faces

def matching(faces,order):
 left=set(faces); low_to_high={}
 for v in order:
  b=1<<v
  for x in sorted(left):
   if not (x&b) and (x|b) in left:
    low_to_high[x]=x|b
    left.remove(x); left.remove(x|b)
 assert set(low_to_high).isdisjoint(set(low_to_high.values()))
 assert 2*len(low_to_high)+len(left)==len(faces)
 return left,low_to_high

def verify_matching(faces,m):
 indeg={x:0 for x in faces};edges={x:[] for x in faces}
 for f in faces:
  v=f
  while v:
   b=v&-v;v-=b;g=f^b
   x,y=(g,f) if m.get(g)==f else (f,g)
   edges[x].append(y);indeg[y]+=1
 ready=deque(x for x in faces if indeg[x]==0);count=0
 while ready:
  x=ready.popleft();count+=1
  for y in edges[x]:
   indeg[y]-=1
   if indeg[y]==0:ready.append(y)
 assert count==len(faces),(count,len(faces))
 return count

def boundary(f):
 out={};z=f;j=0
 while z:
  b=z&-z;z-=b
  out[f^b]= 1 if j%2==0 else -1
  j+=1
 return out

def morse_boundary(c,m,critical):
 z=boundary(c)
 for step in range(5000):
  lower=next((x for x in z if x in m and z[x]),None)
  if lower is None:break
  h=m[lower]
  coeff=z[lower]
  inc=boundary(h)[lower]
  assert inc in (1,-1)
  for q,b in boundary(h).items():
   z[q]=z.get(q,0)-coeff*inc*b
   if z[q]==0:del z[q]
 else:raise RuntimeError('gradient reduction did not terminate')
 assert not any(x in m for x in z)
 return {x:v for x,v in z.items() if x in critical}



def gf2_rank(columns):
 piv={}
 for x in columns:
  while x:
   p=x.bit_length()-1
   if p in piv:x^=piv[p]
   else:piv[p]=x;break
 return len(piv)

def independent_mod2_betti(faces):
 cells={d:sorted(f for f in faces if f and f.bit_count()==d+1)
        for d in range(max(f.bit_count() for f in faces))}
 ranks={}
 for d in range(1,len(cells)):
  idx={f:i for i,f in enumerate(cells[d-1])}
  cols=[]
  for f in cells[d]:
   col=0
   for j in range(N):
    if f>>j&1:col ^= 1<<idx[f^(1<<j)]
   cols.append(col)
  ranks[d]=gf2_rank(cols)
 betti={d:len(cells[d])-ranks.get(d,0)-ranks.get(d+1,0)
        for d in cells}
 betti[0]-=1
 return {d:v for d,v in betti.items() if v}

orders={5:[6,7,5,9,1,0,4,2,3,8],6:[9,5,2,0,4,3,7,8,1,6],7:[2,7,9,1,3,8,4,5,6,0]}
for k,order in orders.items():
 facets,faces=complex_for(k)
 crit,m=matching(faces,order)
 verify_matching(faces,m)
 dims=Counter(x.bit_count()-1 for x in crit)
 assert independent_mod2_betti(faces)==({3:1,4:5} if k==5 else {3:11} if k==6 else {1:11})
 print('k',k,'facets',len(facets),'faces',len(faces),'pairs',len(m),'critical dims',dict(sorted(dims.items())))
 assert not any(x==0 for x in crit)
 if k==5:
  lower=sorted(x for x in crit if x.bit_count()==4)
  upper=sorted(x for x in crit if x.bit_count()==5)
  B=[[morse_boundary(u,m,crit).get(l,0) for u in upper] for l in lower]
  print('Morse degree 4-to-3 matrix:')
  for row in B:print(row)
  # Rows 0..3 have a diagonal unit minor on columns 0,1,3,5.
  assert [[B[r][c] for c in (0,1,3,5)] for r in range(4)] == [
   [-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]]
  assert B[4]==[B[0][c]-B[1][c]-B[2][c]+B[3][c] for c in range(9)]
  # Four unit Smith factors follow: rank is at least four by the minor,
  # at most four by the displayed row relation, and their product is one.
  print('integer boundary: rank 4, unit 4x4 minor, free cokernel rank 1')
 if k in (6,7):
  assert dims==({3:11} if k==6 else {1:11})
 if k==7:
  assert len(faces)==51
 print('PASS',k)

for k in (8,9,10):
 facets,faces=complex_for(k)
 assert facets==[] and faces=={0}, (k,facets)
print('PASS: no disconnected induced subsets of size eight or more')
