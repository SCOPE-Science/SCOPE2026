"""Definition-level verification for complete multipartite outer multiset resolving sets."""

from collections import Counter
import math


def integer_partitions(n):
    def rec(rem, lo, acc):
        if rem == 0:
            yield tuple(acc)
            return
        for x in range(lo, rem + 1):
            yield from rec(rem - x, x, acc + [x])
    yield from rec(n, 1, [])


def part_labels(parts):
    labels = []
    for i, size in enumerate(parts):
        labels.extend([i] * size)
    return labels


def distance(labels, u, v):
    if u == v:
        return 0
    return 1 if labels[u] != labels[v] else 2


def resolves_directly(parts, selected):
    labels = part_labels(parts)
    n = len(labels)
    selected = set(selected)
    seen = set()
    for u in range(n):
        if u in selected:
            continue
        rep = tuple(sorted(distance(labels, u, w) for w in selected))
        if rep in seen:
            return False
        seen.add(rep)
    return True


def resolves_by_structure(parts, selected):
    selected = set(selected)
    used_sizes = set()
    start = 0
    for size in parts:
        omitted = 0
        for v in range(start, start + size):
            omitted += v not in selected
        if omitted > 1:
            return False
        if omitted == 1:
            if size in used_sizes:
                return False
            used_sizes.add(size)
        start += size
    return True


def predicted_counts(parts):
    n = sum(parts)
    mult = Counter(parts)
    sizes = sorted(mult)
    counts = Counter()
    for mask in range(1 << len(sizes)):
        omitted = 0
        coefficient = 1
        for i, q in enumerate(sizes):
            if (mask >> i) & 1:
                omitted += 1
                coefficient *= mult[q] * q
        counts[n - omitted] += coefficient
    return counts


def brute_counts(parts):
    n = sum(parts)
    counts = Counter()
    for mask in range(1 << n):
        selected = [v for v in range(n) if (mask >> v) & 1]
        direct = resolves_directly(parts, selected)
        structural = resolves_by_structure(parts, selected)
        assert direct == structural, (parts, selected, direct, structural)
        if direct:
            counts[len(selected)] += 1
    return counts


def D(n):
    d = 0
    while (d + 1) * (d + 2) // 2 <= n:
        d += 1
    return d


def main():
    graph_types = 0
    for n in range(2, 9):
        for parts in integer_partitions(n):
            if len(parts) < 2:
                continue
            graph_types += 1
            actual = brute_counts(parts)
            predicted = predicted_counts(parts)
            assert actual == predicted, (parts, actual, predicted)

            d = len(set(parts))
            assert min(actual) == n - d
            mult = Counter(parts)
            assert actual[n - d] == math.prod(mult[q] * q for q in mult)

    for n in range(2, 21):
        actual_values = set()
        for parts in integer_partitions(n):
            if len(parts) >= 2:
                actual_values.add(n - len(set(parts)))
        expected_values = set(range(n - D(n), n))
        assert actual_values == expected_values, (n, actual_values, expected_values)

    print(f"complete multipartite graph types checked through order 8: {graph_types}")
    print("direct definition versus structural criterion: PASS")
    print("full resolving-set enumerator: PASS")
    print("outer multiset dimension n - number_of_distinct_part_sizes: PASS")
    print("fixed-order spectrum checked through order 20: PASS")


if __name__ == "__main__":
    main()
