#!/usr/bin/env python3
from itertools import product
from math import comb


def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def multipartite_part_index(parts):
    idx = []
    for i, size in enumerate(parts):
        idx.extend([i] * size)
    return idx


def majority_ok(colors, part_index):
    n = len(colors)
    for v in range(n):
        deg = 0
        same = 0
        pv = part_index[v]
        cv = colors[v]
        for u in range(n):
            if u != v and part_index[u] != pv:
                deg += 1
                if colors[u] == cv:
                    same += 1
        if 2 * same < deg:
            return False
    return True


def rgs_partitions(n):
    # Each yielded tuple is a canonical surjective coloring of the vertices:
    # color labels appear in first-occurrence order.
    if n == 0:
        yield ()
        return
    a = [0] * n
    def rec(pos, max_seen):
        if pos == n:
            yield tuple(a)
            return
        for c in range(max_seen + 2):
            a[pos] = c
            yield from rec(pos + 1, max(max_seen, c))
    a[0] = 0
    yield from rec(1, 0)


def predicted_chi(parts):
    return 2 if all(s % 2 == 0 for s in parts) else 1


def predicted_labeled_two_count(parts):
    if not all(s % 2 == 0 for s in parts):
        return 0
    out = 1
    for s in parts:
        out *= comb(s, s // 2)
    return out


def main():
    graph_types = 0
    canonical_colorings = 0
    valid_canonical_colorings = 0
    labeled_two_assignments = 0
    valid_labeled_two_assignments = 0
    optimal_two_types = 0
    max_order = 8

    rgs_cache = {n: list(rgs_partitions(n)) for n in range(2, max_order + 1)}

    for n in range(2, max_order + 1):
        for parts in integer_partitions(n):
            if len(parts) < 2:
                continue
            graph_types += 1
            pidx = multipartite_part_index(parts)

            best = 0
            for colors in rgs_cache[n]:
                canonical_colorings += 1
                if majority_ok(colors, pidx):
                    valid_canonical_colorings += 1
                    best = max(best, max(colors) + 1)
            want = predicted_chi(parts)
            if best != want:
                raise AssertionError((parts, 'chromatic number', best, want))

            actual_two = 0
            for colors in product((0, 1), repeat=n):
                if 0 not in colors or 1 not in colors:
                    continue
                labeled_two_assignments += 1
                if majority_ok(colors, pidx):
                    valid_labeled_two_assignments += 1
                    actual_two += 1
                    # The theorem asserts exact half-splitting in every part.
                    start = 0
                    for s in parts:
                        block = colors[start:start+s]
                        if sum(block) * 2 != s:
                            raise AssertionError((parts, colors, 'unbalanced valid two-coloring'))
                        start += s
            want_two = predicted_labeled_two_count(parts)
            if actual_two != want_two:
                raise AssertionError((parts, 'labeled two-colorings', actual_two, want_two))
            if want == 2:
                optimal_two_types += 1

    print(
        'ALL CHECKS PASSED; '
        f'multipartite_types={graph_types}; '
        f'canonical_colorings={canonical_colorings}; '
        f'valid_canonical_colorings={valid_canonical_colorings}; '
        f'labeled_two_assignments={labeled_two_assignments}; '
        f'valid_labeled_two_assignments={valid_labeled_two_assignments}; '
        f'chi_two_types={optimal_two_types}; '
        f'max_order={max_order}'
    )


if __name__ == '__main__':
    main()
