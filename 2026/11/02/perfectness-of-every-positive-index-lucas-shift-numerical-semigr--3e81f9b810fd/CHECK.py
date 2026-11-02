"""Reproduce finite checks for a Lucas-shifted semigroup perfection criterion.

Requires Python standard library only. These checks are finite evidence, not the infinite proof.
"""
import heapq


def lucas_numbers(last):
    vals = [2, 1]
    for _ in range(2, last + 1):
        vals.append(vals[-1] + vals[-2])
    return vals


def ap_dijkstra(generators):
    m = generators[0]
    dist = [10**40] * m
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        value, residue = heapq.heappop(heap)
        if value != dist[residue]:
            continue
        for generator in generators:
            nr = (residue + generator) % m
            nv = value + generator
            if nv < dist[nr]:
                dist[nr] = nv
                heapq.heappush(heap, (nv, nr))
    return dist


def verify():
    lucas = lucas_numbers(20)
    coins = [1, 2] + lucas[2:]
    checked_residues = 0
    checked_gaps = 0
    for a in range(2, 18):
        m = lucas[a]
        gens = [m] + [m + coin for coin in coins[:a]]
        dist = ap_dijkstra(gens)
        # Independent unrestricted coin-count dynamic programming.
        beta = [0] + [10**10] * m
        for r in range(1, m + 1):
            beta[r] = 1 + min(beta[r-c] for c in coins[:a] if c <= r)
        for r in range(m):
            assert dist[r] == m * beta[r] + r, (a, r)
        for r in range(1, m - 1):
            assert not(beta[r] > beta[r-1] and beta[r] > beta[r+1]), (a, r)
        assert beta[m-1] <= beta[m-2]
        F = max(dist) - m
        if F >= 1:
            def member(n):
                return n >= dist[n % m]
            for g in range(1, F + 1):
                assert not(not member(g) and member(g-1) and member(g+1)), (a,g)
            checked_gaps += F
        checked_residues += m
    print('VERIFY_OK a_range=2..17 residues=' + str(checked_residues) + ' integer_positions=' + str(checked_gaps) + ' zero_isolated_gaps=16')

if __name__ == '__main__':
    verify()
