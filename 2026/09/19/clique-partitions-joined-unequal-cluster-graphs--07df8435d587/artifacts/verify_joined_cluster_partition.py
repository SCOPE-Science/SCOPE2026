from collections import Counter
from math import comb


def edge_coloring_complete(n):
    """Return an optimal proper edge-coloring of K_n as a list of matchings."""
    if n <= 1:
        return []
    classes = []
    if n % 2 == 1:
        # Vertices are Z_n; color c contains {c+i,c-i}.
        for c in range(n):
            cls = []
            for i in range(1, (n + 1) // 2):
                u = (c + i) % n
                v = (c - i) % n
                cls.append(tuple(sorted((u, v))))
            classes.append(cls)
    else:
        # Vertices are Z_{n-1} plus infinity = n-1.
        m = n - 1
        inf = n - 1
        for c in range(m):
            cls = [tuple(sorted((inf, c)))]
            for i in range(1, n // 2):
                u = (c + i) % m
                v = (c - i) % m
                cls.append(tuple(sorted((u, v))))
            classes.append(cls)

    all_edges = [e for cls in classes for e in cls]
    assert len(all_edges) == comb(n, 2)
    assert len(set(all_edges)) == comb(n, 2)
    expected_colors = n - 1 if n % 2 == 0 else n
    assert len(classes) == expected_colors
    for cls in classes:
        vertices = [v for e in cls for v in e]
        assert len(vertices) == len(set(vertices))
    return classes


def graph_edges(h, r, s):
    edges = set()
    A = [('A', i, u) for i in range(h) for u in range(r)]
    B = [('B', j, v) for j in range(h) for v in range(s)]
    for i in range(h):
        for u in range(r):
            for v in range(u + 1, r):
                edges.add(frozenset((('A', i, u), ('A', i, v))))
    for j in range(h):
        for u in range(s):
            for v in range(u + 1, s):
                edges.add(frozenset((('B', j, u), ('B', j, v))))
    for a in A:
        for b in B:
            edges.add(frozenset((a, b)))
    return edges


def construct_partition(h, r, s):
    assert 2 <= r <= s
    R = edge_coloring_complete(r)
    S = edge_coloring_complete(s)
    t = len(S)
    assert h >= t
    assert len(R) <= len(S)
    for c in range(len(R)):
        assert len(R[c]) <= len(S[c])

    cliques = []
    for i in range(h):
        for c, sclass in enumerate(S):
            j = (i + c) % h
            take = len(R[c]) if c < len(R) else 0
            paired = sclass[:take]
            leftover = sclass[take:]
            if c < len(R):
                for aedge, bedge in zip(R[c], paired):
                    cliques.append((
                        ('A', i, aedge[0]), ('A', i, aedge[1]),
                        ('B', j, bedge[0]), ('B', j, bedge[1]),
                    ))
            # All leftover B-edges in this matching use the same A-vertex.
            for bedge in leftover:
                cliques.append((
                    ('A', i, 0),
                    ('B', j, bedge[0]), ('B', j, bedge[1]),
                ))

    E = graph_edges(h, r, s)
    multiplicity = Counter()
    for Q in cliques:
        for x in range(len(Q)):
            for y in range(x + 1, len(Q)):
                e = frozenset((Q[x], Q[y]))
                assert e in E
                multiplicity[e] += 1

    for e in E:
        if multiplicity[e] == 0:
            cliques.append(tuple(e))
            multiplicity[e] += 1

    assert all(multiplicity[e] == 1 for e in E)
    predicted = h * h * r * s - h * (2 * comb(r, 2) + comb(s, 2))
    assert len(cliques) == predicted
    return len(E), len(cliques)


def main():
    cases = 0
    for r in range(2, 11):
        for s in range(r, 11):
            chi_s = s - 1 if s % 2 == 0 else s
            for h in (chi_s, chi_s + 1):
                construct_partition(h, r, s)
                cases += 1
    print(f"PASS: verified explicit edge partitions in {cases} parameter cases")
    print("range: 2 <= r <= s <= 10; h = chi'(K_s) and chi'(K_s)+1")
    print("each generated clique family partitions every graph edge exactly once")
    print("clique count agrees with h^2 r s - h(2*C(r,2)+C(s,2))")


if __name__ == '__main__':
    main()
