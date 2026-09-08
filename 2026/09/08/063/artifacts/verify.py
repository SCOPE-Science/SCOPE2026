# Independent verifier for complete (k,3)-arc witnesses (stdlib only).
# Rebuilds PG(2,q) incidence from scratch, checks occupancy<=3, completeness,
# spectrum sums, and the dimension-3 NMDS weight distribution. Usage:
#   python3 verify.py wit7.json [wit8.json ...]
import json, sys

class GF8:
    MOD = 0xB
    @staticmethod
    def add(a, b): return a ^ b
    @staticmethod
    def mul(a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            a <<= 1
            if a & 0x8: a ^= GF8.MOD
            b >>= 1
        return r & 0x7

def build(q):
    if q == 7:
        add = lambda a, b: (a + b) % 7
        mul = lambda a, b: (a * b) % 7
        def norm(v):
            nz = next(c for c in v if c != 0)
            inv = pow(nz, -1, 7)
            return tuple((c * inv) % 7 for c in v)
    elif q == 8:
        add, mul = GF8.add, GF8.mul
        def norm(v):
            nz = next(c for c in v if c != 0)
            for b in range(1, 8):
                if GF8.mul(nz, b) == 1: inv = b; break
            return (GF8.mul(v[0], inv), GF8.mul(v[1], inv), GF8.mul(v[2], inv))
    else:
        raise ValueError(q)
    pts, seen = [], {}
    rng = range(q) if q == 7 else range(8)
    for x in rng:
        for y in rng:
            for z in rng:
                if x == y == z == 0: continue
                n = norm((x, y, z))
                if n not in seen:
                    seen[n] = len(pts); pts.append(n)
    lines = list(pts)
    line_pts = []
    for (a, b, c) in lines:
        s = [i for i, (x, y, z) in enumerate(pts)
             if add(add(mul(a, x), mul(b, y)), mul(c, z)) == 0]
        line_pts.append(s)
    return pts, line_pts

def check_file(fn):
    W = json.load(open(fn))
    q, k = W['q'], W['k']
    pts, line_pts = build(q)
    N = q * q + q + 1
    assert len(pts) == N and len(line_pts) == N, (len(pts), len(line_pts))
    for s in line_pts:
        assert len(s) == q + 1, len(s)
    idx = {p: i for i, p in enumerate(pts)}
    S = set()
    for c in W['coords']:
        t = tuple(c)
        assert t in idx, ('bad point', c)
        S.add(idx[t])
    assert len(S) == k, (len(S), k)
    occ = [sum(1 for p in lp if p in S) for lp in line_pts]
    mx = max(occ)
    assert mx <= 3, ('4-secant!', mx)
    n = [occ.count(i) for i in range(4)]
    assert sum(n) == N, n
    assert sum(i * n[i] for i in range(4)) == k * (q + 1), 'incidence count'
    # completeness: every outside point on a 3-secant
    uncovered, covers = [], {}
    for p in range(N):
        if p in S: continue
        found = None
        for li, lp in enumerate(line_pts):
            if p in lp and occ[li] == 3:
                found = li; break
        if found is None: uncovered.append(p)
        else: covers[p] = found
    assert not uncovered, ('incomplete', uncovered)
    # NMDS weight distribution from spectrum: A_{k-i} = n_i*(q-1)
    A = {0: 1}
    for i in range(4):
        A[k - i] = n[i] * (q - 1)
    assert sum(A.values()) == q ** 3, A
    assert min(w for w in A if A[w] > 0 and w > 0) == k - 3, 'NMDS distance'
    print(f"{fn}: VERIFY_OK q={q} k={k} N={N} spectrum(n0..n3)={n} "
          f"NMDS={ {w: A[w] for w in sorted(A)} } uncovered=0 maxocc={mx}")
    return {'file': fn, 'q': q, 'k': k, 'spectrum': n, 'weights': A}

if __name__ == '__main__':
    out = [check_file(f) for f in sys.argv[1:]]
    print('ALL_OK', json.dumps(out, default=str))
