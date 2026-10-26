"""Exact finite checks for edge-covariance precision in superposed uniform triangles.

Requires Python 3 standard library only. Finite checks do not prove asymptotic claims.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb

checks = 0

def check(ok, label='check'):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def formula(n, m):
    assert n >= 5 and m >= 2
    p = F(6, n*(n-1))
    r = p / (n-2)
    u = 1-p
    v = 1-2*p+r
    w = 1-2*p
    q, b, c = u**m, v**m, w**m
    var, adj, dis = q-q*q, b-q*q, c-q*q
    E = comb(n, 2)
    l0 = q+2*(n-2)*b+comb(n-2,2)*c-E*q*q
    l1 = q+(n-4)*b-(n-3)*c
    l2 = q-2*b+c
    check(all(x>0 for x in (l0,l1,l2)), ('spectral positivity',n,m))
    P0 = F(1,E)
    P1diag = F(2,n)
    P1adj = F(n-4,n*(n-2))
    P1dis = F(-4,n*(n-2))
    P2diag = F(n-3,n-1)
    P2adj = -F(n-3,(n-1)*(n-2))
    P2dis = F(2,(n-1)*(n-2))
    invdiag=P0/l0 + P1diag/l1+P2diag/l2
    invadj=P0/l0 + P1adj/l1+P2adj/l2
    invdis=P0/l0 + P1dis/l1+P2dis/l2
    return (var,adj,dis,l0,l1,l2,invdiag,invadj,invdis)


def invert(M):
    n=len(M)
    a=[list(M[i])+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=next((r for r in range(k,n) if a[r][k]),None)
        assert pivot is not None
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k]
        t=a[k][k]
        a[k]=[v/t for v in a[k]]
        for i in range(n):
            if i!=k and a[i][k]:
                t=a[i][k]
                a[i]=[a[i][j]-t*a[k][j] for j in range(2*n)]
    return [row[n:] for row in a]


def enumerated_cov(n,m):
    edges=list(combinations(range(n),2))
    E=len(edges)
    tris=[sum(1<<edges.index(edge) for edge in combinations(t,2)) for t in combinations(range(n),3)]
    moments1=[0]*E
    moments2=[[0]*E for _ in range(E)]
    count=0
    for seq in product(tris, repeat=m):
        mask=0
        for tri in seq:mask |=tri
        selected=[i for i in range(E) if mask>>i&1]
        count+=1
        for i in selected:
            moments1[i]+=1
            for j in selected:
                moments2[i][j]+=1
    check(count == comb(n,3)**m)
    return edges,[[F(moments2[i][j],count)-F(moments1[i]*moments1[j],count*count) for j in range(E)] for i in range(E)]


def finite_enumeration(n,m):
    edges,C=enumerated_cov(n,m)
    var,adj,dis,*_,Pdiag,Padj,Pdis=formula(n,m)
    E=len(edges)
    for i in range(E):
        for j in range(E):
            overlap=len(set(edges[i])&set(edges[j]))
            expected=var if i==j else adj if overlap==1 else dis
            check(C[i][j]==expected,('cov',n,m,i,j))
    Q=invert(C)
    for i in range(E):
        for j in range(E):
            overlap=len(set(edges[i])&set(edges[j]))
            expected=Pdiag if i==j else Padj if overlap==1 else Pdis
            check(Q[i][j]==expected,('inv',n,m,i,j))


if __name__ == '__main__':
    # Independent enumeration of the graph law, not just re-use of pair formulas.
    for n,m in [(5,2),(5,3),(6,2)]:
        finite_enumeration(n,m)

    for n in range(5,18):
        for m in range(2,32):
            var,adj,dis,l0,l1,l2,di,ad,dj=formula(n,m)
            check(var>0)
            check(adj>0)
            check(dis<0)
            check(di>0)
            check(dj>0)
    # Verify that an adjacent precision entry changes sign as layers accumulate.
    for n in range(5,35):
        check(formula(n,2)[7]>0, ('two layers', n))
        check(formula(n,5*n)[7]<0, ('many layers',n))

    # The following decimal-scale comparisons are diagnostics only.
    from decimal import Decimal, localcontext
    for alpha in (F(1,2),F(1),F(3,2),F(2)):
        errors=[]
        with localcontext() as ctx:
            ctx.prec=110
            target_fraction=(4-3*alpha)/(36*alpha*alpha)
            target=Decimal(target_fraction.numerator)/Decimal(target_fraction.denominator)
            for n in (40,80,160):
                m=int(alpha*n)
                z=formula(n,m)
                val=Decimal(z[7].numerator)/Decimal(z[7].denominator)
                errors.append(abs(val-target))
            check(errors[2]<errors[1]<errors[0],('asymptotic diagnostic',alpha,errors))
    print('PASS:',checks,'exact assertions plus high-precision asymptotic diagnostics')
