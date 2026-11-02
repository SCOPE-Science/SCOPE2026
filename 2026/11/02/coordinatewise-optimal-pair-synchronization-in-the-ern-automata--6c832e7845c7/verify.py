#!/usr/bin/env python3
"""Independent finite checks for the stated Cerny pair synchronization formula.
Run with Python 3 standard library. Infinite theorem proved separately.
"""
from collections import deque
from heapq import heappush, heappop


def pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def transition(n, p, letter):
    if p is None:
        return None
    if letter == 'a':
        u, v = ((t + 1) % n for t in p)
    else:
        u, v = (0 if t == n - 1 else t for t in p)
    return None if u == v else tuple(sorted((u, v)))


def coords(n, p):
    i, j = p
    gap = j - i
    if gap < n - gap:
        return i, gap
    if gap > n - gap:
        return j, n - gap
    return i, gap  # antipodal: 0 <= i < n/2


def parameters(n, p):
    i, h = coords(n, p)
    if n % 2 == 0 and h == n // 2:
        n_a = (h - 1) * n - i
        n_b = h
        word = 'a' * (h - 1 - i) + 'b' + ('a' * (n - 1) + 'b') * (h - 1)
    else:
        n_a = h * (n - 1) - i
        n_b = h
        word = 'a' * (n - 1 - i) + 'b' + ('a' * (n - 1) + 'b') * (h - 1)
    return n_a, n_b, word


def reverse_distances(n, weights):
    ps = pairs(n)
    predecessors = {p: [] for p in ps}
    predecessors[None] = []
    for p in ps:
        for x in 'ab':
            nxt = transition(n, p, x)
            predecessors[nxt].append((p, weights['ab'.index(x)], x))
    best = {None: 0}
    ways = {None: 1}
    heap = [(0, 0, None)]
    counter = 0
    while heap:
        d, _, t = heappop(heap)
        if d != best[t]:
            continue
        for p, w, x in predecessors[t]:
            c = d + w
            if c < best.get(p, 10**20):
                best[p] = c
                ways[p] = ways[t]
                counter += 1
                heappush(heap, (c, counter, p))
            elif c == best.get(p):
                ways[p] += ways[t]
    assert len(best) == len(ps) + 1
    return best, ways


def check(n, with_dijkstra):
    ps = pairs(n)
    rho = {}
    for p in ps:
        na, nb, word = parameters(n, p)
        assert na == word.count('a') and nb == word.count('b'), (n, p)
        assert na >= 0 and nb >= 1 and len(word) == na + nb
        end = p
        for ch in word:
            end = transition(n, end, ch)
        assert end is None, (n, p, word, end)
        rho[p] = na + nb
        for ch in 'ab':
            q = transition(n, p, ch)
            qa, qb, _ = (0, 0, '') if q is None else parameters(n, q)
            if ch == 'a':
                assert na - qa <= 1, (n,p,ch,q,na,qa)
                assert nb == qb, (n,p,ch,q)
            else:
                assert na <= qa, (n,p,ch,q)
                assert nb - qb <= 1, (n,p,ch,q)
            assert na+nb - (qa+qb) <= 1
        descending = [ch for ch in 'ab' if rho[p] == (0 if transition(n,p,ch) is None else sum(parameters(n,transition(n,p,ch))[:2])) + 1]
        assert len(descending) == 1, (n,p,descending)
        assert word[0] == descending[0]
    assert sorted(rho.values()) == list(range(1, n*(n-1)//2 + 1)), (n, sorted(rho.values()))
    if with_dijkstra:
        for wa, wb in ((1,1),(1,4),(4,1),(3,7),(11,2)):
            best, ways = reverse_distances(n, (wa, wb))
            for p in ps:
                na, nb, word = parameters(n, p)
                assert best[p] == wa*na + wb*nb, (n,p,wa,wb,best[p],na,nb)
                assert ways[p] == 1, (n,p,wa,wb,ways[p])


def main():
    for n in range(2, 51):
        check(n, n <= 17)
    print('VERIFY_OK: n=2..50, pair potential inequalities, exact word, unique descending transition, distance spectrum; 5 independent positive weightings n=2..17 via reverse Dijkstra')


if __name__ == '__main__':
    main()
