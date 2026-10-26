"""Exact small-instance checks for the capacity-constrained best-shot game.

Uses only the Python standard library. The exhaustive check is limited to n <= 5;
it is a consistency check for the exact count, not a proof of the asymptotic theorem.
"""
from itertools import combinations, product
from math import comb


def cover_count(m: int, q: int, k: int) -> int:
    """Count ordered lists of m k-subsets of a q-set whose union is the q-set."""
    if m == 0:
        return int(q == 0)
    if q == 0:
        return 1
    return sum((-1) ** j * comb(q, j) * comb(q - j, k) ** m
               for j in range(q + 1))


def formula_counts(n: int, k: int) -> dict[int, int]:
    """Number of labelled pure-equilibrium profiles, indexed by nonbuyer count q."""
    counts = {}
    for q in range(k, (k * n) // (k + 1) + 1):
        m = n - q
        a = cover_count(m, q, k)
        if a:
            counts[q] = comb(n, q) * a
    return counts


def brute_counts(n: int, k: int) -> dict[int, int]:
    """Enumerate all pure strategy profiles and test the best-response conditions."""
    vertices = tuple(range(n))
    actions = []
    for i in vertices:
        out_neighbors = tuple(j for j in vertices if j != i)
        actions.append([None] + [tuple(s) for s in combinations(out_neighbors, k)])

    counts = {}
    for profile in product(*actions):
        buyers = {i for i, action in enumerate(profile) if action is not None}
        nominated = set()
        for action in profile:
            if action is not None:
                nominated.update(action)
        # A buyer cannot be nominated, and every nonbuyer must be nominated.
        if buyers & nominated:
            continue
        if (set(vertices) - buyers) - nominated:
            continue
        q = n - len(buyers)
        counts[q] = counts.get(q, 0) + 1
    return counts


def main() -> None:
    comparisons = 0
    for n in range(2, 6):
        for k in range(1, n):
            exact = formula_counts(n, k)
            brute = brute_counts(n, k)
            assert exact == brute, (n, k, exact, brute)
            comparisons += 1
    print(f"PASS: formula matches direct enumeration in {comparisons} cases (2 <= n <= 5).")


if __name__ == "__main__":
    main()
