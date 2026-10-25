"""Finite independent checker for a complete-multipartite locating-domination coalition theorem.

No external packages. Exhaustively visits set partitions of each vertex-labelled
complete multipartite graph with at most nine vertices and at least two parts.
"""
from collections import Counter
from itertools import combinations


def integer_partitions(n, max_part=None):
    if n == 0:
        yield ()
    else:
        if max_part is None:
            max_part = n
        for x in range(min(n, max_part), 0, -1):
            for tail in integer_partitions(n-x, x):
                yield (x,) + tail


def set_partitions_as_masks(n):
    labels = [0]*n
    def visit(i, highest):
        if i == n:
            groups = [0]*(highest+1)
            for v, j in enumerate(labels):
                groups[j] |= 1 << v
            yield groups
        else:
            for j in range(highest+2):
                labels[i] = j
                yield from visit(i+1, max(j, highest))
    yield from visit(1, 0)


def adjacency(ns):
    colors = [i for i, m in enumerate(ns) for _ in range(m)]
    n = len(colors)
    return [sum(1 << j for j in range(n) if colors[i] != colors[j]) for i in range(n)]


def all_ld_sets(ns):
    adj = adjacency(ns)
    n = len(adj)
    result = bytearray(1 << n)
    for mask in range(1 << n):
        seen = set()
        valid = True
        for v in range(n):
            if mask & (1 << v):
                continue
            pattern = adj[v] & mask
            if not pattern or pattern in seen:
                valid = False
                break
            seen.add(pattern)
        result[mask] = valid
    return result


def brute_coalition_number(ns):
    n = sum(ns)
    ld = all_ld_sets(ns)
    best = 0
    for blocks in set_partitions_as_masks(n):
        k = len(blocks)
        if k <= best or any(ld[b] for b in blocks):
            continue
        partners = [False]*k
        for i in range(k):
            for j in range(i):
                if ld[blocks[i] | blocks[j]]:
                    partners[i] = True
                    partners[j] = True
        if all(partners):
            best = k
    return best


def proposed_formula(ns):
    if sum(ns) == 2:
        return 0
    r = sum(x == 2 for x in ns)
    s = sum(x == 1 for x in ns)
    if max(ns) <= 2 and s <= 2 and (r >= 2 or (r == 1 and s == 2)):
        return 4
    return 3


def main():
    profiles = 0
    by_order = Counter()
    four_cases = Counter()
    for n in range(3, 10):
        for ns in integer_partitions(n):
            if len(ns) < 2:
                continue
            observed = brute_coalition_number(ns)
            predicted = proposed_formula(ns)
            if observed != predicted:
                raise AssertionError((ns, observed, predicted))
            by_order[n] += 1
            profiles += 1
            if observed == 4:
                four_cases[n] += 1
    print('VERIFY_OK')
    print('complete_multipartite_profiles_checked', profiles)
    print('by_order', dict(sorted(by_order.items())))
    print('four_cases_by_order', dict(sorted(four_cases.items())))

if __name__ == '__main__':
    main()
