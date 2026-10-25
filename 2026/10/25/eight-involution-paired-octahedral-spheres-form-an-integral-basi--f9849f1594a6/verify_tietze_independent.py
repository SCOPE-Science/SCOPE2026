#!/usr/bin/env python3
"""Independent model and finite-field/Lefschetz cross-check for Tietze J3."""
from collections import Counter,defaultdict
import networkx as nx

# Independent flower graph J_3 = three four-vertex stars, a B triangle, a twisted C-D hexagon.
n=3
A=[4*i for i in range(n)]; B=[4*i+1 for i in range(n)]
C=[4*i+2 for i in range(n)]; D=[4*i+3 for i in range(n)]
e=set()
def add(a,b):e.add(tuple(sorted((a,b))))
for i in range(n):
    add(A[i],B[i]);add(A[i],C[i]);add(A[i],D[i]);add(B[i],B[(i+1)%n])
CD=C+D
for i in range(2*n):add(CD[i],CD[(i+1)%(2*n)])
H=nx.Graph();H.add_edges_from(e)
assert H.number_of_nodes()==12 and H.number_of_edges()==18
p_edges={tuple(sorted((i,(i+1)%5))) for i in range(5)}
p_edges.update(tuple(sorted((i,i+5))) for i in range(5))
p_edges.update(tuple(sorted((5+i,5+(i+2)%5))) for i in range(5))
tee=nx.Graph()
tee.add_edges_from(sorted(edge for edge in p_edges if 0 not in edge))
tee.add_edges_from([(10,11),(11,12),(10,12),(1,10),(4,11),(5,12)])
assert nx.is_isomorphic(H,tee)

ed=sorted(e); N=len(ed)
conf=[sum(1<<j for j,f in enumerate(ed) if set(edge)&set(f) and i!=j) for i,edge in enumerate(ed)]
faces=[];by=defaultdict(list)
for mask in range(1,1<<N):
    if all(not(mask>>i&1) or not(mask&conf[i]) for i in range(N)):
        faces.append(mask);by[mask.bit_count()-1].append(mask)
assert len(faces)==1051

def rank2(rows):
    piv={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i in piv:x^=piv[i]
            else:piv[i]=x;break
    return len(piv)

ranks={}
for d in range(1,6):
    subs={f:i for i,f in enumerate(by[d-1])}
    columns=[]
    for f in by[d]:
        mask=0
        for i in range(N):
            if f>>i&1:mask^=1<<subs[f^(1<<i)]
        columns.append(mask)
    ranks[d]=rank2(columns)
assert ranks=={1:17,2:100,3:235,4:157,5:8},ranks

Auts=list(nx.algorithms.isomorphism.GraphMatcher(H,H).isomorphisms_iter())
assert len(Auts)==12
index={edge:i for i,edge in enumerate(ed)}
traces=[]
for p in Auts:
    perm=[index[tuple(sorted((p[a],p[b])))] for a,b in ed]
    lefs=0
    for mask in faces:
        mapped=[perm[i] for i in range(N) if mask>>i&1]
        if sum(1<<j for j in mapped)!=mask:continue
        inv=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        lefs+=(-1)**((mask.bit_count()-1)+inv)
    # Reduced Lefschetz: ordinary alternating chain trace minus 1.
    traces.append(1-lefs)
assert Counter(traces)=={0:9,-2:2,16:1},traces
print('VERIFY_OK_INDEPENDENT_TIETZE_J3_AND_LEFSCHETZ')
print('INDEPENDENT_FLOWER_J3_ISOMORPHISM_TRUE')
print('MOD2_BOUNDARY_RANKS',ranks)
print('MOD2_REDUCED_BETTI3',len(by[3])-ranks[3]-ranks[4])
print('DIRECT_SIGNED_LEFSCHETZ_TRACES',dict(Counter(traces)))
