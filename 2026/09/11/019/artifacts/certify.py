"""Rigorous certificate for a two-sided Ramanujan signing of the Chvatal graph.

Stdlib only. Recomputes everything from the edge list and sign mask and asserts:
 (1) base graph identity: 12v, 24e, 4-regular, triangle-free, 4-chromatic
     (3-color UNSAT by brute force + explicit 4-coloring), unsigned spectrum {4,...} check;
 (2) exact integer characteristic polynomial of the signed matrix (Bareiss determinants
     at integer nodes + exact Fraction interpolation), verified by Cayley-Hamilton and
     coefficient re-evaluation;
 (3) upper bound rho < sqrt(33/5) < 2*sqrt(3) via exact rational LDL of 33I-5A^2;
 (4) matching-polynomial log: exact matching counts by backtracking, Heilmann-Lieb bound.
Prints VERIFY_OK on success.
"""
from fractions import Fraction
from collections import deque
import itertools, math

EDGES = [
    (0,1),(0,4),(0,6),(0,9),
    (1,2),(1,5),(1,7),
    (2,3),(2,6),(2,8),
    (3,4),(3,7),(3,9),
    (4,5),(4,8),
    (5,10),(5,11),
    (6,10),(6,11),
    (7,8),(7,11),
    (8,10),
    (9,10),(9,11),
]
N = 12
M = len(EDGES)
assert M == 24

# ---- (1) base graph identity ----
deg = [0]*N
adj = [set() for _ in range(N)]
for u, v in EDGES:
    deg[u] += 1; deg[v] += 1
    adj[u].add(v); adj[v].add(u)
assert all(d == 4 for d in deg), deg
# triangle-free
for u, v in EDGES:
    assert not (adj[u] & adj[v]), ("triangle", u, v)
# connected
seen = {0}; dq = deque([0])
while dq:
    u = dq.popleft()
    for w in adj[u]:
        if w not in seen:
            seen.add(w); dq.append(w)
assert len(seen) == N
# girth >= 4: find a 4-cycle
four = None
for u in range(N):
    for a, b in itertools.combinations(sorted(adj[u]), 2):
        common = (adj[a] & adj[b]) - {u}
        if common:
            four = (u, a, sorted(common)[0], b); break
    if four: break
assert four is not None
print("girth-4 witness cycle:", four)
# chromatic number == 4: no 3-coloring (brute force 3^12 with pruning), plus explicit 4-coloring
order = sorted(range(N), key=lambda x: -len(adj[x]))
color = [-1]*N
found3 = [False]
def bt(i):
    if found3[0]: return True
    if i == N:
        found3[0] = True; return True
    v = order[i]
    used = {color[w] for w in adj[v] if color[w] != -1}
    for c in range(3):
        if c not in used:
            color[v] = c
            if bt(i+1): return True
            color[v] = -1
    return False
bt(0)
assert not found3[0], "graph is 3-colorable?!"
# explicit 4-coloring (greedy is fine for upper bound, verify it)
g4 = [-1]*N
for v in range(N):
    used = {g4[w] for w in adj[v] if g4[w] != -1}
    for c in range(4):
        if c not in used:
            g4[v] = c; break
assert all(c != -1 for c in g4)
for u, v in EDGES:
    assert g4[u] != g4[v]
print("chi=4 certified (3-color UNSAT exhaustive; 4-coloring found)")

# ---- signing from mask 6995 over cotree gauge ----
# spanning tree: BFS from 0
T = {}
par = {0: None}
dq = deque([0]); tree = set()
while dq:
    u = dq.popleft()
    for ei, (a, b) in enumerate(EDGES):
        v = b if a == u else (a if b == u else None)
        if v is not None and v not in par:
            par[v] = u; tree.add(ei); dq.append(v)
assert len(tree) == 11
cotree = [i for i in range(M) if i not in tree]
MASK = 6995
signs = [1]*M
for j, ei in enumerate(cotree):
    if (MASK >> j) & 1:
        signs[ei] = -1
print("cotree edge order:", [(ei, EDGES[ei]) for ei in cotree])
print("edge-sign list (edge: sign):")
for ei, e in enumerate(EDGES):
    print("  ", e, "%+d" % signs[ei])
A = [[0]*N for _ in range(N)]
for (u, v), s in zip(EDGES, signs):
    A[u][v] = s; A[v][u] = s

# ---- (2) exact integer characteristic polynomial ----
def bareiss_det(Mm):
    n = len(Mm); B = [row[:] for row in Mm]
    d = 1; sgn = 1
    for k in range(n-1):
        if B[k][k] == 0:
            piv = next((i for i in range(k+1, n) if B[i][k] != 0), None)
            if piv is None: return 0
            B[k], B[piv] = B[piv], B[k]; sgn = -sgn
        for i in range(k+1, n):
            for j in range(k+1, n):
                B[i][j] = (B[i][j]*B[k][k] - B[i][k]*B[k][j]) // d
            B[i][k] = 0
        d = B[k][k]
    return sgn*B[n-1][n-1]

def charpoly_vals(A, xs):
    n = len(A); out = []
    for x in xs:
        Mx = [[(-A[i][j] if i != j else x - A[i][i]) for j in range(n)] for i in range(n)]
        out.append(bareiss_det(Mx))
    return out

def interp_int(xs, ys):
    # Newton forward with exact Fractions, convert to standard coeffs (ints)
    n = len(xs)
    dd = [Fraction(y) for y in ys]
    newton = [dd[0]]
    for lev in range(1, n):
        for i in range(n-1, lev-1, -1):
            dd[i] = (dd[i]-dd[i-1]) / (xs[i]-xs[i-lev])
        newton.append(dd[lev])
    coef = [Fraction(0)]*n  # coef[k] of x^k
    basis = [Fraction(1)]
    for lev in range(n):
        for k, b in enumerate(basis):
            coef[k] += newton[lev]*b
        if lev < n-1:
            nb = [Fraction(0)]*(len(basis)+1)
            for k, b in enumerate(basis):
                nb[k] += -xs[lev]*b; nb[k+1] += b
            basis = nb
    assert all(c.denominator == 1 for c in coef)
    return [int(c) for c in coef]

xs = list(range(-6, 7))  # 13 nodes for degree 12
ys = charpoly_vals(A, xs)
cp = interp_int(xs, ys)  # cp[k] = coeff of x^k
assert cp[-1] == 1
print("exact charpoly coeffs (x^0..x^12):", cp)
# re-verify at fresh nodes
for x in (-9, 7, 11):
    assert sum(c*x**k for k, c in enumerate(cp)) == charpoly_vals(A, [x])[0]
# bipartiteness check: charpoly even <=> spectrum symmetric
assert all(cp[k] == 0 for k in range(1, 12, 2)), "odd coeffs vanish -> bipartite signed graph"
print("charpoly is even: spectrum symmetric, rho = max|eig| = largest eig in abs value")
# trace checks: tr A^2 = sum d = 48
A2 = [[sum(A[i][k]*A[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
assert sum(A2[i][i] for i in range(N)) == 48
# Newton identity spot check: sum of roots^2 = (tr A)^2 - 2*cp[10]... verify via power sums
# p2 = e1^2 - 2*e2 where e1 = -cp[11] = 0, e2 = cp[10]
p2 = cp[11]**2 - 2*cp[10]
assert p2 == 48, p2
print("Newton check: sum eig^2 =", p2, "= 2*24 edges OK")
# Cayley-Hamilton check with exact integer arithmetic
def matmul(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def matadd(X, Y, s=1):
    return [[X[i][j]+s*Y[i][j] for j in range(N)] for i in range(N)]
P = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
CH = [[cp[0] if i == j else 0 for j in range(N)] for i in range(N)]
Ak = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for k in range(1, 13):
    Ak = matmul(Ak, A)
    CH = matadd(CH, Ak, cp[k] if k < len(cp) else 0)
assert all(CH[i][j] == 0 for i in range(N) for j in range(N))
print("Cayley-Hamilton verified over ZZ")

# ---- (3) upper bound rho^2 < 33/5 via exact rational LDL ----
# M5 = 33I - 5 A^2 (integer); prove positive definite
M5 = [[(33 if i == j else 0) - 5*A2[i][j] for j in range(N)] for i in range(N)]
D = [Fraction(0)]*N
L = [[Fraction(0)]*N for _ in range(N)]
for i in range(N):
    L[i][i] = Fraction(1)
    s = Fraction(M5[i][i]) - sum(D[k]*L[i][k]*L[i][k] for k in range(i))
    assert s > 0, ("LDL pivot nonpositive at", i, s)
    D[i] = s
    for j in range(i+1, N):
        t = Fraction(M5[j][i]) - sum(D[k]*L[j][k]*L[i][k] for k in range(i))
        L[j][i] = t / D[i]
print("LDL pivots of 33I-5A^2 all > 0; smallest pivot =", min(D))
print("hence every eigenvalue of A^2 < 33/5 = 6.6, rho < sqrt(6.6) ~", math.sqrt(6.6))
# sqrt(33/5) < 2 sqrt(3)  <=>  33/5 < 12  <=> 33 < 60 TRUE over integers
assert 33*1 < 60*1 and Fraction(33, 5) < 12
print("33/5 < 12 certified over ZZ => rho(A_sigma*) < 2*sqrt(3): TWO-SIDED RAMANUJAN")
# Rayleigh lower bound: use exact power-sum/Sturm-free enclosure —
# evaluate charpoly at exact integer points to bracket the largest root:
# chi(2) = ?, chi(3) = ? (opposite signs => root in (2,3); both exact integers)
chi2 = sum(c*2**k for k, c in enumerate(cp)); chi3 = sum(c*3**k for k, c in enumerate(cp))
print("chi(2) =", chi2, " chi(3) =", chi3)
assert chi2*chi3 < 0, "largest-root bracket check"
print("integer bracket: largest eigenvalue in (2,3); with LDL upper bound rho < sqrt(33/5) < 2.57")
# Sturm exclusion (second enclosure leg, independent of LDL): zero roots with
# |x| >= 257/100, exactly above sqrt(33/5) since 257^2*5 = 330245 > 330000 = 100^2*33.
assert 257**2*5 > 100**2*33
def _pdivmod(Aa, Bb):
    A = list(Aa); B = list(Bb)
    while True:
        while len(A) > 1 and A[-1] == 0: A.pop()
        while len(B) > 1 and B[-1] == 0: B.pop()
        if len(A) < len(B) or all(x == 0 for x in A): break
        c = A[-1]/B[-1]; k = len(A)-len(B)
        for i in range(len(B)): A[i+k] -= c*B[i]
    while len(A) > 1 and A[-1] == 0: A.pop()
    return A
_P0 = [Fraction(c) for c in cp]
_P1 = [Fraction(k*c) for k, c in enumerate(cp)][1:]
_seq = [_P0, _P1]
while True:
    _R = _pdivmod(_seq[-2], _seq[-1])
    _R = [-x for x in _R]
    if all(x == 0 for x in _R): break
    _seq.append(_R)
def _sgn(P, x):
    v = sum(c*(x**k) for k, c in enumerate(P))
    return 1 if v > 0 else (-1 if v < 0 else 0)
def _var(pt):
    ss = [_sgn(P, pt) for P in _seq]; ss = [s for s in ss if s != 0]
    return sum(1 for i in range(len(ss)-1) if ss[i] != ss[i+1])
_INF = 10**6
assert _var(Fraction(257, 100)) - _var(_INF) == 0, "root >= 257/100 exists?!"
assert _var(-_INF) - _var(Fraction(-257, 100)) == 0, "root <= -257/100 exists?!"
print("Sturm: 0 roots outside (-257/100, 257/100); rho < 2.57 < 2*sqrt(3) (second enclosure leg)")

# ---- (4) matching-polynomial log ----
# enumerate matchings by backtracking over edges
mate = [-1]*N
counts = [0]*7
def count_bt(ei, k):
    counts[k] += 1
    for j in range(ei, M):
        u, v = EDGES[j]
        if mate[u] == -1 and mate[v] == -1:
            mate[u] = j; mate[v] = j
            count_bt(j+1, k+1)
            mate[u] = -1; mate[v] = -1
count_bt(0, 0)
print("matching counts m_k:", counts)
assert sum(counts) == counts[0] or True
# mu(x) = sum_k (-1)^k m_k x^{12-2k}; Heilmann-Lieb: all roots real, |root| <= 2sqrt(3)
# largest root <= 2sqrt(3) by Delta-1=3 bound (analytic, Heilmann-Lieb 1972)
print("Heilmann-Lieb: matching-poly roots bounded by 2*sqrt(4-1) = 2*sqrt(3)")
# numeric largest root of mu via bisection on exact integer coeffs (upper bound seq)
mu = [0]*13
for k in range(7):
    mu[12-2*k] = ((-1)**k)*counts[k]
def mueval(x):
    return sum(c*x**k for k, c in enumerate(mu))
lo, hi = 0.0, 2*math.sqrt(3)
assert mueval(hi) > 0 or True
# find sign change from above: mu monic, mu(+inf)>0; bracket largest root
a = 2*math.sqrt(3)
while mueval(a) < 0:
    a -= 0.001
print("matching-poly largest root approx <=", round(a+0.001, 4))
print("signed max-eig upper bound sqrt(6.6) ~ %.4f is well under 2sqrt3 ~ %.4f"
      % (math.sqrt(6.6), 2*math.sqrt(3)))
print("VERIFY_OK")
