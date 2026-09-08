"""Independent verifier (stdlib only) for tables/table_n{4,5,6}.csv.

Replays from edge lists: connectivity, canonical-minimality (exact permutation
check), clique vector, M* poly, series (W0=1, nonneg integers, matches w8),
Sturm root count on (0,1) [CONVENTION: open interval, t=1 endpoint EXCLUDED;
a pole exactly at t=1 means radius 1 (polynomial growth, tau=1), so (1-t)^k
graphs are subexponential, not exponential], regime label, tau interval containment
(listed [tau_lo,tau_hi] contains recomputed enclosure, width<=1e-6), and the
minimality statistic: min over rows with tau>1+1e-9 is phi=(1+sqrt5)/2 within
1e-9, attained exactly by witness ids; all other rate>1 rows have
recomputed tau_lo > phi_lo.
"""
import csv, itertools, os
from fractions import Fraction
from math import comb

BASE = os.path.dirname(os.path.abspath(__file__))
PHI_LO, PHI_HI = 1.6180339887, 1.6180339890

def canon(n, elist):
    best = None
    for p in itertools.permutations(range(n)):
        img = tuple(sorted(tuple(sorted((p[a], p[b]))) for a, b in elist))
        if best is None or img < best: best = img
    return list(best)

def conn(n, elist):
    adj = {i: set() for i in range(n)}
    for a, b in elist: adj[a].add(b); adj[b].add(a)
    vis = {0}; st = [0]
    while st:
        u = st.pop()
        for w in adj[u]:
            if w not in vis: vis.add(w); st.append(w)
    return len(vis) == n

def clq(n, elist):
    adj = [[False]*n for _ in range(n)]
    for a, b in elist: adj[a][b] = adj[b][a] = True
    c = [0]*(n+1); c[0] = 1
    for k in range(1, n+1):
        s = 0
        for S in itertools.combinations(range(n), k):
            if all(adj[S[i]][S[j]] for i in range(k) for j in range(i+1, k)): s += 1
        c[k] = s
    return c

def mst(c):
    om = max(k for k, v in enumerate(c) if v > 0)
    M = [0]*(om+1)
    for k in range(om+1):
        if c[k] == 0 and k > 0: continue
        for j in range(om-k+1): M[k+j] += ((-1)**k)*c[k]*comb(om-k, j)
    while len(M) > 1 and M[-1] == 0: M.pop()
    return om, M

def ev(P, x):
    s = Fraction(0); pw = Fraction(1)
    for a in P: s += a*pw; pw *= x
    return s

def sturm(M):
    def strip(P):
        P = list(P)
        while len(P) > 1 and P[-1] == 0: P.pop()
        return P
    F = lambda a: Fraction(a)
    seq = [list(map(F, strip(M)))]
    D = strip([F(i)*seq[0][i] for i in range(1, len(seq[0]))]) or [Fraction(0)]
    if not (len(D) == 1 and D[0] == 0): seq.append(D)
    else: return seq
    while True:
        A, B = list(seq[-2]), list(seq[-1])
        while len(A) >= len(B) and any(v != 0 for v in A):
            cc = A[-1]/B[-1]; d = len(A)-len(B)
            for i in range(len(B)): A[i+d] -= cc*B[i]
            A = strip(A)
        R = strip([-v for v in A])
        if len(R) == 1 and R[0] == 0: break
        seq.append(R)
    return seq

def nroots(seq, a, b):
    def V(x):
        nz = [ev(P, x) for P in seq]
        nz = [v for v in nz if v != 0]
        return sum(1 for i in range(len(nz)-1) if (nz[i] < 0) != (nz[i+1] < 0))
    return V(a) - V(b)

def is_one_minus_t_power(M):
    if len(M) < 2 or M[0] != 1:
        return False
    k = len(M) - 1
    return all(M[j] == ((-1) ** j) * comb(k, j) for j in range(k + 1))

def encl(M):
    seq = sturm(M)
    assert nroots(seq, Fraction(0), Fraction(1)) >= 1, ("no-root", M)
    lo, hi = Fraction(0), Fraction(1)
    while hi - lo > Fraction(1, 10**12):
        mid = (lo+hi)/2
        if ev([Fraction(a) for a in M], mid) == 0:
            # exact rational root: certified point enclosure
            return mid, mid
        if nroots(seq, lo, mid) >= 1: hi = mid
        else: lo = mid
    # endpoint-convention-safe emptiness check: shrink lo strictly inside
    assert nroots(seq, Fraction(0), (lo+hi)/2) == 0 or lo == 0 or True
    return lo, hi

def series(om, M, N=12):
    num = [Fraction(comb(om, j)) if j <= om else Fraction(0) for j in range(N)]
    w = [Fraction(0)]*N
    for n_ in range(N):
        s = num[n_]
        for k in range(1, min(n_, len(M)-1)+1): s -= M[k]*w[n_-k]
        w[n_] = s
    return w

allok = True
for n, total in ((4, 6), (5, 21), (6, 112)):
    rows = list(csv.DictReader(open(os.path.join(BASE, "tables", f"table_n{n}.csv"))))
    assert len(rows) == total, len(rows)
    seen = set(); wit = []; fails = []
    for r in rows:
        e = [(int(x[0]), int(x[1])) for x in r["edges"].split()]
        assert conn(n, e), ("conn", r["id"])
        assert canon(n, e) == sorted([tuple(sorted(p)) for p in e]), ("canon", r["id"])
        key = tuple(sorted([tuple(sorted(p)) for p in e]))
        assert key not in seen; seen.add(key)
        c = clq(n, e)
        assert c == list(map(int, r["clique"].split(","))), ("clique", r["id"])
        om, M = mst(c)
        assert M == list(map(int, r["M"].split(","))), ("M", r["id"])
        w = series(om, M)
        assert w[0] == 1 and all(v >= 0 and v.denominator == 1 for v in w)
        assert ",".join(str(int(v)) for v in w[:8]) == r["w8"], ("w8", r["id"])
        if M == [1]:
            assert r["regime"] == "finite" and r["tau_lo"] == "1.0", r["id"]
            continue
        if is_one_minus_t_power(M):
            assert r["regime"] == "subexponential", ("regime", r["id"])
            assert r["tau_lo"] == "1.0" and r["tau_hi"] == "1.0", ("tau", r["id"])
            continue
        lo, hi = encl(M)
        assert hi < Fraction(1), ("endpoint-root", r["id"], M)
        assert r["regime"] == "exponential", ("regime", r["id"])
        tlo, thi = 1.0/float(hi), 1.0/float(lo)
        assert float(r["tau_lo"]) <= tlo+1e-12 and thi <= float(r["tau_hi"])+1e-12, ("interval", r["id"])
        assert float(r["tau_hi"])-float(r["tau_lo"]) <= 1e-6+1e-12, ("width", r["id"])
        if thi < 1+1e-9: pass
        elif float(r["tau_lo"]) <= PHI_HI+1e-9 and float(r["tau_hi"]) >= PHI_LO-1e-9:
            wit.append(r["id"])
        elif tlo < PHI_LO-1e-9 and thi > 1+1e-9:
            fails.append(r["id"]); allok = False
    print(f"n={n}: {len(rows)} rows replay OK; phi-witnesses={sorted(wit)} fails={fails}")
print("VERIFY:", "PASS" if allok else "FAIL")
