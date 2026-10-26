"""Exact, dependency-free checks for survivor-induced interaction-count moments.

Run: python verify.py > CERTIFICATE.json
All calculations use Python integers; no sampled or floating-point assertions.
"""
import itertools
import json
from collections import Counter, defaultdict
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n and n >= 0 else 0


def edge_list(n, edge_mask):
    return [edge for j, edge in enumerate(itertools.combinations(range(n), 2))
            if (edge_mask >> j) & 1]


def stats(n, edges):
    d = [0] * n
    adjacent = [0] * n
    for u, v in edges:
        d[u] += 1
        d[v] += 1
        adjacent[u] |= 1 << v
        adjacent[v] |= 1 << u
    m = len(edges)
    wedge = sum(choose(x, 2) for x in d)
    stars = sum(choose(x, 3) for x in d)
    assort = sum((d[u] - 1) * (d[v] - 1) for u, v in edges)
    tri = 0
    for a, b, c in itertools.combinations(range(n), 3):
        if ((adjacent[a] >> b) & 1) and ((adjacent[a] >> c) & 1) and ((adjacent[b] >> c) & 1):
            tri += 1
    paths = assort - 3 * tri
    five = wedge * (m - 2) - 3 * tri - 3 * stars - 2 * paths
    six = choose(m, 3) - tri - stars - paths - five
    assert min(paths, five, six) >= 0
    return (m, wedge, stars, assort, tri, paths, five, six), d


def check_moments(n, edges, s):
    m, w, star, assort, tri, paths, five, six = s
    signatures = [(u | v) for u, v in ((1 << a, 1 << b) for a, b in edges)]
    total = [[0, 0, 0] for _ in range(n + 1)]
    frequencies = [Counter() for _ in range(n + 1)]
    for bits in range(1 << n):
        k = bits.bit_count()
        y = sum((bits & mask) == mask for mask in signatures)
        frequencies[k][y] += 1
        for r in (1, 2, 3):
            total[k][r - 1] += y ** r
    for k in range(n + 1):
        a2 = choose(n - 2, k - 2)
        a3 = choose(n - 3, k - 3)
        a4 = choose(n - 4, k - 4)
        a5 = choose(n - 5, k - 5)
        a6 = choose(n - 6, k - 6)
        formulas = [
            m * a2,
            m * a2 + 2 * w * a3 + 2 * (choose(m, 2) - w) * a4,
            m * a2 + 6 * (w * a3 + (choose(m, 2) - w) * a4)
            + 6 * (tri * a3 + (star + paths) * a4 + five * a5 + six * a6),
        ]
        assert total[k] == formulas, (n, edges, k, total[k], formulas)
    return total, frequencies


def connected(n, edges):
    if not n:
        return False
    reached = {0}
    while True:
        nxt = reached | {v for u, v in edges if u in reached} | {u for u, v in edges if v in reached}
        if nxt == reached:
            return len(reached) == n
        reached = nxt


def main():
    counts = {}
    for n in range(1, 6):
        total_regular = defaultdict(int)
        for mask in range(1 << choose(n, 2)):
            edges = edge_list(n, mask)
            d = [sum(v in e for e in edges) for v in range(n)]
            if len(set(d)) == 1 and connected(n, edges):
                total_regular[d[0]] += 1
        counts[str(n)] = {str(k): v for k, v in sorted(total_regular.items())}
    graph_counter = 0
    cubic_triangles = Counter()
    example_records = {}
    examples = {
        'triangular_prism': [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)],
        'complete_bipartite_3_3': [(u,v) for u in range(3) for v in range(3,6)],
    }
    for name, edges in examples.items():
        s, deg = stats(6, edges)
        moments, freq = check_moments(6, edges, s)
        assert sorted(deg) == [3] * 6
        example_records[name] = {
            'invariants': {'edges':s[0], 'wedges':s[1], 'three_stars':s[2],
                           'degree_mixing':s[3], 'triangles':s[4],
                           'three_edge_paths':s[5], 'five_vertex_edge_triples':s[6],
                           'six_vertex_edge_triples':s[7]},
            'frequency_by_retained_vertex_count': {str(k):dict(sorted(f.items())) for k,f in enumerate(freq)},
            'raw_moment_numerators': {str(k): a for k,a in enumerate(moments)},
        }
    for mask in range(1 << choose(6, 2)):
        edges = edge_list(6, mask)
        s, d = stats(6, edges)
        check_moments(6, edges, s)
        graph_counter += 1
        if len(set(d)) == 1 and d[0] == 3 and connected(6, edges):
            cubic_triangles[s[4]] += 1
    assert dict(cubic_triangles) == {0: 10, 2: 60}, cubic_triangles
    prism = example_records['triangular_prism']['frequency_by_retained_vertex_count']
    bip = example_records['complete_bipartite_3_3']['frequency_by_retained_vertex_count']
    for k in range(7):
        a, b = prism[str(k)], bip[str(k)]
        delta = [a.get(y, 0) - b.get(y, 0) for y in range(10)]
        assert delta == ([-2, 6, -6, 2] + [0]*6 if k == 3 else [0]*10), (k,delta)
    print(json.dumps({
        'certificate_version': 1,
        'scope': 'exact direct retained-subset enumeration and independent motif-count formula',
        'all_six_vertex_simple_graphs_checked': graph_counter,
        'fixed_size_moment_equalities_checked': graph_counter * 7 * 3,
        'connected_regular_labeled_counts_below_six': counts,
        'connected_six_vertex_cubic_labeled_graphs_by_triangles': dict(sorted(cubic_triangles.items())),
        'example_graphs': example_records,
        'exact_fixed_size_distribution_difference': 'Only k=3: unnormalized coefficients (-2,+6,-6,+2) at edge counts 0,1,2,3; all other k agree.',
        'exact_bernoulli_distribution_difference': '2*p^3*(1-p)^3*(z-1)^3',
        'finite_checks_do_not_replace_general_proof': True,
        'result': 'PASS'
    }, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
