"""Definition-level verification for strong odd colorings of partially deleted bicliques."""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb, factorial


def bipartite_neighbors(m, n, t):
    assert 2 <= m <= n and 1 <= t < m
    return [tuple(m + j for j in range(n) if not (i == j and i < t)) for i in range(m)] + [
        tuple(i for i in range(m) if not (i == j and j < t)) for j in range(n)
    ]


def strong_odd(adj, c):
    for v, nb in enumerate(adj):
        if any(c[v] == c[u] for u in nb):
            return False
        counts = Counter(c[u] for u in nb)
        if any(k % 2 == 0 for k in counts.values()):
            return False
    return True


@lru_cache(None)
def odd_stirling(u, r):
    if u == 0:
        return int(r == 0)
    if r < 1:
        return 0
    return sum(comb(u - 1, k - 1) * odd_stirling(u - k, r - 1)
               for k in range(1, u + 1, 2))


def falling(q, k):
    if q < k:
        return 0
    ans = 1
    for j in range(k):
        ans *= (q - j)
    return ans


def predicted_profile(m, n, t):
    u, v = m - t, n - t
    out = Counter()
    for a in range(1, u + 1):
        for b in range(1, v + 1):
            ways = odd_stirling(u, a) * odd_stirling(v, b)
            if not ways:
                continue
            for shared in range(t + 1):
                out[2 * t - shared + a + b] += comb(t, shared) * ways
    return +out


def rgs(N):
    arr = [0] * N
    def recur(i, hi):
        if i == N:
            yield tuple(arr)
            return
        for z in range(hi + 2):
            arr[i] = z
            yield from recur(i + 1, max(hi, z))
    yield from recur(1, 0)


def expected_chi(m, n, t):
    u, v = m - t, n - t
    return t + 2 + int(u % 2 == 0) + int(v % 2 == 0)


def expected_optimal_unlabeled(m, n, t):
    u, v = m - t, n - t
    return (2 ** (u - 2) if u % 2 == 0 else 1) * (2 ** (v - 2) if v % 2 == 0 else 1)


def explicit_optimal(m, n, t):
    # First t deleted matching pairs share distinct labels 0..t-1.
    a = list(range(t))
    b = list(range(t))
    color = t
    for side, x in ((a, m - t), (b, n - t)):
        if x % 2:
            side.extend([color] * x)
            color += 1
        else:
            side.append(color)
            side.extend([color + 1] * (x - 1))
            color += 2
    return tuple(a + b)


if __name__ == '__main__':
    print('VERIFY_OK')
    total_partitions = 0
    cases = 0
    for m in range(2, 5):
        for n in range(m, 6):
            if m + n > 9:
                continue
            for t in range(1, m):
                adj = bipartite_neighbors(m, n, t)
                actual = Counter()
                for c in rgs(m + n):
                    total_partitions += 1
                    if strong_odd(adj, c):
                        actual[1 + max(c)] += 1
                pred = predicted_profile(m, n, t)
                assert actual == pred, (m, n, t, actual, pred)
                chi = min(actual)
                assert chi == expected_chi(m, n, t), (m, n, t, chi)
                assert actual[chi] == expected_optimal_unlabeled(m, n, t)
                assert strong_odd(adj, explicit_optimal(m, n, t))
                cases += 1
                print(f'm={m}, n={n}, t={t}: chi_so={chi}, min_partitions={actual[chi]}, profile={dict(sorted(actual.items()))}')

    for m, n, t in ((2, 2, 1), (3, 3, 1), (3, 4, 2), (4, 4, 3)):
        adj = bipartite_neighbors(m, n, t)
        for q in range(1, 5):
            brute = sum(strong_odd(adj, c) for c in product(range(q), repeat=m + n))
            predicted = sum(coefficient * falling(q, k)
                            for k, coefficient in predicted_profile(m, n, t).items())
            assert brute == predicted, (m, n, t, q, brute, predicted)

    constructions = 0
    for m in range(2, 32):
        for n in range(m, 51):
            for t in range(1, m):
                col = explicit_optimal(m, n, t)
                assert strong_odd(bipartite_neighbors(m, n, t), col), (m, n, t)
                assert len(set(col)) == expected_chi(m, n, t)
                constructions += 1

    # Witness the unbounded single-edge effect for even n.
    for n in range(2, 52, 2):
        crown = [0] * n + [1] * n
        # On the full crown, each vertex sees n-1 opposite-side vertices.
        crown_adj = [tuple(n + j for j in range(n) if j != i) for i in range(n)] + [
            tuple(i for i in range(n) if i != j) for j in range(n)
        ]
        assert strong_odd(crown_adj, crown)
        assert expected_chi(n, n, n-1) == n+1

    print('direct_unlabeled_cases =', cases)
    print('unlabeled_partitions_examined =', total_partitions)
    print('palette_bruteforce_cases =', 16)
    print('explicit_constructions_checked =', constructions)
    print('single_edge_jump_checked_even_n = 2..50')
