from itertools import combinations, product
from math import ceil


def graph(n):
    adj = [set() for _ in range(2 * n)]
    for i in range(n - 1):
        adj[i].add(i + 1)
        adj[i + 1].add(i)
    for i in range(n):
        adj[i].add(n + i)
        adj[n + i].add(i)
    return adj


def zero_forcing(n, initial):
    adj = graph(n)
    blue = set(initial)
    while True:
        forced = None
        for v in tuple(blue):
            white_neighbors = [u for u in adj[v] if u not in blue]
            if len(white_neighbors) == 1:
                forced = white_neighbors[0]
                break
        if forced is None:
            return len(blue) == 2 * n
        blue.add(forced)


def predicted_minimum_sets(n):
    out = set()
    if n % 2 == 0:
        m = n // 2
        for bits in product((0, 1), repeat=m):
            chosen = [n + (2 * j + bit) for j, bit in enumerate(bits)]
            out.add(tuple(sorted(chosen)))
        return out

    m = (n - 1) // 2
    for t in range(m + 1):
        q = 2 * t
        pairs = [(i, i + 1) for i in range(0, q, 2)]
        pairs += [(i, i + 1) for i in range(q + 1, n, 2)]
        for bits in product((0, 1), repeat=m):
            leaves = [n + pair[bit] for pair, bit in zip(pairs, bits)]
            out.add(tuple(sorted(leaves + [n + q])))
            out.add(tuple(sorted(leaves + [q])))
    return out


def main():
    subset_checks = 0
    classification_checks = 0
    count_checks = 0
    for n in range(2, 12):
        k = ceil(n / 2)
        predicted = predicted_minimum_sets(n)
        actual = set()
        for r in range(k):
            for S in combinations(range(2 * n), r):
                subset_checks += 1
                if zero_forcing(n, S):
                    raise AssertionError((n, 'unexpected smaller zero forcing set', S))
        for S in combinations(range(2 * n), k):
            subset_checks += 1
            if zero_forcing(n, S):
                actual.add(tuple(S))
        classification_checks += len(predicted)
        if actual != predicted:
            raise AssertionError((n, len(actual), len(predicted), sorted(actual ^ predicted)[:10]))
        if n % 2 == 0:
            m = n // 2
            expected = 2 ** m
        else:
            m = (n - 1) // 2
            expected = (3 * m + 4) * 2 ** (m - 1)
        count_checks += 1
        if len(actual) != expected:
            raise AssertionError((n, len(actual), expected))
    print(
        'VERIFY_OK n_range=2..11 '
        f'subset_checks={subset_checks} '
        f'classification_checks={classification_checks} '
        f'count_checks={count_checks} max_order=22'
    )


if __name__ == '__main__':
    main()
