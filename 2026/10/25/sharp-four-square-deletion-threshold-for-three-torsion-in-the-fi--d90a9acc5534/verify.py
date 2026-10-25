#!/usr/bin/env python3
"""Exact integral certificate for deletion robustness of the 5-by-5 chessboard complex.

Python 3.10+ standard library only. The output contains an integral Smith-factor
certificate for every forbidden-edge orbit of size at most four.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, gcd

N = 5
CELLS = tuple(product(range(N), repeat=2))
PERMS = tuple(permutations(range(N)))

@lru_cache(maxsize=None)
def canonical(edges):
    """Complete S5 x S5 x C2 orbit key; unused rows/columns need no labels."""
    if not edges:
        return ()
    rr = sorted({r for r, c in edges})
    cc = sorted({c for r, c in edges})
    indexed = tuple((rr.index(r), cc.index(c)) for r, c in edges)
    best = None
    for swap in (False, True):
        pairs = tuple((c, r) if swap else (r, c) for r, c in indexed)
        a, b = (len(cc), len(rr)) if swap else (len(rr), len(cc))
        for rp in permutations(range(a)):
            for cp in permutations(range(b)):
                image = tuple(sorted(N * rp[r] + cp[c] for r, c in pairs))
                if best is None or image < best:
                    best = image
    return best

def orbit_representatives():
    ans = {(): frozenset()}
    yield 0, ans
    for k in range(1, 5):
        following = {}
        for old in ans.values():
            for sq in CELLS:
                if sq in old:
                    continue
                new = old | {sq}
                key = canonical(tuple(sorted(new)))
                following.setdefault(key, new)
        ans = dict(sorted(following.items()))
        yield k, ans

def orbit_size(forbidden):
    """Independent direct orbit computation with all row/column bijections."""
    images = set()
    for rp in PERMS:
        for cp in PERMS:
            one = frozenset((rp[r], cp[c]) for r, c in forbidden)
            images.add(one)
            images.add(frozenset((c, r) for r, c in one))
    return len(images)

def chessboard_faces(forbidden):
    f = {}
    for k in range(1, 6):
        cells = set()
        for rows in combinations(range(N), k):
            for cols in permutations(range(N), k):
                face = tuple((r, c) for r, c in zip(rows, cols))
                if forbidden.isdisjoint(face):
                    cells.add(face)
        f[k-1] = sorted(cells)
    # Each face is in increasing row order, hence canonical orientation.
    return f

def integer_boundary(faces, dimension):
    row_lookup = {face: i for i, face in enumerate(faces[dimension-1])}
    rows = {i: {} for i in range(len(row_lookup))}
    cols = {j: {} for j in range(len(faces[dimension]))}
    for j, face in enumerate(faces[dimension]):
        for i in range(dimension+1):
            facet = face[:i] + face[i+1:]
            r = row_lookup[facet]
            v = (-1)**i
            rows[r][j] = v
            cols[j][r] = v
    return rows, cols

def exact_unit_reduction(rows, cols):
    """Integer row/column operations on +/-1 pivots preserve all Smith factors.

    Each iteration clears the pivot row and column. The resulting matrix is
    integrally equivalent to diag(identity(number_of_pivots), remainder).
    """
    pivots = 0
    while True:
        best = None
        cost = None
        for i, row in rows.items():
            for j, val in row.items():
                if abs(val) == 1:
                    x = (len(row)-1) * (len(cols[j])-1)
                    if cost is None or x < cost:
                        cost, best = x, (i, j, val)
                    if x == 0:
                        break
            if cost == 0:
                break
        if best is None:
            break
        i, j, pivot = best
        row_entries = tuple(rows[i].items())
        col_entries = tuple(cols[j].items())
        for r, val in col_entries:
            if r == i:
                continue
            for c, other in row_entries:
                if c == j:
                    continue
                new_val = rows[r].get(c, 0) - val * other * pivot
                if new_val:
                    rows[r][c] = new_val
                    cols[c][r] = new_val
                else:
                    rows[r].pop(c, None)
                    cols[c].pop(r, None)
        for r, _ in col_entries:
            if r != i:
                rows[r].pop(j, None)
        for c, _ in row_entries:
            if c != j:
                cols[c].pop(i, None)
        del rows[i]
        del cols[j]
        pivots += 1
    assert all(cols[c].get(r) == v for r, row in rows.items() for c,v in row.items())
    assert all(rows[r].get(c) == v for c, col in cols.items() for r,v in col.items())
    return pivots

def exact_residual(rows, cols):
    """Return residual rational rank and unique nonunit invariant factor.

    Only rank 0 and rank 1 occur. Rank 1 is proved by the vanishing of all
    two-by-two minors, not merely by a finite-field calculation.
    """
    entries = [(i,j,v) for i,row in rows.items() for j,v in row.items()]
    if not entries:
        return 0, 0, 0
    i0,j0,a = entries[0]
    for i, row in rows.items():
        for j in cols:
            # Include zero entries: a minor involving a zero is still a minor.
            assert a*row.get(j,0) == row.get(j0,0)*rows[i0].get(j,0)
    g=0
    for _,_,v in entries:
        g=gcd(g,abs(v))
    return 1,g,len(entries)

def cycle_of_four(forbidden):
    rows = {r for r,c in forbidden}
    cols = {c for r,c in forbidden}
    return len(forbidden) == 4 and len(rows)==2 and len(cols)==2

def four_star(forbidden):
    return len(forbidden)==4 and (len({r for r,c in forbidden})==1 or len({c for r,c in forbidden})==1)

def main():
    orbit_profile=[]
    category_count=Counter()
    for k, representatives in orbit_representatives():
        total=0
        for key, forbidden in representatives.items():
            o=orbit_size(forbidden)
            total+=o
            faces=chessboard_faces(forbidden)
            fvec=[len(faces[d]) for d in range(5)]
            # d1,d2,d3 exact rank/Smith data are sufficient for H2.
            for d in (1,2):
                row,col=integer_boundary(faces,d)
                q=exact_unit_reduction(row,col)
                assert exact_residual(row,col)[0] == 0
                if d==1: assert q == fvec[0]-1
                else: assert q == fvec[1]-fvec[0]+1
                if d==2: rank2=q
            row,col=integer_boundary(faces,3)
            p=exact_unit_reduction(row,col)
            residual_rank,g,nnz=exact_residual(row,col)
            assert residual_rank in (0,1)
            assert (residual_rank,g) in ((0,0),(1,3))
            rank3=p+residual_rank
            free_rank=fvec[2]-rank2-rank3
            assert free_rank>=0
            if four_star(forbidden):
                assert (free_rank,g)==(8,0)
                category='four-star'
            elif cycle_of_four(forbidden):
                assert (free_rank,g)==(7,0)
                category='four-cycle'
            else:
                assert (free_rank,g)==(0,3)
                category='three-torsion'
            category_count[(k,category)]+=o
            orbit_profile.append(dict(k=k,key=key,orbit_size=o,faces=fvec,
                 rank_d2=rank2,unit_d3=p,remaining_rank=residual_rank,
                 residual_gcd=g,remaining_nnz=nnz,free_rank=free_rank,
                 category=category))
            print(f'k={k} key={key} orbit={o} f2={fvec[2]} '
                  f'd2rank={rank2} d3=units{p}+rank{residual_rank} '
                  f'residual_gcd={g} H2_free_rank={free_rank} {category}',flush=True)
        assert total==comb(25,k),(k,total,comb(25,k))
        print(f'ORBIT_SUM k={k} orbit_classes={len(representatives)} labeled_sets={total}',flush=True)
    assert category_count[(4,'four-star')]==50
    assert category_count[(4,'four-cycle')]==100
    assert category_count[(4,'three-torsion')]==12500
    for k in (0,1,2,3):
        assert category_count[(k,'three-torsion')]==comb(25,k)
    assert len(orbit_profile)==1+1+2+4+10
    print('FOUR_DELETION_TORSION_FREE 50_star + 100_cycle = 150',flush=True)
    print('FOUR_DELETION_TORSION_Z3 12500',flush=True)
    print('VERIFY_OK_CHESSBOARD_FOUR_DELETION_TORSION_THRESHOLD',flush=True)

if __name__ == '__main__':
    main()
