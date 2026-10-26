"""Enumerate all Eulerian subsets of the binary de Bruijn graph B(4,2)."""
from collections import Counter,deque
from itertools import combinations
from math import comb
N=5; V=1<<(N-1); E=1<<N; MASK=V-1
T=[e>>1 for e in range(E)]
H=[e&MASK for e in range(E)]
# Compute GF2 nullspace of incidence parity equations.
rows=[0]*V
for e,(t,h) in enumerate(zip(T,H)):
 if t!=h:
  rows[t]^=1<<e;rows[h]^=1<<e
piv={}
for row in rows:
 r=row
 while r:
  c=r.bit_length()-1
  if c in piv:r^=piv[c]
  else:piv[c]=r;break
free=[i for i in range(E) if i not in piv]
assert len(free)==17

# systematic gaussian columns: reduced row-echelon, pivot highest bit
for p in sorted(piv,reverse=True):
 for x in piv:
  if x!=p and piv[x]>>p&1:piv[x]^=piv[p]
basis=[]
for f in free:
 v=1<<f
 for p,row in piv.items():
  if row>>f&1:v|=1<<p
 basis.append(v)
for b in basis:
 assert all((r&b).bit_count()%2==0 for r in rows)

def balanced(z):
 for v in range(V):
  a=((z>>(2*v))&3).bit_count() # outgoing edges represented e = v*2 + bit, wait T[e]=e>>1 yes
  # incoming edges target v correspond e=(v<<1)&MASK | (0 or16)? derive H[e]=e&15
  k=v
  c=((z>>k)&1)+((z>>(k+V))&1)
  if a!=c:return False
 return True

def connected(z):
 # residual graph, and require >= N retained words
 r=(1<<E)-1-z
 if r.bit_count()<N:return False
 # For all active vertices, undirected BFS on surviving edges
 adj=[0]*V
 active=0
 for e in range(E):
  if r>>e&1:
   a,b=T[e],H[e];active|=1<<a|1<<b;adj[a]|=1<<b;adj[b]|=1<<a
 seen=0;st=active&-active
 while st:
  u=st.bit_length()-1;st^=1<<u
  if seen>>u&1:continue
  seen|=1<<u;st|=adj[u]&~seen
 return seen==active

balanced_counts=Counter();ok=Counter();bad=Counter();total=0
for subset in range(1<<len(basis)):
 z=0
 for j,b in enumerate(basis):
  if subset>>j&1:z^=b
 if not balanced(z):continue
 total+=1;s=z.bit_count();balanced_counts[s]+=1
 if connected(z):ok[s]+=1
 else:bad[s]+=1
assert len(basis)==17 and total==6600
assert [ok.get(i,0) for i in range(E+1)]==[1,2,2,4,8,14,26,38,56,86,126,166,199,230,254,250,240,204,168,130,98,68,51,30,20,12,9,6,0,0,0,0,0]
print('PARITY_ORDER5_UNIVERSAL_CYCLE_PASS basis=17 balanced=6600')
for s in range(E+1):
 pass
assert sum(balanced_counts.values())==total
