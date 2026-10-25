from itertools import combinations
N=7;POLY=0b10000011;Q=1<<N

def mul(a,b):
 out=0
 while b:
  if b&1:out^=a
  b>>=1;a<<=1
  if a&Q:a^=POLY
 return out

def powgf(a,e):
 r=1
 while e:
  if e&1:r=mul(r,a)
  a=mul(a,a);e>>=1
 return r
F=[powgf(i,11) for i in range(Q)]
S={}; Z=[]
for a,b,c in combinations(range(1,Q),3):
 if c==(a^b):continue
 mask=(1<<a)|(1<<b)|(1<<c)|(1<<(a^b))|(1<<(a^c))|(1<<(b^c))|(1<<(a^b^c))
 if mask in S:continue
 S[mask]=1
 t=F[a]^F[b]^F[c]^F[a^b]^F[a^c]^F[b^c]^F[a^b^c]
 if t==0:Z.append(mask)
print('all blocks',len(S),'zero',len(Z))
base=Z[0]; pts=[a for a in range(1,Q) if base>>a&1];print('seed',pts)
Zset=set(Z);orbits={}
for r in range(1,Q):
 new=0
 for a in pts:new |= 1<<mul(a,r)
 orbits[new]=r
print('orbitsize',len(orbits),'matches',set(orbits)==Zset)
K={}
for mask in Z:
 if mask==base:continue
 isec=(mask & base).bit_count()
 K[isec]=K.get(isec,0)+1
print('nonzero intersections',K)
# incidence graph on blocks
Z=sorted(Z); V=len(Z);A=[[0]*V for _ in range(V)];adj=[set() for _ in range(V)]
for i in range(V):
 for j in range(i+1,V):
  if (Z[i]&Z[j]).bit_count()==1:
   A[i][j]=A[j][i]=1; adj[i].add(j);adj[j].add(i)
print('degree',sorted(set(map(len,adj))))
counts={}; triangles=0
for i in range(V):
 for j in range(i+1,V):
  common=len(adj[i]&adj[j]);typ=(1 if j in adj[i] else 0,common)
  counts[typ]=counts.get(typ,0)+1
  if j in adj[i]:triangles+=common
print('common neighbour pair distribution',sorted(counts.items()))
print('triangles',triangles//3)
# reciprocal spectrum of common neighborhoods? triangle orbits

assert len(S)==11811 and len(Z)==127
assert set(orbits)==Zset
assert sorted(map(len,adj))==[42]*127
assert counts=={(0,8):889,(0,10):889,(0,12):1778,(0,14):889,(0,16):889,(1,15):1778,(1,21):889}
assert triangles//3==15113
print('DIRECT_GRAPH_CERTIFICATE_OK pairs=8001 triangles=15113')
