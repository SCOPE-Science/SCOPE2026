"""Finite checks for coordinate-symmetric fixed Rips spaces of binary cubes.

All computations reconstruct the underlying finite orbit graph.  The proof
for unrestricted dimensions is the neighborhood-fold argument in RESULT.md.
"""
from collections import defaultdict


def orbit_distances(n):
    by_weight = defaultdict(list)
    for x in range(1 << n):
        by_weight[x.bit_count()].append(x)
    maximum = {}
    for a in range(n + 1):
        for b in range(n + 1):
            maximum[a, b] = max((x ^ y).bit_count()
                                for x in by_weight[a] for y in by_weight[b])
            assert maximum[a, b] == min(a + b, 2*n - a - b)
    return maximum


def theoretical_edges(m, k):
    return {frozenset((i, m+j)) for i in range(m) for j in range(m)
            if abs(i-j) < k}


def folded_graph_test(m, k):
    active = set(range(2*m))
    edges = theoretical_edges(m, k)
    def neigh(v):
        return {next(iter(e - {v})) for e in edges if v in e}
    def remove_dominated(anchor, gone):
        assert anchor in active and gone in active and anchor != gone
        assert frozenset((anchor,gone)) not in edges
        assert neigh(anchor) <= neigh(gone), (m,k,anchor,gone)
        active.remove(gone)
        edges.difference_update({e for e in edges if gone in e})
    for a in range(0,m,k):
        for i in range(a+1,min(a+k,m)):
            remove_dominated(a,i)
        for i in range(a+1,min(a+k,m)):
            remove_dominated(m+a,m+i)
    anchors = set(range(0,m,k))
    assert active == anchors | {m+a for a in anchors}
    assert edges == {frozenset((a,m+a)) for a in anchors}
    return len(anchors)


def reduced_betti(m,k):
    size=2*m
    faces={-1:[0]}
    for s in range(1,1<<size):
        left=[i for i in range(m) if (s>>i)&1]
        right=[j for j in range(m) if (s>>(m+j))&1]
        if all(abs(i-j)>=k for i in left for j in right):
            faces.setdefault(s.bit_count()-1,[]).append(s)
    ranks={}
    for d in sorted((d for d in faces if d>=0),reverse=True):
        rows={f:i for i,f in enumerate(faces[d-1])}
        pivot={}
        for s in faces[d]:
            col=1 if d==0 else 0
            if d:
                t=s
                while t:
                    bit=t&-t;t-=bit
                    col ^= 1<<rows[s^bit]
            while col:
                leading=col.bit_length()-1
                if leading not in pivot:
                    pivot[leading]=col
                    break
                col ^= pivot[leading]
        ranks[d]=len(pivot)
    result={d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0)
            for d,fs in faces.items() if d>=0}
    return {d:b for d,b in result.items() if b}


def all_checks():
    orbit_cases=0; folds=0; homologies=0; persistence=0
    for n in range(1,11):
        dist=orbit_distances(n)
        for r in range(n):
            p=r//2; m=p+1; k=n-r
            eligible=[w for w in range(n+1) if dist[w,w] <= r]
            assert eligible == list(range(m)) + list(range(n-m+1,n+1))
            for ia,a in enumerate(eligible):
                for ib,b in enumerate(eligible):
                    model = (ia<m and ib<m) or (ia>=m and ib>=m) or (abs((ia%m)-(ib%m))>=k)
                    # note that weight-orbit ordering is L_0,...,L_{m-1},H_{m-1},...,H_0
                    wa=ia if ia<m else n-eligible[ia]
                    wb=ib if ib<m else n-eligible[ib]
                    if (ia<m)!=(ib<m):
                        model=abs(wa-wb)>=k
                    assert (dist[a,b]<=r)==model,(n,r,a,b,ia,ib)
            orbit_cases+=1
    for m in range(1,26):
        for k in range(1,m+4):
            assert folded_graph_test(m,k)==(m-1)//k+1
            folds+=1
    for n in range(1,15):
        for r in range(n):
            m=r//2+1;k=n-r;d=(m-1)//k
            assert reduced_betti(m,k)=={d:1}, (n,r)
            homologies+=1
    for n in range(2,101):
        for q in range(0,n+5):
            birth=(2*q*n+2*q)//(2*q+1)
            for r in range(n):
                assert (((r//2)//(n-r))>=q) == (r>=birth)
        degrees=[(r//2)//(n-r) for r in range(n)]
        assert degrees==sorted(degrees)
        for r in range(n-1):
            m=r//2+1;k=n-r
            m2=(r+1)//2+1;k2=n-r-1
            old=list(range(0,m,k))
            image=[i//k2 for i in old]
            assert image==sorted(set(image))
            if degrees[r]==degrees[r+1]:
                assert image==list(range(0,(m2-1)//k2+1))
            persistence+=1
    print(f'PASS: {orbit_cases} raw Hamming-orbit scale comparisons (n <= 10)')
    print(f'PASS: {folds} independently checked dominated-vertex deletion sequences')
    print(f'PASS: {homologies} reduced mod-two chain-homology computations (n <= 14)')
    print(f'PASS: {persistence} transition/core-map checks (n <= 100)')
    print('PASS: all barcode-threshold comparisons (n <= 100)')
    print('Example: n=30 gives reduced H_1 interval [20,24).')
    print('Finite checks do not replace the all-parameter proof.')

if __name__=='__main__':
    all_checks()
