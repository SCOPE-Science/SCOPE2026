"""Independent exact finite checks for square-orbit homology character formulas.
Requires networkx>=2.8. All arithmetic is integral; no random data.
"""
from collections import defaultdict
from itertools import permutations, combinations
import networkx as nx


def fourcycles(graph):
    # Canonicalize each undirected simple four-cycle by its *edge* set.
    found = {}
    vertices = list(graph)
    for seq in permutations(vertices, 4):
        a, b, c, d = seq
        if all(graph.has_edge(x, y) for x, y in ((a,b),(b,c),(c,d),(d,a))):
            edge_set = frozenset(frozenset((x,y)) for x,y in ((a,b),(b,c),(c,d),(d,a)))
            if edge_set not in found or seq < found[edge_set]:
                found[edge_set] = seq
    values = list(found.items())
    return [seq for edge_set, seq in values], [edge_set for edge_set, seq in values]


def square_boundaries(graph):
    q, sets = fourcycles(graph)
    assert all(not s & t for s,t in combinations(sets,2)), "Not an edge-disjoint-square graph"
    out = []
    for a,b,c,d in q:
        for u,p,w,r in ((a,b,c,d),(b,c,d,a)):
            bdry={(u,p):1,(w,p):-1,(w,r):1,(u,r):-1}
            assert len(bdry)==4
            assert all(graph.has_edge(x,y) for x,y in bdry)
            out.append(bdry)
    assert len(out)==2*len(q)
    assert len(set().union(*(set(x) for x in out)))==4*len(out), 'Square boundaries overlap'
    return out, q


def neighborhood_faces(graph):
    result={frozenset()}
    for v in graph:
        neigh=list(graph[v])
        for k in range(1,len(neigh)+1):
            result.update(map(frozenset,combinations(neigh,k)))
    return result


def permutation_sign(source, target):
    p=[target.index(x) for x in source]
    parity=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return 1 if parity%2==0 else -1


def simplicial_lefschetz(graph, aut, faces):
    result=0
    for face in faces:
        if not face: continue
        if frozenset(aut[v] for v in face)!=face: continue
        order=sorted(face)
        result+=(-1)**(len(order)-1)*permutation_sign([aut[v] for v in order],order)
    return result


def component_trace(graph,aut):
    # Connected G: bipartite double cover is connected iff G has odd cycle.
    if not nx.is_bipartite(graph):return 1
    color=nx.bipartite.color(graph)
    return 2 if all(color[v]==color[aut[v]] for v in graph) else 0


def cell_trace(square_chains, aut):
    by_support={frozenset(boundary):boundary for boundary in square_chains}
    assert len(by_support)==len(square_chains)
    trace=0
    for bdry in square_chains:
        transported={(aut[a],aut[b]):v for (a,b),v in bdry.items()}
        target=by_support.get(frozenset(transported))
        assert target is not None, 'Square cells must be permuted'
        coeffs={transported[k]*target[k] for k in target}
        assert len(coeffs)==1, 'The induced cellular action must carry the boundary with one sign'
        sign=coeffs.pop()
        assert sign in (-1,1)
        if frozenset(transported)==frozenset(bdry):trace+=sign
    return trace


def verify_graph(graph):
    if not nx.is_connected(graph):return 0
    cells, cycles=square_boundaries(graph)
    if not cells:return 0
    faces=neighborhood_faces(graph)
    n, m=graph.number_of_nodes(),graph.number_of_edges()
    comps=2 if nx.is_bipartite(graph) else 1
    rank=2*m-2*n+comps-len(cells)
    assert rank>=0
    euler=sum((-1)**(len(f)-1) for f in faces if f)
    assert euler==comps-rank, 'Euler characteristic independent check'
    actions=0
    for aut in nx.algorithms.isomorphism.GraphMatcher(graph,graph).isomorphisms_iter():
        vfix=sum(aut[v]==v for v in graph)
        efix=sum(aut[a]==a and aut[b]==b for a,b in graph.edges)
        ctrace=component_trace(graph,aut)
        sqtrace=cell_trace(cells,aut)
        predicted=ctrace+2*efix-2*vfix-sqtrace
        observed=ctrace-simplicial_lefschetz(graph,aut,faces)
        assert predicted==observed, (n,m,aut,predicted,observed)
        actions+=1
    return actions


def main():
    count=0; actions=0; nonbip=0; bip=0
    for graph in nx.graph_atlas_g():
        if len(graph)<3 or not nx.is_connected(graph):continue
        cycles, edgesets=fourcycles(graph)
        if not cycles or any(x & y for x,y in combinations(edgesets,2)):
            continue
        count+=1
        bip+=nx.is_bipartite(graph)
        nonbip+=not nx.is_bipartite(graph)
        actions+=verify_graph(graph)
    assert count==126 and actions==386, (count,actions)
    print(f'PASS: {count} connected graph-isomorphism types (all from the Graph Atlas, <=7 vertices).')
    print(f'PASS: {actions} automorphism actions; simplicial Lefschetz versus signed square-cell trace.')
    print(f'Graph types: {nonbip} non-bipartite; {bip} bipartite.')
    g=nx.disjoint_union(nx.cycle_graph(4),nx.cycle_graph(5));g.add_edge(0,4)
    assert verify_graph(g)==4
    h=nx.disjoint_union(nx.cycle_graph(4),nx.cycle_graph(4));h.add_edge(0,4)
    assert verify_graph(h)==8
    print('PASS: 12 additional graph-automorphism checks on eight- and nine-vertex constructions.')

if __name__=='__main__':main()
