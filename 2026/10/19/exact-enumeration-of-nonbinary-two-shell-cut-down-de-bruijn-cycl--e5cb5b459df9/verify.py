"""Independent exact checks for Hamming-weight 1/2 q-ary universal-cycle census.

No external dependencies. Runs direct finite Euler-route enumeration and the
rooted directed Matrix-Tree determinant, independently of the proof's quotient.
"""
from itertools import product, permutations
from math import factorial, comb


def graph(q, n):
    m = n - 1
    vertices = sorted({tuple(e[:-1]) for e in product(range(q), repeat=n)
                       if 1 <= sum(x != 0 for x in e) <= 2} |
                      {tuple(e[1:]) for e in product(range(q), repeat=n)
                       if 1 <= sum(x != 0 for x in e) <= 2})
    edges = [e for e in product(range(q), repeat=n)
             if 1 <= sum(x != 0 for x in e) <= 2]
    return vertices, edges


def bareiss(a):
    a = [row[:] for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def matrix_tree(q, n):
    vertices, edges = graph(q, n)
    idx = {v: i for i, v in enumerate(vertices)}
    root = (0,) * (n - 1)
    assert root in idx
    L = [[0] * len(vertices) for _ in vertices]
    outgoing = [0] * len(vertices)
    for e in edges:
        a, b = idx[e[:-1]], idx[e[1:]]
        outgoing[a] += 1
        L[a][a] += 1
        L[a][b] -= 1
    rr = idx[root]
    reduced = [[L[i][j] for j in range(len(vertices)) if j != rr]
               for i in range(len(vertices)) if i != rr]
    trees = bareiss(reduced)
    tours = trees
    for d in outgoing:
        tours *= factorial(d - 1)
    return len(vertices), len(edges), trees, tours


def direct_euler_tours(q, n):
    """Brute-force all outgoing-edge local orderings, with a first edge fixed.

    A closed trail from root following a local ordering is an Euler circuit iff
    it uses all distinct arcs; each rooted cyclic circuit has one such ordering.
    """
    vertices, edges = graph(q, n)
    root = (0,) * (n - 1)
    edge_id = {e: i for i, e in enumerate(edges)}
    outgoing = {v: tuple(edge_id[e] for e in edges if e[:-1] == v)
                for v in vertices}
    first = edge_id[root + (1,)]
    choices = []
    for v in vertices:
        ids = outgoing[v]
        if len(ids) == 1:
            continue
        if v == root:
            ps = [(first,) + rest
                  for rest in permutations(tuple(x for x in ids if x != first))]
        else:
            ps = list(permutations(ids))
        choices.append((v, ps))
    # independent enumeration: choose local orders, follow each route greedily
    count = 0
    considered = 0
    for orders in product(*(ps for _, ps in choices)):
        considered += 1
        order = {v: list(ids) for (v, _), ids in zip(choices, orders)}
        for v in vertices:
            if v not in order:
                order[v] = list(outgoing[v])
        used = [0] * len(edges)
        pos = {v: 0 for v in vertices}
        v = root
        for _ in edges:
            if pos[v] == len(order[v]):
                break
            eid = order[v][pos[v]]
            pos[v] += 1
            if used[eid]:
                raise AssertionError("reused edge")
            used[eid] = 1
            v = edges[eid][1:]
        else:
            if v == root and all(used):
                count += 1
    return considered, count


def formula(q, n):
    m = n - 1
    tree = q ** (m * (q - 2) + m // 2)
    circuits = tree * factorial(q - 2) * factorial(q - 1) ** (m * (q - 1))
    return tree, circuits


def main():
    cases = [(2, n) for n in range(2, 11)]
    cases += [(3, n) for n in range(2, 7)]
    cases += [(4, n) for n in range(2, 5)]
    cases += [(5, n) for n in range(2, 4)]
    print("DIRECTED MATRIX-TREE CHECKS")
    for q, n in cases:
        vertices, edges, trees, tours = matrix_tree(q, n)
        expected_tree, expected_tours = formula(q, n)
        assert edges == n * (q - 1) + comb(n, 2) * (q - 1) ** 2
        assert (trees, tours) == (expected_tree, expected_tours)
        print(f"q={q} n={n} vertices={vertices} windows={edges} "
              f"arborescences={trees} cyclic_tours={tours}: OK")
    print("INDEPENDENT OUTGOING-ORDER ENUMERATIONS")
    brute_cases = [(2, n) for n in range(2, 11)] + [(3, 2), (3, 3), (3, 4), (4, 2)]
    for q, n in brute_cases:
        considered, count = direct_euler_tours(q, n)
        expected = formula(q, n)[1]
        assert count == expected, (q, n, considered, count, expected)
        print(f"q={q} n={n} local_orders={considered} "
              f"valid_cyclic_tours={count}: OK")
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
