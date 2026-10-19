#!/usr/bin/env python3
"""Exact rank-chamber verification for length-weighted mutual nearest-neighbor pairs.

For iid unit exponentials, ordered sample values have independent exponential
increments of rates n,n-1,...,1. Conditional ordered-second-moment formulas
are evaluated by rationals over all n! rank permutations, without simulation.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial, sqrt

def check(n):
    means=[sum((F(1,n-j) for j in range(r+1)),F()) for r in range(n)]
    square=[F(1,(n-j)**2) for j in range(n)]
    count1=count2=weighted1=weighted2=cross=near1=near2=0
    for perm in permutations(range(n)):
        good=[i for i in range(n) if perm[i]<perm[(i-1)%n] and perm[i]<perm[(i+1)%n]]
        k=len(good)
        w=sum((means[perm[i]] for i in good),F())
        # E(sum selected exponential order statistics)^2 conditional on ranks
        w2=w*w+sum((square[j] * sum(perm[i]>=j for i in good)**2 for j in range(n)),F())
        minsum=sum((means[min(perm[i],perm[(i-1)%n])] for i in range(n)),F())
        count1+=k;count2+=k*k;weighted1+=w;weighted2+=w2;cross+=k*w
        near1+=minsum;near2+=k*minsum
    fac=factorial(n)
    m1=F(count1,fac); vm=F(count2,fac)-m1*m1
    # normalized circular gaps are exponentials divided by their total S.
    # S~Gamma(n,1) independent of the normalized gap vector.
    ew=F(weighted1,fac*n)
    ew2=F(weighted2,fac*n*(n+1))
    vw=ew2-ew*ew
    cmw=F(cross,fac*n)-m1*ew
    cl=F(near2,fac*n)-m1*F(near1,fac*n)
    if n>=5:
        assert m1==F(n,3)
        assert vm==F(2*n,45)
        assert ew==F(1,9)
        assert vw==F(44,1125*(n+1)),(n,vw)
        assert cmw==F(16,675),(n,cmw)
        assert cl==F(-1,36),(n,cl)
        assert cmw>0 and cl<0
    print(f'n={n}, permutations={fac}, VarM={vm}, EW={ew}, VarW={vw}, Cov(M,W)={cmw}, Cov(M,L)={cl}')

for n in range(3,9):check(n)
print('PASS: all 46,230 exponential-rank configurations through n=8, including second moments')
