#!/usr/bin/env python3
"""Exact finite checks for generalized-repunit multiple digit-sum spectra.

The proof in RESULT.md establishes the theorem for every base and length;
these finite tests are independently computable corroboration, not a proof
of the unbounded quantified statement.
"""
from math import gcd

def digit_sum(x,b):
    s=0
    while x:
        x,a=divmod(x,b)
        s+=a
    return s

def predicted(b,r,w):
    return any(w>=r*j and (w-r*j)%(b-1)==0 for j in range(1,b))

def exact_reachable(b,r,limit):
    M=(b**r-1)//(b-1)
    A=[pow(b,i,M) for i in range(r)]
    S={0}
    for w in range(1,limit+1):
        S={(s+a)%M for s in S for a in A}
        yield w,0 in S

def witness(b,r,j,t):
    assert 1<=j<b and t>=0
    C=[j]*r
    for _ in range(t):
        i=next(i for i in range(r) if C[i]>0)
        C[i]-=1
        C[(i-1)%r]+=b
    N=sum(b**(i+r*h) for i,c in enumerate(C) for h in range(c))
    return N

def run():
    settings=comparisons=0
    for b in range(2,10):
        for r in range(2,8):
            M=(b**r-1)//(b-1)
            if M>1800:continue
            limit=min(90,max(30,3*r*(b-1)))
            for w,found in exact_reachable(b,r,limit):
                assert found==predicted(b,r,w),(b,r,w,found)
                comparisons+=1
            d=gcd(r,b-1); rp=r//d; mp=(b-1)//d
            F=d*mp*(rp-1);G=(rp-1)*(mp+1)//2
            gaps=[w for w in range(d,F+d,d) if not predicted(b,r,w)]
            assert len(gaps)==G,(b,r,'genus',G,len(gaps))
            assert (F==0 and not gaps) or max(gaps)==F,(b,r,'F',F,gaps)
            assert all(predicted(b,r,w) for w in range(F+d,F+d+4*(b-1),d))
            settings+=1
    witness_tests=0
    for b in range(2,11):
        for r in range(4,8):
            M=(b**r-1)//(b-1)
            for j in range(1,b):
                for t in (0,1,2,3,7,13,19):
                    N=witness(b,r,j,t)
                    assert N>0 and N%M==0 and digit_sum(N,b)==r*j+(b-1)*t,(b,r,j,t)
                    witness_tests+=1
    print('PASS:',settings,'finite exact residue-DP settings,',comparisons,'weight comparisons,',witness_tests,'explicit divisible witness checks')

if __name__=='__main__':run()
