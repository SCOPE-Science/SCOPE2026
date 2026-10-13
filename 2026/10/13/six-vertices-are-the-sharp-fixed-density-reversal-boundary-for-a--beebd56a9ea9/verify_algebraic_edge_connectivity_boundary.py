#!/usr/bin/env python3
from itertools import combinations, permutations
import sympy as sp

X = sp.symbols("x")

def connected(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n

def canonical_code(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    best = None
    for p in permutations(range(n)):
        bits = []
        for i, j in combinations(range(n), 2):
            bits.append("1" if tuple(sorted((p[i], p[j]))) in E else "0")
        s = "".join(bits)
        if best is None or s < best:
            best = s
    return best

def edge_connectivity(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    best = len(E)
    # Every nontrivial cut appears once with vertex 0 on the chosen side.
    for mask in range(1 << (n - 1)):
        S = {0}
        for i in range(1, n):
            if mask & (1 << (i - 1)):
                S.add(i)
        if len(S) == n:
            continue
        cut = sum((u in S) != (v in S) for u, v in E)
        if cut < best:
            best = cut
    return best

def laplacian_charpoly_and_a(n, edges):
    L = sp.zeros(n)
    for u, v in edges:
        L[u, u] += 1
        L[v, v] += 1
        L[u, v] -= 1
        L[v, u] -= 1
    poly = sp.Poly(L.charpoly(X).as_expr(), X)
    roots = poly.real_roots()
    assert len(roots) == n
    return roots[1], sp.factor(poly.as_expr())

# Exhaustive lower-order census, quotienting labeled graphs by isomorphism.
classes = {}
for n in range(2, 6):
    poss = list(combinations(range(n), 2))
    reps = {}
    for mask in range(1 << len(poss)):
        edges = [poss[i] for i in range(len(poss)) if (mask >> i) & 1]
        if len(edges) < n - 1 or not connected(n, edges):
            continue
        reps.setdefault(canonical_code(n, edges), edges)
    classes[n] = list(reps.values())

assert {n: len(v) for n, v in classes.items()} == {2: 1, 3: 2, 4: 6, 5: 21}

# No same-order, same-size strict reversal through five vertices.
for n, graphs in classes.items():
    records = []
    for edges in graphs:
        a, poly = laplacian_charpoly_and_a(n, edges)
        lam = edge_connectivity(n, edges)
        records.append((len(edges), a, lam, edges, poly))
    for r1, r2 in combinations(records, 2):
        if r1[0] != r2[0] or r1[2] == r2[2]:
            continue
        reversal = (
            (r1[1] > r2[1] and r1[2] < r2[2])
            or
            (r2[1] > r1[1] and r2[2] < r1[2])
        )
        assert not reversal, (n, r1, r2)

# Six-vertex, seven-edge witness.
A = [(0,4),(1,3),(1,4),(2,3),(2,4),(3,4),(4,5)]
B = [(0,2),(0,5),(1,3),(1,4),(2,3),(3,4),(3,5)]

assert connected(6, A) and connected(6, B)
assert len(A) == len(B) == 7

aA, pA = laplacian_charpoly_and_a(6, A)
aB, pB = laplacian_charpoly_and_a(6, B)
eA = edge_connectivity(6, A)
eB = edge_connectivity(6, B)

assert sp.factor(pA) == X*(X - 6)*(X - 4)*(X - 2)*(X - 1)**2
assert sp.factor(pB) == X*(X - 3)**2*(X - 2)*(X**2 - 6*X + 4)
assert aA == 1
assert aB == 3 - sp.sqrt(5)
assert eA == 1
assert eB == 2
assert aA > aB and eA < eB

print("VERIFY_OK")
print("connected_unlabeled_counts", {n: len(v) for n, v in classes.items()})
print("A_algebraic_connectivity", aA)
print("A_edge_connectivity", eA)
print("A_charpoly", pA)
print("B_algebraic_connectivity", aB)
print("B_edge_connectivity", eB)
print("B_charpoly", pB)
