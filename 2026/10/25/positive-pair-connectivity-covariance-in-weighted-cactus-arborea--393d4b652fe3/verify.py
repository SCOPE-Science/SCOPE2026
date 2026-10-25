"""Exact finite checks for arboreal-gas pair-connectivity covariance on cactus graphs."""
from fractions import Fraction
from itertools import combinations, product
from collections import deque


def block_support(x, y, blocks):
    graph = {}
    for j, block in enumerate(blocks):
        b = ("block", j)
        for v in block:
            a = ("vertex", v)
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)
    start, end = ("vertex", x), ("vertex", y)
    q = deque([start]); parent = {start: None}
    while q:
        t = q.popleft()
        if t == end:
            break
        for z in graph[t]:
            if z not in parent:
                parent[z] = t
                q.append(z)
    assert end in parent
    support = set(); t = end
    while t is not None:
        if t[0] == 'block':
            support.add(t[1])
        t = parent[t]
    return support


def check_graph(n, edges, weights, blocks):
    assert len(edges) == len(weights)
    pairs = list(combinations(range(n), 2))
    support = {pair: block_support(*pair, blocks) for pair in pairs}
    Z = 0
    marg = {pair: Fraction(0) for pair in pairs}
    cross = {pair: Fraction(0) for pair in combinations(pairs, 2)}
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        weight = Fraction(1)
        valid = True
        def root(a):
            while parent[a] != a:
                a = parent[a]
            return a
        for i, (u,v) in enumerate(edges):
            if (mask >> i) & 1:
                ru, rv = root(u), root(v)
                if ru == rv:
                    valid = False
                    break
                parent[ru] = rv
                weight *= weights[i]
        if not valid:
            continue
        Z += weight
        conn = {pair: root(pair[0]) == root(pair[1]) for pair in pairs}
        for pair in pairs:
            if conn[pair]:
                marg[pair] += weight
        for p1,p2 in cross:
            if conn[p1] and conn[p2]:
                cross[(p1,p2)] += weight
    assert Z > 0
    tests = 0
    for p1,p2 in cross:
        numerator = Z * cross[(p1,p2)] - marg[p1] * marg[p2]
        shared = bool(support[p1] & support[p2])
        assert (numerator > 0) == shared, (n, p1, p2, numerator, shared)
        assert (numerator == 0) == (not shared), (n, p1, p2, numerator, shared)
        tests += 1
    for pair in pairs:
        assert 0 < marg[pair] < Z
        tests += 1
    return tests


def identity(a,b,c,d):
    Z=(1+a)*(1+b)*(1+c)*(1+d)-1
    U=a+b+a*b+c+d+c*d
    V=a+c+a*c+b+d+b*d
    S=a+b+c+d
    D=S*Z-U*V
    Q=(a*d*((a+d)*(1+b)*(1+c)+b+c+b*c)
       +b*c*((b+c)*(1+a)*(1+d)+a+d+a*d)
       +2*a*b*c*d)
    assert D == Q


def main():
    count = 0
    for a,b,c,d in product(range(4), repeat=4):
        identity(a,b,c,d); count += 1
    for k in range(3,8):
        edges = [(i,(i+1)%k) for i in range(k)]
        weights = [Fraction([1,2,3,5,7,11,13][i], [2,3,4,5,6,7,8][i]) for i in range(k)]
        count += check_graph(k,edges,weights,[list(range(k))])
    # Two cycles joined at one articulation point.
    count += check_graph(5, [(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],
                          [Fraction(z, z+1) for z in (2,3,4,5,6,7)],
                          [[0,1,2],[0,3,4]])
    # Two cycles separated by a bridge.
    count += check_graph(6,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)],
                          [Fraction(z,z+2) for z in range(2,9)],
                          [[0,1,2],[2,3],[3,4,5]])
    # A triangle joined by a bridge to a four-cycle.
    count += check_graph(7,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,3)],
                          [Fraction(z,z+3) for z in range(2,10)],
                          [[0,1,2],[2,3],[3,4,5,6]])
    print('PASS:',count,'exact identity and graph-connections assertions')

if __name__ == '__main__':
    main()
