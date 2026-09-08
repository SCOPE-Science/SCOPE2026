"""Lemma finite check: all NONEMPTY rank-3 triple families on [6] satisfying the
basis exchange axiom (loops/parallel elements allowed, rank stays exactly 3).

Enumerates all 2^20 subfamilies of C(6,3), filters by the exchange axiom,
excludes the empty family, and for each surviving matroid builds every
multiset-union class of ordered basis pairs with symmetric single-element
exchange adjacency, running BFS from every vertex.

Expected result: 2053 nonempty rank-3 families, all classes connected,
all diameters <= 3, 901 families attaining diameter 3.
(2054 only if counting the empty family, which satisfies exchange vacuously;
it is excluded as it is not a rank-3 matroid.)

Stdlib only.
"""
import itertools
from collections import deque

M = 6
TRIS = list(itertools.combinations(range(M), 3))
N = len(TRIS)  # 20
TIDX = {t: i for i, t in enumerate(TRIS)}
TS = [set(t) for t in TRIS]

# Precompute exchange targets: E[(i,x,ip)] = bitmask of j with j=(i-x)+y, y in ip-i
E = {}
DX = {}
for i in range(N):
    for ip in range(N):
        dx = [x for x in TRIS[i] if x not in TS[ip]]
        DX[(i, ip)] = dx
        for x in dx:
            m = 0
            for y in TS[ip] - TS[i]:
                m |= 1 << TIDX[tuple(sorted((TS[i] - {x}) | {y}))]
            E[(i, x, ip)] = m


def members(F):
    return [i for i in range(N) if (F >> i) & 1]


def exchange_ok(F):
    mem = members(F)
    for i in mem:
        for ip in mem:
            for x in DX[(i, ip)]:
                if not (F & E[(i, x, ip)]):
                    return False
    return True


def pair_diameter(F, mem):
    """Max BFS distance over ordered compatible-pair classes.
    Returns None if any class is disconnected."""
    B = set(mem)
    groups = {}
    for i in mem:
        for j in mem:
            key = tuple(sorted(TRIS[i] + TRIS[j]))
            groups.setdefault(key, []).append((i, j))
    dmax = 0
    for key, nodes in groups.items():
        for (s1, s2) in nodes:
            dist = {(s1, s2): 0}
            dq = deque([(s1, s2)])
            while dq:
                a, b = dq.popleft()
                A1, A2 = TS[a], TS[b]
                for x in A1:
                    for y in A2:
                        s_1 = (A1 - {x}) | {y}
                        s_2 = (A2 - {y}) | {x}
                        if len(s_1) != 3 or len(s_2) != 3:
                            continue
                        i1, i2 = TIDX[tuple(sorted(s_1))], TIDX[tuple(sorted(s_2))]
                        v = (i1, i2)
                        if v != (a, b) and i1 in B and i2 in B and v not in dist:
                            dist[v] = dist[(a, b)] + 1
                            dq.append(v)
            if len(dist) != len(nodes):
                return None
            dmax = max(dmax, max(dist.values()))
    return dmax


def run_lemma_check(verbose=True):
    nmat = 0
    dmax_all = 0
    nd3 = 0
    for F in range(1, 1 << N):  # exclude empty family (mask 0)
        if exchange_ok(F):
            nmat += 1
            d = pair_diameter(F, members(F))
            assert d is not None, f"DISCONNECTED rank-3 family mask {F}"
            assert d <= 3, f"DIAMETER >3 mask {F}"
            dmax_all = max(dmax_all, d)
            if d == 3:
                nd3 += 1
    if verbose:
        print(f"nonempty rank-3 triple families on [6]: {nmat}; "
              f"max pair-diameter = {dmax_all}; #attaining 3: {nd3}")
    return {"nmat": nmat, "dmax": dmax_all, "n_attain_3": nd3}


if __name__ == "__main__":
    import time
    t0 = time.time()
    r = run_lemma_check()
    print(f"time {time.time()-t0:.1f}s")
    assert r["nmat"] == 2053, r
    assert r["dmax"] == 3, r
    assert r["n_attain_3"] == 901, r
    print("LEMMA CHECK PASSED")
