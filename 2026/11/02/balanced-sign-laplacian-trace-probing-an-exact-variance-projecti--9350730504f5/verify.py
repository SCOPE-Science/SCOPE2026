"""Exact finite support checks for permutation edge-count degeneracy."""
from itertools import combinations
from random import Random


def masks(n, pairs, k):
    ans = []
    for a in map(set, combinations(range(n), k)):
        first = sum(1 << i for i, (x, y) in enumerate(pairs) if x in a and y in a)
        second = sum(1 << i for i, (x, y) in enumerate(pairs) if x not in a and y not in a)
        ans.append((first, second))
    return ans


def check_stats(values, k, ell, regular, additive):
    # Covariance is singular iff centered (equivalently, anchored) points have rank < 2.
    a, b = values[0]
    d = [(x-a, y-b) for x, y in values]
    u, v = next(((x, y) for x, y in d if x or y), (0, 0))
    singular = all(u*y == v*x for x, y in d)
    assert singular == (regular or additive)
    assert all(x == y for x, y in d) == regular
    assert all((ell-1)*x+(k-1)*y == 0 for x, y in d) == additive
    if k == ell:
        assert all(x+y == 0 for x, y in d) == additive


def unweighted():
    total = 0
    for n in (4, 5, 6):
        pairs = list(combinations(range(n), 2))
        full = (1 << len(pairs))-1
        stars = {sum(1 << i for i, e in enumerate(pairs) if j in e) for j in range(n)}
        additive = {0, full} | stars | {full ^ s for s in stars}
        for k in range(2, n//2+1):
            partitions = masks(n, pairs, k)
            for g in range(full+1):
                ds = {(g & s).bit_count() for s in stars}
                vals = [((g & x).bit_count(), (g & y).bit_count()) for x, y in partitions]
                check_stats(vals, k, n-k, len(ds) == 1, g in additive)
                total += 1
    return total


def weighted():
    rng = Random(22205)
    total = 0
    for n in (4, 5, 7, 8):
        pairs = list(combinations(range(n), 2))
        for k in range(2, n//2+1):
            partitions = masks(n, pairs, k)
            for run in range(80):
                u = [rng.randrange(-5, 7) for _ in range(n)]
                if run % 3 == 0:
                    w = [u[i]+u[j] for i, j in pairs]
                elif run % 3 == 1:
                    w = [u[min(j-i, n-(j-i))] for i, j in pairs]  # circulant
                else:
                    w = [rng.randrange(-5, 7) for _ in pairs]
                degrees = [sum(z for e, z in zip(pairs, w) if i in e) for i in range(n)]
                W = sum(w)
                additive = all((n-2)*(n-1)*z == (n-1)*(degrees[i]+degrees[j])-2*W
                               for (i, j), z in zip(pairs, w))
                def dot(mask):
                    return sum(z for i, z in enumerate(w) if (mask >> i) & 1)
                vals = [(dot(x), dot(y)) for x, y in partitions]
                check_stats(vals, k, n-k, len(set(degrees)) == 1, additive)
                total += 1
    return total


if __name__ == '__main__':
    print('PASS:', unweighted(), 'simple graph/size cases;', weighted(), 'weighted cases.')
