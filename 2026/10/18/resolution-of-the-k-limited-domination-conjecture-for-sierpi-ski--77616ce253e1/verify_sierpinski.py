"""Reproducible finite checks for k-limited domination on Sierpinski graphs.

The finite checks corroborate but do not replace the universal proof.
Python 3 standard library only.
"""
from itertools import product


def graph_by_definition(n, m):
    vertices = list(product(range(m), repeat=n))
    neighbors = [set() for _ in vertices]
    for i, u in enumerate(vertices):
        for j in range(i):
            v = vertices[j]
            h = next((h for h in range(n) if u[h] != v[h]), None)
            if h is not None and all(u[t] == v[h] and v[t] == u[h]
                                     for t in range(h + 1, n)):
                neighbors[i].add(j)
                neighbors[j].add(i)
    return vertices, neighbors


def graph_by_edge_rule(n, m):
    vertices = list(product(range(m), repeat=n))
    index = {u: i for i, u in enumerate(vertices)}
    neighbors = [set() for _ in vertices]
    for i, u in enumerate(vertices):
        for h in range(n):
            if len(set(u[h+1:])) > 1:
                continue
            for v_h in range(m):
                if v_h == u[h] or any(t != v_h for t in u[h+1:]):
                    continue
                v = u[:h] + (v_h,) + (u[h],) * (n-h-1)
                j = index[v]
                neighbors[i].add(j)
                neighbors[j].add(i)
    return vertices, neighbors


def outside_set(vertices, n, m, k):
    assert n >= 1 and m >= 2 and 1 <= k < m
    if n == 1:
        return {u for u in vertices if u[0] < k}
    r = k if k % 2 == 0 else k - 1
    use_diagonal = k % 2 == 1
    t = r // 2
    def omitted(u):
        a, b = u[-2:]
        delta = (b-a) % m
        return (use_diagonal and delta == 0) or (1 <= delta <= t) or (m-t <= delta < m)
    return {u for u in vertices if omitted(u)}


def is_k_limited(mask, adjacency_masks, k):
    for i, nbr in enumerate(adjacency_masks):
        if (mask >> i) & 1:
            if (nbr & ~mask).bit_count() > k:
                return False
        else:
            if not (nbr & mask):
                return False
    return True


def main():
    pairwise_comparisons = 0
    for n in range(1, 5):
        for m in range(2, 6):
            if m ** n > 650:
                continue
            v1, nbr1 = graph_by_definition(n, m)
            v2, nbr2 = graph_by_edge_rule(n, m)
            assert v1 == v2 and nbr1 == nbr2, (n, m)
            pairwise_comparisons += 1
    print('Independent adjacency implementations agree:', pairwise_comparisons, 'graph instances')

    constructive_instances = 0
    for n in range(1, 6):
        for m in range(2, 7):
            if m ** n > 8000:
                continue
            vertices, nbr = graph_by_edge_rule(n, m)
            index = {u: i for i, u in enumerate(vertices)}
            adj = [sum(1 << j for j in neighbors) for neighbors in nbr]
            for k in range(1, m):
                omitted = outside_set(vertices, n, m, k)
                chosen = set(vertices) - omitted
                assert len(chosen) == (m-k) * m ** (n-1), (n, m, k)
                mask = sum(1 << index[u] for u in chosen)
                assert is_k_limited(mask, adj, k), (n, m, k)
                constructive_instances += 1
    print('Explicit constructions pass direct domination/capacity checks:', constructive_instances, 'cases')

    # Check the clique-quotient structure used by the lower-bound proof.
    quotient_cases = 0
    for n in range(2, 5):
        for m in range(2, 6):
            if m ** n > 650:
                continue
            vertices, nbr = graph_by_definition(n, m)
            prefixes, qnbr = graph_by_definition(n-1, m)
            qindex = {p: i for i, p in enumerate(prefixes)}
            quotient_links = set()
            incidence = [0] * len(vertices)
            for i, u in enumerate(vertices):
                for j in nbr[i]:
                    if i < j and u[:-1] != vertices[j][:-1]:
                        p, q = qindex[u[:-1]], qindex[vertices[j][:-1]]
                        quotient_links.add(tuple(sorted((p, q))))
                        incidence[i] += 1
                        incidence[j] += 1
            expected = {tuple(sorted((i,j))) for i, ns in enumerate(qnbr) for j in ns if i != j}
            assert quotient_links == expected, (n,m)
            assert max(incidence) <= 1
            for p in prefixes:
                degree = len(qnbr[qindex[p]])
                assert degree == (m-1 if len(set(p)) == 1 else m), (n, m, p, degree)
            quotient_cases += 1
    print('Base-clique quotient and link-matching properties agree:', quotient_cases, 'cases')

    # True exhaustive minimum computations (not merely constructive tests).
    exhaustive_cases = 0
    examined = 0
    for n, m in [(1,2),(1,3),(1,4),(1,5),(1,6),(2,2),(2,3),(2,4),(3,2)]:
        vertices, nbr = graph_by_definition(n, m)
        adj = [sum(1 << j for j in neighbors) for neighbors in nbr]
        total = 1 << len(vertices)
        for k in range(1,m):
            minimum = len(vertices) + 1
            for mask in range(total):
                examined += 1
                size = mask.bit_count()
                if size >= minimum:
                    continue
                if is_k_limited(mask, adj, k):
                    minimum = size
            assert minimum == (m-k) * m ** (n-1), (n,m,k,minimum)
            exhaustive_cases += 1
    print('Exhaustive minimum checks:', exhaustive_cases, 'parameter cases,', examined, 'subset masks')
    print('PASS: all exact checks completed')

if __name__=='__main__':
    main()
