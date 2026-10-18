"""Exact checks for excess-degree profiles on Cayley-tree geodesics.

Run: python verify.py. Python standard library only.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import product
from math import factorial
import heapq


def prufer_edges(code, n):
    deg = [1] * n
    for v in code:
        deg[v] += 1
    leaves = [v for v in range(n) if deg[v] == 1]
    heapq.heapify(leaves)
    edges = []
    for v in code:
        w = heapq.heappop(leaves)
        edges.append((w, v))
        deg[v] -= 1
        if deg[v] == 1:
            heapq.heappush(leaves, v)
    edges.append((heapq.heappop(leaves), heapq.heappop(leaves)))
    return edges


def geodesic_excess(edges, n):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    parent = [-1] * n
    parent[0] = 0
    q = deque([0])
    while q:
        x = q.popleft()
        for y in adj[x]:
            if parent[y] < 0:
                parent[y] = x
                q.append(y)
    path = [1]
    while path[-1] != 0:
        path.append(parent[path[-1]])
    path.reverse()
    extra = tuple(len(adj[x]) - (1 if i in (0,len(path)-1) else 2)
                  for i,x in enumerate(path))
    assert all(e >= 0 for e in extra)
    return len(path)-1, extra


def probability(n, k, excess):
    length = k+1
    if k == n-1:
        return Fraction(int(all(x == 0 for x in excess)))
    m = n-k-2
    total = sum(excess)
    if total < 1 or total > m+1:
        return Fraction(0)
    ways = 0
    for i in range(length):
        if excess[i] == 0:
            continue
        amounts = list(excess)
        amounts[i] -= 1
        outside = m-sum(amounts)
        assert outside >= 0
        coefficient = factorial(m)//(factorial(outside) *
                         __import__('math').prod(factorial(x) for x in amounts))
        ways += coefficient * (n-length)**outside
    return Fraction(ways, length * n**m)


def check():
    trees = comparisons = 0
    for n in range(2, 9):
        counts = Counter()
        histograms = {}
        for code in product(range(n), repeat=n-2):
            k, e = geodesic_excess(prufer_edges(code, n), n)
            counts[k] += 1
            histograms.setdefault(k, Counter())[e] += 1
            trees += 1
        assert sum(counts.values()) == n**(n-2)
        for k in range(1, n):
            expected_count = (k+1)*factorial(n-2)//factorial(n-k-1)*n**(n-k-2) if k<n-1 else factorial(n-2)
            assert counts[k] == expected_count, (n,k,counts[k],expected_count)
            mass_total = Fraction(0)
            for excess, count in histograms[k].items():
                observed = Fraction(count, counts[k])
                expected = probability(n,k,excess)
                assert observed == expected, (n,k,excess,observed,expected)
                mass_total += expected
                comparisons += 1
            assert mass_total == 1, (n,k,mass_total)
            if k < n-1:
                observed_R = sum(sum(e)*count for e,count in histograms[k].items())
                expected_R = 1 + Fraction((n-k-2)*(k+1), n)
                assert Fraction(observed_R, counts[k]) == expected_R
                comparisons += 1
                if k+1 >= 2:
                    means = [Fraction(sum(e[i]*count for e,count in histograms[k].items()), counts[k])
                             for i in (0,1)]
                    cross = Fraction(sum(e[0]*e[1]*count for e,count in histograms[k].items()), counts[k])
                    predicted = -Fraction(1,(k+1)**2)-Fraction(n-k-2,n**2)
                    assert cross-Fraction(means[0])*Fraction(means[1]) == predicted
                    comparisons += 1
    print('PASS: %d Cayley trees; %d exact geodesic-profile checks' % (trees, comparisons))


if __name__ == '__main__':
    check()
