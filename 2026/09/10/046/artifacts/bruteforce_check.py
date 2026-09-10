"""Independent brute-force check: is D0 - a0 linearly equivalent (on G2 model)
to any effective divisor of degree 2? Enumerate all effective E (deg 2) and test
whether D0 - a0 - E lies in the Laplacian lattice (exact rational solve).
Also corroborate with n=8 subdivision Dhar test.
"""
import itertools
import sys
sys.path.insert(0, 'output/artifacts')
from dhar_rank import build_graph, dhar_q_reduced
import json

def laplacian_matrix(V, adj):
    n = len(V)
    L = [[0]*n for _ in range(n)]
    for i, v in enumerate(V):
        L[i][i] = len(adj[v])
        for w in adj[v]:
            j = V.index(w)
            L[i][j] -= 1
    return L

def in_laplacian_lattice(L, d):
    """Exact rational Gaussian elimination: does L f = d have rational solution?
    (For Laplacian, rational solvability + sum(d)=0 implies integer solvability
    up to kernel; we verify by constructing integer solution via rounded check.)"""
    n = len(L)
    # augment, eliminate over Fractions
    from fractions import Fraction
    M = [[Fraction(L[i][j]) for j in range(n)] + [Fraction(d[i])] for i in range(n)]
    where = [-1]*n
    row = 0
    for col in range(n):
        piv = None
        for i in range(row, n):
            if M[i][col] != 0:
                piv = i; break
        if piv is None:
            continue
        M[row], M[piv] = M[piv], M[row]
        where[col] = row
        for i in range(n):
            if i != row and M[i][col] != 0:
                f = M[i][col]/M[row][col]
                for j in range(col, n+1):
                    M[i][j] -= f*M[row][j]
        row += 1
    for i in range(row, n):
        if M[i][n] != 0:
            return False, None
    sol = [Fraction(0)]*n
    for j in range(n):
        if where[j] != -1:
            sol[j] = M[where[j]][n]/M[where[j]][j]
    # check integer (up to additive constant): all differences integer
    diffs_ok = all((sol[j]-sol[0]).denominator == 1 for j in range(n))
    return True, (sol, diffs_ok)

V, adj = build_graph(2)
n = len(V)
L = laplacian_matrix(V, adj)
D0 = {v: 0 for v in V}
for i in range(3):
    D0[('M', i, i, 1)] += 1
a0 = ('A', 0)
base = [D0[v] - (1 if v == a0 else 0) for v in V]
assert sum(base) == 2
count = 0
winnable = []
verts = list(range(n))
effs = []
for i in verts:
    for j in range(i, n):
        effs.append((i, j))
print(f"testing {len(effs)} effective divisors of degree 2")
for (i, j) in effs:
    E = [0]*n; E[i] += 1; E[j] += 1
    d = [base[k]-E[k] for k in range(n)]
    assert sum(d) == 0
    ok, info = in_laplacian_lattice(L, d)
    count += 1
    if ok:
        # rational solution exists; check integrality
        sol, diffs_ok = info
        if diffs_ok:
            winnable.append((str(V[i]), str(V[j])))
print(f"winnable count (exact integer cert): {len(winnable)}")
for w in winnable[:10]:
    print("  WINNABLE", w)

# n=8 Dhar corroboration (finer metric sample incl. quarter/eighth points)
V8, adj8 = build_graph(8)
D08 = {v: 0 for v in V8}
for i in range(3):
    D08[('M', i, i, 4)] += 1
fails = 0
tested = 0
for q in V8:
    D = dict(D08); D[q] -= 1
    R, script = dhar_q_reduced(V8, adj8, D, q)
    tested += 1
    if any(c < 0 for c in R.values()):
        fails += 1
print(f"n=8: tested={tested} fails={fails}")
with open("output/artifacts/bruteforce_summary.json", "w") as f:
    json.dump({"n_vertices_G2": n, "n_effective_deg2_tested": len(effs),
               "winnable_exact": winnable, "n8_tested": tested, "n8_fails": fails}, f, indent=1)
print("wrote output/artifacts/bruteforce_summary.json")
