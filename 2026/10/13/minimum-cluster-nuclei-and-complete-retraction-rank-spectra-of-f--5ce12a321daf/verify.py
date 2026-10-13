#!/usr/bin/env python3
"""Reproducible finite checks for S5 cluster retract-rank formulas.
Only finite exhaustive checks; the all-size theorem is proved separately.
"""
from collections import Counter
from itertools import product, combinations
from math import comb, factorial


def onto(a, b):
    if b > a or b <= 0:
        return 0
    return sum((-1) ** (b-j) * comb(b, j) * j ** a for j in range(b + 1))


def predicted(sizes):
    m = len(sizes)
    Q = [[onto(sizes[i], sizes[j]) for j in range(m)] for i in range(m)]
    P = lambda k: sum(sizes[j] for j in range(m) if (k >> j) & 1)
    end = Counter()
    idem = Counter()
    support = set()
    for mask in range(1, 1 << m):
        # F(mask): maps whose cluster-image is contained in mask
        # inclusion/exclusion gives maps with exact cluster-image mask.
        target = [j for j in range(m) if (mask >> j) & 1]
        exact = 0
        for sub in range(mask + 1):
            if sub & ~mask:  # only submasks
                continue
            omitted = len(target) - sub.bit_count()
            val = 1
            for i in range(m):
                val *= sum(Q[i][j] for j in range(m) if (sub >> j) & 1)
            exact += (-1) ** omitted * val
        end[P(mask)] += exact
        count = 1
        for i in range(m):
            if not (mask >> i) & 1:
                count *= sum(Q[i][j] for j in target)
        idem[P(mask)] += count
        if count:
            support.add(mask)
    return end, idem, support


def brute(sizes, direct_algebra=False):
    n = sum(sizes)
    owner = []
    class_mask = []
    for i, k in enumerate(sizes):
        owner.extend([i] * k)
    for i in range(len(sizes)):
        class_mask.append(sum(1 << x for x in range(n) if owner[x] == i))
    pred_end = Counter()
    pred_idem = Counter()
    supports = set()
    candidates = 0
    p_morphisms = 0
    checked_closure = 0
    for tup in product(range(n), repeat=n):
        candidates += 1
        # Verify p-morphism by its full back-and-forth (class-surjectivity)
        if any(set(tup[x] for x in range(n) if owner[x] == i) !=
               {v for v in range(n) if owner[v] == owner[tup[next(x for x in range(n) if owner[x] == i)]]}
               for i in range(len(sizes))):
            continue
        p_morphisms += 1
        rank = len(set(tup))
        pred_end[rank] += 1
        if direct_algebra:
            # Independently test all subset equations for modal closure.
            for sub in range(1 << n):
                inv = sum(1 << x for x in range(n) if (sub >> tup[x]) & 1)
                closed = 0
                for j, cls in enumerate(class_mask):
                    if sub & cls:
                        closed |= cls
                lhs = sum(1 << x for x in range(n) if (closed >> tup[x]) & 1)
                rhs = 0
                for cls in class_mask:
                    if inv & cls:
                        rhs |= cls
                assert lhs == rhs, (sizes, tup, sub)
                checked_closure += 1
        if all(tup[tup[x]] == tup[x] for x in range(n)):
            pred_idem[rank] += 1
            support = 0
            for j in set(owner[v] for v in tup):
                support |= 1 << j
            supports.add(support)
    return pred_end, pred_idem, supports, candidates, p_morphisms, checked_closure


def main():
    shapes = [(1,), (2,), (1,1), (1,2), (2,2), (1,3),
              (1,1,1), (1,1,2), (1,2,2), (2,3), (1,1,1,1),
              (1,1,1,2), (1,1,2,2), (2,2,2), (1,2,3),
              (3,3)]
    total = Counter()
    for sizes in shapes:
        e, i, supp = predicted(sizes)
        eb, ib, sb, cand, pm, checked = brute(sizes, sum(sizes) <= 5)
        assert e == eb, ('endo', sizes, e, eb)
        assert i == ib, ('idem', sizes, i, ib)
        assert supp == sb, ('supports', sizes, supp, sb)
        mi = min(sizes)
        r = sizes.count(mi)
        assert len(supp) == (1 << len(sizes)) - (1 << (len(sizes)-r))
        assert sum(e.values()) == pm
        assert sum(i.values()) <= pm
        total['shapes'] += 1
        total['candidate_tables'] += cand
        total['bounded_maps'] += pm
        total['direct_algebra_subset_checks'] += checked
        total['rank_checks'] += 3
        print('CHECK', sizes, 'endomorphisms', sum(e.values()),
              'idempotents', sum(i.values()), 'dual_ranks', dict(sorted(i.items())))
    print('VERIFY_OK', dict(total))

if __name__ == '__main__':
    main()
