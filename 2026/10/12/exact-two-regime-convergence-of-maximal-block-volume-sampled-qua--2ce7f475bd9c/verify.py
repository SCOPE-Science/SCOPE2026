"""Exact checks for maximal-block volume-sampled quadratic coordinate descent.

Run with Python 3 standard library: python verify.py
All identities are checked in rational arithmetic. Spectral/asymptotic
statements follow from the accompanying analytical proof, not finite tests.
"""
from fractions import Fraction as F
from itertools import product


def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def inverse(A):
    n=len(A)
    W=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        t=next(i for i in range(j,n) if W[i][j]); W[j],W[t]=W[t],W[j]
        d=W[j][j];W[j]=[v/d for v in W[j]]
        for i in range(n):
            if i!=j:
                d=W[i][j]
                W[i]=[W[i][k]-d*W[j][k] for k in range(2*n)]
    return [row[n:] for row in W]


def check(G,x0,maxk=4):
    n=len(G)
    H=inverse(G)
    assert mm(H,G)==[[F(i==j) for j in range(n)] for i in range(n)]
    w=[G[i][i] for i in range(n)];total=sum(w)
    p=[z/total for z in w]
    V=[[G[j][i]/w[i] for i in range(n)] for j in range(n)]
    # Checking that the complement-block minimizer indeed solves selected stationarity equations.
    for i in range(n):
        assert V[i][i]==1
        Hv=[sum(H[j][k]*V[k][i] for k in range(n)) for j in range(n)]
        assert all(Hv[j]==0 for j in range(n) if j!=i)
    Q=[[p[j]*V[j][i]**2 for i in range(n)] for j in range(n)]
    # The symmetric similarity is checked squared to avoid irrational square roots:
    # Q[j,i]*w[i]^(3/2)/w[j]^(3/2) = G[j,i]^2/(tr(G)*sqrt(w[i]*w[j])).
    for j in range(n):
        for i in range(n):
            assert Q[j][i]*w[i]**2*F(1,w[j])== G[j][i]**2/total
            assert Q[j][i]*w[i]**3 == Q[i][j]*w[j]**3
    m=[p[i]*x0[i]**2 for i in range(n)]
    exact_checks=0
    for k in range(1,maxk+1):
        direct=[F(0) for _ in range(n)]
        for seq in product(range(n),repeat=k):
            prob=F(1)
            for i in seq: prob*=p[i]
            x=list(x0)
            for i in seq:
                x=[x[i]*V[j][i] for j in range(n)]
            direct[seq[-1]]+=prob*x[seq[-1]]**2
        assert direct==m,(k,direct,m)
        expected=sum(m[i]*sum(V[j][i]**2 for j in range(n)) for i in range(n))
        brute=F(0)
        for seq in product(range(n),repeat=k):
            prob=F(1)
            for i in seq:prob*=p[i]
            x=list(x0)
            for i in seq:x=[x[i]*V[j][i] for j in range(n)]
            brute+=prob*sum(xi*xi for xi in x)
        assert expected==brute,(k,expected,brute)
        exact_checks+=n**k+1
        m=[sum(Q[j][i]*m[i] for i in range(n)) for j in range(n)]
    return exact_checks


def run():
    matrices=[
        [[F(2),F(1,3)],[F(1,3),F(3)]],
        [[F(2),F(0),F(1)],[F(0),F(3),F(1)],[F(1),F(1),F(2)]],
        [[F(3),F(1),F(1,2)],[F(1),F(4),F(1)],[F(1,2),F(1),F(5)]],
        [[F(2),F(1,2),F(0),F(1,4)],
         [F(1,2),F(3),F(1,3),F(1,4)],
         [F(0),F(1,3),F(4),F(1,4)],
         [F(1,4),F(1,4),F(1,4),F(5)]],
    ]
    total=0
    for t,G in enumerate(matrices):
        n=len(G)
        # Cholesky-free Sylvester test of positive-definiteness using positive Gaussian pivots.
        A=[row[:] for row in G]
        for k in range(n):
            assert A[k][k]>0
            for i in range(k+1,n):
                for j in range(k+1,n):
                    A[i][j]-=A[i][k]*A[k][j]/A[k][k]
        total+=check(G,[F(i+1) for i in range(n)],5 if n<4 else 4)
    G=matrices[1]
    x0=[F(1),F(2),F(3)]
    w=[G[i][i] for i in range(3)]
    x1=[x0[0]*G[i][0]/w[0] for i in range(3)]
    x2=[x1[1]*G[i][1]/w[1] for i in range(3)]
    assert x2==[F(0)]*3
    # Two-dimensional symmetric illustration: exact mean-square factor versus
    # the geometric (almost-sure squared-norm) factor.
    for c in [F(1,4),F(1,2),F(3,4)]:
        R=(1+c*c)/2
        assert R>c and R-c==(1-c)**2/2
    print('PASS:',total,'rational path/norm equalities; inverse-zero absorption; 2D rate separation')

if __name__=='__main__':
    run()
