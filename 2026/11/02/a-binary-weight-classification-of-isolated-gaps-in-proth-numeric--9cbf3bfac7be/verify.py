"""Independent finite checks for an exact isolated-gap criterion.

Only the mathematical proof extends the result to all admissible parameters.
"""
from heapq import heappush, heappop


def popcount(x):
    return x.bit_count()


def predicted(m, k=None, n=None):
    # Minimum number of parts in a Mersenne-coin decomposition.
    best = [0] + [m + 1] * (m - 1)
    coins = [(1 << i) - 1 for i in range(1, m.bit_length() + 1)
             if (1 << i) - 1 < m]
    for t in range(1, m):
        best[t] = 1 + min(best[t - d] for d in coins if d <= t)
    apery = [0] + [(m-1)*(m-r)+m*best[m-r] for r in range(1, m)]
    q = best[m-1] - best[m-2]
    assert q in (-1, 1)
    isolate = [] if q < 0 else [apery[1] - 2*m, apery[1] - m]
    if k is not None:
        s = popcount(k)
        j = next(j for j in range(1, s + 2)
                 if s + popcount(j) <= 2*j)
        h = next(j for j in range(s + 2)
                 if s + popcount(j) <= 2*j + 1)
        assert best[m-1] == 2*j and best[m-2] == 2*h + 1
        sequence_condition = any(s == 2*j0 + 1 - popcount(j0)
                                 for j0 in range(s + 1))
        assert bool(isolate) == sequence_condition
    return apery, isolate


def independent_apery(m):
    # Shortest paths in the residue graph. Generators above the largest
    # possible minimum Mersenne-coin weight cannot affect Apéry minima.
    generators = [2**i*(m-1)+1 for i in range(1, m.bit_length()+1)
                  if 2**i - 1 < m]
    distance = [10**50] * m
    distance[0] = 0
    heap = [(0, 0)]
    while heap:
        dist, residue = heappop(heap)
        if dist != distance[residue]:
            continue
        for gen in generators:
            r = (residue + gen) % m
            new = dist + gen
            if new < distance[r]:
                distance[r] = new
                heappush(heap, (new, r))
    assert all(x < 10**50 for x in distance)
    return distance


def independent_isolated(apery, m):
    conductor = max(apery) - m + 1
    gaps = []
    for r in range(1, m):
        w = apery[r]
        # A nonnegative gap in residue r has the form w-jm, j>=1.
        for g in range(w-m, 0, -m):
            if g - 1 >= apery[(g-1) % m] and g + 1 >= apery[(g+1) % m]:
                gaps.append(g)
    assert not any(g >= conductor for g in gaps)
    return sorted(gaps)


def test(m, k=None, n=None):
    assert m >= 3
    formula_apery, formula_gaps = predicted(m, k, n)
    graph_apery = independent_apery(m)
    assert graph_apery == formula_apery, (m, 'apery')
    actual = independent_isolated(graph_apery, m)
    assert actual == formula_gaps, (m, actual, formula_gaps)
    if actual:
        assert actual == [max(graph_apery)-2*m, max(graph_apery)-m]
    return len(actual)


def main():
    general = 0
    for m in range(3, 202):
        test(m)
        general += 1
    proth = 0
    for n in range(3, 7):
        for k in range(1, 1 << n, 2):
            test(k * (1 << n) + 1, k, n)
            proth += 1
    for n, k in [(7, 1), (7, 7), (7, 31), (7, 63), (7, 127),
                 (8, 3), (8, 7), (8, 31)]:
        test(k * (1 << n) + 1, k, n)
        proth += 1
    # Also verify the Hamming-weight threshold reduction without semigroups.
    for s in range(1, 129):
        j = next(j for j in range(1, s + 2) if s + popcount(j) <= 2*j)
        h = next(j for j in range(s+1) if s + popcount(j) <= 2*j + 1)
        assert h in (j-1, j)
        hit = any(s == 2*u + 1 - popcount(u) for u in range(s+1))
        assert hit == (h == j-1)
    print('VERIFY_OK', 'general_m=' + str(general),
          'proth_pairs=' + str(proth), 'popcount_thresholds=128')


if __name__ == '__main__':
    main()
