"""Finite cross-checks for a family of circular rank-(n-1) automata.

The infinite statement is proved symbolically in RESULT.md.
"""
from collections import deque


def images(n, k):
    return tuple((i + 1) % n for i in range(n)), tuple(i + 1 if i < k else i for i in range(n))


def shortest(n, k):
    A, B = images(n, k)
    todo = deque([(1 << n) - 1])
    dist = {todo[0]: 0}
    while todo:
        m = todo.popleft()
        if m.bit_count() == 1:
            return dist[m], len(dist)
        for f in (A, B):
            nxt = 0
            for i in range(n):
                if (m >> i) & 1:
                    nxt |= 1 << f[i]
            if nxt not in dist:
                dist[nxt] = dist[m] + 1
                todo.append(nxt)
    raise AssertionError('not synchronizing')


def witness(n, k):
    q, r = divmod(n - 1, k)
    if r:
        return 'b' * r + 'a' * (n - r) + ('b' * k + 'a' * (n - k)) * (q - 1) + 'b' * k
    return ('b' * k + 'a' * (n - k)) * (q - 1) + 'b' * k


def cyclic_interval(S, n):
    return S == set(range(n)) or not S or sum((i in S) and (((i+1) % n) not in S) for i in range(n)) == 1


def run():
    bfcases = 0
    nodes = 0
    witness_cases = 0
    domcases = 0
    for n in range(3, 17):
        for k in range(2, n):
            shortest_length, states = shortest(n, k)
            nodes += states
            expected = n * ((n - 1 + k - 1) // k - 1) + k
            w = witness(n, k)
            assert len(w) == shortest_length == expected, (n, k, len(w), shortest_length, expected)
            A, B = images(n, k)
            S = set(range(n))
            for ch in w:
                S = { (A if ch == 'a' else B)[i] for i in S }
            assert len(S) == 1, (n, k, w, S)
            bfcases += 1
    for n in range(3, 23):
        for k in range(2, n):
            A, B = images(n, k)
            for start in range(n):
                for size in range(1, n):
                    I = {(start + d) % n for d in range(size)}
                    IA = {i for i in range(n) if A[i] in I}
                    IB = {i for i in range(n) if B[i] in I}
                    assert cyclic_interval(IA, n) and cyclic_interval(IB, n)
                    if k in I and 0 not in I:
                        assert IA.issubset(IB), (n, k, start, size)
                    else:
                        assert IB == I or IB.issubset(IA), (n, k, start, size)
                    domcases += 1
    for n in range(17, 61):
        for k in range(2, n):
            w = witness(n, k)
            assert len(w) == n * ((n + k - 2) // k - 1) + k
            A, B = images(n, k)
            S = set(range(n))
            for ch in w:
                S = {(A if ch == 'a' else B)[i] for i in S}
            assert len(S) == 1
            witness_cases += 1
    print('VERIFY_OK bfs_cases=%d bfs_states=%d interval_cases=%d large_witnesses=%d' % (bfcases, nodes, domcases, witness_cases))


if __name__ == '__main__':
    run()
