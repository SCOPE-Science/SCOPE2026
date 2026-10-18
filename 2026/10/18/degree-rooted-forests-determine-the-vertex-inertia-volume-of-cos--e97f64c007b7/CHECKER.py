"""Exact checks of vertex-inertia identities for graph cosmological polytopes.

Run with Python 3.9 or later: python CHECKER.py
No third-party packages are required. This checks finite cases only;
the universal assertions follow from the matrix proofs in RESULT.md.
"""
from itertools import combinations, product
from fractions import Fraction
from math import prod


def determinant(mat):
    """Fraction-free Bareiss integer determinant with row pivoting."""
    n = len(mat)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in mat]
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k+1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*pivot - a[i][k]*a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator//prev
            a[i][k] = 0
        prev = pivot
    return sign*a[n-1][n-1]


def data(n, edges):
    edges = [tuple(sorted(e)) for e in edges]
    assert len(set(edges)) == len(edges)
    assert all(0 <= a < b < n for a,b in edges)
    m = len(edges)
    d = [0]*n
    a = [[0]*n for _ in range(n)]
    for u,v in edges:
        d[u] += 1
        d[v] += 1
        a[u][v] = a[v][u] = 1
    assert min(d) > 0
    q = [[(2*d[i] if i==j else 0)-a[i][j] for j in range(n)] for i in range(n)]
    return d,q


def polytope_vertices(n, edges):
    out = []
    for k,(i,j) in enumerate(edges):
        for si,sj,se in ((1,1,-1),(1,-1,1),(-1,1,1)):
            v = [0]*(n+len(edges))
            v[i],v[j],v[n+k] = si,sj,se
            out.append(v)
    return out


def vertex_inertia(n,edges):
    """Return exact pseudo-determinant of vertex covariance via principal minor."""
    vertices = polytope_vertices(n,edges)
    N = n+len(edges)
    K = len(vertices)
    r = [sum(v[i] for v in vertices) for i in range(N)]
    M = [[sum(v[i]*v[j] for v in vertices) for j in range(N)] for i in range(N)]
    T = [[K*M[i][j]-r[i]*r[j] for j in range(N)] for i in range(N)]
    assert all(sum(row)==0 for row in T)
    return Fraction(N*determinant([row[:-1] for row in T[:-1]]),K**(2*(N-1)))


def predicted(n,edges):
    m = len(edges)
    _,q = data(n,edges)
    return Fraction(n+m,m**(n+m))*Fraction(4,9)**n*determinant(q)


def forest_sum(n,edges):
    """Count degree-weighted rooted spanning forests without matrix determinants."""
    d,_ = data(n,edges)
    ans = 0
    for mask in range(1<<len(edges)):
        parent = list(range(n))
        def root(a):
            while a != parent[a]:
                a=parent[a]
            return a
        okay=True
        for k,(u,v) in enumerate(edges):
            if mask&(1<<k):
                ru,rv = root(u),root(v)
                if ru==rv:
                    okay=False
                    break
                parent[ru]=rv
        if not okay:
            continue
        totals={}
        for v in range(n):
            r=root(v)
            totals[r]=totals.get(r,0)+d[v]
        ans+=prod(totals.values())
    return ans


def prufer_tree(n,seq):
    degree=[1]*n
    for x in seq: degree[x]+=1
    edges=[]
    for x in seq:
        leaf=next(i for i in range(n) if degree[i]==1)
        edges.append(tuple(sorted((leaf,x))))
        degree[leaf]-=1
        degree[x]-=1
    leaves=[i for i in range(n) if degree[i]==1]
    edges.append(tuple(leaves))
    return tuple(sorted(edges))


def main():
    tested=0
    for n in range(2,6):
        for code in product(range(n),repeat=n-2):
            edges=prufer_tree(n,code)
            d,q=data(n,edges)
            assert determinant(q)==forest_sum(n,edges)
            assert vertex_inertia(n,edges)==predicted(n,edges)
            tested+=1
    for n in range(3,5):
        poss=list(combinations(range(n),2))
        for mask in range(1<<len(poss)):
            edges=[e for k,e in enumerate(poss) if mask&(1<<k)]
            if not edges or len(edges)<n-1: continue
            if any(all(v not in e for e in edges) for v in range(n)): continue
            reachable={0}
            while True:
                nxt=reachable|{v for u,v in edges if u in reachable}|{u for u,v in edges if v in reachable}
                if nxt==reachable: break
                reachable=nxt
            if len(reachable)<n:continue
            d,q=data(n,edges)
            assert determinant(q)==forest_sum(n,edges)
            assert vertex_inertia(n,edges)==predicted(n,edges)
            tested+=1
    for n in range(2,14):
        star=[(0,i) for i in range(1,n)]
        path=[(i,i+1) for i in range(n-1)]
        a=determinant(data(n,star)[1]); b=determinant(data(n,path)[1])
        assert a == 3*(n-1)*2**(n-2)
        if n==2: assert b==3
        elif n==3: assert b==12
        else:
            prev,cur=3,12
            for k in range(4,n+1):
                prev,cur=cur,4*cur-prev
            assert b==cur
    treeA=[(1,0),(1,2),(1,3),(0,4),(4,5)]
    treeB=[(1,0),(1,2),(0,3),(0,5),(3,4)]
    assert sorted(data(6,treeA)[0])==sorted(data(6,treeB)[0])
    assert (determinant(data(6,treeA)[1]), determinant(data(6,treeB)[1]))==(492,483)
    assert vertex_inertia(6,treeA)==predicted(6,treeA)
    assert vertex_inertia(6,treeB)==predicted(6,treeB)
    print('PASS: all',tested,'small connected graphs and labeled trees, determinants, forest sums and pseudodeterminants')
    print('PASS: star/path determinant recurrences n=2..13; degree-sequence twins (492,483)')

if __name__=='__main__':
    main()
