"""Program check for the preset fallback (q^5.5 forced-(7,4) wall).

Checks, in stdlib Python only:
  q=9 (square, Hermitian model): Hermitian locus x0^4+x1^4+x2^4=0 over F_9
    has 28 points; host H_9 has L=2268 lines, |E|=190512, |P|=81648 distinct
    pairs (pair-disjointness), pair bound |P|<=(9/16)9^5.5, edge bound
    |E|>=(1/4)9^6, and an explicit F of size ceil((3/4)9^5.5) contains 4
    distinct edges on <=6 vertices (exhibited).
  q=7 (non-square, lexicographic same-scale model): |S_7|=19, host/pair
    counts satisfy the same bounds; documents |E(H_7)| < (3/4)7^5.5, i.e. the
    wall claim is vacuous at q=7 (hence true), non-vacuous from q=8 up.
Emits output/artifacts/fallback_certificate.json and prints VERIFY_OK.
"""
import itertools, json, math, os

# ---------------- F_9 = F_3[x]/(x^2+1) ----------------
def f9_add(a, b): return ((a[0]+b[0]) % 3, (a[1]+b[1]) % 3)
def f9_neg(a): return ((-a[0]) % 3, (-a[1]) % 3)
def f9_mul(a, b):
    return ((a[0]*b[0]-a[1]*b[1]) % 3, (a[0]*b[1]+a[1]*b[0]) % 3)
def f9_inv(a):
    assert a != (0, 0)
    s = (a[0]*a[0]+a[1]*a[1]) % 3
    si = 1 if s == 1 else 2
    return ((a[0]*si) % 3, ((-a[1])*si) % 3)
F9 = [(a, b) for a in range(3) for b in range(3)]
ONE9, ZERO9 = (1, 0), (0, 0)
def f9_pow4(a):
    a2 = f9_mul(a, a)
    return f9_mul(a2, a2)

def pg_normalize(vec, add, neg, mul, inv, zero, one):
    for i, c in enumerate(vec):
        if c != zero:
            s = inv(c)
            return tuple(mul(s, x) for x in vec)
    raise ValueError("zero vector")

def build_case(q, field, S_dirs):
    """field: dict with els,add,neg,mul,zero,one. S_dirs: list of normalized dirs."""
    els, add, neg, mul = field['els'], field['add'], field['neg'], field['mul']
    zero, one = field['zero'], field['one']
    pts = list(itertools.product(els, repeat=3))
    pid = {p: i for i, p in enumerate(pts)}
    N = len(pts)
    Sset = set(S_dirs)
    lines = []
    for d in S_dirs:
        i = next(k for k, c in enumerate(d) if c != zero)
        buckets = {}
        for p, idx in pid.items():
            ci = p[i]
            key = tuple(add(p[k], neg(mul(ci, d[k]))) for k in range(3))
            buckets.setdefault(key, []).append(idx)
        for members in buckets.values():
            assert len(members) == q, (q, len(members))
            lines.append(sorted(members))
    assert len(lines) == len(S_dirs)*q*q
    edges = []
    for members in lines:
        for t in itertools.combinations(members, 3):
            edges.append(t)
    pair_owner = {}
    for li, members in enumerate(lines):
        for u, v in itertools.combinations(members, 2):
            k = (u, v) if u < v else (v, u)
            assert k not in pair_owner, "pair on two lines!"
            pair_owner[k] = li
    P = len(pair_owner)
    assert P == len(lines)*q*(q-1)//2
    return N, lines, edges, P

# ---------------- q = 9, Hermitian model ----------------
F = {'els': F9, 'add': f9_add, 'neg': f9_neg, 'mul': f9_mul,
     'zero': ZERO9, 'one': ONE9}
all_nz = [v for v in itertools.product(F9, repeat=3) if v != (ZERO9, ZERO9, ZERO9)]
pg9 = sorted(set(pg_normalize(v, f9_add, f9_neg, f9_mul, f9_inv, ZERO9, ONE9)
                  for v in all_nz))
assert len(pg9) == 9*9+9+1 == 91
S9 = [d for d in pg9
      if f9_add(f9_add(f9_pow4(d[0]), f9_pow4(d[1])), f9_pow4(d[2])) == ZERO9]
assert len(S9) == 28, len(S9)  # Hermitian arc: r^3+1 = 27+1
N9, lines9, edges9, P9 = build_case(9, F, S9)
M9 = len(edges9)
thr9 = math.ceil(0.75*9**5.5)
Fsub = edges9[:thr9]
pdeg = {}
for (a, b, c) in Fsub:
    for u, v in ((a, b), (a, c), (b, c)):
        k = (u, v) if u < v else (v, u)
        pdeg[k] = pdeg.get(k, 0)+1
star_pair, star_deg = max(pdeg.items(), key=lambda kv: kv[1])
assert star_deg >= 4, star_deg
star_edges = [e for e in Fsub if star_pair[0] in e and star_pair[1] in e][:4]
assert len(star_edges) == 4 and len(set(star_edges)) == 4
U = set()
for e in star_edges:
    U.update(e)
assert len(U) <= 6, U
cert9 = dict(q=9, model="hermitian x0^4+x1^4+x2^4=0 over F9",
             S_size=len(S9), N=N9, nlines=len(lines9), M=M9, P=P9,
             pair_bound=float(9/16*9**5.5), edge_floor=float(9**6/4),
             threshold_Cqq=thr9, star_pair=star_pair, star_deg=star_deg,
             star_edges=[list(e) for e in star_edges], union_size=len(U))

# ---------------- q = 7, lexicographic same-scale model ----------------
Fp = {'els': list(range(7)),
      'add': lambda a, b: (a+b) % 7, 'neg': lambda a: (-a) % 7,
      'mul': lambda a, b: (a*b) % 7, 'zero': 0, 'one': 1}
def modinv(a):
    return pow(a, -1, 7)
all_nz7 = [v for v in itertools.product(range(7), repeat=3) if v != (0, 0, 0)]
def norm7(v):
    for c in v:
        if c != 0:
            s = modinv(c)
            return tuple((s*x) % 7 for x in v)
    raise ValueError
pg7 = sorted(set(norm7(v) for v in all_nz7))
assert len(pg7) == 57
m7 = math.floor(7**1.5)+1
assert m7 == 19
S7 = pg7[:m7]
N7, lines7, edges7, P7 = build_case(7, Fp, S7)
M7 = len(edges7)
T7 = 0.75*7**5.5
cert7 = dict(q=7, model="lexicographic same-scale |S|=floor(7^1.5)+1",
             S_dirs=S7, N=N7, nlines=len(lines7), M=M7, P=P7,
             pair_bound=float(9/16*7**5.5), edge_floor=float(7**6/4),
             threshold=float(T7), vacuous=bool(M7 < T7))
assert P7 <= 9/16*7**5.5 and M7 >= 7**6/4
assert P9 <= 9/16*9**5.5 and M9 >= 9**6/4
assert M7 < T7  # wall claim vacuous (hence true) at q=7

cert = dict(C="3/4", q0=7, c0="1/4", q9=cert9, q7=cert7)
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "fallback_certificate.json"), "w") as f:
    json.dump(cert, f, indent=1, default=str)
print("q=9: |S|=28 N=729 lines=2268 M=%d P=%d thr=%d star_deg=%d union=%d"
      % (M9, P9, thr9, star_deg, len(U)))
print("q=7: |S|=19 N=343 lines=931 M=%d P=%d thr=%.2f vacuous=%s"
      % (M7, P7, T7, M7 < T7))
print("VERIFY_OK")
