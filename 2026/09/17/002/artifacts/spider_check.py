"""Exact checks for the nonpath-tree zero-forcing candidate. No dependencies."""
from itertools import combinations
from math import comb


def add(*polys):
    out = [0] * max(map(len, polys))
    for p in polys:
        for i, c in enumerate(p):
            out[i] += c
    return out


def mul(*polys):
    out = [1]
    for p in polys:
        new = [0] * (len(out) + len(p) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(p):
                new[i + j] += a * b
        out = new
    return out


def independence(m):
    if m < 0:
        return [1]
    return [comb(m - j + 1, j) for j in range((m + 1) // 2 + 1)]


def spider_formula(arms):
    # E: inactive, first vertex absent. D: inactive, first vertex present.
    e = [independence(max(0, a - 2)) for a in arms]
    d = [[0] if a == 1 else [0] + independence(a - 3) for a in arms]
    p = [[comb(a, j) for j in range(a + 1)] for a in arms]
    q = [add(pi, [-v for v in ei]) for pi, ei in zip(p, e)]
    h = add(mul(*q), *(mul(q[i], q[j], e[3-i-j])
                       for i, j in combinations(range(3), 2)))
    bad = add(mul(*d), *(mul(d[i], d[j], e[3-i-j])
                         for i, j in combinations(range(3), 2)))
    out = add(mul([1, 1], h), [-v for v in bad])
    return out + [0] * (sum(arms) + 2 - len(out))


def spider(arms):
    adj = [0] * (1 + sum(arms))
    start = 1
    for length in arms:
        prev = 0
        for v in range(start, start + length):
            adj[prev] |= 1 << v
            adj[v] |= 1 << prev
            prev = v
        start += length
    return adj


def closure_counts(adj):
    n = len(adj)
    out = [0] * (n + 1)
    forcing = []
    for s in range(1 << n):
        blue = s
        while True:
            old = blue
            for v in range(n):
                if blue & (1 << v):
                    white = adj[v] & ~blue
                    if white and not (white & (white - 1)):
                        blue |= white
            if blue == old:
                break
        ok = blue == (1 << n) - 1
        forcing.append(ok)
        out[s.bit_count()] += ok
    return out, forcing


def fort_check(adj, forcing):
    # Independent obstruction predicate; propagate existence over all supersets.
    n = len(adj)
    contains_fort = [False] * (1 << n)
    for f in range(1, 1 << n):
        contains_fort[f] = all(
            (adj[v] & f).bit_count() != 1
            for v in range(n) if not f & (1 << v))
    min_fort = min(f.bit_count() for f, ok in enumerate(contains_fort) if ok)
    for v in range(n):
        for mask in range(1 << n):
            if mask & (1 << v):
                contains_fort[mask] |= contains_fort[mask ^ (1 << v)]
    full = (1 << n) - 1
    assert all(ok == (not contains_fort[full ^ s]) for s, ok in enumerate(forcing))
    return min_fort


def main():
    cases = 0
    for n in range(4, 13):
        for a in range(1, (n - 1) // 3 + 1):
            for b in range(a, (n - 1 - a) // 2 + 1):
                arms = (a, b, n - 1 - a - b)
                adj = spider(arms)
                counts, forcing = closure_counts(adj)
                assert counts == spider_formula(arms), (arms, counts, spider_formula(arms))
                assert counts[2] == 9 - 2 * arms.count(1)
                if a >= 2:
                    assert counts[3] == 13 * n - 66 + 2 * arms.count(2)
                fort_check(adj, forcing)
                cases += 1
    print('Full polynomial and independent fort checks passed for', cases, 'spiders, n=4..12.')
    for n in range(2, 13):
        adj = [((1 << (v - 1)) if v else 0) |
               ((1 << (v + 1)) if v + 1 < n else 0) for v in range(n)]
        counts, _ = closure_counts(adj)
        expected = [0] + [comb(n, k) - (comb(n-k-1, k) if n-k-1 >= k else 0)
                          for k in range(1, n + 1)]
        assert counts == expected, (n, counts, expected)
    print('Boyer et al. Proposition 5 path formula verified for n=2..12, all coefficients.')
    for n in range(11, 16):
        data = []
        for arms in [(2, 2, n-5), (2, 4, n-7)]:
            counts, forcing = closure_counts(spider(arms))
            assert counts == spider_formula(arms)
            f = fort_check(spider(arms), forcing)
            data.append((counts, f))
        assert data[0][0][3] > data[1][0][3]
        assert data[0][0][n-4] < data[1][0][n-4] == comb(n, 4)
        assert data[0][1] == 4 and data[1][1] >= 5
        print(n, 'A/B z3:', data[0][0][3], data[1][0][3],
              'A/B z(n-4):', data[0][0][n-4], data[1][0][n-4],
              'min forts:', data[0][1], data[1][1])


if __name__ == '__main__':
    main()
