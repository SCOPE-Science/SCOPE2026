"""Independent character routine: ADDING rim hooks (Pieri-type MN), no beta-sets.
chi(lam, mu) via expanding p_mu in Schur basis: start {():1}, multiply by p_m
by adding all rim hooks of size m. Skew kappa\nu is a rim hook iff connected
and 2x2-free. Height = rows spanned - 1.
"""
from functools import lru_cache

def skew_cells(nu, kap):
    cells = set()
    for i, r in enumerate(kap):
        for j in range(r):
            if j >= (nu[i] if i < len(nu) else 0):
                cells.add((i, j))
    return cells

def is_rim_hook(nu, kap, m):
    if sum(kap) - sum(nu) != m:
        return None
    cells = skew_cells(nu, kap)
    if len(cells) != m or not cells:
        return None
    # 2x2-free
    for (i, j) in cells:
        if (i+1, j) in cells and (i, j+1) in cells and (i+1, j+1) in cells:
            return None
    # connected (edge adjacency)
    stack = [next(iter(cells))]
    seen = {stack[0]}
    while stack:
        i, j = stack.pop()
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            c = (i+d[0], j+d[1])
            if c in cells and c not in seen:
                seen.add(c); stack.append(c)
    if len(seen) != m:
        return None
    rows = {i for (i, j) in cells}
    return len(rows) - 1

def add_children(nu, m):
    """All (kappa, ht) with kappa/nu a rim hook of size m. nu tuple."""
    from kron import partitions
    n0 = sum(nu)
    out = []
    for kap in partitions(n0 + m):
        if len(kap) < len(nu):
            continue
        if any(kap[i] < nu[i] for i in range(len(nu))):
            continue
        ht = is_rim_hook(nu, kap, m)
        if ht is not None:
            out.append((kap, ht))
    return out

from functools import lru_cache
@lru_cache(maxsize=None)
def _add_children(nu, m):
    return add_children(nu, m)

def chi_add(lam, mu):
    cur = {(): 1}
    for m in mu:
        nxt = {}
        for nu, c in cur.items():
            for kap, ht in _add_children(nu, m):
                nxt[kap] = nxt.get(kap, 0) + (c if not (ht & 1) else -c)
        cur = nxt
    return cur.get(tuple(lam), 0)

def kronecker_add(lam, mu_, nu, n):
    import sys
    sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-399/output/artifacts")
    from kron import partitions, z_of, fact
    fn = fact(n); S = 0
    for cl in partitions(n):
        a = chi_add(tuple(lam), cl)
        if not a: continue
        b = chi_add(tuple(mu_), cl)
        if not b: continue
        c = chi_add(tuple(nu), cl)
        if not c: continue
        S += (fn // z_of(cl)) * a * b * c
    assert S % fn == 0
    return S // fn
