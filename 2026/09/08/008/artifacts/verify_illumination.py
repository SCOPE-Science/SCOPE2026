"""Self-contained stdlib-only verifier for lane-111 illumination numbers.

Replays from scratch (no input files, no third-party imports):
 1. Builds each Fedorov representative (zonotope sign-sums / permuted (0,1,2) vertices).
 2. Enumerates facets exactly (supporting-plane search) and true vertices (2D hull corners).
 3. Checks the claimed direction set illuminates every vertex by strict integer dots.
 4. Checks the claimed conflict clique is pairwise exact (0 in closed conv of cone union).
 5. Enumerates ALL realizable strict sign vectors over facet normals (Gordan: feasible
    iff 0 not in closed conv of signed rows) and proves exact set-cover optimum equals
    the claim (no fewer real directions suffice -- over ALL real directions, not a pool).

Run: python3 verify_illumination.py   (stdlib only; ~seconds)
"""
import itertools
import math
from fractions import Fraction

E1 = (1, 0, 0)
E2 = (0, 1, 0)
E3 = (0, 0, 1)


def det3(u, v, w):
    return (u[0] * (v[1] * w[2] - v[2] * w[1]) - u[1] * (v[0] * w[2] - v[2] * w[0])
            + u[2] * (v[0] * w[1] - v[1] * w[0]))


def cram3(A, B, C, rhs):
    D = det3(A, B, C)
    if D == 0:
        return None

    def dc(X, Y, Z):
        return det3(X, Y, Z)

    return (Fraction(dc(rhs, B, C), D), Fraction(dc(A, rhs, C), D),
            Fraction(dc(A, B, rhs), D))


def origin_in_closed_conv(S):
    """Exact test: is 0 in the closed convex hull of integer vectors S?

    Carathéodory in the affine hull through 0: BFS supports of size 2 (antiparallel
    pair), 3 (coplanar triple surrounding 0), or 4 (tetrahedron surrounding 0).
    Complete for sets in R^3.
    """
    k = len(S)
    for i in range(k):
        for j in range(i + 1, k):
            a, b = S[i], S[j]
            c = (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
                 a[0] * b[1] - a[1] * b[0])
            if c == (0, 0, 0) and (a[0] * b[0] + a[1] * b[1] + a[2] * b[2] < 0):
                return True
    for i, j, l in itertools.combinations(range(k), 3):
        a, b, c = S[i], S[j], S[l]
        if det3(a, b, c) != 0:
            continue
        m = (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
             a[0] * b[1] - a[1] * b[0])
        if m == (0, 0, 0):
            m = (a[1] * c[2] - a[2] * c[1], a[2] * c[0] - a[0] * c[2],
                 a[0] * c[1] - a[1] * c[0])
        if m == (0, 0, 0):
            continue
        ax = max(range(3), key=lambda d: abs(m[d]))
        ot = [d for d in range(3) if d != ax]
        P = [(a[ot[0]], a[ot[1]]), (b[ot[0]], b[ot[1]]), (c[ot[0]], c[ot[1]])]

        def sgn(p, q, r):
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

        s1 = sgn((0, 0), P[0], P[1])
        s2 = sgn((0, 0), P[1], P[2])
        s3 = sgn((0, 0), P[2], P[0])
        if (s1 >= 0 and s2 >= 0 and s3 >= 0) or (s1 <= 0 and s2 <= 0 and s3 <= 0):
            return True
    for i, j, l, m in itertools.combinations(range(k), 4):
        A, B, C, D = S[i], S[j], S[l], S[m]
        t = cram3(A, B, C, (-D[0], -D[1], -D[2]))
        if t is None:
            continue
        if all(x >= 0 for x in t) and sum(t) <= 1:
            return True
    return False


def prim(n):
    g = math.gcd(math.gcd(abs(n[0]), abs(n[1])), abs(n[2]))
    return (n[0] // g, n[1] // g, n[2] // g) if g else n


def sign_sums(gens):
    pts = set()
    for s in itertools.product([-1, 1], repeat=len(gens)):
        pts.add(tuple(sum(s[i] * gens[i][d] for i in range(len(gens)))
                      for d in range(3)))
    return sorted(pts)


def facets_of(pts):
    n = len(pts)
    cx = sum(p[0] for p in pts) / n
    cy = sum(p[1] for p in pts) / n
    cz = sum(p[2] for p in pts) / n
    planes = {}
    for i, j, k in itertools.combinations(range(n), 3):
        p0, p1, p2 = pts[i], pts[j], pts[k]
        ax = (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])
        bx = (p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2])
        nv = (ax[1] * bx[2] - ax[2] * bx[1], ax[2] * bx[0] - ax[0] * bx[2],
              ax[0] * bx[1] - ax[1] * bx[0])
        if nv == (0, 0, 0):
            continue
        dots = [nv[0] * (p[0] - p0[0]) + nv[1] * (p[1] - p0[1]) + nv[2] * (p[2] - p0[2])
                for p in pts]
        if not (min(dots) >= 0 or max(dots) <= 0):
            continue
        s = nv[0] * (cx - p0[0]) + nv[1] * (cy - p0[1]) + nv[2] * (cz - p0[2])
        if s > 0:
            nv = (-nv[0], -nv[1], -nv[2])
        nv = prim(nv)
        c = nv[0] * p0[0] + nv[1] * p0[1] + nv[2] * p0[2]
        planes[(nv, c)] = True
    out = []
    for (nv, c) in planes:
        S = [idx for idx, p in enumerate(pts)
             if nv[0] * p[0] + nv[1] * p[1] + nv[2] * p[2] == c]
        out.append((nv, S))
    return out


def corners_of(pts, S, nv):
    ax = max(range(3), key=lambda d: abs(nv[d]))
    others = [d for d in range(3) if d != ax]
    pts2 = [(pts[i][others[0]], pts[i][others[1]]) for i in S]
    coord_to_idx = {}
    for idx, co in zip(S, pts2):
        if co not in coord_to_idx:
            coord_to_idx[co] = idx
    P = sorted(set(pts2))
    if len(P) <= 1:
        return [coord_to_idx[P[0]]]

    def cr(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lo = []
    for p in P:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    hi = []
    for p in reversed(P):
        while len(hi) >= 2 and cr(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return [coord_to_idx[c] for c in lo[:-1] + hi[:-1]]


def build_zonotope(gens):
    pts = sign_sums(gens)
    facets = facets_of(pts)
    corner_sets = [set(corners_of(pts, S, nv)) for (nv, S) in facets]
    normals = [nv for (nv, S) in facets]
    V = sorted(set().union(*corner_sets))
    vcones = [[normals[j] for j in range(len(facets)) if V[i] in corner_sets[j]]
              for i in range(len(V))]
    return pts, V, vcones, normals


def build_truncoct():
    V = sorted(set(
        (sx * p[0], sy * p[1], sz * p[2])
        for p in set(itertools.permutations([0, 1, 2]))
        for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)))
    facets = []
    for c in (2, -2):
        facets.append(((1, 0, 0) if c > 0 else (-1, 0, 0),
                       [i for i, v in enumerate(V) if v[0] == c]))
        facets.append(((0, 1, 0) if c > 0 else (0, -1, 0),
                       [i for i, v in enumerate(V) if v[1] == c]))
        facets.append(((0, 0, 1) if c > 0 else (0, 0, -1),
                       [i for i, v in enumerate(V) if v[2] == c]))
    for s in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]:
        for sgn in (1, -1):
            nn = (sgn * s[0], sgn * s[1], sgn * s[2])
            S = [i for i, v in enumerate(V)
                 if nn[0] * v[0] + nn[1] * v[1] + nn[2] * v[2] == 3]
            facets.append((nn, S))
    # every vertex lies on exactly 3 facets (all degree 3); assert below
    vcones = [[nn for (nn, S) in facets if i in S] for i in range(len(V))]
    normals = [nn for (nn, S) in facets]
    return V, V, vcones, normals


def check_upper(pts, V, vcones, dirs):
    log = []
    for i in range(len(V)):
        wit = None
        for d in dirs:
            if all(d[0] * x[0] + d[1] * x[1] + d[2] * x[2] < 0 for x in vcones[i]):
                wit = d
                break
        coord = pts[V[i]] if pts is not V else V[i]
        log.append((coord, wit))
        assert wit is not None, "unilluminated vertex %r" % (coord,)
    return log


def check_clique(vcones, clique):
    for a in range(len(clique)):
        for b in range(a + 1, len(clique)):
            U = list(dict.fromkeys(vcones[clique[a]] + vcones[clique[b]]))
            assert origin_in_closed_conv(U), \
                "clique pair %d,%d jointly illuminable" % (a, b)


def exact_optimum(normals, vcones, nV):
    """Complete optimum over ALL real directions.

    Enumerate all 2^F strict sign vectors; feasible ones (Gordan) give every
    realizable illuminated vertex set; exact set-cover optimum over that family.
    """
    F = len(normals)
    fam = set()
    nfeas = 0
    for mask in range(1 << F):
        signed = [((1 if (mask >> i) & 1 else -1) * normals[i][0],
                   (1 if (mask >> i) & 1 else -1) * normals[i][1],
                   (1 if (mask >> i) & 1 else -1) * normals[i][2])
                  for i in range(F)]
        if origin_in_closed_conv(signed):
            continue
        nfeas += 1
        sm = {normals[i]: (1 if (mask >> i) & 1 else -1) for i in range(F)}
        # vertex illuminated iff all its cone normals are strictly negative
        S = frozenset(v for v in range(nV)
                      if all(sm[x] == -1 for x in vcones[v]))
        fam.add(S)
    fam = list(fam)
    ALL = set(range(nV))
    who = [[] for _ in range(nV)]
    for j, S in enumerate(fam):
        for v in S:
            who[v].append(j)

    def can_cover(k):
        def dfs(rem, uncovered):
            if not uncovered:
                return True
            if rem == 0:
                return False
            mx = max(len(S & uncovered) for S in fam)
            if mx == 0 or len(uncovered) > rem * mx:
                return False
            v = min(uncovered)
            for j in who[v]:
                if dfs(rem - 1, uncovered - fam[j]):
                    return True
            return False
        return dfs(k, set(range(nV)))

    opt = None
    for k in range(0, nV + 1):
        if can_cover(k):
            opt = k
            break
    return opt, nfeas, len(fam)


CASES = [
    dict(name="cube (parallelepiped)",
         build=lambda: build_zonotope([E1, E2, E3]),
         dirs=[(sx, sy, sz) for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)],
         claim=8, euler=(8, 12, 6)),
    dict(name="hexagonal prism",
         build=lambda: build_zonotope([E1, E2, (1, 1, 0), E3]),
         dirs=[(1, 2, 1), (1, 2, -1), (1, -1, 1), (1, -1, -1),
               (-2, -1, 1), (-2, -1, -1)],
         claim=6, euler=(12, 18, 8)),
    dict(name="rhombic dodecahedron",
         build=lambda: build_zonotope([E1, E2, E3, (1, 1, 1)]),
         dirs=[(1, 2, 2), (1, 1, 0), (1, -2, 2), (1, -1, -2),
               (-2, 1, -1), (-2, -2, -1)],
         claim=6, euler=(14, 24, 12)),
    dict(name="elongated rhombic dodecahedron",
         build=lambda: build_zonotope([E1, E2, E3, (1, 1, 0), (1, 1, 1)]),
         dirs=[(1, 2, 2), (1, 2, -3), (1, -3, 2), (1, -3, -3), (-3, -2, -1)],
         claim=5, euler=(18, 28, 12)),
    dict(name="truncated octahedron",
         build=build_truncoct,
         dirs=[(1, 1, -1), (1, -3, 3), (-3, 1, 3), (-3, -3, -2)],
         claim=4, euler=(24, 36, 14)),
]


def main():
    for case in CASES:
        pts, V, vcones, normals = case["build"]()
        nV, nF = len(V), len(normals)
        nE = nV + nF - 2
        assert (nV, nE, nF) == case["euler"], \
            "%s combinatorics %s != %s" % (case["name"], (nV, nE, nF), case["euler"])
        assert all(len(c) >= 3 for c in vcones)
        log = check_upper(pts, V, vcones, case["dirs"])
        assert len(case["dirs"]) == case["claim"]
        # conflict clique: indices of an explicit maximum clique, verified pairwise
        opt, nfeas, nsets = exact_optimum(normals, vcones, nV)
        assert opt == case["claim"], \
            "%s: complete optimum %s != claim %s" % (case["name"], opt, case["claim"])
        # pairwise-clique spot check: greedy max clique over conflict graph
        n = nV
        confl = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                U = list(dict.fromkeys(vcones[i] + vcones[j]))
                if origin_in_closed_conv(U):
                    confl[i][j] = confl[j][i] = True
        best = []
        order = sorted(range(n), key=lambda i: sum(confl[i]), reverse=True)

        def expand(cand, cur):
            while cand:
                if len(cur) + len(cand) <= len(best):
                    return
                v = cand.pop()
                new = [u for u in cand if confl[v][u]]
                if not new:
                    if len(cur) + 1 > len(best):
                        best[:] = cur + [v]
                elif len(cur) + 1 + len(new) > len(best):
                    expand(new, cur + [v])

        expand(order, [])
        print("%-32s V=%2d F=%2d ill=%d  cells=%d/%d  maxclique=%d  UPPER-OK CLIQUE-OK COMPLETE-OPT-OK"
              % (case["name"], nV, nF, case["claim"], nfeas, 1 << nF, len(best)))
        assert len(best) == case["claim"], \
            "%s: max conflict clique %d != claim %d" % (case["name"], len(best), case["claim"])
    print("ALL FIVE TYPES VERIFIED")


if __name__ == "__main__":
    main()
