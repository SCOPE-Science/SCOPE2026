#!/usr/bin/env python3
"""Independent finite checks for fixed loci of independence-bounded prism complexes.

All tests use defining induced-independence conditions rather than theorem formulas.
Only Python's standard library is required.
"""
from itertools import combinations
from math import comb


def independent_number(vertices, edges):
    vertices = tuple(vertices)
    for r in range(len(vertices), 0, -1):
        for subset in combinations(vertices, r):
            if all(frozenset((a, b)) not in edges for a, b in combinations(subset, 2)):
                return r
    return 0


def prism_edges(n, base_edges):
    e = {frozenset((2*i, 2*i+1)) for i in range(n)}
    for u,v in base_edges:
        for a in (0, 1):
            e.add(frozenset((2*u+a, 2*v+a)))
    return e


def bipartite(n, base_edges):
    neighbors = [[] for _ in range(n)]
    for u,v in base_edges:
        neighbors[u].append(v); neighbors[v].append(u)
    color = {}
    for root in range(n):
        if root not in color:
            color[root] = 0
            queue = [root]
            for v in queue:
                for w in neighbors[v]:
                    if w not in color:
                        color[w] = color[v] ^ 1
                        queue.append(w)
                    elif color[w] == color[v]:
                        return False
    return True


def orbit_check(n, base_edges, k):
    e = prism_edges(n,base_edges)
    for mask in range(1<<n):
        chosen = [i for i in range(n) if mask>>i&1]
        all_layer_vertices = [2*i+a for i in chosen for a in (0,1)]
        is_face = independent_number(all_layer_vertices,e) < k
        expected = len(chosen) < k
        if is_face != expected:
            return False,tuple(chosen)
    return True,None


def all_faces(n,edges,k):
    faces=[]
    for mask in range(1<<(2*n)):
        if not mask: continue
        chosen=[v for v in range(2*n) if mask>>v&1]
        if independent_number(chosen,edges)<k:
            faces.append(tuple(chosen))
    return faces


def rank_gf2(columns):
    pivots={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p not in pivots:
                pivots[p]=v
                break
            v ^= pivots[p]
    return len(pivots)


def reduced_bettis(faces):
    if not faces: return []
    bydim={d:[x for x in faces if len(x)==d+1] for d in range(max(len(x) for x in faces))}
    ranks=[]
    for d in range(1,len(bydim)):
        lower={face:i for i,face in enumerate(bydim[d-1])}
        cols=[]
        for face in bydim[d]:
            v=0
            for sub in combinations(face,d): v ^= 1<<lower[sub]
            cols.append(v)
        ranks.append(rank_gf2(cols))
    bettis=[]
    for d,faces_d in bydim.items():
        if d==0:
            bettis.append(len(faces_d)-1-(ranks[0] if ranks else 0))
        else:
            bettis.append(len(faces_d)-ranks[d-1]-(ranks[d] if d<len(ranks) else 0))
    return bettis


def run():
    checks=0
    families=[]
    for m in range(1,7):
        path=[(i,i+1) for i in range(m-1)]
        star=[(0,i) for i in range(1,m)]
        cycle=[(i,(i+1)%m) for i in range(m)] if m>=4 and m%2==0 else []
        disconnected=[(i,i+1) for i in range(0,m-1,2)]
        for kind,E in [('path',path),('star',star),('matching',disconnected)]+([('cycle',cycle)] if cycle else []):
            assert bipartite(m,E)
            families.append((m,kind,E))
            for k in range(2,m+2):
                ok,witness=orbit_check(m,E,k)
                assert ok,(m,kind,k,witness)
                checks+=1
    # For triangle base, the orbit triple is admissible for k=3,
    # demonstrating the essential role of bipartiteness.
    triangle=[(0,1),(1,2),(0,2)]
    assert not bipartite(3,triangle)
    assert independent_number(range(6),prism_edges(3,triangle))==2
    ok,witness=orbit_check(3,triangle,3)
    assert not ok and len(witness)==3
    homology_cases=0
    for m in range(2,7):
        E=[(i,i+1) for i in range(m-1)]
        edges=prism_edges(m,E)
        for k in (2,3):
            faces=all_faces(m,edges,k)
            betti=reduced_bettis(faces)
            expected=comb(m-1,k-1)
            wantdegree=2*k-3
            assert betti[wantdegree]==expected,(m,k,betti,expected)
            assert sum(betti)==expected,(m,k,betti)
            # Reduced Euler check with the fixed-locus simplex skeleton.
            chi_fixed=1+(-1)**(k-2)*expected
            Lefschetz=1-((-1)**(k-1))*expected
            assert chi_fixed==Lefschetz
            homology_cases+=1
    print(f'VERIFY_OK orbit_tests={checks} bipartite_graph_instances={len(families)} '
          f'finite_homology_cases={homology_cases} nonbipartite_boundary=triangle')

if __name__=='__main__':
    run()
