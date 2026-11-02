#!/usr/bin/env python3
"""Finite checks for constant-weight-three non-overlapping codes.

Run with: python3 verify.py
Only Python's standard library is required.
"""
from itertools import combinations


def words(n):
    for i,j in combinations(range(2,n),2):
        s=['0']*n
        s[i-1]=s[j-1]=s[-1]='1'
        yield (i,j,''.join(s))


def conflicts(x,y):
    n=len(x)
    return any(x[:ell]==y[-ell:] or y[:ell]==x[-ell:]
               for ell in range(1,n))


def predicted(n):
    m,r=divmod(n,3)
    if r==0: return 3*m*(m-1)//2
    if r==1: return m*(3*m-1)//2
    return m*(3*m+1)//2


def extremal_parameters(n):
    m,r=divmod(n,3)
    return [m,m+1] if r==0 else [m+1]


def candidate_family(n,a):
    return tuple(s for i,j,s in words(n) if i>=a and j>=n+1-a)


def exhaustive(n):
    # Exhaust all oriented subsets, not just a chosen construction.
    W=[s for _,_,s in words(n)]
    C=[s for s in W if not conflicts(s,s)]
    bad=[0]*len(C)
    for i,s in enumerate(C):
        for j,t in enumerate(C):
            if i!=j and conflicts(s,t): bad[i]|=(1<<j)
    best=0; winners=[]
    for mask in range(1<<len(C)):
        if mask.bit_count()<best: continue
        u=mask; good=True
        while u:
            bit=u&-u; k=bit.bit_length()-1
            if mask&bad[k]: good=False;break
            u-=bit
        if not good: continue
        if mask.bit_count()>best:
            best=mask.bit_count(); winners=[]
        if mask.bit_count()==best:
            winners.append(frozenset(C[i] for i in range(len(C)) if mask>>i&1))
    predicted_winners={frozenset(candidate_family(n,a)) for a in extremal_parameters(n)}
    assert best==predicted(n),(n,best,predicted(n))
    assert set(winners)==predicted_winners,(n,len(winners),len(predicted_winners))
    return len(C),1<<len(C),len(winners)


def direct_region_check(n):
    all_candidates=list(words(n))
    for a in range(2,(n//2)+1):
        C=candidate_family(n,a)
        assert len(C)==(a-1)*(2*n-3*a)//2,(n,a,len(C))
        for x in C:
            for y in C:
                assert not conflicts(x,y),(n,a,x,y)
    assert max((len(candidate_family(n,a)) for a in range(2,n)),default=0)==predicted(n)


def direct_criterion_check(n):
    W=list(words(n))
    # Every pair, including self, has no overlap exactly when the
    # smallest first-interior index + smallest second-interior index > n.
    for i,j,x in W:
        for p,q,y in W:
            valid = not conflicts(x,x) and not conflicts(y,y) and not conflicts(x,y)
            expected = min(i,p)+min(j,q)>n
            assert valid == expected,(n,(i,j),(p,q),valid,expected)


def main():
    for n in range(4,10):
        a,b,c=exhaustive(n)
        print(f'exhaustive n={n} orientation_candidates={a} subsets={b} optimum={predicted(n)} oriented_maxima={c}')
    for n in range(4,22):
        direct_criterion_check(n)
    print('criterion checked for all ordered pairs, n=4..21')
    for n in range(4,31):
        direct_region_check(n)
    print('formula and direct all-pairs construction n=4..30')
    print('VERIFY_OK')

if __name__=='__main__': main()
