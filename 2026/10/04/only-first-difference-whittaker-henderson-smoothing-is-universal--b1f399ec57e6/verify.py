from fractions import Fraction as F
from math import comb

def inv(A):
    n=len(A)
    M=[row[:] + [F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c])
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for i in range(n):
            if i==c: continue
            q=M[i][c]
            if q:
                M[i]=[M[i][j]-q*M[c][j] for j in range(2*n)]
    return [r[n:] for r in M]

def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def mv(A,x):
    return [sum((A[i][j]*x[j] for j in range(len(x))),F(0)) for i in range(len(A))]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

# p=1: exact positivity and stochasticity on representative rational instances.
for n in range(2,9):
    for lam in [F(1,7),F(1),F(5,2)]:
        A=eye(n)
        for i in range(n-1):
            A[i][i]+=lam; A[i+1][i+1]+=lam
            A[i][i+1]-=lam; A[i+1][i]-=lam
        S=inv(A)
        assert mm(A,S)==eye(n)
        assert all(v>0 for row in S for v in row)
        assert all(sum(row,F(0))==1 for row in S)

# p>=2: exact minimal-length rank-one obstruction and strict witness.
for p in range(2,11):
    d=[F(((-1)**(p-j))*comb(p,j)) for j in range(p+1)]
    C=sum((v*v for v in d),F(0))
    assert C==comb(2*p,p)
    r=[F(j+1) for j in range(p+1)]
    assert sum((d[j]*r[j] for j in range(p+1)),F(0))==0
    for lam in [F(1,11),F(1),F(7,3)]:
        alpha=lam/(1+lam*C)
        S=[[F(int(i==j))-alpha*d[i]*d[j] for j in range(p+1)] for i in range(p+1)]
        A=[[F(int(i==j))+lam*d[i]*d[j] for j in range(p+1)] for i in range(p+1)]
        assert mm(A,S)==eye(p+1)
        y=[F(0)]*p+[F(1)]
        z=mv(S,y)
        assert z[p-2]==-alpha*comb(p,2)<0
        eps=alpha*p/F(4)  # strictly below alpha*p/2
        ys=[y[j]+eps*r[j] for j in range(p+1)]
        assert all(ys[j]>0 for j in range(p+1))
        assert all(ys[j]<ys[j+1] for j in range(p))
        zs=mv(S,ys)
        assert zs[p-2] < 0

print('VERIFY_OK')
