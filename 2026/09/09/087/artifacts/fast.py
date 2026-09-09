"""Fast proper-ordered-partition enumeration for C_{n,k} e-coefficients."""
import sys, itertools
sys.path.insert(0, 'output/artifacts')
from sym import partitions, e_basis_monomial_matrix, invert_matrix
from ellzey import build
from fractions import Fraction
from collections import Counter, defaultdict
from math import factorial

def e_coeffs_fast(n, k, verbose=True):
    arcs, adj = build(n, k)
    arcs_set = set(arcs)
    # independent subsets (bitmasks)
    indep = []
    for mask in range(1, 1 << n):
        vs = [v for v in range(n) if mask >> v & 1]
        ok = all(not adj[vs[a]][vs[b]] for a in range(len(vs)) for b in range(a+1, len(vs)))
        if ok: indep.append(mask)
    by_min = defaultdict(list)
    for m in indep:
        v = (m & (-m)).bit_length() - 1
        by_min[v].append(m)
    W = defaultdict(Counter)  # type -> Counter(power->count), counts ORDERED partitions
    import itertools as _it
    full = (1 << n) - 1
    stack = [(0, [])]  # (used mask, canonical blocks list in min-first order)
    count = 0
    while stack:
        used, blocks = stack.pop()
        if used == full:
            # blocks are canonical (min-ordered); sum over all l! color orders
            for perm in _it.permutations(blocks):
                count += 1
                rank = [0]*n
                for r, B in enumerate(perm):
                    m = B
                    while m:
                        lsb = m & (-m); v = lsb.bit_length() - 1
                        rank[v] = r; m ^= lsb
                asc = sum(1 for (u, v) in arcs if rank[u] < rank[v])
                mu = tuple(sorted(([bin(B).count('1') for B in blocks]), reverse=True))
                W[mu][asc] += 1
            continue
        v = next(v for v in range(n) if not (used >> v & 1))
        for B in by_min[v]:
            if B & used == 0:
                stack.append((used | B, blocks + [B]))
    parts = list(partitions(n))
    amat = {}
    for mu in parts:
        tmu = tuple(mu)
        c = Counter(mu); l = len(mu)
        norders = factorial(l)
        for v in c.values(): norders //= factorial(v)
        amat[tmu] = defaultdict(Fraction)
        for pwr, cnt in W.get(tmu, {}).items():
            amat[tmu][pwr] = Fraction(cnt, norders)
    for mu in parts:
        for pwr, v in amat[tuple(mu)].items():
            assert v.denominator == 1, (mu, pwr, v)
    maxdeg = max((max(d.keys()) if d else 0) for d in W.values())
    _, E = e_basis_monomial_matrix(n, q=n)
    Einv = invert_matrix(E)
    cpolys = {tuple(lam): defaultdict(Fraction) for lam in parts}
    for pwr in range(maxdeg + 1):
        avec = [amat[tuple(mu)].get(pwr, Fraction(0)) for mu in parts]
        cvec = [sum(Einv[i][j] * avec[j] for j in range(len(parts))) for i in range(len(parts))]
        for i, lam in enumerate(parts):
            if cvec[i] != 0: cpolys[tuple(lam)][pwr] = cvec[i]
    return cpolys, W, count

if __name__ == '__main__':
    n, k = int(sys.argv[1]), int(sys.argv[2])
    cpolys, W, count = e_coeffs_fast(n, k)
    print(f"n={n} k={k} proper-ordered={count}")
    for lam in sorted(cpolys):
        d = dict(sorted(cpolys[lam].items()))
        print(tuple(lam), {p: int(v) for p, v in d.items()} if d else 0)
