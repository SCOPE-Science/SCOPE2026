"""Finite exact-integer checks for chain-order polytope asymmetry and center dimensions.

All computations use only integers and the Python standard library.
The analytic proof, not these finite tests, establishes the unrestricted theorem.
"""
from itertools import combinations


def instances(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        rel = {(a, b) for k, (a, b) in enumerate(pairs) if mask >> k & 1}
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (i, k) in rel and (k, j) in rel:
                        rel.add((i, j))
        yield rel


def check(n, rel, chain_set):
    top = n
    pred = {i: [j for j in range(i) if (j, i) in rel] for i in range(n)}
    succ = {i: [j for j in range(i + 1, n) if (i, j) in rel] for i in range(n)}
    cover = {(i, j) for i, j in rel if not any((i, k) in rel and (k, j) in rel for k in range(n))}
    cover.update({(-1, i) for i in range(n) if not pred[i]})
    cover.update({(i, top) for i in range(n) if not succ[i]})
    lengths = {}
    for i in range(n):
        lengths[i] = 1 + max([lengths[j] for j in pred[i]], default=0)
    upper = {}
    for i in range(n - 1, -1, -1):
        upper[i] = 1 + max([upper[j] for j in succ[i]], default=0)
    H = max(lengths.values())
    critical = {i for i in range(n) if lengths[i] + upper[i] - 1 == H}
    O = set(range(n)) - chain_set
    arcpaths = []
    adj = {a: [] for a in [-1] + list(range(n))}
    for a, b in cover:
        adj[a].append(b)

    def dfs(path):
        node = path[-1]
        if node not in chain_set:
            arcpaths.append(tuple(path))
            return
        for nxt in adj[node]:
            dfs(path + [nxt])

    for a in [-1] + sorted(O):
        for b in adj[a]:
            dfs([a, b])

    def obey(xc, yo, margin=0):
        for c in chain_set:
            if xc.get(c, 0) < margin:
                return False
        for path in arcpaths:
            a, b = path[0], path[-1]
            va = 0 if a == -1 else yo[a]
            vb = yo[b] if b != top else yo[top]
            if vb - va < sum(xc.get(v, 0) for v in path[1:-1]) + margin:
                return False
        return True

    # Baseline width-one certificate for every defining inequality.
    zero = {v: 0 for v in chain_set}
    z_o = {v: 0 for v in O}
    z_o[top] = 1
    assert obey(zero, z_o)
    for c in chain_set:
        xc = {v: int(v == c) for v in chain_set}
        yo = {v: int((c, v) in rel) for v in O}
        yo[top] = 1
        assert obey(xc, yo), ('coordinate width', n, rel, chain_set, c)
    for path in arcpaths:
        a, b = path[0], path[-1]
        yo = {v: int(v == b or (b, v) in rel) if b != top else 0 for v in O}
        yo[top] = 1
        assert obey(zero, yo)
        va = 0 if a == -1 else yo[a]
        vb = yo[b] if b != top else 1
        assert vb - va == 1
        if b != top:
            xc2, yo2 = zero, z_o
        elif a != -1:
            xc2 = zero
            yo2 = {v: 1 for v in O}
            yo2[top] = 1
        else:
            c = path[1]
            xc2 = {v: int(v == c) for v in chain_set}
            yo2 = {v: int((c, v) in rel) for v in O}
            yo2[top] = 1
        assert obey(xc2, yo2)
        va2 = 0 if a == -1 else yo2[a]
        vb2 = yo2[b] if b != top else 1
        assert vb2 - va2 == sum(xc2.get(v, 0) for v in path[1:-1])

    # Work in units of 1 / (2(H+1)); margin is exactly 2 units.
    budget = 2 * (H + 1)
    xc = {v: 2 for v in chain_set}
    yo = {v: 2 * lengths[v] for v in O}
    yo[top] = budget
    assert obey(xc, yo, 2)

    def longest(xc, boosted_arc=None):
        yo = {-1: 0}
        for b in list(range(n)) + [top]:
            if b in chain_set:
                continue
            incoming = [path for path in arcpaths if path[-1] == b]
            if not incoming:
                raise AssertionError('missing incoming arc')
            vals = [yo[path[0]] + sum(xc.get(v, 0) for v in path[1:-1]) + 2 +
                    int(path == boosted_arc) for path in incoming]
            yo[b] = max(vals)
        return yo

    # Each noncritical variable and each noncritical compressed edge
    # can receive a strict slack without exceeding the source-sink budget.
    for c in chain_set - critical:
        xx = dict(xc)
        xx[c] += 1
        yy = longest(xx)
        assert yy[top] <= budget
        yy[top] = budget
        assert obey(xx, yy, 2)
        assert xx[c] > 2
    for path in arcpaths:
        nodes = list(path[1:-1]) + [v for v in (path[0], path[-1]) if v not in (-1, top)]
        # An arc lies on a longest chain iff its longest prefix/suffix fit H.
        # For C vertices, the prefix/suffix are determined by the endpoints.
        a, b = path[0], path[-1]
        before = 0 if a == -1 else lengths[a]
        after = 0 if b == top else upper[b] - 1
        arc_on_longest = before + len(path[1:-1]) + (0 if b == top else 1) + after == H
        if b == top:
            arc_on_longest = before + len(path[1:-1]) == H
        if not arc_on_longest:
            yy = longest(xc, boosted_arc=path)
            assert yy[top] <= budget, ('arc bump', n, rel, chain_set, path, yy[top], budget)
            yy[top] = budget
            assert obey(xc, yy, 2)
            va = 0 if a == -1 else yy[a]
            vb = yy[b] if b != top else budget
            assert vb - va > sum(xc.get(v, 0) for v in path[1:-1]) + 2
        else:
            assert all(v in critical for v in nodes)
    return len(arcpaths)


def main():
    tested = arcs = 0
    for n in range(1, 6):
        for rel in instances(n):
            for choice in range(1 << n):
                C = {i for i in range(n) if choice >> i & 1}
                arcs += check(n, rel, C)
                tested += 1
    print('PASS: exact integer certificates on', tested,
          'naturally-labeled-poset/chain-order partition instances and', arcs,
          'compressed path inequalities (n=1..5).')

if __name__ == '__main__':
    main()
