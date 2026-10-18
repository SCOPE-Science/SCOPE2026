"""Independent finite checks of zero forcing in complements of paths and cycles.

Run with Python 3.9+: python verify.py
"""
from itertools import combinations
from math import comb


def graph_complement_of_path_or_cycle(n, cycle):
    h = [set() for _ in range(n)]
    for i in range(n-1):
        h[i].add(i+1)
        h[i+1].add(i)
    if cycle:
        h[0].add(n-1)
        h[-1].add(0)
    return [set(range(n)) - h[i] - {i} for i in range(n)], h


def closure_is_all(n, adj, blue_initial):
    blue = set(blue_initial)
    while True:
        next_blue = None
        for v in sorted(blue):
            white_neighbors = adj[v] - blue
            if len(white_neighbors) == 1:
                next_blue = next(iter(white_neighbors))
                break
        if next_blue is None:
            return len(blue) == n
        blue.add(next_blue)


def expected(n, cycle):
    low = n * (n - 4) + (2 if n == 6 else 0) if cycle else n*n-6*n+10
    return {n-3:low, n-2:comb(n, 2), n-1:n, n:1}


def check(n, cycle):
    adj, h = graph_complement_of_path_or_cycle(n, cycle)
    counts = [0]*(n+1)
    predicted_triples = set()
    for white in combinations(range(n), 3):
        w = set(white)
        if any((h[v] <= w and len(h[v]) == 2) for v in range(n) if v not in w):
            predicted_triples.add(frozenset(w))
    actual_triples = set()
    for mask in range(1 << n):
        blue = [v for v in range(n) if mask & (1 << v)]
        if closure_is_all(n, adj, blue):
            counts[len(blue)] += 1
            if len(blue) == n-3:
                actual_triples.add(frozenset(set(range(n)) - set(blue)))
    expected_counts = expected(n, cycle)
    assert all(counts[k] == expected_counts.get(k, 0) for k in range(n+1)), (n, cycle, counts, expected_counts)
    assert predicted_triples == actual_triples, (n, cycle, len(predicted_triples), len(actual_triples))
    return 1 << n, len(actual_triples)


def main():
    cases = 0
    subsets = 0
    candidates = 0
    for n in range(5, 15):
        for cycle in (False, True):
            num, triple_count = check(n, cycle)
            cases += 1
            subsets += num
            candidates += triple_count
    print(f'VERIFICATION_OK graph_cases={cases} vertex_subsets={subsets} minimum_sets={candidates} n=5..14 modes=path,cycle')

if __name__ == '__main__':
    main()
