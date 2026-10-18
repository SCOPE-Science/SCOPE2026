"""Exact moment-lift and stability-boundary checks for the exchangeable Ito LV linearization.

Run: python verify.py
Uses Python standard library only. Computation illustrates the theorem; the proof is in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt


def model(n, alpha, beta, c, D, H):
    assert n >= 2 and alpha > 0 and beta > c >= 0 and D >= 0 and H >= 0
    r = alpha / (beta + (n - 1)*c)
    delta = D + (n-1)*H
    B = beta + (n - 2)*c
    mat = ((2*r*(-beta+r*delta), -2*r*c*(n-1)),
           (-2*r*c, -2*r*B))
    condition = alpha*delta*B < (beta-c)*(beta+(n-1)*c)**2
    return mat, condition, r, delta


def full_lift_derivative(K, n, alpha, beta, c, D, H):
    r = alpha / (beta+(n-1)*c)
    A = [[-r*(beta if i==j else c) for j in range(n)] for i in range(n)]
    return [[sum(A[i][k]*K[k][j] + K[i][k]*A[j][k] for k in range(n))
             + (2*r*r*(D*K[i][i] + H*sum(K[k][k] for k in range(n) if k!=i))
                if i==j else 0)
             for j in range(n)] for i in range(n)]


def assert_exchangeable_reduction():
    cases=0
    for n in range(2,8):
        for seed in range(1,15):
            alpha=Q(seed+2,7)
            beta=Q(seed+8,4)
            c=Q(seed%4,5)
            D=Q(seed%7,3)
            H=Q(seed%5,6)
            u=Q(seed+3,7)
            v=Q((seed%3)-1,13)
            K=[[u if i==j else v for j in range(n)] for i in range(n)]
            dK=full_lift_derivative(K,n,alpha,beta,c,D,H)
            mat,*_=model(n,alpha,beta,c,D,H)
            du=mat[0][0]*u+mat[0][1]*v
            dv=mat[1][0]*u+mat[1][1]*v
            assert all(dK[i][j]==(du if i==j else dv)
                       for i in range(n) for j in range(n))
            cases+=1
    return cases


def eigenvalues(matrix):
    (a,b),(c,d)=matrix
    discriminant=(a-d)**2+4*b*c
    assert discriminant>=0
    return ((a+d-sqrt(float(discriminant)))/2,
            (a+d+sqrt(float(discriminant)))/2)


def test_stability_equivalence():
    cases=0
    for n in range(2,10):
        for seed in range(1,80):
            alpha=Q(seed+1,7)
            beta=Q(seed%8+10,4)
            c=Q(seed%4,5)
            D=Q(seed%9,3)
            H=Q(seed%11,6)
            mat,stable,_,_=model(n,alpha,beta,c,D,H)
            # We avoid unresolved numerical boundaries: choose nondegenerate grid values.
            determinant=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
            trace=mat[0][0]+mat[1][1]
            assert stable == (determinant>0 and trace<0)
            lo,hi=eigenvalues(mat)
            if determinant!=0:
                assert (hi<0)==stable
            cases+=1
    return cases


def exact_counterexample():
    # Source parameters with all interspecies-noise variance (C=gamma=1, Q=4).
    n=2; alpha=Q(1); beta=Q(2); c=Q(1); D=Q(0); H=Q(4)
    mat,stable,r,delta=model(n,alpha,beta,c,D,H)
    assert mat==((Q(-4,9),Q(-2,3)),(Q(-2,3),Q(-4,3)))
    assert stable
    assert alpha*delta/(beta+(n-1)*c) > beta-c  # Source criterion says unstable.
    assert mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]==Q(4,27)
    assert mat[0][0]+mat[1][1]==Q(-16,9)
    eigen=eigenvalues(mat)
    assert abs(eigen[1]-float((-8+2*sqrt(13))/9))<1e-14
    # With the same parameters, exact real critical species value is 1+2sqrt(3)/3.
    # The published (unsharp) ceiling is 5/3; 2 species are stable, 3 unstable.
    assert Q(5,3)<2 and 2<1+2*sqrt(3)/3<3
    mat3,stable3,_,_=model(3,alpha,beta,c,D,H)
    assert not stable3
    return eigen

if __name__=='__main__':
    n1=assert_exchangeable_reduction()
    n2=test_stability_equivalence()
    eigen=exact_counterexample()
    print(f'PASS {n1} exact full-lift/reduced-moment identities')
    print(f'PASS {n2} exact trace/determinant stability comparisons')
    print('PASS rational two-species counterexample; eigenvalues:',tuple(round(v,12) for v in eigen))
