"""Direct finite enumeration for centralizers and clique polynomial of path weak-endomorphism monoids."""
from itertools import product, combinations
from math import comb


def maps(n):
    for start in range(1, n + 1):
        for steps in product((0, 1), repeat=n - 1):
            values = [start]
            for s in steps:
                values.append(values[-1] + s)
            if values[-1] <= n:
                yield tuple(values)


def clamp(n, a, b):
    return tuple(min(b, max(a, x)) for x in range(1, n + 1))


def compose(f, g):
    return tuple(f[v - 1] for v in g)


def count_formula(n, a, b):
    k = b - a
    L = 2**(a - 1)
    R = 2**(n - b)
    baseline = sum(comb(k, d) * (k - d + 1) for d in range(k + 1))
    return baseline + (L + R - 2) * 2**k + (L - 1) * (R - 1)


def clique_poly_formula(n):
    N = n * (n + 1) // 2
    coefficients = [0] * (N + 1)
    for j in range(1, n + 1):
        for s in range(j * (n - j + 1) + 1):
            coefficients[s] += comb(j * (n - j + 1), s)
    for j in range(1, n):
        for s in range(j * (n - j) + 1):
            coefficients[s] -= comb(j * (n - j), s)
    return coefficients


def test_centralizers(n):
    F = list(maps(n))
    expected_size = (n + 1) * 2**(n - 2) if n >= 2 else 1
    assert len(F) == expected_size
    E = [f for f in F if compose(f, f) == f]
    I = [(a, b) for a in range(1, n + 1) for b in range(a, n + 1)]
    assert set(E) == {clamp(n, a, b) for a,b in I}
    total_commuting_pairs = 0
    for a, b in I:
        e = clamp(n, a, b)
        actual = sum(compose(f, e) == compose(e, f) for f in F)
        expected = count_formula(n, a, b)
        assert actual == expected, (n, a, b, actual, expected)
        total_commuting_pairs += actual
    for a, b in I:
        for c, d in I:
            e1 = clamp(n, a, b)
            e2 = clamp(n, c, d)
            actual = compose(e1,e2) == compose(e2,e1)
            assert actual == (max(a,c)<=min(b,d)), (n,a,b,c,d)
    predicted_pairs = (4*n - 12) * 2**n + (n*n + 9*n) // 2 + 12
    assert total_commuting_pairs == predicted_pairs
    print(f'CENTRALIZER_OK n={n} maps={len(F)} idempotents={len(E)} pairs={total_commuting_pairs}')


def test_cliques(n):
    intervals = [(a,b) for a in range(1,n+1) for b in range(a,n+1)]
    coeffs = [0] * (len(intervals)+1)
    max_sets = []
    for mask in range(1 << len(intervals)):
        chosen = [intervals[i] for i in range(len(intervals)) if mask & (1 << i)]
        if not chosen or max(a for a,b in chosen) <= min(b for a,b in chosen):
            coeffs[len(chosen)] += 1
            if chosen and all(not (max(a for a,b in chosen+[x]) <= min(b for a,b in chosen+[x])) for x in intervals if x not in chosen):
                max_sets.append(frozenset(chosen))
    assert coeffs == clique_poly_formula(n), (coeffs,clique_poly_formula(n))
    expected = [frozenset((a,b) for a,b in intervals if a<=j<=b) for j in range(1,n+1)]
    assert set(max_sets) == set(expected)
    print(f'CLIQUE_OK n={n} cliques={sum(coeffs)} maximal={len(max_sets)}')


if __name__ == '__main__':
    for n in range(1,11):
        test_centralizers(n)
    for n in range(1,6):
        test_cliques(n)
    print('VERIFY_OK')
