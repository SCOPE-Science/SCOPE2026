"""Independent finite checks for cycle source-failure coverage (standard library)."""
from fractions import Fraction as F
from itertools import combinations
from math import ceil


def solve(A, b):
    n=len(b)
    rows=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        t=next(i for i in range(j,n) if rows[i][j])
        rows[j],rows[t]=rows[t],rows[j]
        d=rows[j][j]
        rows[j]=[x/d for x in rows[j]]
        for i in range(n):
            if i==j:continue
            c=rows[i][j]
            if c:rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return [r[-1] for r in rows]


def hitting_floor(n, sources, lam):
    sources=set(sources)
    if not sources:return F(0)
    unpinned=[i for i in range(n) if i not in sources]
    if not unpinned:return F(1)
    loc={v:i for i,v in enumerate(unpinned)}
    A=[[F(i==j) for j in range(len(unpinned))] for i in range(len(unpinned))]
    b=[F(0) for _ in unpinned]
    for v in unpinned:
        i=loc[v]
        for w in ((v-1)%n,(v+1)%n):
            if w in sources:b[i]+=lam/2
            else:A[i][loc[w]]-=lam/2
    return min(solve(A,b))


def gap_floor(g,lam):
    if g==1:return F(1)
    A=[[F(i==j) for j in range(g-1)] for i in range(g-1)]
    b=[F(0) for _ in range(g-1)]
    for i in range(g-1):
        for j in (i-1,i+1):
            if j<0 or j>=g-1:b[i]+=lam/2
            else:A[i][j]-=lam/2
    return min(solve(A,b))


def gaps(n,S):
    S=sorted(S);k=len(S)
    return [((S[(i+1)%k]-S[i])%n or n) for i in range(k)]


def run():
    checks=0
    for lam in (F(2,5),F(3,5)):
        for n in range(3,9):
            ps=[None]+[gap_floor(g,lam) for g in range(1,n+1)]
            assert all(ps[g]>ps[g+1] for g in range(1,n))
            for B in range(1,n+1):
                good=[]
                for k in range(2,n+1):
                    for S in combinations(range(n),k):
                        direct=all(hitting_floor(n,set(S)-{v},lam)>=ps[B] for v in S)
                        a=gaps(n,S)
                        combinatorial=all(a[i-1]+a[i]<=B for i in range(k))
                        assert direct==combinatorial,(lam,n,B,S,direct,a)
                        if direct:good.append(S)
                        checks+=1
                if B==1:assert not good
                else:assert min(len(S) for S in good)==ceil(2*n/B)
    print('VERIFY_OK exact rational direct deletion checks:',checks)

if __name__=='__main__':run()
