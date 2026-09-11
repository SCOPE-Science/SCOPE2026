"""Full TARGET pipeline: DCLS(11) transversal spectrum + mate census.
Step 1: enumerate 3441 normalized orthomorphisms of Z11 (method A: fixed-row backtrack).
Step 2: multiplier-orbit canonical reduction -> C=363 canonical seeds.
Step 3: per-seed transversal counts by TWO independent exact-cover methods; agreement check.
Step 4: universal orthogonal mate M(i,j)=j-i; per-seed decomposition verification.
Writes seeds.json, count_log_A.json, count_log_B.json, spectrum.json, mate_certificate.json.
Stdlib only. Run: python3 run_all.py
"""
import json, time, sys

N = 11
T0 = time.time()

# ---- Step 1: enumerate normalized orthomorphisms theta: Z11->Z11, theta(0)=0,
# theta bijective on nonzero, psi(d)=theta(d)-d bijective on nonzero (psi(0)=0).
theta = [-1]*N; theta[0] = 0
used_t = {0}; used_p = {0}
sols = []
sys.setrecursionlimit(10000)
def bt(i):
    if i == N:
        sols.append(tuple(theta)); return
    for v in range(1, N):
        if v in used_t: continue
        w = (v - i) % N
        if w == 0 or w in used_p: continue
        theta[i] = v; used_t.add(v); used_p.add(w)
        bt(i+1)
        used_t.discard(v); used_p.discard(w)
bt(1)
TOTAL = len(sols)
print(f"enumerated normalized orthomorphisms: {TOTAL}", flush=True)

# ---- Step 2: multiplier action theta^a(d) = a*theta(a^{-1} d); canonical = orbit min.
def apply_mul(t, a):
    inv = pow(a, -1, N)
    return tuple((a*t[(inv*d) % N]) % N for d in range(N))
seen = set(); reps = []; orb_sizes = []
for t in sols:
    if t in seen: continue
    orb = {apply_mul(t, a) for a in range(1, N)}
    seen |= orb; reps.append(min(orb)); orb_sizes.append(len(orb))
reps.sort()
C = len(reps)
print(f"C = {C}", flush=True)
from collections import Counter
print("orbit-size distribution:", dict(sorted(Counter(orb_sizes).items())), flush=True)
json.dump({"C": C, "seeds": [list(t) for t in reps],
           "orbit_size_distribution": {str(k): v for k, v in sorted(Counter(orb_sizes).items())},
           "total_normalized": TOTAL},
          open("seeds.json", "w"))

def square_of(th):
    return [[(th[(j-i) % N]+i) % N for j in range(N)] for i in range(N)]

# ---- Step 3a: Method A — fixed-row order backtrack (rows fixed, cols+symbols MRV-free).
def count_A(L):
    cnt = 0; nodes = [0]
    def rec(r, uc, us):
        nodes[0] += 1
        if r == N: cnt.__iadd__ if False else None; return 1
        row = L[r]; s = 0
        for c in range(N):
            b = 1 << c
            if uc & b: continue
            sb = 1 << row[c]
            if us & sb: continue
            s += rec(r+1, uc|b, us|sb)
        return s
    return rec(0, 0, 0), nodes[0]

logA = []
tA = time.time()
for k, th in enumerate(reps):
    L = square_of(th)
    c, nd = count_A(L)
    logA.append({"seed": list(th), "count": c, "nodes": nd})
    if k % 60 == 0: print(f"A {k}/{C} t={time.time()-tA:.0f}s", flush=True)
print(f"method A done t={time.time()-tA:.0f}s", flush=True)
json.dump(logA, open("count_log_A.json", "w"))

# ---- Step 3b: Method B — generic DLX exact cover over 33 columns (rows+cols+syms),
# 121 cell-options, MRV column choice. Independent code path from method A.
def count_B(L):
    opts = []
    for i in range(N):
        for j in range(N):
            opts.append((i, N+j, 2*N+L[i][j]))
    col2opts = [[] for _ in range(3*N)]
    for k, o in enumerate(opts):
        for c in o: col2opts[c].append(k)
    active_c = [True]*(3*N); alive = [True]*len(opts)
    cnt = [0]; nodes = [0]
    def rec(covered):
        nodes[0] += 1
        if covered == N: cnt[0] += 1; return
        best = -1; bestl = None
        for c in range(3*N):
            if not active_c[c]: continue
            l = [k for k in col2opts[c] if alive[k]]
            if len(l) == 0: return
            if bestl is None or len(l) < len(bestl):
                best = c; bestl = l
                if len(l) == 1: break
        for k in bestl:
            o = opts[k]
            if not (active_c[o[0]] and active_c[o[1]] and active_c[o[2]]): continue
            for c in o: active_c[c] = False
            removed = []
            for c in o:
                for k2 in col2opts[c]:
                    if alive[k2]: alive[k2] = False; removed.append(k2)
            rec(covered+1)
            for k2 in removed: alive[k2] = True
            for c in o: active_c[c] = True
    rec(0)
    return cnt[0], nodes[0]

logB = []
tB = time.time()
for k, th in enumerate(reps):
    L = square_of(th)
    c, nd = count_B(L)
    logB.append({"seed": list(th), "count": c, "nodes": nd})
    if k % 60 == 0: print(f"B {k}/{C} t={time.time()-tB:.0f}s", flush=True)
print(f"method B done t={time.time()-tB:.0f}s", flush=True)
json.dump(logB, open("count_log_B.json", "w"))

# ---- Agreement + spectrum
assert [e["seed"] for e in logA] == [e["seed"] for e in logB]
agree = all(a["count"] == b["count"] for a, b in zip(logA, logB))
print("A/B agreement:", agree, flush=True)
assert agree
counts = [e["count"] for e in logA]
dist = dict(sorted(Counter(counts).items()))
M_DCLS = max(counts)
smax = [e["seed"] for e in logA if e["count"] == M_DCLS]
print("spectrum:", dist, flush=True)
print("M_DCLS:", M_DCLS, "witnesses:", len(smax), flush=True)
json.dump({"C": C, "spectrum": {str(k): v for k, v in dist.items()},
           "M_DCLS": M_DCLS, "S_max": smax[0], "S_max_orbit": smax,
           "per_seed": [{"seed": e["seed"], "count": e["count"]} for e in logA],
           "AB_agreement": agree}, open("spectrum.json", "w"))

# ---- Step 4: universal mate M(i,j) = j-i; verify Latin, orthogonality to every
# seed square, and that T_m = {(i,i+m)} partitions cells into 11 transversals.
M = [[(j-i) % N for j in range(N)] for i in range(N)]
assert all(sorted(M[i]) == list(range(N)) for i in range(N))
assert all(sorted(M[i][j] for i in range(N)) == list(range(N)) for j in range(N))
mate_ok = 0
for th in reps:
    L = square_of(th)
    pairs = {(L[i][j], M[i][j]) for i in range(N) for j in range(N)}
    assert len(pairs) == N*N
    for m in range(N):
        cells = [(i, (i+m) % N) for i in range(N)]
        assert len({c for _, c in cells}) == N
        assert len({L[i][j] for i, j in cells}) == N
    mate_ok += 1
print(f"mates verified: {mate_ok}/{C}", flush=True)
json.dump({"universal_mate": M, "rule": "T_m = {(i, i+m mod 11)}",
           "K": mate_ok, "C": C,
           "proof": "M Latin since j->j-i and i->j-i bijections; orthogonal since (L,M)=(u,v) gives d=v, i=u-theta(v), j=i+v uniquely; each T_m has distinct rows/cols/symbols theta(m)+i."},
          open("mate_certificate.json", "w"))
print(f"TOTAL t={time.time()-T0:.0f}s", flush=True)
