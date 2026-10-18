#!/usr/bin/env python3
"""Finite exact checks for the integral nonmatching-complex representation theorem.
No additional packages are required. These tests corroborate, but do not replace,
the all-n argument by the relative homology long exact sequence.
"""
from itertools import combinations
from math import comb


def permutation_sign(xs):
    return -1 if sum(xs[i] > xs[j] for i in range(len(xs))
                     for j in range(i + 1, len(xs))) % 2 else 1


def partitions(n, lower=1):
    if n == 0:
        yield ()
    else:
        for k in range(lower, n + 1):
            for suffix in partitions(n - k, k):
                yield (k,) + suffix


def permutation_for_cycles(cycles):
    n = sum(cycles)
    p = list(range(n))
    start = 0
    for k in cycles:
        for i in range(k):
            p[start+i] = start+(i+1)%k
        start += k
    return p


def exterior_three_character(n, cycles):
    # Characteristic polynomial det(I+t P) of the vertex permutation module,
    # divided by (1+t) for its invariant line; coefficients are integers.
    a = [1] + [0]*3
    for k in cycles:
        b = a[:]
        if k <= 3:
            c = -(-1)**k
            for j in range(k, 4):
                b[j] += c*a[j-k]
        a = b
    u = [0]*4
    for j in range(4):
        u[j] = a[j] - (u[j-1] if j else 0)
    return u[3]


def all_faces(n):
    edges = list(combinations(range(n), 2))
    edge_id = {edge: i for i, edge in enumerate(edges)}
    f = set()
    for center in range(n):
        star = [edge_id[e] for e in edges if center in e]
        for r in range(1, len(star)+1):
            f.update(combinations(star, r))
    for a, b, c in combinations(range(n), 3):
        f.add(tuple(sorted([edge_id[a,b], edge_id[b,c], edge_id[a,c]])))
    return edges, edge_id, f


def lefschetz_h2(n, p, data):
    edges, edge_id, faces = data
    t = 0
    for face in faces:
        image = [edge_id[tuple(sorted((p[edges[i][0]],p[edges[i][1]])))]
                 for i in face]
        if set(image) == set(face):
            t += (-1)**(len(face)-1)*permutation_sign(image)
    return t-1  # H_0 has the trivial character and no other positive homology.


def check_contraction(n):
    # Triangles (relative 2-cells) map to triangle cycles in the graph.
    # Graph cycles are in the kernel of the vertex-incidence boundary.
    vert = list(range(n))
    edges = list(combinations(vert, 2))
    emap = {e:i for i,e in enumerate(edges)}
    cols = []
    for i,j,k in combinations(vert, 3):
        vec = [0]*len(edges)
        vec[emap[i,j]] += 1
        vec[emap[j,k]] += 1
        vec[emap[i,k]] -= 1
        cols.append(vec)
        for v in range(n):
            incident = sum((1 if b==v else -1 if a==v else 0)*vec[q]
                           for q,(a,b) in enumerate(edges))
            assert incident == 0
    # Standard triangles through vertex 0 form an integral basis for all
    # graph 1-cycles: each non-tree edge (i,j), 1<=i<j<n, occurs with unit
    # coefficient only in its own triangle (0,i,j).
    for i,j in combinations(range(1,n), 2):
        col = cols[list(combinations(range(n),3)).index((0,i,j))]
        assert col[emap[i,j]] == 1
        for a,b in combinations(range(1,n), 2):
            if (a,b)!=(i,j):
                assert col[emap[a,b]] == 0
    # Basis for ker(contraction): boundary of each oriented tetrahedron
    # with apex 0. Check coefficientwise for all generators.
    triangles = list(combinations(range(n),3))
    for i,j,k in combinations(range(1,n),3):
        a = [[0]*len(triangles) for _ in range(1)]
        coef = { (i,j,k): 1,(0,j,k): -1,(0,i,k): 1,(0,i,j): -1 }
        for idx,t in enumerate(triangles):
            a[0][idx] = coef.get(t,0)
        boundary = [sum(a[0][j]*cols[j][q] for j in range(len(cols)))
                    for q in range(len(edges))]
        assert all(x==0 for x in boundary)
    assert comb(n,3)-comb(n-1,2) == comb(n-1,3)


def main():
    cases=0
    for n in range(4,9):
        data=all_faces(n)
        assert len(data[2]) > 0
        check_contraction(n)
        for cyc in partitions(n):
            p=permutation_for_cycles(cyc)
            got=lefschetz_h2(n,p,data)
            expected=exterior_three_character(n,cyc)
            assert got==expected,(n,cyc,got,expected)
            cases+=1
        got=lefschetz_h2(n,list(range(n)),data)
        assert got==comb(n-1,3)
    print('VERIFY_OK_NONMATCHING_K2_INTEGRAL_EXTERIOR_CUBE')
    print('CYCLE_TYPES_CHECKED', cases, 'RANGE_n_4_TO_8')
    print('GRAPH_TRIANGLE_INTEGRAL_SURJECTIVITY_AND_TETRAHEDRAL_KERNEL_CHECKED')

if __name__=='__main__':
    main()
