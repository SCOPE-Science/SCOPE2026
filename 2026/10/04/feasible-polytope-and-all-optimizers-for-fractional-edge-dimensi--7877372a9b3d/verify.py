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

def graph_data(parts):
    lab = labels(parts)
    n = len(lab)
    adj = [[v for v in range(n) if v != u and lab[v] != lab[u]] for u in range(n)]
    edges = [(u,v) for u in range(n) for v in adj[u] if u < v]
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
    return lab, edges, D

def resolving_neighborhood(e, f, D):
    u,v = e
    x,y = f
    n = len(D)
    out = []
    for z in range(n):
        de = min(D[z][u], D[z][v])
        df = min(D[z][x], D[z][y])
        if de != df:
            out.append(z)
    return tuple(out)

def solve_lp(n, neighborhoods):
    A = []
    b = []
    for R in neighborhoods:
        row = [0.0]*n
        for v in R:
            row[v] = -1.0
        A.append(row)
        b.append(-1.0)
    res = linprog([1.0]*n, A_ub=A, b_ub=b, bounds=[(0.0,1.0)]*n, method="highs")
    assert res.success
    return res.fun

def coordinate_range_at_optimum(n, neighborhoods, optimum, idx):
    A = []
    b = []
    for R in neighborhoods:
        row = [0.0]*n
        for v in R:
            row[v] = -1.0
        A.append(row)
        b.append(-1.0)
    # Force total weight equal to optimum, within numerical tolerance via equality.
    Aeq = [[1.0]*n]
    beq = [optimum]
    c = [0.0]*n
    c[idx] = 1.0
    lo = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq,
                 bounds=[(0.0,1.0)]*n, method="highs")
    c[idx] = -1.0
    hi = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq,
                 bounds=[(0.0,1.0)]*n, method="highs")
    assert lo.success and hi.success
    return lo.fun, -hi.fun

types = 0
edge_pairs = 0
coordinate_lps = 0
for N in range(3, 11):
    for r in range(2, N + 1):
        for parts in partitions(N, r):
            lab, edges, D = graph_data(parts)
            neighborhoods = []
            for e,f in combinations(edges,2):
                R = resolving_neighborhood(e,f,D)
                assert len(R) >= 2
                neighborhoods.append(R)
                edge_pairs += 1

            # Verify the exact small resolving neighborhoods that generate the
            # claimed reduced constraint system.
            if r >= 3:
                for x,y in combinations(range(N),2):
                    found = any(set(R) == {x,y} for R in neighborhoods)
                    assert found, (parts, x, y)
            else:
                for x,y in combinations(range(N),2):
                    if lab[x] == lab[y]:
                        found = any(set(R) == {x,y} for R in neighborhoods)
                        assert found, (parts, x, y)
                # Every full resolving neighborhood contains a constrained
                # same-part pair.
                for R in neighborhoods:
                    ok = any(lab[x] == lab[y] for x,y in combinations(R,2))
                    assert ok, (parts, R)

            val = solve_lp(N, neighborhoods)
            if r >= 3:
                target = N/2
            else:
                a,b = parts
                target = ((a/2 if a >= 3 else 1 if a == 2 else 0)
                          + (b/2 if b >= 3 else 1 if b == 2 else 0))
            assert abs(val-target) < 1e-8, (parts,val,target)

            # Check the full optimizer-coordinate ranges predicted by the theorem.
            for v in range(N):
                lo,hi = coordinate_range_at_optimum(N, neighborhoods, val, v)
                coordinate_lps += 2
                m = parts[lab[v]]
                if r >= 3 or m >= 3:
                    elo,ehi = 0.5,0.5
                elif m == 2:
                    elo,ehi = 0.0,1.0
                else:  # singleton part in the bipartite/star case
                    elo,ehi = 0.0,0.0
                assert abs(lo-elo) < 1e-7 and abs(hi-ehi) < 1e-7, (
                    parts,v,(lo,hi),(elo,ehi)
                )
            types += 1

print("VERIFY_OK")
print("multipartite_types_checked =", types)
print("edge_pairs_checked =", edge_pairs)
print("coordinate_optimization_LPs =", coordinate_lps)
print("orders = 3..10")
print("all exact reduced-constraint generators matched")
print("all original vertex-level LP optima matched")
print("all optimizer coordinate ranges matched")
