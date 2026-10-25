"""Exact-rational verification for the theta-method positivity phase diagram on equilateral biclique metric networks.
No external packages required. Examples supplement, and do not replace, the analytic argument.
"""
from fractions import Fraction as F
from itertools import product


def invert(A):
    n=len(A)
    a=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j])
        a[j],a[k]=a[k],a[j]
        z=a[j][j]
        a[j]=[v/z for v in a[j]]
        for i in range(n):
            if i!=j:
                z=a[i][j]
                if z: a[i]=[a[i][c]-z*a[j][c] for c in range(2*n)]
    return [row[n:] for row in a]


def matrices(p,q):
    n=p+q
    D=[q]*p+[p]*q
    M=[[F(D[i],3) if i==j else (F(1,6) if (i<p)!=(j<p) else F(0)) for j in range(n)] for i in range(n)]
    K=[[F(D[i]) if i==j else (F(-1) if (i<p)!=(j<p) else F(0)) for j in range(n)] for i in range(n)]
    return M,K


def full_step(p,q,th,t):
    M,K=matrices(p,q)
    n=p+q
    B=[[M[i][j]+th*t*K[i][j] for j in range(n)] for i in range(n)]
    C=[[M[i][j]-(1-th)*t*K[i][j] for j in range(n)] for i in range(n)]
    I=invert(B)
    return [[sum(I[i][k]*C[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def formula(p,q,th,t):
    n=p+q
    r3=(1-3*(1-th)*t)/(1+3*th*t)
    r12=(1-12*(1-th)*t)/(1+12*th*t)
    ans=[]
    for i in range(n):
        row=[]
        for j in range(n):
            pi=F(1,2*p) if j<p else F(1,2*q)
            v=1 if i<p else -1
            w=1 if j<p else -1
            row.append((r3 if i==j else F(0))+pi*((1-r3)+(r12-r3)*v*w))
        ans.append(row)
    return ans


def condition(p,q,th,t):
    if t==0:return True
    if th==0:return False
    if 6*th*t<1:return False
    m=max(p,q)
    f=m+(m*(15*th-3)-3)*t+18*th*(1-2*(1-th)*m)*t*t
    return f>=0


def run():
    cases=0
    for p,q in product(range(1,6),repeat=2):
        if p==1 and q==1: continue
        for th in (F(0),F(1,4),F(1,3),F(2,5),F(1,2),F(2,3),F(3,4),F(4,5),F(9,10),F(1)):
            sample={F(0),F(1,40),F(1,6),F(1,3),F(1,2),F(2,3),F(1),F(2),F(4),F(10)}
            if th:
                boundary=F(1)/(6*th)
                sample|={boundary,boundary+F(1,100),max(F(0),boundary-F(1,100))}
            for t in sorted(sample):
                A=full_step(p,q,th,t)
                B=formula(p,q,th,t)
                assert A==B, (p,q,th,t,'spectrum')
                assert all(sum(row)==1 for row in A), (p,q,th,t,'row sums')
                nonnegative=all(z>=0 for row in A for z in row)
                assert nonnegative==condition(p,q,th,t), (p,q,th,t,nonnegative,'classification')
                cases+=1
    # Explicit isolated positivity and an open nonpositive gap on both sides.
    assert condition(3,4,F(1,3),F(1,2))
    assert not condition(3,4,F(1,3),F(49,100))
    assert not condition(3,4,F(1,3),F(51,100))
    assert condition(2,3,F(1),F(10))
    print('VERIFIED exact rational spectrum, row sums, and sign classification for',cases,'matrices')


if __name__=='__main__':run()
