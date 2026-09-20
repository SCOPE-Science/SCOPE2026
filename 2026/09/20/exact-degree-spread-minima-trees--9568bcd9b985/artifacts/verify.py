#!/usr/bin/env python3
from math import ceil, floor

def partitions(n, max_part=None):
    if n == 0:
        yield []
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n - first, first):
            yield [first] + rest

def spread(degrees, k):
    counts = {}
    for d in degrees:
        counts[d] = counts.get(d, 0) + 1
    md = max(degrees)
    return max(
        sum(counts.get(j, 0) for j in range(a, a + k + 1))
        for a in range(0, md + 1)
    )

def predicted(n, k):
    if k == 0:
        return ceil((n + 2) / 3)
    return n - floor((n - 2) / (k + 1))

def witness_degrees(n, k):
    if k == 0:
        q, r = divmod(n, 3)
        if r == 0:
            return [1] * (q + 1) + [2] * q + [3] * (q - 1)
        if r == 1:
            return [1] * (q + 1) + [2] * (q + 1) + [3] * (q - 1)
        return [1] * (q + 2) + [2] * q + [3] * q

    q, r = divmod(n - 2, k + 1)
    degrees = [k + 2] * q
    if r:
        degrees.append(r + 1)
    degrees.extend([1] * (n - len(degrees)))
    return degrees

def check_tree_degree_sequence(degrees):
    n = len(degrees)
    return all(d >= 1 for d in degrees) and sum(degrees) == 2 * n - 2

def main():
    checked_multisets = 0
    checked_pairs = 0

    for n in range(2, 41):
        ks = range(0, min(12, n + 3) + 1)
        minima = {k: n + 1 for k in ks}

        # A tree degree multiset is equivalent to a partition of n-2
        # into the positive excesses d_i-1, padded by zeros.
        for p in partitions(n - 2):
            degrees = [x + 1 for x in p] + [1] * (n - len(p))
            assert check_tree_degree_sequence(degrees)
            for k in ks:
                minima[k] = min(minima[k], spread(degrees, k))
                checked_pairs += 1
            checked_multisets += 1

        for k in ks:
            assert minima[k] == predicted(n, k), (n, k, minima[k], predicted(n, k))
            w = witness_degrees(n, k)
            assert len(w) == n
            assert check_tree_degree_sequence(w)
            assert spread(w, k) == predicted(n, k), (n, k, w)

    print("PASS")
    print("orders: 2..40")
    print("window parameters: 0..min(12,n+3)")
    print("tree degree multisets checked:", checked_multisets)
    print("multiset/window checks:", checked_pairs)

if __name__ == "__main__":
    main()
