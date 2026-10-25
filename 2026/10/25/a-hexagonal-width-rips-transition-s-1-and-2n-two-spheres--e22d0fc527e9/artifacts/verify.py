#!/usr/bin/env python3
"""Exact finite replay of a translation-orbit discrete-Morse certificate.

No external packages are required. The companion certificate.json contains
coordinate templates independent of the longitudinal period. The all-period
claim additionally uses the locality lemma proved in RESULT.md.
"""
import collections
import itertools
import json
from pathlib import Path
import sys

CERT = json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))

def mod_vertex(v,n):
    return (int(v[0]), int(v[1])%n)

def shift_face(template,n,t):
    return tuple(sorted((int(x),(int(y)+t)%n) for x,y in template))

def orbit_key(face,n):
    return min(shift_face(face,n,t) for t in range(n))

def graph_dist(a,b,n):
    dx=(a[0]-b[0])%6
    dx=min(dx,6-dx)
    dy=(a[1]-b[1])%n
    dy=min(dy,n-dy)
    return dx+dy

def all_simplices(n):
    V=[(x,y) for x in range(6) for y in range(n)]
    adjacency={v:set() for v in V}
    for i,u in enumerate(V):
        for v in V[i+1:]:
            if graph_dist(u,v,n)<=2:
                adjacency[u].add(v)
                adjacency[v].add(u)
    faces=set()
    for i,u in enumerate(V):
        def descend(s,candidates):
            faces.add(tuple(s))
            while candidates:
                v=candidates.pop(0)
                descend(s+(v,),[w for w in candidates if w in adjacency[v]])
        descend((u,), sorted(v for v in adjacency[u] if v>u))
    return faces

def translated_faces(template,n):
    return [shift_face(template,n,t) for t in range(n)]

def run(n, verbose=False):
    assert n>=7
    live=all_simplices(n)
    initial=collections.Counter(len(z) for z in live)
    assert initial == {1:6*n,2:36*n,3:62*n,4:36*n,5:6*n}, (n,initial)
    cofaces=collections.defaultdict(set)
    for tau in live:
        for sigma in itertools.combinations(tau,len(tau)-1):
            if sigma:
                cofaces[sigma].add(tau)
    for ci,pair in enumerate(CERT["collapse_pairs"]):
        A=translated_faces(pair["free_face"],n)
        B=translated_faces(pair["unique_cofacet"],n)
        assert len(set(A))==n and len(set(B))==n, ("orbit not free",n,ci)
        for sigma,tau in zip(A,B):
            assert sigma in live and tau in live and len(tau)==len(sigma)+1
            assert set(sigma).issubset(tau)
            assert cofaces[sigma]&live == {tau}, ("not free",n,ci,sigma)
            assert not (cofaces[tau]&live), ("cofacet not maximal",n,ci)
            live.remove(sigma)
            live.remove(tau)
    reduced=collections.Counter(len(z) for z in live)
    assert reduced=={1:6*n,2:19*n,3:15*n},(n,reduced)

    triangle_order=[orbit_key(shift_face(a,n,0),n) for a in CERT["triangle_order"]]
    assert len(set(triangle_order))==15
    priority={k:i for i,k in enumerate(triangle_order)}
    tri_orbits={orbit_key(z,n) for z in live if len(z)==3}
    edge_orbits={orbit_key(z,n) for z in live if len(z)==2}
    assert tri_orbits==set(triangle_order)
    assert len(edge_orbits)==19

    matched_edges=set()
    matched_triangles=set()
    for mi,pair in enumerate(CERT["morse_pairs"]):
        E=translated_faces(pair["edge"],n)
        T=translated_faces(pair["triangle"],n)
        assert len(set(E))==n and len(set(T))==n
        for e,t in zip(E,T):
            assert e in live and t in live and set(e).issubset(t)
            assert e not in matched_edges and t not in matched_triangles
            matched_edges.add(e);matched_triangles.add(t)
            # The matched triangle is strictly the highest-priority
            # triangle incident to this edge, apart from itself.
            for third in [(x,y) for x in range(6) for y in range(n)]:
                if third in e: continue
                tri=tuple(sorted((*e,third)))
                if tri in live and tri!=t:
                    assert priority[orbit_key(tri,n)] < priority[orbit_key(t,n)],(
                        "Morse priority cycle",n,mi,e,tri,t)
    assert len(matched_edges)==13*n and len(matched_triangles)==13*n
    critical_triangles={t for t in live if len(t)==3}-matched_triangles
    remaining_edges={e for e in live if len(e)==2}-matched_edges
    assert len(critical_triangles)==2*n and len(remaining_edges)==6*n
    required=set()
    for template in CERT["residual_edge_orbits"]:
        required.update(translated_faces(template,n))
    assert remaining_edges==required

    # The remaining one-skeleton consists of a tree in every column,
    # joined by a single longitudinal n-cycle on the x=5 vertices.
    expected_tree={(0,4),(1,3),(2,4),(3,5),(4,5)}
    cycle_edges=set()
    tree_edges=set()
    for edge in remaining_edges:
        a,b=edge
        if a[1]==b[1]:
            tree_edges.add(edge)
            assert tuple(sorted((a[0],b[0]))) in expected_tree
        else:
            cycle_edges.add(edge)
            assert a[0]==b[0]==5
            assert (a[1]-b[1])%n in (1,n-1)
    assert len(tree_edges)==5*n and len(cycle_edges)==n
    assert all(
        sum(1 for e in tree_edges if all(v[1]==col for v in e))==5
        for col in range(n))
    assert len(CERT["collapse_pairs"])==53
    if verbose:
        print(f"n={n} initial={[initial[d] for d in range(1,6)]} "
              f"orbit_collapses={53*n} remaining={[reduced[d] for d in range(1,4)]} "
              f"morse_pairs={13*n} critical=(1,1,{2*n}) OK")
    return {"n":n,"initial_faces":sum(initial.values()),
            "elementary_collapse_pairs":53*n,
            "edge_triangle_morse_pairs":13*n,
            "critical_2_cells":2*n}
if __name__=="__main__":
    ns=[int(z) for z in sys.argv[1:]] if len(sys.argv)>1 else list(range(7,21))
    for n in ns: run(n,True)
    print("VERIFY_OK_C6_CN_RIPS2_WEDGE")
