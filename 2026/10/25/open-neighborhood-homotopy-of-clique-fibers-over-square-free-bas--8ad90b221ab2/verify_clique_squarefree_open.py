"""Exact finite cross-checks for open-neighborhood clique-fiber homotopy.

Uses only the Python standard library. Finite tests support, but do not
prove, the infinite statement; the full proof uses simplicial collapses
and homotopy pushouts.
"""
from itertools import combinations


def all_faces(facets):
    result = {()}
    for facet in facets:
        facet = sorted(facet)
        for j in range(1, len(facet) + 1):
            result.update(combinations(facet, j))
    return result


def neighborhood_faces(m, n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < v < n
        adj[u].add(v)
        adj[v].add(u)
    return all_faces([
        {(v * m + c) for c in range(m) if c != i}
        | {(w * m + i) for w in adj[v]}
        for v in range(n) for i in range(m)
    ])


def collapse_check(m, n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    faces = neighborhood_faces(m, n, edges)
    expected_pairs = 0
    for v in range(n):
        for i in range(m):
            horiz = [v * m + c for c in range(m) if c != i]
            pivot, others = horiz[0], horiz[1:]
            wing = [w * m + i for w in sorted(adj[v])]
            if len(wing) < 2:
                continue
            lowers = []
            for j in range(2, len(wing) + 1):
                for cross in combinations(wing, j):
                    for k in range(len(others) + 1):
                        for sub in combinations(others, k):
                            lowers.append(tuple(sorted(cross + sub)))
            lowers.sort(key=lambda x: (-len(x), x))
            for lower in lowers:
                upper = tuple(sorted(lower + (pivot,)))
                assert lower in faces and upper in faces, (m, n, v, i, lower)
                assert not any(
                    len(coface) == len(lower) + 1 and set(lower).issubset(coface)
                    and coface != upper for coface in faces
                ), (m, n, v, i, lower)
                # A true free codimension-one pair.
                faces.remove(lower)
                faces.remove(upper)
            expected_pairs += len(lowers)
    target_facets = []
    for u, v in edges:
        for x, y in ((u, v), (v, u)):
            for i in range(m):
                target_facets.append({x * m + c for c in range(m) if c != i} | {y * m + i})
    target = all_faces(target_facets)
    assert faces == target, (len(faces), len(target), len(faces ^ target))
    predicted_pairs = m * 2 ** (m - 2) * sum(2 ** len(adj[v]) - len(adj[v]) - 1 for v in range(n))
    assert expected_pairs == predicted_pairs
    return expected_pairs, target


def rank_mod2(columns):
    pivots = {}
    for col in columns:
        x = col
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                pivots[p] = x
                break
            x ^= pivots[p]
    return len(pivots)


def reduced_betti_mod2(faces):
    dim = max(len(f) for f in faces) - 1
    by_degree = [[face for face in faces if len(face) == k + 1] for k in range(dim + 1)]
    boundary_ranks = [0]
    for k in range(1, dim + 1):
        target_index = {face: j for j, face in enumerate(by_degree[k - 1])}
        columns = []
        for face in by_degree[k]:
            x = 0
            for f in combinations(face, k):
                x ^= 1 << target_index[f]
            columns.append(x)
        boundary_ranks.append(rank_mod2(columns))
    boundary_ranks.append(0)
    b = [len(by_degree[k]) - boundary_ranks[k] - boundary_ranks[k + 1]
         for k in range(dim + 1)]
    b[0] -= 1
    return b


def evaluate(name, m, n, edges):
    assert n >= 2 and edges
    # The no-four-cycle assumption checked directly.
    e = set(edges)
    for a in range(n):
        for b in range(a + 1, n):
            common = [x for x in range(n) if (min(a, x), max(a, x)) in e
                      and (min(b, x), max(b, x)) in e]
            assert len(common) <= 1, (name, 'contains a four-cycle')
    pair_count, residual = collapse_check(m, n, edges)
    actual = reduced_betti_mod2(neighborhood_faces(m, n, edges))
    edge_count = len(edges)
    q = m * m - 3 * m + 1
    predicted = [0] * len(actual)
    predicted[1] = edge_count - n + 1
    predicted[2] += edge_count * q
    predicted[m - 2] += n
    assert actual == predicted, (name, m, actual, predicted)
    print(name, 'm=', m, 'n=', n, 'edges=', edge_count,
          'pairs=', pair_count, 'mod2=', actual, 'OK')


def main():
    graphs = [
        ('edge', 2, [(0, 1)]),
        ('path5', 5, [(0, 1), (1, 2), (2, 3), (3, 4)]),
        ('star3', 4, [(0, 1), (0, 2), (0, 3)]),
        ('broom5', 5, [(0, 1), (1, 2), (2, 3), (2, 4)]),
        ('triangle', 3, [(0, 1), (0, 2), (1, 2)]),
        ('cycle5', 5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]),
        ('theta', 7, [(0, 1), (1, 2), (2, 6), (0, 3), (3, 4), (4, 6), (0, 5), (5, 6)]),
    ]
    for name, n, edges in graphs:
        for m in (4, 5):
            evaluate(name, m, n, edges)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
