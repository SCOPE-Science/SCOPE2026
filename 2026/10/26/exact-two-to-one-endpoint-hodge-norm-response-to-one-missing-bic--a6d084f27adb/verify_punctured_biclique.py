"""Exact rational validation of cut and cycle projections on K_{m,n} minus one edge.

This checks finite cases only; the accompanying mathematical proof covers all m,n >= 2.
Uses only Python standard library.
"""
from fractions import Fraction as F


def inverse(A):
    n = len(A)
    aug = [[F(x) for x in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(A)]
    for j in range(n):
        p = next(i for i in range(j,n) if aug[i][j])
        aug[j],aug[p] = aug[p],aug[j]
        q=aug[j][j]
        aug[j] = [v/q for v in aug[j]]
        for i in range(n):
            if i!=j:
                q=aug[i][j]
                if q:
                    aug[i] = [aug[i][k]-q*aug[j][k] for k in range(2*n)]
    return [row[n:] for row in aug]


def direct(m,n):
    V=m+n
    edges=[(a,m+b) for a in range(m) for b in range(n) if (a,b)!=(0,0)]
    L=[[0]*V for _ in range(V)]
    for x,y in edges:
        L[x][x]+=1; L[y][y]+=1
        L[x][y]-=1; L[y][x]-=1
    # Ground vertex V-1 and solve L phi = b_e, phi_ground=0.
    U=inverse([row[:V-1] for row in L[:V-1]])
    Q=[]
    for x,y in edges:
        b=[F(int(i==x)-int(i==y)) for i in range(V-1)]
        phi=[sum(U[i][j]*b[j] for j in range(V-1)) for i in range(V-1)]+[F(0)]
        Q.append([phi[a]-phi[b] for a,b in edges])
    P=[]
    for j,col in enumerate(Q):
        P.append([F(int(i==j))-v for i,v in enumerate(col)])
    normq=max(sum(abs(v) for v in col) for col in Q)
    normp=max(sum(abs(v) for v in col) for col in P)
    t=(m-1)*(n-1)
    targetq=F(3)-F(2,m)-F(2,n)+F(2,m*n)-F(2,m*n*t)
    targetp=F(4*t,m*n)-F(4,m*n*t)
    assert normq==targetq,(m,n,normq,targetq)
    assert normp==targetp,(m,n,normp,targetp)
    # Both non-square edge classes have strictly smaller column sums if m,n>=3.
    for j,(a,b) in enumerate(edges):
        csq=sum(abs(v) for v in Q[j]); csp=sum(abs(v) for v in P[j])
        if a!=0 and b!=m:
            assert csq==targetq and csp==targetp
        elif m>=3 and n>=3:
            assert csq<targetq and csp<targetp
    return len(edges)


if __name__=='__main__':
    total=0; cases=0
    for m in range(2,8):
        for n in range(2,8):
            total+=direct(m,n); cases+=1
    print('PASS',cases,'parameter pairs,',total,'exact rational projector columns; both norms and extremal edge orbits')
