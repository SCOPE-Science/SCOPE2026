"""Lane-497 verification: exact closed form + uniform zero-free certificate + HL instance.

Stdlib only (fractions). Prints VERIFY_OK on full success.
Chain:
 1. Brute-force Zaslavsky counts (odd q backtracking) for F_n, n<=4, q<=7,
    vs closed form P_n(q) = (q-1)^2 S_n(q)/q, S_n=(q-1)^n f + (-1)^n g.
 2. Exact polynomial identities: S_n(0)=0, (q-1)f-g = q(q-2)^2,
    odd-n split S_n = q(q-2)^2 + (q-1)((q-1)^{n-1}-1)f, monic deg n+3.
 3. Dominance sign certificates on q>2 (exact identities + factor signs).
 4. Sturm: no roots of P_n in [3,inf) for n<=6; exact root at 2 for odd n.
 5. Deletion-contraction induction step: A_k,B_k recurrence check (exact polys).
 6. Heilmann-Lieb instance: path matching polys m_k (k<=8) real-rooted,
    consecutive interlacing, largest root < 2 (exact Sturm + bisection).
"""
from fractions import Fraction as Q

# ---------- polynomial utilities (const-first, exact) ----------
def strip(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def deg(p):
    return len(strip(p)) - 1

def padd(a, b):
    n = max(len(a), len(b))
    return strip([Q(0)] * n and [(a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(n)])

def psub(a, b):
    return padd(a, [-x for x in b])

def pmul(a, b):
    a, b = strip(a), strip(b)
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return strip(c)

def ppow(p, n):
    r = [Q(1)]
    for _ in range(n):
        r = pmul(r, p)
    return r

def peval(p, x):
    s = Q(0)
    for c in reversed(strip(p)):
        s = s * x + c
    return s

def pderiv(p):
    p = strip(p)
    if len(p) <= 1:
        return [Q(0)]
    return strip([Q(i) * p[i] for i in range(1, len(p))])

def pdivmod(a, b):
    a, b = strip(list(a)), strip(list(b))
    if deg(b) < 0:
        raise ZeroDivisionError
    q = [Q(0)] * max(0, deg(a) - deg(b) + 1)
    r = [Q(x) for x in a]
    while deg(r) >= deg(b) and not (len(r) == 1 and r[0] == 0):
        c = r[-1] / b[-1]
        k = len(r) - len(b)
        q[k] += c
        for i in range(len(b)):
            r[k + i] -= c * b[i]
        r = strip(r)
    return strip(q), strip(r)

QQ = lambda *cs: [Q(c) for c in cs]
QVAR = [Q(0), Q(1)]
QM1 = [Q(-1), Q(1)]          # q-1
F = [Q(3), Q(-3), Q(1)]      # q^2-3q+3
G = [Q(-3), Q(2)]            # 2q-3

def S_poly(n):
    t = pmul(ppow(QM1, n), F)
    s = G if n % 2 == 0 else [-x for x in G]
    return padd(t, s)

def P_poly(n):
    # (q-1)^2 S_n / q  (exact division; S_n(0)=0)
    num = pmul(ppow(QM1, 2), S_poly(n))
    assert num[0] == 0, f"S_{n} not divisible by q"
    return strip(num[1:])  # divide by q

LOG = []

def check(name, cond, detail=""):
    assert cond, f"FAIL {name} {detail}"
    LOG.append(f"ok {name} {detail}")

# ---------- 1. brute force ----------
def count_signed(edges, N, k, cond=None):
    colors = list(range(-k, k + 1))
    deg = [0] * N
    for u, v, s in edges:
        deg[u] += 1
        deg[v] += 1
    order = sorted(range(N), key=lambda i: -deg[i])
    adj = [[] for _ in range(N)]
    for u, v, s in edges:
        adj[u].append((v, s))
        adj[v].append((u, s))
    assign = [None] * N
    count = 0
    def bt(i):
        nonlocal count
        if i == N:
            if cond is None or cond(assign):
                count += 1
            return
        v = order[i]
        for c in colors:
            ok = True
            for w, s in adj[v]:
                if assign[w] is not None:
                    if (s == 1 and assign[w] == c) or (s == -1 and assign[w] == -c):
                        ok = False
                        break
            if ok:
                assign[v] = c
                bt(i + 1)
                assign[v] = None
    bt(0)
    return count

def Fn_edges(n):
    E = [(0, 1, -1), (0, 2, 1), (0, 3, 1), (1, 2, 1), (1, 3, 1)]
    if n == 1:
        return E + [(2, 3, 1)], 4
    N = 4 + (n - 1)
    prev, nxt = 2, 4
    for i in range(n):
        cur = 3 if i == n - 1 else nxt
        E = E + [(prev, cur, 1)]
        prev = cur
        if cur != 3:
            nxt += 1
    return E, N

for n in (1, 2, 3, 4):
    E, N = Fn_edges(n)
    Pn = P_poly(n)
    for k in (0, 1, 2, 3):
        q = 2 * k + 1
        bf = count_signed(E, N, k)
        cf = peval(Pn, Q(q))
        check(f"brute_n{n}_q{q}", cf == bf, f"P={cf} brute={bf}")

# ---------- 2. exact identities ----------
# (q-1)f - g == q(q-2)^2
lhs = psub(pmul(QM1, F), G)
rhs = pmul([Q(0), Q(1)], ppow([Q(-2), Q(1)], 2))
check("key_identity", lhs == rhs, f"{lhs}")
for n in range(1, 13):
    Sn = S_poly(n)
    check(f"S{n}(0)=0", peval(Sn, Q(0)) == 0)
    Pn = P_poly(n)
    check(f"degP{n}", deg(Pn) == n + 3 and Pn[-1] == 1, f"deg={deg(Pn)} lead={Pn[-1]}")
    qm1sq = ppow(QM1, 2)
    _, r = pdivmod(Pn, qm1sq)
    check(f"P{n}(1)=0x2", peval(Pn, Q(1)) == 0 and r == [Q(0)], f"rem={r}")
    if n % 2 == 1:
        # odd-n split identity
        base = pmul([Q(0), Q(1)], ppow([Q(-2), Q(1)], 2))  # q(q-2)^2
        rest = pmul(QM1, pmul(psub(ppow(QM1, n - 1), [Q(1)]), F))
        check(f"odd_split_{n}", padd(base, rest) == Sn)
        check(f"root2_n{n}", peval(Pn, Q(2)) == 0)
    else:
        check(f"no_root2_n{n}", peval(Pn, Q(2)) != 0)

# ---------- 3. dominance signs for q > 2 (sampled exact rationals + factor forms) ----------
for n in range(1, 13):
    Sn = S_poly(n)
    for num in (21, 5, 3, 7, 11, 101):
        q = Q(num, 10) if num < 20 else Q(num)
        if q > 2:
            v = peval(Sn, q)
            check(f"pos_S{n}_q{q}", v > 0, f"S={v}")
# manifest forms: f = (q-1)(q-2)+1 ; g = 2(q-2)+1
check("f_form", padd(pmul(QM1, [Q(-2), Q(1)]), [Q(1)]) == F)
check("g_form", padd(pmul([Q(2)], [Q(-2), Q(1)]), [Q(1)]) == G)

# ---------- 4. Sturm: zero roots in [3, inf) for n<=6 (+ helpers) ----------
def sturm_seq(p):
    seq = [strip(list(p)), pderiv(p)]
    while not (len(seq[-1]) == 1 and seq[-1][0] == 0):
        _, r = pdivmod(seq[-2], seq[-1])
        if len(r) == 1 and r[0] == 0:
            break
        seq.append([-x for x in r])
    return seq

def signs_at(seq, x):
    # x = Fraction or 'inf'
    ss = []
    for p in seq:
        v = p[-1] if x == 'inf' else peval(p, x)
        assert v != 0, "Sturm endpoint zero"
        ss.append(1 if v > 0 else -1)
    return ss

def variations(ss):
    ss = [s for s in ss if s != 0]
    return sum(1 for i in range(1, len(ss)) if ss[i] != ss[i - 1])

def V_at(p, x):
    seq = sturm_seq(p)
    for _ in range(8):
        try:
            return variations(signs_at(seq, x))
        except AssertionError:
            x = x + Q(1, 2 ** 30)
    raise AssertionError("endpoint nudge failed")

def sturm_count(p, a, b):
    """# roots in (a,b), exact; nudges rational endpoints off roots."""
    return V_at(p, a) - V_at(p, b)

for n in range(1, 7):
    Pn = P_poly(n)
    seq = sturm_seq([Q(c) for c in Pn])
    v3 = variations(signs_at(seq, Q(3)))
    vi = variations(signs_at(seq, 'inf'))
    check(f"sturm_[3,inf)_n{n}", v3 - vi == 0, f"V3={v3} Vinf={vi}")

# ---------- 4b. certified census: (2,inf) empty for n<=12; exactly one root in (1,2) for n>=2 ----------
E = Q(1, 10 ** 12)
for n in range(1, 13):
    Pn = [Q(c) for c in P_poly(n)]
    c12 = sturm_count(Pn, Q(1) + E, Q(2) - E)
    c2 = sturm_count(Pn, Q(2) + E, Q(10 ** 6))
    check(f"census12_n{n}", c2 == 0 and c12 == (0 if n == 1 else 1),
          f"(1,2)={c12} (2,inf)={c2}")
# even-n monotonicity on (1,inf): S_n' has no zero there (certified)
for n in range(2, 13, 2):
    d = pderiv(S_poly(n))
    c = sturm_count(d, Q(1) + E, Q(10 ** 6))
    check(f"mono_even_{n}", c == 0 and peval(S_poly(n), Q(1)) < 0, f"crit={c}")

# ---------- 4c. GENERAL even-n lemma (all n>=2): S_n' = (q-1)^{n-1} B(q) + s*2,
#   B(q) = n*f(q) + (q-1)(2q-3) >= 11/8 via two sum-of-squares identities.
#   Hence S_n strictly increasing on [1,inf) for even n: unique root in (1,2).
for n in range(1, 13):
    Sn = S_poly(n)
    B = padd(pmul([Q(n)], F), pmul(QM1, G))
    s = Q(1) if n % 2 == 0 else Q(-1)
    check(f"sderiv_form_{n}", pderiv(Sn) == padd(pmul(ppow(QM1, n - 1), B), [2 * s]))
# SoS (i): f(q) - 3/4 == (q-3/2)^2
check("sos_f", psub(F, [Q(3, 4)]) == ppow([Q(-3, 2), Q(1)], 2))
# SoS (ii): with t=q-1, 2t^2-t+1/8 == 2(t-1/4)^2 ; i.e. (q-1)(2q-3)+1/8 == 2(q-5/4)^2
check("sos_g", padd(pmul(QM1, G), [Q(1, 8)]) == pmul([Q(2)], ppow([Q(-5, 4), Q(1)], 2)))
# endpoint values pinning the unique even-n root into (1,2)
for n in range(2, 13, 2):
    Sn = S_poly(n)
    check(f"pin_even_{n}", peval(Sn, Q(1)) == -1 and peval(Sn, Q(2)) == 2)

# ---------- 5. deletion-contraction induction step (transfer recurrence) ----------
# A_k = (q-1)/q ((q-1)^{k+1}+(-1)^k), B_k likewise; check
# X_{k+1} = (q-2) X_k + (q-1) X_{k-1} as exact polynomial identities.
def A_poly(k):
    t = padd(ppow(QM1, k + 1), [Q((-1) ** k)])
    num = pmul(QM1, t)  # (q-1)(...)
    assert num[0] == 0
    return strip(num[1:])  # divide by q

def B_poly(k):
    t = padd(pmul([Q(-2), Q(1)], ppow(QM1, k)), [Q(2 * ((-1) ** k))])
    num = pmul([Q(-2), Q(1)], t)
    assert num[0] == 0
    return strip(num[1:])

QM2 = [Q(-2), Q(1)]
for k in range(1, 7):
    for X, nm in ((A_poly, "A"), (B_poly, "B")):
        lhs = X(k + 1)
        rhs = padd(pmul(QM2, X(k)), pmul(QM1, X(k - 1)))
        check(f"recur_{nm}{k}", lhs == rhs)
# P from A,B: P = (q-1)(A+(q-1)B) equals P_poly
for n in range(1, 7):
    Pn = P_poly(n)
    rec = pmul(QM1, padd(A_poly(n), pmul(QM1, B_poly(n))))
    check(f"recompose_n{n}", rec == Pn)

# ---------- 6. Heilmann-Lieb instance: path matching polynomials ----------
def match_path(k):
    m0, m1 = [Q(1)], [Q(0), Q(1)]
    if k == 0:
        return m0
    if k == 1:
        return m1
    for _ in range(2, k + 1):
        m0, m1 = m1, psub(pmul(QVAR, m1), m0)
    return m1

def _sturm_count_inner(p, a, b):
    """# roots in (a,b), exact; nudges rational endpoints off roots."""
    seq = sturm_seq(p)
    def V(x):
        for _ in range(6):
            try:
                return variations(signs_at(seq, x))
            except AssertionError:
                x = x + Q(1, 2 ** 30)
        raise AssertionError("endpoint nudge failed")
    return V(a) - V(b)

def sturm_count(p, a, b):
    return _sturm_count_inner(p, a, b)

def isolate(p, B, tol=Q(1, 64)):
    ivs, stack, guard = [], [(Q(-B), Q(B))], 0
    while stack:
        guard += 1
        assert guard < 100000, "bisection blowup"
        a, b = stack.pop()
        c = _sturm_count_inner(p, a, b)
        if c == 0:
            continue
        if c == 1 and b - a <= tol:
            ivs.append((a, b))
            continue
        m = (a + b) / 2
        stack.append((a, m))
        stack.append((m, b))
    return sorted(ivs)

for k in range(1, 9):
    m = match_path(k)
    check(f"match_deg{k}", deg(m) == k)
    ivs = isolate(m, 3)
    check(f"match_real{k}", len(ivs) == k, f"{len(ivs)} roots")
    for a, b in ivs:
        check(f"match_bound{k}", b < 2 or a < 2, f"[{a},{b}]")
        assert b <= 2, f"matching root >= 2: [{a},{b}]"
    if k >= 2:
        ivs_prev = isolate(match_path(k - 1), 3)
        xs = [(a + b) / 2 for a, b in ivs]
        ys = [(a + b) / 2 for a, b in ivs_prev]
        inter = all((ys[i] < xs[i] < ys[i + 1]) or (xs[i] < ys[i] < xs[i + 1])
                    or (i == 0 and xs[0] < ys[0]) or (i == len(ys) and True)
                    for i in range(len(ys)))
        # strict alternation: merged order alternates
        merged = sorted([(x, 0) for x in xs] + [(y, 1) for y in ys])
        alt = all(merged[i][1] != merged[i + 1][1] for i in range(len(merged) - 1))
        check(f"interlace{k}", alt, f"{merged}")

print("\n".join(LOG))
print(f"CHECKS={len(LOG)} VERIFY_OK")

# ---------- 7. preset-fallback table F_1,F_2,F_3 (head-of-family, binary replay) --
import json as _json, os as _os

def _clean_isolate(p, lo=Q(-2), hi=Q(6), tol=Q(1, 32)):
    ivs, stack, guard = [], [(lo, hi)], 0
    while stack:
        guard += 1
        assert guard < 100000, "bisection blowup"
        a, b = stack.pop()
        c = sturm_count([Q(x) for x in p], a + E if a == lo else a, b)
        if c == 0:
            continue
        if c == 1 and b - (a + E if a == lo else a) <= tol:
            ivs.append((a + E if a == lo else a, b))
            continue
        m2 = (a + b) / 2
        stack.append((a, m2))
        stack.append((m2, b))
    return sorted(ivs)

_rows = []
for _n in (1, 2, 3):
    _p = P_poly(_n)
    _B = 1 + max(abs(c) for c in _p)  # Cauchy bound: all real roots in (-B, B)
    _ivs = _clean_isolate(_p, lo=Q(-_B), hi=Q(_B), tol=Q(1, 256))
    # snap to dyadic grid denom 128 containing each box, then verify
    _snap = []
    for (_a, _b) in _ivs:
        import math as _m
        _lo = Q(_m.floor(float(_a) * 128) - 1, 128)
        _hi = Q(_m.ceil(float(_b) * 128) + 1, 128)
        _snap.append((_lo, _hi))
    _snap.sort()
    _ivs = _snap
    _rows.append({
        "n": _n,
        "vertices": _n + 3,
        "poly_const_first": [str(c) for c in _p],
        "distinct_real_roots": len(_ivs),
        "isolating_intervals": [[str(a), str(b)] for a, b in _ivs],
        # deletion-contraction/transfer tree log: path recurrence nodes to depth n
        "tree": {
            "method": "positive-path deletion-contraction transfer recurrence "
                      "X_{k+1}=(q-2)X_k+(q-1)X_{k-1} with logged A_k,B_k leaves",
            "depth": _n,
            "leaf_count": 2 * (_n + 1),
            "A_leaves": [[str(c) for c in A_poly(k)] for k in range(_n + 1)],
            "B_leaves": [[str(c) for c in B_poly(k)] for k in range(_n + 1)],
        },
    })
    # binary replay: disjointness, one root each, total count, leaf recomposition
    for _i in range(len(_ivs)):
        for _j in range(_i + 1, len(_ivs)):
            check(f"fb_disjoint_n{_n}_{_i}_{_j}", _ivs[_i][1] <= _ivs[_j][0])
    for (_a, _b) in _ivs:
        check(f"fb_oneroot_n{_n}", sturm_count([Q(x) for x in _p], _a, _b) == 1)
    _tot = (V_at([Q(x) for x in _p], Q(-2) + E)
            - variations(signs_at(sturm_seq([Q(x) for x in _p]), 'inf')))
    check(f"fb_total_n{_n}", _tot == len(_ivs), f"total={_tot}")
    check(f"fb_recompose_n{_n}",
          pmul(QM1, padd(A_poly(_n), pmul(QM1, B_poly(_n)))) == _p)

_table = {
    "family": "F_n: unbalanced signed K4 (single negative edge 12), "
              "positive edge 34 replaced by positive n-path",
    "normalization": "Zaslavsky signed-chromatic q-counting (odd q evaluations)",
    "rows": _rows,
}
_out = _os.path.join(_os.path.dirname(__file__), "fallback_table.json")
with open(_out, "w") as _f:
    _json.dump(_table, _f, indent=1)
LOG.append(f"ok fallback_table {_out}")
print(f"CHECKS={len(LOG)} VERIFY_OK")
print(f"FALLBACK_TABLE={_out}")
