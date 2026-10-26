#!/usr/bin/env python3
"""Exact shattering tests for vertex-geodesic systems of diameter-four trees."""
from functools import lru_cache
from itertools import combinations_with_replacement, product
import json
import os


def make_tree(branch_leaves):
    """Center 0; one adjacent node per entry; the entry counts its leaf children."""
    parent = [-1]
    for count in branch_leaves:
        center = len(parent)
        parent.append(0)
        for _ in range(count):
            parent.append(center)
    return parent


def path_vertices(parent, x, y):
    ancestry = set()
    z = x
    while z != -1:
        ancestry.add(z)
        z = parent[z]
    segment = []
    z = y
    while z not in ancestry:
        segment.append(z)
        z = parent[z]
    lca = z
    segment.append(lca)
    z = x
    while z != lca:
        segment.append(z)
        z = parent[z]
    return frozenset(segment)


def concepts(parent):
    n = len(parent)
    return {tuple(sorted(path_vertices(parent, i, j))): (i, j)
            for i in range(n) for j in range(i, n)}


def solver(parent):
    shapes = sorted(concepts(parent))
    n = len(parent)
    full = (1 << len(shapes)) - 1
    tests = [sum(1 << j for j, s in enumerate(shapes) if v in s)
             for v in range(n)]
    @lru_cache(None)
    def rank(mask):
        best = 0
        for test in tests:
            yes, no = mask & test, mask & ~test
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best
    d = rank(full)
    def witness(depth, mask):
        if depth == 0:
            j = (mask & -mask).bit_length() - 1
            return {'endpoints': list(concepts(parent)[shapes[j]])}
        for v, test in enumerate(tests):
            yes, no = mask & test, mask & ~test
            if yes and no and rank(yes) >= depth-1 and rank(no) >= depth-1:
                return {'query': v, 'zero': witness(depth-1, no),
                        'one': witness(depth-1, yes)}
        raise AssertionError('no shattered tree')
    return d, witness(d, full), len(shapes), rank.cache_info().currsize


def verify_certificate(parent, cert, d):
    seen = []
    def go(node, trace):
        if 'endpoints' in node:
            x, y = node['endpoints']
            p = path_vertices(parent, x, y)
            assert len(trace) == d
            assert all((v in p) == bool(label) for v, label in trace)
            seen.append({'labels': ''.join(str(b) for _, b in trace),
                         'endpoints': [x, y]})
        else:
            v = node['query']
            assert 0 <= v < len(parent)
            go(node['zero'], trace + [(v, 0)])
            go(node['one'], trace + [(v, 1)])
    go(cert, [])
    assert len(seen) == 2 ** d
    assert len({x['labels'] for x in seen}) == 2 ** d
    return seen


def main():
    out = {'definition':'All nonempty undirected tree-vertex geodesic paths, including singleton paths.',
           'minimum_witnesses': [], 'exhaustive_checks': [], 'spot_checks': []}
    for shape, expected in (((1, 1), 3), ((0, 1, 1), 4)):
        p = make_tree(shape)
        d, cert, count, states = solver(p)
        assert d == expected
        leaves = verify_certificate(p, cert, d)
        out['minimum_witnesses'].append({'branch_leaves':list(shape),
             'parent':p,'concept_count':count,'dimension':d,
             'certificate':cert,'leaves_checked':len(leaves)})
    for d, p in ((1, [-1,0]), (2, [-1,0,0]), (3, [-1,0,0,1])):
        observed, cert, nconcepts, _ = solver(p)
        assert observed == d
        leaves = verify_certificate(p, cert, d)
        out['minimum_witnesses'].append({'diameter':d, 'parent':p,
            'concept_count':nconcepts,'dimension':d,
            'certificate':cert,'leaves_checked':len(leaves)})
    # The lower-diameter layers include singleton, edge, stars, and double stars.
    out['lower_diameters'] = []
    for d, p in ((0, [-1]), (1, [-1,0])):
        observed, _, _, _ = solver(p)
        assert observed == d
        out['lower_diameters'].append({'diameter':d,'vertices':len(p),'dimension':observed})
    for m in range(2, 10):
        p = [-1] + [0]*m
        observed, _, _, _ = solver(p)
        assert observed == 2
        out['lower_diameters'].append({'diameter':2,'vertices':len(p),'dimension':observed})
    for left in range(1, 7):
        for right in range(1, 7):
            p = [-1,0] + [0]*left + [1]*right
            observed, _, _, _ = solver(p)
            assert observed == 3
            out['lower_diameters'].append({'diameter':3,'vertices':len(p),'dimension':observed})
    total = 0
    for n in range(5, 13):
        by_degree = {}
        for degree in range(2, n):
            for a in combinations_with_replacement(range(n), degree):
                if sum(a) + degree + 1 != n: continue
                if sum(t > 0 for t in a) < 2: continue
                p = make_tree(a)
                d, _, count, states = solver(p)
                expected = 3 if degree == 2 else 4
                assert d == expected, (n, a, d, expected)
                assert count == n*(n+1)//2
                by_degree.setdefault(degree, 0)
                by_degree[degree] += 1
                total += 1
        out['exhaustive_checks'].append({'vertices':n,
            'canonical_shapes_checked':sum(by_degree.values()),
            'center_degree_distribution':by_degree})
    # Larger samples test a uniform number of arms and unequal branching sizes.
    for a in ((1, 5), (3, 3), (0, 1, 5), (0, 0, 1, 2), (1, 1, 1, 1, 1)):
        p = make_tree(a)
        if len(p) > 22: continue
        d, _, count, states = solver(p)
        assert d == (3 if len(a) == 2 else 4)
        out['spot_checks'].append({'branch_leaves':list(a),'dimension':d,
                                  'concept_count':count, 'states':states})
    out['all_claimed_checks_passed'] = True
    print('EXHAUSTIVE_CANONICAL_SHAPES',total)
    print('CERTIFICATE_ROOTS',[(w.get('branch_leaves', w.get('diameter')),w['certificate']['query']) for w in out['minimum_witnesses']])
    print('DIAMETER_FOUR_CLASSIFICATION_OK')
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tree_geodesic_certificates.json'),'w') as f:
        json.dump(out,f,indent=2,sort_keys=True)
        f.write('\n')

if __name__ == '__main__':
    main()
