"""Reproduce rational Green-matrix and complex deficit checks (supplementary finite tests)."""
from fractions import Fraction as F
from math import comb, sqrt, sin, cos


def invert(M):
    n=len(M)
    a=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
    for k in range(n):
        z=next(i for i in range(k,n) if a[i][k]);a[k],a[z]=a[z],a[k]
        p=a[k][k];a[k]=[v/p for v in a[k]]
        for i in range(n):
            if i!=k:
                t=a[i][k];a[i]=[u-t*v for u,v in zip(a[i],a[k])]
    return [row[n:] for row in a]


def gram(alpha,d):
    D=[[F(0) for _ in range(d)] for _ in range(d+alpha)]
    for j in range(d):
        for k in range(alpha+1): D[j+k][j]=F((-1)**k*comb(alpha,k))
    Q=[[sum(D[k][i]*D[k][j] for k in range(d+alpha)) for j in range(d)] for i in range(d)]
    return Q,D


def dot(a,b): return sum(x.conjugate()*y for x,y in zip(a,b))

def check():
    count=0
    for alpha in range(1,6):
        for d in range(2,10):
            Q,D=gram(alpha,d);G=invert(Q)
            assert all(G[i][j]>0 for i in range(d) for j in range(d))
            C2=sum(sum(row) for row in G)
            assert C2==F(comb(d+2*alpha,2*alpha+1),comb(2*alpha,alpha))
            L=[sum(row) for row in G]
            for k in range(16):
                a=[(0.25+abs(sin((j+1)*(k+1)*1.7)))*complex(cos((j+1)*k*.37),sin((j+1)*k*.37)) for j in range(d)]
                s=[v/abs(v) for v in a]
                u=sum(abs(v) for v in a)
                E=sum(abs(sum(complex(D[r][j])*a[j] for j in range(d)))**2 for r in range(d+alpha))
                v=[sum(float(G[i][j])*s[j] for j in range(d)) for i in range(d)]
                q=dot(s,v).real
                graph=sum(float(G[i][j])*abs(s[i]-s[j])**2 for i in range(d) for j in range(i+1,d))
                h=[a[j]-u*v[j]/q for j in range(d)]
                amp=q*sum(abs(sum(complex(D[r][j])*h[j] for j in range(d)))**2 for r in range(d+alpha))
                deficit=float(C2)*E-u*u
                assert abs(deficit-graph*E-amp)<1e-7*(1+abs(deficit))
                assert deficit>=-1e-8
                count+=1
    print('PASS',count,'rational Green and complex-deficit cases')

if __name__=='__main__':check()
