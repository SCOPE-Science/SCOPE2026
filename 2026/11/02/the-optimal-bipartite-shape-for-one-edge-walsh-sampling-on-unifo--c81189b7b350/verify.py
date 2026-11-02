"""Exact independent checks for the spanning-tree Walsh Gram spectrum.
Run with Python 3.10+; standard library only.
"""
from fractions import Fraction as Q
from itertools import combinations


def spectrum(a, b):
    assert 2 <= a <= b
    m = a*b
    n = a+b
    mu = Q(m-2*(n-1), m)
    return [(Q(0),1), (Q(1)+m*mu*mu,1),
            (Q(4*(b-1),m),a-1), (Q(4*(a-1),m),b-1),
            (Q(4*(n-3),m),(a-1)*(b-1))]


def kappa_squared(a, b):
    assert 2 <= a <= b
    m=a*b; n=a+b
    return max(Q(m+(m-2*(n-1))**2,4*(a-1)), Q(n-3,a-1))


def rank(M):
    A = [list(map(Q, row)) for row in M]
    if not A: return 0
    R,C=len(A),len(A[0]); q=0
    for j in range(C):
        pivot=next((i for i in range(q,R) if A[i][j]),None)
        if pivot is None: continue
        A[q],A[pivot]=A[pivot],A[q]
        z=A[q][j]
        A[q]=[v/z for v in A[q]]
        for i in range(R):
            if i != q and A[i][j]:
                mult=A[i][j]
                A[i]=[x-mult*y for x,y in zip(A[i],A[q])]
        q+=1
        if q==R:break
    return q


def tree_masks(a,b):
    n=a+b;m=a*b; edges=[(i,a+j) for i in range(a) for j in range(b)]
    for combo in combinations(range(m),n-1):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        good=True
        for index in combo:
            x,y=edges[index]
            u,v=root(x),root(y)
            if u==v:
                good=False;break
            parent[u]=v
        if good:
            mask=0
            for index in combo: mask|=1<<index
            yield mask


def exact_gram(a,b):
    m=a*b; masks=list(tree_masks(a,b)); count=len(masks)
    assert count == a**(b-1)*b**(a-1), (a,b,count)
    s=[0]*m; pair=[[0]*m for _ in range(m)]
    for mask in masks:
        included=[i for i in range(m) if mask>>i&1]
        for i in included:s[i]+=1
        for i in included:
            for j in included:pair[i][j]+=1
    G=[[Q(0)]*(m+1) for _ in range(m+1)]
    G[0][0]=Q(1)
    for i in range(m):
        G[0][i+1]=G[i+1][0]=Q(1)-Q(2*s[i],count)
        for j in range(m):
            G[i+1][j+1] =Q(1)-Q(2*(s[i]+s[j]),count)+Q(4*pair[i][j],count)
    return G


def predicted_gram(a,b):
    m=a*b; n=a+b;mu=Q(m-2*(n-1),m)
    p=Q(n-1,m)
    G=[[Q(0)]*(m+1) for _ in range(m+1)]
    G[0][0]=Q(1)
    for i in range(m):
        G[0][i+1]=G[i+1][0]=mu
        for j in range(m):
            if i==j: cv=p-p*p
            else:
                ti,tj=divmod(i,b); ui,uj=divmod(j,b)
                K=Q(ti==ui,b)+Q(tj==uj,a)-Q(1,m)
                cv=-K*K
            G[i+1][j+1]=mu*mu+4*cv
    return G


def matvec(G,vec):
    return [sum(a*b for a,b in zip(row,vec)) for row in G]


def eigencheck(G,v,lamb):
    assert any(v)
    assert matvec(G,v)==[lamb*x for x in v]


def verify_spectrum(a,b):
    G=exact_gram(a,b); P=predicted_gram(a,b)
    assert G==P, (a,b,'Gram mismatch')
    m=a*b;n=a+b; sp=spectrum(a,b)
    assert sum(mult for _,mult in sp)==m+1
    assert rank(G)==m
    assert sum(value*mult for value,mult in sp)==m+1
    mu=Q(m-2*(n-1),m)
    eigencheck(G,[Q(1)]+[mu]*m,Q(1)+m*mu*mu)
    eigencheck(G,[-m*mu]+[Q(1)]*m,Q(0))
    left=Q(4*(b-1),m);right=Q(4*(a-1),m);both=Q(4*(n-3),m)
    for i in range(1,a):
        v=[Q(0)]*(m+1)
        for j in range(b):v[1+i*b+j]+=1;v[1+j]-=1
        eigencheck(G,v,left)
    for j in range(1,b):
        v=[Q(0)]*(m+1)
        for i in range(a):v[1+i*b+j]+=1;v[1+i*b]-=1
        eigencheck(G,v,right)
    for i in range(1,a):
        for j in range(1,b):
            v=[Q(0)]*(m+1)
            v[1]+=1;v[1+i*b+j]+=1;v[1+j]-=1;v[1+i*b]-=1
            eigencheck(G,v,both)
    vals=[x for x,k in sp if x]
    assert kappa_squared(a,b)==max(vals)/min(vals)
    return len(list(tree_masks(a,b)))


if __name__=='__main__':
    total=0
    for a in range(2,5):
        for b in range(a,5):
            total+=verify_spectrum(a,b)
    expected={4:([2],Q(2)),5:([2],Q(5,2)),6:([3],Q(3,2)),
        7:([3],Q(2)),8:([4],Q(5,3)),9:([3,4],Q(3)),
        10:([3],Q(15,4)),11:([3],Q(5)),12:([3],Q(13,2)),
        13:([3],Q(33,4)),14:([3],Q(41,4)),15:([2],Q(12))}
    for n,(a_expected,k_expected) in expected.items():
        candidates=[(a,kappa_squared(a,n-a)) for a in range(2,n//2+1)]
        best=min(v for a,v in candidates)
        assert best==k_expected
        assert [a for a,v in candidates if v==best]==a_expected
    for n in range(16,201):
        lower=Q(4*(n-4)+(2*n-14)**2,2*(n-2))
        assert lower>n-3
        assert kappa_squared(2,n-2)==n-3
        assert kappa_squared(3,n-3)>n-3
        for a in range(4,n//2+1):
            assert kappa_squared(a,n-a)>=lower>n-3
    print('PASS: direct exact Gram enumeration, spectral identities, rank, optimization')
    print('independent labelled spanning-tree samples:',total)
    print('small-order partitions: 4..15; large-order inequalities: 16..200')
