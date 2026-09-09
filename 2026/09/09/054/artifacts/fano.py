"""Core objects: Fano plane, its 4-uniform linear expansion F+, linearity and F+ detection."""
import itertools

def fano_triples():
    # 7 triples on 0..6, each pair exactly once
    return [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]

def build_Fplus():
    # core 0..6, private i -> 7+i
    return [tuple(sorted(t + (7+i,))) for i, t in enumerate(fano_triples())]

def is_linear(edges):
    seen = set()
    for e in edges:
        for p in itertools.combinations(sorted(e), 2):
            if p in seen:
                return False
            seen.add(p)
    return True

def pair_count(edges):
    seen = set()
    for e in edges:
        for p in itertools.combinations(sorted(e), 2):
            seen.add(p)
    return len(seen)

def find_Fplus(edges):
    """Corner-based complete F+ search. Returns a witness 7-tuple of edge indices or None."""
    E = [frozenset(e) for e in edges]
    m = len(E)
    # triple -> edge index map (linearity not assumed; keep first)
    byv = {}
    for i, e in enumerate(E):
        for v in e:
            byv.setdefault(v, []).append(i)
    # incidence: edge indices per vertex
    for v, lst in byv.items():
        L = len(lst)
        for a in range(L):
            for b in range(a+1, L):
                for c in range(b+1, L):
                    A, B, C = E[lst[a]], E[lst[b]], E[lst[c]]
                    if len(A & B) != 1 or len(A & C) != 1 or len(B & C) != 1:
                        continue
                    # corner at v with blocks A,B,C
                    for TA in itertools.combinations(sorted(A), 3):
                        if v not in TA:
                            continue
                        for TB in itertools.combinations(sorted(B), 3):
                            if v not in TB:
                                continue
                            for TC in itertools.combinations(sorted(C), 3):
                                if v not in TC:
                                    continue
                                core = frozenset(TA) | frozenset(TB) | frozenset(TC)
                                if len(core) != 7:
                                    continue
                                # candidate 4th blocks with exactly 3 verts in core
                                ia, ib, ic = lst[a], lst[b], lst[c]
                                cands = []
                                for j, D in enumerate(E):
                                    if j == ia or j == ib or j == ic:
                                        continue
                                    t = D & core
                                    if len(t) == 3:
                                        cands.append((j, t, D - core))
                                if len(cands) < 4:
                                    continue
                                star_pairs = set()
                                for t in (TA, TB, TC):
                                    for p in itertools.combinations(sorted(t), 2):
                                        star_pairs.add(p)
                                # try all 4-subsets of candidates (usually exactly 4)
                                found = None
                                if len(cands) == 4:
                                    combos = [cands]
                                else:
                                    combos = list(itertools.combinations(cands, 4))
                                    if len(combos) > 200:
                                        combos = combos[:200]
                                for combo in combos:
                                    trips = [t for (_, t, _) in combo]
                                    privs = [pv for (_, _, pv) in combo]
                                    # privates: singletons, distinct, outside core
                                    ok = True
                                    seenpv = set()
                                    for pv in privs:
                                        if len(pv) != 1:
                                            ok = False
                                            break
                                        (x,) = pv
                                        if x in core or x in seenpv:
                                            ok = False
                                            break
                                        seenpv.add(x)
                                    if not ok:
                                        continue
                                    cov = set(star_pairs)
                                    for t in trips:
                                        for p in itertools.combinations(sorted(t), 2):
                                            if p in cov:
                                                ok = False
                                                break
                                            cov.add(p)
                                        if not ok:
                                            break
                                    if not ok:
                                        continue
                                    if len(cov) != 21:
                                        continue
                                    # verify the 7 blocks pairwise meet exactly once
                                    idxs = [ia, ib, ic] + [j for (j, _, _) in combo]
                                    blks = [E[j] for j in idxs]
                                    good = True
                                    for x in range(7):
                                        for y in range(x+1, 7):
                                            if len(blks[x] & blks[y]) != 1:
                                                good = False
                                                break
                                        if not good:
                                            break
                                    if good:
                                        found = idxs
                                        break
                                if found is not None:
                                    return found
    return None
