#!/usr/bin/env python3
"""Exact checks for tandem-square-avoiding order-four universal cycles.

Python 3 standard library only. All arithmetic is integral and deterministic.
This checks finite instances and the structural matrix identities;
all-parameter validity follows from the written algebraic proof.
"""
from itertools import product, combinations
from math import factorial


def graph(q):
    states = list(product(range(q), repeat=3))
    pos = {s: i for i, s in enumerate(states)}
    out = [[] for _ in states]
    for i, (a, b, c) in enumerate(states):
        for d in range(q):
            if a == c and b == d:
                continue
            out[i].append((pos[(b, c, d)], (a, b, c, d)))
    return states, out


def det_bareiss(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if not a[k][k]:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            old_ik = a[i][k]
            for j in range(k + 1, n):
                top = p * a[i][j] - old_ik * a[k][j]
                if top % prev:
                    raise AssertionError('nonexact Bareiss division')
                a[i][j] = top // prev
            a[i][k] = 0
        prev = p
    return sign * a[-1][-1]


def tree_closed(q):
    return (q ** (q**3 - q**2 + q - 4)
            * (q - 1) ** (2 * (q - 1))
            * (q**2 - 2*q + 2) ** ((q-1)*(q-2)//2))


def cycles_closed(q):
    return (tree_closed(q) * factorial(q-2)**(q*q)
            * factorial(q-1)**(q**3-q*q))


def brute_binary_tours(states, out):
    i0 = states.index((0, 0, 0))
    fixed = next((j, word) for j, word in out[i0] if word == (0, 0, 0, 1))
    edge_ids = {(i, j, w): eid for eid, (i, j, w) in enumerate(
        (i, j, w) for i, arr in enumerate(out) for j, w in arr)}
    total = len(edge_ids)
    used = [False] * total
    used[edge_ids[(i0, *fixed)]] = True
    answers = []
    def dfs(at, trail):
        if len(trail) == total:
            if at == i0:
                word = ''.join(str(w[-1]) for w in trail)
                assert len({word[i:]+word[:i] for i in range(len(word))}) == len(word)
                answers.append(word)
            return
        for nxt, w in out[at]:
            eid = edge_ids[(at, nxt, w)]
            if used[eid]:
                continue
            used[eid] = True
            dfs(nxt, trail + [w])
            used[eid] = False
    dfs(fixed[0], [fixed[1]])
    assert len(answers) == len(set(answers))
    return answers


def main():
    for q in (2, 3, 4):
        states, edges = graph(q)
        n = len(states)
        assert n == q**3
        assert sum(map(len, edges)) == q**4 - q**2
        degree_in = [0] * n
        for i, arr in enumerate(edges):
            assert len(arr) == (q-1 if states[i][0] == states[i][2] else q)
            for j, word in arr:
                degree_in[j] += 1
                assert not (word[0] == word[2] and word[1] == word[3])
        assert degree_in == list(map(len, edges))
        L = [[0] * n for _ in range(n)]
        for i, arr in enumerate(edges):
            L[i][i] = len(arr)
            for j, _ in arr:
                L[i][j] -= 1
        arbs = det_bareiss([r[:-1] for r in L[:-1]])
        assert arbs == tree_closed(q), (q, arbs, tree_closed(q))
        if q == 2:
            tours = brute_binary_tours(states, edges)
            assert len(tours) == cycles_closed(q) == 4
        print('q={} vertices={} allowed_words={} trees={} cycles={}'.format(
            q, n, sum(map(len, edges)), arbs, cycles_closed(q)))
    for length in range(4, 151):
        v = ('0100' + '1100' * 38)[:length]
        assert len(v) == length
        assert all(not (v[i] == v[i+2] and v[i+1] == v[i+3])
                   for i in range(length - 3))
        assert v[0] == v[2] and v[-3] != v[-1]
    print('non-Eulerian witness verified for vertex lengths 4..150')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
