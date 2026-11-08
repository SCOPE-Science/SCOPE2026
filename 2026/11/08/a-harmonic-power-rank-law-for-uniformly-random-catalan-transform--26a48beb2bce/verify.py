"""Finite exact consistency checks for the power-rank law in Catalan monoids.

No probabilistic inference is made from finite enumeration. Standard-library only.
"""
from collections import Counter
from math import comb


def maps(n):
    def generate(a):
        i = len(a) + 1
        if i > n:
            yield tuple(a)
        else:
            for y in range(a[-1], i + 1):
                yield from generate(a + [y])
    yield from generate([1])


def image_powers(f, kmax):
    a = tuple(range(1, len(f) + 1))
    out = [len(a)]
    for _ in range(kmax):
        a = tuple(f[i - 1] for i in a)
        out.append(len(set(a)))
    return out


def depth_in_forest(f, x):
    d = 0
    for y in range(x + 1, len(f) + 1):
        j = y
        while f[j - 1] != j:
            j = f[j - 1]
            d += (j == x)
    return d


def predicted_image_ranks(f, kmax):
    n = len(f)
    # For k>=1, a nonfixed vertex occurs as an image if and only if
    # it has a descendant k generations below it in the parent forest.
    actual_parents = [v - 1 for v in f]
    result = [n]
    roots = {i for i, v in enumerate(f, 1) if v == i}
    for k in range(1, kmax + 1):
        im = set(roots)
        for u in range(1, n + 1):
            v = u
            for _ in range(k):
                v = f[v - 1]
            im.add(v)
        # Now build independently from strict descendants, to avoid
        # using iterative image sets as the comparison oracle.
        predicted = set(roots)
        for target in range(1, n + 1):
            for u in range(1, n + 1):
                v = u
                steps = 0
                while f[v - 1] != v:
                    v = f[v - 1]
                    steps += 1
                    if v == target and steps >= k:
                        predicted.add(target)
                        break
                if target in predicted:
                    break
        assert im == predicted, (f, k, im, predicted)
        result.append(len(predicted))
    return result


def main():
    total = 0
    for n in range(1, 11):
        rank_totals = [0] * min(n, 5)
        num = 0
        for f in maps(n):
            a = image_powers(f, min(n, 5) - 1)
            b = predicted_image_ranks(f, min(n, 5) - 1)
            assert a == b, (n, f, a, b)
            for k, v in enumerate(a):
                rank_totals[k] += v
            num += 1
        assert num == comb(2*n, n)//(n+1)
        print('EXACT_OK', n, 'maps', num, 'mean_rank_numerators', rank_totals)
        total += num
    print('VERIFY_OK', total)

if __name__ == '__main__':
    main()
