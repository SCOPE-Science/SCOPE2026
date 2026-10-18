"""Exact finite checks for partial-feedback directional localization on crown graphs.

Run with Python 3.10+; no external packages required. This program checks
finite examples, not the general mathematical proof.
"""
from collections import defaultdict
from itertools import combinations, product


def graph(n):
    adj = [set() for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n + j)
                adj[n + j].add(i)
    return adj


def shortest_distances(adj):
    result = []
    for p in range(len(adj)):
        d = [None] * len(adj)
        d[p] = 0
        queue = [p]
        for v in queue:
            for w in adj[v]:
                if d[w] is None:
                    d[w] = d[v] + 1
                    queue.append(w)
        assert all(x is not None for x in d)
        result.append(d)
    return result


def response_options(adj, d, p, robber):
    if p == robber:
        return (p,)
    return tuple(x for x in sorted(adj[p]) if d[x][robber] + 1 == d[p][robber])


def exact_win(n, cops):
    """Solve finite perfect-information belief-state reachability game."""
    adj = graph(n)
    N = 2 * n
    d = shortest_distances(adj)
    full = (1 << N) - 1
    response = [[response_options(adj, d, p, v) for v in range(N)]
                for p in range(N)]
    closed = [sum(1 << x for x in adj[v] | {v}) for v in range(N)]
    expand = [0] * (full + 1)
    for mask in range(1, full + 1):
        low = mask & -mask
        expand[mask] = expand[mask ^ low] | closed[low.bit_length() - 1]
    actions = []
    for probes in combinations(range(N), cops):
        by_reply = defaultdict(int)
        for robber in range(N):
            for answers in product(*(response[p][robber] for p in probes)):
                by_reply[answers] |= 1 << robber
        actions.append(tuple(set(q for q in by_reply.values() if q.bit_count() > 1)))
    winning = {1 << v for v in range(N)}
    while True:
        added = []
        for belief in range(1, full + 1):
            if belief in winning:
                continue
            for replies in actions:
                if all((belief & q).bit_count() <= 1 or
                       expand[belief & q] in winning for q in replies):
                    added.append(belief)
                    break
        if not added:
            return full in winning
        winning.update(added)
        if full in winning:
            return True


def theoretical_strategy_checks(n):
    """Enumerate adversarial replies for the two-round upper strategy."""
    adj = graph(n)
    N = 2 * n
    d = shortest_distances(adj)
    missing = n - 1
    first = tuple(i for i in range(n) if i != missing)
    reply_groups = defaultdict(set)
    for robber in range(N):
        for answers in product(*(response_options(adj, d, p, robber)
                                 for p in first)):
            reply_groups[answers].add(robber)
    for candidates in reply_groups.values():
        if len(candidates) == 1:
            continue
        assert len(candidates) == 2
        assert missing in candidates
        other = next(v for v in candidates if v != missing)
        assert n <= other < 2 * n and other != n + missing
        eliminated_a = other - n
        eliminated_b = missing
        remaining = set(range(N)) - {eliminated_a, n + eliminated_b}
        second = tuple(i for i in range(n) if i != eliminated_a)
        second_groups = defaultdict(set)
        for robber in remaining:
            for answers in product(*(response_options(adj, d, p, robber)
                                     for p in second)):
                second_groups[answers].add(robber)
        assert all(len(c) == 1 for c in second_groups.values())


def lower_family_checks(n):
    """Check the robust family of beliefs sustaining n-2 probes."""
    states = [(None, None)] + [(i, j) for i in range(n) for j in range(n) if i != j]
    for absent_b, absent_a in states:
        S = set(range(2 * n))
        if absent_b is not None:
            S.remove(absent_a)
            S.remove(n + absent_b)
        for used in combinations(range(n), n - 2):
            remaining = sorted(set(range(n)) - set(used))
            witnesses = [(p, q) for p in remaining for q in remaining
                         if p != q and p in S and n + q in S]
            assert witnesses
            p, q = witnesses[0]
            # Both candidates must be able to give the same shortest-path answer.
            adj = graph(n)
            d = shortest_distances(adj)
            for i in used:
                assert n + q in response_options(adj, d, i, p)
                assert n + q in response_options(adj, d, i, n + q)
                assert p in response_options(adj, d, n + i, p)
                assert p in response_options(adj, d, n + i, n + q)
            closed = {p, n + q} | adj[p] | adj[n + q]
            assert closed == set(range(2 * n)) - {q, n + p}


def main():
    for n in range(3, 7):
        assert not exact_win(n, n - 2), (n, 'lower')
        assert exact_win(n, n - 1), (n, 'upper')
        print(f'Exact belief-state game: n={n}, min cops={n-1}')
    for n in range(5, 8):
        theoretical_strategy_checks(n)
        lower_family_checks(n)
        print(f'Explicit upper policy and lower invariant: n={n} pass')
    print('All exact finite checks passed.')


if __name__ == '__main__':
    main()
