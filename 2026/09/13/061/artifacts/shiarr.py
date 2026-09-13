"""Exact restriction + characteristic polynomial for cone extended Shi B."""
from fractions import Fraction
import itertools
from functools import lru_cache

# ---------- integer vector utils ----------
def to_frac_vec(v):
    return tuple(Fraction(x) for x in v)

def primitive_canon(v):
    # v: tuple of Fraction, nonzero -> primitive integer tuple, sign-normalized
    from math import gcd
    # clear denominators
    dens = [x.denominator for x in v]
    L = 1
    for d in dens:
        L = L*d//gcd(L,d)
    w = [int(x*L) for x in v]
    g = 0
    for a in w:
        g = gcd(g, a)
    w = [a//g for a in w]
    # sign normalize: first nonzero positive
    for a in w:
        if a != 0:
            if a < 0:
                w = [-a for a in w]
            break
    return tuple(w)

def rank_int(rows):
    # exact rank of integer/rational matrix rows (list of tuples)
    M = [list(map(Fraction, r)) for r in rows]
    if not M:
        return 0
    n = len(M); m = len(M[0])
    r = 0
    R = [row[:] for row in M]
    for c in range(m):
        piv = None
        for i in range(r, n):
            if R[i][c] != 0:
                piv = i; break
        if piv is None:
            continue
        R[r], R[piv] = R[piv], R[r]
        for i in range(n):
            if i != r and R[i][c] != 0:
                f = R[i][c]/R[r][c]
                for j in range(c, m):
                    R[i][j] -= f*R[r][j]
        r += 1
    return r

def null_basis_int(n0, d):
    # integer basis of hyperplane n0.x=0 in Q^d: return list of integer vecs
    # find coordinate with nonzero entry, use standard construction
    v = list(n0)
    i0 = next(i for i in range(d) if v[i] != 0)
    B = []
    for j in range(d):
        if j == i0:
            continue
        b = [0]*d
        b[j] = v[i0]
        b[i0] = -v[j]
        B.append(tuple(b))
    return B  # d-1 vectors spanning H0

# ---------- arrangement ----------
def build_cone(l, k):
    # coords x1..xl,z (dim l+1); return list of (name, normal tuple int)
    d = l+1
    N = []
    def e(i):
        v=[0]*d; v[i]=1; return v
    z=[0]*d; z[l]=1
    levels = list(range(-k+1, k+1))
    for i in range(l):
        for m in levels:
            n = e(i)[:]; n[l] = -m
            N.append((f"x{i+1}={m}z", tuple(n)))
    for i in range(l):
        for j in range(i+1, l):
            for m in levels:
                n1 = [0]*d; n1[i]=1; n1[j]=-1; n1[l]=-m
                n2 = [0]*d; n2[i]=1; n2[j]=1; n2[l]=-m
                N.append((f"x{i+1}-x{j+1}={m}z", tuple(n1)))
                N.append((f"x{i+1}+x{j+1}={m}z", tuple(n2)))
    N.append(("z=0", tuple(z)))
    return N

def restrict_to_hyperplane(N, idx0, d):
    # X = hyperplane with normal n0; return list of canonical restricted normals in Z^{d-1}
    n0 = N[idx0][1]
    B = null_basis_int(n0, d)  # basis of X
    out = []
    for t,(name,n) in enumerate(N):
        if t == idx0:
            continue
        # restricted coords: (n.b for b in B)
        r = tuple(sum(Fraction(n[i])*B[j][i] for i in range(d)) for j in range(d-1))
        if all(x==0 for x in r):
            continue  # contains X (shouldn't happen for distinct hyperplanes)
        out.append(primitive_canon(r))
    # deduplicate
    seen = []
    for v in out:
        if v not in seen:
            seen.append(v)
    return seen

def restrict_step(vecs, h_idx):
    # restrict arrangement (list of canon tuples in Z^d) to hyperplane vecs[h_idx]; return canon list in Z^{d-1}
    d = len(vecs[0])
    v = list(vecs[h_idx])
    i0 = next(i for i in range(d) if v[i] != 0)
    out = []
    for j,w in enumerate(vecs):
        if j == h_idx:
            continue
        w = list(w)
        # w' = w - (w_i0/v_i0) v, drop coord i0
        num = w[i0]; den = v[i0]
        r = []
        for i in range(d):
            if i == i0:
                continue
            # w_i - num/den * v_i
            r.append(Fraction(w[i])*den - Fraction(num)*v[i])
        if all(x==0 for x in r):
            continue
        out.append(primitive_canon(tuple(r)))
    seen=[]
    for x in out:
        if x not in seen:
            seen.append(x)
    return seen

from functools import lru_cache

def char_poly(vecs, d):
    # exact chi via deletion-restriction with memo; returns integer coeff list highest-degree first
    # canonical state
    vecs = tuple(sorted(set(vecs)))
    memo = {}
    def key(vs, dd):
        return (vs, dd)
    def chi(vs, dd):
        k = (vs, dd)
        if k in memo:
            return memo[k]
        if len(vs)==0:
            # t^dd
            p = [0]*(dd+1); p[0]=1
            memo[k]=p; return p
        # if some coordinate never appears (coloop-free part): rank check to peel off t factors
        r = rank_int([list(v) for v in vs])
        if r < dd:
            # chi = t^{dd-r} * chi(essentialized in r dims)
            # essentialize: project onto support coords: find r independent coords
            M = [list(v) for v in vs]
            # find pivot columns via elimination
            cols = pivot_cols(M, r)
            vs2 = tuple(sorted(set(tuple(v[c] for c in cols) for v in vs)))
            sub = chi(vs2, r)
            p = sub + [0]*(dd-r)
            memo[k]=p; return p
        # choose H: last
        H = vs[-1]
        rest = tuple(v for v in vs if v != H)
        # deletion
        p1 = chi(tuple(sorted(set(rest))), dd)
        # restriction: compute restricted vecs
        lst = list(vs)
        h = lst.index(H)
        vsr = tuple(sorted(set(restrict_step(lst, h))))
        p2 = chi(vsr, dd-1)
        p = polysub(p1, pad(p2, len(p1)))
        memo[k]=p; return p
    return chi(vecs, d)

def pivot_cols(M, r):
    m = len(M[0])
    cols=[]; rows_used=0
    R=[row[:] for row in M]
    n=len(R)
    for c in range(m):
        piv=None
        for i in range(rows_used,n):
            if R[i][c]!=0:
                piv=i;break
        if piv is None: continue
        R[rows_used],R[piv]=R[piv],R[rows_used]
        for i in range(n):
            if i!=rows_used and R[i][c]!=0:
                f=R[i][c]/R[rows_used][c]
                for j in range(c,m):
                    R[i][j]-=f*R[rows_used][j]
        cols.append(c); rows_used+=1
        if rows_used==r: break
    return cols

def polysub(a,b):
    n=max(len(a),len(b))
    a=[0]*(n-len(a))+list(a); b=[0]*(n-len(b))+list(b)
    return [x-y for x,y in zip(a,b)]

def pad(p,n):
    # pad polynomial (highest-first) to length n with leading zeros
    p=list(p)
    return [0]*(n-len(p))+p

def show_poly(p):
    import sympy as sp
    t=sp.Symbol('t')
    e=sum(c*t**(len(p)-1-i) for i,c in enumerate(p))
    return str(sp.expand(e)), str(sp.factor(e))
