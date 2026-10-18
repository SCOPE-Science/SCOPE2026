"""Independent finite checks and constructive witnesses for odd biclique covers of cycle bouquets.

Run with Python 3: python verify_bouquets.py
No external dependencies are required. Finite checks supplement, not replace, the proof.
"""
from itertools import combinations, product


def cycle_bouquet(lengths):
    assert len(lengths) >= 1 and all(l >= 3 for l in lengths)
    next_id = 1
    petals = []
    edges = set()
    for length in lengths:
        p = tuple(range(next_id, next_id + length - 1))
        next_id += length - 1
        petals.append(p)
        cycle = (0,) + p
        for i in range(len(cycle)):
            edges.add(tuple(sorted((cycle[i], cycle[(i + 1) % len(cycle)]))))
    return next_id, petals, edges


def witness_bicliques(lengths):
    n, petals, target = cycle_bouquet(lengths)
    chosen = []
    odd = [i for i, l in enumerate(lengths) if l % 2]
    even = [i for i, l in enumerate(lengths) if l % 2 == 0]

    # Two triangles with one common vertex are represented by two bicliques.
    for i, j in zip(odd[::2], odd[1::2]):
        a, b = petals[i][0], petals[i][-1]
        c, d = petals[j][0], petals[j][-1]
        chosen.append((frozenset((b, d)), frozenset((0, c))))
        chosen.append((frozenset((a, c)), frozenset((0, b))))
    if len(odd) % 2:
        p = petals[odd[-1]]
        a, b = p[0], p[-1]
        chosen.append((frozenset((0,)), frozenset((a, b))))
        chosen.append((frozenset((a,)), frozenset((b,))))

    # Each square has one biclique.
    for i in even:
        p = petals[i]
        chosen.append((frozenset((0, p[1])), frozenset((p[0], p[-1]))))

    # Replace an edge u-v with a length-three path u-x-y-v by toggling a K2,2.
    for i, l in enumerate(lengths):
        p = petals[i]
        if l % 2:
            u = p[0]
            extra = p[1:-1]
        else:
            u = p[1]
            extra = p[2:-1]
        v = p[-1]
        assert len(extra) % 2 == 0
        for x, y in zip(extra[::2], extra[1::2]):
            chosen.append((frozenset((u, y)), frozenset((x, v))))
            u = y

    expected = sum((l - 1) // 2 for l in lengths) + (len(odd) % 2)
    assert len(chosen) == expected
    assert all(a and b and not (a & b) for a, b in chosen)
    return n, target, chosen


def covered_edges(bicliques):
    out = set()
    for left, right in bicliques:
        for u in left:
            for v in right:
                edge = tuple(sorted((u, v)))
                if edge in out:
                    out.remove(edge)
                else:
                    out.add(edge)
    return out


def rank2(n, edges):
    rows = [0] * n
    for u, v in edges:
        rows[u] ^= 1 << v
        rows[v] ^= 1 << u
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, n) if rows[i] & (1 << col)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(n):
            if i != rank and rows[i] & (1 << col):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def all_biclique_masks(n):
    pairs = list(combinations(range(n), 2))
    masks = set()
    for labels in product((0, 1, 2), repeat=n):
        if 1 not in labels or 2 not in labels:
            continue
        mask = sum(1 << i for i, (u, v) in enumerate(pairs)
                   if labels[u] + labels[v] == 3)
        masks.add(mask)
    return pairs, masks


def exact_min_le_four(n, target):
    pairs, masks = all_biclique_masks(n)
    t = sum(1 << i for i, edge in enumerate(pairs) if edge in target)
    if t == 0: return 0
    if t in masks: return 1
    pair_sums = {a ^ b for a in masks for b in masks}
    if t in pair_sums: return 2
    if any(t ^ a in pair_sums for a in masks): return 3
    # For sizes tested below, the constructive witness shows the minimum is 4.
    return 4


def main():
    tested = 0
    largest_n = 0
    for t in range(1, 5):
        for lengths in product(range(3, 9), repeat=t):
            n, edges, covering = witness_bicliques(lengths)
            if n > 24: continue
            assert covered_edges(covering) == edges, lengths
            expected_rank = 2 * sum((l - 1) // 2 for l in lengths)
            assert rank2(n, edges) == expected_rank, lengths
            assert len(edges) == sum(lengths)
            tested += 1
            largest_n = max(n, largest_n)
    print('constructive/rank cases:', tested, 'max vertices:', largest_n)
    exact_cases = [(3,), (4,), (5,), (6,), (7,),
                   (3, 3), (3, 4), (3, 5), (4, 4), (3, 3, 3)]
    for lengths in exact_cases:
        n, edges, covering = witness_bicliques(lengths)
        assert n <= 7
        exact = exact_min_le_four(n, edges)
        expected = len(covering)
        assert exact == expected, (lengths, exact, expected)
        print('brute-force minimum', lengths, exact)
    print('all checks passed')


if __name__ == '__main__':
    main()
