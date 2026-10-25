#!/usr/bin/env python3
"""Independent reproducible integral cellular computation for cube graph two-particle spaces.

Python 3; needs NumPy, SciPy, SymPy. No external files or private inputs.
"""
from itertools import combinations, permutations
from collections import defaultdict
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def rank_mod(matrix, prime):
    a = (matrix.toarray() if hasattr(matrix, 'toarray') else np.asarray(matrix)).copy().astype(np.int64) % prime
    m, n = a.shape
    rank = 0
    cols = []
    for j in range(n):
        if rank == m:
            break
        options = np.flatnonzero(a[rank:, j])
        if len(options) == 0:
            continue
        k = rank + int(options[0])
        if k != rank:
            a[[rank, k]] = a[[k, rank]]
        a[rank, j:] = (a[rank, j:] * pow(int(a[rank, j]), -1, prime)) % prime
        below = np.flatnonzero(a[rank+1:, j]) + rank + 1
        if len(below):
            a[below, j:] = (a[below, j:] - a[below, j:j+1] * a[rank:rank+1, j:]) % prime
        cols.append(j)
        rank += 1
    return rank, cols


def make_complex():
    d = 4
    vertices = range(16)
    edges = sorted((v, v ^ (1 << i)) for v in vertices for i in range(d) if v < (v ^ (1 << i)))
    assert len(edges) == 32
    cells0 = list(combinations(vertices, 2))
    idx0 = {cell: i for i, cell in enumerate(cells0)}
    cells1 = [(v, edge) for edge in edges for v in vertices if v not in edge]
    idx1 = {cell: i for i, cell in enumerate(cells1)}
    cells2 = [(e, f) for a, e in enumerate(edges) for f in edges[a+1:] if not set(e).intersection(f)]
    idx2 = {cell: i for i, cell in enumerate(cells2)}
    assert (len(cells0), len(cells1), len(cells2)) == (120, 448, 400)
    r1 = []; c1 = []; v1 = []
    for j, (v, (a, b)) in enumerate(cells1):
        for u, s in [(b, +1), (a, -1)]:
            r1.append(idx0[tuple(sorted((v, u)))])
            c1.append(j)
            v1.append(s)
    boundary1 = coo_matrix((v1, (r1, c1)), shape=(120,448), dtype=np.int64).tocsr()
    r2 = []; c2 = []; v2 = []
    for j, (e, f) in enumerate(cells2):
        for u, s in [(e[1], +1), (e[0], -1)]:
            r2.append(idx1[(u, f)]); c2.append(j); v2.append(s)
        for u, s in [(f[1], -1), (f[0], +1)]:
            r2.append(idx1[(u, e)]); c2.append(j); v2.append(s)
    boundary2 = coo_matrix((v2, (r2, c2)), shape=(448, 400), dtype=np.int64).tocsc()
    assert (boundary1 @ boundary2).nnz == 0
    cycles = []
    for i, j in combinations(range(4),2):
        for x in vertices:
            if not ((x >> i) & 1 or (x >> j) & 1):
                cycles.append((x, x^(1<<i), x^(1<<i)^(1<<j), x^(1<<j)))
    assert len(cycles) == 24
    pairs = []; tori = []
    for a, b in combinations(range(24),2):
        A, B = cycles[a], cycles[b]
        if not set(A).isdisjoint(B):
            continue
        v = defaultdict(int)
        for k in range(4):
            u, w = A[k], A[(k+1)%4]
            e = tuple(sorted((u, w)))
            se = +1 if u < w else -1
            for l in range(4):
                z, y = B[l], B[(l+1)%4]
                f = tuple(sorted((z, y)))
                sf = +1 if z < y else -1
                p = tuple(sorted((e, f)))
                v[idx2[p]] += se * sf * (+1 if e < f else -1)
        assert len(v) == 16 and all(abs(t) == 1 for t in v.values())
        pairs.append((a,b)); tori.append(v)
    assert len(pairs) == 132
    T = coo_matrix(([v for col in tori for v in col.values()],
                    ([i for col in tori for i in col],
                     [j for j, col in enumerate(tori) for _ in col])),
                   shape=(400,132),dtype=np.int64).tocsc()
    assert (boundary2 @ T).nnz == 0
    return boundary1, boundary2, cycles, pairs, T


def symmetry_orbits(cycles, pairs):
    ci = {frozenset(c):i for i,c in enumerate(cycles)}
    pi = {p:i for i,p in enumerate(pairs)}
    perms = []
    for perm in permutations(range(4)):
        for mask in range(16):
            def transform(v):
                return mask ^ sum(((v>>i)&1)<<perm[i] for i in range(4))
            perms.append(tuple(ci[frozenset(transform(v) for v in cyc)] for cyc in cycles))
    assert len(perms) == 384 and len(set(perms)) == 384
    unseen = set(range(132)); orbits=[]
    while unseen:
        a, b = pairs[min(unseen)]
        orbit = {pi[tuple(sorted((q[a],q[b])))] for q in perms}
        assert orbit <= unseen
        orbits.append(sorted(orbit))
        unseen -= orbit
    assert list(map(len, orbits)) == [24,12,96]
    # Identify by original coordinate-face vertex intersections: first two are parallel,
    # third meets in exactly one free coordinate.
    for k, orbit in enumerate(orbits):
        i, j = pairs[orbit[0]]
        a, b = set(cycles[i]), set(cycles[j])
        assert not (a & b)
        varying = lambda verts: {v for v in range(4) if len({(w>>v)&1 for w in verts}) == 2}
        assert len(varying(a)&varying(b)) == (2 if k in (0,1) else 1)
    return orbits


def main():
    b1, b2, cycles, pairs, T = make_complex()
    orbits=symmetry_orbits(cycles,pairs)
    rank_boundary,_=rank_mod(b2,101)
    rank_tori,cols=rank_mod(T,2)
    assert (rank_boundary, rank_tori)==(312,88)
    assert rank_mod(T,101)[0]==88
    rank_rows,rows=rank_mod(T[:,cols].T,2)
    assert rank_rows==88
    B=sp.Matrix(T[rows,:][:,cols].toarray())
    det=int(B.det(method='domain-ge'))
    assert abs(det)==1
    coords=B.inv()*sp.Matrix(T[rows,:].toarray())
    assert all(v.q==1 for v in coords)
    assert B*coords == sp.Matrix(T[rows,:].toarray())
    output={}
    for k,orbit in enumerate(orbits):
        mat=coords[:,orbit]
        S=smith_normal_form(mat,domain=ZZ)
        diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i] !=0]
        output[k]=diag
    assert len(output[0])==24 and all(v==1 for v in output[0])
    assert len(output[1])==12 and all(v==1 for v in output[1])
    assert len(output[2])==88 and sorted(output[2])==[1]*82+[2]*6
    for extra in [0,1]:
        mat=coords[:,orbits[2]+orbits[extra]]
        S=smith_normal_form(mat,domain=ZZ)
        diag=[abs(int(S[i,i])) for i in range(88)]
        assert diag == [1]*88
    assert rank_mod(T[:,orbits[0]+orbits[1]],101)[0]==36
    print('CUBICAL_CELL_COUNTS',b1.shape[0],b1.shape[1],b2.shape[1])
    print('BOUNDARY_1_BOUNDARY_2_ZERO',True)
    print('BOUNDARY2_RANK_MOD101',rank_boundary)
    print('SQUARE_FACES',len(cycles),'VERTEX_DISJOINT_FACE_PAIRS',len(pairs))
    print('SQUARE_TORI_BOUNDARY_ZERO',True)
    print('SQUARE_TORI_RANK_MOD2',rank_tori)
    print('UNIT_MINOR_DETERMINANT',det)
    print('INTEGRAL_H2_RANK',400-rank_boundary)
    print('AUTOMORPHISM_GROUP_ORDER',384)
    print('TORUS_SYMMETRY_ORBITS',[len(o) for o in orbits])
    print('ORBIT_LATTICE_RANKS',[len(output[k]) for k in range(3)])
    print('NONPARALLEL_QUOTIENT_INVARIANT_FACTORS',[v for v in output[2] if v>1])
    print('NONPARALLEL_QUOTIENT_INDEX',2**6)
    print('ADD_EITHER_PARALLEL_ORBIT_GENERATES_FULL_INTEGRAL_H2',True)
    print('VERIFY_OK_HYPERCUBE_TWO_PARTICLE_TORUS_PARITY_INDEX')

if __name__=='__main__':main()
