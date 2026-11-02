"""Exact finite checks for wheel spanning-tree exchange eccentricities.
Run: python3 verify_wheel_metric.py. Python standard library only.
"""
from collections import Counter, deque
from itertools import combinations


def connected_components(nv, edges):
    parent = list(range(nv))
    def root(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        x, y = root(u), root(v)
        if x != y:
            parent[x] = y
    return len({root(i) for i in range(nv)})


def enumerate_trees(m):
    # Rim vertices 0,...,m-1; hub vertex m.
    edges = [(i, (i+1) % m) for i in range(m)] + [(i, m) for i in range(m)]
    all_indices = set(range(2*m))
    trees = []
    for ix in combinations(range(2*m), m):
        if connected_components(m+1, (edges[i] for i in ix)) == 1:
            trees.append(frozenset(ix))
    distribution = Counter()
    for tree in trees:
        complement = [edges[i] for i in all_indices - tree]
        # |E(complement)|=m and |V|=m+1, so its cyclic rank is components-1.
        cycles = connected_components(m+1, complement) - 1
        ecc = m - cycles
        distribution[ecc] += 1
        assert m - m//3 <= ecc <= m
    assert min(distribution) == m - m//3
    assert max(distribution) == m
    assert distribution[m] == 2**(m+1)-4
    # For small orders verify the matroidal formula against the actual basis graph BFS.
    if m <= 5:
        index = {t: i for i, t in enumerate(trees)}
        graph = [[] for t in trees]
        for i, t in enumerate(trees):
            for outgoing in t:
                for incoming in all_indices - t:
                    j = index.get((t-{outgoing})|{incoming})
                    if j is not None:
                        graph[i].append(j)
        for i, t in enumerate(trees):
            dist = [-1]*len(trees)
            dist[i] = 0
            queue = deque([i])
            while queue:
                x = queue.popleft()
                for y in graph[x]:
                    if dist[y] == -1:
                        dist[y] = dist[x] + 1
                        queue.append(y)
            assert -1 not in dist
            assert max(dist) == m-(connected_components(m+1,
                [edges[k] for k in all_indices - t])-1)
            for j, u in enumerate(trees):
                assert dist[j] == m-len(t & u)
    return len(trees), distribution


if __name__ == '__main__':
    for m in range(3, 11):
        count, dist = enumerate_trees(m)
        print('WHEEL_TREE_METRIC_PASS', 'm='+str(m), 'trees='+str(count),
              'radius='+str(min(dist)), 'diameter='+str(max(dist)),
              'peripheral='+str(dist[m]))
    print('ALL_WHEEL_TREE_METRIC_CHECKS_PASS')
