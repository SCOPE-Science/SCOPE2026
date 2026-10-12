#!/usr/bin/env python3
"""Independent finite checks for commuting nuclei on chains and products of chains.

Run with Python 3, no third-party dependencies.
"""
from itertools import product
from collections import Counter
from math import comb


def closure(n, mask):
    fixed = [i for i in range(n - 1) if (mask >> i) & 1] + [n - 1]
    return tuple(min(y for y in fixed if y >= x) for x in range(n))


def allowed(n, sm, tm):
    one = two = False
    for x in range(n):
        s = (x == n - 1) or bool((sm >> x) & 1)
        t = (x == n - 1) or bool((tm >> x) & 1)
        if s and t:
            if one and two:
                return False
            one = two = False
        elif s:
            one = True
        elif t:
            two = True
    return True


def rank_number(n, k):
    if not (1 <= k <= n):
        return 0
    return sum(comb(k + a - 1, a) * comb(n - a - 1, n - k - a) *
               2 ** (n - k - a) for a in range(n - k + 1))


def count_formula(n):
    if n == 0:
        return 1
    prev, cur = 1, 4
    if n == 1:
        return prev
    for _ in range(3, n + 1):
        prev, cur = cur, 4 * cur - 2 * prev
    return cur


def exhaustive_chain(n):
    size = 1 << (n - 1)
    ops = [closure(n, m) for m in range(size)]
    rank_counts = Counter()
    tested = 0
    for s, f in enumerate(ops):
        for t, g in enumerate(ops):
            fg = tuple(f[g[x]] for x in range(n))
            gf = tuple(g[f[x]] for x in range(n))
            actual = fg == gf
            predicted = allowed(n, s, t)
            assert actual == predicted, (n, s, t)
            if actual:
                common = tuple(x for x in range(n) if f[x] == x and g[x] == x)
                joint = tuple(min(y for y in common if y >= x) for x in range(n))
                assert fg == gf == joint, (n, s, t)
                rank_counts[len(common)] += 1
            tested += 1
    assert sum(rank_counts.values()) == count_formula(n)
    assert all(rank_counts[k] == rank_number(n, k) for k in range(1, n+1))
    return tested, sum(rank_counts.values()), dict(sorted(rank_counts.items()))


def independently_classify_all_maps(n):
    # Independent oracle over all n^n functions (only n <= 5).
    all_maps = (tuple(v) for v in product(range(n), repeat=n))
    ops = set()
    for f in all_maps:
        if (all(f[x] >= x for x in range(n)) and
            all(f[x] <= f[x+1] for x in range(n-1)) and
            all(f[f[x]] == f[x] for x in range(n)) and
            all(f[min(x,y)] == min(f[x], f[y]) for x in range(n) for y in range(n))):
            ops.add(f)
    expected = {closure(n, m) for m in range(1 << (n-1))}
    assert ops == expected
    return len(ops)


def product_check(dims):
    # Exhaustively construct all direct-product nuclei independently from
    # extensivity, isotonicity, idempotence and preservation of binary meets.
    pts = list(product(*[range(n) for n in dims]))
    top = tuple(n-1 for n in dims)
    def meet(a,b):
        return tuple(min(x,y) for x,y in zip(a,b))
    local_ops = [[closure(n, mask) for mask in range(1 << (n-1))] for n in dims]
    tuple_ops = []
    for local in product(*local_ops):
        table = tuple(tuple(op[x] for op, x in zip(local, p)) for p in pts)
        assert all(all(q[i] >= p[i] for i in range(len(dims))) for p,q in zip(pts,table))
        assert all(meet(table[pts.index(p)],table[pts.index(q)]) ==
                   table[pts.index(meet(p,q))] for p in pts for q in pts)
        tuple_ops.append(table)
    num = 0
    for f in tuple_ops:
        for g in tuple_ops:
            if all(f[pts.index(g[i])] == g[pts.index(f[i])] for i in range(len(pts))):
                num += 1
    result = 1
    for n in dims:
        result *= count_formula(n)
    assert num == result
    return len(tuple_ops),num


def independently_classify_product(dims):
    pts = list(product(*[range(n) for n in dims]))
    index = {p:i for i,p in enumerate(pts)}
    local_ops = [[closure(n, mask) for mask in range(1 << (n-1))] for n in dims]
    expected = {tuple(tuple(op[x] for op,x in zip(local,p)) for p in pts)
                for local in product(*local_ops)}
    candidates = [[j for j,q in enumerate(pts) if all(y >= x for x,y in zip(p,q))]
                  for p in pts]
    found = set()
    for outputs in product(*candidates):
        f = tuple(pts[j] for j in outputs)
        if not all(f[index[f[i]]] == f[i] for i in range(len(pts))):
            continue
        if not all(f[index[tuple(min(a,b) for a,b in zip(pts[i],pts[j]))]] ==
                   tuple(min(a,b) for a,b in zip(f[i],f[j]))
                   for i in range(len(pts)) for j in range(len(pts))):
            continue
        found.add(f)
    assert found == expected, (dims,len(found),len(expected))
    return len(found)


if __name__ == '__main__':
    checks = 0
    for n in range(1, 11):
        tested, count, ranks = exhaustive_chain(n)
        checks += tested
        print('CHAIN', n, 'tested', tested, 'commuting', count, 'joint_ranks', ranks)
    for n in range(1, 6):
        print('ALL_FUNCTIONS', n, 'nuclei', independently_classify_all_maps(n))
    for dims in [(2,2),(2,3),(3,3)]:
        print('PRODUCT', dims, 'nuclei', *product_check(dims))
    for dims in [(2,2),(2,3)]:
        print('ALL_PRODUCT_FUNCTIONS', dims, 'nuclei', independently_classify_product(dims))
    print('VERIFY_OK ordered_pairs_checked', checks, 'refined_ranks_checked',
          sum(range(1,11)), 'independent_full_map_classifications', 5,
          'product_instances', 3, 'independent_full_product_classifications', 2)
