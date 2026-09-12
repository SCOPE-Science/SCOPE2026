"""Exact certificate for the joint signing: integer characteristic polynomial
(LeVerrier), closed-form factorisation, exact LDL Ramanujan bound, and exact
40-vertex lift girth census. Prints the certificate values."""
import json
from collections import deque
from fractions import Fraction

N = 20
EDGES = []
for i in range(10):
    EDGES.append((i, (i + 1) % 10))
    EDGES.append((i, 10 + i))
    EDGES.append((10 + i, 10 + ((i + 3) % 10)))
EDGE_INDEX = {tuple(sorted(e)): i for i, e in enumerate(EDGES)}
ADJ = {v: sorted(w for w in range(N) if tuple(sorted((v, w))) in EDGE_INDEX)
       for v in range(N)}

CENSUS = json.load(open("artifacts/girth_census.json"))
TREE = set(CENSUS["tree_edges"])
COTREE = CENSUS["cotree"]
MASK = CENSUS["unfolding_mask"]


def sign_of(ei):
    if ei in TREE:
        return 1
    return -1 if (MASK >> COTREE.index(ei)) & 1 else 1


def signed_matrix():
    A = [[0] * N for _ in range(N)]
    for (u, v), ei in EDGE_INDEX.items():
        s = sign_of(ei)
        A[u][v] = s
        A[v][u] = s
    return A


def charpoly_leverrier(M):
    n = len(M)
    Af = [[Fraction(M[i][j]) for j in range(n)] for i in range(n)]
    Mk = [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
          for i in range(n)]
    c = [Fraction(0)] * (n + 1)
    c[n] = Fraction(1)
    for k in range(1, n + 1):
        AM = [[sum(Af[i][t] * Mk[t][j] for t in range(n)) for j in range(n)]
              for i in range(n)]
        ck = -sum(AM[i][i] for i in range(n)) / k
        c[n - k] = ck
        Mk = [[AM[i][j] + (ck if i == j else 0) for j in range(n)]
              for i in range(n)]
    assert all(x.denominator == 1 for x in c)
    return [int(x) for x in c]


def ldl_pivots(M):
    n = len(M)
    B = [[Fraction(M[i][j]) for j in range(n)] for i in range(n)]
    piv = []
    for k in range(n):
        piv.append(B[k][k])
        if B[k][k] <= 0:
            return piv, False
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                B[i][j] -= B[i][k] * B[k][j] / B[k][k]
    return piv, True


def count_cycles(adjmap, nverts, L):
    seen = set()

    def dfs(start, cur, depth, path, vis):
        if depth == L:
            if start in adjmap[cur]:
                rots = [tuple(path[(i + j) % L] for j in range(L))
                        for i in range(L)]
                rev = tuple(reversed(path))
                rots += [tuple(rev[(i + j) % L] for j in range(L))
                         for i in range(L)]
                seen.add(min(rots))
            return
        for w in adjmap[cur]:
            if w == start or w in vis:
                continue
            vis.add(w)
            path.append(w)
            dfs(start, w, depth + 1, path, vis)
            path.pop()
            vis.remove(w)

    for s in range(nverts):
        dfs(s, s, 1, [s], {s})
    return seen


def main():
    A = signed_matrix()
    cp = charpoly_leverrier(A)
    assert cp == [0] * 8 + [15625, 0, -18750, 0, 9375, 0, -2500, 0,
                            375, 0, -30, 0, 1], cp
    # closed form (x^2-5)^6 x^8
    s = [15625, -18750, 9375, -2500, 375, -30, 1]
    rem = s[:]
    for _ in range(6):
        assert sum(rem[i] * 5 ** i for i in range(len(rem))) == 0
        nxt = [0] * len(rem)
        nxt[-1] = rem[-1]
        for k in range(len(rem) - 2, -1, -1):
            nxt[k] = rem[k] + 5 * nxt[k + 1]
        assert nxt[0] == 0
        rem = nxt[1:]
    assert rem == [1], rem
    Np = [[(141 if i == j else 0) - 50 * A[i][j] for j in range(N)]
          for i in range(N)]
    Nm = [[(141 if i == j else 0) + 50 * A[i][j] for j in range(N)]
          for i in range(N)]
    piv_p, ok_p = ldl_pivots(Np)
    piv_m, ok_m = ldl_pivots(Nm)
    assert ok_p and ok_m
    assert Fraction(141, 50) ** 2 < 8
    ladj = {k: [] for k in range(40)}
    for (u, v), ei in EDGE_INDEX.items():
        if sign_of(ei) == 1:
            ladj[u].append(v)
            ladj[v].append(u)
            ladj[u + 20].append(v + 20)
            ladj[v + 20].append(u + 20)
        else:
            ladj[u].append(v + 20)
            ladj[v + 20].append(u)
            ladj[u + 20].append(v)
            ladj[v].append(u + 20)
    assert all(len(ladj[k]) == 3 for k in range(40))
    c4 = count_cycles(ladj, 40, 4)
    c6 = count_cycles(ladj, 40, 6)
    c8 = count_cycles(ladj, 40, 8)
    assert len(c4) == 0 and len(c6) == 0 and len(c8) > 0
    print("charpoly: x^8 (x^2-5)^6")
    print("LDL min pivots:", min(piv_p), min(piv_m))
    print("lift: C4=%d C6=%d C8=%d girth=8" % (len(c4), len(c6), len(c8)))
    with open("artifacts/spectral_lift_certificate.json", "w") as f:
        json.dump({"charpoly_const_first": cp,
                   "ldl_min_pivot_141I_minus_50A": str(min(piv_p)),
                   "ldl_min_pivot_141I_plus_50A": str(min(piv_m)),
                   "lift_cycle_counts": {"C4": 0, "C6": 0, "C8": len(c8)},
                   "eight_cycle": sorted(c8)[0]}, f, indent=1)


if __name__ == "__main__":
    main()
