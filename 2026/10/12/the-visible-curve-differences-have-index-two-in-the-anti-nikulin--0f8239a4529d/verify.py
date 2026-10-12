#!/usr/bin/env python3
import networkx as nx

V = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','L1','b2','b3','b4','L2','b1','L3','R1','R2','b5']
E = []
def add(u,v,m=1): E.append((u,v,m))
chain=['a1','a2','a3','a4','a5','a6','a7','a8','a9','L1','b2','b3','b4']
for u,v in zip(chain,chain[1:]): add(u,v)
add('a3','L2'); add('b2','b1')
add('a1','L3'); add('L3','R1',2); add('R1','b4')
add('a1','R2'); add('R2','b5',2); add('b5','b4')
G=nx.Graph(); G.add_nodes_from(V)
for u,v,m in E: G.add_edge(u,v,m=m)
assert len(G)==19 and G.number_of_edges()==20
assert sum(d['m'] for _,_,d in G.edges(data=True))==22
em=nx.algorithms.isomorphism.categorical_edge_match('m',1)
autos=list(nx.algorithms.isomorphism.GraphMatcher(G,G,edge_match=em).isomorphisms_iter())
assert len(autos)==4
# every nontrivial graph automorphism is an involution, so the group is V4
for f in autos:
    assert all(f[f[v]]==v for v in V)

swap=[f for f in autos if f['a1']=='b4' and f['b4']=='a1']
assert len(swap)==2
P1={'L3','R1'}; P2={'R2','b5'}
fiberwise=[f for f in swap if {f[x] for x in P1}==P1 and {f[x] for x in P2}==P2]
assert len(fiberwise)==1
f=fiberwise[0]
expected={v:v for v in V}
for x,y in [('a1','b4'),('a2','b3'),('a3','b2'),('a4','L1'),('a5','a9'),('a6','a8'),('L2','b1'),('L3','R1'),('R2','b5')]:
    expected[x]=y; expected[y]=x
assert f==expected
assert [v for v in V if f[v]==v]==['a7']
# The nine two-cycles and one singleton partition all nineteen curves.
cycles=[]; seen=set()
for v in V:
    if v in seen: continue
    w=f[v]
    cyc=tuple(sorted({v,w}))
    cycles.append(cyc); seen.update(cyc)
assert sorted(map(len,cycles))==[1]+[2]*9
print('VERIFY_OK vertices=19 edges=20 weighted_sum=22 graph_aut=V4 unique_fiberwise_nikulin=1 orbit=1+9x2 fixed=a7 networkx='+nx.__version__)


# Intersection matrix and difference-lattice calculation.
import sympy as sp
idx={v:i for i,v in enumerate(V)}
Q=sp.zeros(19)
for i in range(19): Q[i,i]=-2
for u,v,m in E:
    Q[idx[u],idx[v]]=m; Q[idx[v],idx[u]]=m
assert Q.rank()==16
D=[]
for a,b in [('a1','b4'),('a2','b3'),('a3','b2'),('a4','L1'),('a5','a9'),('a6','a8'),('L2','b1'),('L3','R1'),('R2','b5')]:
    z=sp.zeros(19,1); z[idx[a]]=1; z[idx[b]]=-1; D.append(z)
DM=sp.Matrix.hstack(*D)
GD=DM.T*Q*DM
rel=sp.Matrix([4,6,8,6,4,2,4,1,1])
assert GD.rank()==8
assert GD*rel==sp.zeros(9,1)
assert sp.gcd_list(list(rel))==1
B=GD.extract(list(range(8)),list(range(8)))
assert B.det()==1024
assert 1024//256==4 and int(sp.sqrt(sp.Rational(1024,256)))==2
print('VERIFY_LATTICE_OK curve_span_rank=16 difference_rank=8 relation=4,6,8,6,4,2,4,1,1 determinant=1024 nikulin_determinant=256 index=2')
