#!/usr/bin/env python3
"""Standalone exact finite checks of the isolated-edge/triangle covariance identities.

No third-party dependencies. This checks finite samples only; the stated all-n
result is established by the combinatorial proof in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def fall(n,k):
    ans=1
    for i in range(k): ans*=n-i
    return ans


def closed(n,m):
    N=comb(n,2)
    Q=comb(n-2,2)
    if not 3 <= m <= Q+1: return Fraction(0)
    EJ=Fraction(N*choose(Q,m-1),choose(N,m))
    a=Fraction(comb(n-2,3),fall(Q,3))
    b=Fraction(comb(n,3),fall(N,3))
    return EJ*(m-1)*(m-2)*(a*(m-3)-b*m)


def exhaustive(n):
    edges=list(combinations(range(n),2))
    N=len(edges)
    emap={e:i for i,e in enumerate(edges)}
    mask_inc=[]
    for u,v in edges:
        mask=sum(1<<k for k,(a,b) in enumerate(edges) if (a in (u,v) or b in (u,v)))
        mask_inc.append(mask)
    tri_masks=[]
    for a,b,c in combinations(range(n),3):
        tri_masks.append(sum(1<<emap[tuple(sorted(e))] for e in ((a,b),(a,c),(b,c))))
    s=defaultdict(lambda:[0,0,0,0])
    for g in range(1<<N):
        m=g.bit_count()
        j=sum(1 for i,inc in enumerate(mask_inc) if (g & inc)==(1<<i))
        t=sum(1 for tri in tri_masks if (g&tri)==tri)
        r=s[m];r[0]+=1;r[1]+=j;r[2]+=t;r[3]+=j*t
    count=0
    for m,(size,sumj,sumt,sumjt) in s.items():
        cov=Fraction(sumjt,size)-Fraction(sumj*sumt,size*size)
        assert cov==closed(n,m),(n,m,cov,closed(n,m))
        if 3<=m<=comb(n-2,2)+1:
            assert (cov>0)==(m> (n+1)//2)
            assert (cov<0)==(m<= (n+1)//2)
        else: assert cov==0
        count+=1
    return count,1<<N


def check_binomial(n,p):
    # Independent-edge formula checks against exact graph distributions.
    edges=list(combinations(range(n),2)); N=len(edges)
    emap={e:i for i,e in enumerate(edges)}
    masks=[sum(1<<k for k,(a,b) in enumerate(edges) if (a in (u,v) or b in (u,v))) for u,v in edges]
    tri=[sum(1<<emap[e] for e in ((a,b),(a,c),(b,c))) for a,b,c in combinations(range(n),3)]
    ej=et=ejt=Fraction(0)
    for g in range(1<<N):
        m=g.bit_count();pr=p**m*(1-p)**(N-m)
        j=sum((g&inc)==1<<i for i,inc in enumerate(masks))
        t=sum((g&tri_mask)==tri_mask for tri_mask in tri)
        ej+=pr*j;et+=pr*t;ejt+=pr*j*t
    assert ejt-ej*et == -N*(n-2)**2*p**4*(1-p)**(2*n-4)


def main():
    total=0
    for n in (5,6):
        rows,graphs=exhaustive(n);print(f'n={n}: {graphs} graphs, {rows} exact covariance identities')
        total+=rows
    check_binomial(5,Fraction(1,3))
    check_binomial(5,Fraction(2,3))
    # Check the sharp noninteger threshold, and algebraic exact formula at 100 sizes.
    for n in range(5,105):
        N=comb(n,2);Q=comb(n-2,2)
        A=Fraction(4,3*(n-1)*(n*n-5*n+2))
        B=Fraction(4,3*(n+1)*(n*n-n-4))
        threshold=Fraction(3*A,A-B)
        alternate=Fraction(n,2)+1-Fraction(n+5,3*n*n-6*n-1)
        assert threshold==alternate
        assert (n+1)//2 < threshold < (n+1)//2 + 1
        assert 3 <= (n+1)//2 < Q+1
        total+=3
    print('PASS: all exact finite checks, including',total,'identity/inequality assertions')

if __name__=='__main__':main()
