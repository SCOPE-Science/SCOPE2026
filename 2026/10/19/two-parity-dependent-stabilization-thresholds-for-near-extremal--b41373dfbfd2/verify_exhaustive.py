"""Independent exact enumeration of one-swap graphs of near-maximum sum-free subsets.
Runs using only Python standard library; repeats no mathematical assumptions about
which sets exist. Increasing-order backtracking prunes only completed Schur triples.
"""
from collections import Counter
from collections import deque


def enumerate_sets(n):
    k = (n + 1) // 2 - 1
    triples = []
    by_last = [[] for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = a + b
            if c <= n:
                by_last[c].append((a, b))
    result = []

    def rec(v, bits, count):
        if count == k:
            result.append(bits)
            return
        if v > n or count + n - v + 1 < k:
            return
        allowed = all(not ((bits >> (a - 1)) & 1 and (bits >> (b - 1)) & 1)
                      for a, b in by_last[v])
        # If a=b=v/2, both prior bits already present, so the new v would
        # complete a (possibly repeated-addend) Schur triple.
        if allowed:
            rec(v + 1, bits | (1 << (v - 1)), count + 1)
        rec(v + 1, bits, count)

    rec(1, 0, 0)
    return result


def graph_profile(n):
    sets = enumerate_sets(n)
    indices = {s:i for i, s in enumerate(sets)}
    assert len(indices) == len(sets)
    adj = [set() for _ in sets]
    for i, s in enumerate(sets):
        for a in range(n):
            if s & (1 << a):
                for b in range(n):
                    if not s & (1 << b):
                        j = indices.get(s ^ (1 << a) ^ (1 << b))
                        if j is not None:
                            adj[i].add(j)
    components = []
    unseen = set(range(len(sets)))
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = [start]
        for u in queue:
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v)
                    queue.append(v)
        components.append(len(queue))
    return len(sets), sum(map(len,adj)) // 2, sorted(components, reverse=True)


def expected(n):
    if n % 2:
        m = (n-1)//2
        return 2*m+4, m*(m+1)+5, [m+3,m+1]
    m=n//2
    return 3*m+2, m*(m-1)+(m-1)*(m-2)//2+2*(m-1)+9, [2*m+2,m]


if __name__ == '__main__':
    for n in [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]:
        p = graph_profile(n)
        if (n%2==1 and n>=15) or (n%2==0 and n>=20):
            assert p == expected(n), (n,p,expected(n))
        if n == 13:
            assert p == (18,47,[9,7,1,1])
        if n == 18:
            assert p == (31,125,[20,9,1,1])
        print(n, p)
    print('VERIFY_OK')
