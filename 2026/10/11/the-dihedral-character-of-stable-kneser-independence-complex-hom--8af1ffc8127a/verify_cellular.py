#!/usr/bin/env python3
"""Independent chord-graph cellular trace and low-degree boundary checks.

The model consists of the graph complementary to an m-cycle, with one
oriented 2-cell for each triangle. No use of Schrijver complex face lists.
"""
from itertools import combinations


def parity(perm):
    return 1 if (sum(a > b for i, a in enumerate(perm)
                     for b in perm[i+1:]) % 2 == 0) else -1


def formula(m, refl, j):
    if not refl:
        if j == 0:
            return (m*(m-4)*(m-5))//6 - m*(m-3)//2 + m - 1
        if m%2 == 0 and j == m//2:
            return m//2-1
        if m%3 == 0 and j in (m//3, 2*m//3):
            return m//3-1
        return -1
    return 1 if m%2 else ((3-m//2) if j%2 == 0 else (m//2-3))


def rank_modp(rows, mod):
    pivots = {}
    rank = 0
    for vec in rows:
        v = dict((i, a%mod) for i, a in vec.items() if a%mod)
        while v:
            k = min(v)
            if k in pivots:
                w = pivots[k]
                scale = v[k]
                for col, val in w.items():
                    t = (v.get(col, 0)-scale*val) % mod
                    if t:
                        v[col] = t
                    else:
                        v.pop(col, None)
            else:
                mul = pow(v[k], -1, mod)
                pivots[k] = {col: (mul*val)%mod for col, val in v.items()}
                rank += 1
                break
    return rank


def run(m):
    edges = [e for e in combinations(range(m), 2)
             if (e[1]-e[0]) not in (1,m-1)]
    triangles = [t for t in combinations(range(m), 3)
                 if all(tuple(sorted(e)) in edges for e in combinations(t, 2))]
    assert len(edges) == m*(m-3)//2
    assert len(triangles) == m*(m-4)*(m-5)//6
    edge_lookup = {e:i for i,e in enumerate(edges)}
    cols = []
    for a,b,c in triangles:
        cols.append({edge_lookup[(a,b)]:1, edge_lookup[(a,c)]:-1,
                     edge_lookup[(b,c)]:1})
    if m <= 13:
        for p in (2,3,5):
            assert rank_modp(cols,p) == len(edges)-m+1, (m,p)
    counts = 0
    for refl in (False, True):
        for j in range(m):
            f = (lambda x:(j-x)%m) if refl else (lambda x:(x+j)%m)
            total = -1  # remove the trivial H0 character
            total += sum(f(x)==x for x in range(m))
            for edge in edges:
                image = tuple(f(x) for x in edge)
                if set(image) == set(edge):
                    total -= parity([edge.index(x) for x in image])
            for tri in triangles:
                image = tuple(f(x) for x in tri)
                if set(image) == set(tri):
                    total += parity([tri.index(x) for x in image])
            assert total == formula(m, refl, j), (m,refl,j,total,formula(m,refl,j))
            counts += 1
    print('m=%d chords=%d triangles=%d elements=%d' % (m,len(edges),len(triangles),counts))


if __name__ == '__main__':
    for size in range(8, 21):
        run(size)
    print('CELLULAR TRACE AND BOUNDARY CHECKS PASS')
