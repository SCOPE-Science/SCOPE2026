"""Exact finite checks for the open-neighborhood collapse of K_3 square C_n."""
from collections import Counter, defaultdict
from itertools import combinations


def faces_from_facets(facets):
    cells = [set(), set(), set(), set()]
    for F in facets:
        for r in range(1, 5):
            cells[r - 1].update(combinations(F, r))
    return cells


def verify(n):
    def v(a, i):
        return (a % 3) * n + (i % n)

    def nbr(a, i):
        return {v(a + 1, i), v(a - 1, i), v(a, i + 1), v(a, i - 1)}

    vertices = set(range(3 * n))
    graph = {v(a, i): nbr(a, i) for a in range(3) for i in range(n)}
    for x in vertices:
        assert len(graph[x]) == 4 and all(x in graph[y] for y in graph[x])
    facets = {tuple(sorted(graph[x])) for x in vertices}
    assert len(facets) == 3 * n
    cells = faces_from_facets(facets)
    original = tuple(map(len, cells))
    assert cells[0] == {(x,) for x in vertices}
    if n == 4:
        assert original == (12, 42, 48, 12)
        return original, None
    assert n == 3 or n >= 5
    assert original == (3 * n, 12 * n, 12 * n, 3 * n), (n, original)

    # All free-face tests use the current full face sets, not a proposed matching.
    pairs = 0
    for a in range(3):
        for i in range(n):
            A, B = v(a + 1, i), v(a - 1, i)
            C, D = v(a, i + 1), v(a, i - 1)
            tri = tuple(sorted((A, B, C)))
            tet = tuple(sorted((A, B, C, D)))
            assert tri in cells[2] and tet in cells[3]
            assert sum(set(tri).issubset(T) for T in cells[3]) == 1
            cells[2].remove(tri)
            cells[3].remove(tet)
            pairs += 1
    for a in range(3):
        for i in range(n):
            A, B = v(a + 1, i), v(a - 1, i)
            D = v(a, i - 1)
            edge = tuple(sorted((A, B)))
            tri = tuple(sorted((A, B, D)))
            assert edge in cells[1] and tri in cells[2]
            assert sum(set(edge).issubset(T) for T in cells[2]) == 1
            cells[1].remove(edge)
            cells[2].remove(tri)
            pairs += 1
    assert pairs == 6 * n and not cells[3]
    assert tuple(map(len, cells)) == (3 * n, 9 * n, 6 * n, 0)
    predicted = set()
    for a in range(3):
        for i in range(n):
            U, D = v(a, i + 1), v(a, i - 1)
            for b in (a + 1, a - 1):
                predicted.add(tuple(sorted((v(b, i), U, D))))
    assert cells[2] == predicted

    # The core is a connected orientable closed combinatorial surface.
    tri_edges = defaultdict(list)
    link_edges = defaultdict(set)
    for j, triangle in enumerate(sorted(cells[2])):
        for k in range(3):
            edge = tuple(triangle[t] for t in range(3) if t != k)
            tri_edges[edge].append((j, (-1) ** k))
        for u in triangle:
            link_edges[u].add(tuple(v for v in triangle if v != u))
    assert set(tri_edges) == cells[1]
    assert all(len(v) == 2 for v in tri_edges.values())
    for u in vertices:
        links = defaultdict(set)
        for x, y in link_edges[u]:
            links[x].add(y)
            links[y].add(x)
        assert len(links) == 6 and all(len(s) == 2 for s in links.values())
        seen = {next(iter(links))}
        agenda = list(seen)
        for x in agenda:
            for y in links[x]:
                if y not in seen:
                    seen.add(y)
                    agenda.append(y)
        assert len(seen) == 6

    # Propagate integral orientations of triangles across every edge.
    adjacency = defaultdict(list)
    for visits in tri_edges.values():
        (a, sign_a), (b, sign_b) = visits
        adjacency[a].append((b, -sign_a * sign_b))
        adjacency[b].append((a, -sign_a * sign_b))
    sign = {0: 1}
    agenda = [0]
    for a in agenda:
        for b, step in adjacency[a]:
            if b not in sign:
                sign[b] = sign[a] * step
                agenda.append(b)
            assert sign[b] == sign[a] * step
    assert len(sign) == 6 * n  # connectivity of the dual graph
    assert len(cells[0]) - len(cells[1]) + len(cells[2]) == 0
    return original, (3 * n, 9 * n, 6 * n, 0)


if __name__ == "__main__":
    print('n=4 exceptional:', verify(4)[0], 'Euler=6 (not a torus)')
    totals = Counter()
    for n in [3] + list(range(5, 41)):
        before, after = verify(n)
        totals['tested_instances'] += 1
        totals['checked_free_pairs'] += 6 * n
        totals['original_tetrahedra'] += before[3]
        totals['core_triangles'] += after[2]
    print('CHECKED', ' '.join(f'{key}={totals[key]}' for key in sorted(totals)))
    print('ALL_CHECKS_PASS')
