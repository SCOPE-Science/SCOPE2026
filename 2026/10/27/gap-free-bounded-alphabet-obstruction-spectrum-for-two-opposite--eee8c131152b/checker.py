"""Independent finite diagnostics for the bounded-domain binary team obstruction theorem.

The proof for all alphabet sizes is given in RESULT.md; this script checks
small complete bipartite edge subsets and explicit unbounded witness families.
"""
from collections import Counter
from itertools import product


def pseudoforest(a, b, edges):
    adj = [[] for _ in range(a + b)]
    for x, y in edges:
        u, v = x, a + y
        adj[u].append(v)
        adj[v].append(u)
    seen = set()
    for root in range(a + b):
        if root in seen:
            continue
        todo = [root]
        seen.add(root)
        verts = degrees = 0
        while todo:
            u = todo.pop()
            verts += 1
            degrees += len(adj[u])
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
        if degrees // 2 > verts:
            return False
    return True


def directly_satisfies(edges):
    # Enumerate all splitting-disjunction partitions, without using graph theory.
    for selection in range(1 << len(edges)):
        rows, columns = {}, {}
        valid = True
        for i, (x, y) in enumerate(edges):
            if selection & (1 << i):
                if x in rows and rows[x] != y:
                    valid = False
                    break
                rows[x] = y
            else:
                if y in columns and columns[y] != x:
                    valid = False
                    break
                columns[y] = x
        if valid:
            return True
    return False


def obstruction(a, b, edges):
    edges = list(edges)
    return (not pseudoforest(a, b, edges)
            and all(pseudoforest(a, b, edges[:i] + edges[i + 1:])
                    for i in range(len(edges))))


def odd_theta(t):
    # Alternating Hamiltonian 2t-cycle plus a noncycle chord.
    assert t >= 3
    result = {(i, i) for i in range(t)}
    result |= {((i + 1) % t, i) for i in range(t)}
    result.add((0, 1))
    return result


def even_theta(t):
    # Three internally disjoint paths of lengths 2, 2, 2t-2,
    # connecting row vertices 0 and 1, on t rows and t+1 columns.
    assert t >= 2
    result = {(0, 0), (1, 0), (0, 1), (1, 1)}
    last = 0
    for i in range(2, t):
        result.add((last, i))
        result.add((i, i))
        last = i
    result.add((last, t))
    result.add((1, t))
    return result


checks = 0
for a, b in [(1, 1), (1, 5), (2, 2), (2, 3), (2, 4),
             (3, 3), (3, 4), (4, 4)]:
    all_edges = list(product(range(a), range(b)))
    minimum = Counter()
    for mask in range(1 << (a * b)):
        subset = [e for i, e in enumerate(all_edges) if (mask >> i) & 1]
        good = pseudoforest(a, b, subset)
        checks += 1
        if a * b <= 9:
            assert directly_satisfies(subset) == good
            checks += 1
        if not good and all(pseudoforest(a, b, subset[:i] + subset[i+1:])
                            for i in range(len(subset))):
            minimum[len(subset)] += 1
    s = min(a, b)
    maximum = None if (s == 1 or (a, b) == (2, 2)) else (
        2 * s + 1 if a == b else 2 * s + 2)
    expected_spectrum = set(range(6, maximum + 1)) if maximum else set()
    assert set(minimum) == expected_spectrum, (a, b, minimum)
    checks += 1
    print(f'K_{a},{b}: min-obstruction size:counts {sorted(minimum.items())}')

for t in range(2, 41):
    ev = even_theta(t)
    assert len(ev) == 2 * t + 2 and len({x for x, y in ev}) == t
    assert len({y for x, y in ev}) == t + 1
    assert obstruction(t, t + 1, ev)
    checks += 4
    if t >= 3:
        od = odd_theta(t)
        assert len(od) == 2 * t + 1
        assert obstruction(t, t, od)
        checks += 2

print('Finite checks:', checks)
print('ALL_CHECKS_OK')
