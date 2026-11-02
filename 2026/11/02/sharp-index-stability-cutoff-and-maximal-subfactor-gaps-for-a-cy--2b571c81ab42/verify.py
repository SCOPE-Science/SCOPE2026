"""Exact finite tests for maximal disjoint translates of {0,1,4} in cyclic groups.

No third-party packages are required. Run with: python verify.py
"""
from collections import Counter

GAPS = (2, 5, 6, 7, 8, 9)
DELTA = (-4, -3, -1, 1, 3, 4)


def valid_gaps(gaps):
    if not gaps:
        return False
    k = len(gaps)
    if any(g not in GAPS for g in gaps):
        return False
    for i, g in enumerate(gaps):
        before, after = gaps[(i - 1) % k], gaps[(i + 1) % k]
        if g == 2 and (before == 2 or after == 2):
            return False
        if g >= 7 and (before != 2 or after != 2):
            return False
    return True


def selected_from_gaps(gaps):
    n = sum(gaps)
    b, out = 0, set()
    for gap in gaps:
        if b in out:
            raise ValueError('repeated selected vertex')
        out.add(b)
        b = (b + gap) % n
    if b != 0 or len(out) != len(gaps):
        raise ValueError('invalid circular gaps')
    return n, out


def direct_maximal(n, chosen):
    # Independent translates plus maximality checked without using the gap rule.
    delta = {d % n for d in DELTA}
    for b in chosen:
        for c in chosen:
            if c != b and (c - b) % n in delta:
                return False
    return len(set(chosen) | {(b + d) % n for b in chosen for d in DELTA}) == n


def graph_size_counts(n):
    # Independent/maximal subsets, independently constructed from the difference graph.
    # Delta residues may collide in small n, hence OR masks, not a sum.
    neigh = [sum(1 << j for j in {(i + d) % n for d in DELTA}) for i in range(n)]
    counts = Counter()
    for mask in range(1, 1 << n):
        bits = mask
        good = True
        covered = mask
        while bits:
            lsb = bits & -bits
            i = lsb.bit_length() - 1
            if mask & neigh[i]:
                good = False
                break
            covered |= neigh[i]
            bits -= lsb
        if good and covered == (1 << n) - 1:
            counts[mask.bit_count()] += 1
    return counts


def gap_size_counts(n):
    # Independent weighted-composition enumeration of all cyclic gap words.
    words = Counter()
    def rec(rem, path):
        if rem == 0:
            if valid_gaps(path):
                words[len(path)] += 1
            return
        if rem < 0:
            return
        for g in GAPS:
            if g <= rem:
                path.append(g)
                rec(rem - g, path)
                path.pop()
    rec(n, [])
    counts = {}
    for k, w in words.items():
        assert (n * w) % k == 0
        counts[k] = n * w // k
    return Counter(counts)


WITNESSES = {
    14: ((2, 6, 6), (2, 5, 2, 5)),
    15: ((5, 5, 5), (2, 5, 2, 6)),
    16: ((5, 5, 6), (2, 5, 2, 7)),
    17: ((5, 6, 6), (2, 5, 2, 8)),
    18: ((6, 6, 6), (2, 5, 2, 9)),
}


def insert_five(gaps):
    # A 5-gap inserted after an edge with both neighboring gaps <= 6
    # preserves the local admissibility conditions.
    gaps = list(gaps)
    for i in range(len(gaps)):
        if gaps[i] <= 6 and gaps[(i + 1) % len(gaps)] <= 6:
            gaps.insert(i + 1, 5)
            assert valid_gaps(gaps)
            return tuple(gaps)
    raise ValueError('no insertion edge')


def main():
    checked = 0
    for n in range(5, 19):
        graph = graph_size_counts(n)
        gaps = gap_size_counts(n)
        assert graph == gaps, (n, graph, gaps)
        expected = [1] if n in (5, 6) else [2] if n <= 11 else [2, 3] if n == 12 else [3] if n == 13 else [3, 4]
        assert sorted(graph) == expected, (n, graph)
        checked += 1
    for base, pair in WITNESSES.items():
        a, b = pair
        for step in range(30):
            n = base + 5 * step
            assert len(b) == len(a) + 1
            for w in (a, b):
                assert sum(w) == n and valid_gaps(w)
                nm, chosen = selected_from_gaps(w)
                assert nm == n and direct_maximal(n, chosen), (n, w)
            a, b = insert_five(a), insert_five(b)
            checked += 2
    print('VERIFY_OK')
    print('Exhaustive independent graph/gap size-count comparisons: 14 orders, n=5..18.')
    print('Constructive two-size witnesses independently tested: 300 configurations through n=163.')
    print('Stable orders n>=5: 5,6,7,8,9,10,11,13; all n>=14 have two constructive sizes.')

if __name__ == '__main__':
    main()
