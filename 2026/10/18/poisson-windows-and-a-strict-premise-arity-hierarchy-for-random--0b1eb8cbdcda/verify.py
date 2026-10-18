#!/usr/bin/env python3
"""Finite exact checks for random attribute implications and overlap bounds."""
from itertools import combinations, product
from fractions import Fraction
from math import comb

def events(m,k):
    return [(tuple(A),b) for A in combinations(range(m),k) for b in range(m) if b not in A]

def holds(columns,n,A,b):
    inter=(1<<n)-1
    for a in A: inter &= columns[a]
    return inter&(~columns[b])&((1<<n)-1)==0

def check_exact():
    cases=0
    for k in (2,3):
        for m in range(k+1, 6 if k==2 else 5):
            for n in (1,2,3):
                if n*m>15: continue
                ev=events(m,k)
                expected=Fraction(0)
                positive=0
                zero_support_imp=0
                for col in product(range(1<<n),repeat=m):
                    count=0
                    for A,b in ev:
                        if holds(col,n,A,b):
                            count+=1
                            supp=(1<<n)-1
                            for a in A:supp &=col[a]
                            if supp==0:zero_support_imp+=1
                    expected+=count
                    positive+=(count>0)
                tot=2**(n*m)
                q=Fraction(2**(k+1)-1,2**(k+1))
                assert expected/Fraction(tot)==len(ev)*q**n,(k,m,n)
                assert 0 <= positive <= tot
                cases+=1
    print('FINITE_EXPECTATION_OK',cases)

def check_overlap():
    tests=0
    for k in range(2,5):
        N=k+1;m=2*N
        alphabet=range(m)
        ref=(tuple(range(k)),k)
        base=set(ref[0])|{ref[1]}
        for A,b in events(m,k):
            if (A,b)==ref: continue
            other=set(A)|{b}
            s=len(base&other)
            if not s:continue
            both=0
            for bits in product((0,1),repeat=len(base|other)):
                d=dict(zip(sorted(base|other),bits))
                bad1=(all(d[i] for i in ref[0]) and not d[ref[1]])
                bad2=(all(d[i] for i in A) and not d[b])
                both+=not(bad1 or bad2)
            prob=Fraction(both,2**len(base|other))
            a=Fraction(1,2**N);q=1-a
            if s<N:
                bound=1-2*a+a*a*(2**s)
                assert prob<=bound, (k,ref,(A,b),s,prob,bound)
                assert bound**N < q**(2*N-s), (k,s,bound,q)
            else:
                assert prob==1-2*a,(k,s,prob)
            tests+=1
    print('OVERLAP_OK',tests)
if __name__=='__main__':
    check_exact();check_overlap();print('VERIFY_OK')
