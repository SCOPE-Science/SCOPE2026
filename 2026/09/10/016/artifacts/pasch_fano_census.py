"""Unit-tested exact Pasch + Fano census (stdlib only).
Pasch = 4 triples pairwise intersecting in exactly 1 vertex on 6 vertices (K4 lines):
  anchor = vertex a + unordered pair of blocks {B1,B2} through a.
  B1\\{a}={b,c}, B2\\{a}={d,e}: Pasch iff [(b,d)&(c,e) share third vertex f] or
  [(b,e)&(c,d) share third vertex f]. Each Pasch found exactly 6 times (once per vertex).
Fano census: vertex-anchored (3 blocks through v pairwise disjoint outside v + 4
  transversals pairwise agreeing in exactly 1 slot); each copy found exactly 7 times.
Unit tests: single Pasch -> Pasch 1, Fano 0; Fano plane -> Fano 1, Pasch>=1; empty -> 0.
"""
import itertools

def build_index(blocks):
    pair = {}
    ve = {}
    for i, (x, y, z) in enumerate(blocks):
        for p in ((x, y), (x, z), (y, z)):
            a, b = (p[1], p[0]) if p[0] > p[1] else p
            pair[(a, b)] = i
        for v in (x, y, z):
            ve.setdefault(v, []).append(i)
    return pair, ve

def ethru(pair, a, b):
    if a > b:
        a, b = b, a
    return pair.get((a, b), -1)

def count_pasch(blocks):
    pair, ve = build_index(blocks)
    raw = 0
    for a, L in ve.items():
        for ii in range(len(L)):
            B1 = blocks[L[ii]]
            bc = [u for u in B1 if u != a]
            b, c = bc
            for jj in range(ii + 1, len(L)):
                B2 = blocks[L[jj]]
                de = [u for u in B2 if u != a]
                d, e = de
                # pattern 1: (b,d) & (c,e) share third vertex
                k1 = ethru(pair, b, d)
                k2 = ethru(pair, c, e)
                if k1 >= 0 and k2 >= 0 and k1 != L[ii] and k1 != L[jj] and k2 != L[ii] and k2 != L[jj]:
                    f1 = [u for u in blocks[k1] if u != b and u != d]
                    f2 = [u for u in blocks[k2] if u != c and u != e]
                    if len(f1) == 1 and len(f2) == 1 and f1[0] == f2[0]:
                        f = f1[0]
                        if len({a, b, c, d, e, f}) == 6:
                            raw += 1
                # pattern 2: (b,e) & (c,d) share third vertex
                k1 = ethru(pair, b, e)
                k2 = ethru(pair, c, d)
                if k1 >= 0 and k2 >= 0 and k1 != L[ii] and k1 != L[jj] and k2 != L[ii] and k2 != L[jj]:
                    f1 = [u for u in blocks[k1] if u != b and u != e]
                    f2 = [u for u in blocks[k2] if u != c and u != d]
                    if len(f1) == 1 and len(f2) == 1 and f1[0] == f2[0]:
                        f = f1[0]
                        if len({a, b, c, d, e, f}) == 6:
                            raw += 1
    assert raw % 6 == 0, f"pasch raw {raw} not divisible by 6"
    return raw // 6

def count_fano(blocks):
    eset = set(blocks)
    pair, ve = build_index(blocks)
    raw = 0
    verts = list(ve.keys())
    for v in verts:
        L = ve[v]
        P = [[u for u in blocks[i] if u != v] for i in L]
        for ii in range(len(L)):
            for jj in range(ii + 1, len(L)):
                if P[ii][0] in P[jj] or P[ii][1] in P[jj]:
                    continue
                S2 = set(P[jj])
                for kk in range(jj + 1, len(L)):
                    if P[kk][0] in S2 or P[kk][1] in S2:
                        continue
                    if P[kk][0] in P[ii] or P[kk][1] in P[ii]:
                        continue
                    pres = []
                    for x in P[ii]:
                        for y in P[jj]:
                            for z in P[kk]:
                                if tuple(sorted((x, y, z))) in eset:
                                    pres.append((x, y, z))
                    for q in itertools.combinations(range(len(pres)), 4):
                        ok = True
                        for p1 in range(4):
                            for p2 in range(p1 + 1, 4):
                                ag = sum(1 for t in range(3) if pres[q[p1]][t] == pres[q[p2]][t])
                                if ag != 1:
                                    ok = False
                                    break
                            if not ok:
                                break
                        if ok:
                            raw += 1
    assert raw % 7 == 0, f"fano raw {raw} not divisible by 7"
    return raw // 7

# ---- unit tests ----
P = [(0,1,2),(0,3,4),(1,3,5),(2,4,5)]
assert count_pasch(P) == 1, count_pasch(P)
assert count_fano(P) == 0
FANO = [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
assert count_fano(FANO) == 1, count_fano(FANO)
assert count_pasch(FANO) >= 1, count_pasch(FANO)
print("fano pasch-count =", count_pasch(FANO))
assert count_pasch([(0,1,2),(3,4,5)]) == 0
assert count_fano([(0,1,2),(3,4,5)]) == 0
# greedy-builder incremental rule check: feed a Pasch triple-by-triple; 4th must complete one
print("UNIT_TESTS_OK")
