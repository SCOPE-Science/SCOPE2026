#!/usr/bin/env python3
"""Direct finite checks of linear-cluster modal endomorphism formulas.

Uses explicit binary accessibility and brute force function tables. No external packages.
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def stirling(n, k):
    row = [0] * (k + 1)
    row[0] = 1
    for _ in range(n):
        nxt = [0] * (k + 1)
        for j in range(1, k + 1):
            nxt[j] = j * row[j] + row[j - 1]
        row = nxt
    return row[k]


def compositions(n):
    if n == 1:
        yield (1,)
        return
    for bits in product((0, 1), repeat=n - 1):
        blocks = []
        size = 1
        for b in bits:
            if b:
                blocks.append(size)
                size = 1
            else:
                size += 1
        blocks.append(size)
        yield tuple(blocks)


def counts_formula(a):
    h = len(a)
    e = Counter()
    i = Counter()
    for t in range(h):
        target_indices = tuple(range(t, h))
        k = len(target_indices)
        # Choose the positive source-block lengths of a nondecreasing
        # onto map [h] -> [t,h). Enumerated independently of function tables.
        for chunks in compositions(h):
            if len(chunks) != k:
                continue
            ptr = 0
            val = 1
            for target, chunk in zip(target_indices, chunks):
                last = ptr + chunk - 1
                preceding_size = sum(a[ptr:last])
                onto = factorial(a[target]) * stirling(a[last], a[target])
                val *= a[target] ** preceding_size * onto
                ptr += chunk
            e[sum(a[t:])] += val
        i[sum(a[t:])] += a[t] ** sum(a[:t])
    return e, i


def brute_counts(a):
    n = sum(a)
    level = []
    for idx, sz in enumerate(a):
        level.extend((idx,) * sz)
    up = []
    for x in range(n):
        up.append(tuple(y for y in range(n) if level[x] <= level[y]))
    up_sets = [set(u) for u in up]
    e, i = Counter(), Counter()
    checked = maps = 0
    for f in product(range(n), repeat=n):
        checked += 1
        ok = True
        for x in range(n):
            if {f[y] for y in up[x]} != up_sets[f[x]]:
                ok = False
                break
        if not ok:
            continue
        maps += 1
        image = set(f)
        cardinality = len(image)
        e[cardinality] += 1
        if any(f[f[x]] != f[x] for x in range(n)):
            continue
        i[cardinality] += 1
        # Additional independent structural assertion: every idempotent
        # image equals an entire final string of complete reflexive clusters.
        assert any(image == {j for j in range(n) if level[j] >= t}
                   for t in range(len(a)))
    return e, i, checked, maps, up


def direct_modal_checks(a, up):
    n = sum(a)
    all_masks = range(1 << n)
    # d(S) = set of states with an R-successor in S.
    def diamond(mask):
        return sum(1 << x for x, dest in enumerate(up)
                   if any((mask >> y) & 1 for y in dest))
    valid = 0
    for f in product(range(n), repeat=n):
        algebra_endomorphism = True
        for mask in all_masks:
            inv = sum(1 << x for x in range(n) if (mask >> f[x]) & 1)
            d = diamond(mask)
            inv_d = sum(1 << x for x in range(n) if (d >> f[x]) & 1)
            if diamond(inv) != inv_d:
                algebra_endomorphism = False
                break
        relation_pmorphism = all({f[y] for y in up[x]} == set(up[f[x]])
                                for x in range(n))
        assert algebra_endomorphism == relation_pmorphism, (a, f)
        valid += algebra_endomorphism
    return valid


def run():
    shapes = 0
    tables = 0
    boundeds = 0
    assertions = 0
    for n in range(1, 7):
        for a in compositions(n):
            predicted_e, predicted_i = counts_formula(a)
            actual_e, actual_i, checked, valid, up = brute_counts(a)
            assert predicted_e == actual_e, ('endomorphisms', a, predicted_e, actual_e)
            assert predicted_i == actual_i, ('idempotents', a, predicted_i, actual_i)
            assert set(actual_e) == {sum(a[t:]) for t in range(len(a))}
            if n <= 3:
                assert direct_modal_checks(a, up) == valid
            shapes += 1
            tables += checked
            boundeds += valid
            assertions += 3 + (n <= 3)
    # Larger full-table spot checks with irregular and uniform cluster sizes.
    for a in [(2, 2, 3), (1, 1, 1, 1, 1, 1, 1)]:
        predicted_e, predicted_i = counts_formula(a)
        actual_e, actual_i, checked, valid, _ = brute_counts(a)
        assert predicted_e == actual_e
        assert predicted_i == actual_i
        tables += checked
        boundeds += valid
        shapes += 1
        assertions += 2
    # All-height homogeneous closed form and exact binomial rank law.
    for r in range(1, 6):
        for h in range(1, 9):
            e, i = counts_formula((r,) * h)
            for ell in range(1, h + 1):
                desired = comb(h - 1, ell - 1) * factorial(r) ** ell * r ** (r * (h - ell))
                assert e[r * ell] == desired
                assert i[r * ell] == r ** (r * (h - ell))
                assertions += 2
            assert sum(e.values()) == factorial(r) * (factorial(r) + r ** r) ** (h - 1)
            assertions += 1
    print('VERIFY_OK', f'{shapes} shapes', f'{tables} full function tables',
          f'{boundeds} bounded endomorphisms', f'{assertions} exact comparison assertions')


if __name__ == '__main__':
    run()
