"""Exact finite checks for a capped-path metric Lipschitz-polytope facet law.

This is a finite verification aid, not a substitute for the all-n proof.
Uses only the Python standard library.
"""
from itertools import product


def actual_vertex(word):
    n = len(word)
    adjacency = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            gap = min(j - i, 2)
            diff = abs(word[i] - word[j])
            if diff > gap:
                return False
            if diff == gap:
                adjacency[i].append(j)
                adjacency[j].append(i)
    reachable = {0}
    frontier = [0]
    while frontier:
        for j in adjacency[frontier.pop()]:
            if j not in reachable:
                reachable.add(j)
                frontier.append(j)
    return len(reachable) == n


def classified_vertex(word):
    if min(word) != 0:
        return False
    if max(word) == 1:
        return all(word[i] != word[i + 1] for i in range(len(word) - 1))
    if max(word) != 2:
        return False
    if any(abs(word[i] - word[i + 1]) > 1 for i in range(len(word) - 1)):
        return False
    return all(value != 1 or
               (i > 0 and word[i - 1] != 1) or
               (i + 1 < len(word) and word[i + 1] != 1)
               for i, value in enumerate(word))


def product_polynomials(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def generating_coefficients(nmax):
    # h(z) = N(z) / (A(z) B(z)),
    # N(z) = 2 z^3 (1+z)^3, A=1-z-2z^2-2z^3,
    # B=1-z-z^2-z^3. The facet coefficient is h_n+2 for n>=2.
    denominator = product_polynomials([1, -1, -2, -2], [1, -1, -1, -1])
    numerator = [0, 0, 0, 2, 6, 6, 2]
    coefficients = [0] * (nmax + 1)
    for n in range(nmax + 1):
        coefficients[n] = (numerator[n] if n < len(numerator) else 0) - sum(
            denominator[j] * coefficients[n - j]
            for j in range(1, min(n, len(denominator) - 1) + 1)
        )
    return [coefficients[n] + 2 for n in range(nmax + 1)]


def run():
    g = generating_coefficients(24)
    assert g[2:11] == [2, 4, 12, 32, 84, 216, 536, 1304, 3124]
    assert all(x > 0 for x in g[2:])
    total_words = 0
    total_vertices = 0
    for n in range(2, 11):
        vertices = set()
        predicted = set()
        for word in product((0, 1, 2), repeat=n):
            if min(word) != 0:
                continue
            total_words += 1
            if actual_vertex(word):
                vertices.add(word)
            if classified_vertex(word):
                predicted.add(word)
        assert vertices == predicted, n
        assert len(vertices) == g[n], (n, len(vertices), g[n])
        total_vertices += len(vertices)
        print(f'n={n}: vertices={len(vertices)}; rational generating coefficient={g[n]}')
    print(f'PASS: all {total_words} normalized ternary candidates examined; '
          f'{total_vertices} extreme words reproduced by 3 independent descriptions')


if __name__ == '__main__':
    run()
