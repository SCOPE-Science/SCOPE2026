"""Independent finite word-model and spanning-tree checks for theta graphs."""
from collections import Counter
from itertools import product, combinations
from math import prod


def edges_for(lengths):
    edges = []
    n = 2
    for length in lengths:
        vs = [0] + list(range(n, n + length - 1)) + [1]
        n += length - 1
        edges += list(zip(vs, vs[1:]))
    return n, edges


def word_census(lengths):
    """Enumerate signs only; count constrained patterns without checking DAGs."""
    path_words = [list(product((0, 1), repeat=L)) for L in lengths]
    result = Counter()
    for words in product(*path_words):
        plus_full = {i for i, w in enumerate(words) if all(w)}
        minus_full = {i for i, w in enumerate(words) if not any(w)}
        if plus_full and minus_full:
            continue
        bad = 0
        for i, w in enumerate(words):
            if len(w) == 1:
                # This unique direct path can have a parallel directed
                # alternative through a full-sign second path.
                if (w[0] and plus_full - {i}) or (not w[0] and minus_full - {i}):
                    bad += 1
                continue
            if sum(w) == 1 and plus_full - {i}:
                bad += 1
            elif sum(w) == len(w) - 1 and minus_full - {i}:
                bad += 1
        result[sum(lengths) - bad] += 1
    return result


def formula(lengths):
    """Calculate the asserted product by elementary polynomial arithmetic."""
    A, B = [1], [1]
    def mul(f, g):
        h = [0] * (len(f) + len(g) - 1)
        for i, a in enumerate(f):
            for j, b in enumerate(g):
                h[i+j] += a*b
        return h
    for L in lengths:
        A = mul(A, [2**L - L - 1, L])
        B = mul(B, [2**L - L - 2, L])
    out = Counter()
    for q, (a, b) in enumerate(zip(A, B)):
        count = 2*(a-b) + (prod(2**L-2 for L in lengths) if q == 0 else 0)
        if count: out[sum(lengths)-q] = count
    return out


def tree_count_via_union_find(lengths):
    n, edges = edges_for(lengths)
    count = 0
    for indexes in combinations(range(len(edges)), n-1):
        parent = list(range(n))
        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        ok = True
        for index in indexes:
            u, v = edges[index]
            a, b = find(u), find(v)
            if a == b:
                ok = False
                break
            parent[a] = b
        if ok and len({find(v) for v in range(n)}) == 1:
            count += 1
    return count


def run():
    tested = 0
    for lengths in ((2,2,2),(2,3,4),(3,3,3),(2,2,2,2),
                    (1,2,3,4),(2,2,2,2,2),(1,2,2),
                    (1,3,4),(2,2,3),(2,2,2,3),(3,3,3,3)):
        observed = word_census(lengths)
        expected = formula(lengths)
        assert observed == expected, (lengths, observed, expected)
        tree_count = tree_count_via_union_find(lengths)
        direct_formula = sum(prod(lengths[j] for j in range(len(lengths)) if j != i)
                             for i in range(len(lengths)))
        assert tree_count == direct_formula, (lengths, tree_count, direct_formula)
        n = 2 + sum(x-1 for x in lengths)
        assert observed[n-1] == 2*tree_count, (lengths, observed, tree_count)
        tested += 1
    print(f'WORD_AND_SPANNING_TREE_PASS cases={tested}')

if __name__ == '__main__':
    run()
