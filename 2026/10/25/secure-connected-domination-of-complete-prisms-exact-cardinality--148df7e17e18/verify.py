"""Exhaustive graph-definition checks for secure connected domination of complete prisms.

Run: python verify.py
No packages outside the Python standard library are required.
"""
from collections import Counter
from math import comb


def adjacency(n):
    return [{v for v in range(2*n) if v != u
             and (v // n == u // n or abs(v-u) == n)}
            for u in range(2*n)]


def connected_dominating(n, selected, adj):
    if not selected:
        return False
    if any(not (adj[v] & selected) for v in range(2*n) if v not in selected):
        return False
    frontier = [next(iter(selected))]
    seen = set(frontier)
    for v in frontier:
        for w in adj[v] & selected:
            if w not in seen:
                seen.add(w)
                frontier.append(w)
    return seen == selected


def secure_connected(n, selected, adj):
    if not connected_dominating(n, selected, adj):
        return False
    for u in range(2*n):
        if u in selected:
            continue
        if not any(connected_dominating(n, (selected - {v}) | {u}, adj)
                   for v in selected & adj[u]):
            return False
    return True


def structural_characterization(n, selected):
    a = {i for i in selected if i < n}
    b = {i-n for i in selected if i >= n}
    return bool(a & b) and (
        (len(a) >= 2 and len(b) >= 2)
        or (len(a) == 1 and len(b) == n)
        or (len(b) == 1 and len(a) == n))


def theoretical_coefficients(n):
    # Pairs of a- and b-element index sets with at least one common index.
    result = Counter()
    for a in range(2, n+1):
        for b in range(2, n+1):
            disjoint = comb(n-a, b) if b <= n-a else 0
            result[a+b] += comb(n, a) * (comb(n, b) - disjoint)
    result[n+1] += 2*n
    return +result


def theoretical_minimal(n):
    result = Counter({4: comb(n, 2)*(2*n-3)})
    result[n+1] += 2*n
    return +result


def run():
    total = 0
    for n in range(3, 9):
        adj = adjacency(n)
        actual = Counter()
        minimal = Counter()
        all_good_masks = set()
        selections = {}
        for mask in range(1 << (2*n)):
            selected = {v for v in range(2*n) if mask & (1 << v)}
            selections[mask] = selected
            outcome = secure_connected(n, selected, adj)
            assert outcome == structural_characterization(n, selected), (
                "classification", n, mask)
            if outcome:
                actual[len(selected)] += 1
                all_good_masks.add(mask)
        for mask in all_good_masks:
            selected = selections[mask]
            if all(mask ^ (1 << v) not in all_good_masks for v in selected):
                minimal[len(selected)] += 1
        assert actual == theoretical_coefficients(n), (
            "polynomial", n, actual, theoretical_coefficients(n))
        assert minimal == theoretical_minimal(n), (
            "minimal polynomial", n, minimal, theoretical_minimal(n))
        total += (1 << (2*n))
        print("n=%d subsets=%d admissible=%d minimal=%s" %
              (n, 1 << (2*n), sum(actual.values()), dict(sorted(minimal.items()))))
    print("SUCCESS: %d vertex subsets, n=3,...,8" % total)


if __name__ == "__main__":
    run()
