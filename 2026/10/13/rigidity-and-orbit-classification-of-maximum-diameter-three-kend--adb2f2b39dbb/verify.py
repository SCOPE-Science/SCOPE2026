#!/usr/bin/env python3
"""Finite cross-checks for diameter-three Kendall-tau anticode rigidity.

The all-length theorem is proved mathematically in RESULT.md; no finite
computation is used as a substitute for its universal quantifier.
"""
import itertools
from collections import Counter, deque
from math import factorial


def check(n):
    perms = list(itertools.permutations(range(n)))
    size = len(perms)
    where = {p: i for i, p in enumerate(perms)}
    pos_reversal = tuple(range(n - 1, -1, -1))
    signs = []
    for p in perms:
        pos = [0] * n
        for i, x in enumerate(p):
            pos[x] = i
        signs.append(sum(
            (int(pos[a] > pos[b]) << k)
            for k, (a, b) in enumerate(itertools.combinations(range(n), 2))
        ))
    swap_neighbors = []
    for p in perms:
        swap_neighbors.append([
            where[p[:i] + (p[i+1], p[i]) + p[i+2:]]
            for i in range(n - 1)
        ])
    dist = [[-1] * size for _ in range(size)]
    for i in range(size):
        drow = dist[i]
        drow[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in swap_neighbors[u]:
                if drow[v] == -1:
                    drow[v] = drow[u] + 1
                    q.append(v)
        for j in range(size):
            assert drow[j] == (signs[i] ^ signs[j]).bit_count()

    adj = [0] * size
    for i in range(size):
        for j in range(i + 1, size):
            if dist[i][j] <= 3:
                adj[i] |= 1 << j
                adj[j] |= 1 << i

    # Exact maximal-clique traversal, without early pruning.
    maximum = 0
    max_cliques = set()
    def bronk(R, P, X):
        nonlocal maximum, max_cliques
        if P == 0 and X == 0:
            count = R.bit_count()
            if count > maximum:
                maximum = count
                max_cliques = {R}
            elif count == maximum:
                max_cliques.add(R)
            return
        union = P | X
        if union:
            pivot = max(
                (u for u in range(size) if (union >> u) & 1),
                key=lambda u: (P & adj[u]).bit_count()
            )
            options = P & ~adj[pivot]
        else:
            options = P
        while options:
            bit = options & -options
            v = bit.bit_length() - 1
            bronk(R | bit, P & adj[v], X & adj[v])
            P ^= bit
            X |= bit
            options ^= bit
    bronk(0, (1 << size) - 1, 0)
    assert maximum == 2 * (n - 1)

    # Reconstruct all distinct double balls from graph edges.
    balls = [sum(1 << j for j in range(size) if dist[i][j] <= 1) for i in range(size)]
    from_edges = set()
    edge_by_code = {}
    for i in range(size):
        for j in swap_neighbors[i]:
            if i < j:
                c = balls[i] | balls[j]
                assert c.bit_count() == maximum
                from_edges.add(c)
                assert c not in edge_by_code  # uniqueness of centers
                edge_by_code[c] = (i, j)
    assert from_edges == max_cliques
    assert len(from_edges) == factorial(n) * (n - 1) // 2

    # Independent orbit generation: all label permutations and positional reversal.
    left_actions = list(itertools.permutations(range(n)))
    transforms = []
    for labeling in left_actions:
        for reverse in (False, True):
            transforms.append(tuple(
                where[tuple(labeling[a] for a in (p[::-1] if reverse else p))]
                for p in perms
            ))
    assert len(transforms) == 2 * factorial(n)
    remaining = set(from_edges)
    orbit_sizes = []
    stabilizers = []
    while remaining:
        c = min(remaining)
        members = [i for i in range(size) if c >> i & 1]
        orbit = set()
        for tr in transforms:
            mapped = sum(1 << tr[i] for i in members)
            assert mapped in from_edges
            orbit.add(mapped)
        orbit_sizes.append(len(orbit))
        stabilizers.append(len(transforms) // len(orbit))
        remaining -= orbit
    orbit_sizes.sort()
    stabilizers.sort()
    expected_orbits = (
        [factorial(n)] * ((n-1)//2)
        if n % 2 else
        [factorial(n) // 2] + [factorial(n)] * ((n-2)//2)
    )
    assert orbit_sizes == sorted(expected_orbits)
    assert sum(orbit_sizes) == len(from_edges)
    print('N', n, 'ambient', size, 'maximum', maximum,
          'labeled_maxima', len(max_cliques),
          'orbits', ','.join(map(str, orbit_sizes)),
          'stabilizers', ','.join(map(str, stabilizers)),
          'all_equal_double_balls', True)


def rank_two_local_check(n):
    permutations = list(itertools.permutations(range(n)))
    inversion_sets = set()
    for p in permutations:
        pos = {a: k for k, a in enumerate(p)}
        inv = frozenset(
            (a, b) for a in range(n) for b in range(a + 1, n)
            if pos[a] > pos[b]
        )
        if len(inv) == 2:
            inversion_sets.add(inv)
    expected = set()
    for i in range(n - 1):
        for j in range(i + 2, n - 1):
            expected.add(frozenset({(i,i+1),(j,j+1)}))
    for i in range(n - 2):
        expected.add(frozenset({(i,i+1),(i,i+2)}))
        expected.add(frozenset({(i,i+2),(i+1,i+2)}))
    assert inversion_sets == expected
    e = {(i, i+1) for i in range(n - 1)}
    h = {(i, i+2) for i in range(n - 2)}
    degrees = {v: sum(v in s for s in expected) for v in e | h}
    assert all(degrees[v] == n - 2 for v in e)
    assert all(degrees[v] == 2 for v in h)
    print('RANK2', n, 'inversion_patterns', len(expected), 'local_degrees', 'verified')


for n in (5,6,7):
    rank_two_local_check(n)
for n in (5,6):
    check(n)
print('VERIFY_OK n5_max=8 n5_count=240 n6_max=10 n6_count=1800 rank2_n5_to_n7=true')
