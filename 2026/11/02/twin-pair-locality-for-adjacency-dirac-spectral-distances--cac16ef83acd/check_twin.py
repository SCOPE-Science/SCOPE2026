"""Exact-rational finite diagnostics for an adjacency-commutator twin-pair theorem.

Requires only Python 3 standard library. These finite checks are not proofs of
any statement with a universal quantifier.
"""
from fractions import Fraction as F
from random import Random


def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def test(n, gamma, w, other, f):
    assert len(w)==n-2 and len(f)==n
    D=[[F(0) for _ in range(n)] for _ in range(n)]
    D[0][1]=D[1][0]=gamma
    for j in range(2,n):
        D[0][j]=D[j][0]=D[1][j]=D[j][1]=w[j-2]
    for i in range(2,n):
        for j in range(i+1,n):
            D[i][j]=D[j][i]=other[i-2][j-2]
    C=gamma*gamma+sum((t*t for t in w),F(0))/2
    def comm(p):
        return [[D[i][j]*(p[j]-p[i]) for j in range(n)] for i in range(n)]
    p=[F(1,2),F(-1,2)]+[F(0)]*(n-2)
    K=comm(p)
    Q=matmul(transpose(K),K)
    QQ=matmul(Q,Q)
    assert all(QQ[i][j]==C*Q[i][j] for i in range(n) for j in range(n))
    assert sum((Q[i][i] for i in range(n)),F(0))==2*C
    # Testing vector e_0-e_1 has squared Euclidean length two.
    H=comm(f)
    v=[H[i][0]-H[i][1] for i in range(n)]
    assert sum((t*t for t in v),F(0))==2*(f[0]-f[1])**2*C
    return C


def main():
    rng=Random(20261027)
    checks=0
    for n in range(2,13):
        for k in range(35):
            g=F(rng.randint(-7,7), rng.randint(1,6))
            w=[F(rng.randint(-7,7),rng.randint(1,7)) for _ in range(n-2)]
            h=[[F(0) for _ in range(n-2)] for _ in range(n-2)]
            for i in range(n-2):
                for j in range(i+1,n-2):
                    h[i][j]=h[j][i]=F(rng.randint(-8,8),rng.randint(1,8))
            f=[F(rng.randint(-8,8),rng.randint(1,6)) for _ in range(n)]
            test(n,g,w,h,f)
            checks+=1
    # Two unweighted graph regimes, with all possible sizes of the twin neighborhood.
    for adjacent in (False,True):
        for n in range(3,14):
            for k in range(n-1):
                w=[F(1) if j<k else F(0) for j in range(n-2)]
                h=[[F(1) if i!=j and (i+j)%3==0 else F(0)
                    for j in range(n-2)] for i in range(n-2)]
                f=[F((i*3)%7-2,4) for i in range(n)]
                test(n,F(int(adjacent)),w,h,f)
                checks+=1
    print(f'EXACT_RATIONAL_OK cases={checks}')

if __name__=='__main__':main()
