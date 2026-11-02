#!/usr/bin/env python3
"""Self-contained finite checks of the closed-Hamming-neighborhood theorem.

Run: python3 VERIFY.py
No external packages or external data are required.
"""
from functools import lru_cache
from itertools import combinations, product


def neighborhoods(d, q):
    words = tuple(product(range(q), repeat=d))
    balls = tuple(sum(1 << j for j, x in enumerate(words)
                      if sum(a != b for a, b in zip(x, y)) <= 1)
                  for y in words)
    return words, balls


def vc_dimension(balls):
    n = len(balls)
    best = 0
    for k in range(1, min(n, 4) + 1):
        shattered = False
        for support in combinations(range(n), k):
            traces = set()
            for center in range(n):
                trace = sum(1 << i for i, query in enumerate(support)
                            if (balls[query] >> center) & 1)
                traces.add(trace)
                if len(traces) == (1 << k):
                    shattered = True
                    break
            if shattered:
                break
        if shattered:
            best = k
        else:
            break
    return best


def littlestone_dimension(balls):
    n = len(balls)
    all_centers = (1 << n) - 1
    @lru_cache(None)
    def value(version_space):
        if version_space.bit_count() <= 1:
            return 0
        best = 0
        for ball in balls:
            yes = version_space & ball
            no = version_space & (all_centers ^ ball)
            if yes and no:
                candidate = 1 + min(value(yes), value(no))
                if candidate > best:
                    best = candidate
        return best
    return value(all_centers)


def expected(d, q):
    if d == 1:
        return (0, 0)
    if (d, q) == (2, 2):
        return (1, 1)
    if (d, q) == (2, 3):
        return (2, 3)
    return (3, 3)


def witness_checks():
    # An explicit full trace table, independently obtained from Hamming distance.
    supports = {
        (2, 2): ((0, 0),),
        (2, 3): ((0, 0), (0, 1)),
        (2, 4): ((0, 0), (0, 1), (1, 2)),
        (3, 2): ((0, 0, 0), (0, 0, 1), (0, 1, 0)),
    }
    for (d, q), queries in supports.items():
        words, _ = neighborhoods(d, q)
        traces = {tuple(int(sum(a != b for a, b in zip(c, y)) <= 1)
                        for y in queries) for c in words}
        assert len(traces) == (1 << len(queries)), (d, q, queries)

    # Tree encoding: [query, child_for_zero, child_for_one]; leaves are [center].
    tree = [
        [0, 0],
        [[0, 1],
            [[1, 0], [[2, 2]], [[1, 2]]],
            [[1, 0], [[2, 1]], [[1, 1]]]],
        [[0, 1],
            [[1, 1], [[2, 0]], [[1, 0]]],
            [[1, 0], [[0, 1]], [[0, 0]]]],
    ]
    leaves = []
    def visit(node, path):
        if len(node) == 1:
            center = tuple(node[0])
            assert len(path) == 3
            for query, bit in path:
                assert int(sum(a != b for a, b in zip(center, query)) <= 1) == bit
            leaves.append(center)
            return
        assert len(node) == 3
        query = tuple(node[0])
        for bit in (0, 1):
            visit(node[1 + bit], path + [(query, bit)])
    visit(tree, [])
    assert len(leaves) == 8 and len(set(leaves)) == 8
    print('SHATTERING_WITNESSES_PASS; TERNARY_ROOK_DEPTH3_CERTIFICATE_PASS leaves=8')


def main():
    witness_checks()
    cases = [(1, 2), (1, 5), (2, 2), (2, 3), (2, 4),
             (2, 5), (3, 2), (3, 3), (4, 2)]
    for d, q in cases:
        _, balls = neighborhoods(d, q)
        observed = vc_dimension(balls), littlestone_dimension(balls)
        assert observed == expected(d, q), ((d, q), observed)
        print('EXACT_FINITE_CASE_PASS', (d, q), 'VC/Ldim=', observed)
    print('ALL_CLOSED_HAMMING_RADIUS_ONE_CHECKS_PASS cases=', len(cases))


if __name__ == '__main__':
    main()
