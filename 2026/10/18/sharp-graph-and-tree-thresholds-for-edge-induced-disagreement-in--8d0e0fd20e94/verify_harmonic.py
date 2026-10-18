#!/usr/bin/env python3
"""Exact finite verification for pinned two-source harmonic opinions.
Standalone: Python 3 standard library only. Vertex labels 0,...,n-1.
Leaders 0 and 1 are pinned at 0 and 1; followers 2,...,n-1.
No network, external data, or approximate arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def harmonic(n, edges):
    """Solve integer grounded-Laplacian equations exactly."""
    E = set(tuple(sorted(e)) for e in edges)
    m = n-2
    a = [[Q(0) for _ in range(m+1)] for __ in range(m)]
    for x in range(2,n):
        i=x-2
        for u,v in E:
            if x not in (u,v):
                continue
            y=v if u==x else u
            a[i][i]+=1
            if y==1:
                a[i][m]+=1
            elif y>=2:
                a[i][y-2]-=1
    for k in range(m):
        pivot=next((i for i in range(k,m) if a[i][k]),None)
        if pivot is None:
            raise ValueError('singular grounded Laplacian: disconnected graph')
        a[k],a[pivot]=a[pivot],a[k]
        coeff=a[k][k]
        a[k]=[z/coeff for z in a[k]]
        for i in range(m):
            if i==k: continue
            fac=a[i][k]
            if fac:
                a[i]=[a[i][j]-fac*a[k][j] for j in range(m+1)]
    return (Q(0),Q(1))+tuple(a[i][m] for i in range(m))


def polarization(h):
    # Equivalent to global disagreement divided by n, including both pinned leaders.
    mean=sum(h)/len(h)
    return sum((v-mean)**2 for v in h)


def connected(n,edges):
    seen={0}
    while True:
        reach=seen | {v if u in seen else u for u,v in edges if (u in seen) != (v in seen)}
        if reach==seen:break
        seen=reach
    return len(seen)==n


def graph_edges(n,mask):
    return tuple(e for j,e in enumerate(combinations(range(n),2)) if mask >> j & 1)


def exhaustive_graphs(max_n=5):
    total=0
    for n in range(2,max_n+1):
        pairs=list(combinations(range(n),2));free_pairs=list(combinations(range(2,n),2))
        num_connected=0; comparisons=0; strict_decrease=0; unchanged=0
        for mask in range(1 << len(pairs)):
            edges=tuple(pairs[j] for j in range(len(pairs)) if mask >> j & 1)
            if not connected(n,edges):continue
            num_connected+=1
            h=harmonic(n,edges);p=polarization(h)
            edge_set=set(edges)
            for e in free_pairs:
                if e in edge_set: continue
                hh=harmonic(n,edges+(e,));d=polarization(hh)-p
                if d>0:
                    raise AssertionError(('unexpected increase below six',n,edges,e,d))
                comparisons+=1
                if d<0:strict_decrease+=1
                else:unchanged+=1
        print('graphs n=%d connected=%d eligible_pairs=%d decreases=%d ties=%d' %
              (n,num_connected,comparisons,strict_decrease,unchanged))
        total+=comparisons
    return total


def prufer_edges(n,seq):
    degrees=[1]*n
    for x in seq:degrees[x]+=1
    E=[]
    for x in seq:
        leaf=next(v for v in range(n) if degrees[v]==1)
        E.append(tuple(sorted((leaf,x))))
        degrees[leaf]-=1
        degrees[x]-=1
    u,v=[i for i in range(n) if degrees[i]==1]
    E.append((u,v))
    return tuple(E)


def exhaustive_trees(max_n=6):
    for n in range(2,max_n+1):
        num_trees=0; comparisons=0; decreases=0;ties=0
        for seq in product(range(n),repeat=n-2):
            edges=prufer_edges(n,seq)
            h=harmonic(n,edges); p=polarization(h)
            setE=set(edges)
            for e in combinations(range(2,n),2):
                if e in setE:continue
                d=polarization(harmonic(n,edges+(e,)))-p
                if d>0:
                    raise AssertionError(('unexpected tree increase below seven',n,edges,e,d))
                comparisons+=1
                if d<0:decreases+=1
                else:ties+=1
            num_trees+=1
        print('trees n=%d labeled=%d eligible_pairs=%d decreases=%d ties=%d' %
              (n,num_trees,comparisons,decreases,ties))


def check_witnesses():
    # Six vertices, a five-cycle and a pendant follower, with strictly interior follower opinions.
    six=((0,3),(0,5),(1,2),(1,5),(2,3),(2,4))
    x=harmonic(6,six)
    xx=harmonic(6,six+((3,5),))
    assert x==(Q(0),Q(1),Q(2,3),Q(1,3),Q(2,3),Q(1,2)),x
    assert xx==(Q(0),Q(1),Q(9,13),Q(5,13),Q(9,13),Q(6,13)),xx
    assert polarization(xx)-polarization(x)==Q(43,36504)
    assert all(0<v<1 for v in x[2:])
    print('six-vertex witness: P_old=%s P_new=%s delta=%s' %
          (polarization(x),polarization(xx),polarization(xx)-polarization(x)))

    # Seven-vertex tree, leaders are relabelled so pinned at vertices 0,1.
    # Original vertex labels (0,1,2,3,4,5,6), original pinned at (2,5).
    # The permutation below turns original pinned 2->0 and 5->1.
    seven_original=((1,0),(1,2),(0,4),(0,6),(2,3),(4,5))
    perm={2:0,5:1,0:2,1:3,3:4,4:5,6:6}
    seven=tuple(tuple(sorted((perm[u],perm[v]))) for u,v in seven_original)
    e=tuple(sorted((perm[4],perm[6])))
    y=harmonic(7,seven)
    yy=harmonic(7,seven+(e,))
    # Check by reindexing to the original order for easy reproduction.
    def original_coordinates(h): return tuple(h[perm[i]] for i in range(7))
    assert original_coordinates(y)==(Q(1,2),Q(1,4),Q(0),Q(0),Q(3,4),Q(1),Q(1,2))
    assert original_coordinates(yy)==(Q(6,11),Q(3,11),Q(0),Q(0),Q(8,11),Q(1),Q(7,11))
    assert polarization(yy)-polarization(y)==Q(137,6776)
    print('seven-vertex tree witness: P_old=%s P_new=%s delta=%s' %
          (polarization(y),polarization(yy),polarization(yy)-polarization(y)))


def main():
    exhaustive_graphs(5)
    exhaustive_trees(6)
    check_witnesses()
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
