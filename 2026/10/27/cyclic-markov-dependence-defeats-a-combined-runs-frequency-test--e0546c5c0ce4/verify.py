"""Finite exact checks for a three-state directional Markov alternative.
All calculations use the Python standard library and integer/rational arithmetic.
This finite checker does not replace the infinite-horizon CLT proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

DELTA=F(1,4)
P=(F(1,3),F(1,3)+DELTA,F(1,3)-DELTA)
C=(1-3*DELTA*DELTA)/(1+3*DELTA*DELTA)
assert C==F(13,19)


def direct_enumeration(n):
    # Each path begins at uniform random state and has independent increments.
    tot=3*12**(n-1)
    runs=[0]*n
    direction=F(0)
    Q=F(0)
    assertions=0
    for initial in range(3):
        for increments in product(range(3),repeat=n-1):
            weight=1
            states=[initial]
            dscore=0
            nonzero=0
            for x in increments:
                weight*=4 if x==0 else (7 if x==1 else 1)
                nonzero+=(x!=0)
                dscore+=(1 if x==1 else (-1 if x==2 else 0))
                states.append((states[-1]+x)%3)
            runs[nonzero+1-1]+=weight
            direction+=F(weight*dscore,tot)
            counts=[states.count(i) for i in range(3)]
            Q+=F(weight*3*sum((3*z-n)**2 for z in counts),tot*9*n)
    assert sum(runs)==tot;assertions+=1
    for k in range(n):
        want=F(comb(n-1,k)*2**k,3**(n-1))
        assert F(runs[k],tot)==want;assertions+=1
    assert direction==F(n-1,2);assertions+=1
    # The exact Pearson expectation has the even-lag spectral expansion.
    exact=F(2)+F(4,n)*sum((n-2*k)*(-3*DELTA*DELTA)**k for k in range(1,n//2+1) if 2*k<n)
    assert Q==exact;(assertions:=assertions+1)
    print('n=%d exact paths=%d; run-law, directional mean, Pearson mean PASS'%(n,3**n))
    return assertions


def check():
    assertions=0
    for n in range(2,9):assertions+=direct_enumeration(n)
    # Entire matrix has equal stationary marginals but unequal next-step laws.
    for i in range(3):
        assert sum(P)==1; assertions+=1
        assert P[0]==F(1,3) and P[1]!=P[2];assertions+=1
    # Asymptotic Pearson scaling is strictly below the iid scaling.
    assert 0<C<1;assertions+=1
    for n in (16,32,64,128,256):
        val=F(2)+F(4,n)*sum((n-2*k)*(-3*DELTA*DELTA)**k for k in range(1,n//2+1) if 2*k<n)
        assert val>0 and abs(val-2*C)<F(16,n);assertions+=1
    print('PASS:',assertions,'exact assertions; limiting Pearson scale =',C)

if __name__=='__main__':check()
