"""Standard-library checks for zero-forcing enumeration on rook graphs.

Run: python3 verify.py
Each direct coloring test is independent of the bipartite-forest recursion.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb, factorial

@lru_cache(None)
def stirling(n, k):
    if n == k == 0:
        return 1
    if n < 0 or k <= 0 or k > n:
        return 0
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)


def is_zero_forcing(m, n, whites):
    """Direct repeated color-change simulation; independent from the forest test."""
    white = set(whites)
    vertices = range(m * n)
    while white:
        chosen = None
        for u in vertices:
            if u in white:
                continue
            adjacent_white = [v for v in white
                              if u // n == v // n or u % n == v % n]
            if len(adjacent_white) == 1:
                chosen = adjacent_white[0]
                break
        if chosen is None:
            return False
        white.remove(chosen)
    return True


def is_forest_and_leaf_accessible(m, n, whites):
    """Different, graph-structural predicate using union/find on white edges."""
    if not whites:
        return True
    degree_row = [0] * m
    degree_col = [0] * n
    parent = list(range(m + n))

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for u in whites:
        a, b = divmod(u, n)
        degree_row[a] += 1
        degree_col[b] += 1
        ra, rb = root(a), root(m + b)
        if ra == rb:
            return False
        parent[ra] = rb
    return ((0 in degree_row and 1 in degree_col) or
            (0 in degree_col and 1 in degree_row))


def tree_type_counts(p, q):
    """Numbers of all trees, no row-leaf trees, no column-leaf trees."""
    total = p ** (q - 1) * q ** (p - 1)
    no_row_leaf = q ** (p - 1) * factorial(p) * stirling(q - 1, p)
    no_col_leaf = p ** (q - 1) * factorial(q) * stirling(p - 1, q)
    assert total >= no_row_leaf + no_col_leaf
    return total, no_row_leaf, no_col_leaf


@lru_cache(None)
def forest_profile(m, n):
    """Counts labeled two-color forests by edge count and four existence flags.
    Anchor-decomposition is an independent implementation of the component EGF.
    Flag bits: isolated row 1, isolated column 2, leaf row 4, leaf column 8.
    """
    if m == 0 and n == 0:
        return {(0, 0): 1}
    out = defaultdict(int)
    if m == 0:
        for (edges, flags), count in forest_profile(0, n - 1).items():
            out[(edges, flags | 2)] += count
    else:
        for (edges, flags), count in forest_profile(m - 1, n).items():
            out[(edges, flags | 1)] += count
        for p in range(1, m + 1):
            for q in range(1, n + 1):
                total, no_row, no_col = tree_type_counts(p, q)
                # 12: leaves in both colors; 4: row only; 8: column only.
                types = ((12, total - no_row - no_col),
                         (4, no_col), (8, no_row))
                for newflags, trees in types:
                    if trees == 0:
                        continue
                    ways_to_choose_labels = comb(m - 1, p - 1) * comb(n, q)
                    for (edges, flags), count in forest_profile(m - p, n - q).items():
                        out[(edges + p + q - 1, flags | newflags)] += (
                            ways_to_choose_labels * trees * count)
    return dict(out)


def species_white_counts(m, n):
    out = defaultdict(int)
    for (edges, flags), count in forest_profile(m, n).items():
        valid = edges == 0 or ((flags & 1 and flags & 8) or
                               (flags & 2 and flags & 4))
        if valid:
            out[edges] += count
    return dict(out)


def expected_minimum_count(m, n):
    if min(m, n) < 2:
        raise ValueError('This expression is for m,n >= 2')
    return (m * (m - 1) ** (n - 1) *
            (n ** (m - 2) - factorial(n) * stirling(m - 2, n)) +
            n * (n - 1) ** (m - 1) *
            (m ** (n - 2) - factorial(m) * stirling(n - 2, m)))


def direct_counts(m, n):
    count = defaultdict(int)
    for bitmap in range(1 << (m * n)):
        white = {i for i in range(m * n) if bitmap & (1 << i)}
        direct = is_zero_forcing(m, n, white)
        structural = is_forest_and_leaf_accessible(m, n, white)
        assert direct == structural, (m, n, bitmap, direct, structural)
        if direct:
            count[len(white)] += 1
    return dict(count)


def verify_bipartite_prufer(p, q):
    """Direct edge-subset spanning-tree enumeration, not Prüfer-code generation."""
    vcount = p + q
    edges = [(a, p + b) for a in range(p) for b in range(q)]
    totals = [0, 0, 0]  # all, no row leaf, no col leaf
    for selected in __import__('itertools').combinations(edges, vcount - 1):
        par = list(range(vcount))
        degrees = [0] * vcount
        def root(z):
            while par[z] != z:
                z = par[z]
            return z
        acyclic = True
        for a, b in selected:
            degrees[a] += 1
            degrees[b] += 1
            ra, rb = root(a), root(b)
            if ra == rb:
                acyclic = False
                break
            par[ra] = rb
        if not acyclic or len({root(v) for v in range(vcount)}) != 1:
            continue
        totals[0] += 1
        totals[1] += all(d > 1 for d in degrees[:p])
        totals[2] += all(d > 1 for d in degrees[p:])
    assert tuple(totals) == tree_type_counts(p, q), (p, q, totals, tree_type_counts(p,q))
    return totals[0]


def main():
    cases = [(1,1), (1,2), (1,4), (2,2), (2,3),
             (2,4), (3,3), (3,4), (4,4)]
    tested = 0
    for m, n in cases:
        brute = direct_counts(m, n)
        species = species_white_counts(m, n)
        assert brute == species, (m, n, brute, species)
        if m >= 2 and n >= 2:
            k = m + n - 2
            assert max(brute) == k
            assert brute[k] == expected_minimum_count(m, n)
        print(f'rook {m}x{n}: PASS, white-edge counts {sorted(brute.items())}')
        tested += 1 << (m * n)
    tree_instances = 0
    for p in range(1, 5):
        for q in range(1, 5):
            tree_instances += verify_bipartite_prufer(p, q)
    # Extra nonexhaustive parameter tests of the exact closed minimum formula.
    for m in range(2, 7):
        for n in range(2, 7):
            observed = species_white_counts(m, n).get(m + n - 2, 0)
            assert observed == expected_minimum_count(m, n)
    print(f'PASS: {tested} exhaustive initial colorings; '
          f'{tree_instances} direct bipartite spanning-tree instances; '
          '25 larger parameter comparisons')

if __name__ == '__main__':
    main()
