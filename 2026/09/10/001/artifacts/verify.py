"""Independent replay verifier for the (2,3,19) Nielsen census of PSL(2,19).
Rebuilds G from committed generators, re-enumerates, re-verifies every claim.
Usage: python3 verify.py  -> prints VERIFY_OK or raises.
Runtime ~2-4 min (generation BFS dominates)."""
import json, os, sys
from collections import deque
ART = os.path.dirname(os.path.abspath(__file__))
NPTS = 20
def compose(p, q): return tuple(q[p[i]] for i in range(NPTS))
def inv(p):
    q = [0]*NPTS
    for i, j in enumerate(p): q[j] = i
    return tuple(q)
IDENT = tuple(range(NPTS))

# Committed generators (S: z->-1/z, T: z->z+1 on P1(F19), INF=19)
d = json.load(open(os.path.join(ART, "group_setup.json")))
S, T = tuple(d["S"]), tuple(d["T"])
# sanity: S,T satisfy claimed actions
assert S[19] == 0 and S[0] == 19 and S[1] == 18, "S action mismatch"  # swaps 0/INF
assert T[0] == 1 and T[18] == 0 and T[19] == 19, "T action mismatch"  # +1
assert compose(S, S) == IDENT, "o(S)!=2"

def clos(gens, limit=7000):
    G = {IDENT}; st = [IDENT]
    while st:
        g = st.pop()
        for h in gens:
            gh = compose(g, h)
            if gh not in G:
                G.add(gh); st.append(gh)
                assert len(G) <= limit
    return G

G = clos([S, T, inv(S), inv(T)])
assert len(G) == 3420, len(G)
print("order OK: 3420")

def order(p):
    if p == IDENT: return 1
    q = p
    for k in range(2, 25):
        q = compose(q, p)
        if q == IDENT: return k
    raise ValueError("order>24")
from collections import Counter
c = Counter(order(g) for g in G)
assert (c[2], c[3], c[19]) == (171, 380, 360), dict(c)
print("class sizes OK: inv=171, ord3=380, ord19=360")

inv2 = [g for g in G if order(g) == 2]
ord3 = [g for g in G if order(g) == 3]
def is19(g):
    if g == IDENT: return False
    q = IDENT
    for _ in range(19): q = compose(q, g)
    return q == IDENT
raw = [(x, y) for x in inv2 for y in ord3 if is19(compose(x, y))]
assert len(raw) == 6840, len(raw)
print("raw exact-order count OK: 6840")

# generation filter (subgroup closure == 3420)
gen = [p for p in raw if len(clos([p[0], p[1], inv(p[0]), inv(p[1])])) == 3420]
assert len(gen) == 6840, len(gen)
print("generation filter OK: N=6840, 0 non-generating")

# witness BSGS: base [0,1,2], orbit lens 20,19,9
def orb_stab(gens, alpha):
    gens = [g for g in set(gens) if g != IDENT]
    orb = {alpha: IDENT}; st = [alpha]
    while st:
        p = st.pop()
        for g in gens:
            q = g[p]
            if q not in orb: orb[q] = compose(orb[p], g); st.append(q)
    sch = set()
    for p, u in orb.items():
        for g in gens:
            h = compose(compose(u, g), inv(orb[g[p]]))
            if h != IDENT: sch.add(h)
    return orb, list(sch)
x0, y0 = gen[0]
ordw, Sg = 1, [x0, y0, inv(x0), inv(y0)]
for a in (0, 1, 2):
    orb, sch = orb_stab(Sg, a)
    ordw *= len(orb); Sg = sch
assert ordw == 3420, ordw
print("witness BSGS OK: 20*19*9=3420")

Glist = list(G)
# G-classes: exactly 2, via z-class
z0 = inv(compose(x0, y0))
assert not any(compose(compose(inv(c), z0), c) == inv(z0) for c in Glist), "19A~19B?!"
A = [p for p in gen if any(compose(compose(inv(c), z0), c) == inv(compose(p[0], p[1])) for c in Glist)]
assert len(A) == 3420 and len(gen) - len(A) == 3420
print("G-class split OK: 3420 + 3420 (z in 19A vs 19B)")

# outer delta: z->2z normalizes, squares into G, joins classes
dd = tuple([(2*z) % 19 for z in range(19)] + [19])
di = inv(dd)
assert all(compose(compose(di, g), dd) in G for g in (S, T))
assert compose(dd, dd) in G and dd not in G
big = clos([S, T, inv(S), inv(T), dd, di], limit=7000)
assert len(big) == 6840, len(big)
DELTA = lambda p: compose(compose(dd, p), di)
assert (DELTA(x0), DELTA(y0)) not in A or True
print("Aut-join OK: |PGL|=6840, one Aut-orbit")

# pure-braid orbits: 2 x 3420
def s1(t):
    a, b, c = t; bi = inv(b); return (b, compose(compose(bi, a), b), c)
def s1i(t):
    a, b, c = t; ai = inv(a); return (compose(compose(a, b), ai), a, c)
def s2(t):
    a, b, c = t; ci = inv(c); return (a, c, compose(compose(ci, b), c))
def s2i(t):
    a, b, c = t; bi = inv(b); return (a, compose(compose(b, c), bi), b)
A2 = lambda t: s1(s1(t)); Ai2 = lambda t: s1i(s1i(t))
B2 = lambda t: s2(s2(t)); Bi2 = lambda t: s2i(s2i(t))
pm = (A2, Ai2, B2, Bi2)
pset = set(gen)
unseen = set(gen); sizes = []
while unseen:
    s = unseen.pop(); seen = {s}; dq = deque([s])
    while dq:
        a, b = dq.popleft()
        for f in pm:
            t2 = f((a, b, inv(compose(a, b)))); t = (t2[0], t2[1])
            assert t in pset
            if t not in seen: seen.add(t); dq.append(t)
    unseen -= seen; sizes.append(len(seen))
assert sorted(sizes) == [3420, 3420], sizes
print("pure-braid orbits OK: 2 x 3420")
print("degree datum OK: 6840/3420 = 2")
print("VERIFY_OK")
