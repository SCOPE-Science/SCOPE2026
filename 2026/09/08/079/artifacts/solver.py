# Solver used for the RS/paperfolding string-attractor inventory (lane-245).
# Pure stdlib. Deterministic (no randomness, fixed tie-breaking).
import sys, time

def rs_prefix(n):
    w = []
    for i in range(n):
        b = bin(i)[2:]
        c = 0
        for k in range(len(b) - 1):
            if b[k] == '1' and b[k + 1] == '1':
                c ^= 1
        w.append(c)
    return w

def pf_prefix(n):
    w = []
    for m in range(1, n + 1):
        u = m
        while u % 2 == 0:
            u //= 2
        w.append(0 if u % 4 == 1 else 1)
    return w

def build(w):
    """Group distinct factors by (64-bit rolling hash, length).
    Returns list of (unionmask, length, starts). NOTE: discovery-grade grouping;
    verify.py re-checks everything with exact string comparisons + suffix-array counts."""
    n = len(w)
    B = 9113823
    M = (1 << 64) - 1
    H = [0] * (n + 1)
    P = [1] * (n + 1)
    for i, c in enumerate(w):
        H[i + 1] = ((H[i] * B) + (c + 1)) & M
        P[i + 1] = (P[i] * B) & M
    def h(i, j):
        return (H[j] - ((H[i] * P[j - i]) & M)) & M
    table = {}
    for i in range(n):
        for j in range(i + 1, n + 1):
            key = (h(i, j), j - i)
            e = table.get(key)
            if e is None:
                table[key] = [j - i, [i]]
            else:
                e[1].append(i)
    out = []
    for key, (l, S) in table.items():
        m = 0
        for s in S:
            m |= ((1 << l) - 1) << s
        out.append((m, l, tuple(S)))
    return out

def greedy_ub(factors, n):
    masks = [f[0] for f in factors]
    gmask = 0
    chosen = []
    unc = [True] * len(masks)
    nunc = len(masks)
    pos_cover = [[] for _ in range(n)]
    for j, m in enumerate(masks):
        mm = m
        while mm:
            b = mm & -mm
            p = b.bit_length() - 1
            pos_cover[p].append(j)
            mm ^= b
    while nunc > 0:
        best = -1
        bestc = -1
        for p in range(n):
            if (gmask >> p) & 1:
                continue
            c = 0
            for j in pos_cover[p]:
                if unc[j]:
                    c += 1
            if c > bestc:
                bestc = c
                best = p
        chosen.append(best)
        gmask |= (1 << best)
        for j in pos_cover[best]:
            if unc[j]:
                unc[j] = False
                nunc -= 1
    return chosen, gmask

def disjoint_lb(factors):
    order = sorted(range(len(factors)), key=lambda j: factors[j][0].bit_count())
    used = 0
    fam = []
    for j in order:
        m = factors[j][0]
        if not (m & used):
            fam.append(j)
            used |= m
    return fam

def exact_min(factors, n, ub=None, time_limit=120):
    """Complete branch-and-bound minimum hitting-set search.
    Returns (opt_size, witness, nodes, timed_out). timed_out False => proven optimum."""
    masks = [f[0] for f in factors]
    D = len(masks)
    ALL = (1 << D) - 1
    t0 = time.time()
    cover = [0] * n
    for j, m in enumerate(masks):
        bit = 1 << j
        mm = m
        while mm:
            b = mm & -mm
            p = b.bit_length() - 1
            cover[p] |= bit
            mm ^= b
    if ub is None:
        g, _ = greedy_ub(factors, n)
        ub = list(g)
    best = list(ub)
    nodes = [0]
    poslist = []
    for m in masks:
        pl = []
        mm = m
        while mm:
            b = mm & -mm
            pl.append(b.bit_length() - 1)
            mm ^= b
        poslist.append(pl)
    covcount = [c.bit_count() for c in cover]
    for pl in poslist:
        pl.sort(key=lambda p: -covcount[p])
    sys.setrecursionlimit(100000)
    deadline = t0 + time_limit
    timed_out = [False]
    factor_order = sorted(range(D), key=lambda j: masks[j].bit_count())
    def lb(U):
        used = 0
        cnt = 0
        for j in factor_order:
            if (U >> j) & 1:
                m = masks[j]
                if not (m & used):
                    cnt += 1
                    used |= m
        return cnt
    def dfs(chosen, U):
        nodes[0] += 1
        if time.time() > deadline:
            timed_out[0] = True
            return True
        if U == 0:
            if len(chosen) < len(best):
                best[:] = list(chosen)
            return False
        if len(chosen) >= len(best):
            return False
        if len(chosen) + lb(U) >= len(best):
            return False
        chset = set(chosen)
        bj = -1
        bjns = None
        Utmp = U
        while Utmp:
            b = Utmp & -Utmp
            j = b.bit_length() - 1
            Utmp ^= b
            avail = [p for p in poslist[j] if p not in chset]
            if len(avail) == 0:
                return False
            if bjns is None or len(avail) < len(bjns):
                bjns = avail
                bj = j
                if len(avail) == 1:
                    break
        for p in bjns:
            if timed_out[0]:
                return True
            if len(chosen) + 1 >= len(best):
                break
            chosen.append(p)
            if dfs(chosen, U & ~cover[p]):
                return True
            chosen.pop()
        return False
    dfs([], ALL)
    return (len(best), best, nodes[0], timed_out[0])
