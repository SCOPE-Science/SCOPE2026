"""Finite checks for low-degree GLMY path persistence of forward circulant digraphs.
This code corroborates the unrestricted proof; it does not establish it by sampling.
Python 3 standard library only. Run: python verify.py
"""
from collections import defaultdict


def rank_mod_p(columns, prime):
    pivots = {}
    for col in columns:
        row = {j: v % prime for j, v in col.items() if v % prime}
        while row:
            i = min(row)
            if i not in pivots:
                inverse = pow(row[i], -1, prime)
                pivots[i] = {j: v * inverse % prime for j, v in row.items()}
                break
            factor = row[i]
            for j, value in pivots[i].items():
                z = (row.get(j, 0) - factor * value) % prime
                if z:
                    row[j] = z
                else:
                    row.pop(j, None)
    return len(pivots)


def boundary_2(n, triple):
    a, b, c = triple
    out = defaultdict(int)
    out[(b, c)] += 1
    if a != c:
        out[(a, c)] -= 1
    out[(a, b)] += 1
    return {e: v for e, v in out.items() if v}


def add(dst, src, sign=1):
    for edge, v in src.items():
        dst[edge] += sign * v
        if dst[edge] == 0:
            del dst[edge]


def first_homology_finite_model(n, k):
    edges = [(i, (i + j) % n) for i in range(n) for j in range(1, k + 1)]
    edge_idx = {e: idx for idx, e in enumerate(edges)}
    paths_by_endpoint = defaultdict(list)
    for u, v in edges:
        for step in range(1, k + 1):
            w = (v + step) % n
            paths_by_endpoint[(u, w)].append((u, v, w))
    columns = []
    for (u, w), triples in paths_by_endpoint.items():
        # A regular diagonal shortcut is zero, while a present shortcut is
        # an allowed edge. In either case each elementary 2-path is allowed.
        if u == w or (u, w) in edge_idx:
            generators = [{edge_idx[e]: z for e, z in boundary_2(n, p).items()} for p in triples]
        else:
            # A forbidden shortcut creates one cancellation constraint.
            # Differences against the first path span the relevant kernel.
            first = boundary_2(n, triples[0])
            generators = []
            for triple in triples[1:]:
                d = defaultdict(int)
                add(d, boundary_2(n, triple))
                add(d, first, -1)
                generators.append({edge_idx[e]: v for e, v in d.items() if v})
        columns.extend(generators)
    unit_cycle = {edge_idx[(i, (i + 1) % n)]: 1 for i in range(n)}
    # Test winding exactly over the integers at stages without reciprocal arcs.
    if 2 * k < n:
        for col in columns:
            assert sum(v * ((edges[j][1] - edges[j][0]) % n) for j, v in col.items()) == 0
    bettis = []
    for p in (2, 3, 5, 101):
        r = rank_mod_p(columns, p)
        beta = len(edges) - n + 1 - r
        bettis.append(beta)
        # The generator is nonzero exactly when adjoining its column raises rank.
        assert (rank_mod_p(columns + [unit_cycle], p) == r + 1) == (2 * k < n)
    expected = int(2 * k < n)
    assert bettis == [expected] * len(bettis), (n, k, bettis)
    return len(edges), len(columns)


def chain_filling_at_death(n):
    k = (n + 1) // 2
    a, b = k, n - k
    assert 1 <= a <= k and 1 <= b <= k
    # Q(u,j) satisfies boundary(Q(u,j)) = unit_path(u,j) - long_edge(u,u+j).
    def shortening(u, j):
        return [(u, (u + s - 1) % n, (u + s) % n) for s in range(2, j + 1)]
    base = [(0, a % n, 0)]
    base += shortening(0, a)
    base += shortening(a % n, b)
    total = defaultdict(int)
    for triple in base:
        assert ((triple[1] - triple[0]) % n) <= k
        assert ((triple[2] - triple[1]) % n) <= k
        assert triple[0] == triple[2] or ((triple[2] - triple[0]) % n) <= k
        add(total, boundary_2(n, triple))
    cycle = {(u, (u + 1) % n): 1 for u in range(n)}
    assert dict(total) == cycle, (n, total)
    return len(base)


def main():
    tested = 0
    generators = 0
    for n in range(3, 13):
        for k in range(1, n):
            edges, cols = first_homology_finite_model(n, k)
            tested += 1
            generators += cols
    fillings = [chain_filling_at_death(n) for n in range(3, 31)]
    assert all(t == n-1 for n, t in zip(range(3, 31), fillings))
    print('VERIFY_OK', 'low_degree_models=', tested, 'boundary_generators=', generators,
          'explicit_integer_fillings=', len(fillings), 'four_prime_fields=2,3,5,101')


if __name__ == '__main__':
    main()
