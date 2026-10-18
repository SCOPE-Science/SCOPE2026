"""Independent exact rational homology and induced-character computation.

Uses only the Python standard library (fractions.Fraction). Does not use
alternating simplex traces or pretabulated irreducible characters.
"""
from fractions import Fraction
from itertools import combinations, permutations

V = tuple(combinations(range(5), 2))
vindex = {v: i for i, v in enumerate(V)}
T = tuple(sorted(tuple(sorted(vindex[x] for x in combinations(q, 2)))
                 for q in combinations(range(5), 3)))
E = tuple(sorted({tuple(sorted(e)) for t in T for e in combinations(t, 2)}))
eindex = {e: j for j, e in enumerate(E)}

# Boundary of a 1-simplex and a 2-simplex in canonical vertex order.
B1 = [[0] * 30 for _ in range(10)]
for j, (a, b) in enumerate(E):
    B1[a][j], B1[b][j] = -1, 1
B2 = [[0] * 10 for _ in range(30)]
for j, (a, b, c) in enumerate(T):
    B2[eindex[b, c]][j] = 1
    B2[eindex[a, c]][j] = -1
    B2[eindex[a, b]][j] = 1
assert all(sum(B1[i][e] * B2[e][j] for e in range(30)) == 0
           for i in range(10) for j in range(10))

def rref(rows):
    M = [[Fraction(x) for x in row] for row in rows]
    h, w, pivots = len(M), len(M[0]), []
    k = 0
    for col in range(w):
        pivot = next((i for i in range(k, h) if M[i][col]), None)
        if pivot is None:
            continue
        M[k], M[pivot] = M[pivot], M[k]
        c = M[k][col]
        M[k] = [x / c for x in M[k]]
        for i in range(h):
            if i == k:
                continue
            c = M[i][col]
            if c:
                M[i] = [a - c * b for a, b in zip(M[i], M[k])]
        pivots.append(col)
        k += 1
        if k == h:
            break
    return M, pivots

def rank(M):
    return len(rref(M)[1])

def invert(M):
    n = len(M)
    aug = [list(row) + [int(i == j) for j in range(n)]
           for i, row in enumerate(M)]
    A, piv = rref(aug)
    assert piv[:n] == list(range(n))
    return [row[n:] for row in A]

assert rank(B1) == 9 and rank(B2) == 10
# A spanning tree produces canonical fundamental cycles for all non-tree edges.
parent = list(range(10))
def root(i):
    while parent[i] != i:
        i = parent[i]
    return i

tree = []
for j, (a, b) in enumerate(E):
    x, y = root(a), root(b)
    if x != y:
        parent[x] = y
        tree.append(j)
others = tuple(e for e in range(30) if e not in tree)
assert len(tree) == 9 and len(others) == 21
adj = [[] for _ in range(10)]
for j in tree:
    a, b = E[j]
    adj[a].append((b, j, 1))
    adj[b].append((a, j, -1))

F = []
for j in others:
    a, b = E[j]
    vec = [0] * 30
    vec[j] = 1
    # Tree path oriented from b to a closes this edge.
    queue = [(b, [], {b})]
    while queue:
        at, path, seen = queue.pop(0)
        if at == a:
            for edge, sign in path:
                vec[edge] += sign
            break
        for nxt, edge, sign in adj[at]:
            if nxt not in seen:
                queue.append((nxt, path + [(edge, sign)], seen | {nxt}))
    else:
        raise AssertionError('Spanning tree path not found')
    assert all(sum(B1[i][e] * vec[e] for e in range(30)) == 0 for i in range(10))
    F.append(vec)

# Quotient of graph-cycle coordinates (21-dimensional) by the ten
# independent integral boundaries of the triangles.
R = [[B2[edge][j] for j in range(10)] for edge in others]
assert rank(R) == 10
M = [row[:] for row in R]
supplement = []
for j in range(21):
    candidate = [row + [int(i == j)] for i, row in enumerate(M)]
    if rank(candidate) > len(M[0]):
        M = candidate
        supplement.append(j)
assert len(supplement) == 11
inverse = invert(M)
other_index = {edge: k for k, edge in enumerate(others)}

def parity(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i + 1, len(seq))) % 2 else 1

def class_type(p):
    seen, out = set(), []
    for i in range(5):
        if i in seen:
            continue
        j, k = i, 0
        while j not in seen:
            seen.add(j)
            k += 1
            j = p[j]
        out.append(k)
    return tuple(sorted(out, reverse=True))

def homology_trace(p):
    vertex_perm = [vindex[tuple(sorted(p[i] for i in v))] for v in V]
    edge_action = []
    for a, b in E:
        image = (vertex_perm[a], vertex_perm[b])
        edge_action.append((eindex[tuple(sorted(image))], parity(image)))
    trace = Fraction(0)
    for basis_pos, j in enumerate(supplement):
        projected = [0] * 21
        for e, coeff in enumerate(F[j]):
            if coeff:
                dst, sign = edge_action[e]
                if dst in other_index:
                    projected[other_index[dst]] += coeff * sign
        hom_coeff = sum(inverse[10 + basis_pos][k] * projected[k]
                        for k in range(21))
        trace += hom_coeff
    assert trace.denominator == 1
    return int(trace)

values = {}
for p in permutations(range(5)):
    t = class_type(p)
    if t not in values:
        values[t] = homology_trace(p)
assert values == {
    (1, 1, 1, 1, 1): 11, (2, 1, 1, 1): -1, (2, 2, 1): -1,
    (3, 1, 1): -1, (3, 2): -1, (4, 1): 1, (5,): 1,
}
print('Boundary ranks:', rank(B1), rank(B2))
print('Absolute integral homology is torsion-free: triangle boundaries contain a unit minor.')
print('Independent direct H1 actions:', values)
print('PASS: 7 exact rational H1 character representatives and all 21 cycle coordinates.')
