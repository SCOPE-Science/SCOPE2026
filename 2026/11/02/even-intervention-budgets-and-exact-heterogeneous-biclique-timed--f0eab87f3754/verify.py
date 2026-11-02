"""Exact independent small-instance tests for timed threshold intervention on bipartite networks."""
from collections import Counter
from heapq import heappop, heappush
from itertools import combinations, combinations_with_replacement, product


def half_wave_cost(a_thresholds, b_thresholds):
    """One parity-thread optimum: graph states are (side, positive-count)."""
    a, b = len(a_thresholds), len(b_thresholds)
    f = [sum(t <= j for t in a_thresholds) for j in range(b + 1)]
    g = [sum(t <= i for t in b_thresholds) for i in range(a + 1)]
    dist = {}
    queue = []
    for u in range(a + 1):
        dist[(0, u)] = u
        heappush(queue, (u, 0, u))
    while queue:
        cost, side, count = heappop(queue)
        if cost != dist[(side, count)]:
            continue
        if (side == 0 and count == a) or (side == 1 and count == b):
            return cost
        natural = g[count] if side == 0 else f[count]
        limit = b if side == 0 else a
        other = 1 - side
        for next_count in range(natural, limit + 1):
            key = (other, next_count)
            new_cost = cost + next_count - natural
            if new_cost < dist.get(key, 10 ** 20):
                dist[key] = new_cost
                heappush(queue, (new_cost, other, next_count))
    raise AssertionError('all vertices can be directly targeted')


def independent_full_state_cost(n, edges, thresholds):
    """Exact full-state Dijkstra, without count compression or parity splitting."""
    nb = [[] for _ in range(n)]
    for u, v in edges:
        nb[u].append(v)
        nb[v].append(u)
    full = (1 << n) - 1
    dist = {0: 0}
    queue = [(0, 0)]
    while queue:
        cost, old = heappop(queue)
        if cost != dist[old]:
            continue
        if old == full:
            # The next unforced update is fully positive, hence Q_k=V.
            return cost
        natural = 0
        for i in range(n):
            if sum((old >> j) & 1 for j in nb[i]) >= thresholds[i]:
                natural |= 1 << i
        susceptible = [i for i in range(n) if not (natural >> i) & 1]
        for choice in range(1 << len(susceptible)):
            nxt = natural
            for j, i in enumerate(susceptible):
                if (choice >> j) & 1:
                    nxt |= 1 << i
            new_cost = cost + choice.bit_count()
            if new_cost < dist.get(nxt, 10 ** 20):
                dist[nxt] = new_cost
                heappush(queue, (new_cost, nxt))
    raise AssertionError('reachable by seeding all')


def test_bicliques():
    count = 0
    for a in range(1, 4):
        for b in range(1, 4):
            edges = [(u, a + v) for u in range(a) for v in range(b)]
            for A in combinations_with_replacement(range(1, b + 1), a):
                for B in combinations_with_replacement(range(1, a + 1), b):
                    got = 2 * half_wave_cost(A, B)
                    direct = independent_full_state_cost(a + b, edges, A + B)
                    assert got == direct, (A, B, got, direct)
                    count += 1
    return count


def test_all_bipartite_small():
    count = 0
    for n in range(2, 6):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            edges = [e for i, e in enumerate(all_edges) if (mask >> i) & 1]
            nbr = [set() for _ in range(n)]
            for u, v in edges:
                nbr[u].add(v)
                nbr[v].add(u)
            side = [-1] * n
            bipartite = True
            for start in range(n):
                if side[start] != -1:
                    continue
                side[start] = 0
                queue = [start]
                for u in queue:
                    for v in nbr[u]:
                        if side[v] == -1:
                            side[v] = 1 - side[u]
                            queue.append(v)
                        elif side[v] == side[u]:
                            bipartite = False
            if not bipartite:
                continue
            # Isolates have threshold zero, as required by 0 <= threshold <= degree.
            choices = [range(1, len(N) + 1) if N else (0,) for N in nbr]
            for tau in product(*choices):
                optimum = independent_full_state_cost(n, edges, tau)
                assert optimum % 2 == 0, (n, edges, tau, optimum)
                count += 1
    return count


def test_uniform_formula():
    count = 0
    for a in range(1, 11):
        for b in range(1, 11):
            for alpha in range(1, b + 1):
                for beta in range(1, a + 1):
                    expected = 2 * min(alpha, beta)
                    obtained = 2 * half_wave_cost((alpha,) * a, (beta,) * b)
                    assert obtained == expected, (a, b, alpha, beta, obtained)
                    count += 1
    return count


if __name__ == '__main__':
    a = test_bicliques()
    b = test_all_bipartite_small()
    c = test_uniform_formula()
    print('PASS: independent full-state bicliques', a)
    print('PASS: independent all small bipartite graph instances', b)
    print('PASS: uniform-threshold exact formula instances', c)
