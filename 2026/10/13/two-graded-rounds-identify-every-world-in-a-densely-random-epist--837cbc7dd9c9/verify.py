#!/usr/bin/env python3
"""Exact finite checks of graded vs ordinary refinement on randomly marked S5 grids.

Only standard Python library. No network, external data, or hidden dependencies.
"""
from collections import Counter
from itertools import product
from random import Random


def compress(items):
    lookup = {v: k for k, v in enumerate(sorted(set(items)))}
    return tuple(lookup[v] for v in items)


def refinement(matrix, counting, steps=2):
    n = len(matrix)
    assert n and all(len(row) == n for row in matrix)
    colors = compress(tuple(matrix[i][j] for i in range(n) for j in range(n)))
    out = [colors]
    for _ in range(steps):
        rows = [[colors[i*n+k] for k in range(n)] for i in range(n)]
        cols = [[colors[k*n+j] for k in range(n)] for j in range(n)]
        if counting:
            rf = [tuple(sorted(Counter(row).items())) for row in rows]
            cf = [tuple(sorted(Counter(col).items())) for col in cols]
        else:
            rf = [tuple(sorted(set(row))) for row in rows]
            cf = [tuple(sorted(set(col))) for col in cols]
        new = [(colors[i*n+j],rf[i],cf[j])
               for i in range(n) for j in range(n)]
        colors = compress(new)
        out.append(colors)
    return out


def histograms(matrix):
    n = len(matrix)
    row_degrees = [sum(row) for row in matrix]
    col_degrees = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    row_hists = [[0]*(n+1) for _ in range(n)]
    col_hists = [[0]*(n+1) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                row_hists[i][col_degrees[j]] += 1
                col_hists[j][row_degrees[i]] += 1
    return [tuple(a) for a in row_hists], [tuple(a) for a in col_hists]


def same_partition(a,b):
    assert len(a)==len(b)
    amap,bmap={},{}
    for x,y in zip(a,b):
        if x in amap: assert amap[x]==y
        else: amap[x]=y
        if y in bmap: assert bmap[y]==x
        else: bmap[y]=x
    return True


def test(matrix):
    n = len(matrix)
    graded = refinement(matrix, counting=True, steps=2)
    ordinary = refinement(matrix, counting=False, steps=2)
    # Depth one types of complete row/column S5 relations.
    rd = [sum(row) for row in matrix]
    cd = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    direct = compress([(matrix[i][j], rd[i], cd[j])
                       for i in range(n) for j in range(n)])
    assert same_partition(direct, graded[1]), (matrix, direct, graded[1])
    rh, ch = histograms(matrix)
    if len(set(rh)) == n and len(set(ch)) == n:
        assert len(set(graded[2])) == n*n, 'Histogram sufficient condition failed'
    # Each refinement is nested and uses the appropriate set/multiset semantics.
    for seq in (graded, ordinary):
        assert len(set(seq[0])) <= len(set(seq[1])) <= len(set(seq[2]))
    return (len(set(graded[0])),len(set(graded[1])),len(set(graded[2])),
            len(set(ordinary[2])))


def run():
    exhaustive = 0
    full_depth2 = {}
    for n in (1,2,3):
        counts=Counter()
        for bits in product((0,1),repeat=n*n):
            mat=[bits[i*n:(i+1)*n] for i in range(n)]
            counts[test(mat)] += 1
            exhaustive+=1
        full_depth2[n]=sum(v for k,v in counts.items() if k[2]==n*n)
    rng=Random(415921)
    cases=0
    summaries={}
    for p in (0.25,0.5,0.75):
        for n,rep in ((4,100),(6,100),(10,100),(20,100),(40,100),(64,100),(96,100)):
            a=b=c=0
            for _ in range(rep):
                mat=[[int(rng.random()<p) for j in range(n)] for i in range(n)]
                d0,d1,d2,o2=test(mat)
                a+=d2==n*n
                b+=d1<n*n
                c+=o2==2
                cases+=1
            summaries[(p,n)] = (a,b,c)
    print('VERIFY_OK exhaustive_binary_square_matrices',exhaustive,
          'random_trials',cases,'parameter_batches',len(summaries))
    print('small_exact_depth2_full_counts',full_depth2)
    for key in sorted(summaries):
        if key[1] in (20,40,64,96): print('density,size',key,'full_depth2,not_full_depth1,ordinary_two',summaries[key])


if __name__=='__main__':run()
