from functools import lru_cache
from math import comb


def catalan(n):
    return comb(2 * n, n) // (n + 1)


@lru_cache(maxsize=None)
def catalan_maps(n):
    def rec(j, chosen):
        if j == n:
            yield tuple(chosen)
            return
        for value in range(chosen[-1] if chosen else 0, j + 1):
            yield from rec(j + 1, chosen + [value])
    return tuple(rec(0, []))


def weights(n, fixed):
    ds = [((fixed[j + 1] if j + 1 < len(fixed) else n + 1) - fixed[j])
          for j in range(len(fixed))]
    return [[catalan(ds[j]) if a == j else comb(ds[j] + ds[a] - 2, ds[j] - 1)
             for a in range(j + 1)] for j in range(len(ds))]


def weighted_sum(n, fixed):
    w = weights(n, fixed)
    k = len(fixed)
    total = 0
    for g in catalan_maps(k):
        count = 1
        for j in range(k):
            if j + 1 < k and g[j] == g[j + 1]:
                continue
            count *= w[j][g[j]]
        total += count
    return total


def transfer(n, fixed):
    w = weights(n, fixed)
    k = len(fixed)
    D = [1]
    for j in range(1, k):
        prefix = 0
        nd = []
        for b in range(j + 1):
            same = D[b] if b < len(D) else 0
            nd.append(same + prefix)
            if b < len(D):
                prefix += D[b] * w[j - 1][b]
        D = nd
    return sum(D[a] * w[k - 1][a] for a in range(k))


def brute(n, fixed, elements):
    e = tuple(max(s for s in fixed if s <= i) - 1 for i in range(1, n + 1))
    return sum(tuple(f[e[i]] for i in range(n)) ==
               tuple(e[f[i]] for i in range(n)) for f in elements)


def main():
    for n in range(1, 10):
        elements = catalan_maps(n)
        assert len(elements) == catalan(n)
        for mask in range(1 << (n - 1)):
            fixed = (1,) + tuple(i + 2 for i in range(n - 1) if mask & (1 << i))
            target = brute(n, fixed, elements)
            by_sum = weighted_sum(n, fixed)
            by_transfer = transfer(n, fixed)
            assert target == by_sum == by_transfer, (n, fixed, target, by_sum, by_transfer)
        print('PASS', n, len(elements), 1 << (n - 1))
    elements = catalan_maps(6)
    assert brute(6, (1, 2, 6), elements) == 18
    assert brute(6, (1, 5, 6), elements) == 31
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
