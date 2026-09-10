"""Exact Dhar / q-reduced divisor rank check for D0 on subdivided K3,3.

Model: K3,3 bipartition A={a0,a1,a2}, B={b0,b1,b2}. Each of 9 edges subdivided
into n segments (n even so edge-midpoints are vertices). D0 = sum of midpoints
of the 3 matching edges a_i-b_i.
Test: for every vertex q, D0 - q is equivalent to an effective divisor
(i.e. q-reduced representative has no negative entries).
Logs explicit firing scripts for replay.
"""
import json

def build_graph(n):
    # vertices: ('A',i), ('B',j), ('M',i,j,k) k=1..n-1 along edge a_i->b_j
    V = []
    idx = {}
    def add(v):
        if v not in idx:
            idx[v] = len(V); V.append(v)
    for i in range(3):
        add(('A', i))
    for j in range(3):
        add(('B', j))
    for i in range(3):
        for j in range(3):
            for k in range(1, n):
                add(('M', i, j, k))
    adj = {v: [] for v in V}
    def link(u, v):
        adj[u].append(v); adj[v].append(u)
    for i in range(3):
        for j in range(3):
            chain = [('A', i)] + [('M', i, j, k) for k in range(1, n)] + [('B', j)]
            for u, v in zip(chain[:-1], chain[1:]):
                link(u, v)
    return V, adj

def dhar_q_reduced(V, adj, D, q):
    """D: dict v->int. Returns (R, script) with R q-reduced equiv to D.
    Fires subsets S not containing q while legal. Records script."""
    D = dict(D)
    for v in V:
        D.setdefault(v, 0)
    script = []
    n = len(V)
    # safety bound on iterations
    for _ in range(100000):
        # find maximal fireable set: Dhar burning from q
        # burned = {q}; iteratively burn v if D[v] < # edges to burned set
        burned = {q}
        changed = True
        while changed:
            changed = False
            for v in V:
                if v in burned:
                    continue
                e_to_burned = sum(1 for w in adj[v] if w in burned)
                if D[v] < e_to_burned:
                    burned.add(v); changed = True
        S = [v for v in V if v not in burned]
        if not S:
            break
        Sset = set(S)
        # fire S: each v in S loses outdeg_S(v), each v not in S gains indeg
        newD = dict(D)
        for v in S:
            outdeg = sum(1 for w in adj[v] if w not in Sset)
            newD[v] -= outdeg
        for v in V:
            if v not in Sset:
                newD[v] += sum(1 for w in adj[v] if w in Sset)
        D = newD
        script.append(sorted(map(str, S)))
        if len(script) > 5000:
            raise RuntimeError("script too long")
    return D, script

def main():
    for n in [2, 4, 6]:
        V, adj = build_graph(n)
        # D0 midpoints of matching edges at k=n//2
        D0 = {v: 0 for v in V}
        for i in range(3):
            D0[('M', i, i, n // 2)] += 1
        assert sum(D0.values()) == 3
        fails = []
        total = 0
        maxscript = 0
        for q in V:
            D = dict(D0); D[q] -= 1
            R, script = dhar_q_reduced(V, adj, D, q)
            total += 1
            maxscript = max(maxscript, len(script))
            if any(c < 0 for c in R.values()):
                fails.append((str(q), {str(k): v for k, v in R.items() if v < 0}))
        print(f"n={n}: vertices={len(V)} tested={total} fails={len(fails)} maxscript={maxscript}")
        for f in fails[:10]:
            print("  FAIL", f)
    # detailed log for n=2 with scripts
    V, adj = build_graph(2)
    D0 = {v: 0 for v in V}
    for i in range(3):
        D0[('M', i, i, 1)] += 1
    log = {"n": 2, "vertices": [str(v) for v in V],
           "D0": {str(k): v for k, v in D0.items() if v},
           "results": []}
    for q in V:
        D = dict(D0); D[q] -= 1
        R, script = dhar_q_reduced(V, adj, D, q)
        ok = all(c >= 0 for c in R.values())
        log["results"].append({"q": str(q), "winnable": ok,
                               "n_fires": len(script),
                               "R": {str(k): v for k, v in R.items() if v != 0}})
    with open("output/artifacts/dhar_n2_log.json", "w") as f:
        json.dump(log, f, indent=1)
    print("wrote output/artifacts/dhar_n2_log.json")

if __name__ == "__main__":
    main()
