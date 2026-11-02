"""Independent exhaustive checker for optimal sub-quorum colorings.

Run: python3 verify_subquorum.py
Uses no nonstandard packages. Graphs are specified by their multipartite part sizes.
The mathematical proof applies to all orders; these exhaustive tests are finite.
"""
from itertools import combinations
from math import factorial


def colorings(n):
    """Canonical set partitions of a subset of n positions into nonempty classes.

    Zero marks an uncolored position; positive colors are canonicalized in
    order of first appearance, so each unlabeled coloring occurs exactly once.
    """
    a = [0] * n

    def rec(i, used):
        if i == n:
            yield tuple(a), used
            return
        for c in range(used + 2):
            a[i] = c
            yield from rec(i + 1, max(used, c))

    yield from rec(0, 0)


def legitimate(a, part_of, groups):
    colored = [i for i, c in enumerate(a) if c]
    for i in colored:
        ne = [j for j in colored if part_of[j] != part_of[i]]
        same = 1 + sum(a[j] == a[i] for j in ne)
        if 2 * same < 1 + len(ne):
            return False
    return True


def structural(a, groups, M):
    c = [[a[v] for v in g if a[v]] for g in groups]
    big = [i for i, size in enumerate(map(len, groups)) if size == M]
    support_sizes = sorted((len(v) for v in c if v), reverse=True)
    if M >= 4:
        return support_sizes == [M] and any(
            len(c[i]) == M and len(set(c[i])) == M for i in big
        )
    if support_sizes == [3]:
        return any(len(c[i]) == 3 and len(set(c[i])) == 3 for i in big)
    if support_sizes == [3, 1]:
        return any(len(c[i]) == 3 and len(set(c[i])) == 3 for i in big)
    if support_sizes == [3, 3]:
        nonempty = [v for v in c if v]
        return (len(nonempty) == 2 and
                all(len(set(v)) == 3 for v in nonempty) and
                set(nonempty[0]) == set(nonempty[1]))
    return False


def profiles(total, minimum=2):
    def rec(rem, previous, prefix):
        if not rem:
            if len(prefix) >= minimum and max(prefix) >= 3:
                yield tuple(prefix)
            return
        for v in range(previous, rem + 1):
            yield from rec(rem - v, v, prefix + [v])
    yield from rec(total, 1, [])


def expected(lens):
    m = max(lens)
    p = sum(t == m for t in lens)
    if m >= 4:
        return p
    N = sum(lens)
    return p * (3 * N + 3 * p - 11)


def check(lens):
    groups = []
    cur = 0
    for x in lens:
        groups.append(tuple(range(cur, cur + x)))
        cur += x
    part_of = [-1] * cur
    for j, group in enumerate(groups):
        for v in group:
            part_of[v] = j
    M = max(lens)
    count = 0
    for a, used in colorings(cur):
        if used != M:
            continue
        if legitimate(a, part_of, groups):
            count += 1
            assert structural(a, groups, M), (lens, a, 'unclassified')
    assert count == expected(lens), (lens, count, expected(lens))
    return count


def main():
    tested = 0
    total_unlabeled = 0
    for order in range(4, 10):
        for lens in profiles(order):
            total_unlabeled += check(lens)
            tested += 1
    extra = [(3, 3, 3, 1), (4, 4, 2), (4, 3, 3), (5, 5), (5, 3, 2), (6, 3, 1)]
    for lens in extra:
        total_unlabeled += check(lens)
        tested += 1
    print('VERIFY_OK profiles={} classified_optimal_unlabeled={} smallest_part=1 maximum_order=10'.format(tested, total_unlabeled))
    for lens in [(3, 1), (3, 3), (3, 3, 3), (4, 3, 3), (4, 4, 1), (5, 5)]:
        print('EXAMPLE {} normalized={} named={}'.format(lens, expected(lens), expected(lens)*factorial(max(lens))))

if __name__ == '__main__':
    main()
