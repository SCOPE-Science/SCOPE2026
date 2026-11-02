"""Exact finite checks for a pseudo-Frobenius family of five consecutive squares.

The unbounded theorem follows from the symbolic integer inequalities in RESULT.md,
not from extrapolation of these computations.
"""
import heapq


def apery(n):
    m = n * n
    generators = tuple((n + i) ** 2 for i in range(1, 5))
    shortest = [None] * m
    shortest[0] = 0
    heap = [(0, 0)]
    while heap:
        value, residue = heapq.heappop(heap)
        if value != shortest[residue]:
            continue
        for generator in generators:
            dest = (residue + generator) % m
            candidate = value + generator
            old = shortest[dest]
            if old is None or candidate < old:
                shortest[dest] = candidate
                heapq.heappush(heap, (candidate, dest))
    assert all(value is not None for value in shortest)
    return m, generators, shortest


def verify(k, exhaustive=True):
    assert k >= 4
    n = 12 * k
    a = n ** 2
    g1, g2, g3, g4 = ((n + i) ** 2 for i in range(1, 5))
    assert (n + 4) ** 2 < 2 * a
    m, generators, shortest = apery(n) if exhaustive else (None, None, None)
    count = 0
    for j in range(2 * k):
        f = 5 * g2 + 2 * j * g3 + (3 * k - 1 - j) * g4 - a
        assert f > 0
        representations = (
            2 * g2 + (5 + 2 * j) * g3 + (3 * k - 3 - j) * g4,
            (8 + 2 * j) * g3 + (3 * k - 4 - j) * g4,
            (3 * k - 4 - j) * a + (9 + 2 * j) * g1 + g2,
            (3 * k - 2 - j) * a + (4 + 2 * j) * g1 + 4 * g2,
        )
        assert all(f + g == r for g, r in zip((g1, g2, g3, g4), representations))
        t0 = 3 * k + 3 + j
        remainder = 192 * k + 48 * k * j + 4 + 2 * j
        assert f == (t0 + 2) * a + remainder
        assert 0 < remainder < a
        assert 48 * k + 8 > 36 * k + 22
        if exhaustive:
            # Exact membership criterion from shortest residue representatives.
            assert f < shortest[f % a], (k, j, 'not a gap')
            for g in (g1, g2, g3, g4):
                assert f + g >= shortest[(f + g) % a], (k, j, g)
        count += 1
    if exhaustive:
        type_count = sum(
            all(value + g > shortest[(r + g) % a] for g in generators)
            for r, value in enumerate(shortest)
        )
        assert type_count >= 2 * k
        return count, type_count
    return count, None


def main():
    cases = [4, 5, 6, 7, 8, 9, 10]
    tested = []
    for k in cases:
        witnesses, type_count = verify(k)
        tested.append((k, witnesses, type_count))
    for k in [11, 20, 50, 100, 1000]:
        verify(k, exhaustive=False)
    print('VERIFY_OK cases=', len(tested), 'witnesses=', sum(row[1] for row in tested),
          'min_type=', min(row[2] for row in tested), 'max_type=', max(row[2] for row in tested),
          'symbolic_pattern_extra_k=11,20,50,100,1000')
    print('k,witnesses,exact_type: ', tested)


if __name__ == '__main__':
    main()
