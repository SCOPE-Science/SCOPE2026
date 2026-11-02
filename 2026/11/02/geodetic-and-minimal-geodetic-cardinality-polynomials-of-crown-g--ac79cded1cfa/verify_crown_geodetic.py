#!/usr/bin/env python3
"""Independent finite check of the geodetic-set and minimal-set formulas for crown graphs.

No third-party dependencies. Graph shortest paths are computed by BFS, independently
of the closed-form proof. Exhaustive testing is finite evidence, not an infinite proof.
"""
from collections import Counter, deque
from math import comb


def expected_all(n):
    ans = Counter()
    for k in range(2 * n + 1):
        value = comb(2 * n, k)
        if k <= n:
            value -= comb(n, k) * 2**k
        if k == n:
            value += 2
        if 6 <= k <= n:
            value += comb(n, k) * (2**k - 2 - 2*k - k*(k - 1))
        if value:
            ans[k] = value
    return ans


def expected_minimal(n):
    ans = Counter({2: n, n: 2})
    if n == 2:
        raise ValueError('n must be at least three')
    if n >= 6:
        ans[6] += comb(n, 3) * comb(n - 3, 3)
    return ans


def graph(n):
    N = 2 * n
    adj = [[] for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].append(n+j)
                adj[n+j].append(i)
    return adj


def intervals(adj):
    N = len(adj)
    ds = []
    for start in range(N):
        d = [-1] * N
        d[start] = 0
        Q = deque([start])
        while Q:
            v = Q.popleft()
            for w in adj[v]:
                if d[w] == -1:
                    d[w] = d[v] + 1
                    Q.append(w)
        assert all(x != -1 for x in d)
        ds.append(d)
    interval = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            interval[a][b] = sum(1<<v for v in range(N)
                                 if ds[a][v] + ds[v][b] == ds[a][b])
    return interval


def predicted_from_structure(S, n):
    X = {i for i in range(n) if S & (1<<i)}
    Y = {i for i in range(n) if S & (1<<(n+i))}
    if X & Y:
        return True
    if not X:
        return len(Y) == n
    if not Y:
        return len(X) == n
    return len(X) >= 3 and len(Y) >= 3


def run(max_n=9):
    total_masks=0
    for n in range(3, max_n + 1):
        N = 2*n
        I = intervals(graph(n))
        allmask = (1 << N) - 1
        covered = [0]*(1 << N)
        observed_all = Counter()
        observed_min = Counter()
        for S in range(1, 1 << N):
            lsb = S & -S
            a = lsb.bit_length()-1
            T = S ^ lsb
            c = covered[T] | lsb
            rem=T
            while rem:
                q=rem & -rem
                rem^=q
                b=q.bit_length()-1
                c |= I[a][b]
            covered[S]=c
            actual = c == allmask
            assert actual == predicted_from_structure(S,n), (n,S,actual)
            if actual:
                k=S.bit_count()
                observed_all[k]+=1
                if all(covered[S^(1<<v)] != allmask for v in range(N)
                       if S & (1<<v)):
                    observed_min[k]+=1
        assert observed_all==expected_all(n), (n,observed_all,expected_all(n))
        assert observed_min==expected_minimal(n), (n,observed_min,expected_minimal(n))
        assert sum(observed_min.values()) == n+2+(comb(n,3)*comb(n-3,3) if n>=6 else 0)
        total_masks += (1<<N)-1
        print('n=%d all=%d minimal=%s verified_subsets=%d' %
              (n,sum(observed_all.values()),dict(sorted(observed_min.items())),(1<<N)-1))
    print('VERIFY_OK graph_orders=%d tested_subsets=%d structural_and_polynomial_agreement=true' %
          (max_n-2,total_masks))

if __name__ == '__main__':
    run(9)
