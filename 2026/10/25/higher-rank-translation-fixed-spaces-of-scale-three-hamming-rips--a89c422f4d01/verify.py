"""Finite tests of higher-rank geometric fixed spaces of binary cube Rips complexes.
Requires only Python 3 standard library; no external data.
"""
from itertools import combinations
from collections import Counter, deque


def span(basis):
    s = {0}
    for a in basis:
        s |= {x ^ a for x in tuple(s)}
    return frozenset(s)


def subspaces(n, r):
    seen = set()
    for basis in combinations(range(1, 1 << n), r):
        H = span(basis)
        if len(H) == (1 << r) and H not in seen:
            seen.add(H)
            yield H


def orbit_graph(n, H):
    # Construct the whole orbit graph from actual Hamming cross-orbit distances.
    assert max(w.bit_count() for w in H) <= 3
    orbits = []
    seen = set()
    for x in range(1 << n):
        if x not in seen:
            O = frozenset(x ^ h for h in H)
            seen.update(O)
            assert max((a ^ b).bit_count() for a in O for b in O) <= 3
            orbits.append(O)
    adj = [set() for _ in orbits]
    for i,j in combinations(range(len(orbits)),2):
        if max((a ^ b).bit_count() for a in orbits[i] for b in orbits[j]) <= 3:
            adj[i].add(j)
            adj[j].add(i)
    return adj


def distances(adj, start):
    distance = {start:0}
    q = deque([start])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in distance:
                distance[w]=distance[v]+1
                q.append(w)
    return distance


def check_cube_graph(adj, dimension):
    # A verifiable isomorphism: reconstruct binary labels from distances to
    # the origin and each of its neighbors; check all graph edges exactly.
    n = len(adj)
    assert n == 1 << dimension
    assert all(len(N) == dimension for N in adj)
    origin = 0
    roots = sorted(adj[origin])
    d0 = distances(adj,origin)
    assert len(d0)==n
    dn = [distances(adj,u) for u in roots]
    labels = []
    for v in range(n):
        lab = sum(1 << i for i,dd in enumerate(dn) if dd[v] == d0[v]-1)
        assert lab.bit_count() == d0[v]
        labels.append(lab)
    assert len(set(labels))==n
    for v in range(n):
        for w in range(n):
            assert (w in adj[v]) == ((labels[v]^labels[w]).bit_count()==1)


def check_circles(adj, number):
    assert len(adj) == 4*number
    assert all(len(N)==2 for N in adj)
    seen = set()
    components = []
    for u in range(len(adj)):
        if u not in seen:
            component = set(distances(adj,u))
            seen.update(component)
            components.append(component)
            assert len(component)==4
            assert sum(len(adj[v]) for v in component)==8
    assert len(components)==number


def main():
    total = good = 0
    classes = Counter()
    for n in range(2,7):
        for r in range(2,min(n,4)+1):
            for H in subspaces(n,r):
                total+=1
                if max(x.bit_count() for x in H)>3:
                    # No vertex orbit forms a simplex, so fixed space is empty.
                    continue
                assert r<=3
                adj=orbit_graph(n,H)
                assert all(not(adj[u] & adj[v]) for u in range(len(adj)) for v in adj[u])
                if r==2:
                    weights=tuple(sorted(x.bit_count() for x in H if x))
                    assert weights in {(1,1,2),(1,2,3),(2,2,2),(2,3,3)}
                    if weights==(2,3,3):
                        check_circles(adj,1 << (n-4))
                    else:
                        check_cube_graph(adj,n-2)
                else:
                    weights=None
                    assert len(adj)==1 << (n-3) and all(not N for N in adj)
                good+=1
                classes[r,weights]+=1
    print('HYPERCUBE_SCALE3_HIGHER_RANK_FIXED_VERIFIED',total,'subgroups',good,'admissible',dict(sorted(classes.items(),key=str)))

if __name__=='__main__':
    main()
