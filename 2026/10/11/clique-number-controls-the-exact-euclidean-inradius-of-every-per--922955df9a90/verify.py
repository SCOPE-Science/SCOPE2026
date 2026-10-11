#!/usr/bin/env python3
from itertools import combinations

def edge_set(edges):
    return {tuple(sorted(e)) for e in edges}

def adjacent(E,a,b):
    return tuple(sorted((a,b))) in E

def subsets(n):
    for mask in range(1<<n):
        yield tuple(i for i in range(n) if (mask>>i)&1)

def stable(E,S):
    return all(not adjacent(E,a,b) for a,b in combinations(S,2))

def clique(E,S):
    return all(adjacent(E,a,b) for a,b in combinations(S,2))

def maximal_cliques(n,E):
    cs=[set(S) for S in subsets(n) if S and clique(E,S)]
    return [tuple(sorted(C)) for C in cs if not any(C<D for D in cs)]

def check(name,n,edges):
    E=edge_set(edges)
    st=[S for S in subsets(n) if stable(E,S)]
    mc=maximal_cliques(n,E)
    omega=max(map(len,mc))
    r=1.0/(omega+omega**0.5)

    # Every stable-set vertex satisfies every claimed halfspace.
    for S in st:
        ss=set(S)
        for C in mc:
            assert len(ss.intersection(C)) <= 1

    # Uniform center attains predicted radius and only maximum clique facets are extra tangent.
    dcoord=r
    dcl=[(1-len(C)*r)/(len(C)**0.5) for C in mc]
    assert min([dcoord]+dcl) >= r-1e-12
    tang=[len(C) for C,d in zip(mc,dcl) if abs(d-r)<1e-11]
    assert tang and all(k==omega for k in tang)
    assert len(tang)==sum(1 for C in mc if len(C)==omega)

    # Incenter uniqueness criterion.
    covered=set().union(*(set(C) for C in mc if len(C)==omega))
    unique=(len(covered)==n)
    if not unique:
        u=next(v for v in range(n) if v not in covered)
        slacks=[1-r*(len(C)+len(C)**0.5) for C in mc if u in C]
        assert slacks and min(slacks)>1e-12
    return omega,unique,len(st),len(mc)

tests=[
    ("empty5",5,[]),
    ("complete5",5,list(combinations(range(5),2))),
    ("path5",5,[(0,1),(1,2),(2,3),(3,4)]),
    ("cycle4",4,[(0,1),(1,2),(2,3),(3,0)]),
    ("K23",5,[(i,j) for i in range(2) for j in range(2,5)]),
    ("triangle_plus_isolate",4,[(0,1),(1,2),(0,2)]),
    ("two_triangles_shared_vertex",5,[(0,1),(1,2),(0,2),(2,3),(3,4),(2,4)]),
]
rows=[check(*t) for t in tests]
assert any(u for _,u,_,_ in rows)
assert any(not u for _,u,_,_ in rows)
print("VERIFY_OK perfect-stable-set-inradius cases=%d stable_sets=%d maximal_cliques=%d" %
      (len(rows),sum(x[2] for x in rows),sum(x[3] for x in rows)))
