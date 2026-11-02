#!/usr/bin/env python3
"""Independent finite checks for the crown zero-forcing configuration theorem."""
from collections import Counter, deque
from itertools import combinations


def instance(n):
    vertices = range(2*n)
    neighbors = [set() for _ in vertices]
    for i in range(n):
        for j in range(n):
            if i != j:
                neighbors[i].add(n+j)
                neighbors[n+j].add(i)
    def closure(white):
        black = set(vertices) - set(white)
        while True:
            new = set()
            for v in black:
                missing = neighbors[v] - black
                if len(missing) == 1:
                    new.update(missing)
            if not new:
                return len(black) == 2*n
            black.update(new)

    # Exhaustively check all candidate sets with four initially white vertices.
    successful = set()
    for w in combinations(vertices, 4):
        if closure(w):
            successful.add(frozenset(w))
    expected = set()
    pairs = list(combinations(range(n), 2))
    for aa in pairs:
        for bb in pairs:
            if aa != bb:
                expected.add(frozenset(aa + tuple(n+i for i in bb)))
    assert successful == expected, (n, len(successful), len(expected))
    # The candidate exchange graph is generated from original zero-forcing sets,
    # not from assumed Johnson-graph edges.
    conf = sorted(expected, key=lambda w: tuple(sorted(w)))
    ids = {w:i for i,w in enumerate(conf)}
    graph = [[] for _ in conf]
    for i,w in enumerate(conf):
        for x in w:
            for y in vertices:
                if y not in w:
                    next_w = frozenset((w-{x}) | {y})
                    j = ids.get(next_w)
                    if j is not None:
                        graph[i].append(j)
        graph[i] = sorted(set(graph[i]))
    # Derive shortest paths from the actual exchange graph.
    N = len(pairs)
    k = 2*(n-2)
    distance_total = 0
    histogram = Counter()
    ecc = set()
    for i,w in enumerate(conf):
        aa = frozenset(v for v in w if v < n)
        bb = frozenset(v-n for v in w if v >= n)
        deg = 4*n-10 if len(aa&bb) == 1 else 4*n-8
        assert len(graph[i]) == deg
        distances = [-1]*len(conf)
        distances[i] = 0
        queue = deque([i])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distances[v] < 0:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        assert -1 not in distances
        ecc.add(max(distances))
        for j,z in enumerate(conf):
            cc = frozenset(v for v in z if v < n)
            dd = frozenset(v-n for v in z if v >= n)
            lower = (2-len(aa&cc)) + (2-len(bb&dd))
            exception = int(aa == dd and bb == cc and len(aa&bb)==1)
            assert distances[j] == lower + exception, (n,i,j,distances[j],lower,exception)
        distance_total += sum(distances)
        histogram.update(distances)
    assert len(ecc) == 1 and ecc.pop() == (3 if n==3 else 4)
    assert len(conf) == N*(N-1)
    wiener = distance_total//2
    assert distance_total%2 == 0
    r = N-1-k
    predicted = [N*(N-1), 2*N*k*(N-2), N*(N-2)*(k*k+2*r),
                 N*k*(2*(N-2)*r+1), N*r*((N-2)*r+1)]
    assert [histogram[d] for d in range(5)] == predicted, (n,histogram,predicted)
    expected_w = N*((N-1)**2*(n-1)*(n-2)+(n-2))
    assert wiener == expected_w
    print('PRIMARY_PASS', n, 'states',len(conf),'edges',sum(map(len,graph))//2,
          'diam',3 if n==3 else 4,'wiener',wiener)

if __name__ == '__main__':
    for n in range(3,9):
        instance(n)
    print('PRIMARY_CROWN_CERTIFICATE_OK')
