"""Exact-rational checks of the one-step sign-variation phase classification.
Requires only Python's standard library. The mathematical proof covers all sizes.
"""
from fractions import Fraction as F
from itertools import combinations


def determinant(A):
    m=[row[:] for row in A]
    n=len(m)
    d=F(1)
    for j in range(n):
        pivot=next((k for k in range(j,n) if m[k][j]),None)
        if pivot is None:return F(0)
        if pivot!=j:
            m[j],m[pivot]=m[pivot],m[j]
            d=-d
        p=m[j][j]
        d*=p
        for i in range(j+1,n):
            q=m[i][j]/p
            for k in range(j+1,n):m[i][k]-=q*m[j][k]
            m[i][j]=F(0)
    return d


def inverse(A):
    n=len(A)
    m=[[A[i][j] for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next((k for k in range(j,n) if m[k][j]),None)
        assert p is not None
        m[j],m[p]=m[p],m[j]
        u=m[j][j]
        for k in range(2*n):m[j][k]/=u
        for i in range(n):
            if i!=j:
                u=m[i][j]
                for k in range(2*n):m[i][k]-=u*m[j][k]
    return [row[n:] for row in m]


def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]


def birthdeath(n, up, down):
    q=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n-1):
        q[i][i+1]=up[i];q[i+1][i]=down[i]
        q[i][i]-=up[i];q[i+1][i+1]-=down[i]
    return q


def signchanges(v):
    v=[1 if x>0 else -1 for x in v if x]
    return sum(a!=b for a,b in zip(v,v[1:]))


def check(n,up,down,theta,h):
    q=birthdeath(n,up,down)
    A=[[F(int(i==j))-theta*h*q[i][j] for j in range(n)] for i in range(n)]
    G=inverse(A)
    B=[[F(int(i==j))+(1-theta)*h*q[i][j] for j in range(n)] for i in range(n)]
    P=matmul(G,B)
    alpha=1-1/theta; beta=1/theta
    assert all(P[i][j]==alpha*F(int(i==j))+beta*G[i][j] for i in range(n) for j in range(n))
    assert all(sum(P[i],F(0))==1 for i in range(n))
    assert all(P[i][j]>0 for i in range(n) for j in range(n))
    if theta==1:
        assert all(determinant([[P[i][j] for j in cols] for i in rows])>=0
                   for k in range(1,n+1) for rows in combinations(range(n),k)
                   for cols in combinations(range(n),k))
    elif n>=3:
        for i in range(n-2):
            M=determinant([[P[r][c] for c in (i+1,i+2)] for r in (i,i+1)])
            assert M==-alpha*beta*G[i][i+2] and M<0
            r1=P[i][i+1]/P[i][i+2]
            r2=P[i+1][i+1]/P[i+1][i+2]
            r3=P[i+2][i+1]/P[i+2][i+2]
            assert max(r1,r3)<r2
            t=(max(r1,r3)+r2)/2
            v=[F(0)]*n;v[i+1]=F(1);v[i+2]=-t
            w=[sum((P[r][c]*v[c] for c in range(n)),F(0)) for r in range(n)]
            assert signchanges(v)==1 and w[i]<0<w[i+1] and w[i+2]<0
            assert signchanges(w)>=2
    elif n==2:
        assert determinant(P)>0
    return 1


def main():
    tests=0
    for n in range(2,6):
        choices=((F(1),F(1)), (F(1),F(2)),(F(2),F(3)),(F(3,2),F(1,3)))
        for off in range(4):
            up=[choices[(i+off)%4][0] for i in range(n-1)]
            down=[choices[(i+off)%4][1] for i in range(n-1)]
            for theta in (F(1),F(5,4),F(2),F(5)):
                for h in (F(1,7),F(1),F(7,3)):
                    tests+=check(n,up,down,theta,h)
    q=birthdeath(3,[F(1),F(1)],[F(1),F(1)])
    h=F(1);theta=F(2)
    G=inverse([[F(int(i==j))-theta*h*q[i][j] for j in range(3)] for i in range(3)])
    P=[[F(int(i==j))/2+G[i][j]/2 for j in range(3)] for i in range(3)]
    assert P==[[F(16,21),F(1,7),F(2,21)],[F(1,7),F(5,7),F(1,7)],[F(2,21),F(1,7),F(16,21)]]
    v=[F(0),F(1),F(-4)]
    assert [sum((P[i][j]*v[j] for j in range(3)),F(0)) for i in range(3)]==[F(-5,21),F(1,7),F(-61,21)]
    print(f'VERIFY_OK: {tests} exact-rational parameter cases, all minors when theta=1, sharp negative minors and sign witnesses for theta>1')


if __name__=='__main__':main()
