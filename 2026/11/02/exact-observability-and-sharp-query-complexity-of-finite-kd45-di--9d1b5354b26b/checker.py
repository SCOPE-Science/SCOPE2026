#!/usr/bin/env python3
"""Standalone finite checks of disagreement-profile and query theorems."""
from collections import defaultdict
from itertools import product


def disagreement(views, x, mask):
    for a in views:
        for b in views:
            if (a & (mask ^ x)) == 0 and (b & x) == 0:
                return True
    return False


def run():
    tested_pairs = 0
    for n in range(1, 8):
        mask = (1 << n) - 1
        fiber = defaultdict(list)
        for a in range(1, mask + 1):
            for b in range(1, mask + 1):
                signature = sum(int(disagreement((a, b), x, mask)) << x
                                for x in range(mask + 1))
                fiber[signature].append((a, b))
                tested_pairs += 1
                if (a & b) == 0:
                    minimal = {
                        x for x in range(mask + 1)
                        if disagreement((a, b), x, mask)
                        and all(not disagreement((a, b), y, mask)
                                for y in range(x)
                                if (y & x) == y)
                    }
                    assert minimal == {a, b}, (n, a, b, minimal)
                else:
                    assert signature == 0, (n, a, b)
        positives = 3**n - 2**(n + 1) + 1
        assert len(fiber) == 1 + positives // 2, (n, len(fiber))
        assert len(fiber[0]) == mask**2 - positives
        assert all(len(v) == 2 for k, v in fiber.items() if k != 0)
        assert all(disagreement((a, b), x, mask) ==
                   disagreement((a, b), mask ^ x, mask)
                   for a in range(1, mask + 1)
                   for b in range(1, mask + 1)
                   for x in range(mask + 1))
        print(f'n={n}: pointed_profiles={len(fiber)}, minimal_queries={2**(n - 1)-1}, ordered_successor_pairs={mask**2}')

    # Multi-agent symmetry, endpoint, and the all-zero/delta adversaries.
    cases = 0
    for n in range(1, 5):
        mask = (1 << n) - 1
        representatives = [x for x in range(1, mask) if x < (mask ^ x)]
        assert len(representatives) == 2**(n - 1) - 1
        for r in (2, 3, 4):
            for views in product(range(1, mask + 1), repeat=r):
                values = [disagreement(views, x, mask) for x in range(mask + 1)]
                assert not values[0] and not values[mask]
                assert all(values[x] == values[mask ^ x]
                           for x in range(mask + 1))
                cases += 1
                if n == 4 and r == 4 and cases > 50000:
                    break
            if n == 4 and r == 4 and cases > 50000:
                break
        assert not any(disagreement((mask, mask), x, mask)
                       for x in range(mask + 1))
        for x in representatives:
            vals = [disagreement((x, mask ^ x), y, mask)
                    for y in range(mask + 1)]
            assert [y for y, z in enumerate(vals) if z] == [x, mask ^ x]
        # Check the constant-row KD45 realization at the relation level.
        for a in range(1, mask + 1):
            rel = {(w, v) for w in range(n) for v in range(n)
                   if a & (1 << v)}
            assert all(any((w, v) in rel for v in range(n))
                       for w in range(n))                    # serial
            assert all((w, u) in rel
                       for w, v in rel for vv, u in rel if v == vv)  # transitive
            assert all((v, u) in rel
                       for w, v in rel for ww, u in rel if ww == w)  # Euclidean
    print('multi_agent_cases_checked=', cases)
    print('ordered_two_agent_successor_pairs_checked=', tested_pairs)
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    run()
