"""Reproduce finite two-partition representations of anonymous S5 knowledge."""
from collections import defaultdict
from itertools import product


def set_partitions(n):
    """Canonical restricted-growth encodings of partitions of range(n)."""
    def build(i, labels, top):
        if i == n:
            return [tuple(frozenset(v for v, k in enumerate(labels) if k == b)
                          for b in range(top + 1))]
        result = []
        for j in range(top + 2):
            result += build(i + 1, labels + [j], max(j, top))
        return result
    return build(1, [0], 0)


def operator(n, E, F):
    """All 2**n operator outputs encoded as bitmasks."""
    e = [next(B for B in E if w in B) for w in range(n)]
    f = [next(B for B in F if w in B) for w in range(n)]
    ans = []
    for mask in range(1 << n):
        S = {j for j in range(n) if mask & (1 << j)}
        ans.append(sum(1 << w for w in range(n) if e[w] <= S or f[w] <= S))
    return tuple(ans)


def analyze(n, op):
    """Recover all ordered two-agent S5 representations in the two-core case.

    Returns (represented, count, core, components, reconstructed_pairs).
    """
    assert len(op) == 1 << n
    for x in range(1 << n):
        for y in range(1 << n):
            if x & y == x and op[x] & op[y] != op[x]:
                return (False, 0, None, None, [])
    core = []
    for w in range(n):
        eligible = [frozenset(i for i in range(n) if mask & (1 << i))
                    for mask in range(1 << n) if op[mask] & (1 << w)]
        mins = tuple(sorted((B for B in eligible
                             if not any(A < B for A in eligible)),
                            key=lambda B: tuple(sorted(B))))
        if len(mins) != 2 or w not in mins[0] or w not in mins[1]:
            return (False, 0, None, None, [])
        core.append(mins)
    for w in range(n):
        for B in core[w]:
            if any(B not in core[v] for v in B):
                return (False, 0, core, None, [])
    blocks = sorted(set(B for pair in core for B in pair), key=lambda B: (len(B), tuple(sorted(B))))
    index = {B: i for i, B in enumerate(blocks)}
    g = [set() for _ in blocks]
    for A, B in core:
        a, b = index[A], index[B]
        g[a].add(b)
        g[b].add(a)
    col = {}
    components = []
    for start in range(len(blocks)):
        if start in col:
            continue
        col[start] = 0
        work = [start]
        comp = []
        while work:
            v = work.pop()
            comp.append(v)
            for u in g[v]:
                if u in col:
                    if col[u] == col[v]:
                        return (False, 0, core, None, [])
                else:
                    col[u] = 1 - col[v]
                    work.append(u)
        components.append(comp)
    pairs = []
    for bits in product((0, 1), repeat=len(components)):
        block_colors = {v: col[v] ^ bits[j]
                        for j, comp in enumerate(components) for v in comp}
        E = frozenset(blocks[v] for v in range(len(blocks)) if block_colors[v] == 0)
        F = frozenset(blocks[v] for v in range(len(blocks)) if block_colors[v] == 1)
        assert sorted(x for B in E for x in B) == list(range(n))
        assert sorted(x for B in F for x in B) == list(range(n))
        assert operator(n, E, F) == op
        pairs.append((E, F))
    assert len(set(pairs)) == (1 << len(components))
    return (True, len(pairs), core, len(components), pairs)


def exhaustive_small():
    for n in range(1, 7):
        P = set_partitions(n)
        fibers = defaultdict(set)
        for E, F in product(P, repeat=2):
            fibers[operator(n, E, F)].add((frozenset(E), frozenset(F)))
        positive = 0
        for op, actual in fibers.items():
            ok, count, core, components, predicted = analyze(n, op)
            if ok:
                assert set(predicted) == actual, (n, core, count, len(actual))
                positive += 1
        print('EXHAUSTIVE_OK', n, 'partitions', len(P), 'operators', len(fibers),
              'two-core operators', positive)


def explicit_boundaries():
    W = set(range(3))
    C = [(frozenset((0, 1)), frozenset((0, 2))),
         (frozenset((0, 1)), frozenset((1, 2))),
         (frozenset((0, 2)), frozenset((1, 2)))]
    op = tuple(sum(1 << w for w in W
                   if any(A <= frozenset(i for i in W if mask & (1 << i)) for A in C[w]))
               for mask in range(8))
    ok, _, recovered, _, _ = analyze(3, op)
    assert not ok and recovered == C  # Odd-cycle incidence obstruction.
    # A disjoint union of two 2x2 grids has two independent color swaps.
    E = (frozenset((0, 1)), frozenset((2, 3)),
         frozenset((4, 5)), frozenset((6, 7)))
    F = (frozenset((0, 2)), frozenset((1, 3)),
         frozenset((4, 6)), frozenset((5, 7)))
    ok, count, _, c, pairs = analyze(8, operator(8, E, F))
    assert ok and c == 2 and count == 4
    assert len(set(frozenset((e, f)) for e, f in pairs)) == 2
    print('BOUNDARY_OK three-point-odd-cycle and eight-point-two-components')


if __name__ == '__main__':
    exhaustive_small()
    explicit_boundaries()
    print('ALL_CHECKS_OK')
