"""Exact-rational checks of the circum-ball formula for partial permutohedra."""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import prod


def q_sums(n,k):
    labels=range(n-k+1,n+1)
    return sum(labels),sum(j*j for j in labels)


def solve(m,n):
    assert m>=1 and n>=1
    K=min(m,n)
    candidates=[]
    for k in range(K+1):
        S,Q=q_sums(n,k)
        lo=F(n,2) if k==0 else F(n-k,2) if k<K else F(0)
        hi=None if k==0 else F(n-k+1,2)
        t=max(F(S,m),lo)
        if hi is not None: t=min(t,hi)
        val=m*t*t+Q-2*t*S
        candidates.append((val,t,k))
    val,t,k=min(candidates)
    return t,val


def farthest(m,n,t):
    K=min(m,n)
    h=[(k, m*t*t+q-2*t*s) for k in range(K+1)
       for s,q in [q_sums(n,k)]]
    best=max(v for _,v in h)
    return best,[k for k,v in h if v==best]


def check(m,n):
    t,R2=solve(m,n)
    assert F(0)<t<=F(n,2)
    vmax,ks=farthest(m,n,t)
    assert vmax==R2
    # Exact optimality: t is a convex combination of orbit barycentres
    Slo=min(q_sums(n,k)[0] for k in ks)
    Shi=max(q_sums(n,k)[0] for k in ks)
    assert Slo <= m*t <= Shi
    assert ks==list(range(min(ks),max(ks)+1)) and len(ks)<=2
    if m>n*(n+1):
        S,Q=q_sums(n,n)
        assert t==F(S,m) and R2==F(Q)-F(S*S,m) and ks==[n]
    if m==n*(n+1):
        assert t==F(1,2) and ks==[n-1,n]
    # Compare against the entire defining vertex set, not just a selected orbit.
    if m<=5 and n<=6:
        count=0
        for k in range(min(m,n)+1):
            labels=tuple(range(n-k+1,n+1))
            for slots in combinations(range(m),k):
                for entries in permutations(labels):
                    x=[0]*m
                    for i,j in zip(slots,entries):x[i]=j
                    sq=sum((F(y)-t)**2 for y in x)
                    assert sq<=R2
                    assert (sq==R2)==(k in ks)
                    count+=1
        return count
    return 0


def main():
    total=0
    for m in range(1,61):
        for n in range(1,61):
            total+=check(m,n)
    print('PASS: 3600 exact parameter pairs; examined',total,'individual vertices.')
    # Cubical limiting regime: scaled circumcenter/radius approach cube limits.
    for m in range(1,9):
        for n in (200,1000):
            t,R2=solve(m,n)
            assert abs(t/F(n)-F(1,2)) < F(4*m,n)
            assert abs(R2/F(n*n)-F(m,4)) < F(4*m*m,n)
    print('PASS: large-label cubical asymptotic bounds checked in 16 instances.')

if __name__=='__main__':main()
