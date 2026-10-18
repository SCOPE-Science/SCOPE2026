"""Self-contained exact checks of weighted-wheel projector identities.

This finite checker is supplementary; all-parameter statements require the proof.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, sinh, cosh, tanh


def invert(A):
    n=len(A)
    U=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next((k for k in range(col,n) if U[k][col]),None)
        assert pivot is not None
        U[col],U[pivot]=U[pivot],U[col]
        scale=U[col][col]
        U[col]=[v/scale for v in U[col]]
        for k in range(n):
            if k!=col:
                f=U[k][col]
                if f:
                    U[k]=[v-f*w for v,w in zip(U[k],U[col])]
    return [row[n:] for row in U]


def main():
    assertions=0
    ratios=(F(1,4),F(1,2),F(1),F(2),F(3),F(5))
    for m in range(3,12):
        for r in ratios:
            B=[]
            for j in range(m):
                row=[F(0)]*m
                row[j]=F(1)
                B.append(row)
            for j in range(m):
                row=[F(0)]*m
                row[j]-=r
                row[(j+1)%m]+=r
                B.append(row)
            A=[[sum(B[e][i]*B[e][j] for e in range(2*m))
                for j in range(m)] for i in range(m)]
            G=invert(A)
            P=[[sum(B[e][i]*G[i][j]*B[f][j]
                 for i in range(m) for j in range(m))
                 for f in range(2*m)] for e in range(2*m)]
            g0=G[0][0]
            ga=G[0][m//2]
            S=F(1)+2*r*(g0-ga)
            R=2*(1-g0)+2*r*(g0-ga)
            assert sum(G[0])==1; assertions+=1
            for e in range(2*m):
                assert sum(abs(v) for v in P[e])==(S if e<m else R)
                assertions+=1
                assert P[e][e]>=0; assertions+=1
            assert max(sum(abs(v) for v in P[e]) for e in range(2*m))==max(S,R)
            assertions+=1
            for e in range(2*m):
                for f in range(2*m):
                    assert P[e][f]==P[f][e]; assertions+=1
            if m<=7:
                for e in range(2*m):
                    for f in range(2*m):
                        assert sum(P[e][k]*P[k][f] for k in range(2*m))==P[e][f]
                        assertions+=1

    def norm_branches(m,x):
        u=x/m
        v=(cosh(x)-(1.0 if m%2==0 else cosh(u)))/sinh(x)
        a=v/cosh(u)
        g=tanh(u)*cosh(x)/sinh(x)
        return 1+a,2-2*g+a
    for m in (100,300,1000,3000):
        x=log(m)
        s,r=norm_branches(m,x)
        assert r>s; assertions+=1
        assert abs(m*(3-r)-2*log(m)-2)<0.5; assertions+=1
        # Narrow localization: near log(m) beats fixed unit offsets asymptotically.
        if m>=1000:
            for offset in (-1.0,1.0):
                assert r>norm_branches(m,x+offset)[1]; assertions+=1
    print('PASS: %d exact rational and asymptotic checks' % assertions)


if __name__=='__main__':
    main()
