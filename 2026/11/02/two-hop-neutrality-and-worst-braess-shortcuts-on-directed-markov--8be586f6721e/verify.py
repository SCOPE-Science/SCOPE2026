"""Exact independent coefficient checks for one-chord directed-cycle generators.

Run: python verify.py   (Python 3 standard library only)
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random


def mul(A,B):
    m=len(A);n=len(B);p=len(B[0]);return [[sum((A[i][k]*B[k][j] for k in range(n)),Q(0)) for j in range(p)] for i in range(m)]


def charcoeff(A):
    """Faddeev-LeVerrier coefficients of det(zI-A), exact rational arithmetic."""
    n=len(A);B=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    out=[Q(1)]
    for k in range(1,n+1):
        U=mul(A,B);c=-sum((U[i][i] for i in range(n)),Q(0))/k
        out.append(c)
        B=[[U[i][j]+(c if i==j else 0) for j in range(n)] for i in range(n)]
    return out


def calc(n,k,rate,t):
    """Direct generator eigen-coefficients, without the proposed formula."""
    L=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i,r in enumerate(rate):
        L[i][i]+=r;L[i][(i+1)%n]-=r
    L[0][0]+=t;L[0][k]-=t
    A=[[-v for v in row] for row in L]
    p=charcoeff(A)
    assert p[-1]==0
    return p[-2],p[-3]


def e2(arr):return sum((x*y for x,y in combinations(arr,2)),Q(0))


def closed(n,k,rate,t):
    w=[1/x for x in rate];A=w[1:k]; B=w[k:];P=Q(1)
    for r in rate:P*=r
    a1=P*(sum(w)+t/rate[0]*sum(B))
    a2=P*(e2(w)+t/rate[0]*(e2(B)+sum(A)*sum(B)))
    return a1,a2


def main():
    rng=Random(106187)
    checks=0
    for n in range(3,9):
        for k in range(1,n):
            for j in range(14):
                rate=[Q(rng.randrange(1,9),rng.randrange(1,7)) for _ in range(n)]
                if j%3==0:rate=[Q(1) for _ in range(n)]
                t=Q(rng.randrange(0,11),rng.randrange(1,8))
                a1,a2=calc(n,k,rate,t)
                b1,b2=closed(n,k,rate,t)
                assert a1==b1 and a2==b2,(n,k,rate,t,a1,a2,b1,b2)
                assert a1>0 and a2>0
                checks+=4
                if j%3==0:
                    u=Q(n*(n-1)+t*(n-k)*(n+k-3),2*(n+t*(n-k)))
                    assert a2/a1==u
                    assert (u-Q(n-1,2))==Q(t*(n-k)*(k-2),2*(n+t*(n-k)))
                    checks+=2
    for n in range(4,40):
        for k in range(1,n):
            for t in [Q(1,3),Q(2),Q(7,2),Q(100)]:
                K=Q(n*(n-1)+t*(n-k)*(n+k-3),2*(n+t*(n-k)))
                sign=(K>Q(n-1,2))-(K<Q(n-1,2))
                assert sign==(-1 if k==1 else 0 if k==2 else 1)
                checks+=1
        for t in [Q(1,2),Q(1),Q(3),Q(25)]:
            vals={y:Q(y*(n-2-y),n+t*y) for y in range(1,n-2)}
            if vals:
                winner=max(vals.values())
                for y in vals:
                    assert (vals[y]==winner)==(all(vals[y]>=v for v in vals.values()))
                    checks+=1
                for y in range(1,n-3):
                    sg=(vals[y+1]>vals[y])-(vals[y+1]<vals[y])
                    th=n*(n-2*y-3)-t*y*(y+1)
                    assert sg==(th>0)-(th<0)
                    checks+=1
    # A two-hop chord can reverse sign under rate heterogeneity.
    assert closed(4,2,[Q(1),Q(2),Q(1),Q(1)],Q(1))[1]/closed(4,2,[Q(1),Q(2),Q(1),Q(1)],Q(1))[0] < closed(4,2,[Q(1),Q(2),Q(1),Q(1)],Q(0))[1]/closed(4,2,[Q(1),Q(2),Q(1),Q(1)],Q(0))[0]
    assert closed(4,2,[Q(1),Q(1,2),Q(1),Q(1)],Q(1))[1]/closed(4,2,[Q(1),Q(1,2),Q(1),Q(1)],Q(1))[0] > closed(4,2,[Q(1),Q(1,2),Q(1),Q(1)],Q(0))[1]/closed(4,2,[Q(1),Q(1,2),Q(1),Q(1)],Q(0))[0]
    checks+=2
    print('PASS',checks,'exact rational assertions')

if __name__=='__main__':main()
