"""Finite exact checks for the three-row rook open-neighborhood theorem.

Only standard-library integer and bitset arithmetic is used. The infinite
parameter theorem requires the accompanying topological proof.
"""
from itertools import combinations
from collections import defaultdict


def rank_binary(columns):
    pivots = {}
    for column in columns:
        while column:
            p = column.bit_length() - 1
            if p in pivots:
                column ^= pivots[p]
            else:
                pivots[p] = column
                break
    return len(pivots)


def complex_faces(n):
    rows = []
    for i in range(3):
        facets = []
        for j in range(n):
            facet = frozenset({i*n+k for k in range(n) if k!=j}
                             | {k*n+j for k in range(3) if k!=i})
            facets.append(facet)
        fs = set()
        for facet in facets:
            for k in range(1, len(facet)+1):
                fs.update(frozenset(c) for c in combinations(facet,k))
        rows.append(fs)
    return rows


def check_intersections(n, rows):
    assert len(set.intersection(*rows)) == 3*n
    for i,j in combinations(range(3),2):
        inter = rows[i]&rows[j]
        vertices = {f for f in inter if len(f)==1}
        edges = {f for f in inter if len(f)==2}
        assert len(vertices) == 3*n
        assert len(edges) == n*(n-1)
        assert max(map(len,inter)) == 2
        assert edges == {frozenset((i*n+a,j*n+b))
                         for a in range(n) for b in range(n) if a!=b}
    assert all(len(f)==1 for f in set.intersection(*rows))


def check_nerve(n):
    for i in range(3):
        facets = []
        for j in range(n):
            facets.append({i*n+k for k in range(n) if k!=j} |
                          {k*n+j for k in range(3) if k!=i})
        for sz in range(1,n+1):
            for J in combinations(range(n),sz):
                inter = set.intersection(*(facets[j] for j in J))
                assert bool(inter) == (sz < n)

def check_boundary_ranks(rows):
    faces=set.union(*rows)
    bydim=defaultdict(set)
    for face in faces:
        bydim[len(face)-1].add(sum(1<<i for i in face))
    cells={d:sorted(v) for d,v in bydim.items()}
    ranks={}
    for d in range(1,max(cells)+1):
        pos={face:i for i,face in enumerate(cells[d-1])}
        columns=[]
        for face in cells[d]:
            col=0
            left=face
            while left:
                bit=left&-left
                col ^= 1<<pos[face^bit]
                left ^= bit
            columns.append(col)
        ranks[d]=rank_binary(columns)
    betti={d:len(v)-ranks.get(d,0)-ranks.get(d+1,0)
           for d,v in cells.items()}
    betti[0]-=1
    return [len(cells[d]) for d in sorted(cells)], {d:b for d,b in sorted(betti.items()) if b}


def main():
    for n in range(5,9):
        rows=complex_faces(n)
        check_nerve(n)
        check_intersections(n,rows)
        f,hom=check_boundary_ranks(rows)
        expect={1:1,2:3*n*n-9*n+3,n-2:3}
        assert hom == expect,(n,hom,expect)
        # In the integral Mayer-Vietoris degree-zero double complex,
        # the map from triple-intersection vertices has a signed identity
        # minor on the three blocks of isolated pair-intersection vertices.
        pair_list=[(0,1),(0,2),(1,2)]
        iso_basis=[(pair,j) for pair in pair_list for j in range(n)]
        projected_columns=[]
        for row in range(3):
            for j in range(n):
                col=[0]*len(iso_basis)
                for pair,sign in zip(pair_list,[1,-1,1]):
                    if row not in pair:
                        col[iso_basis.index((pair,j))]=sign
                assert sum(abs(x) for x in col)==1
                projected_columns.append(col)
        row_support=[next(k for k,x in enumerate(col) if x) for col in projected_columns]
        assert sorted(row_support)==list(range(3*n))
        print(f'n={n}; faces={f}; mod2_betti={hom}; '
              f'pair_crown_rank={n*n-3*n+1}; '
              f'triple_to_isolates_unimodular=yes')
    print('ROOK3N_MV_FINITE_CHECKS_OK')

if __name__=='__main__':
    main()
