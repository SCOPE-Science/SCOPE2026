#!/usr/bin/env python3
from itertools import combinations, permutations
import sympy as sp

alpha = sp.symbols("alpha", real=True)
x = sp.symbols("x")

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

def adjacency_matrix(n, edges):
    A = sp.zeros(n)
    for u, v in edges:
        A[u, v] = 1
        A[v, u] = 1
    return A

def canonical_code(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    pairs = list(combinations(range(n), 2))
    best = None
    for p in permutations(range(n)):
        code = "".join(
            "1" if tuple(sorted((p[i], p[j]))) in E else "0"
            for i, j in pairs
        )
        if best is None or code < best:
            best = code
    return best

def connected_unlabeled_representatives(n):
    pairs = list(combinations(range(n), 2))
    reps = {}
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if (mask >> i) & 1]
        if len(edges) < n - 1 or not connected(n, edges):
            continue
        reps.setdefault(canonical_code(n, edges), edges)
    return list(reps.values())

def eigenvector_maximizers(n, edges):
    A = adjacency_matrix(n, edges)
    poly = sp.Poly(A.charpoly(x).as_expr(), x)
    rho = poly.real_roots()[-1]
    M = x * sp.eye(n) - A
    cof = []
    for i in range(n):
        cof_i = sp.factor(M.minor_submatrix(i, i).det()).subs(x, rho)
        cof.append(sp.simplify(cof_i))
    # For a connected graph, adj(rho I-A) is a positive multiple of vv^T.
    # Thus these principal cofactors are proportional to squared Perron entries.
    winners = []
    for i in range(n):
        if all(sp.sign(sp.simplify(cof[i] - cof[j])) >= 0 for j in range(n)):
            winners.append(i)
    return tuple(winners), rho, sp.factor(poly.as_expr())

def pagerank_expressions(n, edges):
    A = adjacency_matrix(n, edges)
    deg = [sum(int(A[i, j]) for j in range(n)) for i in range(n)]
    PT = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            if A[i, j]:
                PT[i, j] = sp.Rational(1, deg[j])
    rhs = sp.Rational(1, n) * (1 - alpha) * sp.ones(n, 1)
    p = (sp.eye(n) - alpha * PT).inv() * rhs
    return [sp.factor(sp.cancel(z)) for z in p]

def pair_roots_01(exprs):
    roots = set()
    for i, j in combinations(range(len(exprs)), 2):
        num = sp.together(exprs[i] - exprs[j]).as_numer_denom()[0]
        P = sp.Poly(num, alpha)
        if P.is_zero:
            continue
        for r in sp.real_roots(P):
            if bool(r > 0) and bool(r < 1):
                roots.add(r)
    return sorted(roots)

def unique_maximizer_at(exprs, value):
    vals = [sp.simplify(e.subs(alpha, value)) for e in exprs]
    winners = []
    for i, vi in enumerate(vals):
        if all(i == j or sp.sign(sp.simplify(vi - vj)) == 1
               for j, vj in enumerate(vals)):
            winners.append(i)
    return tuple(winners)

def check_graph_all_damping(n, edges):
    evmax, _, _ = eigenvector_maximizers(n, edges)
    pr = pagerank_expressions(n, edges)
    roots = pair_roots_01(pr)
    bounds = [sp.Integer(0)] + roots + [sp.Integer(1)]
    samples = [sp.simplify((l + r) / 2) for l, r in zip(bounds, bounds[1:])]
    # Root points are checked separately because a third coordinate could,
    # in principle, be the unique maximum at a crossing of two lower scores.
    samples += roots
    for z in samples:
        prmax = unique_maximizer_at(pr, z)
        if len(evmax) == 1 and len(prmax) == 1:
            assert evmax == prmax, (n, edges, z, evmax, prmax)

def positive_on_open_unit_interval(expr):
    num, den = sp.together(expr).as_numer_denom()
    roots = []
    for P in (sp.Poly(num, alpha), sp.Poly(den, alpha)):
        for r in sp.real_roots(P):
            if bool(r > 0) and bool(r < 1):
                roots.append(r)
    assert roots == []
    assert sp.sign(sp.simplify(expr.subs(alpha, sp.Rational(1, 2)))) == 1

counts = {}
for n in range(2, 6):
    reps = connected_unlabeled_representatives(n)
    counts[n] = len(reps)
    for edges in reps:
        check_graph_all_damping(n, edges)

assert counts == {2: 1, 3: 2, 4: 6, 5: 21}

# Sharp witness: a triangle on 3,4,5; a bridge 0-3; and leaves 1,2 at 0.
W = [(0,1),(0,2),(0,3),(3,4),(3,5),(4,5)]
evmax, rho, charpoly = eigenvector_maximizers(6, W)
assert evmax == (3,)
assert sp.sign(rho - 2) == 1
assert charpoly == x*(x + 1)*(x**4 - x**3 - 5*x**2 + 3*x + 4)

pr = pagerank_expressions(6, W)
expected = [
    (4*alpha**3 + 7*alpha**2 - 11*alpha - 6) /
        (2*(alpha + 3)*(4*alpha**2 - alpha - 6)),
    (3*alpha**2 + alpha - 6) /
        (2*(alpha + 3)*(4*alpha**2 - alpha - 6)),
    (3*alpha**2 + alpha - 6) /
        (2*(alpha + 3)*(4*alpha**2 - alpha - 6)),
    (4*alpha**3 + alpha**2 - 5*alpha - 6) /
        (2*(alpha + 3)*(4*alpha**2 - alpha - 6)),
    (alpha + 1)*(2*alpha - 3) /
        ((alpha + 3)*(4*alpha**2 - alpha - 6)),
    (alpha + 1)*(2*alpha - 3) /
        ((alpha + 3)*(4*alpha**2 - alpha - 6)),
]
for got, want in zip(pr, expected):
    assert sp.simplify(got - want) == 0

for j in range(1, 6):
    positive_on_open_unit_interval(sp.factor(pr[0] - pr[j]))

assert sp.simplify(sp.factor(pr[0] - pr[1]) - (
    2*alpha*(alpha**2 + alpha - 3) /
    ((alpha + 3)*(4*alpha**2 - alpha - 6))
)) == 0
assert sp.simplify(sp.factor(pr[0] - pr[3]) - (
    3*alpha*(alpha - 1) /
    ((alpha + 3)*(4*alpha**2 - alpha - 6))
)) == 0
assert sp.simplify(sp.factor(pr[0] - pr[4]) - (
    alpha*(4*alpha**2 + 3*alpha - 9) /
    (2*(alpha + 3)*(4*alpha**2 - alpha - 6))
)) == 0

print("VERIFY_OK")
print("connected_unlabeled_counts", counts)
print("witness_edges", W)
print("witness_eigenvector_max", evmax)
print("witness_perron_root", rho)
print("witness_charpoly", charpoly)
print("witness_pagerank_max_for_all_0_lt_alpha_lt_1", 0)
