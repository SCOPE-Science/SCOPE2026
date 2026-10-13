from itertools import permutations, combinations
from collections import Counter
from math import factorial


def derangements(n):
    for p in permutations(range(n)):
        if all(p[i] != i for i in range(n)):
            yield p


def cycle_count(p):
    seen = [False] * len(p)
    c = 0
    for i in range(len(p)):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return c


def af_formula(p):
    n = len(p)
    return n * (n - 3) // 2 + cycle_count(p)


def af_by_topological_orders(p):
    n = len(p)
    inv = [0] * n
    for i, j in enumerate(p):
        inv[j] = i
    # After orienting nonmatching crown edges and contracting M_p,
    # arc i -> k exists exactly when i != k and k != p^{-1}(i).
    total = n * (n - 2)
    best_acyclic = 0
    for order in permutations(range(n)):
        pos = [0] * n
        for r, v in enumerate(order):
            pos[v] = r
        forward = 0
        for i in range(n):
            for k in range(n):
                if i != k and k != inv[i] and pos[i] < pos[k]:
                    forward += 1
        best_acyclic = max(best_acyclic, forward)
    return total - best_acyclic


def direct_af(p):
    """Directly delete nonmatching edges until M_p is the unique perfect matching.
    Used only through n=5 as an independent finite stress test."""
    n = len(p)
    matching = {(i, p[i]) for i in range(n)}
    candidates = [(i, j) for i in range(n) for j in range(n)
                  if i != j and (i, j) not in matching]
    other_matchings = []
    for q in derangements(n):
        if q == p:
            continue
        # Only edges outside M_p can be deleted.
        witness_edges = {(i, q[i]) for i in range(n)} - matching
        other_matchings.append(witness_edges)
    for r in range(len(candidates) + 1):
        for comb in combinations(candidates, r):
            S = set(comb)
            if all(S & W for W in other_matchings):
                return r
    raise AssertionError("no anti-forcing set found")


def recurrence_polys(N):
    # Counter exponent -> coefficient for D_n(t)=sum derangements t^{cycles}.
    D = [Counter() for _ in range(N + 1)]
    D[0][0] = 1
    if N >= 1:
        D[1] = Counter()
    for n in range(2, N + 1):
        c = Counter()
        for k, v in D[n-1].items():
            c[k] += (n - 1) * v
        for k, v in D[n-2].items():
            c[k+1] += (n - 1) * v
        D[n] = c
    return D


def main():
    order_checks = 0
    direct_checks = 0
    distribution_checks = 0
    spectrum_checks = 0
    extremal_checks = 0

    # Exact FAS/topological-order verification for every perfect matching through n=6.
    for n in range(3, 7):
        for p in derangements(n):
            got = af_by_topological_orders(p)
            want = af_formula(p)
            assert got == want, (n, p, got, want)
            order_checks += 1

    # Direct uniqueness-after-deletion verification through n=5.
    for n in range(3, 6):
        for p in derangements(n):
            got = direct_af(p)
            want = af_formula(p)
            assert got == want, ("direct", n, p, got, want)
            direct_checks += 1

    # Distribution/recurrence and spectrum/extrema through n=9.
    D = recurrence_polys(9)
    for n in range(3, 10):
        brute = Counter(cycle_count(p) for p in derangements(n))
        assert brute == D[n], ("recurrence", n, brute, D[n])
        distribution_checks += 1

        support = sorted(brute)
        assert support == list(range(1, n // 2 + 1)), ("spectrum", n, support)
        spectrum_checks += 1

        assert brute[1] == factorial(n - 1), ("min-count", n, brute[1])
        m = n // 2
        if n % 2 == 0:
            expected_max_count = factorial(n) // (2**m * factorial(m))
        else:
            expected_max_count = factorial(n) // (3 * 2**(m-1) * factorial(m-1))
        assert brute[m] == expected_max_count, ("max-count", n, brute[m], expected_max_count)
        extremal_checks += 2

    print(
        "VERIFY_OK "
        f"order_checks={order_checks} direct_checks={direct_checks} "
        f"distribution_checks={distribution_checks} spectrum_checks={spectrum_checks} "
        f"extremal_checks={extremal_checks} max_order=18"
    )


if __name__ == "__main__":
    main()
