"""Independent exhaustive check of locating-dominating coalition partitions.

Enumerates unlabelled vertex partitions of small complete multipartite graphs.
Graph adjacency and the locating-dominating test are implemented directly.
No theorem-specific shortcut is used in the search.
"""

from functools import lru_cache


def integer_partitions(n, low=1):
    if n == 0:
        yield ()
    else:
        for k in range(low, n + 1):
            for rest in integer_partitions(n - k, k):
                yield (k,) + rest


def set_partitions(n):
    # Restricted-growth strings enumerate unordered partitions exactly once.
    labels = [0] * n

    def rec(i, current_max):
        if i == n:
            blocks = [0] * (current_max + 1)
            for j, label in enumerate(labels):
                blocks[label] |= 1 << j
            yield tuple(blocks)
            return
        for label in range(current_max + 2):
            labels[i] = label
            yield from rec(i + 1, max(current_max, label))

    if n:
        yield from rec(1, 0)


def adjacency(part_sizes):
    n = sum(part_sizes)
    all_vertices = (1 << n) - 1
    rows = []
    offset = 0
    for size in part_sizes:
        part_mask = ((1 << size) - 1) << offset
        rows.extend([all_vertices ^ part_mask] * size)
        offset += size
    return rows


def locating_dominating_flags(rows):
    n = len(rows)
    full = (1 << n) - 1
    good = bytearray(1 << n)
    for chosen in range(1 << n):
        outside = full ^ chosen
        signatures = set()
        ok = True
        while outside:
            lowbit = outside & -outside
            outside ^= lowbit
            vertex = lowbit.bit_length() - 1
            sig = rows[vertex] & chosen
            if sig == 0 or sig in signatures:
                ok = False
                break
            signatures.add(sig)
        good[chosen] = ok
    return good


def measured_coalition_number(part_sizes):
    ld = locating_dominating_flags(adjacency(part_sizes))
    best = 0
    for parts in set_partitions(sum(part_sizes)):
        length = len(parts)
        if length <= best:
            continue
        if any(ld[mask] for mask in parts):
            continue
        if all(any(ld[mask | other] for j, other in enumerate(parts) if i != j)
               for i, mask in enumerate(parts)):
            best = length
    return best


def predicted_coalition_number(part_sizes):
    n = sum(part_sizes)
    singleton_parts = sum(size == 1 for size in part_sizes)
    if n < 3 or len(part_sizes) < 2:
        raise ValueError("Only connected complete multipartite graphs of order at least 3")
    return 4 if (n >= 4 and max(part_sizes) <= 2 and singleton_parts <= 2) else 3


def main():
    checked = 0
    for n in range(3, 10):
        for sizes in integer_partitions(n):
            if len(sizes) < 2:
                continue
            got = measured_coalition_number(sizes)
            expected = predicted_coalition_number(sizes)
            if got != expected:
                raise AssertionError((sizes, got, expected))
            checked += 1
        print(f"Order {n}: all connected multipartite part profiles checked", flush=True)

    larger = [(1, 1, 2, 2, 2, 2), (1, 1, 1, 2, 2, 2), (2, 2, 2, 2, 2),
              (1, 1, 1, 1, 2, 2), (1, 1, 1, 1, 1, 1, 2),
              (1, 2, 3, 4), (2, 2, 3, 3), (4, 6)]
    for sizes in larger:
        got = measured_coalition_number(sizes)
        expected = predicted_coalition_number(sizes)
        if got != expected:
            raise AssertionError((sizes, got, expected))
        checked += 1
        print(f"Order 10, profile {sizes}: {got}", flush=True)

    print(f"PASS: {checked} graph profiles, exhaustive partition searches", flush=True)


if __name__ == '__main__':
    main()
