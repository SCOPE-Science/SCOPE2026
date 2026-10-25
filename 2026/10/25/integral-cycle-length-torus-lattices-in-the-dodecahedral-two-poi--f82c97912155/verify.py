#!/usr/bin/env python3
"""Exact cycle-length torus lattices in the two-point dodecahedral configuration space.

Requires Python 3.10+, SymPy 1.12+, and NetworkX 3.0+.
The enumerations, integral determinants, and Smith forms are recomputed.
"""
from collections import Counter, defaultdict
from itertools import combinations
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import networkx as nx

EDGE_LIST = [
    (0,1),(0,10),(0,19),(1,2),(1,8),(2,3),(2,6),(3,4),(3,19),
    (4,5),(4,17),(5,6),(5,15),(6,7),(7,8),(7,14),(8,9),
    (9,10),(9,13),(10,11),(11,12),(11,18),(12,13),(12,16),
    (13,14),(14,15),(15,16),(16,17),(17,18),(18,19)
]
EXPECTED = {
 (5,5):(36,36,()), (5,8):(120,36,(2,)),
 (5,9):(60,36,(2,)), (5,10):(72,36,(2,)),
 (5,11):(180,36,()), (5,12):(60,36,(2,)),
 (5,14):(60,30,(2,)), (8,8):(75,36,(2,)*12),
 (8,9):(60,36,(2,)*7), (8,10):(30,19,(2,)),
 (8,11):(60,36,(2,)*5), (9,9):(10,10,())
}
MINOR_ROWS = [
 0,2,4,6,9,12,15,17,25,27,31,33,36,40,42,75,77,79,85,88,90,
 121,126,129,132,134,163,166,169,174,203,206,211,239,242,284
]

def rank_mod(columns,p):
    pivot = {}
    for col in columns:
        w={i:v%p for i,v in col.items() if v%p}
        while w:
            i=min(w)
            if i in pivot:
                f=w[i]
                row=pivot[i]
                w={j:(w.get(j,0)-f*row.get(j,0))%p for j in w.keys()|row.keys()}
                w={j:v for j,v in w.items() if v}
            else:
                inv=pow(w[i],-1,p)
                pivot[i]={j:v*inv%p for j,v in w.items()}
                break
    return len(pivot)

def main():
    edges=EDGE_LIST
    assert edges == sorted(edges) and len(edges)==30
    assert len(set(edges))==30
    adj={u:set() for u in range(20)}
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    assert all(len(adj[u])==3 for u in range(20))
    G=nx.Graph(); G.add_nodes_from(range(20));G.add_edges_from(edges)
    GP=nx.Graph()
    for i in range(10):
        GP.add_edge(i,(i+1)%10)
        GP.add_edge(i,10+i)
        GP.add_edge(10+i,10+(i+2)%10)
    assert nx.is_isomorphic(G, GP)

    # Canonical simple cycles: first vertex is minimum, first successor < last.
    cycles=[]
    def visit(start,path,used):
        u=path[-1]
        for v in sorted(adj[u]):
            if v==start:
                if len(path)>=3 and path[1]<path[-1]:
                    cycles.append(tuple(path))
            elif v>start and v not in used:
                visit(start,path+[v],used|{v})
    for start in range(20):
        visit(start,[start],{start})
    assert len(cycles)==1168
    cycle_counts=Counter(map(len,cycles))
    assert cycle_counts == {5:12,8:30,9:20,10:36,11:120,12:100,
                            13:60,14:180,15:180,16:90,17:180,18:130,20:30}

    edge_index={edge:i for i,edge in enumerate(edges)}
    oriented=[]
    for cycle in cycles:
        d={}
        for u,v in zip(cycle, cycle[1:]+cycle[:1]):
            k=edge_index[tuple(sorted((u,v)))]
            d[k]=1 if u<v else -1
        assert len(d)==len(cycle)
        oriented.append(d)

    squares=[(i,j) for i in range(30) for j in range(i+1,30)
             if set(edges[i]).isdisjoint(edges[j])]
    assert len(squares)==375
    square_idx={e:i for i,e in enumerate(squares)}
    onecells=[(i,v) for i,(a,b) in enumerate(edges)
                for v in range(20) if v not in (a,b)]
    one_idx={q:i for i,q in enumerate(onecells)}
    vertices=list(combinations(range(20),2))
    zero_idx={q:i for i,q in enumerate(vertices)}
    assert len(vertices)==190 and len(onecells)==540
    d1=[]
    for i,v in onecells:
        a,b=edges[i]
        d1.append({zero_idx[tuple(sorted((b,v)))]:1,
                   zero_idx[tuple(sorted((a,v)))]:-1})
    d2=[]
    for i,j in squares:
        a,b=edges[i];c,d=edges[j]
        d2.append({one_idx[(j,b)]:1,one_idx[(j,a)]:-1,
                   one_idx[(i,d)]:-1,one_idx[(i,c)]:1})
    for col in d2:
        boundary={}
        for j,b in col.items():
            for k,a in d1[j].items():
                boundary[k]=boundary.get(k,0)+a*b
        assert all(v==0 for v in boundary.values())
    assert rank_mod(d2,101)==339
    assert rank_mod(d2,2)==339
    print('GRAPH_AND_CELLS',20,30,190,540,375)
    print('BOUNDARY2_RANK_MOD_101_AND_2',339,339)

    pairs=defaultdict(list)
    for i,c in enumerate(cycles):
        supp=set(c)
        for j in range(i+1,len(cycles)):
            if supp.isdisjoint(cycles[j]):
                pairs[tuple(sorted((len(c),len(cycles[j]))))].append((i,j))
    assert set(pairs)==set(EXPECTED)
    assert sum(map(len,pairs.values()))==823

    def torus(i,j):
        ans={}
        for k,a in oriented[i].items():
            for l,b in oriented[j].items():
                # This is the orientation inherited from the product of cycles,
                # taking the sign of the coordinate swap into account.
                assert k!=l and set(edges[k]).isdisjoint(edges[l])
                ans[square_idx[tuple(sorted((k,l)))]]=a*b*(1 if k<l else -1)
        return ans

    by_pair={q:[torus(*ij) for ij in pairs[q]] for q in EXPECTED}
    for group in by_pair.values():
        for v in group:
            boundary={}
            for k,s in v.items():
                for j,c in d2[k].items():
                    boundary[j]=boundary.get(j,0)+s*c
            assert all(x==0 for x in boundary.values())
    print('SIMPLE_CYCLES',len(cycles),'PRODUCT_TORI',sum(len(v) for v in by_pair.values()))

    # Thirty-six vertex-disjoint facial-pentagon tori form a primitive lattice.
    base=by_pair[(5,5)]
    assert len(base)==36
    minor=Matrix([[v.get(r,0) for v in base] for r in MINOR_ROWS])
    determinant=int(minor.det(method='domain-ge'))
    assert abs(determinant)==1, determinant
    inv=minor.inv()
    print('PENTAGON_TORUS_UNIT_MINOR',determinant,'MINOR_ROWS',MINOR_ROWS)
    # Since rank(d2) >=339 and 36 primitive independent cycles exist in C2,
    # ker(d2) has rank 36 and equals their primitive span integrally.
    assert len(base)+339 == 375
    for pair in sorted(EXPECTED):
        group=by_pair[pair]
        coordinates=inv*Matrix([[v.get(r,0) for v in group] for r in MINOR_ROWS])
        assert all(int(x)==x for x in coordinates)
        # Verify the projection is an equality of COMPLETE integral chains,
        # not just equality on thirty-six selected coordinates.
        for i in range(375):
            for j,v in enumerate(group):
                assert sum(base[k].get(i,0)*int(coordinates[k,j])
                           for k in range(36)) == v.get(i,0)
        smith=smith_normal_form(coordinates,domain=ZZ)
        invariants=[abs(int(smith[k,k])) for k in range(min(smith.shape))
                    if smith[k,k]!=0]
        result=(len(group),len(invariants),tuple(v for v in invariants if v!=1))
        assert result==EXPECTED[pair],(pair,result,EXPECTED[pair])
        print('PAIR',pair,'TORI',result[0],'LATTICE_RANK',result[1],
              'QUOTIENT_FREE_RANK',36-result[1],'TORSION_INVARIANTS',result[2])
    print('VERIFY_OK_DODECAHEDRON_LENGTH_PAIR_TORUS_LATTICES')

if __name__=='__main__':
    main()
