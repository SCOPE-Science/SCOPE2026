"""Reproducible integral Morse reduction for the independence complex of a truncated octahedron."""
import collections,itertools,heapq,math,hashlib,time
import networkx as nx
V=sorted({v for a,b in itertools.product((-1,1),repeat=2) for v in itertools.permutations((0,a,2*b))});n=len(V)
E=[(i,j) for i in range(n) for j in range(i+1,n) if sum((V[i][k]-V[j][k])**2 for k in range(3))==2]; A=[0]*n
for i,j in E:A[i]|=1<<j;A[j]|=1<<i
F=set()
def visit(m,options):
 if m:F.add(m)
 while options:
  bit=options&-options;options-=bit;v=bit.bit_length()-1
  visit(m|bit,options & ~A[v])
visit(0,(1<<n)-1)
by_card=collections.Counter(m.bit_count() for m in F)
remaining=F.copy();matched={}
for v in range(n):
 bit=1<<v
 for m in list(remaining):
  if m&bit or m|bit not in remaining:continue
  upper=m|bit
  remaining.remove(m);remaining.remove(upper)
  matched[m]=upper
critical=sorted(remaining)
print('F',sorted(by_card.items()),'MATCHES',len(matched),'CRITICAL',[(m.bit_count()-1,m) for m in critical],flush=True)
# Validate the global discrete Morse matching, not only the 5-6 subgraph.
# Unmatched face-cover edges point down; matched edges point up.
indeg_full={m:0 for m in F};children=collections.defaultdict(list);hasse=0
for up in F:
 x=up
 while x:
  bit=x&-x;x-=bit;lo=up^bit
  if not lo:continue
  hasse+=1
  if matched.get(lo)==up:src,dst=lo,up
  else:src,dst=up,lo
  children[src].append(dst);indeg_full[dst]+=1
front=collections.deque(m for m,d in indeg_full.items() if d==0);visited=0
while front:
 a=front.popleft();visited+=1
 for b in children[a]:
  indeg_full[b]-=1
  if indeg_full[b]==0:front.append(b)
assert visited==len(F),(visited,len(F))
print('FULL_ACYCLIC_HASSE',hasse,'visited',visited,flush=True)

# DAG on 5-6 matches: every matched 6-face has selected 5-face; other matched 5-faces in its boundary are downstream.
pairs56={lo:up for lo,up in matched.items() if lo.bit_count()==6}
print('PAIRS_5_6',len(pairs56))
def boundary(m):
 x=m;j=0
 while x:
  bit=x&-x;x-=bit
  yield m^bit, (-1 if j%2 else 1)
  j+=1
succ={a:set() for a in pairs56};indeg={a:0 for a in pairs56}
for lo,up in pairs56.items():
 for t,c in boundary(up):
  if t in pairs56 and t!=lo:succ[lo].add(t)
for a in succ:
 for b in succ[a]:indeg[b]+=1
heap=[a for a in indeg if indeg[a]==0];heapq.heapify(heap)
order=[]
while heap:
 a=heapq.heappop(heap);order.append(a)
 for b in succ[a]:
  indeg[b]-=1
  if indeg[b]==0:heapq.heappush(heap,b)
print('DAG',len(order),'OF',len(pairs56),flush=True)
assert len(order)==len(pairs56)
# Each matched 5-face is eliminated by the boundary of its paired 6-face (unit coefficient).
unit={lo:dict(boundary(up))[lo] for lo,up in pairs56.items()}
crit5=sorted(m for m in remaining if m.bit_count()==6)
assert len(crit5)==4
# explicit induced matchings of 6 independent edges
ind_match=[]
def visit_m(chosen,allowed):
 if len(chosen)==6:
  ind_match.append(tuple(chosen));return
 for k,e in enumerate(allowed):
  a,b=e;ban=(1<<a)|(1<<b)|A[a]|A[b]
  visit_m(chosen+[e],[f for f in allowed[k+1:] if not ((1<<f[0]|1<<f[1])&ban)])
visit_m([],E)
assert len(ind_match)==56,len(ind_match)
def sphere_chain(edges):
 out=collections.defaultdict(int)
 for choices in itertools.product((0,1), repeat=6):
  vertices=[e[k] for e,k in zip(edges,choices)]
  inv=sum(vertices[i]>vertices[j] for i in range(6) for j in range(i+1,6))
  sign=(-1)**(sum(choices)+inv)
  m=sum(1<<v for v in vertices)
  out[m]+=sign
 assert len(out)==64
 return dict(out)
def reduce_cycle(chain):
 chain=chain.copy()
 for lo in order:
  c=chain.get(lo,0)
  if c:
   k=c*unit[lo]
   for t,v in boundary(pairs56[lo]):
    chain[t]=chain.get(t,0)-k*v
    if chain[t]==0:del chain[t]
 for lo in pairs56:assert lo not in chain
 # Noncritical upper 5-faces may remain: they are uniquely determined by the critical coordinates through the lower 4-face boundary equations.
 return tuple(chain.get(m,0) for m in crit5)
chains=[sphere_chain(es) for es in ind_match]
coords=[reduce_cycle(c) for c in chains]
print('SPHERE_COORDS_COUNT',len(coords),'UNIQUE',len(set(coords)),'SAMPLE',coords[:6], 'ALL_PRIMITIVE', all(math.gcd(*c)==1 for c in coords),flush=True)
# 48 full signed permutation automorphisms, orbits of induced matchings
maps=[]
for p in itertools.permutations(range(3)):
 for s in itertools.product((-1,1),repeat=3):
  g=tuple(V.index(tuple(s[k]*v[p[k]] for k in range(3))) for v in V)
  maps.append((p,s,g))
assert len({g for p,s,g in maps})==48
# The coordinate model is the usual Cayley graph of adjacent transpositions in S4.
G0=nx.Graph();G0.add_nodes_from(range(n));G0.add_edges_from(E)
words=list(itertools.permutations(range(4)));where={w:i for i,w in enumerate(words)}
G1=nx.Graph();G1.add_nodes_from(range(len(words)))
for i,w in enumerate(words):
 for k in range(3):
  z=list(w);z[k],z[k+1]=z[k+1],z[k]
  G1.add_edge(i,where[tuple(z)])
assert nx.is_isomorphic(G0,G1)
assert sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(G0,G0).isomorphisms_iter())==48

support={frozenset(frozenset(e) for e in edges):i for i,edges in enumerate(ind_match)}
remaining_ids=set(range(len(ind_match)));orbits=[]
while remaining_ids:
 i=min(remaining_ids);es=ind_match[i]
 orbit={support[frozenset(frozenset((g[a],g[b])) for a,b in es)] for p,s,g in maps}
 remaining_ids-=orbit;orbits.append(sorted(orbit))
print('ORBITS',sorted(len(o) for o in orbits),flush=True)
for oo in orbits:
 if len(oo)==8:print('EIGHT_ORBIT_COORDS',[(i,coords[i]) for i in oo],flush=True)
# exact determinant/rank Smith of 4x56 matrix using sympy
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
A0=Matrix.hstack(*(Matrix(c) for c in coords));D=smith_normal_form(A0,domain=ZZ)
print('SMITH_NONZERO',tuple(D[i,i] for i in range(min(D.shape)) if D[i,i]))
for orb in orbits:
 M=Matrix.hstack(*(Matrix(coords[i]) for i in orb))
 D1=smith_normal_form(M,domain=ZZ)
 print('ORBIT_RESULT',len(orb),'rank',M.rank(),'smith',tuple(D1[i,i] for i in range(min(D1.shape)) if D1[i,i]),flush=True)
# select 4 columns determinant +/-1
orb8=next(o for o in orbits if len(o)==8)
orb8bases=[(ids,int(Matrix.hstack(*(Matrix(coords[i]) for i in ids)).det())) for ids in itertools.combinations(orb8,4)]
print('ORBIT8_UNIT_BASIS',next((v for v in orb8bases if abs(v[1])==1),None),flush=True)
basis=None
for ids in itertools.combinations(range(len(coords)),4):
 d=Matrix.hstack(*(Matrix(coords[i]) for i in ids)).det()
 if abs(d)==1:
  basis=(ids,d);break
print('UNIT_BASIS',basis,flush=True)
# find if an orbit of size 8 is a signed 4-point action, group module decomposition
# determine character by fixed oriented simplices, via signed simplicial Lefschetz since all reduced homology is in degree 5.
face_sets={k:[m for m in F if m.bit_count()==k] for k in range(1,13)}
def face_trace(g):
 total=-1
 for size,L in face_sets.items():
  for m in L:
   x=m;v=[]
   while x:
    b=x&-x;x-=b;v.append(g[b.bit_length()-1])
   m2=sum(1<<w for w in v)
   if m2!=m:continue
   inv=sum(v[i]>v[j] for i in range(size) for j in range(i+1,size))
   total+=(-1)**(size-1+inv)
 return -total
chrs={((p,s)):face_trace(g) for p,s,g in maps}
print('CHAR_VALUES_MULT',dict(collections.Counter(chrs.values())),flush=True)
assert chrs[((0,1,2),(1,1,1))]==4
assert chrs[((0,1,2),(-1,-1,-1))]==-4
# Exact identification of the rational character: for the proper rotation R,
# R permutes the four unoriented cube diagonals; the character is the sum of
# the sign of this S4 permutation and its 3-dimensional standard character.
diags=[(1,a,b) for a,b in itertools.product((-1,1), repeat=2)]
def perm_sign(u):
 return (-1)**sum(u[i]>u[j] for i in range(len(u)) for j in range(i+1,len(u)))
for p,s,g in maps:
 delta=perm_sign(p)*math.prod(s)
 Q=[]
 for v in diags:
  vv=tuple(delta*s[k]*v[p[k]] for k in range(3))
  if vv[0]==-1:vv=tuple(-x for x in vv)
  Q.append(diags.index(vv))
 predicted=delta*(perm_sign(Q)+sum(Q[i]==i for i in range(4))-1)
 assert chrs[p,s]==predicted,((p,s),chrs[p,s],predicted)
print('ALL_48_CHARACTER_VALUES_MATCH_SIGN_PLUS_STANDARD_TWIST',flush=True)
# A second, chain-level check of the entire integral action: represent 48 maps
# on the certified unimodular geometric basis and compare to Lefschetz traces.
base_ids=next(ids for ids,d in orb8bases if abs(d)==1)
B=Matrix.hstack(*(Matrix(coords[i]) for i in base_ids))
assert abs(B.det())==1
B_inv=B.inv()
def push(c,g):
 out=collections.defaultdict(int)
 for m,v in c.items():
  a=[];x=m
  while x:
   b=x&-x;x-=b;a.append(g[b.bit_length()-1])
  inv=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
  out[sum(1<<t for t in a)]+=v*(-1 if inv%2 else 1)
 return {m:v for m,v in out.items() if v}
actions={}
for p,s,g in maps:
 M=Matrix.hstack(*(B_inv*Matrix(reduce_cycle(push(chains[i],g))) for i in base_ids))
 assert all(x.q==1 for x in M)
 assert int(M.trace())==chrs[p,s]
 assert abs(int(M.det()))==1
 actions[(p,s)]=M
assert actions[((0,1,2),(-1,-1,-1))]==-Matrix.eye(4)
print('ALL_48_INTEGRAL_ACTION_MATRICES_MATCH_LEFSCHETZ',flush=True)
print('VERIFY_OK_TRUNCATED_OCTAHEDRAL_H5_OCTAHEDRAL_ACTION')
