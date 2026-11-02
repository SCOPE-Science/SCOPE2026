"""Self-contained reproducibility checks for signed Roman labelings of Kneser K(n,2).
Uses only the Python standard library. The mathematical proof covers all n>=12.
"""
from itertools import combinations

def construction(n):
    assert n >= 12
    if n % 2:
        a = (n - 3) // 2
        special = set()
    else:
        a = n // 2 - 1
        special = {(a, a + 1), (a + 2, a + 3), (a + 4, a + 5)}
    cycle = {tuple(sorted((i, (i + 1) % a))) for i in range(a)}
    exceptional = cycle | special
    f = {}
    for i, j in combinations(range(n), 2):
        f[i, j] = (-1 if i < a <= j else (2 if (i, j) in exceptional else 1))
    return f

def direct_check(n):
    f = construction(n)
    edges = list(f)
    weight = sum(f.values())
    expected = 3 if n % 2 else 4
    assert weight == expected, (n, 'wrong weight', weight)
    all_two = [e for e in edges if f[e] == 2]
    for e in edges:
        i, j = e
        closed = f[e] + sum(f[h] for h in edges if h != e and i not in h and j not in h)
        assert closed >= 1, (n, e, 'closed-neighborhood', closed)
        if f[e] == -1:
            assert any(i not in h and j not in h for h in all_two), (n, e, 'undefended')
    return len(edges), weight

def algebraic_check(n):
    f = construction(n)
    weight = sum(f.values())
    degrees = [sum(f[tuple(sorted((i, j)))] for j in range(n) if j != i) for i in range(n)]
    assert sum(degrees) == 2 * weight
    assert weight == (3 if n % 2 else 4)
    for (i, j), label in f.items():
        assert weight - degrees[i] - degrees[j] + 2 * label >= 1
        if label == -1:
            assert any(h[0] not in (i,j) and h[1] not in (i,j) and f[h] == 2 for h in f)

if __name__ == '__main__':
    for n in range(12, 21):
        count, weight = direct_check(n)
        print(f'n={n}: {count} vertices, weight={weight}, all closed neighborhoods and defenders passed')
    for n in range(21, 41):
        algebraic_check(n)
    print('VERIFY_OK: direct n=12..20; algebraic n=21..40')
