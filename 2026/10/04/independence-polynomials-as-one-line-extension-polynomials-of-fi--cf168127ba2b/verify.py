from itertools import combinations


def subsets(vertices):
    vertices = list(vertices)
    for r in range(len(vertices)+1):
        for s in combinations(vertices, r):
            yield frozenset(s)


def independent_sets(vertices, edges):
    edges = [frozenset(e) for e in edges]
    return [S for S in subsets(vertices) if all(not e <= S for e in edges)]


def incidence_from_hypergraph(vertices, edges, n):
    lines = []
    for idx, e in enumerate(edges):
        e = frozenset(e)
        for j in range(n-1):
            lines.append((idx, j, e))
    return lines


def is_kmn_free(vertices, lines, m, n):
    for M in combinations(vertices, m):
        M = frozenset(M)
        c = sum(1 for _,_,e in lines if M <= e)
        if c >= n:
            return False
    return True


def extension_ok(vertices, lines, S, m, n):
    new_lines = list(lines) + [("new", 0, frozenset(S))]
    return is_kmn_free(vertices, new_lines, m, n)


def saturation_edges(vertices, lines, m, n):
    out = set()
    for M in combinations(vertices, m):
        M = frozenset(M)
        c = sum(1 for _,_,e in lines if M <= e)
        if c == n-1:
            out.add(M)
    return out


def all_m_hypergraphs(q, m):
    verts = tuple(range(q))
    possible = list(map(frozenset, combinations(verts, m)))
    for mask in range(1 << len(possible)):
        yield verts, {possible[i] for i in range(len(possible)) if mask >> i & 1}

# Exhaustive realization / extension-polynomial checks in small cases.
instances = 0
for m, qmax in [(2,4),(3,5)]:
    for q in range(m, qmax+1):
        for vertices, edges in all_m_hypergraphs(q, m):
            for n in (2,3,4):
                lines = incidence_from_hypergraph(vertices, edges, n)
                assert is_kmn_free(vertices, lines, m, n)
                assert saturation_edges(vertices, lines, m, n) == edges
                indep = set(independent_sets(vertices, edges))
                good = {S for S in subsets(vertices) if extension_ok(vertices, lines, S, m, n)}
                assert good == indep
                instances += 1

# Verify the graph-to-m-uniform hardness gadget exactly for all graphs through 5 vertices.
reductions = 0
for q in range(0,6):
    vertices = tuple(range(q))
    graph_edges = list(map(frozenset, combinations(vertices, 2)))
    for mask in range(1 << len(graph_edges)):
        G = {graph_edges[i] for i in range(len(graph_edges)) if mask >> i & 1}
        iG = len(independent_sets(vertices, G))
        for m in range(2,6):
            core = tuple(range(q, q + m - 2))
            H_vertices = tuple(range(q + m - 2))
            C = frozenset(core)
            H = {frozenset(e | C) for e in G}
            iH = len(independent_sets(H_vertices, H))
            expected = ((1 << (m-2)) - 1) * (1 << q) + iG
            assert iH == expected
            reductions += 1

print(f"checked_extension_instances={instances}")
print(f"checked_hardness_instances={reductions}")
print("VERIFY_OK")
