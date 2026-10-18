#!/usr/bin/env python3
"""Exact character checks for four-path-free complete-multipartite complexes.

Enumerates representatives of every within-part permutation cycle type for
selected complete multipartite graphs and evaluates orientation-sensitive
simplicial Lefschetz traces. Uses Python 3 standard library only.
"""
from itertools import combinations, product


def partition_types(n, smallest=1):
    if n == 0:
        yield ()
    else:
        for x in range(smallest, n + 1):
            for y in partition_types(n - x, x):
                yield (x,) + y


def example_perm(sizes):
    full = []
    for cyc in sizes:
        arr = list(range(sum(cyc)))
        out = arr[:]
        pos = 0
        for length in cyc:
            for t in range(length):
                out[pos + t] = pos + ((t + 1) % length)
            pos += length
        full.append(tuple(out))
    return full


def face(mask, colors):
    counts = [sum(bool(mask >> j & 1) for j, color in enumerate(colors) if color == c)
              for c in range(max(colors) + 1)]
    nz = [a for a in counts if a]
    return (len(nz) == 1 or len(nz) == 2 and min(nz) == 1 or
            len(nz) == 3 and max(nz) == 1)


def test(parts):
    n = sum(parts)
    colors = sum(([i] * size for i, size in enumerate(parts)), [])
    faces = [0] + [mask for mask in range(1, 1 << n) if face(mask, colors)]
    choices = [example_perm((cycle_type,))[0] for cycle_type in []]
    by_part = [list(partition_types(size)) for size in parts]
    checked = 0
    for classes in product(*by_part):
        g = [0] * n
        start = 0
        for part_size, cycle_type in zip(parts, classes):
            pos = 0
            for length in cycle_type:
                for t in range(length):
                    g[start + pos + t] = start + pos + (t + 1) % length
                pos += length
            start += part_size
        fixed = [sum(g[j] == j for j, color in enumerate(colors) if color == i)
                 for i in range(len(parts))]
        m = len(parts)
        F = sum(fixed)
        char = (m - 1) * (1 - F)
        char += sum(fixed[i] * fixed[j] for i in range(m) for j in range(i + 1, m))
        char += sum(fixed[i] * fixed[j] * fixed[k]
                    for i in range(m) for j in range(i + 1, m)
                    for k in range(j + 1, m))
        # Direct trace on augmented simplicial chains. For each fixed face,
        # orientation sign times alternating dimension sign is (-1)^cycles.
        full_cycles = []
        unseen = set(range(n))
        while unseen:
            x = min(unseen)
            cycle = 0
            y = x
            while y in unseen:
                unseen.remove(y)
                cycle |= 1 << y
                y = g[y]
            full_cycles.append(cycle)
        score = 0
        for mask in faces:
            isfixed = all((mask & c) in (0, c) for c in full_cycles)
            if not isfixed:
                continue
            ncycle = sum((mask & c) == c for c in full_cycles)
            score += (-1) ** ncycle
        lefschetz = -score
        assert lefschetz == char, (parts, classes, lefschetz, char)
        checked += 1
    return checked


def main():
    cases = ((2, 2), (3, 3), (2, 2, 2), (3, 3, 3),
             (2, 2, 2, 2), (1, 1, 1, 1, 1), (2, 3, 3), (1, 3, 4), (4, 4))
    total = 0
    for parts in cases:
        n = test(parts)
        total += n
        print('parts', parts, 'cycle_types_checked', n)
    print('total_cycle_type_classes_checked:', total)
    print('augmented_oriented_lefschetz_character: PASS')


if __name__ == '__main__':
    main()
