"""Steinberg rational growth series census for RACGs on connected graphs n=4,5,6.

Convention (Davis, Thm 17.1.9/Cor 17.1.10; Steinberg formula):
  1/W(t) = sum_{T spherical} (-1)^|T| / W_T(t^{-1}).
For RACG on graph G (edges = commuting pairs): T spherical iff T is a clique,
W_T(u)=(1+u)^|T|. With c_k = #k-cliques, om = clique number:
  1/W(t) = M(t)/(1+t)^om,  M(t) = sum_k (-1)^k c_k t^k (1+t)^{om-k} in ZZ[t],
  M(0) = 1.  Hence W(t) = (1+t)^om / M(t).
Growth rate tau = 1/radius(W); radius = smallest root of M in (0,1) by
Pringsheim (coefficients are cardinalities, hence >= 0); tau = 1 if M has no
root in (0,1) (poles then only possibly at t=1).

Root isolation is EXACT: Sturm sequences over Fraction (no floats); interval
[lo,hi] for smallest root r in (0,1) certified by Sturm counts
(#roots(0,lo) == 0 and #roots(lo,hi) >= 1 with sign-change/endpoint checks).
Subexponential graphs are certified by exact factorization M == (1-t)^k or
(t-1)^k... precisely M(t) == (t-1)^k up to sign, i.e. single pole at t=1.
Finite graphs: M == 1.

Stdlib only. Writes tables/table_n{4,5,6}.csv.
Columns: id, edges, m, clique, om, M, tau_lo, tau_hi, regime, w8.
"""
import itertools, csv, os
from fractions import Fraction
from math import comb

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tables")
os.makedirs(OUT, exist_ok=True)

def canonical_reps(n):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    m = len(edges)
    perms = list(itertools.permutations(range(n)))
    def canon(elist):
        eset = set(elist); best = None
        for p in perms:
            img = tuple(sorted(tuple(sorted((p[i], p[j]))) for (i, j) in eset))
            if best is None or img < best: best = img
        return best
    seen = {}
    out = []
    for mask in range(1 << m):
        elist = [edges[i] for i in range(m) if (mask >> i) & 1]
        adjl = {i: set() for i in range(n)}
        for a, b in elist:
            adjl[a].add(b); adjl[b].add(a)
        vis = {0}; stack = [0]
        while stack:
            u = stack.pop()
            for w in adjl[u]:
                if w not in vis: vis.add(w); stack.append(w)
        if len(vis) != n: continue
        c = canon(elist)
        if c in seen: continue
        seen[c] = True; out.append(list(c))
    out.sort(key=lambda e: (len(e), e))
    return out

def clique_vector(n, elist):
    adj = [[False]*n for _ in range(n)]
    for a, b in elist: adj[a][b] = adj[b][a] = True
    c = [0]*(n+1); c[0] = 1
    for k in range(1, n+1):
        s = 0
        for S in itertools.combinations(range(n), k):
            ok = True
            for ii in range(k):
                for jj in range(ii+1, k):
                    if not adj[S[ii]][S[jj]]: ok = False; break
                if not ok: break
            if ok: s += 1
        c[k] = s
    return c

def mstar(c):
    om = max(k for k, v in enumerate(c) if v > 0)
    M = [0]*(om+1)
    for k in range(om+1):
        if c[k] == 0 and k > 0: continue
        for j in range(om-k+1):
            M[k+j] += ((-1)**k)*c[k]*comb(om-k, j)
    while len(M) > 1 and M[-1] == 0: M.pop()  # strip padding zeros
    return om, M

# ---- exact Sturm machinery ----
def _strip(P):
    P = list(P)
    while len(P) > 1 and P[-1] == 0: P.pop()
    return P

def sturm_seq(M):
    seq = [[Fraction(a) for a in _strip(M)]]
    D = [Fraction(i)*seq[0][i] for i in range(1, len(seq[0]))]
    D = _strip(D) if D else [Fraction(0)]
    if len(D) == 1 and D[0] == 0: return seq
    seq.append(D)
    while True:
        A, B = list(seq[-2]), list(seq[-1])
        while len(A) >= len(B) and any(v != 0 for v in A):
            c = A[-1]/B[-1]; d = len(A)-len(B)
            for i in range(len(B)): A[i+d] -= c*B[i]
            A = _strip(A)
        R = _strip([-v for v in A])
        if len(R) == 1 and R[0] == 0: break
        seq.append(R)
        if len(seq) > 30: raise RuntimeError("sturm too long")
    return seq

def _eval(P, x):
    s = Fraction(0); pw = Fraction(1)
    for a in P: s += a*pw; pw *= x
    return s

def nroots_open(seq, a, b):
    """#distinct roots in (a,b); requires M(a)!=0 (a=0 ok since M(0)=1)."""
    def V(x):
        nz = [_eval(P, x) for P in seq]
        nz = [v for v in nz if v != 0]
        return sum(1 for i in range(len(nz)-1) if (nz[i] < 0) != (nz[i+1] < 0))
    return V(a) - V(b)

def peval(M, x): return _eval([Fraction(a) for a in M], x)

def is_one_minus_t_power(M):
    """Exact test M == (1-t)^k for some k>=1. Coeff list low-to-high."""
    if len(M) < 2 or M[0] != 1:
        return False
    k = len(M) - 1
    return all(M[j] == ((-1) ** j) * comb(k, j) for j in range(k + 1))

def smallest_root_interval(M, tol=Fraction(1, 10**12)):
    """M in ZZ coeffs, M(0)=1, nonconstant. Returns ('exp',(lo,hi)) with
    0<lo<hi<1... (hi<=1) certifying smallest root in (0,1) lies in [lo,hi] and
    no root in (0,lo); or ('subexp',k) with M(t)==(1-t)^k*((...)) — here caller
    handles (t-1) factoring; or ('subexp',0)."""
    seq = sturm_seq(M)
    if nroots_open(seq, Fraction(0), Fraction(1)) == 0:
        # root possibly AT t=1 only
        if peval(M, Fraction(1)) == 0:
            return ('endpoint', None)
        return ('subexp', None)
    lo, hi = Fraction(0), Fraction(1)
    assert peval(M, lo) != 0
    while hi - lo > tol:
        mid = (lo + hi)/2
        if peval(M, mid) == 0:
            hi = mid; continue
        if nroots_open(seq, lo, mid) >= 1:
            hi = mid
        else:
            assert nroots_open(seq, mid, hi) >= 1
            lo = mid
    assert nroots_open(seq, Fraction(0), lo) == 0
    return ('exp', (lo, hi))

def factor_one_minus_t(M):
    """Divide out factors of (t-1): return (k, Mred) with M = (t-1)^k Mred."""
    M = list(M); k = 0
    while len(M) > 1 and sum(M) == 0:  # M(1)==0
        # synthetic division by (t-1): M(t)=(t-1)Q(t)+M(1)
        Q = [0]*(len(M)-1)
        Q[-1] = M[-1]
        for i in range(len(M)-2, 0, -1):
            Q[i-1] = M[i] + Q[i]
        M = _strip(Q); k += 1
    return k, M

def series_check(om, M, N=12):
    num = [Fraction(comb(om, j)) if j <= om else Fraction(0) for j in range(N)]
    w = [Fraction(0)]*N
    for n_ in range(N):
        s = num[n_]
        for k in range(1, min(n_, len(M)-1)+1): s -= M[k]*w[n_-k]
        w[n_] = s
    return w

def gid(n, i): return f"n{n}-{i:03d}"

EXPECTED = {4: 6, 5: 21, 6: 112}
for n in (4, 5, 6):
    R = canonical_reps(n)
    assert len(R) == EXPECTED[n], (n, len(R))
    rows = []
    for i, e in enumerate(R):
        c = clique_vector(n, e)
        om, M = mstar(c)
        w = series_check(om, M)
        assert w[0] == 1 and all(v >= 0 and v.denominator == 1 for v in w), (n, i)
        if M == [1]:
            regime, tlo, thi = 'finite', Fraction(1), Fraction(1)
        elif is_one_minus_t_power(M):
            # exact affine-type test BEFORE Sturm: M == (1-t)^k, pole only at
            # t=1 (radius 1, polynomial growth), tau = 1 exactly.
            regime, tlo, thi = 'subexponential', Fraction(1), Fraction(1)
        else:
            kind, pay = smallest_root_interval(M)
            assert kind == 'exp', (n, i, M, kind)
            lo, hi = pay
            assert hi < Fraction(1), (n, i, M, lo, hi)
            regime = 'exponential'
            tlo, thi = Fraction(1, 1)/hi, Fraction(1, 1)/lo
        rows.append(dict(id=gid(n, i), edges=" ".join(f"{a}{b}" for a, b in e),
                         m=len(e), clique=",".join(map(str, c)), om=om,
                         M=",".join(map(str, M)),
                         tau_lo=float(tlo), tau_hi=float(thi),
                         regime=regime, w8=",".join(str(int(v)) for v in w[:8])))
    with open(os.path.join(OUT, f"table_n{n}.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader(); wr.writerows(rows)
    ex = [(r['tau_lo'], r['id']) for r in rows if r['regime'] == 'exponential']
    ex.sort()
    print(f"n={n}: total={len(rows)} finite={sum(1 for r in rows if r['regime']=='finite')} "
          f"subexp={sum(1 for r in rows if r['regime']=='subexponential')} exp={len(ex)}")
    if ex: print("  min-tau:", ex[0], " next:", ex[1] if len(ex) > 1 else None,
                 " max-tau:", ex[-1])
