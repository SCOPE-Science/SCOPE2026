"""Exact combinatorial certification of the spherical great-circle arrangement for the regular truncated tetrahedron.
All sign/cone/adjacency operations use signed integers; only the final spherical angle evaluation uses floats.
"""
import itertools, collections, math, json
import numpy as np
V=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=np.int64)
R=np.array([2*V[i]+V[j] for i in range(4) for j in range(4) if j!=i],dtype=np.int64)
F=[]
for i in range(4): F.append([3*i+j for j in range(3)])
for i in range(4):
 oth=[j for j in range(4) if j!=i]
 F.append([3*j+([k for k in range(4) if k!=j].index(k)) for j in oth for k in oth if j!=k])
E=[]
for i in range(4):
 for j,k in itertools.combinations([z for z in range(4) if z!=i],2):
  E.append((3*i+([z for z in range(4) if z!=i].index(j)), 3*i+([z for z in range(4) if z!=i].index(k))))
for i,j in itertools.combinations(range(4),2):
 E.append((3*i+([z for z in range(4) if z!=i].index(j)),3*j+([z for z in range(4) if z!=j].index(i))))
assert len(E)==18 and len(set(tuple(sorted(x)) for x in E))==18

def prim(x):
 x=np.array(x,dtype=np.int64);g=math.gcd(*[abs(int(q)) for q in x]);return tuple(int(q//g) for q in x)
rays=set()
for a,b in itertools.combinations(R,2):
 c=np.cross(a,b)
 if np.any(c):
  q=prim(c);rays.add(q);rays.add(tuple(-x for x in q))
Q=np.array(sorted(rays),dtype=np.int64)
M=Q@R.T # 132x12 exact
cell_data=[]
for signs in itertools.product((-1,1),repeat=12):
 sig=np.array(signs,dtype=np.int64)
 possible=np.all(M*sig>=0,axis=1)
 if not np.any(possible):continue
 valid=Q[possible]
 w=np.sum(valid,axis=0,dtype=np.int64)
 if np.any(R@w*sig<=0):continue
 # all extreme rays valid and sum is strictly inside -> full dimension cell
 assert np.linalg.matrix_rank(valid.astype(float))==3
 edges={};adj=collections.defaultdict(list)
 for i in range(12):
  at=[tuple(int(x) for x in v) for v in valid if R[i]@v==0]
  if not at:continue
  if len(at)!=2:
   raise RuntimeError(('boundary ray count',i,signs,at))
  a,b=at;edges[i]=(a,b);adj[a].append((b,i));adj[b].append((a,i))
 assert all(len(v)==2 for v in adj.values()),(signs,adj)
 assert len(adj)==len(valid),(signs,len(adj),len(valid))
 first=min(adj);out_edge=adj[first][0];prev=None;curr=first;cycle=[]
 while True:
  opts=adj[curr] if prev is None else [p for p in adj[curr] if p[0]!=prev]
  nxt,idx=opts[0];cycle.append(idx)
  if nxt==first:break
  prev,curr=curr,nxt
  assert len(cycle)<=len(adj)
 assert len(cycle)==len(adj)
 klist=[]
 for j in range(len(cycle)):
  a=R[cycle[j-1]]*sig[cycle[j-1]];b=R[cycle[j]]*sig[cycle[j]]
  k=int(a@b);assert -11<k<11;klist.append(k)
 act=[min(signs[i] for i in f)<0 and max(signs[i] for i in f)>0 for f in F]
 nt,nh=sum(act[:4]),sum(act[4:])
 # independently count intersected edges
 crossings=sum(signs[a]!=signs[b] for a,b in E)
 assert crossings==nt+nh,(signs,(nt,nh),crossings)
 area=2*math.pi-sum(math.acos(k/11) for k in klist)
 assert area>0
 cell_data.append({'signs':signs,'type':(nt,nh),'area':area,'edges':len(cycle),'angles':tuple(klist),'rays':len(valid)})
from collections import defaultdict,Counter
cnt=Counter(c['type'] for c in cell_data)
coefs=defaultdict(Counter); areas=defaultdict(float);sides=Counter()
for c in cell_data:
 coefs[c['type']].update(c['angles']); areas[c['type']]+=c['area'];sides[c['edges']]+=1
assert len(cell_data)==134
assert sum(cnt.values())==134
assert abs(sum(areas.values())-4*math.pi)<1e-11
assert dict(cnt)=={(0,4):6,(1,3):24,(1,4):48,(2,3):24,(2,4):24,(3,3):8}
print('EXHAUSTIVE: 4096 sign patterns tested ->',len(cell_data),'nonempty open spherical chambers')
print('Cell polygons:',dict(sides))
for typ in sorted(cnt):print('type',typ,'n_cells',cnt[typ], 'arccos_counts',sorted(coefs[typ].items()),'prob',areas[typ]/(4*math.pi))
print('Side probabilities:',{k:sum(v for typ,v in areas.items() if sum(typ)==k)/(4*math.pi) for k in (4,5,6)})
print('sum area',sum(areas.values()))
with open('incidence_certificate_recomputed.json','w') as f:
 json.dump({'chambers':len(cell_data),'counts':{str(k):v for k,v in cnt.items()},'angles':{str(k):dict(c) for k,c in coefs.items()},'probabilities':{str(k):areas[k]/(4*math.pi) for k in cnt},'total_area':sum(areas.values()),'sign_patterns_tested':2**12,'ray_count':len(Q),'cell_edge_counts':dict(sides)},f,indent=2)
