#!/usr/bin/env python3
"""Exact-rational test of the single-chord path Kirchhoff-index theorem.

Uses Fraction-valued Gauss-Jordan inversion of a grounded Laplacian,
independent of the pseudoinverse/ramp derivation in the proof.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F


def inv(a):
    n=len(a)
    aug=[[F(a[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        ip=next(i for i in range(col,n) if aug[i][col])
        aug[col],aug[ip]=aug[ip],aug[col]
        z=aug[col][col]
        aug[col]=[v/z for v in aug[col]]
        for i in range(n):
            if i != col and aug[i][col]:
                z=aug[i][col]
                aug[i]=[v-z*w for v,w in zip(aug[i],aug[col])]
    return [row[n:] for row in aug]


def kirchhoff(n,i,j,t):
    g=[[F(0)]*(n-1) for _ in range(n-1)]
    for u,v,w in [(k,k+1,F(1)) for k in range(n-1)]+[(i-1,j-1,t)]:
        if u<n-1:g[u][u]+=w
        if v<n-1:g[v][v]+=w
        if u<n-1 and v<n-1:
            g[u][v]-=w;g[v][u]-=w
    a=inv(g)
    return n*sum(a[k][k] for k in range(n-1))-sum(map(sum,a))


def c(n,d):return F(d*(3*n*d-2*d*d+2),12)

def model(n,i,j,t):
    d=j-i
    l=i-1;r=n-j
    s=c(n,d)-F(d*d*(l-r)**2,4*n)
    k0=F(n*(n*n-1),6)
    return k0-F(n)*t*s/(1+t*d)


def phase(n,t):
    ds=range(n-1,1,-2)
    vals={d:c(n,d)/(d+1/t) for d in ds}
    mx=max(vals.values())
    return {(F(n-d+1,2), F(n+d+1,2)) for d,v in vals.items() if v==mx}


def crossing(n,d):
    assert d>=4 and d<=n-1 and (n-d-1)%2==0
    assert 4*d>3*n+4
    return F(6*(d-1)*(n+1-d),d*(d-2)*(4*d-3*n-4))


def main():
    tested=0
    for n in range(4,13):
        times=[F(1,20),F(1,2),F(1),F(5),F(100)]
        for d in range(n-1,3,-2):
            if 4*d>3*n+4:
                th=crossing(n,d)
                times += [th*F(999,1000),th,th*F(1001,1000)]
        for t in sorted(set(times)):
            allk={(i,j):kirchhoff(n,i,j,t) for i in range(1,n) for j in range(i+2,n+1)}
            for (i,j),actual in allk.items():
                assert actual==model(n,i,j,t),(n,i,j,t,actual,model(n,i,j,t))
            best=min(allk.values())
            actual_best={pair for pair,v in allk.items() if v==best}
            pred=phase(n,t)
            assert pred==actual_best,(n,t,pred,actual_best)
            tested+=len(allk)
    print('VERIFY_OK exact_laplacian_chords=',tested)

if __name__=='__main__':main()
