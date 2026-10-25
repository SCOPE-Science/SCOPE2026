#!/usr/bin/env python3
"""Self-contained finite structural verifier for icosahedral independence homology."""
import itertools
from collections import Counter
import networkx as nx

N=12
T,B=10,11
U=tuple(range(5))
V=tuple(range(5,10))

def u(i): return i%5
def v(i): return 5+i%5

def graph():
 G=nx.Graph(); G.add_nodes_from(range(12))
 for i in range(5):
  G.add_edges_from([(T,u(i)),(B,v(i)),(u(i),u(i+1)),(v(i),v(i+1)),(u(i),v(i)),(u(i),v(i-1))])
 return G

G=graph()
assert len(G)==12 and G.number_of_edges()==30 and set(dict(G.degree()).values())=={5}
all_pairs=set(itertools.combinations(range(12),2))
comp_edges={x for x in all_pairs if not G.has_edge(*x)}
tri={x for x in itertools.combinations(range(12),3) if all(tuple(sorted(e)) in comp_edges for e in itertools.combinations(x,2))}
assert len(tri)==20 and len(comp_edges)==36
mult=Counter(tuple(sorted(e)) for t in tri for e in itertools.combinations(t,2))
sphere_edges={e for e in comp_edges if mult[e]==2}
left_edges={e for e in comp_edges if mult[e]==0}
assert len(sphere_edges)==30 and len(left_edges)==6
assert all(mult[e] in (0,2) for e in comp_edges)

J=nx.Graph();J.add_nodes_from(range(12));J.add_edges_from(sphere_edges)
assert nx.is_connected(J) and set(dict(J.degree()).values())=={5}
for x in range(12):
 link=nx.Graph()
 link.add_nodes_from(J.neighbors(x))
 link.add_edges_from([tuple(sorted(t-set([x]))) for t in map(set,tri) if x in t])
 assert nx.is_isomorphic(link,nx.cycle_graph(5))
assert nx.is_isomorphic(G,J)
assert 12-30+20==2

# Check formula J is isomorphic to G by a particular point permutation.
psi={T:T,B:B}
psi.update({u(i):v(2*i) for i in range(5)})
psi.update({v(i):u(2*i+4) for i in range(5)})
assert {tuple(sorted((psi[a],psi[b]))) for a,b in G.edges}==sphere_edges

# Antipodal pairs have distance 3, and are exactly the uncovered complementary edges.
distance= dict(nx.all_pairs_shortest_path_length(G))
assert left_edges=={(i,j) for i,j in itertools.combinations(range(12),2) if distance[i][j]==3}
assert all(sum(x in e for e in left_edges)==1 for x in range(12))
opp={a:b for a,b in left_edges}
opp.update({b:a for a,b in left_edges})
assert all(opp[opp[i]]==i for i in range(12))

# Canonical primitive fundamental cycle of 2-sphere S with consistent orientations.
edgecof={e:[] for e in sphere_edges}
for t in tri:
 for i in range(3):
  ed= t[:i]+t[i+1:]
  edgecof[ed].append((t,(-1)**i))
assert all(len(z)==2 for z in edgecof.values())
sign={next(iter(tri)):1}
while len(sign)<len(tri):
 old=len(sign)
 for ed,(a,b) in edgecof.items():
  (ta,sa),(tb,sb)=a,b
  if ta in sign and tb not in sign: sign[tb]=-sign[ta]*sa//sb
  if tb in sign and ta not in sign: sign[ta]=-sign[tb]*sb//sa
 assert len(sign)>old
assert all(sum(sign[t]*s for t,s in ab)==0 for ab in edgecof.values())

def permutation_sign(seq):
 return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def orientation_sign_on_sphere(g):
 image={tuple(sorted(g[x] for x in t)):sign[t]*permutation_sign([g[x] for x in t]) for t in tri}
 ratio={image[t]//sign[t] for t in tri}
 assert ratio in ({1},{-1})
 return next(iter(ratio))

def h1_trace(g):
 return sum((1 if (g[a],g[b])==(a,b) else -1 if (g[a],g[b])==(b,a) else 0) for a,b in sorted(left_edges))

def order(g):
 p={i:i for i in range(12)}
 for k in range(1,121):
  p={i:g[p[i]] for i in p}
  if all(p[i]==i for i in p): return k
 raise Exception('Order exceeds 120')

autos=[g for g in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
assert len(autos)==120
assert len({tuple(g[i] for i in range(12)) for g in autos})==120
h2char={tuple(g[i] for i in range(12)):orientation_sign_on_sphere(g) for g in autos}
rot=[g for g in autos if orientation_sign_on_sphere(g)==1]
assert len(rot)==60
central={i:opp[i] for i in range(12)}
assert any(g==central for g in autos)
assert orientation_sign_on_sphere(central)==-1
assert all({i:central[g[i]] for i in range(12)}=={i:g[central[i]] for i in range(12)} for g in autos)

# Every automorphism respects the sphere and antipodal pair structure.
assert all({tuple(sorted((g[a],g[b]))) for a,b in sphere_edges}==sphere_edges for g in autos)
assert all({tuple(sorted((g[a],g[b]))) for a,b in left_edges}==left_edges for g in autos)

counts=Counter((orientation_sign_on_sphere(g),order(g),h1_trace(g)) for g in autos)
assert counts=={(1,1,6):1,(1,2,-2):15,(1,3,0):20,(1,5,1):24,(-1,2,-6):1,(-1,2,2):15,(-1,6,0):20,(-1,10,-1):24} or False
# For central involution, order2, etc. (could be order2 even rotations).
for rotg in rot:
 o=order(rotg)
 expected={1:6,2:-2,3:0,5:1}[o]
 assert h1_trace(rotg)==expected
 assert h1_trace({i:central[rotg[i]] for i in range(12)})==-expected

print('VERTICES 12 GRAPH_EDGES 30 COMPLEMENT_EDGES 36')
print('INDEPENDENCE_FACE_VECTOR 12 36 20')
print('SPHERE_FACE_VECTOR 12 30 20')
print('SPHERE_VERTEX_LINKS 12_CYCLES_OF_LENGTH_5')
print('EXTRA_EDGES 6 = ANTIPODAL_PAIRS')
print('AUTOMORPHISMS 120 ROTATIONS 60 INVERSION_ANTIPODE TRUE')
for k,n in sorted(counts.items()):print('CLASS (sphere_degree,element_order,H1_trace) multiplicity',k,n)
print('ROTATION_H1_CHARACTER (1,2,3,5A,5B) = (6,-2,0,1,1)')
print('H2_CHARACTER = orientation_sign, antipodal_inversion_minus')
print('VERIFY_OK_ICOSAHEDRAL_INDEPENDENCE_INTEGRAL_MODULE')
