#!/usr/bin/env python3
"""Exhaustive finite verification of the scale-two four-by-n torus-grid collapse."""
from itertools import combinations
from collections import Counter


def index(n, column, row):
    return 4 * (column % n) + (row % 4)


def compatible(n, a, b):
    ca, ra = divmod(a, 4)
    cb, rb = divmod(b, 4)
    dc = min((ca - cb) % n, (cb - ca) % n)
    dr = min((ra - rb) % 4, (rb - ra) % 4)
    return dc + dr <= 2


def faces(n):
    nverts = 4 * n
    neighbors = [set(w for w in range(nverts) if w != v and compatible(n, v, w))
                 for v in range(nverts)]
    found = set()

    def traverse(face, candidates):
        found.add(face)
        for k, w in enumerate(candidates):
            traverse(face + (w,), [x for x in candidates[k+1:] if x in neighbors[w]])

    for v in range(nverts):
        traverse((v,), [w for w in range(v+1, nverts) if w in neighbors[v]])
    return found


def compare_and_collapse(n):
    full = faces(n)
    slabs = []
    for j in range(n):
        vs = {index(n, j, r) for r in range(4)} | {index(n, j + 1, r) for r in range(4)}
        slab = {f for f in full if set(f).issubset(vs)}
        assert len(slab) == 80, (n, j, len(slab))
        assert Counter(map(len, slab)) == Counter({1:8, 2:24, 3:32, 4:16})
        # The only four missing edges are the antipodal cross-column pairs.
        missing = [tuple(sorted((a,b))) for a,b in combinations(sorted(vs), 2)
                   if not compatible(n,a,b)]
        want = [tuple(sorted((index(n,j,r), index(n,j+1,r+2)))) for r in range(4)]
        assert sorted(missing) == sorted(want)
        slabs.append(slab)
    union = set().union(*slabs)
    assert len(union) == 4*n + 18*n + 28*n + 15*n
    assert Counter(map(len, full)) == Counter({1:4*n, 2:22*n, 3:40*n, 4:27*n, 5:4*n})
    assert Counter(map(len, full - union)) == Counter({2:4*n, 3:12*n, 4:12*n, 5:4*n})
    # Each non-slab face is uniquely associated to one pair of columns distance two.
    for f in full - union:
        longpairs = [tuple(sorted((a, b))) for a,b in combinations(f,2)
                     if divmod(a,4)[0] != divmod(b,4)[0]
                     and min((divmod(a,4)[0]-divmod(b,4)[0])%n,
                             (divmod(b,4)[0]-divmod(a,4)[0])%n)==2]
        assert len(longpairs) == 1, (n, f, longpairs)
        assert (longpairs[0][0] % 4) == (longpairs[0][1] % 4)
    remain = set(full)
    count = 0
    for j in range(n):
        for r in range(4):
            ends = {index(n,j-1,r), index(n,j+1,r)}
            middle = index(n,j,r)
            others = [index(n,j,r-1),index(n,j,r+1)]
            for q in (2,1,0):
                for subset in combinations(others,q):
                    a = tuple(sorted(ends | set(subset)))
                    b = tuple(sorted(ends | set(subset) | {middle}))
                    assert a in remain and b in remain
                    # A free face must be contained in one and only one maximal simplex.
                    assert [f for f in remain if len(f)>len(a) and set(a).issubset(f)] == [b], (n,j,r,a)
                    remain.remove(a)
                    remain.remove(b)
                    count += 1
    assert remain == union
    assert count == 16*n
    # Consecutive sphere slabs share a full tetrahedron; others are disjoint.
    for i in range(n):
        for j in range(i+1,n):
            overlap = slabs[i] & slabs[j]
            if (j-i) in (1,n-1):
                assert Counter(map(len,overlap)) == Counter({1:4,2:6,3:4,4:1})
            else:
                assert not overlap
    return len(full), count


def rank_mod_p(columns, rowindex, p):
    pivots = {}
    for face in columns:
        col = {}
        for i in range(len(face)):
            key = face[:i]+face[i+1:]
            j = rowindex[key]
            c = -1 if i%2 else 1
            col[j] = (col.get(j,0)+c)%p
            if not col[j]:del col[j]
        while col:
            i = max(col)
            if i not in pivots:
                c = pow(col[i], -1, p)
                pivots[i] = {j: (v*c)%p for j,v in col.items()}
                break
            c = col[i]
            for j,v in pivots[i].items():
                z = (col.get(j,0)-c*v)%p
                if z:col[j]=z
                elif j in col:del col[j]
    return len(pivots)


def homology(n,p):
    allfs=faces(n)
    dims = [[f for f in allfs if len(f)==k] for k in range(1,6)]
    ranks = [0]
    for d in range(1,5):
        rows = {f:i for i,f in enumerate(dims[d-1])}
        ranks.append(rank_mod_p(dims[d], rows, p))
    betas = [len(dims[d])-ranks[d]-ranks[d+1] if d<4 else len(dims[d])-ranks[d]
             for d in range(5)]
    betas[0]-=1
    assert betas == [0,1,0,n,0], (n,p,betas)
    return betas


def main():
    for n in range(7,25):
        f,pairs = compare_and_collapse(n)
        print('COLLAPSE_OK',n,f,pairs)
    for n in range(7,11):
        for p in (2,3,5):
            homology(n,p)
            print('HOMOLOGY_OK',n,p)
    print('VERIFY_OK 18 complete simplicial collapses; 12 exact homology checks')

if __name__ == '__main__':
    main()
