#!/usr/bin/env python3
"""Exhaustive finite checks for the injectively timed path formula."""
from itertools import permutations, combinations


def simulates_zero_forcing(times, seed_mask):
    """Return whether the seed mask corrupts every path vertex."""
    m = len(times)
    n = m + 1
    blue = [bool(seed_mask & (1 << i)) for i in range(n)]
    edge_at = [None] * (m + 1)
    for edge, t in enumerate(times):
        edge_at[t] = edge
    for t in range(1, m + 1):
        edge = edge_at[t]
        left, right = edge, edge + 1
        if blue[left] and not blue[right]:
            blue[right] = True
        elif blue[right] and not blue[left]:
            blue[left] = True
    return all(blue)


def brute_tz(times):
    n = len(times) + 1
    tested = 0
    for size in range(1, n + 1):
        for seed_tuple in combinations(range(n), size):
            mask = sum(1 << v for v in seed_tuple)
            tested += 1
            if simulates_zero_forcing(times, mask):
                return size, seed_tuple, tested
    raise AssertionError("no forcing set")


def peak_chains(times):
    # Edge positions are represented internally by zero-based indices.
    peaks = [i for i in range(1, len(times)-1)
             if times[i-1] < times[i] > times[i+1]]
    chains = []
    if peaks:
        cur = [peaks[0]]
        for p in peaks[1:]:
            if p - cur[-1] == 2:
                cur.append(p)
            else:
                chains.append(cur)
                cur = [p]
        chains.append(cur)
    return peaks, chains


def formula_tz(times):
    _, chains = peak_chains(times)
    return 1 + sum((len(c) + 1) // 2 for c in chains)


def direct_cut_number(times):
    m = len(times)
    peaks, _ = peak_chains(times)
    for k in range(m + 1):
        for cuts in combinations(range(m), k):
            C = set(cuts)
            if all(any(c in C for c in (p-1, p, p+1)) for p in peaks):
                return k
    raise AssertionError("no cut set")


def witness_permutation(m):
    # Blocks (1,3,2),(4,6,5),... create isolated peak neighborhoods.
    out = []
    a = 1
    while a + 2 <= m:
        out.extend([a, a+2, a+1])
        a += 3
    out.extend(range(a, m+1))
    return tuple(out)


def main():
    total_permutations = 0
    total_seed_sets_tested = 0
    maxima = []
    for m in range(1, 9):
        local_max = 0
        for times in permutations(range(1, m+1)):
            brute, _, tested = brute_tz(times)
            formula = formula_tz(times)
            cuts = direct_cut_number(times)
            assert brute == formula == cuts + 1, (times, brute, formula, cuts)
            total_seed_sets_tested += tested
            total_permutations += 1
            local_max = max(local_max, formula)
        n = m + 1
        predicted_max = (n + 2) // 3
        assert local_max == predicted_max, (n, local_max, predicted_max)
        w = witness_permutation(m)
        assert sorted(w) == list(range(1, m+1))
        assert formula_tz(w) == predicted_max
        maxima.append((n, local_max, w))
    print("ALL CHECKS PASSED")
    print(f"permutations={total_permutations}")
    print(f"seed_sets_tested={total_seed_sets_tested}")
    print("maxima=" + ";".join(f"n={n}:TZ={z}:witness={','.join(map(str,w))}" for n,z,w in maxima))


if __name__ == "__main__":
    main()
