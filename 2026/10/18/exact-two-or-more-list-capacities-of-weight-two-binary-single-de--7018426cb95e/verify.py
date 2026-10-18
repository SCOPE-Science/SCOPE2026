"""Reproduce exact constant-weight-two single-deletion list-code constructions."""
from itertools import combinations


def descendants(word, n):
    bits = ['0'] * n
    for i in word:
        bits[i] = '1'
    return {''.join(bits[:j] + bits[j + 1:]) for j in range(n)}


def graph_edges(m, degree, list_size):
    if degree == 0:
        return set()
    if list_size == 2:
        assert degree == 1 and m >= 3
        shift = (m + 1) // 2
        return {(i, i + shift) for i in range(m // 2)}
    edges = set()
    even_degree = 2 * (degree // 2)
    for gap in range(1, even_degree // 2 + 1):
        for i in range(m):
            j = (i + gap) % m
            edges.add(tuple(sorted((i, j))))
    if degree % 2:
        if m % 2 == 0:
            for i in range(m // 2):
                edges.add((i, i + m // 2))
        else:
            step = (m - 1) // 2
            cycle = [(j * step) % m for j in range(m)]
            for j in range(0, m - 1, 2):
                edges.add(tuple(sorted((cycle[j], cycle[j + 1]))))
    return edges


def witness(n, list_size):
    assert n >= 2 and list_size >= 2
    if n == 3 and list_size == 2:
        return {(0, 1), (1, 2)}
    m = n - 1
    d = min(list_size - 1, m - 1)
    e = graph_edges(m, d, list_size)
    return {(i, i + 1) for i in range(m)} | {(i, j + 1) for i, j in e}


def optimum(n, list_size):
    if n == 3 and list_size == 2:
        return 2
    m = n - 1
    return m + m * min(list_size - 1, m - 1) // 2


def max_preimage_count(n, words):
    multiplicity = {}
    for w in words:
        for y in descendants(w, n):
            multiplicity[y] = multiplicity.get(y, 0) + 1
    return max(multiplicity.values(), default=0)


cases = 0
for n in range(2, 25):
    for list_size in sorted(x for x in set([2,3,4,5, n - 1, n, n + 2]) if x >= 2):
        c = witness(n, list_size)
        assert all(0 <= i < j < n for i, j in c)
        assert len(c) == optimum(n, list_size), (n, list_size, len(c), optimum(n, list_size))
        assert max_preimage_count(n, c) <= list_size, (n, list_size)
        cases += 1
print('CONSTRUCTION_OK', cases, 'cases, n=2..24, selected list sizes')

for n in range(2, 7):
    allwords = list(combinations(range(n), 2))
    masks = [descendants(w, n) for w in allwords]
    for list_size in range(2, n + 2):
        found = 0
        for mask in range(1 << len(allwords)):
            if mask.bit_count() <= found:
                continue
            code = [allwords[j] for j in range(len(allwords)) if mask >> j & 1]
            if max_preimage_count(n, code) <= list_size:
                found = len(code)
        assert found == optimum(n, list_size), (n, list_size, found, optimum(n,list_size))
        print('EXHAUSTIVE', n, list_size, found)
print('EXHAUSTIVE_OK n=2..6, all list sizes=2..n+1')
