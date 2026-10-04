#!/usr/bin/env python3
from itertools import combinations
from math import comb, factorial
from functools import lru_cache


def triples_of(n):
    return list(combinations(range(n), 3))


def generate_psts(n):
    triples = triples_of(n)
    chosen = []

    def rec(start, used_pairs):
        yield tuple(chosen)
        for j in range(start, len(triples)):
            t = triples[j]
            ps = tuple(combinations(t, 2))
            if all(p not in used_pairs for p in ps):
                chosen.append(t)
                yield from rec(j + 1, used_pairs | set(ps))
                chosen.pop()

    yield from rec(0, set())


def leave_edges(n, blocks):
    covered = set()
    for t in blocks:
        covered.update(combinations(t, 2))
    return tuple(e for e in combinations(range(n), 2) if e not in covered)


def matching_poly(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    @lru_cache(None)
    def f(mask):
        if mask == 0:
            return (1,)
        v = (mask & -mask).bit_length() - 1
        rest = mask & ~(1 << v)
        ans = list(f(rest))
        nbrs = adj[v] & rest
        while nbrs:
            wbit = nbrs & -nbrs
            nbrs -= wbit
            b = f(rest & ~wbit)
            if len(ans) < len(b) + 1:
                ans.extend([0] * (len(b) + 1 - len(ans)))
            for k, c in enumerate(b):
                ans[k + 1] += c
        return tuple(ans)

    return f((1 << n) - 1)


def direct_extension_poly(n, blocks):
    # Independent direct enumeration of all subsets of candidate new blocks
    # {x,u,v}; this is used only for n <= 5.
    edges = leave_edges(n, blocks)
    counts = [0] * (n // 2 + 1)
    for mask in range(1 << len(edges)):
        used_old = set()
        ok = True
        k = 0
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                # Pair {x,u} or {x,v} would repeat if an old point reappears.
                if u in used_old or v in used_old:
                    ok = False
                    break
                used_old.add(u)
                used_old.add(v)
                k += 1
        if ok:
            counts[k] += 1
    while len(counts) > 1 and counts[-1] == 0:
        counts.pop()
    return tuple(counts)


def involution_number(n):
    return sum(factorial(n) // (2**k * factorial(k) * factorial(n - 2*k))
               for k in range(n // 2 + 1))


def check_ultra_log_concave(poly):
    d = len(poly) - 1
    for k in range(1, d):
        left = poly[k] * poly[k] * comb(d, k - 1) * comb(d, k + 1)
        right = poly[k - 1] * poly[k + 1] * comb(d, k) * comb(d, k)
        assert left >= right


def main():
    examined = 0
    direct_examined = 0
    census = {}
    max_totals = {}

    for n in range(1, 8):
        count = 0
        best = -1
        best_count = 0
        for blocks in generate_psts(n):
            count += 1
            examined += 1
            edges = leave_edges(n, blocks)
            poly = matching_poly(n, edges)
            check_ultra_log_concave(poly)
            total = sum(poly)
            assert total <= involution_number(n)
            if total > best:
                best = total
                best_count = 1
            elif total == best:
                best_count += 1
            if n <= 5:
                direct_examined += 1
                assert direct_extension_poly(n, blocks) == poly
        census[n] = count
        max_totals[n] = best
        assert best == involution_number(n)
        assert best_count == 1  # uniquely the empty partial triple system

    # Standard Fano STS on 7 points has empty leave and no nontrivial
    # induced one-point partial extension over the same 7 old points.
    fano = (
        (0,1,2), (0,3,4), (0,5,6),
        (1,3,5), (1,4,6), (2,3,6), (2,4,5),
    )
    assert leave_edges(7, fano) == ()
    assert matching_poly(7, ()) == (1,)

    # Empty systems: coefficient rows are matchings of K_n.
    expected = {
        1: (1,),
        2: (1,1),
        3: (1,3),
        4: (1,6,3),
        5: (1,10,15),
        6: (1,15,45,15),
        7: (1,21,105,105),
    }
    for n, row in expected.items():
        assert matching_poly(n, tuple(combinations(range(n),2))) == row

    assert census == {1:1, 2:1, 3:2, 4:5, 5:26, 6:271, 7:5596}
    assert [max_totals[n] for n in range(1,8)] == [1,2,4,10,26,76,232]
    print('PSTS_CENSUS', census)
    print('DIRECT_EXTENSION_CHECKS', direct_examined)
    print('MAX_EXTENSION_TOTALS', [max_totals[n] for n in range(1,8)])
    print('TOTAL_PSTS_CHECKED', examined)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
