"""Exact-rational spectral and positivity replay for matched bipartite Gauss diffusion."""
from fractions import Fraction as F
from math import sqrt

def mm(A,B):
    m=len(A); t=len(B); k=len(B[0]);
    return [[sum(A[i][p]*B[p][j] for p in range(t)) for j in range(k)] for i in range(m)]

def inv(A):
    n=len(A); U=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next(p for p in range(col,n) if U[p][col]); U[col],U[pivot]=U[pivot],U[col]
        z=U[col][col]; U[col]=[v/z for v in U[col]]
        for r in range(n):
            if r!=col:
                z=U[r][col]
                if z:U[r]=[U[r][j]-z*U[col][j] for j in range(2*n)]
    return [row[n:] for row in U]

def lap(n,a,b):
    z=2*n; L=[[F(0) for _ in range(z)] for _ in range(z)]
    for i in range(n):
        for j in range(n):
            w=b if i==j else a
            L[i][i]+=w;L[n+j][n+j]+=w;L[i][n+j]-=w;L[n+j][i]-=w
    return L

def mats(n,a,b,h):
    L=lap(n,a,b);L2=mm(L,L);m=2*n
    D=[[12*F(int(i==j))+6*h*L[i][j]+h*h*L2[i][j] for j in range(m)] for i in range(m)]
    N=[[12*F(int(i==j))-6*h*L[i][j]+h*h*L2[i][j] for j in range(m)] for i in range(m)]
    return mm(N,inv(D))

def Qx(n,r,t):
    return 144*(n*r-n+2)+72*(1+r)*(n*r-n+2)*t+12*(n*r**3-n+2+4*r+4*r*r)*t*t+6*r*(1+r)*(n*(1-r)+2*r)*t**3+r*(1+r)*((n-1)*(1-r*r)+r)*t**4

def Qy(r,t):
    return 288+144*(1+r)*t+24*(1+2*r+2*r*r)*t*t+12*r*r*(1+r)*t**3+r*(1+r)*(r*r+r-1)*t**4

def Qsame(r,t):
    return 144*r*t+72*r*(1+r)*t*t+12*r*(1+r)**2*t**3+r*(1+r)*(1+r+r*r)*t**4

def ff(x):return 12*x/(x*x+6*x+12)

def run():
    checks=0
    for n in range(3,7):
        for a in [F(1),F(3,2)]:
            for b in [F(0),F(1,8),F(1,2),F(1),F(5,4),F(3,2),F(3)]:
                for h in [F(0),F(1,8),F(1,2),F(1),F(4),F(20)]:
                    T=mats(n,a,b,h)
                    u=n*a;v=(n-2)*a+2*b;w=u+v
                    A=ff(u*h);B=ff(v*h);C=ff(w*h)
                    types={'same':(A+B-C)/(2*n),'matched':((n-1)*(B-A)+C)/(2*n),'unmatched':(A-B+C)/(2*n)}
                    for i in range(2*n):
                        assert sum(T[i])==1
                        assert T[i][i]>0
                        for j in range(2*n):
                            assert T[i][j]==T[j][i]
                            if i==j: continue
                            typ=('same' if i//n==j//n else ('matched' if i%n==j%n else 'unmatched'))
                            assert T[i][j]==types[typ],(n,a,b,h,i,j,typ,T[i][j],types[typ])
                            checks+=1
                    if h:
                        r=v/u;t=h*u
                        Den=(t*t+6*t+12)*((r*t)**2+6*r*t+12)*(((1+r)*t)**2+6*(1+r)*t+12)
                        assert types['matched']==6*h*u*Qx(n,r,t)/(n*Den)
                        assert types['unmatched']==6*h*u*Qy(r,t)/(n*Den)
                        assert types['same']==6*h*u*Qsame(r,t)/(n*Den)
                        checks+=3
    print('VERIFY_OK',checks,'exact rational assertions')
if __name__=='__main__':run()
