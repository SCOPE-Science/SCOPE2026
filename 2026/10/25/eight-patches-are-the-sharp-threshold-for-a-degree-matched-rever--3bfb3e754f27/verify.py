"""Exact isolate-free-site polynomial census for habitat trees of order at most eight.

Python 3, standard library only. Run: python verify.py > certificate.json
Every enumeration and comparison is in exact integers.
"""
import collections
import itertools
import json


def graph_adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        adj[u].add(v)
        adj[v].add(u)
    return adj


def canonical_tree_code(n, edges):
    """AHU central-root code: equal exactly for isomorphic unrooted trees."""
    adj = graph_adjacency(n, edges)
    if n == 1:
        return '()'
    alive = set(range(n))
    while len(alive) > 2:
        leaves = [v for v in alive if len(adj[v] & alive) == 1]
        assert leaves
        alive.difference_update(leaves)

    def root_code(v, parent):
        return '(' + ''.join(sorted(root_code(w, v) for w in adj[v] if w != parent)) + ')'
    return min(root_code(v, -1) for v in alive)


def all_unlabelled_trees(max_order=8):
    """Complete generation: every nontrivial tree can lose a leaf."""
    current = {'()': ()}
    yield 1, current
    for n in range(2, max_order + 1):
        next_trees = {}
        for edges in current.values():
            for v in range(n - 1):
                new_edges = tuple(sorted((*edges, (v, n - 1))))
                code = canonical_tree_code(n, new_edges)
                next_trees.setdefault(code, new_edges)
        current = dict(sorted(next_trees.items()))
        yield n, current


def isolate_free_coefficients(n, edges):
    adj = graph_adjacency(n, edges)
    neighbors = [sum(1 << v for v in s) for s in adj]
    result = [0] * (n + 1)
    for mask in range(1 << n):
        if all((mask & (1 << v)) == 0 or (mask & neighbors[v]) != 0
               for v in range(n)):
            result[mask.bit_count()] += 1
    return tuple(result)


def add(a, b):
    result = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        result[i] += x
    for i, x in enumerate(b):
        result[i] += x
    return tuple(result)


def sub(a, b):
    result = list(a) + [0] * max(0, len(b) - len(a))
    for i, x in enumerate(b):
        result[i] -= x
    return tuple(result)


def multiply(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return tuple(r)


def isolate_free_dp(n, edges):
    """Independent rooted-tree polynomial DP, not subset enumeration.

    Child states: U=absent, S=selected with selected child,
    R=selected with no selected child (requires selected parent).
    """
    adj = graph_adjacency(n, edges)

    def rec(v, parent):
        no_parent = (1,)
        no_selected_child = (1,)
        all_selected_parent = (1,)
        for w in adj[v]:
            if w == parent:
                continue
            u, s, r = rec(w, v)
            no_parent = multiply(no_parent, add(u, s))
            no_selected_child = multiply(no_selected_child, u)
            all_selected_parent = multiply(all_selected_parent, add(add(u, s), r))
        U = no_parent
        R = (0,) + no_selected_child
        S = (0,) + sub(all_selected_parent, no_selected_child)
        return U, S, R

    u, s, r = rec(0, -1)
    result = add(u, s)
    return tuple(result) + (0,) * (n + 1 - len(result))


def degrees(n, edges):
    return tuple(sorted(len(s) for s in graph_adjacency(n, edges)))


def comparison_sign(delta):
    signs = set((x > 0) - (x < 0) for x in delta) - {0}
    if not signs:
        return 'identical'
    if len(signs) == 1:
        return 'coefficientwise_positive' if 1 in signs else 'coefficientwise_negative'
    return 'mixed'


def main():
    records = []
    all_groups = {}
    sizes = []
    for n, trees in all_unlabelled_trees(8):
        data = {}
        for code, edges in trees.items():
            enumerated = isolate_free_coefficients(n, edges)
            independently = isolate_free_dp(n, edges)
            assert enumerated == independently, (n, code, enumerated, independently)
            data[code] = {'edges': edges, 'coefficients': enumerated,
                          'degrees': degrees(n, edges)}
        groups = collections.defaultdict(list)
        for code, item in data.items():
            groups[item['degrees']].append(code)
        counts = collections.Counter()
        for deg, members in sorted(groups.items()):
            for ca, cb in itertools.combinations(sorted(members), 2):
                a, b = data[ca]['coefficients'], data[cb]['coefficients']
                delta = tuple(x - y for x, y in zip(a, b))
                sign = comparison_sign(delta)
                counts[sign] += 1
                records.append({'order': n, 'degrees': deg,
                                'tree_a': ca, 'tree_b': cb,
                                'isolate_free_coefficient_difference': delta,
                                'classification': sign})
        sizes.append({'order': n, 'tree_types': len(trees),
                      'degree_matched_pairs': sum(counts.values()),
                      'coefficientwise_ordered':
                      counts['coefficientwise_positive'] + counts['coefficientwise_negative'],
                      'equal': counts['identical'], 'mixed': counts['mixed']})
        all_groups[n] = data
    assert [(x['tree_types'], x['degree_matched_pairs'], x['mixed'])
            for x in sizes] == [(1, 0, 0), (1, 0, 0), (1, 0, 0),
                                 (2, 0, 0), (3, 0, 0), (6, 1, 0),
                                 (11, 5, 0), (23, 23, 1)]
    mixed_records = [r for r in records if r['classification'] == 'mixed']
    assert len(mixed_records) == 1
    assert mixed_records[0]['order'] == 8
    assert sorted(mixed_records[0]['isolate_free_coefficient_difference']) == sorted(
        (0, 0, 0, 0, 0, 1, 0, -1, 0))

    # Publicly displayed witness uses fixed vertex labels, independently of
    # which representative the exhaustive generator selected.
    t_edges = ((0, 1), (0, 5), (0, 7), (1, 2), (1, 4), (2, 3), (5, 6))
    h_edges = ((0, 1), (0, 4), (0, 6), (1, 2), (1, 3), (4, 5), (6, 7))
    assert degrees(8, t_edges) == degrees(8, h_edges) == (1, 1, 1, 1, 2, 2, 3, 3)
    ta = canonical_tree_code(8, t_edges)
    ha = canonical_tree_code(8, h_edges)
    assert ta != ha and {ta, ha} == {mixed_records[0]['tree_a'], mixed_records[0]['tree_b']}
    tc, hc = isolate_free_coefficients(8, t_edges), isolate_free_coefficients(8, h_edges)
    assert tc == isolate_free_dp(8, t_edges)
    assert hc == isolate_free_dp(8, h_edges)
    assert tc == (1, 0, 7, 8, 15, 14, 10, 4, 1)
    assert hc == (1, 0, 7, 8, 15, 13, 10, 5, 1)
    assert tuple(a - b for a, b in zip(tc, hc)) == (0, 0, 0, 0, 0, 1, 0, -1, 0)

    out = {
        'scientific_object': 'site-percolated tree, no selected isolated vertices',
        'method': ('complete leaf-extension generation by unrooted tree center codes; '
                   'all surviving subsets enumerated; independent rooted-tree polynomial DP; '
                   'exact coefficient sign test after t=p/(1-p)'),
        'size_census': sizes,
        'comparison_manifest': records,
        'witness': {
            'T_edges': t_edges,
            'H_edges': h_edges,
            'common_degree_multiset': degrees(8, t_edges),
            'T_coefficients': tc, 'H_coefficients': hc,
            'difference_C_T_minus_C_H': (0, 0, 0, 0, 0, 1, 0, -1, 0),
            'difference_in_t': 't^5*(1-t^2)',
            'difference_in_p': 'p^5*(1-p)*(1-2*p)',
            'interior_reversal': 'p=1/2'
        },
        'interpretation': ('C(t)=sum over S with no isolated selected vertices t^|S|; '
                           'P(no isolates)=(1-p)^n*C(p/(1-p)). '
                           'Identical degree multisets give identical expected isolate count.'),
        'exact_arithmetic': True,
        'dependencies': 'Python 3 standard library',
    }
    print(json.dumps(out, sort_keys=True, separators=(',', ':'), ensure_ascii=False))

if __name__ == '__main__':
    main()
