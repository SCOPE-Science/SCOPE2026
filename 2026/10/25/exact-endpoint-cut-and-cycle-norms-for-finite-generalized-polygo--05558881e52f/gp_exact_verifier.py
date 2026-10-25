"""Exact rational checks for incidence graphs of weak generalized polygons.
Run: python3 gp_exact_verifier.py (Python standard library only).
"""
from fractions import Fraction as F
from itertools import combinations


def invert(a):
    n = len(a)
    rows = [[F(z) for z in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        p = next((i for i in range(k, n) if rows[i][k]), None)
        assert p is not None, 'Grounded Laplacian singular'
        if p != k:
            rows[k], rows[p] = rows[p], rows[k]
        inv = 1 / rows[k][k]
        rows[k] = [z * inv for z in rows[k]]
        for i in range(n):
            if i != k and rows[i][k]:
                factor = rows[i][k]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[k])]
    return [row[n:] for row in rows]


def projective_plane(q):
    def canon(t):
        z = next(x for x in t if x % q)
        inverse = pow(z, -1, q)
        return tuple((a * inverse) % q for a in t)
    v = sorted({canon((x, y, z)) for x in range(q) for y in range(q) for z in range(q) if (x, y, z) != (0, 0, 0)})
    edges = [(i, len(v) + j) for i, a in enumerate(v) for j, b in enumerate(v) if sum(x*y for x, y in zip(a, b)) % q == 0]
    return 2 * len(v), edges


def perfect_matchings(xs):
    if not xs:
        yield ()
        return
    x = xs[0]
    for i in range(1,len(xs)):
        y=xs[i]
        for rest in perfect_matchings(xs[1:i] + xs[i+1:]):
            yield ((x,y),) + rest


def doily():
    pts = list(combinations(range(6),2))
    lines = list(perfect_matchings(list(range(6))))
    edges = [(i,len(pts)+j) for i,p in enumerate(pts) for j,line in enumerate(lines) if p in line]
    return len(pts)+len(lines),edges


def grid(s):
    pts = [(i,j) for i in range(s+1) for j in range(s+1)]
    ls = [('row',i) for i in range(s+1)] + [('col',j) for j in range(s+1)]
    edges = [(i,len(pts)+j) for i,(a,b) in enumerate(pts) for j,(kind,k) in enumerate(ls) if (a if kind=='row' else b)==k]
    return len(pts)+len(ls),edges


def biclique(s,t):
    return s+t+2, [(u,s+1+v) for u in range(s+1) for v in range(t+1)]


def subdivide(n, edges):
    out = []
    for i,(a,b) in enumerate(edges):
        w=n+i
        out.extend([(a,w),(w,b)])
    return n+len(edges),out


def formula(m,s,t):
    a=b=1
    r=F(0)
    for j in range(1,m+1):
        a *= s if j%2 else t
        b *= t if j%2 else s
        if j<m: r += F(1,a)+F(1,b)
        else:
            assert a==b, 'middle edge-count compatibility fails'
            r += F(1,a)
    Q=1+F(2*m-2)/(1+r)
    P=F(2*m)/(1+r)
    return Q,P,r


def graph_invariants(n, edges):
    from collections import deque
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    diameter=0
    girth=10**9
    for start in range(n):
        dist=[-1]*n;par=[-1]*n
        dist[start]=0
        todo=deque([start])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if dist[w]<0:
                    dist[w]=dist[v]+1;par[w]=v;todo.append(w)
                elif par[v]!=w:
                    girth=min(girth,dist[v]+dist[w]+1)
        assert min(dist)>=0
        diameter=max(diameter,max(dist))
    return diameter,girth


def test(title,m,s,t,n,edges):
    assert graph_invariants(n,edges)==(m,2*m), (title,graph_invariants(n,edges),m)
    g = [[0]*(n-1) for _ in range(n-1)]
    for a,b in edges:
        for u,v in ((a,b),(b,a)):
            if u<n-1:
                g[u][u]+=1
                if v<n-1:g[u][v]-=1
    inverse=invert(g)
    qval,pval,r=formula(m,s,t)
    for u,v in edges:
        potential=[(inverse[i][u] if u<n-1 else F(0))-(inverse[i][v] if v<n-1 else F(0)) for i in range(n-1)]+[F(0)]
        col=sum(abs(potential[a]-potential[b]) for a,b in edges)
        diag=potential[u]-potential[v]
        cyc=1+col-2*diag
        assert col==qval and cyc==pval, (title,(u,v),col,qval,cyc,pval)
    print(f'{title}: m={m} s={s} t={t} vertices={n} columns={len(edges)} Q={qval} P={pval} PASS')
    return len(edges)


def main():
    cases=[('biclique(2,3)',2,2,3,*biclique(2,3)),
           ('Fano plane',3,2,2,*projective_plane(2)),
           ('PG(2,3)',3,3,3,*projective_plane(3)),
           ('grid(2)',4,2,1,*grid(2)),
           ('grid(3)',4,3,1,*grid(3)),
           ('doily',4,2,2,*doily()),
           ('subdivided Fano',6,1,2,*subdivide(*projective_plane(2))),
           ('subdivided doily',8,1,2,*subdivide(*doily()))]
    cols=sum(test(*c) for c in cases)
    assert formula(3,2,2)[0]==F(53,21)
    assert formula(3,2,2)[1]==F(16,7)
    assert formula(4,2,2)[0]==F(47,15)
    assert formula(4,2,2)[1]==F(128,45)
    for m in (2,3,4,6,8):
        for q in range(2,16):
            if q>=2:
                x,y,r=formula(m,q,q)
                R=2*sum((F(1,q**j) for j in range(1,m)),F(0))+F(1,q**m)
                assert R==r
                assert x==1+F(2*m-2)/(1+R)
                assert y==F(2*m)/(1+R)
    print(f'GENERALIZED_POLYGON_EXACT_OK configurations={len(cases)} independent_full_columns={cols} equal_order_formula_cases={5*14} topology_checks={len(cases)}')

if __name__=='__main__':main()
