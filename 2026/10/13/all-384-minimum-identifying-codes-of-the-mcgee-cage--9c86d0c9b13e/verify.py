#!/usr/bin/env python3
"""Reproduce the minimum identifying-code census and symmetry classes of the McGee graph.
Requires Python >=3.10, a C++17 compiler and networkx >=3.0.
Run: python3 verify.py (from any directory).
"""
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import networkx as nx

HERE=Path(__file__).resolve().parent
EXPECTED={
 (1919283,16,2,6), (1462891,16,6,5),
 (1140085,32,2,4), (1664369,32,2,5), (1403187,32,2,6),
 (1402169,32,3,4), (1134197,32,3,5), (1395507,32,3,5),
 (1395303,32,4,4), (600041,32,4,5), (697203,32,4,5),
 (1219301,32,5,4), (1225331,32,5,6)
}
with TemporaryDirectory() as directory:
    binary=Path(directory)/'mcgee_codes'
    subprocess.run(['c++','-std=c++17','-O3',str(HERE/'verify.cpp'),'-o',str(binary)],check=True)
    output=subprocess.run([str(binary)],capture_output=True,text=True,check=True).stdout.splitlines()
assert output[0]=='CENSUS_OK N=24 tests=300 k10=0 k11=384 methods=signatures+separators'
codes={int(line.split()[1]) for line in output[1:]}
assert len(codes)==384 and len(output)==385

# Independently construct the LCF graph and check the masks.
G=nx.LCF_graph(24,[-12,7,-7],8)
assert G.number_of_nodes()==24 and G.number_of_edges()==36
assert all(d==3 for _,d in G.degree())
assert len(nx.cycle_basis(G))>=1
assert nx.girth(G)==7
closed=[(1<<v)|sum(1<<w for w in G.neighbors(v)) for v in range(24)]
for c in codes:
    signatures=[c&b for b in closed]
    assert all(signatures) and len(set(signatures))==24

# GraphMatcher enumerates every edge-preserving bijection, not a subgroup sample.
aut=[tuple(p[v] for v in range(24)) for p in nx.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
assert len(aut)==32 and len(set(aut))==32
for p in aut:
    assert set(p)==set(range(24))
    assert all(G.has_edge(p[u],p[v]) for u,v in G.edges())
A={p[0] for p in aut}
assert A=={0,3,6,9,12,15,18,21}
B=set(range(24))-A

def act(code,perm):
    out=0
    for v in range(24):
        if code>>v&1: out|=1<<perm[v]
    return out

pending=set(codes)
orbits=[]
while pending:
    rep=min(pending)
    orbit={act(rep,p) for p in aut}
    assert orbit<=pending
    pending.difference_update(orbit)
    a=sum(bool(rep>>v&1) for v in A)
    e=sum(bool(rep>>u&1 and rep>>v&1) for u,v in G.edges())
    orbits.append((rep,len(orbit),a,e))
assert set(orbits)==EXPECTED
assert Counter(s for _,s,_,_ in orbits)==Counter({32:11,16:2})
assert sum(s for _,s,_,_ in orbits)==384
print('VERIFY_OK graph=McGee(24,36,girth7) exhaustive_masks=C(24,10)+C(24,11)=4457400')
print('VERIFY_OK gamma_ID=11 optimum_codes=384 independent_conditions=2 automorphisms=32 orbits=13 orbit_sizes=16x2+32x11')
print('VERIFY_OK eight_vertex_orbit=0,3,...,21 orbit_representatives=',','.join(map(str,sorted(x[0] for x in orbits))))
