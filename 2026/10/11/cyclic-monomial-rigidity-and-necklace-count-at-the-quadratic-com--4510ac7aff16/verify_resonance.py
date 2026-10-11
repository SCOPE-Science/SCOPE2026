"""Exact finite diagnostics for the cyclic resonance classification (Python 3 stdlib)."""
from itertools import combinations
from math import comb, factorial, gcd


def necklace(word):
    n = len(word)
    return min(word[j:] + word[:j] for j in range(n))


def words(p, q):
    n = p + q
    for s in combinations(range(n), q):
        yield tuple(1 if j in s else 0 for j in range(n))


def vertex_list(w, p, q):
    a = [0]
    for x in w[:-1]:
        a.append(a[-1] + (p if x else -q))
    assert a[-1] + (p if w[-1] else -q) == 0
    assert len(set(a)) == len(a)
    return a


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def power(a, k):
    n = len(a)
    b = [[int(i == j) for j in range(n)] for i in range(n)]
    for _ in range(k):
        b = multiply(b, a)
    return b


def test(p, q):
    n = p + q
    all_words = list(words(p, q))
    necklaces = {necklace(w) for w in all_words}
    assert len(necklaces) == comb(n, q) // n
    shapes = set()
    for w in necklaces:
        v = vertex_list(w, p, q)
        shapes.add(tuple(sorted(x - min(v) for x in v)))
        assert {x % n for x in v} == set(range(n))
        for a in v:
            assert sum(a + root in v for root in (p, -q)) == 1
        A = [[v[i] if i == j else 0 for j in range(n)] for i in range(n)]
        T = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            T[(j + 1) % n][j] = j + 1
        D = [[multiply(A, T)[i][j] - multiply(T, A)[i][j]
              for j in range(n)] for i in range(n)]
        AD, DA = multiply(A, D), multiply(D, A)
        assert all(AD[i][j] - DA[i][j] - (p-q)*D[i][j] - p*q*T[i][j] == 0
                   for i in range(n) for j in range(n))
        k = factorial(n)
        TN = power(T, n)
        DN = power(D, n)
        assert all(TN[i][j] == (k if i == j else 0)
                   for i in range(n) for j in range(n))
        assert all(DN[i][j] == (k * p**q * (-q)**p if i == j else 0)
                   for i in range(n) for j in range(n))
    assert len(shapes) == len(necklaces)
    return n, len(necklaces)


if __name__ == '__main__':
    cases = []
    for p in range(1, 6):
        for q in range(1, 6):
            if gcd(p, q) == 1:
                cases.append((p, q, *test(p, q)))
    assert (2, 3, 5, 2) in cases
    print('CYCLIC_RESONANCE_EXACT_FINITE_OK', len(cases), 'coprime pairs')
