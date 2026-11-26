"""Exact finite checks for 1-limited domination minimizers on circular ladders."""

from itertools import product


def verify():
    # A column code is a + 2*b for the two membership bits a,b.
    cols = [(i & 1, i >> 1) for i in range(4)]
    states = list(product(range(4), repeat=2))
    arcs = {v: set() for v in states}
    for i, j, k in product(range(4), repeat=3):
        x, y, z = cols[i], cols[j], cols[k]
        if all((y[t] != x[t]) + (y[t] != z[t]) + (y[t] != y[1-t]) == 1
               for t in (0, 1)):
            arcs[i, j].add((j, k))

    def reachable(v):
        seen, todo = set(), [v]
        while todo:
            w = todo.pop()
            if w not in seen:
                seen.add(w)
                todo.extend(arcs[w])
        return seen

    assert sum(map(len, arcs.values())) == 10
    reach = {v: reachable(v) for v in states}
    components = {frozenset(w for w in reach[v] if v in reach[w]) for v in states}
    cycles = [c for c in components if len(c) > 1 or any(v in arcs[v] for v in c)]
    assert sorted(sorted(a+4*b for a, b in c) for c in cycles) == [[0, 3, 12, 15], [5], [10]]
    for c in cycles:
        assert all(len(arcs[v] & c) == 1 for v in c)
        assert all(sum(v in arcs[w] for w in c) == 1 for v in c)

    for n in range(3, 9):
        neighbors = [((i-1) % n, (i+1) % n, i+n) for i in range(n)] + [
            ((i-1) % n+n, (i+1) % n+n, i) for i in range(n)]
        actual = {tuple(zip(b[:n], b[n:])) for b in product(range(2), repeat=2*n)
                  if all(sum(b[i] != b[j] for j in ns) == 1
                         for i, ns in enumerate(neighbors))}
        expected = {((1, 0),)*n, ((0, 1),)*n}
        if n % 4 == 0:
            expected.update(tuple((((i+t) % 4)//2,)*2 for i in range(n)) for t in range(4))
        assert actual == expected
    print('VERIFY_OK: 16 states, 10 arcs, two loops and a four-cycle; full direct template agreement for n=3..8')


if __name__ == '__main__':
    verify()
