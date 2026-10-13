"""Definition-based finite checks for the visibility polynomial of half graphs.

Run: python3 verify.py
Only the standard library is used. Generic breadth-first search tests geodesic
visibility; the enumerator independently implements the boundary-pair formula.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def half_graph(n):
    adjacency = [set() for _ in range(2 * n)]
    for i in range(n):
        for j in range(i, n):
            adjacency[i].add(n + j)
            adjacency[n + j].add(i)
    return adjacency


def distance(adjacency, source, target, forbidden=0):
    todo = deque([(source, 0)])
    seen = {source}
    while todo:
        vertex, depth = todo.popleft()
        if vertex == target:
            return depth
        for nxt in adjacency[vertex]:
            if nxt not in seen and (not (forbidden >> nxt & 1) or nxt == target):
                seen.add(nxt)
                todo.append((nxt, depth + 1))
    return None


def by_geodesics(adjacency, selection):
    points = [v for v in range(len(adjacency)) if selection >> v & 1]
    return all(distance(adjacency, a, b) == distance(adjacency, a, b, selection)
               for a, b in combinations(points, 2))


def by_boundaries(n, selection):
    A = [i + 1 for i in range(n) if selection >> i & 1]
    B = [i + 1 for i in range(n) if selection >> (n + i) & 1]
    if not A or not B:
        return True
    q, p = max(A), min(B)
    if q < p:
        return True
    if q > p:
        return (any(i not in A for i in range(1, p + 1))
                and any(j not in B for j in range(q, n + 1)))
    return ((len(A) == 1 or any(j not in B for j in range(q, n + 1)))
            and (len(B) == 1 or any(i not in A for i in range(1, p + 1))))


def binomial(n):
    return [comb(n, i) for i in range(n + 1)]


def add_to(target, source, shift=0, coefficient=1):
    for k, value in enumerate(source):
        target[k + shift] += coefficient * value


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def polynomial_formula(n):
    out = [0] * (2 * n + 1)
    add_to(out, binomial(n), coefficient=2)
    out[0] -= 1
    for q in range(1, n + 1):
        for p in range(1, n + 1):
            if q < p:
                add_to(out, binomial(q - 1 + n - p), 2)
            elif q > p:
                first = binomial(q - 1)
                second = binomial(n - p)
                add_to(first, binomial(q - p - 1), p, -1)
                add_to(second, binomial(q - p - 1), n - q + 1, -1)
                add_to(out, multiply(first, second), 2)
            else:
                add_to(out, binomial(n - 1), 2)
                term_a = binomial(p - 1)
                term_b = binomial(n - p)
                term_a[0] -= 1
                term_b[0] -= 1
                add_to(out, term_a, n - p + 2, -1)
                add_to(out, term_b, p + 1, -1)
                if 2 <= p <= n - 1:
                    out[n + 1] += 1
    return out


def verify():
    tested = 0
    for n in range(3, 9):
        adjacency = half_graph(n)
        counts = Counter()
        for selection in range(1 << (2 * n)):
            direct = by_geodesics(adjacency, selection)
            assert direct == by_boundaries(n, selection), (n, selection)
            counts[selection.bit_count()] += direct
            tested += 1
        formula = polynomial_formula(n)
        assert formula == [counts[k] for k in range(2 * n + 1)], n
        assert sum(formula) == (4 ** (n + 1) + 24 * n - 13) // 9, n
        assert formula[2 * n - 2] == 1 and formula[-2:] == [0, 0], n
        print('n=', n, 'count=', sum(formula), 'degree=', 2 * n - 2,
              'top=', formula[-3], 'coefficients=', formula, sep='')
    for n in range(9, 51):
        f = polynomial_formula(n)
        assert sum(f) == (4 ** (n + 1) + 24 * n - 13) // 9
        assert f[2 * n - 2] == 1 and f[2 * n - 1:] == [0, 0]
        assert f[0] == 1 and f[1] == 2 * n and f[2] == comb(2 * n, 2)
    print('PASS: exhaustive-subset-cases=', tested, '; formula-n=3..50')


if __name__ == '__main__':
    verify()
