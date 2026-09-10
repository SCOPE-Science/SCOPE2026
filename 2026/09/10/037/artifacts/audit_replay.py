"""Independent audit replay for N4 F7^- fragile-doubleton claim.
Fresh code path: forward-only GF(3) elimination, full-subset lambda scan,
exhaustive (S,C) minor search with S7 bases-set isomorphism. No shared code
with n4_fragile.py / verify_n4.py. Reads NOTHING from those files; A4 numbers
copied from DRAFT.md independently re-typed.
"""
import itertools, json, sys, time

t0 = time.time()

A4 = [
 [2,0,2,1,2,1,0,0],
 [2,1,0,2,0,2,2,0],
 [2,0,2,0,0,1,0,0],
 [2,0,2,2,2,2,2,2],
 [0,1,1,1,1,1,1,1],
 [2,1,0,0,0,2,0,0],
 [2,0,0,2,2,2,2,0],
 [1,0,1,2,1,2,1,1],
]
DIM = 8
COLS = []
for i in range(8):
    v = [0]*8; v[i] = 1; COLS.append(v)
for j in range(8):
    COLS.append([A4[r][j] % 3 for r in range(8)])
N = 16
FULL = (1 << N) - 1

_RC = {}
def R(mask):
    v = _RC.get(mask)
    if v is not None:
        return v
    rows = [list(COLS[i]) for i in range(N) if (mask >> i) & 1]
    r = 0
    m = len(rows)
    for c in range(DIM):
        piv = -1
        for k in range(r, m):
            if rows[k][c] % 3:
                piv = k; break
        if piv < 0:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = 1 if rows[r][c] % 3 == 1 else 2
        pv = rows[r]
        for k in range(r + 1, m):
            if rows[k][c] % 3:
                f = (rows[k][c] * inv) % 3
                rk = rows[k]
                rows[k] = [(rk[d] - f * pv[d]) % 3 for d in range(DIM)]
        r += 1
        if r == DIM:
            break
    _RC[mask] = r
    return r

def pop(m):
    c = 0
    while m:
        c += m & 1; m >>= 1
    return c

# ---- F7^- reference (standard integer model), independent dim-3 rank ----
F = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,1],[1,1,1]]
def r3(rows):
    M = [list(x) for x in rows]
    r = 0
    for c in range(3):
        piv = -1
        for k in range(r, len(M)):
            if M[k][c] % 3:
                piv = k; break
        if piv < 0:
            continue
        M[r], M[piv] = M[piv], M[r]
        if M[r][c] % 3 == 2:
            M[r] = [(-x) % 3 for x in M[r]]
        for k in range(len(M)):
            if k != r and M[k][c] % 3:
                f = M[k][c] % 3
                M[k] = [(M[k][d] - f * M[r][d]) % 3 for d in range(3)]
        r += 1
    return r

TRIPS = list(itertools.combinations(range(7), 3))
FB = frozenset(t for t in TRIPS if r3([F[i] for i in t]) == 3)
FL = sorted(t for t in TRIPS if r3([F[i] for i in t]) <= 2)
def degseq(lines):
    d = [0]*7
    for t in lines:
        for i in t:
            d[i] += 1
    return sorted(d)
FDEG = degseq(FL)
print("F reference: rank=%d bases=%d lines=%d deg=%s" % (r3(F), len(FB), len(FL), FDEG), flush=True)
print("F lines:", FL, flush=True)
assert r3(F) == 3 and len(FB) == 29 and len(FL) == 6, "F model must be non-Fano"

PERMS = list(itertools.permutations(range(7)))
FB_PERMSET = set()
for p in PERMS:
    FB_PERMSET.add(frozenset(tuple(sorted((p[a], p[b], p[c]))) for (a, b, c) in FB))
print("distinct permuted F-bases families:", len(FB_PERMSET), flush=True)

def iso_perm(S, rf):
    Sm = 0
    for i in S:
        Sm |= (1 << i)
        if rf(1 << i) != 1:
            return None
    L = len(S)
    for a in range(L):
        for b in range(a + 1, L):
            if rf((1 << S[a]) | (1 << S[b])) != 2:
                return None
    if rf(Sm) != 3:
        return None
    B = set(); lines = []; deg = [0]*7
    for t in TRIPS:
        m = (1 << S[t[0]]) | (1 << S[t[1]]) | (1 << S[t[2]])
        if rf(m) == 3:
            B.add(t)
        else:
            lines.append(t)
            for i in t:
                deg[i] += 1
    if len(lines) != 6 or sorted(deg) != FDEG:
        return None
    if frozenset(B) not in FB_PERMSET:
        return None
    for p in PERMS:
        if frozenset(tuple(sorted((p[a], p[b], p[c]))) for (a, b, c) in B) == FB:
            return list(p)
    return None

def search_minor(Gmask, fixed):
    G = [i for i in range(N) if (Gmask >> i) & 1]
    rF = R(fixed)
    for S in itertools.combinations(G, 7):
        Sm = 0
        for i in S:
            Sm |= (1 << i)
        rest = [g for g in G if not ((Sm >> g) & 1)]
        nr = len(rest)
        for cb in range(1 << nr):
            Cm = fixed
            for k in range(nr):
                if (cb >> k) & 1:
                    Cm |= (1 << rest[k])
            rC = R(Cm)
            if R(Sm | Cm) - rC != 3:
                continue
            def rf(m, _C=Cm, _r=rC):
                return R(m | _C) - _r
            p = iso_perm(S, rf)
            if p is not None:
                return {"S": list(S), "C": [i for i in range(N) if (Cm >> i) & 1 and not ((fixed >> i) & 1)],
                        "fixed": [i for i in range(N) if (fixed >> i) & 1], "perm": p}
    return None

def min_lambda(Em):
    rE = R(Em)
    worst = 99; wx = None
    m = 0
    while m <= FULL:
        if (m & ~Em) == 0:
            k = pop(m)
            if 2 <= k <= pop(Em) - 2:
                lam = R(m) + R(Em ^ m) - rE
                if lam < worst:
                    worst = lam; wx = m
                    if worst < 2:
                        break
        m += 1
    return rE, worst, wx

print("N4 rank:", R(FULL), flush=True)
assert R(FULL) == 8

a, b = 0, 1
Em = FULL ^ ((1 << a) | (1 << b))
E = [i for i in range(N) if (Em >> i) & 1]
print("Em size:", len(E), flush=True)
rE, worst, wx = min_lambda(Em)
print("Em rank=%d min-lambda(2..12)=%d" % (rE, worst), flush=True)
assert worst >= 2, ("NOT 3-connected", wx, worst)

# positive cert replay (stored values from DRAFT)
S = [2,3,4,5,6,12,13]; C = [9,10,11,14,15]; D = [7,8]; perm = [0,3,1,4,2,5,6]
assert sorted(S + C + D) == sorted(E), "S,C,D must partition Em"
assert sorted(perm) == list(range(7)), "perm must be a permutation"
Cm = sum(1 << i for i in C)
rC = R(Cm)
Sm = sum(1 << i for i in S)
assert R(Sm | Cm) - rC == 3, "contracted rank must be 3"
def rf2(m, _C=Cm, _r=rC):
    return R(m | _C) - _r
for i in S:
    assert rf2(1 << i) == 1, ("loop in minor", i)
B = frozenset(t for t in TRIPS if rf2((1 << S[t[0]]) | (1 << S[t[1]]) | (1 << S[t[2]])) == 3)
assert len(B) == 29, ("minor bases != 29", len(B))
Bmapped = frozenset(tuple(sorted((perm[x], perm[y], perm[z]))) for (x, y, z) in B)
assert Bmapped == FB, "stored perm must carry minor bases exactly onto F7^- bases"
print("stored minor cert VERIFIED: S=%s C=%s D=%s perm maps 29 bases exactly" % (S, C, D), flush=True)

# independent re-search for a minor in Em (ignores stored cert)
found = search_minor(Em, 0)
print("independent Em minor search:", ("FOUND S=%s" % found["S"]) if found else "NONE", flush=True)
assert found is not None, "Em must have an F7^- minor"

# fragility replay: all 28 sides
EXPECTED = {2:(True,False),3:(True,False),4:(False,True),5:(True,False),6:(True,False),
            7:(True,False),8:(True,False),9:(False,True),10:(False,True),11:(False,True),
            12:(False,True),13:(False,True),14:(False,True),15:(False,True)}
allok = True; match = True
for e in E:
    Gd = Em ^ (1 << e)
    d = search_minor(Gd, 0) is not None
    assert R(1 << e) == 1, ("unexpected loop", e)
    c = search_minor(Gd, 1 << e) is not None
    frag = ((not d) or (not c))
    allok = allok and frag
    exp = EXPECTED[e]
    if (d, c) != exp:
        match = False
    print("e=%2d del=%s con=%s fragile=%s expected=%s" % (e, d, c, frag, exp), flush=True)
print("FRAGILE_ALL:", allok, "TABLE_MATCHES_DRAFT:", match, flush=True)
assert allok, "every element must be fragile"

# sanity: N4 itself 3-connected
rF, wF, _ = min_lambda(FULL)
print("N4 min-lambda(2..14)=%d" % wF, flush=True)

print("AUDIT_REPLAY_OK pair=(0,1) rank=%d minlam=%d fragrows=14/14 table_match=%s seconds=%.1f" % (
    rE, worst, match, time.time() - t0), flush=True)
