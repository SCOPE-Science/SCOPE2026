#!/usr/bin/env python3
"""Exact combinatorial incidence verification for Fermat quintic distinguished lines.
Only Python standard library. Interpret an edge (u,v,k) as X_v=-zeta^k X_u, with zeta a primitive fifth root of unity.
"""
from itertools import combinations, product
from collections import Counter


def all_lines():
    lines=[]
    for omitted in range(5):
        r=[x for x in range(5) if x!=omitted]
        matchings=[((r[0],r[1]),(r[2],r[3])),((r[0],r[2]),(r[1],r[3])),((r[0],r[3]),(r[1],r[2]))]
        for matching in matchings:
            for k,l in product(range(5),repeat=2):
                lines.append((omitted,tuple((a,b,e) for (a,b),e in zip(matching,(k,l)))))
    assert len(set(lines))==375
    return lines


def four_coordinate_compatible(edges):
    """Four nonzero coordinates satisfy all four binomial constraints exactly in Q(zeta_5)."""
    adj={x:[] for x in set(p for a,b,k in edges for p in (a,b))}
    for a,b,k in edges:
        adj[a].append((b,1,k)); adj[b].append((a,1,(-k)%5))
    assert len(adj)==4
    # Potential (parity, exponent): X_vertex = (-1)^parity*zeta^exponent*X_root.
    root=min(adj)
    potentials={root:(0,0)}
    frontier=[root]
    for v in frontier:
        s,e=potentials[v]
        for w,ds,de in adj[v]:
            proposed=((s+ds)%2,(e+de)%5)
            if w in potentials:
                if potentials[w]!=proposed:
                    return False
            else:
                potentials[w]=proposed
                frontier.append(w)
    return len(potentials)==4


def intersection_type(A,B):
    omitted_a, edges_a=A
    omitted_b, edges_b=B
    for edge in edges_a:
        if edge in edges_b:
            return 'two'  # two-coordinate endpoint, exactly one common edge
    if omitted_a!=omitted_b:
        return 'skew'
    if {v[:2] for v in edges_a}=={v[:2] for v in edges_b}:
        return 'skew'
    return 'four' if four_coordinate_compatible(edges_a+edges_b) else 'skew'


def independent_mod11_intersection(A,B):
    """Secondary check via ranks over F_11; not substituted for the exact proof."""
    prime=11
    def basis(line):
        result=[]
        for a,b,k in line[1]:
            vec=[0]*5;vec[a]=1;vec[b]=-pow(3,k,prime)%prime
            result.append(vec)
        return result
    cols=basis(A)+basis(B)
    mat=[[cols[c][r] for c in range(4)] for r in range(5)]
    rank=0
    for c in range(4):
        pivot=next((r for r in range(rank,5) if mat[r][c]%prime),None)
        if pivot is None:continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        inv=pow(mat[rank][c],-1,prime)
        for j in range(c,4):mat[rank][j]=mat[rank][j]*inv%prime
        for r in range(rank+1,5):
            factor=mat[r][c]
            for j in range(c,4):mat[r][j]=(mat[r][j]-factor*mat[rank][j])%prime
        rank+=1
        if rank==4:break
    return rank<=3


def main():
    lines=all_lines()
    neighbors=[set() for _ in lines]
    pair_counts=Counter()
    for i,j in combinations(range(len(lines)),2):
        t=intersection_type(lines[i],lines[j]); pair_counts[t]+=1
        assert (t!='skew')==independent_mod11_intersection(lines[i],lines[j]), (i,j,t)
        if t!='skew':neighbors[i].add(j);neighbors[j].add(i)
    assert pair_counts=={'two':5250,'four':1875,'skew':63000},pair_counts
    degrees=Counter(len(a) for a in neighbors)
    assert degrees=={38:375},degrees

    # Every two-coordinate point is encoded by its support pair and ratio label.
    pencils={}
    for u,v in combinations(range(5),2):
        for label in range(5):
            hits={i for i,(_,edges) in enumerate(lines) if (u,v,label) in edges}
            assert len(hits)==15
            pencils[(u,v,label)]=hits
    assert len(pencils)==50
    assert sum(len(p) for p in pencils.values())==750
    assert all(sum(i in p for p in pencils.values())==2 for i in range(375))
    # Recover the incidence graph of the 50 Fano components directly from
    # the 375 lines: its vertices are the 50 two-coordinate pencils.
    membership={i:[] for i in range(375)}
    for vertex, pencil in pencils.items():
        for i in pencil: membership[i].append(vertex)
    family_edges={frozenset(membership[i]) for i in range(375)}
    assert len(family_edges)==375
    for vertex in pencils:
        assert sum(vertex in e for e in family_edges)==15
    all_family_edges={frozenset((u,v)) for u,v in combinations(pencils,2)
                      if not (set(u[:2])&set(v[:2]))}
    assert family_edges==all_family_edges   # Petersen graph blown up by 5

    high_edges={tuple(sorted((i,j))) for p in pencils.values() for i,j in combinations(p,2)}
    assert len(high_edges)==5250
    # No edge at a four-coordinate point is contained in a high-point pencil.
    for i,j in high_edges: assert j in neighbors[i]

    common_two=Counter(); common_four=Counter(); common_skew=Counter()
    for i,j in combinations(range(375),2):
        cm=len(neighbors[i]&neighbors[j])
        if j in neighbors[i]:
            (common_two if (i,j) in high_edges else common_four)[cm]+=1
        else: common_skew[cm]+=1
    assert common_two=={13:5250},common_two
    assert common_four=={1:1875},common_four
    assert common_skew=={2:16500,3:37500,5:7500,7:1500},common_skew
    # Each 15-clique is a high-point pencil: any clique of >=4 contains an
    # edge with at least two other common neighbors. Such edges are only high
    # edges, and their entire common-neighbor set is exactly the pencil.
    for p in pencils.values():
        for i,j in combinations(p,2):
            assert neighbors[i]&neighbors[j]==p-{i,j}
    # Exact graph connectedness.
    reached={0}; frontier=[0]
    for i in frontier:
        for j in neighbors[i]-reached:
            reached.add(j);frontier.append(j)
    assert len(reached)==375
    print('VERIFY_OK lines=375 high_points=50 high_multiplicity=15 double_points=1875 adjacency=5250+1875 total=7125 valency=38 two_edge_common=13 four_edge_common=1 nonadjacent_common=2:16500,3:37500,5:7500,7:1500 connected=yes maximum_clique=15 maximal_15_cliques=50 Fano_family_graph=KG5,2_blowup5 independent_mod11_rank=all_pairs')

if __name__=='__main__': main()
