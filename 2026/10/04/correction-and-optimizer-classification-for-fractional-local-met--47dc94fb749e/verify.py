from itertools import combinations
from collections import deque
from scipy.optimize import linprog

def partitions(n, r, lo=1):
    if r == 0:
        if n == 0:
            yield ()
        return
    for x in range(lo, n + 1):
        if n - x < x * (r - 1):
            break
        for q in partitions(n - x, r - 1, x):
            yield (x,) + q

def labels(parts):
    out = []
    for i, a in enumerate(parts):
        out += [i] * a
    return out

def distances(lab):
    n = len(lab)
    adj = [[j for j in range(n) if j != i and lab[j] != lab[i]] for i in range(n)]
    D = [[10**9]*n for _ in range(n)]
    for s in range(n):
        D[s][s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if D[s][v] == 10**9:
                    D[s][v] = D[s][u] + 1
                    q.append(v)
    return adj, D

def local_neighborhoods(parts):
    lab = labels(parts)
    adj, D = distances(lab)
    n = len(lab)
    rows = []
    edges = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                edges += 1
                row = [1 if D[x][u] != D[x][v] else 0 for x in range(n)]
                expected = [1 if lab[x] in (lab[u], lab[v]) else 0 for x in range(n)]
                assert row == expected, (parts, u, v, row, expected)
                rows.append(row)
    return rows, edges

def solve_lp(rows, n):
    res = linprog(
        c=[1.0]*n,
        A_ub=[[-float(a) for a in row] for row in rows],
        b_ub=[-1.0]*len(rows),
        bounds=[(0.0, 1.0)]*n,
        method="highs",
    )
    assert res.success
    return res.fun, res.x

types = edges = 0
for N in range(2, 11):
    for r in range(2, N + 1):
        for parts in partitions(N, r):
            rows, e = local_neighborhoods(parts)
            val, x = solve_lp(rows, N)
            target = 1.0 if r == 2 else r/2.0
            assert abs(val - target) < 1e-8, (parts, val, target)

            # Check the explicit constructions used in the proof.
            lab = labels(parts)
            if r == 2:
                f = [0.0]*N
                f[0] = 1.0
            else:
                f = [1.0/(2.0*parts[lab[v]]) for v in range(N)]
            for row in rows:
                assert sum(f[v]*row[v] for v in range(N)) >= 1.0 - 1e-10

            types += 1
            edges += e

# Explicit contradiction witness to the published k-1 formula:
# K_3 has k=3 and the feasible function f(v)=1/2 on all vertices.
rows, _ = local_neighborhoods((1,1,1))
witness = [0.5,0.5,0.5]
assert all(sum(witness[v]*row[v] for v in range(3)) >= 1 for row in rows)
assert abs(sum(witness) - 1.5) < 1e-12

print("VERIFY_OK")
print("multipartite_types_checked =", types)
print("edge_local_neighborhoods_checked =", edges)
print("orders = 2..10")
print("all direct local-resolving neighborhoods matched endpoint-part unions")
print("all LP optima matched 1 for two parts and k/2 for k>=3")
print("K3 explicit feasible witness weight = 3/2")
