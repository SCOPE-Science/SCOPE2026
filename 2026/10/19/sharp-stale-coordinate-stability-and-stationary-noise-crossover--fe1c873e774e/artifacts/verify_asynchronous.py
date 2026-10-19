"""Standalone exact-arithmetic checks for delayed randomized coordinate relaxation.

Run with Python 3 (standard library). These checks complement but cannot
replace the analytic stability proof in RESULT.md.
"""
from fractions import Fraction as F
from random import Random


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def trans(A):
    return [list(x) for x in zip(*A)]


def apply_L(X, T1, T2):
    P = matmul(matmul(T1, X), trans(T1))
    R = matmul(matmul(T2, X), trans(T2))
    return [[(P[i][j] + R[i][j]) / 2 for j in range(len(X))]
            for i in range(len(X))]


def setup(beta, r, sigma_sq):
    z = F(0); o = F(1)
    T1 = [[o-beta,z,z,-beta*r], [z,o,z,z],
          [o,z,z,z], [z,o,z,z]]
    T2 = [[o,z,z,z], [z,o-beta,-beta*r,z],
          [o,z,z,z], [z,o,z,z]]
    Q = [[sigma_sq / 2 if i == j and i < 2 else z
          for j in range(4)] for i in range(4)]
    return T1,T2,Q


def solution(beta,r,sigma_sq):
    D=beta*(1-r*r)*(4-2*beta-beta*beta*r*r)
    u=2-beta*r*r; v=2-beta
    a=sigma_sq*u/D
    b=-sigma_sq*r*v/D
    c=sigma_sq*v/D
    return [[a,b,c,b],[b,a,b,c],[c,b,a,b],[b,c,b,a]],D


def tests():
    rng=Random(34016)
    count=0
    for _ in range(300):
        r=F(rng.randint(1,9),10)
        beta=F(rng.randint(1,10),10)
        sig=F(rng.randint(1,9),rng.randint(1,9))
        T1,T2,Q=setup(beta,r,sig)
        X,D=solution(beta,r,sig)
        assert D>0
        LX=apply_L(X,T1,T2)
        for i in range(4):
            for j in range(4):
                assert X[i][j]-LX[i][j]==Q[i][j], (r,beta,i,j)
                count+=1
        # The four eigenvalues of D*X/sigma_sq in the two commuting swap symmetries.
        u=2-beta*r*r;v=2-beta
        vals=[u-v,u-v,u+v-2*r*v,u+v+2*r*v]
        expected=[beta*(1-r*r), beta*(1-r*r),
                  (1-r)*(4-beta*(1-r)),(1+r)*(4-beta*(1+r))]
        assert vals==expected
        assert min(vals)>0
        count+=2
        # Fresh/current-neighbour one-step covariance balance.
        a=sig/(beta*(2-beta)*(1-r*r))
        b=-r*a
        U1=[[1-beta,-beta*r],[F(0),F(1)]]
        U2=[[F(1),F(0)],[-beta*r,1-beta]]
        C=[[a,b],[b,a]]
        temp1=matmul(matmul(U1,C),trans(U1))
        temp2=matmul(matmul(U2,C),trans(U2))
        for i in range(2):
            for j in range(2):
                q=sig/2 if i==j else F(0)
                assert C[i][j]==(temp1[i][j]+temp2[i][j])/2+q
                count+=1
        target=(2*sig*r*r*(beta-1)/
                ((2-beta)*(1-r*r)*(4-2*beta-beta*beta*r*r)))
        assert X[0][0]-a==target
        count+=1
    # Two consecutive transitions inject energy into every augmented mode.
    for beta,r in [(F(1,3),F(2,3)), (F(3,2),F(4,5))]:
        T1,T2,Q=setup(beta,r,F(1))
        LQ=apply_L(Q,T1,T2)
        B=[[Q[i][j]+LQ[i][j] for j in range(4)] for i in range(4)]
        # All principal leading minors are positive (Sylvester criterion),
        # computed by Gaussian elimination exactly.
        for n in range(1,5):
            A=[row[:n] for row in B[:n]]
            pivots=[]
            for j in range(n):
                p=A[j][j];assert p>0
                pivots.append(p)
                for i in range(j+1,n):
                    f=A[i][j]/p
                    for k in range(j+1,n):A[i][k]-=f*A[j][k]
            assert all(p>0 for p in pivots)
            count+=1
    return count

if __name__=='__main__':
    print(f'PASS: {tests()} exact-rational assertions')
