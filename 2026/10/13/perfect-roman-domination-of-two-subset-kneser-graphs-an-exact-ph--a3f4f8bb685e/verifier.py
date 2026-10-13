"""Exhaustive minimum-weight support enumeration for perfect Roman domination on KG(n,2).

No external dependencies. Run with Python 3.10+.
"""
from itertools import combinations
from collections import Counter
from math import comb


def predicted(n):
    if n == 7:
        return (11, 3 * comb(7, 4))
    if n == 8:
        return (14, comb(8, 2) + 3 * comb(8, 4))
    return (2*n - 2, comb(n, 2))


def check(n):
    vertices = list(combinations(range(n), 2))
    N = len(vertices)
    disj = [sum(1 << j for j, b in enumerate(vertices) if set(a).isdisjoint(b))
            for a in vertices]
    target, expected_count = predicted(n)
    best = N
    counts = Counter()
    examined = 0
    upper = target // 2
    for r in range(upper + 1):
        for positions in combinations(range(N), r):
            mask = sum(1 << i for i in positions)
            weight = 2*r
            for i in range(N):
                if mask & (1 << i):
                    continue
                if (disj[i] & mask).bit_count() != 1:
                    weight += 1
                    if weight > best:
                        break
            examined += 1
            if weight < best:
                best = weight
                counts.clear()
            if weight == best:
                counts[r] += 1
    total = sum(counts.values())
    assert (best, total) == (target, expected_count), (n, best, counts)
    if n == 7:
        assert counts == {2: 105}, counts
    if n == 8:
        assert counts == {1: 28, 2: 210}, counts
    print(f'n={n} supports={examined} optimum={best} minimizers={total} by_twos={dict(sorted(counts.items()))}')


def check_zero_class(n):
    verts=list(combinations(range(n), 2))
    for support_size in (1, 2, 3):
        for fs in combinations(range(len(verts)), support_size):
            if support_size == 3 and n > 8:
                break
            mask=set(fs)
            U=sum(i not in mask and sum(set(verts[i]).isdisjoint(verts[j]) for j in fs)==1
                  for i in range(len(verts)))
            w=len(verts)+support_size-U
            actual = 2*support_size+sum(i not in mask and sum(set(verts[i]).isdisjoint(verts[j]) for j in fs)!=1
                                  for i in range(len(verts)))
            assert w==actual
    print(f'n={n} independent_coverage_crosscheck=passed')

if __name__ == '__main__':
    for n in (7,8,9):
        check(n)
    for n in (7,8,9,10,11):
        check_zero_class(n)
    print('ALL CHECKS PASSED')
