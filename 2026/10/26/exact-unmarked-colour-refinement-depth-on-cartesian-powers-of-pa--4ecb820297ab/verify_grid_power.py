"""Independent exact-round checks for uniform color refinement on Cartesian powers of paths.

Python 3 standard library only. Not a proof for all n,d; tests exact finite cases.
"""
import itertools
import math
from collections import Counter, defaultdict


def partition(values):
    d = {}
    return tuple(d.setdefault(v, len(d)) for v in values)


def refine(colors, neighbors):
    old = partition(colors)
    sigs = [(old[v], tuple(sorted(Counter(old[w] for w in adj).items())))
            for v, adj in enumerate(neighbors)]
    return partition(sigs)


def build(n, dim):
    verts = list(itertools.product(range(n), repeat=dim))
    index = {v: j for j, v in enumerate(verts)}
    adjacency = []
    for x in verts:
        row = []
        for i in range(dim):
            for delta in (-1, 1):
                xi = x[i] + delta
                if 0 <= xi < n:
                    y = list(x)
                    y[i] = xi
                    row.append(index[tuple(y)])
        adjacency.append(row)
    return verts, adjacency


def profile(x, n, t):
    counts = Counter(min(i, n - 1 - i) for i in x)
    return tuple(counts.get(i, 0) for i in range(t))


def check_full(n, dim):
    r = (n-1)//2
    vertices, adjacency = build(n, dim)
    colors = (0,) * len(vertices)
    for t in range(r+1):
        expected = partition(profile(x, n, t) for x in vertices)
        assert partition(colors) == expected, ('partition', n, dim, t)
        assert len(set(colors)) == math.comb(dim+t,t), ('class_count',n,dim,t)
        if t < r:
            colors = refine(colors, adjacency)
    assert partition(colors) == partition(refine(colors, adjacency)), ('not_stable',n,dim)
    counts = Counter(profile(x, n, r+1) for x in vertices)
    assert len(counts) == math.comb(dim+r,r), ('orbit_count',n,dim)
    for hist, actual in counts.items():
        expected = math.factorial(dim)
        for cj in hist:
            expected //= math.factorial(cj)
        if n%2 == 0:
            expected *= 2**dim
        else:
            expected *= 2**(dim-hist[-1])
        assert expected == actual, ('orbit_size',n,dim,hist,actual,expected)
    return len(vertices)


def weighted_profile_neighbors(n, hist):
    r=(n-1)//2
    target=defaultdict(int)
    for j, cnt in enumerate(hist):
        if not cnt:
            continue
        if r==0:
            target[hist]+=cnt
            continue
        if j>0:
            h=list(hist);h[j]-=1;h[j-1]+=1
            target[tuple(h)] += cnt * (2 if (j==r and n%2==1) else 1)
        if j<r:
            h=list(hist);h[j]-=1;h[j+1]+=1
            target[tuple(h)] += cnt
        elif n%2==0:
            target[hist] += cnt
    return dict(target)


def compositions(total, bins):
    if bins == 1:
        yield (total,)
        return
    for first in range(total+1):
        for rest in compositions(total-first, bins-1):
            yield (first,) + rest


def check_quotient(n,dim):
    r=(n-1)//2
    states=list(compositions(dim,r+1))
    ix={s:i for i,s in enumerate(states)}
    neighbours = [[(ix[u],c) for u,c in weighted_profile_neighbors(n,s).items()] for s in states]
    colors=(0,)*len(states)
    for t in range(r+1):
        expected=partition(tuple(s[:t]) for s in states)
        assert partition(colors)==expected, ('quotient_partition',n,dim,t)
        if t<r:
            p=partition(colors)
            sigs=[]
            for v,row in enumerate(neighbours):
                co=defaultdict(int)
                for w,c in row:
                    co[p[w]]+=c
                sigs.append((p[v],tuple(sorted(co.items()))))
            colors=partition(sigs)
    assert len(set(colors))==len(states), ('quotient_orbits',n,dim)
    return len(states)


def main():
    full=0
    vertex_total=0
    for n in range(2,18):
        for dim in range(1,10):
            if n**dim > 900:
                continue
            vertex_total+=check_full(n,dim)
            full+=1
    quot=0
    state_total=0
    for n in range(2,30):
        for dim in range(1,13):
            if math.comb(dim+(n-1)//2,(n-1)//2)>600:
                continue
            state_total+=check_quotient(n,dim)
            quot+=1
    for n, dim in ((51,2),(101,2),(20,3),(11,6),(5,50),(2,100)):
        state_total+=check_quotient(n,dim)
        quot+=1
    print(f'FULL_GRAPH_CONFIGURATIONS={full}')
    print(f'FULL_GRAPH_TOTAL_VERTICES={vertex_total}')
    print(f'WEIGHTED_QUOTIENT_CONFIGURATIONS={quot}')
    print(f'WEIGHTED_QUOTIENT_TOTAL_STATES={state_total}')
    print('ALL_TESTS_PASS')


if __name__=='__main__':main()
