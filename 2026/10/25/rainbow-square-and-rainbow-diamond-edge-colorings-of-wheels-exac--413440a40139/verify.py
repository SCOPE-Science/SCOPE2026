"""Direct exhaustive checks of rainbow C4 and rainbow diamond edge-colorings of wheel graphs.
The checker constructs the actual graph and the complete edge-pair conflict relations.
"""
from itertools import combinations, permutations, product
from math import factorial


def graph(n):
    assert n >= 3
    vertices = tuple(range(n + 1))
    edges = sorted({tuple(sorted(pair)) for i in range(n)
                    for pair in ((n, i), (i, (i + 1) % n))})
    return vertices, edges


def constraints(n, kind):
    vertices, edges = graph(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    conflicts = {tuple(sorted((i, j))) for i, j in combinations(range(len(edges)), 2)
                 if set(edges[i]).intersection(edges[j])}
    small_subgraphs = set()
    for four in combinations(vertices, 4):
        four_edges = tuple(edge for edge in edges if set(edge).issubset(four))
        if kind == 'D':
            # Every five-edge selection spanning a K4-e, even inside an induced K4.
            for sub in combinations(four_edges, 5):
                # The five edges of K4-e necessarily form a diamond.
                small_subgraphs.add(frozenset(sub))
        else:
            # Enumerate all 4-cycle edge sets without assuming a wheel structure.
            for perm in permutations(four):
                sub = frozenset(tuple(sorted((perm[i], perm[(i + 1) % 4])))
                                for i in range(4))
                if sub.issubset(edge_index):
                    small_subgraphs.add(sub)
    for sub in small_subgraphs:
        ix = sorted(edge_index[e] for e in sub)
        conflicts.update(combinations(ix, 2))
    return edges, conflicts, len(small_subgraphs)


def is_valid(colors, conflicts):
    return all(colors[a] != colors[b] for a, b in conflicts)


def transfer_count(n):
    size = n - 4
    T = [[int(i != j + 1) for j in range(size)] for i in range(size)]
    Z = [[int(i == j) for j in range(size)] for i in range(size)]
    for _ in range(n):
        Z = [[sum(Z[i][a] * T[a][j] for a in range(size))
              for j in range(size)] for i in range(size)]
    return sum(Z[i][i] for i in range(size))


def direct_normalized_census(n, kind):
    edges, conflict, _ = constraints(n, kind)
    indices = {edge: j for j, edge in enumerate(edges)}
    spoke = [indices[tuple(sorted((n, i)))] for i in range(n)]
    rim = [indices[tuple(sorted((i, (i+1) % n)))] for i in range(n)]
    colors = [None] * len(edges)
    for i, j in enumerate(spoke):
        colors[j] = i
    allowed = [tuple(v for v in range(n)
                     if all(colors[j] != v for j in spoke
                            if tuple(sorted((j, rim[i]))) in conflict))
               for i in range(n)]
    accepted = 0
    for choices in product(*allowed):
        for i, j in enumerate(rim):
            colors[j] = choices[i]
        if is_valid(colors, conflict):
            accepted += 1
    return accepted, allowed


assert len(constraints(3, 'B')[1]) == len(constraints(3, 'D')[1]) == 15
assert len(constraints(4, 'B')[1]) == 28
D4_edges, D4_conflict, D4_diamonds = constraints(4, 'D')
assert len(D4_edges) == 8 and len(D4_conflict) == 26, (len(D4_conflict),D4_diamonds)
# Precisely the two opposite rim-edge pairs can reuse colors.
assert D4_diamonds == 4
for n in range(5, 13):
    E_B, C_B, num_4cyc = constraints(n, 'B')
    E_D, C_D, num_diam = constraints(n, 'D')
    assert E_B == E_D and C_B == C_D
    assert num_4cyc == num_diam == n

for n in range(5, 9):
    got_B, allowed_B = direct_normalized_census(n, 'B')
    got_D, allowed_D = direct_normalized_census(n, 'D')
    expected = transfer_count(n)
    assert got_B == got_D == expected, (n, got_B, got_D, expected)
    assert all(len(a) == n-4 for a in allowed_B)
    assert allowed_B == allowed_D
    print('n=%d normalized=%d named=%d' % (n, expected, factorial(n)*expected))

for n in range(5, 16):
    edges, C_B, _ = constraints(n, 'B')
    indices = {edge: k for k, edge in enumerate(edges)}
    colors = [None] * len(edges)
    for i in range(n):
        colors[indices[tuple(sorted((n, i)))]] = i
        colors[indices[tuple(sorted((i, (i+1) % n)))]] = (i+3)%n
    assert is_valid(colors, C_B)

# At n=4, alternating two fresh rim colors satisfy D, while four fresh rim colors are necessary for B.
indices = {edge: k for k, edge in enumerate(D4_edges)}
colors = [None] * 8
for i in range(4):
    colors[indices[tuple(sorted((4, i)))]] = i
    colors[indices[tuple(sorted((i,(i+1)%4)))]] = 4 + i%2
assert is_valid(colors, D4_conflict)
assert not is_valid(colors, constraints(4, 'B')[1])
print('VERIFY_OK B/D direct graph conflicts, finite normalized census, transfer matrix, constructions')
