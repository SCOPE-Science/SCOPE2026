#!/usr/bin/env python3
"""Exact finite verifier for 3-edge-coloring Kempe moves of GP(8,3).

Requires Python 3.10+ standard library only. The graph is fixed by the
explicit generalized-Petersen presentation; no external data is needed.
"""
from collections import Counter, deque
from itertools import combinations

N = 8
VERTICES = 2 * N
EDGES = sorted({tuple(sorted(e)) for i in range(N) for e in
                ((i, (i+1)%N), (N+i, N+(i+3)%N), (i, N+i))})
assert len(EDGES) == 24
FULL = (1 << len(EDGES)) - 1
AT_VERTEX = [tuple(e for e, edge in enumerate(EDGES) if v in edge)
             for v in range(VERTICES)]
assert all(len(a) == 3 for a in AT_VERTEX)


def enumerate_matchings():
    """Choose first uncovered vertex; each perfect matching occurs once."""
    out = set()
    def visit(covered, mask):
        if covered == (1 << VERTICES)-1:
            out.add(mask)
            return
        v = next(v for v in range(VERTICES) if not (covered >> v) & 1)
        for e in AT_VERTEX[v]:
            a,b = EDGES[e]
            w = b if a == v else a
            if not (covered >> w) & 1:
                visit(covered | (1 << v) | (1 << w), mask | (1 << e))
    visit(0, 0)
    return sorted(out)


def factorizations_from_matchings(matchings):
    ms = set(matchings)
    out = set()
    for a in matchings:
        for b in matchings:
            if a & b:
                continue
            c = FULL ^ a ^ b
            if c in ms:
                out.add(tuple(sorted((a,b,c))))
    return sorted(out)


def factorizations_from_edge_coloring():
    """Independent direct search: assign one of three colors to each edge.

    Fix colors at vertex 0 to 0,1,2 in increasing edge-index order to
    quotient exactly the six global color permutations. Dynamic selection
    of the edge with fewest available colors reduces branching.
    """
    colors = [-1] * len(EDGES)
    used = [0] * VERTICES
    for c,e in enumerate(AT_VERTEX[0]):
        colors[e] = c
        a,b = EDGES[e]
        used[a] |= (1 << c)
        used[b] |= (1 << c)
    out = set()
    def visit(left):
        if left == 0:
            classes = [0,0,0]
            for e,c in enumerate(colors):
                classes[c] |= 1 << e
            out.add(tuple(sorted(classes)))
            return
        choices = None
        edge_id = None
        for e,c in enumerate(colors):
            if c != -1:
                continue
            a,b = EDGES[e]
            opts = tuple(c for c in range(3) if not ((used[a] | used[b]) >> c) & 1)
            if not opts:
                return
            if choices is None or len(opts) < len(choices):
                choices, edge_id = opts, e
                if len(choices) == 1:
                    break
        a,b = EDGES[edge_id]
        for c in choices:
            bit = 1 << c
            colors[edge_id] = c
            used[a] |= bit
            used[b] |= bit
            visit(left-1)
            used[a] ^= bit
            used[b] ^= bit
            colors[edge_id] = -1
    visit(len(EDGES)-3)
    return sorted(out)


def components_of_two_factor(mask):
    """Return exact connected-component edge masks from a 2-regular graph."""
    unused = mask
    result = []
    while unused:
        first = (unused & -unused).bit_length()-1
        start = EDGES[first][0]
        vertices = {start}
        queue = [start]
        while queue:
            v = queue.pop()
            for e in AT_VERTEX[v]:
                if (mask >> e) & 1:
                    a,b = EDGES[e]
                    w = b if a == v else a
                    if w not in vertices:
                        vertices.add(w)
                        queue.append(w)
        edge_mask = sum(1 << e for e,(a,b) in enumerate(EDGES)
                        if ((mask >> e) & 1) and a in vertices)
        assert edge_mask and edge_mask & unused
        assert not(edge_mask & (mask ^ unused))
        unused ^= edge_mask
        result.append((len(vertices), edge_mask))
    return sorted(result)


def adjacency_by_switches(factors):
    index = {f:i for i,f in enumerate(factors)}
    adj = [set() for _ in factors]
    for i,(a,b,c) in enumerate(factors):
        for x,y,z in ((a,b,c),(a,c,b),(b,c,a)):
            for _,component in components_of_two_factor(x|y):
                changed = tuple(sorted((x ^ component, y ^ component, z)))
                j = index[changed]
                if j != i:
                    adj[i].add(j)
    assert all(i in adj[j] for j,neighbors in enumerate(adj) for i in neighbors)
    return adj


def adjacency_by_pairs(factors):
    """Independent pairwise recognition of one connected alternating switch."""
    adj = [set() for _ in factors]
    for i,j in combinations(range(len(factors)),2):
        F,G = factors[i], factors[j]
        common = set(F) & set(G)
        if len(common) != 1:
            continue
        z = next(iter(common))
        x,y = (a for a in F if a != z)
        p,q = (a for a in G if a != z)
        for xx in (p,q):
            altered = x ^ xx
            if altered and (y ^ (q if xx == p else p)) == altered:
                # Each edge in the altered set lies on a 2-colored cycle.
                parts = components_of_two_factor(altered)
                if len(parts) == 1:
                    # A connected even cycle is exactly one full component;
                    # every vertex of the altered subgraph has degree 0 or 2.
                    deg = [0] * VERTICES
                    for e,(a,b) in enumerate(EDGES):
                        if altered >> e & 1:
                            deg[a] += 1
                            deg[b] += 1
                    if all(d in (0,2) for d in deg):
                        adj[i].add(j)
                        adj[j].add(i)
                        break
    return adj


def graph_components(adj):
    unseen = set(range(len(adj)))
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        comp = {start}
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if w in unseen:
                    unseen.remove(w)
                    comp.add(w)
                    queue.append(w)
        result.append(comp)
    return sorted(result, key=lambda c:(-len(c),min(c)))


def distances(adj, comp):
    ecc = []
    for s in sorted(comp):
        distance = {s:0}
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if w not in distance:
                    distance[w] = distance[v] + 1
                    queue.append(w)
        assert set(distance) == comp
        ecc.append(max(distance.values()))
    return min(ecc), max(ecc), Counter(ecc)


def certify_isomorphism(adj, component):
    # Image of each factorization index under a full explicit graph bijection.
    # Vertices 0..7 stand for u_i; vertices 8..15 stand for v_i.
    certificate = {
        2:0, 3:8, 5:7, 6:15, 7:3, 8:11, 9:2, 10:1,
        12:9, 13:12, 14:13, 15:5, 16:6, 17:14, 18:10, 19:4
    }
    assert set(certificate) == component
    assert set(certificate.values()) == set(range(VERTICES))
    target = {tuple(sorted(e)) for e in EDGES}
    actual = {tuple(sorted((certificate[i],certificate[j])))
              for i in component for j in adj[i] if i < j}
    assert actual == target
    # The equality of edge sets plus bijectivity certifies all nonedges too.
    return certificate


def main():
    matchings = enumerate_matchings()
    assert len(matchings) == 33
    factors = factorizations_from_matchings(matchings)
    direct = factorizations_from_edge_coloring()
    assert factors == direct and len(factors) == 20
    adj = adjacency_by_switches(factors)
    other = adjacency_by_pairs(factors)
    assert adj == other
    assert sum(map(len,adj)) == 54
    comps = graph_components(adj)
    assert sorted(map(len,comps)) == [4,16]
    big,small = comps
    assert sum(len(adj[i]) for i in big)//2 == 24
    assert Counter(len(adj[i]) for i in small) == Counter({1:3,3:1})
    assert Counter(len(adj[i]) for i in big) == Counter({3:16})
    assert sum(len(adj[i]) for i in small)//2 == 3
    assert distances(adj,big)[:2] == (4,4)
    assert distances(adj,small)[:2] == (1,2)
    profile = Counter()
    for f in factors:
        pair_profiles = tuple(sorted(tuple(length for length,_ in components_of_two_factor(x|y))
                                     for x,y in combinations(f,2)))
        profile[pair_profiles] += 1
    assert profile == Counter({((6,10),(6,10),(6,10)):16,
                               ((8,8),(16,),(16,)):3,
                               ((8,8),(8,8),(8,8)):1})
    certificate = certify_isomorphism(adj,big)
    print('VERIFY_OK')
    print('perfect_matchings=33 (first-uncovered-vertex recursion)')
    print('unlabeled_three_edge_colorings=20 (independent edge-color DFS agrees)')
    print('Kempe_edges=27 (switch generation and pairwise test agree)')
    print('Kempe_components=16+4')
    print('large_component=GP(8,3), vertices=16, edges=24, radius=4, diameter=4')
    print('small_component=K1,3, vertices=4, edges=3, radius=1, diameter=2')
    print('cycle_profiles=16*(6+10)^3; 3*(8+8,16,16); 1*(8+8)^3')
    print('explicit_graph_isomorphism=' + str(sorted(certificate.items())))

if __name__ == '__main__':
    main()
