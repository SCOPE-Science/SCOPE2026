"""Exact finite scope check for indicated total domination on trees of at most 6 vertices.
Only the standard Python library is needed.  No random sampling.
"""
from functools import lru_cache
from itertools import product
from heapq import heapify, heappop, heappush


def edges_from_prufer(seq, n):
    degrees = [1] * n
    for u in seq:
        degrees[u] += 1
    leaves = [i for i in range(n) if degrees[i] == 1]
    heapify(leaves)
    edges = []
    for u in seq:
        v = heappop(leaves)
        edges.append((v, u))
        degrees[v] -= 1
        degrees[u] -= 1
        if degrees[u] == 1:
            heappush(leaves, u)
    a = heappop(leaves)
    b = heappop(leaves)
    edges.append((a, b))
    return edges


def unrooted_code(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    def root_code(v, parent):
        return '(' + ''.join(sorted(root_code(w, v) for w in adj[v] if w != parent)) + ')'
    return min(root_code(v, -1) for v in range(n))


def game_values(n, edges):
    adj = [0] * n
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    full = (1 << n) - 1
    covered = [0] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        covered[mask] = covered[mask ^ bit] | adj[bit.bit_length() - 1]
    @lru_cache(maxsize=None)
    def g(played, declared):
        currently = covered[played] | declared
        if currently == full:
            return 0
        # Minimax induction. Each move adds one previously unplayed neighbor.
        return 1 + min(
            max(g(played | (1 << u), declared)
                for u in range(n) if adj[v] & (1 << u))
            for v in range(n) if not (currently & (1 << v))
        )
    return [g(0, d) for d in range(1 << n)]


def bad_pairs(vals):
    result = []
    for a in range(len(vals)):
        b = a
        while True:
            if vals[a] > vals[b]:
                result.append((b, a, vals[b], vals[a]))
            if b == 0:
                break
            b = (b - 1) & a
    return result


def one_example(n, edges):
    vals = game_values(n, edges)
    return vals[0], bad_pairs(vals)


def run():
    canonical = {}
    for n in range(2, 7):
        representations = {}
        for seq in product(range(n), repeat=n-2):
            edges = edges_from_prufer(seq, n)
            code = unrooted_code(n, edges)
            representations.setdefault(code, edges)
        classes = len(representations)
        violations = []
        for code, edges in sorted(representations.items()):
            base, bad = one_example(n, edges)
            if bad:
                violations.append((code, edges, base, len(bad), bad[0]))
        canonical[n] = classes
        print('n=%d labeled_trees=%d isomorphism_classes=%d violating_classes=%d' %
              (n, n**(n-2), classes, len(violations)))
        if n <= 5:
            assert not violations
        if n == 6:
            assert classes == 6 and len(violations) == 1
            print('six_vertex_unique_bad', violations[0])
            witness_edges = [(0,1), (1,2), (2,3), (3,4), (2,5)]
            expect = unrooted_code(6, witness_edges)
            assert violations[0][0] == expect
            val = game_values(6, witness_edges)
            assert val[0] == 3 and val[1<<5] == 4
    assert canonical == {2:1, 3:1, 4:2, 5:3, 6:6}
    # Additional unbounded-family small-case assertions, not used for infinite proof.
    for r in range(0,8):
        edges = [(0,1),(1,2),(2,3),(3,4),(2,5)] + [(1,6+i) for i in range(r)]
        full_declared = 1 << 5
        vals = game_values(6+r, edges)
        assert vals[0] == 3 and vals[full_declared] == 4
        print('family_r=%d vertices=%d ordinary=%d declared=%d' %
              (r,6+r,vals[0],vals[full_declared]))
    print('CHECKS_PASSED')

if __name__ == '__main__':
    run()
