"""Exhaustive finite checks of optimal two-rainbow labels on middle graphs.

Usage: python verify.py
Only Python's standard library is required.
"""
from itertools import combinations


def middle_neighborhoods(n, edges):
    edges = tuple(tuple(sorted(e)) for e in edges)
    L = n + len(edges)
    nbr = [set() for _ in range(L)]
    for j, (u, v) in enumerate(edges):
        k = n + j
        nbr[u].add(k)
        nbr[v].add(k)
        nbr[k].update((u, v))
    for i in range(len(edges)):
        for j in range(i):
            if set(edges[i]) & set(edges[j]):
                nbr[n + i].add(n + j)
                nbr[n + j].add(n + i)
    return tuple(tuple(sorted(s)) for s in nbr)


def direct_count(n, edges):
    nbr = middle_neighborhoods(n, edges)
    slots = 2 * len(nbr)
    found = 0
    total_attempts = 0
    for w in range(n + 1):
        for selected_bits in combinations(range(slots), w):
            total_attempts += 1
            masks = [0] * len(nbr)
            for b in selected_bits:
                masks[b // 2] |= 1 << (b % 2)
            if all(x or (lambda q: q == 3)(sum_or(masks[k] for k in nbr[i]))
                   for i, x in enumerate(masks)):
                assert w == n, ('unexpected lighter function', n, edges, w)
                found += 1
    return found, total_attempts


def sum_or(values):
    y = 0
    for v in values:
        y |= v
    return y


def cycles(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    found = set()
    for start in range(n):
        def visit(path):
            last = path[-1]
            for nxt in adj[last]:
                if nxt == start and len(path) >= 4 and len(path) % 2 == 0:
                    p = tuple(path)
                    r = tuple([p[0]] + list(reversed(p[1:])))
                    found.add(min(p, r))
                elif nxt > start and nxt not in path and len(path) < n:
                    visit(path + [nxt])
        visit([start])
    return tuple(found)


def proper_two_colorings(n, edges, free):
    free = set(free)
    adj = {v: set() for v in free}
    for u, v in edges:
        if u in free and v in free:
            adj[u].add(v)
            adj[v].add(u)
    painted = {}
    c = 0
    for start in free:
        if start in painted:
            continue
        c += 1
        painted[start] = 0
        queue = [start]
        for v in queue:
            for w in adj[v]:
                if w not in painted:
                    painted[w] = 1 - painted[v]
                    queue.append(w)
                elif painted[w] == painted[v]:
                    return 0
    return 2 ** c


def predicted_count(n, edges):
    edges = tuple(tuple(sorted(e)) for e in edges)
    m = len(edges)
    all_cycles = cycles(n, edges)
    cycle_sets = []
    for k in range(len(all_cycles) + 1):
        for selected in combinations(all_cycles, k):
            vertices = [v for c in selected for v in c]
            if len(set(vertices)) == len(vertices):
                cycle_sets.append((set(vertices), 2 ** k))
    total = 0
    for cycle_vertices, cycle_orientations in cycle_sets:
        candidates = [(u, v) for u, v in edges
                      if u not in cycle_vertices and v not in cycle_vertices]
        for mask in range(1 << len(candidates)):
            selected = [e for i, e in enumerate(candidates) if mask & (1 << i)]
            ends = [x for e in selected for x in e]
            if len(ends) != len(set(ends)):
                continue
            uncovered = set(range(n)) - cycle_vertices - set(ends)
            total += cycle_orientations * proper_two_colorings(n, edges, uncovered)
    return total


def run():
    cases = []
    # Every labeled simple graph on up to four vertices, plus larger test families.
    for n in range(1, 5):
        possible = tuple(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            cases.append((n, tuple(e for i, e in enumerate(possible) if mask & (1 << i))))
    cases += [
        (5, ((i, i + 1) for i in range(4))),
        (5, ((0, i) for i in range(1, 5))),
        (5, ((i, (i + 1) % 5) for i in range(5))),
        (5, ((0, 1), (0, 2), (0, 3), (3, 4))),
        (5, ((0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4))),
        (5, tuple(combinations(range(5), 2))),
        (6, ((i, i + 1) for i in range(5))),
        (6, ((i, (i + 1) % 6) for i in range(6))),
        (6, ((0, i) for i in range(1, 6))),
        (6, ((0, 1), (0, 2), (0, 3), (3, 4), (4, 5))),
        (6, ((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5))),
    ]
    attempts = 0
    max_size = 0
    for n, raw in cases:
        es = tuple(sorted(set(tuple(sorted(e)) for e in raw)))
        brute, ct = direct_count(n, es)
        predicted = predicted_count(n, es)
        assert brute == predicted, (n, es, brute, predicted)
        attempts += ct
        max_size = max(max_size, n + len(es))
    # The path corollary is checked a second way, without enumerating color labels.
    path = [1, 2, 3]
    for n in range(3, 32):
        path.append(sum(path[-3:]))
        if n <= 6:
            value = predicted_count(n, tuple((i, i + 1) for i in range(n - 1)))
            assert value == path[n]
    for n in range(1, 12):
        es = tuple((0, i) for i in range(1, n))
        expected = 2 if n == 1 else 2 + (n - 1) * 2 ** (n - 2)
        assert predicted_count(n, es) == expected
    print('VERIFICATION_OK cases=%d weighted_assignments=%d max_middle_vertices=%d' %
          (len(cases), attempts, max_size))
    print('PATH_COUNTS n=1..12: ' + ','.join(map(str, path[1:13])))
    print('K4_EXACT=%d C4_EXACT=%d C5_EXACT=%d' %
          (predicted_count(4, tuple(combinations(range(4), 2))),
           predicted_count(4, tuple((i, (i + 1) % 4) for i in range(4))),
           predicted_count(5, tuple((i, (i + 1) % 5) for i in range(5)))))


if __name__ == '__main__':
    run()
