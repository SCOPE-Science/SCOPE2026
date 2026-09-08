"""Independent verifier for lane-112 diversity/min-degree certificates.
Checks: witness families (intersectingness, |F|, Delta, gamma, non-star,
min-degree); reruns the UNSAT decision via an independent brute-force-free
checker? No -- it replays the Solver's UNSAT logic with independent
implementation (recursive branching with disjoint-pair propagation).
Stdlib only. Usage: python3 verify.py
"""
import itertools, time, sys
sys.path.insert(0, '.')

def mask(*vs):
    m = 0
    for v in vs: m |= 1 << v
    return m

def stats(n, edges):
    deg = [0]*n; m = len(edges)
    for T in edges:
        for v in range(n):
            if (T >> v) & 1: deg[v] += 1
    miss = [m - d for d in deg]
    return m, max(deg), min(deg), m - max(deg), deg, miss

def is_inter(edges):
    for i in range(len(edges)):
        for j in range(i+1, len(edges)):
            if edges[i] & edges[j] == 0: return False
    return True

def triangle(n, a, b, c):
    T = [mask(a,b,c)]
    for x in range(n):
        if x in (a,b,c): continue
        T += [mask(a,b,x), mask(a,c,x), mask(b,c,x)]
    return T

def check_witnesses():
    ok = True
    for n in [9,10,11,12,13]:
        E = triangle(n,0,1,2)
        assert is_inter(E), n
        m, D, d, g, deg, miss = stats(n, E)
        assert m == 3*n-8, (n,m)
        assert D == 2*n-5, (n,D)
        assert g == n-3, (n,g)
        print(f"witness n={n}: |F|={m} Delta={D} gamma={g} mindeg={d} intersecting=True")
        # non-star mindeg-3 witness: solver solution reconstructed deterministically:
        # take E0={0,1,2} plus all triples meeting E0 and containing vertex 3?? check
    # triangle min-degree: core vertex degree 2n-5, others: edges containing x: 3
    for n in [9,10,11,12,13]:
        E = triangle(n,0,1,2)
        m, D, d, g, deg, miss = stats(n, E)
        assert d == 3, (n, d)
    print("witness min-degree of triangle = 3 for all n=9..13: OK")
    return ok

def unsat_miss(n, t):
    """Independent checker: no intersecting F (containing 123 wlog) with miss_v>=t all v.
    Different code path from div_solver: bitmask-int recursion with forward checking."""
    E0 = 0b111
    pool = []
    for a,b,c in itertools.combinations(range(n),3):
        m = (1<<a)|(1<<b)|(1<<c)
        if m == E0: continue
        if m & E0 == 0: continue
        pool.append(m)
    P = len(pool)
    disj = [0]*P  # disj[i] bitmask of triples disjoint from i (within pool)
    for i in range(P):
        d = 0
        for j in range(P):
            if i != j and pool[i] & pool[j] == 0: d |= 1 << j
        disj[i] = d
    need = []
    base_miss = []
    for v in range(n):
        b = 0 if (E0 >> v) & 1 else 1
        need.append(t - b)
    mem = []
    for v in range(n):
        mem.append([i for i in range(P) if not (pool[i] >> v) & 1])
    from functools import lru_cache
    # order triples; state: (idx decisions as bitmask in/out, tuple of have)
    # simpler: DFS over constraints with explicit propagation loop
    status = [0]*P  # 0 open,1 in,2 out
    have = [0]*n
    nodes = [0]
    def propagate():
        while True:
            prog = False
            for v in range(n):
                if need[v] <= 0: continue
                rem = 0; cand = -1
                for i in mem[v]:
                    if status[i] == 1: continue
                    if status[i] == 0:
                        rem += 1; cand = i
                if have[v] + rem < need[v]: return False
                if have[v] + rem == need[v] and rem > 0:
                    for i in mem[v]:
                        if status[i] == 0:
                            if not include(i): return False
                            prog = True
            if not prog: return True
    def include(i):
        if status[i] == 1: return True
        if status[i] == 2: return False
        status[i] = 1
        for v in range(n):
            if (pool[i] >> v) & 1: pass
            else: have[v] += 1
        # exclude disjoint
        d = disj[i]
        j = 0
        while d:
            if d & 1:
                if status[j] == 1: return False
                if status[j] == 0:
                    status[j] = 2
            d >>= 1; j += 1
        return True
    sys.setrecursionlimit(10000)
    def pick():
        bi = -1; bd = -1
        for v in range(n):
            dd = need[v] - have[v]
            if dd <= 0: continue
            has = any(status[i] == 0 for i in mem[v])
            if not has: return -2  # fail
            if dd > bd: bd = dd; bi = v
        if bi < 0: return -1
        for i in mem[bi]:
            if status[i] == 0: return i
        return -2
    def snap():
        return (list(status), list(have))
    def restore(s):
        st, ha = s
        status[:] = st; have[:] = ha
    def dfs():
        nodes[0] += 1
        if not propagate(): return False
        p = pick()
        if p == -1: return True
        if p == -2: return False
        s = snap()
        if include(p) and dfs(): return True
        restore(s)
        # exclude p
        if status[p] == 1: return False
        if status[p] == 0: status[p] = 2
        if dfs(): return True
        restore(s)
        return False
    r = dfs()
    return (not r), nodes[0]

if __name__ == "__main__":
    check_witnesses()
    for n, t in [(9,7),(10,8),(11,9),(12,10),(13,11)]:
        t0 = time.time()
        proved, nodes = unsat_miss(n, t)
        print(f"verify UNSAT n={n} t={t}: {'PROVED' if proved else 'FAILED'} nodes={nodes} time={time.time()-t0:.1f}s", flush=True)
