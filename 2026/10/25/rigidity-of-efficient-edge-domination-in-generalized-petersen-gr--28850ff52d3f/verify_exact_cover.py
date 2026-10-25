#!/usr/bin/env python3
"""Independent exact-cover enumeration of dominating induced matchings in GP(n,2).

Standard-library-only Python 3. Every edge is a column; a selected edge covers its
closed line-graph neighborhood. A solution covers every column exactly once.
"""

def graph(n):
    assert n >= 5
    e = set()
    for i in range(n):
        e.add(tuple(sorted((i, (i + 1) % n))))
        e.add(tuple(sorted((i, n + i))))
        e.add(tuple(sorted((n + i, n + (i + 2) % n))))
    return tuple(sorted(e))


def neighborhoods(edges, nv):
    inc = [0] * nv
    for i, (a, b) in enumerate(edges):
        inc[a] |= 1 << i
        inc[b] |= 1 << i
    closed = [(inc[a] | inc[b]) for a, b in edges]
    return closed


def enumerate_dim(n):
    edges = graph(n)
    closed = neighborhoods(edges, 2 * n)
    columns = [[i for i, c in enumerate(closed) if c >> j & 1]
               for j in range(len(edges))]
    solutions = set()
    def rec(uncovered, rows):
        if not uncovered:
            solutions.add(frozenset(rows))
            return
        best = None
        for j in range(len(edges)):
            if not (uncovered >> j & 1):
                continue
            possible = [i for i in columns[j]
                        if (uncovered & closed[i]) == closed[i]]
            if not possible:
                return
            if best is None or len(possible) < len(best):
                best = possible
            if len(best) == 1:
                break
        for i in best:
            rec(uncovered ^ closed[i], rows + (i,))
    rec((1 << len(edges)) - 1, ())
    return edges, solutions


def predicted(n, edges):
    if n % 5:
        return set()
    by_edge = {e: i for i, e in enumerate(edges)}
    output = set()
    for shift in range(5):
        chosen = set()
        for r in range(n // 5):
            b = (5 * r + shift) % n
            choices = (( (b+1)%n, n+(b+1)%n ),
                       ( (b+3)%n, (b+4)%n ),
                       ( n+b, n+(b+2)%n ))
            for a, c in choices:
                chosen.add(by_edge[tuple(sorted((a, c)))])
        output.add(frozenset(chosen))
    return output


def main():
    for n in range(5, 31):
        edges, actual = enumerate_dim(n)
        expected = predicted(n, edges)
        assert actual == expected, (n, len(actual), len(expected))
        if n % 5 == 0:
            assert len(actual) == 5
            assert all(len(m) == 3*n//5 for m in actual)
            assert set.union(*(set(m) for m in actual)) == set(range(3*n))
            assert sum(len(m) for m in actual) == 3*n
            print('n=%d: five DIMs, exact edge partition, %d edges per DIM' % (n,3*n//5))
        else:
            print('n=%d: no DIM' % n)
    print('EXACT_COVER_OK')


if __name__ == '__main__':
    main()
