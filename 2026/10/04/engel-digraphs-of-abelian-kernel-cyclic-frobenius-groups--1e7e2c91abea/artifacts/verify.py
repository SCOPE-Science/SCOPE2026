from itertools import product
from collections import defaultdict, deque


def all_kernel(moduli):
    return list(product(*[range(n) for n in moduli]))


def verify_case(moduli, scalar, m):
    K = all_kernel(moduli)
    zero = tuple(0 for _ in moduli)

    def add(a, b):
        return tuple((x + y) % n for x, y, n in zip(a, b, moduli))

    def neg(a):
        return tuple((-x) % n for x, n in zip(a, moduli))

    def act(i, a):
        return tuple((pow(scalar, i, n) * x) % n for x, n in zip(a, moduli))

    # Exact order and fixed-point-free action of every nonidentity complement element.
    assert all(pow(scalar, m, n) == 1 % n for n in moduli)
    for j in range(1, m):
        for v in K:
            if v != zero:
                assert act(j, v) != v

    elements = [(v, i) for v in K for i in range(m)]
    identity = (zero, 0)

    def mul(x, y):
        v, i = x
        w, j = y
        return (add(v, act(i, w)), (i + j) % m)

    def inv(x):
        v, i = x
        mi = (-i) % m
        return (neg(act(mi, v)), mi)

    def comm(x, y):
        return mul(mul(inv(x), inv(y)), mul(x, y))

    def engel_arc(x, y):
        z = x
        seen = set()
        for depth in range(1, len(elements) + 2):
            z = comm(z, y)
            if z == identity:
                return True, depth
            if z in seen:
                return False, None
            seen.add(z)
        raise AssertionError('iteration bound exceeded')

    # Reconstruct all conjugate complements directly.
    H = [(zero, j) for j in range(m)]
    blocks = []
    for a in K:
        ka = (a, 0)
        block = frozenset(
            mul(mul(inv(ka), h), ka)
            for h in H if h != identity
        )
        blocks.append(block)
    assert len(set(blocks)) == len(K)

    kernel_nontrivial = {(v, 0) for v in K if v != zero}
    outside = set(elements) - {(v, 0) for v in K}
    assert set().union(*blocks) == outside
    membership = {x: i for i, block in enumerate(blocks) for x in block}

    vertices = [x for x in elements if x != identity]
    arcs = set()
    depths = defaultdict(int)

    for x in vertices:
        for y in vertices:
            if x == y:
                continue
            got, depth = engel_arc(x, y)
            xk = x in kernel_nontrivial
            yk = y in kernel_nontrivial
            if xk and yk:
                predicted = True
            elif (not xk) and yk:
                predicted = True
            elif xk and (not yk):
                predicted = False
            else:
                predicted = membership[x] == membership[y]
            assert got == predicted
            if got:
                arcs.add((x, y))
                depths[depth] += 1
                assert depth <= 2
                if (not xk) and yk:
                    assert depth == 2
                else:
                    assert depth == 1

    k = len(K)
    predicted_arcs = (
        (k - 1) * (k - 2)
        + k * (m - 1) * (m - 2)
        + k * (m - 1) * (k - 1)
    )
    assert len(arcs) == predicted_arcs
    assert depths[1] == (k - 1) * (k - 2) + k * (m - 1) * (m - 2)
    assert depths[2] == k * (m - 1) * (k - 1)

    # Degree formulas.
    indeg = {v: 0 for v in vertices}
    outdeg = {v: 0 for v in vertices}
    for x, y in arcs:
        outdeg[x] += 1
        indeg[y] += 1
    for v in vertices:
        if v in kernel_nontrivial:
            assert (indeg[v], outdeg[v]) == (k * m - 2, k - 2)
        else:
            assert (indeg[v], outdeg[v]) == (m - 2, k + m - 3)

    # Strong components by Kosaraju, computed only from the enumerated arc set.
    adj = {v: [] for v in vertices}
    radj = {v: [] for v in vertices}
    for x, y in arcs:
        adj[x].append(y)
        radj[y].append(x)

    seen = set()
    order = []
    def dfs(start):
        stack = [(start, 0)]
        seen.add(start)
        while stack:
            v, idx = stack[-1]
            if idx < len(adj[v]):
                w = adj[v][idx]
                stack[-1] = (v, idx + 1)
                if w not in seen:
                    seen.add(w)
                    stack.append((w, 0))
            else:
                order.append(v)
                stack.pop()
    for v in vertices:
        if v not in seen:
            dfs(v)

    seen.clear()
    comps = []
    for start in reversed(order):
        if start in seen:
            continue
        comp = set([start])
        seen.add(start)
        q = [start]
        while q:
            v = q.pop()
            for w in radj[v]:
                if w not in seen:
                    seen.add(w)
                    comp.add(w)
                    q.append(w)
        comps.append(comp)

    sizes = sorted(len(c) for c in comps)
    assert sizes == sorted([k - 1] + [m - 1] * k)
    assert len(comps) == k + 1
    kernel_index = next(i for i, c in enumerate(comps) if c == kernel_nontrivial)
    comp_index = {v: i for i, c in enumerate(comps) for v in c}
    condensation = {(comp_index[x], comp_index[y]) for x, y in arcs if comp_index[x] != comp_index[y]}
    assert len(condensation) == k
    assert all(j == kernel_index and i != kernel_index for i, j in condensation)

    # Underlying undirected graph has diameter exactly two.
    uadj = {v: set() for v in vertices}
    for x, y in arcs:
        uadj[x].add(y)
        uadj[y].add(x)
    maxdist = 0
    for s in vertices:
        dist = {s: 0}
        q = deque([s])
        while q:
            v = q.popleft()
            for w in uadj[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    q.append(w)
        assert len(dist) == len(vertices)
        maxdist = max(maxdist, max(dist.values()))
    assert maxdist == 2

    # On outside vertices the co-Engel graph is complete k-partite with complement blocks as parts.
    for x in outside:
        for y in outside:
            if x >= y:
                continue
            engel_undirected = (x, y) in arcs or (y, x) in arcs
            assert engel_undirected == (membership[x] == membership[y])

    return {
        'kernel_order': k,
        'complement_order': m,
        'group_order': k * m,
        'arcs': len(arcs),
        'depth1': depths[1],
        'depth2': depths[2],
        'strong_components': len(comps),
        'diameter': maxdist,
    }


CASES = [
    ((3,), 2, 2),
    ((5,), 2, 4),
    ((7,), 2, 3),
    ((9,), 8, 2),
    ((5, 5), 2, 4),
    ((7, 7), 3, 6),
]

rows = [verify_case(*case) for case in CASES]
assert [r['arcs'] for r in rows] == [8, 102, 128, 128, 2502, 14996]
print('VERIFY_OK')
for row in rows:
    print(row)
