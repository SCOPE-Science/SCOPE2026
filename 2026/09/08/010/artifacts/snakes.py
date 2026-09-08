"""Step 2: peel-word snake generator + exact domination solver + tables to n=18."""
import itertools, sys, json, math, time

def snakes_fixed_ear(n):
    """All snakes with T1=(0,1,2). Yields frozenset of diagonals. Count = 2^(n-4)."""
    # state: covered cyclic interval [a..b] (mod n) going forward; exposed diag (a,b)
    out = []
    def rec(a, b, covered, tris):
        if covered == n:
            out.append(tris)
            return
        # prepend a-1
        v = (a - 1) % n
        rec(v, b, covered + 1, tris + [(v, a, b)])
        # append b+1
        w = (b + 1) % n
        # avoid double-counting final forced step: if covered==n-1 both choices coincide
        if covered == n - 1:
            return  # already added via prepend branch (same triangle (a,b,v=w))
        rec(a, w, covered + 1, tris + [(a, b, w)])
    rec(0, 2, 3, [(0, 1, 2)])
    return out

def diags_of(n, tris):
    d = set()
    for (x, y, z) in tris:
        for (a, b) in ((x, y), (y, z), (x, z)):
            i, j = (a, b) if ((b - a) % n) not in (1, n - 1) else (None, None)
            if i is not None:
                d.add((min(a, b), max(a, b)) if max(a, b) - min(a, b) not in (n - 1,) else None)
    # simpler: edge (a,b) is boundary iff cyclic diff in {1,n-1}
    d = set()
    for (x, y, z) in tris:
        for (a, b) in ((x, y), (y, z), (x, z)):
            if (b - a) % n not in (1, n - 1):
                d.add((min(a, b), max(a, b)))
    return frozenset(d)

def adj_masks(n, diags):
    masks = [(1 << i) for i in range(n)]
    for i in range(n):
        masks[i] |= (1 << ((i - 1) % n)) | (1 << ((i + 1) % n))
    for (a, b) in diags:
        masks[a] |= (1 << b)
        masks[b] |= (1 << a)
    return masks

def gamma_bruteforce(n, masks):
    full = (1 << n) - 1
    # increasing subset size
    for k in range(n + 1):
        for combo in itertools.combinations(range(n), k):
            cov = 0
            for v in combo:
                cov |= masks[v]
            if cov == full:
                return k
    return n

def gamma_branchbound(n, masks):
    full = (1 << n) - 1
    best = n + 1
    # greedy upper bound
    uncovered = full
    g = 0
    while uncovered:
        # pick vertex covering most of uncovered
        bi, bc = -1, -1
        for i in range(n):
            c = bin(masks[i] & uncovered).count("1")
            if c > bc:
                bc, bi = c, i
        uncovered &= ~masks[bi]
        g += 1
    best = g
    # order vertices; branch on first uncovered vertex u: must pick someone in N[u]
    from functools import lru_cache
    # use recursion with memo on (covered_mask, k_left)? sizes too big; simple DFS with pruning
    sys.setrecursionlimit(10000)
    def dfs(covered, chosen, start_order):
        nonlocal best
        if chosen >= best:
            return
        if covered == full:
            best = chosen
            return
        # lower bound: remaining/max new coverage
        rem = full & ~covered
        r = bin(rem).count("1")
        mx = 0
        for i in range(n):
            c = bin(masks[i] & rem).count("1")
            if c > mx:
                mx = c
        import math
        lb = (r + mx - 1) // mx
        if chosen + lb >= best:
            return
        # first uncovered vertex
        u = (rem & -rem).bit_length() - 1
        # candidates: N[u], try high-coverage first
        cands = []
        m = masks[u]
        v = 0
        mm = m
        while mm:
            if mm & 1:
                cands.append(v)
            v += 1
            mm >>= 1
        cands.sort(key=lambda i: -bin(masks[i] & rem).count("1"))
        for i in cands:
            dfs(covered | masks[i], chosen + 1, 0)
    dfs(0, 0, 0)
    return best

def canonical_key(n, diags):
    """Min over dihedral maps of sorted diagonal tuple."""
    dl = list(diags)
    best = None
    for s in range(n):
        for refl in (False, True):
            img = []
            for (a, b) in dl:
                if refl:
                    a, b = (-a) % n, (-b) % n
                a, b = (a + s) % n, (b + s) % n
                img.append((min(a, b), max(a, b)))
            t = tuple(sorted(img))
            if best is None or t < best:
                best = t
    return best

if __name__ == "__main__":
    # counts check
    for n in range(4, 13):
        tris = snakes_fixed_ear(n)
        assert len(tris) == 2 ** (n - 4), (n, len(tris))
        print(f"n={n} fixed-ear words={len(tris)} expect {2**(n-4)}", flush=True)
    # total labelled across starts: rotate word sets
    for n in range(5, 11):
        seen = set()
        for s in range(n):
            for t in snakes_fixed_ear(n):
                d = diags_of(n, t)
                # rotate labels by s
                r = frozenset((min((a+s) % n, (b+s) % n), max((a+s) % n, (b+s) % n)) for (a, b) in d)
                seen.add(r)
        print(f"n={n} total labelled snakes={len(seen)} expect {n*2**(n-5)}", flush=True)
