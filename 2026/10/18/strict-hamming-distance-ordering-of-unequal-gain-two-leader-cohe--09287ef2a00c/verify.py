"""Exact arithmetic checks for two-anchor grounded hypercube Laplacians.

Uses sympy only; the infinite-dimensional (all integer d) monotonicity is proved
analytically in RESULT.md, not by finite tests.
"""
from fractions import Fraction as F
from math import comb
from sympy import Matrix, Rational, eye, zeros


def bc(d, k):
    N = 1 << d
    B, C = F(0), F(0)
    for j in range(1, d + 1):
        count = sum(comb(k, r) * comb(d-k, j-r)
                    for r in range(max(0, j-(d-k)), min(j,k)+1) if r % 2)
        B += F(count, N*j)
        C += F(count, 2*N*j*j)
    return B, C


def g0(d):
    N=1<<d
    return sum((F(comb(d,j),2*N*j) for j in range(1,d+1)),F(0))


def form(d,k,a,b):
    N=1<<d; s=a+b;p=a*b;B,C=bc(d,k)
    return 2*N*g0(d) + (N*(1-p*B*B)-2*p*C)/(s+2*p*B)


def direct(d,k,a,b):
    N=1<<d
    L=zeros(N)
    for i in range(N):
        L[i,i]=d
        for z in range(d): L[i,i^(1<<z)]-=1
    L[0,0]+=Rational(a.numerator,a.denominator)
    j=(1<<k)-1
    L[j,j]+=Rational(b.numerator,b.denominator)
    return F(str(sum(L.inv()[i,i] for i in range(N))))


def run():
    checks=0
    gains=((F(1),F(1)),(F(1,3),F(2,1)),(F(7,4),F(9,2)),(F(1,29),F(95,2)))
    for d in range(2,12):
        N=1<<d
        items=[bc(d,k) for k in range(1,d+1)]
        assert all(items[k][0]>items[k-1][0] and items[k][1]>items[k-1][1] for k in range(1,d))
        checks+=2*(d-1)
        for B,C in items:
            # Harmonic-potential max principle certificate inequality.
            assert 2*C < N*B*B
            checks+=1
        BD=items[-1][0]-items[-2][0]
        CD=items[-1][1]-items[-2][1]
        harmonic=sum((F(1,r) for r in range(1,d+1)),F(0))
        assert BD==F(1,N*d)
        assert CD==F(harmonic,2*N*d)
        checks+=2
        for a,b in gains:
            vals=[form(d,k,a,b) for k in range(1,d+1)]
            assert all(vals[k-1]>vals[k] for k in range(1,d))
            checks+=d-1
        # Equal-gain exact dimension-free sharp lower bound on one-bit regret.
        for v in (F(1,3),F(3,2),F(17,4)):
            assert form(d,d-1,v,v)-form(d,d,v,v)>F(1,2*d)
            checks+=1
    for d in range(2,5):
        for k in range(1,d+1):
            for a,b in gains:
                assert direct(d,k,a,b)==form(d,k,a,b),(d,k,a,b)
                checks+=1
    print(f'VERIFY_OK {checks} exact rational formula, monotonicity, endpoint and direct-matrix tests')

if __name__=='__main__':
    run()
