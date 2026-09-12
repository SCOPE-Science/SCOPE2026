"""Independent verifier: different spanning tree (DFS from vertex 7, reversed
adjacency order), subset-method cycle inventory, LeVerrier recomputation,
Bareiss leading-minor Ramanujan check, BFS girth. Prints VERIFY_OK."""
import itertools
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
ADJ = {v: sorted((w for w in range(N)
                  if tuple(sorted((v, w))) in EDGE_INDEX), reverse=True)
       for v in range(N)}


def alt_tree():
    tree = set()
    seen = {7}
    stack = [7]
    while stack:
        u = stack.pop()
        for w in ADJ[u]:
            if w not in seen:
                seen.add(w)
                tree.add(EDGE_INDEX[tuple(sorted((u, w)))])
                stack.append(w)
    assert len(tree) == N - 1
    return tree


def six_sets():
    out = []
    for combo in itertools.combinations(range(N), 6):
        S = set(combo)
        if any(sum(1 for w in ADJ[v] if w in S) != 2 for v in S):
            continue
        seen = {combo[0]}
        stack = [combo[0]]
        while stack:
            u = stack.pop()
            for w in ADJ[u]:
                if w in S and w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(seen) == 6:
            out.append(combo)
    return out


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
    return [int(x) for x in c]


def bareiss_det(M):
    n = len(M)
    B = [row[:] for row in M]
    prev = 1
    for k in range(n - 1):
        assert B[k][k] != 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                B[i][j] = (B[i][j] * B[k][k] - B[i][k] * B[k][j]) // prev
            B[i][k] = 0
        prev = B[k][k]
    return B[n - 1][n - 1]


def girth(adjmap, nverts):
    best = 10 ** 9
    for s in range(nverts):
        dist = {s: 0}
        par = {s: -1}
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for w in adjmap[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    par[w] = u
                    queue.append(w)
                elif par[u] != w and dist[w] <= dist[u]:
                    best = min(best, dist[u] + dist[w] + 1)
    return best


def main():
    tree = alt_tree()
    cotree = sorted(i for i in range(len(EDGES)) if i not in tree)
    sets = six_sets()
    assert len(sets) == 20, len(sets)
    sols = []
    for mm in range(2048):
        ok = True
        for S in sets:
            Ss = set(S)
            cyc, prev, cur = [S[0]], None, S[0]
            for _ in range(6):
                if len(cyc) == 6:
                    break
                nxt = [w for w in ADJ[cur] if w in Ss and w != prev][0]
                prev, cur = cur, nxt
                cyc.append(cur)
            el = [EDGE_INDEX[tuple(sorted((cyc[j], cyc[(j + 1) % 6])))]
                  for j in range(6)]
            par = sum(1 for e in el
                      if e not in tree and (mm >> cotree.index(e)) & 1) % 2
            if par == 0:
                ok = False
                break
        if ok:
            sols.append(mm)
    assert len(sols) == 1, sols

    def sign_of(ei):
        if ei in tree:
            return 1
        return -1 if (sols[0] >> cotree.index(ei)) & 1 else 1

    A = [[0] * N for _ in range(N)]
    for (u, v), ei in EDGE_INDEX.items():
        A[u][v] = A[v][u] = sign_of(ei)
    cp = charpoly_leverrier(A)
    assert cp == json.load(
        open("artifacts/spectral_lift_certificate.json")
    )["charpoly_const_first"]
    Np = [[(141 if i == j else 0) - 50 * A[i][j] for j in range(N)]
          for i in range(N)]
    Nm = [[(141 if i == j else 0) + 50 * A[i][j] for j in range(N)]
          for i in range(N)]
    minors = ([bareiss_det([row[:k] for row in Np[:k]]) for k in range(1, 21)]
              + [bareiss_det([row[:k] for row in Nm[:k]])
                 for k in range(1, 21)])
    assert all(v > 0 for v in minors)
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
    assert girth(ladj, 40) == 8
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
