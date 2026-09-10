"""Replayable certificate: rank(D0) = 0 on unit K3,3, refuting the target's rank-1 clause.

Method (independent of dhar_rank.py brute force): step-by-step Dhar burning
from q=a0 on model G2 (each K3,3 edge subdivided once; all metric edges length
1/2; D0 and q supported on vertices, so vertex-set fires capture metric fires
and the burning below is also a valid metric-graph burning trace).

Certificate content:
 1. G2 sanity: 6 original vertices + 9 midpoints = 15 vertices; trivalent
    originals; genus b1 = E-V+1 = 4.
 2. Burning log from a0 for divisor D0 - a0, each burn justified by
    D[v] < #{edges from v to already-burned set}.
 3. Whole graph burns => D0 - a0 is a0-reduced with value -1 at a0
    => D0 - a0 not equivalent to any effective divisor (metric Baker-Norine /
    Luo reduced-divisor criterion) => rank(D0) <= 0 => rank(D0) = 0 (effective).
"""
import json

A = [('A', i) for i in range(3)]
B = [('B', j) for j in range(3)]
M = {(i, j): ('M', i, j) for i in range(3) for j in range(3)}
V = A + B + list(M.values())
adj = {v: [] for v in V}
for i in range(3):
    for j in range(3):
        for u, v in [[('A', i), M[(i, j)]], [M[(i, j)], ('B', j)]]:
            adj[u].append(v)
            adj[v].append(u)

E = sum(len(n) for n in adj.values()) // 2
V0 = 6
g = E - len(V) + 1
assert len(V) == 15 and E == 18 and g == 4, (len(V), E, g)
assert all(len(adj[v]) == 3 for v in A + B)
assert all(len(adj[v]) == 2 for v in M.values())

D0 = {v: 0 for v in V}
for i in range(3):
    D0[M[(i, i)]] = 1
assert sum(D0.values()) == 3
q = ('A', 0)
D = dict(D0)
D[q] -= 1

burned = {q}
log = [{"burned": str(q), "reason": "origin q (D[q] = -1 < 0)"}]
order = [q]
while True:
    progressed = False
    for v in V:
        if v in burned:
            continue
        e = sum(1 for w in adj[v] if w in burned)
        if D[v] < e:
            burned.add(v)
            order.append(v)
            log.append({"burned": str(v), "D": D[v],
                        "edges_to_burned": e,
                        "burned_neighbors": sorted(str(w) for w in adj[v] if w in burned)})
            progressed = True
    if not progressed:
        break

unburned = [v for v in V if v not in burned]
result = {
    "genus": g, "n_vertices": len(V), "n_edges": E,
    "D0_support": sorted(str(v) for v in V if D0[v]),
    "q": str(q),
    "n_burned": len(burned), "n_unburned": len(unburned),
    "unburned": sorted(map(str, unburned)),
    "burn_order": [str(v) for v in order],
    "burn_log": log,
    "R_at_q": D[q],
    "conclusion": ("WHOLE_GRAPH_BURNS: D0-a0 is a0-reduced with R(a0)=-1, "
                   "hence not effective-equivalent; rank(D0)=0, NOT 1. TARGET REFUTED.")
    if not unburned else "INCOMPLETE: graph did not fully burn",
}
with open("output/artifacts/verify_disproof.json", "w") as f:
    json.dump(result, f, indent=1)
print(f"burned {len(burned)}/{len(V)}; unburned={unburned}")
print("VERIFY_OK" if not unburned and D[q] == -1 else "VERIFY_FAIL")
