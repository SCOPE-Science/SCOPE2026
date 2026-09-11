"""Exact finite-field WLP pipeline for type-(2,3,3) CIs in k[x,y,z] (stdlib only).

Strategy: Macaulay matrices -> quotient monomial bases -> multiplication-by-L
matrix with entries linear in (a,b,c) -> exact 5x5 determinant (quintic) via
permutation expansion. D == 0 polynomial  <=>  every L fails middle degree
<=> fails WLP. D != 0  <=>  WLP holds in middle degree (plus rank checks).
"""
import itertools, random, json, sys

def mons3(d):
    out = []
    for i in range(d, -1, -1):
        for j in range(d - i, -1, -1):
            k = d - i - j
            out.append((i, j, k))
    return out

def rref_mod(rows, ncols, p):
    M = [list(r) for r in rows]
    pivots = []
    r = 0
    for c in range(ncols):
        piv = -1
        for i in range(r, len(M)):
            if M[i][c] % p != 0:
                piv = i
                break
        if piv < 0:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c] % p, -1, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p != 0:
                f = M[i][c] % p
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        pivots.append(c)
        r += 1
    return M, pivots

class Ring:
    """Quotient k[x,y,z]/(gens) over F_p with Macaulay reduction data."""
    def __init__(self, gens, p, dmax=6):
        self.gens = gens  # list of dict exp->coeff
        self.p = p
        self.deg = [sum(e) for e in [next(iter(g)) for g in gens]]
        self.M = {}       # d -> monomial list
        self.basis = {}   # d -> list of monomials (non-pivot)
        self.bidx = {}    # d -> {mon: idx}
        self.red = {}     # d -> {mon_index (pivot) : {basis_mon: coeff}}
        self.dims = {}
        for d in range(dmax + 1):
            mons = mons3(d)
            self.M[d] = mons
            idx = {m: i for i, m in enumerate(mons)}
            rows = []
            for g in gens:
                dg = None
                for e in g:
                    dg = sum(e)
                    break
                if d < dg:
                    continue
                for m in mons3(d - dg):
                    row = [0] * len(mons)
                    for e, c in g.items():
                        key = (m[0]+e[0], m[1]+e[1], m[2]+e[2])
                        row[idx[key]] = (row[idx[key]] + c) % p
                    rows.append(row)
            R, piv = rref_mod(rows, len(mons), p)
            pivset = set(piv)
            B = [mons[i] for i in range(len(mons)) if i not in pivset]
            self.basis[d] = B
            self.bidx[d] = {m: i for i, m in enumerate(B)}
            self.dims[d] = len(B)
            # reduction rules for pivot monomials
            rules = {}
            prow = {}
            for row in R:
                # find pivot col
                for c in range(len(mons)):
                    if row[c] == 1 and all(row[cc] == 0 for cc in pivset if cc != c):
                        # check it's a pivot row: leading 1 at c, zeros at other pivots
                        pass
                # simpler: pivot col = first nonzero among pivset
            # build map pivot->row
            for row in R:
                pc = -1
                for c in piv:
                    if row[c] % p != 0:
                        pc = c
                        break
                if pc >= 0:
                    rules[self.M[d][pc]] = {B[j]: (-row[self.M[d].index(B[j])]) % p
                                            for j in range(len(B)) if row[self.M[d].index(B[j])] % p != 0}
            self.red[d] = rules

    def reduce_mon(self, mon, d):
        """Reduce a degree-d monomial to dict basis_mon->coeff (mod p)."""
        if mon in self.bidx[d]:
            return {mon: 1}
        return dict(self.red[d].get(mon, {}))

    def hf(self, dmax=6):
        return [self.dims[d] for d in range(dmax + 1)]

def padd(a, b, p):
    o = dict(a)
    for k, v in b.items():
        o[k] = (o.get(k, 0) + v) % p
        if o[k] == 0:
            del o[k]
    return o

def pmul(a, b, p):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = (ka[0]+kb[0], ka[1]+kb[1], ka[2]+kb[2])
            o[k] = (o.get(k, 0) + va * vb) % p
            if o[k] == 0:
                del o[k]
    return o

def det5(M, p):
    """M: 5x5 list of poly dicts. Exact determinant."""
    det = {}
    for perm in itertools.permutations(range(5)):
        # sign
        inv = 0
        for i in range(5):
            for j in range(i+1, 5):
                if perm[i] > perm[j]:
                    inv += 1
        t = {(0, 0, 0): 1}
        for i in range(5):
            t = pmul(t, M[i][perm[i]], p)
            if not t:
                break
        if not t:
            continue
        if inv % 2 == 1:
            t = {k: (-v) % p for k, v in t.items()}
        det = padd(det, t, p)
    return det

def middle_matrix(ring, d_src=2):
    """5x5 (or nbs x nbt) matrix of xL, entries = linear polys in (a,b,c)."""
    p = ring.p
    Bs, Bt = ring.basis[d_src], ring.basis[d_src+1]
    LA = {(1,0,0): 1}
    LB = {(0,1,0): 1}
    LC = {(0,0,1): 1}
    LV = [(1,0,0), (0,1,0), (0,0,1)]
    LP = [LA, LB, LC]
    # M[row_t][col_s]
    M = [[{} for _ in Bs] for _ in Bt]
    for j, s in enumerate(Bs):
        for v, lp in zip(LV, LP):
            u = (s[0]+v[0], s[1]+v[1], s[2]+v[2])
            r = ring.reduce_mon(u, d_src+1)
            for m, c in r.items():
                i = ring.bidx[d_src+1][m]
                M[i][j] = padd(M[i][j], {k: (vv * c) % p for k, vv in lp.items()}, p)
    return M

def eval_poly(D, pt, p):
    s = 0
    for (i, j, k), c in D.items():
        s = (s + c * pow(pt[0], i, p) * pow(pt[1], j, p) * pow(pt[2], k, p)) % p
    return s

def numeric_mult_matrix(ring, L, d_src):
    p = ring.p
    Bs, Bt = ring.basis[d_src], ring.basis[d_src+1]
    import copy
    M = [[0]*len(Bs) for _ in Bt]
    for j, s in enumerate(Bs):
        for v, lv in zip([(1,0,0),(0,1,0),(0,0,1)], L):
            if lv % p == 0:
                continue
            u = (s[0]+v[0], s[1]+v[1], s[2]+v[2])
            r = ring.reduce_mon(u, d_src+1)
            for m, c in r.items():
                M[ring.bidx[d_src+1][m]][j] = (M[ring.bidx[d_src+1][m]][j] + lv*c) % p
    return M

def rank_mod(M, p):
    R, piv = rref_mod([row[:] for row in M], len(M[0]) if M else 0, p)
    return len(piv)

def full_wlp_check(ring, L):
    """Ranks of xL: A_d -> A_{d+1} for d=0..4 at concrete L."""
    return [rank_mod(numeric_mult_matrix(ring, L, d), ring.p) for d in range(5)]

def rand_poly(deg, p, rng):
    return {e: rng.randrange(p) for e in mons3(deg)}

def rand_ci(p, rng, tries=200):
    for _ in range(tries):
        gens = [rand_poly(2, p, rng), rand_poly(3, p, rng), rand_poly(3, p, rng)]
        if any(all(v == 0 for v in g.values()) for g in gens):
            continue
        R = Ring(gens, p)
        if R.hf() == [1, 3, 5, 5, 3, 1, 0]:
            return gens, R
    return None, None

def fmt_poly(g):
    ts = []
    for e in sorted(g, key=lambda e: (-sum(e), e)):
        ts.append(f"{g[e]}*x^{e[0]}y^{e[1]}z^{e[2]}")
    return "(" + " + ".join(ts) + ")"

def fmt_quint(D):
    if not D:
        return "0"
    return " + ".join(f"{c}*a^{i}b^{j}c^{k}" for (i, j, k), c in sorted(D.items()))
