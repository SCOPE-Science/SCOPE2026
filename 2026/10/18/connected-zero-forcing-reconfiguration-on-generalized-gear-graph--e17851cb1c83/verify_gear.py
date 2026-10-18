"""Standalone exact finite checks for generalized gear zero-forcing reconfiguration.

Run: python3 verify_gear.py
Uses only the Python standard library. The proof for arbitrary parameters is in RESULT.md.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations


def graph(m, r):
    L = r + 1
    N = m * L
    nbr = [set() for _ in range(N + 1)]
    for x in range(1, N + 1):
        y = x % N + 1
        nbr[x].add(y)
        nbr[y].add(x)
    for s in range(L, N + 1, L):
        nbr[0].add(s)
        nbr[s].add(0)
    return nbr


def forces_all(nbr, initial):
    colored = set(initial)
    while True:
        to_color = set()
        for v in colored:
            white = nbr[v] - colored
            if len(white) == 1:
                to_color.update(white)
        if not to_color:
            return len(colored) == len(nbr)
        colored.update(to_color)


def predicted_sets(m, r):
    L = r + 1
    N = m * L
    wrap = lambda x: (x - 1) % N + 1
    sets = set()
    for x in range(1, N + 1):
        sets.add(tuple(sorted((0, wrap(x), wrap(x + 1)))))
    for s in range(L, N + 1, L):
        for k in range(L):
            sets.add(tuple(sorted((wrap(s + 1), wrap(s - L + k), wrap(s - L + k + 1)))))
            sets.add(tuple(sorted((wrap(s - 1), wrap(s + k), wrap(s + k + 1)))))
    return sets


def check(m, r):
    nbr = graph(m, r)
    size = len(nbr)
    assert not any(forces_all(nbr, z) for z in combinations(range(size), 2))
    actual = {z for z in combinations(range(size), 3) if forces_all(nbr, z)}
    predicted = predicted_sets(m, r)
    assert actual == predicted, (m, r, actual - predicted, predicted - actual)
    assert len(actual) == m * (3 * r + 2)

    # Independent pair-bucket construction: two triples are adjacent iff
    # they share two elements. No formula for degrees/edges is assumed.
    buckets = defaultdict(list)
    for triple in actual:
        for pair in combinations(triple, 2):
            buckets[pair].append(triple)
    adj = {t: set() for t in actual}
    for bucket in buckets.values():
        for x, y in combinations(bucket, 2):
            adj[x].add(y)
            adj[y].add(x)
    degrees = Counter(len(adj[t]) for t in actual)
    exp = ({4: 4 * m, 6: m} if r == 1 else
           {3: 2 * m, 4: 3 * (r - 1) * m, 5: 2 * m, 6: m})
    assert degrees == exp, (m, r, degrees, exp)
    assert sum(map(len, adj.values())) // 2 == m * (6 * r + 5)
    start = next(iter(actual))
    seen = {start}
    queue = deque([start])
    while queue:
        for w in adj[queue.popleft()]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    assert len(seen) == len(actual)
    # The center-containing optima are an induced rim cycle.
    H = [t for t in actual if 0 in t]
    assert len(H) == m * (r + 1)
    assert all(len(adj[t].intersection(H)) == 2 for t in H)
    assert all(any(0 in u for u in adj[t]) for t in actual if 0 not in t)
    return len(list(combinations(range(size), 3))), len(actual)


def main():
    cases = 0
    candidates = 0
    bases = 0
    for m in range(4, 9):
        for r in range(1, 7):
            num, good = check(m, r)
            candidates += num
            bases += good
            cases += 1
    print(f"VERIFICATION_OK cases={cases} tested_triples={candidates} minimum_sets={bases} parameters=m4..8_r1..6")


if __name__ == '__main__':
    main()
