"""Self-contained verifier for the 37-graph maximality finding (lane-1142).

Reproves: each graph in r46data.g6 on 35 vertices is K4-free with alpha<=5,
and admits NO single-vertex extension to a Ramsey(4,6;36) graph, because no
triangle-free vertex set meets all independent 5-sets (exhaustive fail-first
branch-and-bound). Run: python3 verify_maximality.py  (expects r46data.g6 in
the lane root; also works if copied next to this script). ~20 s total.
"""
import sys, os, time

def find_ledger():
    for p in ['r46data.g6', '../r46data.g6', '../../r46data.g6',
              os.path.join(os.path.dirname(__file__), 'r46data.g6')]:
        if os.path.exists(p):
            return p
    # workspace fallback
    root = '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1142/r46data.g6'
    return root

def parse_g6(line, n_expected=35):
    line = line.strip()
    n = ord(line[0]) - 63
    assert n == n_expected, n
    bits = []
    for ch in line[1:]:
        v = ord(ch) - 63
        for k in range(5, -1, -1):
            bits.append((v >> k) & 1)
    bits = bits[:n * (n - 1) // 2]
    adj = [[0] * n for _ in range(n)]
    idx = 0
    for j in range(1, n):
        for i in range(j):
            b = bits[idx]; idx += 1
            adj[i][j] = adj[j][i] = b
    return adj

def count_K4(adj):
    n = len(adj); c = 0
    for a in range(n):
        for b in range(a + 1, n):
            if adj[a][b]:
                for cc in range(b + 1, n):
                    if adj[a][cc] and adj[b][cc]:
                        # count c<d pairs below; full K4 count via edge pairs
                        pass
    # exact K4 count
    c = 0
    nm = []
    for i in range(n):
        m = 0
        for j in range(n):
            if adj[i][j]:
                m |= (1 << j)
        nm.append(m)
    for a in range(n):
        for b in range(a + 1, n):
            if adj[a][b]:
                cn = nm[a] & nm[b]
                cl = [cc for cc in range(b + 1, n) if (cn >> cc) & 1]
                for i in range(len(cl)):
                    for j in range(i + 1, len(cl)):
                        if adj[cl[i]][cl[j]]:
                            c += 1
    return c

def has_indep6(adj):
    n = len(adj); found = [False]
    sys.setrecursionlimit(100000)
    def dfs(cands, depth):
        if found[0]:
            return True
        if depth == 6:
            found[0] = True
            return True
        if len(cands) < 6 - depth:
            return False
        for idx in range(len(cands)):
            if len(cands) - idx < 6 - depth:
                break
            v = cands[idx]
            av = adj[v]
            new = [u for u in cands[idx+1:] if not av[u]]
            if dfs(new, depth + 1):
                return True
        return False
    dfs(list(range(n)), 0)
    return found[0]

def all_indep5(adj):
    out = []
    def rec(cands, chosen):
        if len(chosen) == 5:
            out.append(tuple(chosen)); return
        need = 5 - len(chosen); L = len(cands)
        if L < need:
            return
        for idx in range(L):
            if L - idx < need:
                break
            v = cands[idx]; av = adj[v]
            new = [u for u in cands[idx+1:] if not av[u]]
            chosen.append(v); rec(new, chosen); chosen.pop()
    rec(list(range(len(adj))), [])
    return out

def prove_no_extension(adj, fams):
    n = len(adj); N = len(fams)
    F = [set(f) for f in fams]
    contains = [[] for _ in range(n)]
    for i, f in enumerate(F):
        for v in f:
            contains[v].append(i)
    nm = [0]*n
    for i in range(n):
        b = 0
        for j in range(n):
            if adj[i][j]:
                b |= (1 << j)
        nm[i] = b
    sys.setrecursionlimit(100000)
    nodes = [0]
    def forms_tri(S_mask, v):
        inter = S_mask & nm[v]
        while inter:
            lsb = inter & (-inter)
            a = lsb.bit_length() - 1
            if nm[a] & inter:
                return True
            inter ^= lsb
        return False
    full = (1 << N) - 1
    vcov = [0]*n
    for i, f in enumerate(fams):
        for v in f:
            vcov[v] |= (1 << i)
    def rec(S_mask, covered):
        nodes[0] += 1
        if covered == full:
            return S_mask
        best_opts = None
        for idx in range(N):
            if not (covered >> idx) & 1:
                opts = [v for v in F[idx] if not (S_mask >> v) & 1 and not forms_tri(S_mask, v)]
                if not opts:
                    return None
                if best_opts is None or len(opts) < len(best_opts):
                    best_opts = opts
                    if len(opts) == 1:
                        break
        best_opts.sort(key=lambda v: bin(vcov[v] & ~covered).count('1'), reverse=True)
        for v in best_opts:
            r = rec(S_mask | (1 << v), covered | vcov[v])
            if r is not None:
                return r
        return None
    w = rec(0, 0)
    return (w is None), nodes[0]

def main():
    p = find_ledger()
    graphs = [parse_g6(l) for l in open(p) if l.strip()]
    print(f"ledger {p}: {len(graphs)} graphs")
    assert len(graphs) == 37
    for gi, adj in enumerate(graphs):
        k4 = count_K4(adj)
        i6 = has_indep6(adj)
        assert k4 == 0, (gi, k4)
        assert not i6, gi
    print("all 37 are valid Ramsey(4,6;35) witnesses")
    t0 = time.time()
    for gi, adj in enumerate(graphs):
        fams = all_indep5(adj)
        proved, nodes = prove_no_extension(adj, fams)
        assert proved, f"graph {gi} unexpectedly extends"
        print(f"g{gi}: indep5={len(fams)} proved_no_ext=True nodes={nodes}", flush=True)
    print(f"MAXIMALITY VERIFIED in {time.time()-t0:.0f}s")

if __name__ == '__main__':
    main()
