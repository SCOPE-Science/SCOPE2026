from fractions import Fraction
from itertools import product
from math import comb, factorial


def stirling2(n,k):
    if n < 0 or k < 0 or k > n:
        return 0
    dp=[0]*(k+1)
    dp[0]=1
    for _ in range(n):
        nxt=[0]*(k+1)
        for j in range(1,k+1):
            nxt[j]=dp[j-1]+j*dp[j]
        dp=nxt
    return dp[k]


def harmonic(m,q=1):
    return sum((Fraction(1,k**q) for k in range(1,m+1)),Fraction(0))


def closed_doubleton(m):
    h1=harmonic(m,1); h2=harmonic(m,2); h3=harmonic(m,3)
    mean=Fraction(1,2)*(h1*h1-2*h1+h2)
    B=h1*h1-2*h1*h2+3*h2-2*h3
    cov=-Fraction(m,2)*B
    return mean,cov,B


def transform_algebra(m):
    # Reconstruct F_{m,2}(1) and covariance from logarithmic derivatives
    # of H_{m-2}(y) at y=1/m, all as exact rational arithmetic.
    h1=harmonic(m,1); h2=harmonic(m,2); h3=harmonic(m,3)
    B=m*h1-m-1
    C=m*m*(h2-1)-2*m*h1+2*m+1
    E=2*m**3*(h3-1)-6*m*m*(h2-1)+6*m*(h1-1)-2
    A=1+2*B+Fraction(B*B+C,2)
    thetaA=B*B+2*B+(B+3)*C+Fraction(E,2)
    mean=Fraction(A,m*m)
    cov=Fraction(thetaA-(m-2)*A,m*m)
    return mean,cov


def run():
    sequence_count=0
    coefficient_checks=0
    for m in range(2,5):
        max_t=8
        for t in range(m,max_t+1):
            weighted={r:0 for r in range(2,min(4,t)+1)}
            for seq in product(range(m), repeat=t):
                if len(set(seq))==m and len(set(seq[:-1]))<m:
                    counts=[seq.count(i) for i in range(m)]
                    for r in weighted:
                        weighted[r]+=sum(c==r for c in counts)
                sequence_count+=1
            for r,got in weighted.items():
                expected=factorial(m)*comb(t-1,r)*stirling2(t-1-r,m-2)
                assert got==expected,(m,t,r,got,expected)
                coefficient_checks+=1

    algebra_checks=0
    sign_checks=0
    increment_checks=0
    prev_B=None
    for m in range(2,1001):
        mean,cov,B=closed_doubleton(m)
        mean2,cov2=transform_algebra(m)
        assert mean==mean2
        assert cov==cov2
        algebra_checks+=2
        if m==2:
            assert B==0 and cov==0
        else:
            assert B>0 and cov<0
            sign_checks+=1
        if prev_B is not None:
            n=m-1
            rhs=Fraction(2,(n+1)**3)*(n*(n+1)*harmonic(n,1)-(n+1)**2*harmonic(n,2)+2*n)
            assert B-prev_B==rhs and rhs>0
            increment_checks+=1
        prev_B=B

    print('VERIFY_OK')
    print(f'sequences_enumerated={sequence_count}')
    print(f'coefficient_checks={coefficient_checks}')
    print(f'exact_algebra_checks={algebra_checks}')
    print(f'sign_checks={sign_checks}')
    print(f'increment_checks={increment_checks}')
    print('max_exact_m=1000')

if __name__=='__main__':
    run()
