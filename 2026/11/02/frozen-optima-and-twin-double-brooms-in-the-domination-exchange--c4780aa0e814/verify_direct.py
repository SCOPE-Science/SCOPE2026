"""Independent exhaustive dominating-set and token-slide checker for small ladders.

Only Python standard library is required. Vertex 2*c+r denotes row r,
column c (zero based). This script enumerates all subsets of candidate sizes.
"""
from itertools import combinations
from collections import Counter


def exact_minimum_sets(n):
    vertices = 2 * n
    neighborhoods = []
    for c in range(n):
        for r in (0, 1):
            verts = {2*c+r, 2*c+1-r}
            if c:
                verts.add(2*(c-1)+r)
            if c+1 < n:
                verts.add(2*(c+1)+r)
            neighborhoods.append(sum(1 << x for x in verts))
    whole = (1 << vertices) - 1
    for size in range(vertices+1):
        found = []
        for sub in combinations(range(vertices), size):
            covered = 0
            for x in sub:
                covered |= neighborhoods[x]
            if covered == whole:
                found.append(sum(1 << x for x in sub))
        if found:
            return size, found
    raise AssertionError('No dominating set')


def slide(a, b):
    diff = a ^ b
    if diff.bit_count() != 2:
        return False
    x = (diff & -diff).bit_length()-1
    y = (diff ^ (1 << x)).bit_length()-1
    return abs(x//2-y//2)+abs(x%2-y%2) == 1


def graph_stats(words):
    N = len(words)
    g = [set() for _ in range(N)]
    for a in range(N):
        for b in range(a+1, N):
            if slide(words[a],words[b]):
                g[a].add(b)
                g[b].add(a)
    unseen = set(range(N))
    comps = []
    while unseen:
        start = unseen.pop()
        reached = {start}
        todo = [start]
        while todo:
            for v in g[todo.pop()]:
                if v not in reached:
                    reached.add(v)
                    unseen.discard(v)
                    todo.append(v)
        comps.append(reached)
    return g, comps


for n in range(5,13):
    gamma, words = exact_minimum_sets(n)
    graph, comps = graph_stats(words)
    edges = sum(map(len, graph)) // 2
    if n % 2:
        assert gamma == n//2+1
        assert len(words) == 2
        assert len(comps) == 2
        assert edges == 0
    elif n == 6:
        assert gamma == 4
        assert len(words) == 17
        assert sorted(map(len,comps)) == [1,1,1,7,7]
        assert edges == 12
    else:
        k = n//2
        assert gamma == k+1
        assert len(words) == 4*k+4
        assert len(comps) == 2*k-2
        assert sorted(map(len, comps)) == [1]*(2*k-4)+[k+4,k+4]
        assert edges == 2*k+6
        assert Counter(map(len,graph)) == {0:2*k-4,1:8,2:2*k-4,3:4}
        for comp in comps:
            if len(comp) > 1:
                assert sum(len(graph[i]) for i in comp) // 2 == len(comp)-1
                assert sum(len(graph[i]) == 3 for i in comp) == 2
                assert sum(len(graph[i]) == 1 for i in comp) == 4
    print('n', n, 'minimum', gamma, 'states', len(words), 'edges', edges,
          'components', sorted(map(len,comps)))
print('DIRECT_EXHAUSTIVE_LADDER_PASS')
