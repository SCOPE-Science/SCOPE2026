"""Exact checks for capacity-one Nash-subgraph enumeration on paths and cycles.

No third-party packages are required. Run with: python verify_capacity_cycle.py
"""
from collections import Counter
from math import comb, sqrt


def predicted(n, cycle):
    """Counts indexed by the number of provider vertices."""
    ans = Counter()
    for k in range((n + 1) // 2, 2 * n // 3 + 1):
        dimers = 2 * n - 3 * k
        trimers = 2 * k - n
        if dimers < 0 or trimers < 0:
            continue
        x = comb(n - k, trimers) * 2**dimers
        if cycle:
            assert (n * x) % (n - k) == 0
            x = n * x // (n - k)
        ans[k] = x
    return ans


def exhaustive(n, cycle):
    """Enumerate all bipartitions and selected edges independently of tilings."""
    edges = [(i, i + 1) for i in range(n - 1)]
    if cycle:
        edges.append((n - 1, 0))
    ans = Counter()
    for assignment in range(1 << n):
        k = assignment.bit_count()
        if k == 0 or k == n:
            continue
        allowed = [uv for uv in edges if ((assignment >> uv[0]) & 1) != ((assignment >> uv[1]) & 1)]
        for mask in range(1 << len(allowed)):
            degree = [0] * n
            for e, (u, v) in enumerate(allowed):
                if mask >> e & 1:
                    degree[u] += 1
                    degree[v] += 1
            if all(degree[v] == 1 if (assignment >> v & 1) else degree[v] >= 1
                   for v in range(n)):
                ans[k] += 1
    return ans


def recurrence_polys(max_n):
    """Independent recurrence from oriented 2-blocks and centered 3-blocks."""
    pol = [Counter({0: 1}), Counter(), Counter({1: 2})]
    for n in range(3, max_n + 1):
        curr = Counter()
        for k, a in pol[n - 2].items():
            curr[k + 1] += 2 * a
        for k, a in pol[n - 3].items():
            curr[k + 2] += a
        pol.append(curr)
    return pol


def main():
    total_checks = 0
    for cycle in (False, True):
        for n in range(3, 10):
            direct = exhaustive(n, cycle)
            exact = predicted(n, cycle)
            assert direct == exact, (cycle, n, direct, exact)
            total_checks += 1
    paths = recurrence_polys(32)
    for n in range(3, 33):
        assert paths[n] == predicted(n, False)
        total_checks += 1
    a = {0: 3, 1: 0, 2: 4, 3: 3}
    for n in range(4, 33):
        a[n] = 2*a[n-2] + a[n-3]
        assert sum(predicted(n, True).values()) == a[n]
        total_checks += 1
    # The exact limiting provider density and variance are distinguished from finite-n results.
    mu = 1 - 1/sqrt(5)
    sigma2 = 1 - 11/(5*sqrt(5))
    assert 0.5 < mu < 2/3 and sigma2 > 0
    for n in (20, 40, 80, 160):
        # Build coefficient counts using the integer formula; test only asymptotic convergence.
        coeff = predicted(n, True)
        total = sum(coeff.values())
        mean = sum(k*v for k, v in coeff.items()) / total
        variance = sum((k-mean)**2*v for k, v in coeff.items()) / total
        assert abs(mean/n - mu) < (1e-3 if n == 20 else 1e-6)
        assert abs(variance/n - sigma2) < (1e-3 if n == 20 else 1e-6)
        total_checks += 1
    print('VERIFIED:', total_checks, 'independent exact/asymptotic checks')
    print('C8:', dict(predicted(8, True)), 'P8:', dict(predicted(8, False)))
    print('C12:', dict(predicted(12, True)))
    print('asymptotic provider density:', format(mu,'.12f'))
    print('asymptotic variance coefficient:', format(sigma2,'.12f'))


if __name__ == '__main__':
    main()
