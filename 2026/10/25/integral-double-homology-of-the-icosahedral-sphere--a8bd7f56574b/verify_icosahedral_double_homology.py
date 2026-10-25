#!/usr/bin/env python3
"""Exact integral double-homology computation for the boundary of an icosahedron.

Requirements: Python 3.11+, NumPy, SymPy.
The script enumerates all induced subcomplexes, computes integral homology bases
using Smith normal decompositions, constructs the inclusion-induced double
differentials, and verifies them by exact unit-pivot reductions over Z.
"""
from __future__ import annotations
import itertools, json, collections
from pathlib import Path
import numpy as np
import sympy as sp
from sympy import Matrix, ZZ, eye, zeros
from sympy.matrices.normalforms import smith_normal_decomp

N = 12
OUT = Path(__file__).with_name("COMPUTATION.json")

# Standard icosahedral graph: top and bottom poles, two 5-cycles, and a band.
edges = set()
def add_edge(a, b):
    edges.add(tuple(sorted((a, b))))
for i in range(5):
    u, un = 2+i, 2+(i+1)%5
    ell, elln = 7+i, 7+(i+1)%5
    add_edge(0, u); add_edge(1, ell)
    add_edge(u, un); add_edge(ell, elln)
    add_edge(u, ell); add_edge(u, 7+(i-1)%5)

simplices_by_size = {1: [], 2: [], 3: []}
for r in (1, 2, 3):
    for s in itertools.combinations(range(N), r):
        if r == 1:
            simplices_by_size[r].append(s)
        elif r == 2 and s in edges:
            simplices_by_size[r].append(s)
        elif r == 3 and all(tuple(sorted(e)) in edges
                            for e in itertools.combinations(s, 2)):
            simplices_by_size[r].append(s)
assert (len(simplices_by_size[1]), len(simplices_by_size[2]),
        len(simplices_by_size[3])) == (12, 30, 20)
assert all(sum(v in e for e in edges) == 5 for v in range(N))

def faces(mask, q):
    if q == -1:
        return [()]
    return [s for s in simplices_by_size[q+1]
            if all((mask >> v) & 1 for v in s)]

# Modular linear algebra, used to locate nonzero H_0 and H_1 groups.
def rref_mod(A, p):
    A = np.array(A, dtype=int, copy=True) % p
    if A.ndim == 1:
        A = A.reshape(1, -1)
    m, n = A.shape
    pivots, r = [], 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i, c] % p), None)
        if pivot is None:
            continue
        if pivot != r:
            A[[r, pivot]] = A[[pivot, r]]
        A[r, :] = (A[r, :] * pow(int(A[r, c]), -1, p)) % p
        for i in range(m):
            if i != r and A[i, c] % p:
                fac = int(A[i, c]) % p
                A[i, :] = (A[i, :] - fac*A[r, :]) % p
        pivots.append(c)
        r += 1
        if r == m:
            break
    return A, pivots

def rank_mod(A, p):
    A = np.asarray(A, dtype=int)
    if A.ndim == 1:
        A = A.reshape(1, -1)
    return len(rref_mod(A, p)[1])

def nullspace_mod(A, p):
    A = np.asarray(A, dtype=int)
    if A.ndim == 1:
        A = A.reshape(1, -1)
    _, pivots = rref_mod(A, p)
    m, n = A.shape
    R, pivots = rref_mod(A, p)
    free = [c for c in range(n) if c not in pivots]
    out = []
    for f in free:
        v = np.zeros(n, dtype=int); v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = (-R[i, f]) % p
        out.append(v)
    return np.column_stack(out) if out else np.zeros((n, 0), dtype=int)

def col_basis_mod(A, p):
    A = np.asarray(A, dtype=int)
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    if A.shape[1] == 0:
        return np.zeros((A.shape[0], 0), dtype=int)
    _, pivots = rref_mod(A, p)
    return A[:, pivots] % p

def complement_mod(B, Z, p):
    B = col_basis_mod(B, p)
    cols = [B[:, i] for i in range(B.shape[1])]
    r = len(cols); H = []
    for j in range(Z.shape[1]):
        z = Z[:, j] % p
        candidate = np.column_stack(cols + [z]) if cols else z.reshape(-1, 1)
        new_r = rank_mod(candidate, p)
        if new_r > r:
            H.append(z); cols.append(z); r = new_r
    return np.column_stack(H) if H else np.zeros((Z.shape[0], 0), dtype=int)

def boundary_mod(mask, q, p, f):
    src, tgt = f[q], f[q-1]
    tidx = {s:i for i,s in enumerate(tgt)}
    A = np.zeros((len(tgt), len(src)), dtype=int)
    if q == 0:
        for j, s in enumerate(src):
            A[tidx[()], j] = 1
    elif q >= 1:
        for j, s in enumerate(src):
            for i in range(len(s)):
                A[tidx[s[:i]+s[i+1:]], j] = (-1)**i
    return A % p

def homology_mod(mask, p):
    f = {q:faces(mask, q) for q in (-1, 0, 1, 2)}
    D = {-1:np.zeros((0,1),dtype=int)}
    for q in (0,1,2):
        D[q] = boundary_mod(mask, q, p, f)
    D[3] = np.zeros((len(f[2]),0),dtype=int)
    out = {}
    for q in (-1,0,1,2):
        Z = nullspace_mod(D[q], p)
        B = col_basis_mod(D[q+1], p)
        H = complement_mod(B, Z, p)
        out[q] = H.shape[1]
    return out

# Integral Smith normal decomposition. Returns S,U,V with S = U*A*V.
def snf(A):
    A = Matrix(A)
    m, n = A.shape
    if m == 0 or n == 0:
        return zeros(m,n), eye(m), eye(n)
    S, U, V = smith_normal_decomp(A, domain=ZZ)
    assert U*A*V == S
    return S, U, V

def boundary_Z(mask, q, f):
    src, tgt = f[q], f[q-1]
    tidx = {s:i for i,s in enumerate(tgt)}
    A = sp.zeros(len(tgt), len(src))
    if q == 0:
        for j, s in enumerate(src):
            A[tidx[()], j] = 1
    elif q >= 1:
        for j, s in enumerate(src):
            for i in range(len(s)):
                A[tidx[s[:i]+s[i+1:]], j] = (-1)**i
    return A

def integral_homology_selected(mask, needed_qs):
    f = {q:faces(mask, q) for q in (-1,0,1,2)}
    D = {q:boundary_Z(mask, q, f) for q in (0,1,2)}
    D[3] = sp.zeros(len(f[2]),0)
    decomps = {}
    wanted = set(needed_qs)
    wanted.update(q+1 for q in needed_qs if q+1 in (1,2))
    for q in wanted:
        if q in D:
            decomps[q] = snf(D[q])
    out = {}
    for q in needed_qs:
        Sq, Uq, Vq = decomps[q]
        rq = sum(1 for i in range(min(Sq.shape)) if Sq[i,i] != 0)
        Z = Vq[:, rq:]
        coords = (Vq.inv()*D[q+1])[rq:,:] if D[q+1].cols else sp.zeros(Z.cols,0)
        SB, UB, VB = snf(coords)
        rb = sum(1 for i in range(min(SB.shape)) if SB[i,i] != 0)
        factors = [abs(int(SB[i,i])) for i in range(rb)]
        # For subcomplexes of S^2, H_0 and H_1 are free; this exact
        # computation confirms the boundary lattice is saturated.
        assert all(d == 1 for d in factors), (mask, q, factors)
        H = Z * UB.inv()[:, rb:]
        projection = UB[rb:,:] * Vq.inv()[rq:,:]
        assert D[q]*H == sp.zeros(D[q].rows, H.cols)
        assert projection*H == sp.eye(H.cols)
        assert projection*D[q+1] == sp.zeros(projection.rows, D[q+1].cols)
        out[q] = {"faces":f[q], "H":H, "projection":projection,
                  "dim":H.cols, "rankD":rq, "rankB":rb}
    return out

def inclusion_matrix(source, target, q, intdata):
    sd = intdata.get(source, {}).get(q)
    td = intdata.get(target, {}).get(q)
    hs = sd["dim"] if sd else 0
    ht = td["dim"] if td else 0
    if hs == 0 or ht == 0:
        return sp.zeros(ht, hs)
    sf, tf = faces(source,q), faces(target,q)
    tidx = {s:i for i,s in enumerate(tf)}
    E = sp.zeros(len(tf), len(sf))
    for j, s in enumerate(sf):
        E[tidx[s],j] = 1
    M = td["projection"] * E * sd["H"]
    assert all(v.q == 1 for v in M)
    return M

def build_double_differential(q, l, intdata, inc_cache):
    src_masks = [mask for mask in range(1<<N)
                 if mask.bit_count()==l and intdata.get(mask,{}).get(q,{"dim":0})["dim"]>0]
    tgt_masks = [mask for mask in range(1<<N)
                 if mask.bit_count()==l+1 and intdata.get(mask,{}).get(q,{"dim":0})["dim"]>0]
    so, to, ns, nt = {}, {}, 0, 0
    for mask in src_masks:
        so[mask] = ns; ns += intdata[mask][q]["dim"]
    for mask in tgt_masks:
        to[mask] = nt; nt += intdata[mask][q]["dim"]
    D = sp.zeros(nt, ns)
    for mask in src_masks:
        hs, base = intdata[mask][q]["dim"], so[mask]
        for x in range(N):
            if (mask >> x) & 1:
                continue
            target = mask | (1 << x)
            ht = intdata.get(target,{}).get(q,{"dim":0})["dim"]
            if not ht:
                continue
            key = (mask,target,q)
            if key not in inc_cache:
                inc_cache[key] = inclusion_matrix(mask,target,q,intdata)
            M = inc_cache[key]
            sign = (-1)**((mask & ((1<<x)-1)).bit_count())
            rb = to[target]
            for i in range(ht):
                for j in range(hs):
                    if M[i,j]:
                        D[rb+i,base+j] += sign*M[i,j]
    return D

def unit_pivot_reduce(A):
    """Unimodular row/column elimination using only pivots +1 or -1."""
    M = [[int(v) for v in row] for row in A.tolist()]
    pivots = 0
    while M and M[0]:
        m, n = len(M), len(M[0])
        row_nz = [sum(x != 0 for x in row) for row in M]
        col_nz = [sum(M[i][j] != 0 for i in range(m)) for j in range(n)]
        best = None; bestscore = None
        for i in range(m):
            for j, x in enumerate(M[i]):
                if x in (1,-1):
                    score = row_nz[i]*col_nz[j]
                    if best is None or score < bestscore:
                        best, bestscore = (i,j,x), score
                        if score <= 1:
                            break
            if bestscore is not None and bestscore <= 1:
                break
        if best is None:
            break
        i, j, pivot = best
        pivotrow = M[i]
        # Schur complement for a unit pivot is equivalent to integral
        # row/column operations, hence preserves Smith invariant factors.
        newM = []
        for ii, row in enumerate(M):
            if ii == i:
                continue
            aic = row[j]
            newM.append([
                val - (aic*pivotrow[jj]//pivot)
                for jj, val in enumerate(row) if jj != j
            ])
        M = newM
        pivots += 1
    nonzero = sum(x != 0 for row in M for x in row)
    return pivots, len(M), (len(M[0]) if M else 0), nonzero

def main():
    # Enumerate all induced subcomplexes over F_2. H_0 and H_1 of a
    # subcomplex of S^2 are torsion-free, so these ranks identify all
    # nonzero integral H_0/H_1 groups; H_2 is Z only for the full sphere.
    mod2 = {}
    for mask in range(1<<N):
        mod2[mask] = homology_mod(mask, 2)
    needed = {}
    for mask, dims in mod2.items():
        qs = [q for q in (0,1) if dims[q] > 0]
        if qs:
            needed[mask] = qs
    intdata = {}
    for mask, qs in needed.items():
        intdata[mask] = integral_homology_selected(mask, qs)
        for q in qs:
            assert intdata[mask][q]["dim"] == mod2[mask][q]
    inc_cache, Dmats, unit = {}, {}, {}
    for q in (0,1):
        for l in range(N):
            Dmats[q,l] = build_double_differential(q,l,intdata,inc_cache)
        # terminal differential out of C^N
        last_dim = Dmats[q,N-1].rows
        Dmats[q,N] = sp.zeros(0,last_dim)
    # Verify d^2=0 exactly.
    for q in (0,1):
        for l in range(1,N+1):
            A, B = Dmats[q,l], Dmats[q,l-1]
            assert A.cols == B.rows
            assert A*B == sp.zeros(A.rows,B.cols), (q,l,"d^2")
    # Every nonzero Smith factor of every differential is 1: the unit-pivot
    # elimination exhausts each matrix and leaves an all-zero residual.
    ranks, dimensions = {}, {}
    for q in (0,1):
        for l in range(N+1):
            D = Dmats[q,l]
            rank, rr, cc, nz = unit_pivot_reduce(D)
            assert nz == 0, (q,l,rank,rr,cc,nz)
            ranks[q,l] = rank
            dimensions[q,l] = D.cols
            assert rank == rank_mod(np.array(D.tolist(),dtype=int),2)
    hh = {}
    for q in (0,1):
        for l in range(N+1):
            prev = ranks.get((q,l-1),0) if l else 0
            dim = dimensions[q,l]
            h = dim-ranks[q,l]-prev
            assert h >= 0
            if h:
                hh[f"q={q},l={l}"] = h
    # Add the two endpoint groups: reduced H_{-1} of the empty subcomplex
    # and H_2 of the full icosahedral sphere.
    hh["q=-1,l=0"] = 1
    hh["q=2,l=12"] = 1
    expected = {
        "q=-1,l=0":1, "q=0,l=2":1, "q=0,l=5":10,
        "q=1,l=7":10, "q=1,l=10":1, "q=2,l=12":1
    }
    assert hh == expected, hh
    report = {
        "complex":"boundary of the icosahedron",
        "vertex_count":12, "edge_count":30, "triangle_count":20,
        "induced_subcomplexes_enumerated":1<<N,
        "induced_subcomplexes_with_nonzero_H0_or_H1":len(needed),
        "integral_inclusion_maps_constructed":len(inc_cache),
        "all_d_squared_zero":True,
        "all_differentials_exhausted_by_unit_pivots":True,
        "differential_ranks":{
            f"q={q},l={l}":{"chain_dimension":dimensions[q,l],"rank":ranks[q,l]}
            for q in (0,1) for l in range(N+1)
        },
        "nonzero_double_homology_regraded":{
            "HH_(0,0)":1, "HH_(-1,4)":1, "HH_(-4,10)":10,
            "HH_(-5,14)":10, "HH_(-8,20)":1, "HH_(-9,24)":1
        },
        "total_rank":24,
        "limitations":[
            "This is the integral double homology of this single icosahedral sphere.",
            "No classification of other sphere triangulations or moment-angle spaces is claimed."
        ]
    }
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"status":"PASS","report":str(OUT),"groups":expected,
                      "total_rank":24,"subsets":1<<N,
                      "unit_pivot_checks":len(ranks),"maps":len(inc_cache)},sort_keys=True))

if __name__ == "__main__":
    main()
