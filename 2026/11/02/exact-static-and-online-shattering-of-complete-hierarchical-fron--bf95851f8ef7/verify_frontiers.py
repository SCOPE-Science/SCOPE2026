#!/usr/bin/env python3
"""Standalone finite checks for dimensions of complete rooted-tree frontiers.
No downloaded input or external dependencies; all examples independently generated.
"""
from functools import lru_cache
from itertools import combinations, product


def frontiers(branching):
    children = []
    def make(level):
        v = len(children)
        children.append([])
        if level < len(branching):
            for _ in range(branching[level]):
                children[v].append(make(level + 1))
        return v
    make(0)
    @lru_cache(None)
    def at(v):
        if not children[v]:
            return (1 << v,)
        result = (1 << v,)
        result += tuple(sum(parts) for parts in product(*(at(w) for w in children[v])))
        return result
    ans = at(0)
    assert len(ans) == len(set(ans))
    return children, ans


def vc_exact(C, n):
    k = 0
    for d in range(n + 1):
        good = False
        for Q in combinations(range(n), d):
            masks = {sum(((c >> q) & 1) << i for i, q in enumerate(Q)) for c in C}
            if len(masks) == 1 << d:
                good = True
                break
        if not good:
            break
        k = d
    return k


def ld_exact(C, n):
    ones = [sum(1 << i for i, c in enumerate(C) if c >> q & 1) for q in range(n)]
    @lru_cache(None)
    def rec(version):
        ans = 0
        for b in ones:
            yes, no = version & b, version & ~b
            if yes and no:
                ans = max(ans, 1 + min(rec(yes), rec(no)))
        return ans
    return rec((1 << len(C)) - 1)


def last_parents(children, branching):
    depth = {0: 0}
    todo = [0]
    while todo:
        v = todo.pop()
        for w in children[v]:
            depth[w] = depth[v] + 1
            todo.append(w)
    return [v for v in depth if depth[v] == len(branching) - 1]


def test_case(b, full_vc):
    children, C = frontiers(b)
    n = len(children)
    pred = 1
    for t in b[:-1]:
        pred *= t
    assert len(C) >= 1 << pred, (b, len(C), pred)
    D = ld_exact(C, n)
    assert D == pred, (b, D, pred)
    parents = last_parents(children, b)
    assert len(parents) == pred
    traces = {sum(((c >> p) & 1) << j for j, p in enumerate(parents)) for c in C}
    assert len(traces) == (1 << pred), (b, 'lower VC failure')
    if full_vc:
        assert vc_exact(C, n) == pred, (b, 'VC mismatch')
    else:
        # Complete last-block witness check: no two of the root/leaf block can vary independently.
        for p in parents:
            Q = [p] + children[p]
            for x, y in combinations(Q, 2):
                traces2 = {((c >> x) & 1, (c >> y) & 1) for c in C}
                assert len(traces2) < 4, (b, p, x, y)
    return n, len(C), D


def main():
    checks = 0
    for h in (1, 2, 3):
        for b in product((1, 2, 3), repeat=h):
            n = sum(_prod(b[:i]) for i in range(h + 1))
            if n > 15:
                continue
            result = test_case(b, True)
            checks += 1
            print('CASE', b, 'vertices', result[0], 'frontiers', result[1], 'VC=Ldim', result[2])
    print('FULL_SMALL_EXHAUSTION_PASS cases=', checks)
    for b in ((2, 2, 2, 2), (1, 2, 2, 2), (2, 1, 2, 2)):
        n, N, d = test_case(b, False)
        print('LARGER_TREE_RECURSION_PASS', b, 'vertices', n, 'frontiers', N, 'VC_lower=Ldim', d)
    F = [1]
    for h in range(1, 11):
        F.append(1 + F[-1] * F[-1])
    assert F[:6] == [1, 2, 5, 26, 677, 458330]
    for h in range(4, 11):
        assert F[h].bit_length() - 1 > 1 << (h - 1)
    print('BINARY_FRONTIER_ENTROPY_GAP_PASS height4_frontiers=', F[4], 'h10_floor_entropy=', F[10].bit_length()-1)
    print('ALL_COMPLETE_FRONTIER_CHECKS_PASS')


def _prod(seq):
    p = 1
    for x in seq:
        p *= x
    return p


if __name__ == '__main__':
    main()
