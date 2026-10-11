"""Independent topology check of the two fourteen-point circulant witnesses.

Uses direct subset enumeration, free-face elementary collapses, closed-manifold
link tests, and obstruction to orienting adjacent triangular faces. Standard
library only. Both representatives are checked, and the complete stated
collapse certificate is verified at each individual step.
"""
import itertools
import json
import math
import sys
from collections import Counter, defaultdict, deque

N = 14
REPRESENTATIVES = ((1,3,4),(1,2,5,7))


def complexes(steps):
    graph_edges = {(i,j) for i in range(N) for j in range(i+1,N)
                   if min(j-i,N-(j-i)) in steps}
    f = defaultdict(set)
    f[0].add(())
    for size in range(1,N+1):
        for simplex in itertools.combinations(range(N),size):
            if all((a,b) not in graph_edges for a,b in itertools.combinations(simplex,2)):
                f[size].add(simplex)
    return f


def collapse_one(fs, small, big):
    small=tuple(small);big=tuple(big)
    assert len(big)==len(small)+1
    assert small in fs[len(small)] and big in fs[len(big)]
    assert set(small).issubset(big)
    assert sum(set(small).issubset(cell) for cell in fs[len(big)])==1
    # The asserted free-face incidence guarantees no higher coface of small.
    assert not any(set(small).issubset(cell)
                   for k in range(len(big)+1,N+1) for cell in fs[k])
    fs[len(small)].remove(small)
    fs[len(big)].remove(big)


def manifold_data(fs):
    assert all(not fs[k] for k in range(4,N+1))
    vertices, edges, triangles = fs[1], fs[2], fs[3]
    edge_incidence=Counter(tuple(sorted(pair)) for t in triangles
                           for pair in itertools.combinations(t,2))
    assert set(edge_incidence)==edges and set(edge_incidence.values())=={2}
    for v in range(N):
        link_vertices={w for e in edges if v in e for w in e if w!=v}
        link_edges=[tuple(w for w in t if w!=v) for t in triangles if v in t]
        adj=defaultdict(set)
        for a,b in link_edges:
            adj[a].add(b);adj[b].add(a)
        assert set(adj)==link_vertices
        assert all(len(neighbors)==2 for neighbors in adj.values())
        stack=[next(iter(link_vertices))]; seen=set()
        while stack:
            x=stack.pop()
            if x not in seen:
                seen.add(x);stack.extend(adj[x]-seen)
        assert seen==link_vertices
    # Connectivity of the triangulated surface.
    connected=set(); stack=[0]; adj=defaultdict(set)
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    while stack:
        v=stack.pop()
        if v not in connected:
            connected.add(v);stack.extend(adj[v]-connected)
    assert len(connected)==N
    chi=len(vertices)-len(edges)+len(triangles)
    assert chi==0
    # Propagate orientations around triangle dual graph. A conflict proves
    # there is no coherent orientation on the closed connected surface.
    edge_to_tris=defaultdict(list)
    for tri in triangles:
        a,b,c=tri
        for e,sgn in (((b,c),+1),((a,c),-1),((a,b),+1)):
            edge_to_tris[e].append((tri,sgn))
    nbr=defaultdict(list)
    for e,pair in edge_to_tris.items():
        assert len(pair)==2
        (ta,sa),(tb,sb)=pair
        required=-sa*sb
        nbr[ta].append((tb,required))
        nbr[tb].append((ta,required))
    root=min(triangles)
    orientations={root:1}; queue=deque([root]); contradiction=None
    while queue:
        t=queue.popleft()
        for u,transition in nbr[t]:
            prediction=orientations[t]*transition
            if u in orientations:
                if orientations[u]!=prediction:
                    contradiction=(t,u,orientations[u],prediction)
            else:
                orientations[u]=prediction;queue.append(u)
    assert len(orientations)==len(triangles)
    assert contradiction is not None, 'The surface is orientable, not a Klein bottle'
    # Connected closed nonorientable surface with Euler characteristic zero
    # is a Klein bottle by the classification theorem for closed surfaces.
    return {"f_vector":[len(vertices),len(edges),len(triangles)],
            "euler_characteristic":chi,
            "orientable":False,
            "all_vertex_links_single_cycles":True,
            "homotopy_type":"Klein bottle"}


def verify(cert):
    assert cert['representatives']==[list(r) for r in REPRESENTATIVES]
    assert len(cert['collapse_pairs'])==14
    actual={}
    for representative in REPRESENTATIVES:
        fs=complexes(representative)
        original=[len(fs[k]) for k in range(1, max(fs)+1) if fs[k]]
        if representative==REPRESENTATIVES[0]:
            assert original==[14,49,42,7]
            for lower,upper in cert['collapse_pairs']:
                collapse_one(fs,lower,upper)
        else:
            assert original==[14,42,28]
            # Datta--Upadhyay Q_{7,2} has triangles
            # {i,i+1,i+2} and {i,i+2,i+8} modulo 14.
            # The map i -> 3i carries it onto this independence complex.
            published = set()
            for i in range(N):
                for tri in ((i,i+1,i+2),(i,i+2,i+8)):
                    published.add(tuple(sorted(3*j % N for j in tri)))
            assert published == fs[3]
        result=manifold_data(fs)
        actual[str(representative)]={"original_f_vector":original,**result}
    assert cert['manifold_results']==actual
    # Each of the six torsion-positive step sets lies in exactly one unit orbit.
    units=[a for a in range(1,N) if math.gcd(a,N)==1]
    def orbit(steps):
        return sorted({tuple(sorted({min(a*d%N,N-(a*d%N)) for d in steps}))
                       for a in units})
    expected=[[(1,3,4),(1,5,6),(2,3,5)],
              [(1,2,5,7),(1,3,6,7),(3,4,5,7)]]
    assert [orbit(steps) for steps in REPRESENTATIVES]==expected
    assert cert['unit_orbits']==[[list(x) for x in o] for o in expected]
    return actual


def main():
    if len(sys.argv)!=2:
        raise ValueError('Usage: python verify_surface.py certificate.json')
    with open(sys.argv[1],encoding='utf-8') as inp:
        cert=json.load(inp)
    data=verify(cert)
    print('SURFACE_PASS: two explicit closed nonorientable chi-zero surfaces; one after 14 free-face collapses.')
    print('Topological representatives:',data)


if __name__=='__main__':
    main()
