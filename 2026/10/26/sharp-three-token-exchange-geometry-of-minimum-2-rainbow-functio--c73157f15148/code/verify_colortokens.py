"""Exhaustive, independently encoded 2-rainbow-domination certificate for the 4-cube."""
from itertools import combinations, permutations
from collections import Counter, deque
from math import comb

V=tuple(range(16))
N=tuple(sum(1<<(v^(1<<j)) for j in range(4)) for v in V)
counts=[]
opt=[]
for k in range(8):
 c=0
 for tokens in combinations(range(32),k):
  a=b=0
  for t in tokens:
   if t<16:a|=1<<t
   else:b|=1<<(t-16)
  empty=(~(a|b))&65535
  works=True
  while empty:
   p=empty & -empty;v=p.bit_length()-1;empty^=p
   if not (a & N[v]) or not (b & N[v]):works=False;break
  if works:
   c+=1
   if k==7:opt.append((a,b))
 counts.append(c)
assert counts[:7]==[0]*7
assert len(opt)==320
S=set(opt)
assert len(S)==320
orbit_sizes=[]
remaining=set(S)
while remaining:
 a,b=next(iter(remaining))
 orbit=set()
 for pi in permutations(range(4)):
  p=[sum(((v>>j)&1)<<pi[j] for j in range(4)) for v in V]
  for shift in V:
   aa=sum(1<<(p[v]^shift) for v in V if a&(1<<v))
   bb=sum(1<<(p[v]^shift) for v in V if b&(1<<v))
   orbit.add((aa,bb));orbit.add((bb,aa))
 assert orbit<=S
 remaining-=orbit
 orbit_sizes.append(len(orbit))
assert sorted(orbit_sizes)==[128,192]
assert Counter((a&b).bit_count() for a,b in opt)==Counter({0:192,1:128})

packed=sorted(a|(b<<16) for a,b in opt)
adj=[[] for _ in packed]
pairdist=Counter()
for i in range(320):
 for j in range(i+1,320):
  dist=(packed[i]^packed[j]).bit_count()//2
  pairdist[dist]+=1
  if dist==3:adj[i].append(j);adj[j].append(i)
assert pairdist==Counter({3:4320,4:1440,5:22080,6:11520,7:11680})
assert set(map(len,adj))=={27}
classes=[((x&65535)&(x>>16)).bit_count() for x in packed]
degree_types=Counter()
edge_types=Counter()
for i in range(320):
 local=Counter(classes[j] for j in adj[i])
 degree_types[(classes[i],local[0],local[1])]+=1
 for j in adj[i]:
  if i<j:edge_types[tuple(sorted((classes[i],classes[j])))]+=1
assert degree_types==Counter({(0,15,12):192,(1,18,9):128})
assert edge_types==Counter({(0,0):1440,(0,1):2304,(1,1):576})
assert sum(map(len,adj))//2==4320
hist=Counter()
for s in range(320):
 d={s:0};Q=deque([s])
 while Q:
  v=Q.popleft()
  for w in adj[v]:
   if w not in d:d[w]=d[v]+1;Q.append(w)
 assert len(d)==320
 hist[max(d.values())]+=1
assert hist==Counter({3:320})
print('enumerated_assignments',sum(comb(32,k) for k in range(8)))
print('feasible_by_weight_0_through_7',counts)
print('optima',len(opt),'orbit_sizes',sorted(orbit_sizes),'doubled_vertex_distribution',sorted(Counter((a&b).bit_count() for a,b in opt).items()))
print('token_distance_histogram',sorted(pairdist.items()))
print('distance_three_graph','vertices',320,'edges',4320,'degree',27,'components',1,'radius',3,'diameter',3)
print('orbit_partition_degrees',sorted(degree_types.items()),'orbit_edge_counts',sorted(edge_types.items()))
