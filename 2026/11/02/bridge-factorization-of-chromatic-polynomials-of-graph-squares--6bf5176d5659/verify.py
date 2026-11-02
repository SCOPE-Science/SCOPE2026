"""Direct finite checks for a bridge decomposition formula for graph-square colorings.

Run with Python 3 (standard library only): python verify.py
All comparisons use the original graph-distance definition, not a recurrence
for bridge color extensions.  Finite checks corroborate rather than prove the theorem.
"""
from fractions import Fraction
from itertools import combinations
from math import prod
from random import Random


def square(adj):
    out = [set(ns) for ns in adj]
    for v in range(len(adj)):
        for w in adj[v]:
            out[v].update(adj[w])
        out[v].discard(v)
    return out


def colorings(adj, q):
    n = len(adj)
    order = sorted(range(n), key=lambda x: (-len(adj[x]), x))
    prev = [[j for j in range(i) if order[j] in adj[order[i]]]
            for i in range(n)]
    state = [-1] * n
    def search(i):
        if i == n:
            return 1
        forbidden = {state[j] for j in prev[i]}
        total = 0
        for value in range(q):
            if value not in forbidden:
                state[i] = value
                total += search(i + 1)
        state[i] = -1
        return total
    return search(0)


def connected(adj):
    if not adj:
        return False
    reach = {0}
    frontier = [0]
    for u in frontier:
        for v in adj[u]:
            if v not in reach:
                reach.add(v)
                frontier.append(v)
    return len(reach) == len(adj)


def bridge_decompose(adj):
    n = len(adj)
    bridge_edges = []
    for a in range(n):
        for b in adj[a]:
            if a < b:
                clone = [set(ns) for ns in adj]
                clone[a].remove(b)
                clone[b].remove(a)
                if not connected_between(clone, a, b):
                    bridge_edges.append((a, b))
    blocks = [set(ns) for ns in adj]
    for a, b in bridge_edges:
        blocks[a].remove(b)
        blocks[b].remove(a)
    parts = []
    owner = {}
    for a in range(n):
        if a in owner:
            continue
        stack = [a]
        owner[a] = len(parts)
        for u in stack:
            for v in blocks[u]:
                if v not in owner:
                    owner[v] = len(parts)
                    stack.append(v)
        parts.append(stack)
    cores = []
    for part in parts:
        loc = {v: i for i, v in enumerate(part)}
        cores.append([{loc[z] for z in blocks[v]} for v in part])
    t = [0] * n
    for a, b in bridge_edges:
        t[a] += 1
        t[b] += 1
    return cores, parts, t


def connected_between(adj, a, b):
    seen = {a}
    stack = [a]
    for u in stack:
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return b in seen


def prediction(adj, q):
    if q < 2:
        return 0
    cores, parts, t = bridge_decompose(adj)
    value = Fraction(prod(colorings(square(h), q) for h in cores),
                     (q * (q - 1)) ** (len(cores) - 1))
    for core, part in zip(cores, parts):
        for i, orig in enumerate(part):
            value *= prod(q - len(core[i]) - 1 - j for j in range(t[orig]))
    assert value.denominator == 1, (q, value)
    return value.numerator


def graph_from_edges(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def finite_exhaustion():
    tests = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for bitset in range(1 << len(pairs)):
            adj = graph_from_edges(n, [e for i, e in enumerate(pairs)
                                       if bitset & (1 << i)])
            if not connected(adj):
                continue
            for q in (2, 3, 4, 5):
                actual = colorings(square(adj), q)
                expected = prediction(adj, q)
                assert actual == expected, (n, bitset, q, actual, expected)
                tests += 1
    print('ALL_CONNECTED_LABELLED_GRAPHS_THROUGH_FIVE_OK', tests)


def assemble(cores, bridge_list):
    offsets = []
    total = 0
    for c in cores:
        offsets.append(total)
        total += len(c)
    ans = [set() for _ in range(total)]
    for i, core in enumerate(cores):
        for a, neigh in enumerate(core):
            ans[offsets[i] + a].update(offsets[i] + b for b in neigh)
    for i, a, j, b in bridge_list:
        u, v = offsets[i] + a, offsets[j] + b
        ans[u].add(v)
        ans[v].add(u)
    return ans


def random_core(rng, n):
    adj = [set() for _ in range(n)]
    for i in range(1, n):
        j = rng.randrange(i)
        adj[i].add(j)
        adj[j].add(i)
    for i in range(n):
        for j in range(i):
            if j not in adj[i] and rng.randrange(3) == 0:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def random_block_trees():
    rng = Random(1404)
    tests = 0
    for k in (2, 3, 4):
        for iteration in range(40 if k == 2 else 25):
            lens = [rng.randint(1, 4) for _ in range(k)]
            if sum(lens) > 11:
                continue
            blocks = [random_core(rng, n) for n in lens]
            bridges = [(rng.randrange(i), 0, i, 0) for i in range(1, k)]
            # Distinct and repeated attachment vertices both occur.
            bridges = [(p, rng.randrange(lens[p]), i, rng.randrange(lens[i]))
                       for p, _, i, _ in bridges]
            adj = assemble(blocks, bridges)
            for q in (2, 3, 4, 5):
                actual = colorings(square(adj), q)
                expected = prediction(adj, q)
                assert actual == expected, (lens, bridges, q, actual, expected)
                tests += 1
    print('RANDOM_BLOCK_TREES_EXACT_COLORINGS_OK', tests)


def cycle(n):
    return graph_from_edges(n, [(i, (i + 1) % n) for i in range(n)])


def example_census():
    lengths = [cycle(3) for _ in range(4)]
    path = assemble(lengths, [(0, 0, 1, 0), (1, 1, 2, 0), (2, 1, 3, 0)])
    star = assemble(lengths, [(0, 0, 1, 0), (0, 1, 2, 0), (0, 2, 3, 0)])
    def diameter(adj):
        diam = 0
        for source in range(len(adj)):
            dist = {source: 0}
            todo = [source]
            for u in todo:
                for v in adj[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        todo.append(v)
            diam = max(diam, max(dist.values()))
        return diam
    assert diameter(path) == 7 and diameter(star) == 5
    for q in (3, 4, 5):
        assert colorings(square(path), q) == colorings(square(star), q)
    assert colorings(square(path), 4) == 192
    print('NONISOMORPHIC_BRIDGE_TREES_SAME_CHROMATIC_POLYNOMIAL_WITNESS_OK')
    assert colorings(square(cycle(6)), 4) == 96
    sixpair = assemble([cycle(6), cycle(6)], [(0, 0, 1, 0)])
    assert colorings(square(sixpair), 4) == 768
    print('NONCHORDAL_SIX_CYCLE_BRIDGE_WITNESS_OK')


if __name__ == '__main__':
    finite_exhaustion()
    random_block_trees()
    example_census()
    print('VERIFY_OK')
