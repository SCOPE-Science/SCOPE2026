#!/usr/bin/env python3
"""Exact finite-boundary verification for signed opinion centrality."""
from fractions import Fraction
from itertools import combinations, permutations, product


def solve(a, b):
    """Exact Gauss-Jordan elimination with first available nonzero pivot."""
    n = len(b)
    rows = [[Fraction(v) for v in a[i]] + [Fraction(b[i])]
            for i in range(n)]
    for j in range(n):
        k = next((k for k in range(j, n) if rows[k][j]), None)
        assert k is not None, "Unexpected singular positive-definite matrix"
        rows[j], rows[k] = rows[k], rows[j]
        p = rows[j][j]
        rows[j] = [v / p for v in rows[j]]
        for k in range(n):
            if k != j:
                q = rows[k][j]
                rows[k] = [x - q * y for x, y in zip(rows[k], rows[j])]
    assert all(rows[i][j] == Fraction(i == j) for i in range(n)
               for j in range(n))
    return tuple(r[-1] for r in rows)


def matrix(n, signs, edges, unsigned=False):
    h = [[int(i == j) for j in range(n)] for i in range(n)]
    for (i, j), sig in zip(edges, signs):
        if sig:
            h[i][i] += 1
            h[j][j] += 1
            x = 1 if unsigned else sig
            h[i][j] -= x
            h[j][i] -= x
    return h


def is_connected(n, signs, edges):
    seen = {0}
    frontier = [0]
    while frontier:
        i = frontier.pop()
        for (u, v), sig in zip(edges, signs):
            if sig and i in (u, v):
                j = v if i == u else u
                if j not in seen:
                    seen.add(j)
                    frontier.append(j)
    return len(seen) == n


def witness_criterion_4(signs, edges):
    # Every negative edge must meet one vertex; this vertex has no positive edges.
    for c in range(4):
        negative = [(i, j) for (i, j), sig in zip(edges, signs) if sig < 0]
        positive = [(i, j) for (i, j), sig in zip(edges, signs) if sig > 0]
        if len(negative) >= 2 and all(c in e for e in negative) and all(
                c not in e for e in positive):
            return True
    return False


def orbit_key(signs, edges, n):
    d = {edge: sig for edge, sig in zip(edges, signs)}
    return min(tuple(d[tuple(sorted((p[i], p[j])))] for i, j in edges)
               for p in permutations(range(n)))


def run():
    cases = 0
    for n in (2, 3, 4):
        edges = tuple(combinations(range(n), 2))
        connected = negative = 0
        classes = {}
        min_h = Fraction(2)
        for signs in product((-1, 0, 1), repeat=len(edges)):
            if not is_connected(n, signs, edges):
                continue
            connected += 1
            h = solve(matrix(n, signs, edges), (1,) * n)
            assert all(sum(matrix(n, signs, edges)[i][j] * h[j]
                           for j in range(n)) == 1 for i in range(n))
            assert all(v >= Fraction(3-n, n+1) for v in h)
            if n >= 3:
                hp = matrix(n, signs, edges, unsigned=True)
                # Extract the diagonal of the unsigned Green matrix exactly.
                for i in range(n):
                    ei = tuple(int(j == i) for j in range(n))
                    gii = solve(hp, ei)[i]
                    assert h[i] >= min(Fraction(0), 2*gii - 1)
                    assert gii >= Fraction(2, n+1)
            lowest = min(h)
            min_h = min(min_h, lowest)
            has_negative = lowest < 0
            if has_negative:
                negative += 1
                if n == 4:
                    key = orbit_key(signs, edges, n)
                    classes[key] = classes.get(key, 0) + 1
            if n == 4:
                assert has_negative == witness_criterion_4(signs, edges)
            cases += 1
        print(f'n={n}: connected={connected}, negative={negative}, min={min_h}')
        if n == 2:
            assert (connected, negative, min_h) == (2, 0, Fraction(1,3))
        if n == 3:
            assert (connected, negative, min_h) == (20, 0, Fraction(0))
        if n == 4:
            assert (connected, negative, min_h) == (624, 104, Fraction(-1,5))
            sizes = sorted(classes.values())
            assert sizes == [4, 4, 12, 12, 12, 12, 24, 24]
            expected = {
                (-1,-1,-1,0,0,0):4,
                (-1,-1,0,0,0,1):24,
                (-1,-1,-1,0,0,1):12,
                (-1,-1,0,0,1,1):12,
                (-1,-1,0,1,0,1):24,
                (-1,-1,-1,0,1,1):12,
                (-1,-1,0,1,1,1):12,
                (-1,-1,-1,1,1,1):4,
            }
            assert classes == expected
            for key, size in sorted(classes.items()):
                print(' '.join('-' if v == -1 else '+' if v == 1 else '.'
                               for v in key), size)
    # Arbitrary-n equality witness, independent closed-form substitution.
    for n in range(3, 31):
        a = Fraction(3-n, n+1)
        b = Fraction(n-1, n+1)
        assert (n*a - (-(n-1))*b) == 1
        assert 2*b + a == 1
    print(f'PASS: {cases} connected signed graphs, full 4-vertex classification, '
          'and 28 arbitrary-size equality witnesses')


if __name__ == '__main__':
    run()
