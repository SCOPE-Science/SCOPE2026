"""Reproducibility checks for finite uniform-block down-interpretation laws."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def blocks(n, b):
    """Each unordered partition of {0,...,n-1} into b-sets exactly once."""
    assert n % b == 0 and 1 <= b <= n
    def rec(left):
        if not left:
            yield ()
        else:
            lead = left[0]
            for tail in combinations(left[1:], b-1):
                selected=(lead,)+tail
                rem=tuple(x for x in left if x not in selected)
                for v in rec(rem): yield (selected,)+v
    yield from rec(tuple(range(n)))


def fall(a,r):
    ans=1
    for j in range(r): ans*=a-j
    return ans


def factorial_moment(n,b,k,r):
    if b*r>k:return Fraction(0)
    return Fraction(fall(n//b,r)*fall(k,b*r),fall(n,b*r))


def formula_transition(n,b,k):
    ans={}
    for j in range(k//b+1):
        ans[b*j]=sum((Fraction((-1)**s, factorial(j)*factorial(s))*factorial_moment(n,b,k,j+s)
                     for s in range(k//b-j+1)),Fraction(0))
    return {s:q for s,q in ans.items() if q}


def observe_partition(s,P):
    return frozenset(x for B in P if set(B)<=s for x in B)


def brute_transition(n,b,k):
    P=list(blocks(n,b)); S=set(range(k))
    d=Counter(len(observe_partition(S,M)) for M in P)
    return {j:Fraction(v,len(P)) for j,v in d.items()}


def dp_distribution(n,b,p,t):
    d={k:Fraction(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1)}
    for _ in range(t):
        nd=Counter()
        for k,q in d.items():
            if not q:continue
            for j,v in formula_transition(n,b,k).items():nd[j]+=q*v
        d=nd
    return {j:q for j,q in d.items() if q}


def brute_distribution(n,b,p,t):
    P=list(blocks(n,b))
    states=Counter()
    for mask in range(2**n):
        s=frozenset(j for j in range(n) if (mask>>j)&1)
        states[s]+=p**len(s)*(1-p)**(n-len(s))
    for _ in range(t):
        nxt=Counter()
        for s,q in states.items():
            for part in P:
                nxt[observe_partition(s,part)]+=q/len(P)
        states=nxt
    out=Counter()
    for s,q in states.items():out[len(s)]+=q
    return {j:q for j,q in out.items() if q}


def run():
    cases=[(2,2),(4,2),(6,2),(8,2),(3,3),(6,3),(9,3),(4,4),(8,4)]
    for n,b in cases:
        for k in range(n+1):
            assert brute_transition(n,b,k)==formula_transition(n,b,k),(n,b,k)
        print('transition checks: n=%d b=%d OK'%(n,b))
    cases2=[(2,2,3),(4,2,3),(6,2,3),(8,2,2),(3,3,3),(6,3,3),(9,3,1),(4,4,3),(8,4,2)]
    for n,b,tmax in cases2:
        for t in range(tmax+1):
            lhs=brute_distribution(n,b,Fraction(1,2),t)
            rhs=dp_distribution(n,b,Fraction(1,2),t)
            assert lhs==rhs,(n,b,t,lhs,rhs)
        print('distribution checks: n=%d b=%d depths=0..%d OK'%(n,b,tmax))
    print('example n=4 b=2 p=1/2 depth=2',dp_distribution(4,2,Fraction(1,2),2))
    print('example n=6 b=3 p=1/2 depth=2',dp_distribution(6,3,Fraction(1,2),2))
    print('ALL_CHECKS_OK')

if __name__=='__main__':run()
