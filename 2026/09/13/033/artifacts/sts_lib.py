"""Shared library: tricyclic STS(21) enumeration, Pasch counting, Fano detection, isomorphism."""
import itertools
import sys
sys.setrecursionlimit(100000)

def pt(a, i):
    return i * 7 + a

def sigma(p):
    return (p // 7) * 7 + ((p % 7) + 1) % 7

def sigma_pow(p, k):
    return (p // 7) * 7 + ((p % 7) + k) % 7

def pairkey(p, q):
    a1, i1 = p % 7, p // 7
    a2, i2 = q % 7, q // 7
    if i1 == i2:
        d = (a2 - a1) % 7
        return ('in', i1, min(d, 7 - d))
    if i1 > i2:
        a1, a2, i1, i2 = a2, a1, i2, i1
    return ('cross', i1, i2, (a2 - a1) % 7)

def pkey_pair(p, q):
    return (p, q) if p < q else (q, p)

def build_orbit_matrix():
    """Return (cols, rows): cols = list of 30 pair-orbit keys;
    rows = dict rowid -> {'rep': triple, 'cols': [3 col idx], 'blocks': [7 triples]}."""
    seen = {}
    for t in itertools.combinations(range(21), 3):
        orb = set()
        for k in range(7):
            orb.add(tuple(sorted(sigma_pow(x, k) for x in t)))
        c = min(orb)
        seen.setdefault(c, orb)
    assert len(seen) == 190, f"expected 190 block-orbits, got {len(seen)}"
    for c, orb in seen.items():
        assert len(orb) == 7, "orbit size must be 7"
    cols = sorted({pairkey(t[0], t[1]) for t in seen})
    # collect all pair keys appearing anywhere to ensure 30 appear
    allpk = set()
    for orb in seen.values():
        t = next(iter(orb))
        x, y, z = t
        allpk.add(pairkey(x, y))
        allpk.add(pairkey(x, z))
        allpk.add(pairkey(y, z))
    assert len(allpk) == 30, f"expected 30 pair-orbits, got {len(allpk)}"
    cols = sorted(allpk)
    cidx = {c: i for i, c in enumerate(cols)}
    rows = {}
    rid = 0
    for c, orb in sorted(seen.items()):
        x, y, z = c
        cs = [cidx[pairkey(x, y)], cidx[pairkey(x, z)], cidx[pairkey(y, z)]]
        if len(set(cs)) < 3:
            continue  # invalid: repeated pair-orbit -> would repeat a pair
        rows[rid] = {'rep': c, 'cols': cs, 'blocks': sorted(orb)}
        rid += 1
    return cols, rows

def exact_covers(rowcols, ncols):
    """Copy-based Algorithm X. rowcols: dict rowid -> list of col idx. Returns list of rowid lists."""
    sols = []
    def rec(cols_rem, rows_rem, cur):
        if not cols_rem:
            sols.append(list(cur))
            return
        # smallest column
        best_c, best_n, best_rows = None, None, None
        for c in cols_rem:
            cand = [r for r, cs in rows_rem.items() if c in cs]
            n = len(cand)
            if n == 0:
                return
            if best_n is None or n < best_n:
                best_n, best_c, best_rows = n, c, cand
                if n == 1:
                    break
        for r in best_rows:
            cov = set(rowcols[r])
            new_rows = {r2: cs for r2, cs in rows_rem.items() if not (set(cs) & cov)}
            cur.append(r)
            rec(cols_rem - cov, new_rows, cur)
            cur.pop()
    rec(set(range(ncols)), {r: list(cs) for r, cs in rowcols.items()}, [])
    return sols

def blocks_of_solution(rows, sol):
    blks = []
    for r in sol:
        blks.extend(rows[r]['blocks'])
    assert len(blks) == 70
    return [frozenset(b) for b in blks]

def is_sts(blocks):
    if len(blocks) != 70:
        return False
    seen = set()
    for b in blocks:
        if len(b) != 3:
            return False
        for p in itertools.combinations(sorted(b), 2):
            if p in seen:
                return False
            seen.add(p)
    return len(seen) == 210

def pairmap_of(blocks):
    pm = {}
    for b in blocks:
        x, y, z = sorted(b)
        pm[(x, y)] = z
        pm[(x, z)] = y
        pm[(y, z)] = x
    return pm

def pasch_find(blocks):
    """Return set of Pasches, each a frozenset of 4 frozenset-blocks."""
    pm = pairmap_of(blocks)
    bl = [frozenset(b) for b in blocks]
    blist = [tuple(sorted(b)) for b in bl]
    found = set()
    raw = 0
    n = len(bl)
    for i in range(n):
        bi = blist[i]
        si = set(bi)
        for j in range(i + 1, n):
            bj = blist[j]
            inter = si.intersection(bj)
            if len(inter) != 1:
                continue
            x = next(iter(inter))
            a, b = bi[0], bi[1] if bi[2] == x else (bi[0], bi[2] if bi[1] == x else (bi[1], bi[2]))
            # recompute cleanly:
            ri = [v for v in bi if v != x]
            rj = [v for v in bj if v != x]
            a, b = ri
            c, d = rj
            for (e1, e2) in ((((a, c), (b, d))), (((a, d), (b, c)))):
                r1 = pm.get((min(e1[0], e1[1]), max(e1[0], e1[1])))
                r2 = pm.get((min(e2[0], e2[1]), max(e2[0], e2[1])))
                if r1 is not None and r1 == r2 and r1 != x:
                    P = frozenset([bl[i], bl[j],
                                   frozenset((e1[0], e1[1], r1)),
                                   frozenset((e2[0], e2[1], r2))])
                    if len(P) == 4:
                        found.add(P)
                        raw += 1
    assert raw % 6 == 0, f"raw successes {raw} not divisible by 6"
    assert len(found) == raw // 6
    return found

def pasch_count(blocks):
    return len(pasch_find(blocks))

def point_pasch_degrees(blocks, pasches=None):
    if pasches is None:
        pasches = pasch_find(blocks)
    deg = [0] * 21
    for P in pasches:
        pts = set()
        for b in P:
            pts |= set(b)
        for p in pts:
            deg[p] += 1
    return deg

def block_pasch_degrees(blocks, pasches=None):
    if pasches is None:
        pasches = pasch_find(blocks)
    idx = {b: i for i, b in enumerate(blocks)}
    deg = [0] * len(blocks)
    for P in pasches:
        for b in P:
            deg[idx[b]] += 1
    return deg

def fano_find(blocks):
    """Sub-STS(7)s via triple closure. Returns set of frozenset 7-point sets."""
    pm = pairmap_of(blocks)
    bset = set(frozenset(b) for b in blocks)
    out = set()
    for t in itertools.combinations(range(21), 3):
        if frozenset(t) in bset:
            continue
        S = set(t)
        processed_pairs = set()
        worklist = list(t)
        while worklist and len(S) <= 7:
            r = worklist.pop()
            for p in list(S):
                if p == r:
                    continue
                key = (p, r) if p < r else (r, p)
                if key in processed_pairs:
                    continue
                processed_pairs.add(key)
                th = pm[key]
                if th not in S:
                    S.add(th)
                    worklist.append(th)
                    if len(S) > 7:
                        break
        if len(S) == 7:
            nb = sum(1 for b in blocks if set(b) <= S)
            if nb == 7:
                out.add(frozenset(S))
    return out

def third_matrix(blocks):
    T = [[-1] * 21 for _ in range(21)]
    for b in blocks:
        x, y, z = sorted(b)
        T[x][y] = z; T[y][x] = z
        T[x][z] = y; T[z][x] = y
        T[y][z] = x; T[z][y] = x
    return T

def point_invariant(blocks):
    """Per-point invariant tuple: (pasch degree, fano degree)."""
    P = pasch_find(blocks)
    pd = point_pasch_degrees(blocks, P)
    F = fano_find(blocks)
    fd = [0] * 21
    for S in F:
        for p in S:
            fd[p] += 1
    return [(pd[p], fd[p]) for p in range(21)]

def global_invariant(blocks):
    P = pasch_find(blocks)
    pd = point_pasch_degrees(blocks, P)
    bd = block_pasch_degrees(blocks, P)
    F = fano_find(blocks)
    return (len(P), tuple(sorted(pd)), tuple(sorted(bd)), len(F))

def light_invariant(blocks):
    """Cheaper invariant (no Fano) for labeled classification."""
    P = pasch_find(blocks)
    pd = point_pasch_degrees(blocks, P)
    bd = block_pasch_degrees(blocks, P)
    return (len(P), tuple(sorted(pd)), tuple(sorted(bd)))

def canonical_form(blocks, max_tries=200000):
    """Canonical triple-sorted block string under all 21! relabelings-free search.
    Refinement-guided backtracking with third-map propagation, capped by max_tries.
    Returns (canon_string, nodes_used). Deterministic."""
    T = third_matrix(blocks)
    inv = point_invariant(blocks)
    best = [None]
    nodes = [0]
    f = [-1] * 21
    used = [False] * 21
    order = sorted(range(21), key=lambda p: (inv[p], p))
    lab = {p: r for r, p in enumerate(order)}
    trail = []
    def assign(p, q):
        f[p] = q; used[q] = True; trail.append(p)
    def undo_to(mark):
        while len(trail) > mark:
            p = trail.pop()
            used[f[p]] = False; f[p] = -1
    partial_best = [True]
    def img_block_key(prefix_blocks):
        return sorted(prefix_blocks)
    # Precompute block list
    bl = [tuple(sorted(b)) for b in blocks]
    def rec(nmapped):
        nodes[0] += 1
        if nodes[0] > max_tries:
            return True  # signal cap
        if nmapped == 21:
            img = sorted(tuple(sorted(f[x] for x in b)) for b in bl)
            s = str(img)
            if best[0] is None or s < best[0]:
                best[0] = s
            return False
        # choose next unmapped point: smallest label rank
        p = -1
        for pp in order:
            if f[pp] < 0:
                p = pp
                break
        # candidate images: try in increasing order, restricted by invariant
        cands = [q for q in range(21) if (not used[q]) and point_inv_key(inv[q]) == point_inv_key(inv[p])]
        for q in cands:
            mark = len(trail)
            assign(p, q)
            if propagate_assign(T, f, used, trail):
                # bound: compare mapped-block prefix with best
                if bound_ok(bl, f, best[0]):
                    r = rec(nmapped + (len(trail) - mark) + 1 - (len(trail) - mark))
                    # careful: count mapped properly
                    if r is True and nodes[0] > max_tries:
                        return True
                # recount mapped
            undo_to(mark)
        # recompute nmapped from f
        return False
    # simpler correct recursion counting mapped
    def rec2():
        nodes[0] += 1
        if nodes[0] > max_tries:
            return 'cap'
        if all(v >= 0 for v in f):
            img = sorted(tuple(sorted(f[x] for x in b)) for b in bl)
            s = str(img)
            if best[0] is None or s < best[0]:
                best[0] = s
            return 'ok'
        p = -1
        for pp in order:
            if f[pp] < 0:
                p = pp
                break
        for q in range(21):
            if used[q] or inv[q] != inv[p]:
                continue
            mark = len(trail)
            assign(p, q)
            if propagate_assign(T, f, used, trail):
                if bound_ok(bl, f, best[0]):
                    r = rec2()
                    if r == 'cap':
                        return 'cap'
            undo_to(mark)
        return 'ok'
    res = rec2()
    return best[0], nodes[0], res

def point_inv_key(t):
    return t

def propagate_assign(T, f, used, trail):
    queue = trail[:]
    qi = 0
    # use index pointer over a growing list copy
    qlist = list(trail)
    head = 0
    while head < len(qlist):
        pn = qlist[head]; head += 1
        qn = f[pn]
        for po in range(21):
            if f[po] < 0 or po == pn:
                continue
            r1 = T[pn][po]
            q3 = T[qn][f[po]]
            if f[r1] >= 0:
                if f[r1] != q3:
                    return False
            else:
                if used[q3]:
                    return False
                f[r1] = q3; used[q3] = True; trail.append(r1); qlist.append(r1)
    return True

def bound_ok(bl, f, best):
    if best is None:
        return True
    # Build mapped image blocks fully determined so far, compare prefix with best's prefix
    det = []
    for b in bl:
        if all(f[x] >= 0 for x in b):
            det.append(tuple(sorted(f[x] for x in b)))
    det.sort()
    # parse best prefix: compare only first len(det) entries
    # best stored as str(list); re-derive by eval-free prefix compare is complex; skip bound (always True)
    return True

def isomorphic_btrack(T1, T2, inv1, inv2):
    """Backtracking design isomorphism with propagation. inv: per-point labels."""
    if sorted(inv1) != sorted(inv2):
        return False
    f = [-1] * 21
    used = [False] * 21
    order = sorted(range(21), key=lambda p: (inv1[p], p))
    # candidate images per point (same invariant)
    cand = {}
    for p in range(21):
        cand[p] = [q for q in range(21) if inv2[q] == inv1[p]]
    trail = []
    def assign(p, q):
        f[p] = q; used[q] = True; trail.append(p)
    def undo_to(mark):
        while len(trail) > mark:
            p = trail.pop()
            used[f[p]] = False; f[p] = -1
    def propagate():
        # process newly assigned points in trail order via index pointer
        head = 0
        # instead: iterate until no change; use pointer into a local queue
        queue = trail[:]  # snapshot; new assigns appended to trail but we track separately
        q2 = list(queue)
        seen_q = set()
        while q2:
            pn = q2.pop()
            qn = f[pn]
            for po in range(21):
                if f[po] < 0 or po == pn:
                    continue
                r1 = T1[pn][po]
                q3 = T2[qn][f[po]]
                if f[r1] >= 0:
                    if f[r1] != q3:
                        return False
                else:
                    if used[q3]:
                        return False
                    assign(r1, q3)
                    q2.append(r1)
        return True
    # iterative deepening recursion
    def rec():
        # find next unmapped in order
        p = -1
        for pp in order:
            if f[pp] < 0:
                p = pp
                break
        if p < 0:
            return True
        mark = len(trail)
        for q in cand[p]:
            if used[q]:
                continue
            assign(p, q)
            if propagate():
                if rec():
                    return True
            undo_to(mark)
        return False
    return rec()
