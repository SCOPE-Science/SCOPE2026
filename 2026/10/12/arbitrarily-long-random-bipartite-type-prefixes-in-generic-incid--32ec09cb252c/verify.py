from itertools import product
from math import comb


def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)


def a_formula(r):
    return sum(comb(r, p) * (1 << (p * (r - p))) for p in range(r + 1))


def set_partitions(n):
    if n == 0:
        yield ()
        return
    # Restricted-growth strings: canonical encoding of set partitions.
    a = [0] * n
    def rec(i, mx):
        if i == n:
            yield tuple(a)
            return
        for v in range(mx + 2):
            a[i] = v
            yield from rec(i + 1, max(mx, v))
    a[0] = 0
    if n == 1:
        yield (0,)
    else:
        yield from rec(1, 0)


def injective_signatures(r):
    sigs = set()
    for colors in product((0, 1), repeat=r):  # 0=point, 1=line
        cross = [(i, j) for i in range(r) for j in range(r)
                 if colors[i] == 0 and colors[j] == 1]
        for mask in range(1 << len(cross)):
            edges = tuple(cross[t] for t in range(len(cross)) if (mask >> t) & 1)
            sigs.add((colors, edges))
    return sigs


def all_tuple_signatures(r):
    sigs = set()
    for rg in set_partitions(r):
        k = 0 if r == 0 else max(rg) + 1
        for colors in product((0, 1), repeat=k):
            cross = [(i, j) for i in range(k) for j in range(k)
                     if colors[i] == 0 and colors[j] == 1]
            for mask in range(1 << len(cross)):
                edges = tuple(cross[t] for t in range(len(cross)) if (mask >> t) & 1)
                sigs.add((rg, colors, edges))
    return sigs


def contains_kmn(colors, edges, m, n):
    points = [i for i, c in enumerate(colors) if c == 0]
    lines = [j for j, c in enumerate(colors) if c == 1]
    E = set(edges)
    from itertools import combinations
    for P in combinations(points, m):
        for L in combinations(lines, n):
            if all((p, l) in E for p in P for l in L):
                return True
    return False


def main():
    expected_a = [1, 2, 6, 26, 162, 1442, 18306, 330626]
    expected_b = [1, 2, 8, 46, 362, 3804, 52994, 981838]
    assertions = 0

    for r in range(8):
        assert a_formula(r) == expected_a[r]
        assertions += 1
        b = sum(stirling2(r, k) * a_formula(k) for k in range(r + 1))
        assert b == expected_b[r]
        assertions += 1

    # Direct signature enumeration, independent of the closed formulas.
    for r in range(6):
        ai = len(injective_signatures(r))
        assert ai == expected_a[r]
        assertions += 1
        bi = len(all_tuple_signatures(r))
        assert bi == expected_b[r]
        assertions += 1

    # In the claimed low-arity range r < min(m,n), every realized finite
    # signature is automatically K_{m,n}-free, so no forbidden biclique can
    # alter the random-bipartite pattern count.
    for m in range(2, 7):
        for n in range(2, 7):
            for r in range(min(m, n)):
                for colors, edges in injective_signatures(r):
                    assert not contains_kmn(colors, edges, m, n)
                    assertions += 1

    print('a_0..7 =', expected_a)
    print('b_0..7 =', expected_b)
    print('exact assertions =', assertions)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
