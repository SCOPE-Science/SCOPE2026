"""Independent small-order checks for partial weak-majority colourings of clique prisms.

Run with Python 3.10+. The mathematical proof, not finite testing, establishes
claims for arbitrary orders.
"""
from math import factorial
from itertools import combinations


def colourings_canonical(v):
    # A zero means uncolored. Positive colors appear in restricted-growth order.
    f = [0] * v
    def rec(i, top):
        if i == v:
            yield tuple(f), top
        else:
            for c in range(top + 2):
                f[i] = c
                yield from rec(i + 1, top + (c == top + 1))
    yield from rec(0, 0)


def admissible(f, n):
    # Brute-force graph-neighborhood definition; independent of the proof's
    # row-size inequality and the structural classification.
    for v, c in enumerate(f):
        if c == 0:
            continue
        layer, j = divmod(v, n)
        neighbors = [layer*n + h for h in range(n) if h != j]
        neighbors.append((1-layer)*n + j)
        same = 1 + sum(f[w] == c for w in neighbors)
        total = 1 + sum(f[w] != 0 for w in neighbors)
        if 2*same < total:
            return False
    return True


def predicted_unlabelled(n):
    # Here each 4-class partition has exactly 4! named four-colour labelings.
    # The sum treats the two labels within each layer as ordered (4-to-1).
    val = 0
    for a in range(1, n // 2 + 1):
        for b in range(1, (n - 2 * a) // 2 + 1):
            val += factorial(n) // (factorial(a)**2 * factorial(b)**2 * factorial(n - 2*a - 2*b))
    return val // 4


def all_checks():
    expected = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4}
    for n in expected:
        best = 0
        number_best = 0
        n_four = 0
        for f, k in colourings_canonical(2*n):
            if k < max(best, 4 if n >= 4 else 0):
                continue
            if admissible(f, n):
                if k > best:
                    best = k
                    number_best = 1
                elif k == best:
                    number_best += 1
                if k == 4:
                    n_four += 1
                    x = set(i for i in range(n) if f[i])
                    y = set(i for i in range(n) if f[n+i])
                    assert x.isdisjoint(y)
                    assert len(x) % 2 == len(y) % 2 == 0
                    assert len(set(f[:n]) - {0}) == 2
                    assert len(set(f[n:]) - {0}) == 2
                    assert not ((set(f[:n]) - {0}) & (set(f[n:]) - {0}))
        assert best == expected[n], (n, best)
        if n >= 4:
            assert n_four == predicted_unlabelled(n), (n, n_four, predicted_unlabelled(n))
        print(f'n={n}: max colours={best}; canonical optimum partitions={number_best}; canonical four-colour partitions={n_four}')
    for n in range(4, 45):
        # Explicit construction gives a correct colouring for every n >= 4.
        f = [0]*(2*n)
        f[0], f[1], f[n+2], f[n+3] = 1, 2, 3, 4
        assert admissible(f, n)
        assert predicted_unlabelled(n) > 0
    print('All checks passed; orders through 5 exhaustive, orders 4..44 constructive.')

if __name__ == '__main__':
    all_checks()
