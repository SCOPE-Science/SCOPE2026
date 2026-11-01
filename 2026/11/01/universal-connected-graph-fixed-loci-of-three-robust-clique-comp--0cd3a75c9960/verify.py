"""Finite verification of the vertex-orbit description for three-robust clique fixed spaces.

Uses only Python's standard library.  All comparisons use the original forbidden
independent triples, rather than the matching or quotient formula.
"""
from itertools import combinations


def symmetric_bipartite(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    matrix = [[False] * n for _ in range(n)]
    for k, (i, j) in enumerate(pairs):
        matrix[i][j] = matrix[j][i] = bool(mask & (1 << k))
    edges = {(i, n + j) for i in range(n) for j in range(n) if matrix[i][j]}
    return matrix, edges


def alpha_at_most_two(vertices, edges):
    ed = set(edges)
    for triple in combinations(vertices, 3):
        if all((min(x, y), max(x, y)) not in ed for x, y in combinations(triple, 2)):
            return False
    return True


def fixed_orbit_faces(n, edges):
    return {frozenset(S) for k in range(n + 1) for S in combinations(range(n), k)
            if alpha_at_most_two([x for i in S for x in (i, i + n)], edges)}


def model_orbit_faces(matrix):
    n = len(matrix)
    e = {(i, j) for i in range(n) for j in range(i+1, n)
         if matrix[i][j] or (matrix[i][i] and matrix[j][j])}
    return {frozenset()} | {frozenset((i,)) for i in range(n)} | {frozenset(p) for p in e}


def connected(n, edges):
    if not n:
        return False
    seen = {0}
    for _ in range(n):
        seen |= {y if x == z else x for x, y in edges for z in seen if x == z or y == z}
    return len(seen) == n


def lift_graph(n, q_edges, root=0):
    edges = {(min(i, j+n), max(i, j+n)) for i, j in q_edges}
    edges |= {(min(j, i+n), max(j, i+n)) for i, j in q_edges}
    edges.add((root, n+root))
    return edges


def rank_binary(vectors):
    pivots = {}
    for x in vectors:
        while x:
            pivot = x.bit_length() - 1
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
                break
    return len(pivots)


def reduced_homology_ranks(n, edges):
    faces = {k: [f for f in combinations(range(n), k + 1)
                 if alpha_at_most_two(f, edges)] for k in range(4)}
    boundaries = {}
    for k in range(1, 4):
        low = {f: i for i, f in enumerate(faces[k - 1])}
        columns = []
        for f in faces[k]:
            column = 0
            for removed in range(len(f)):
                column ^= 1 << low[f[:removed] + f[removed + 1:]]
            columns.append(column)
        boundaries[k] = rank_binary(columns)
    return ([len(faces[k]) - boundaries.get(k, 0) - boundaries.get(k + 1, 0)
             - (1 if k == 0 else 0) for k in range(4)],
            [len(faces[k]) for k in range(4)])


def main():
    symmetric_cases = 0
    for n in range(1, 5):
        for mask in range(1 << (n * (n + 1) // 2)):
            m, edges = symmetric_bipartite(n, mask)
            assert fixed_orbit_faces(n, edges) == model_orbit_faces(m), (n, mask)
            symmetric_cases += 1

    connected_lifts = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            E = {p for k, p in enumerate(pairs) if mask & (1 << k)}
            if not connected(n, E):
                continue
            lifted = lift_graph(n, E)
            assert connected(2*n, lifted), (n, mask)
            assert fixed_orbit_faces(n, lifted) == (
                {frozenset()} | {frozenset((i,)) for i in range(n)}
                | {frozenset(x) for x in E}), (n, mask)
            connected_lifts += 1

    n = 3
    tri = {(0, 1), (0, 2), (1, 2)}
    h, f = reduced_homology_ranks(2*n, lift_graph(n, tri))
    assert h == [0, 0, 0, 1], (h, f)
    print(f'VERIFY_OK symmetric_matrices={symmetric_cases} connected_lifts={connected_lifts} '
          f'triangle_lift_fvector={f} reduced_mod2_betti={h}')

if __name__ == '__main__':
    main()
