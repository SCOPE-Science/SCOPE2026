"""Independent exhaustive checks of locating-dominating coalitions.

Run with Python 3.10 or newer, no third-party dependencies.
"""
from collections import Counter
from itertools import product


def partitions(n):
    """Each unordered set partition exactly once, as an RGS."""
    a = [0] * n
    def rec(i, highest):
        if i == n:
            groups = [0] * (highest + 1)
            for v, j in enumerate(a):
                groups[j] |= 1 << v
            yield tuple(groups)
        else:
            for k in range(highest + 2):
                a[i] = k
                yield from rec(i+1, max(highest, k))
    yield from rec(1, 0)


def ld_table(sizes):
    n = sum(sizes)
    part = [j for j, s in enumerate(sizes) for _ in range(s)]
    adj = [sum(1 << w for w in range(n) if part[w] != part[v]) for v in range(n)]
    table = [False] * (1 << n)
    for s in range(1 << n):
        outside = [v for v in range(n) if not s & (1 << v)]
        neighbors = [adj[v] & s for v in outside]
        table[s] = all(neighbors) and len(set(neighbors)) == len(outside)
    return table


def direct(sizes):
    n = sum(sizes)
    ld = ld_table(sizes)
    hist = Counter()
    for groups in partitions(n):
        if any(ld[g] for g in groups):
            continue
        k = len(groups)
        if all(any(i != j and ld[groups[i] | groups[j]] for j in range(k)) for i in range(k)):
            hist[k] += 1
    return hist


def formula(r):
    return 2**(r-3) * (4**r - 5*2**r + 6) if r >= 3 else 1


def graph_edge_pattern_count(r):
    # Count all surjective r-tuples of six possible inter-block edges
    # that produce a 4-block LDC partition. Each has 2**r orientations.
    ed = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
    good = 0
    for chosen in product(range(6), repeat=r):
        edges = set(chosen)
        vertex_covers = [(i,j) for i in range(4) for j in range(i+1,4)
                         if all(i in ed[e] or j in ed[e] for e in edges)]
        if not vertex_covers:
            continue
        if not any(all(v in ed[t] for t in edges) for v in range(4)) and all(any(v in cover for cover in vertex_covers) for v in range(4)):
            # every part has two vertices in different blocks by construction
            good += 1
    return good * 2**r // 24


def test_auxiliary_five_block_obstruction():
    # Independent exhaustive test of the abstract two-cover lemma,
    # including possible loops and repeated twin-class occupancy.
    k = 5
    edges = [(i, i) for i in range(k)] + [
        (i, j) for i in range(k) for j in range(i+1, k)]
    for mask in range(1, 1 << len(edges)):
        chosen = [e for t, e in enumerate(edges) if mask & (1 << t)]
        if any(all(v in e for e in chosen) for v in range(k)):
            continue
        pairs = [(a,b) for a in range(k) for b in range(a+1,k)
                 if all(a in e or b in e for e in chosen)]
        assert not all(any(v in p for p in pairs) for v in range(k)), (mask, chosen)
    print('AUXILIARY_LOOP_MULTIGRAPH_NO_FIVE_BLOCK_COVER_OK', (1 << len(edges))-1)


def main():
    tests = [(2,2),(2,3),(2,4),(3,3),(2,2,2),(3,2,2),(2,2,2,2),
             (3,3,2),(2,2,2,2,2),(3,2,2,2)]
    for sizes in tests:
        result = direct(sizes)
        prediction = 4 if all(s == 2 for s in sizes) else 3
        assert max(result) == prediction, (sizes, result, prediction)
        if prediction == 4:
            assert result[4] == formula(len(sizes)), (sizes, result)
        print('DIRECT_ALL_VERTEX_PARTITIONS_OK', sizes, 'maximum', max(result),
              'four-block_count', result.get(4,0))
    test_auxiliary_five_block_obstruction()
    for r in range(2, 7):
        count = graph_edge_pattern_count(r)
        assert count == formula(r), (r, count, formula(r))
        print('INDEPENDENT_EDGE_ASSIGNMENT_COUNT_OK', r, count)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
