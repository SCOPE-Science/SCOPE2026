#!/usr/bin/env python3
"""Exact independent checks of random-priority envy / coupon-singleton identities."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


def law_by_coupon_states(n):
    # Delete self loops from the state (seen, singleton count).
    @lru_cache(None)
    def rec(seen, single):
        if seen == n:
            return {single: Fraction(1)}
        denom = n - seen + single
        out = Counter()
        for k,v in rec(seen+1,single+1).items():
            out[k] += Fraction(n-seen, denom)*v
        if single:
            for k,v in rec(seen,single-1).items():
                out[k] += Fraction(single,denom)*v
        return dict(out)
    return rec(0,0)


def law_by_rsd_joint_probabilities(n):
    # E[z^U] = E[(1+(z-1))^U] = sum_{r=0}^n b_r (z-1)^r.
    b=[Fraction(1)]+[Fraction() for _ in range(n)]
    for r in range(1,n+1):
        for js in combinations(range(1,n+1),r):
            p=Fraction(factorial(r))
            for t,i in enumerate(js,1): p /= n-i+t
            b[r]+=p
    ans={j:sum((b[r]*comb(r,j)*((-1)**(r-j)) for r in range(j,n+1)),Fraction()) for j in range(n+1)}
    return {k:v for k,v in ans.items() if v}


def law_by_direct_rank_enumeration(n):
    labels=tuple(range(n))
    permitted=[]
    for t in range(n):
        permitted.append([r for r in permutations(labels) if r.index(t)==min(r.index(q) for q in range(t,n))])
    mass=Counter(); total=1
    for p in permitted:total*=len(p)
    for rankings in product(*permitted):
        # Choices are the labels 0,...,n-1 by conditioning on the completed allocation.
        winners=sum(all(rankings[l].index(l)<rankings[l].index(k) for l in range(k+1,n)) for k in range(n))
        mass[winners]+=1
    return {k:Fraction(v,total) for k,v in mass.items()},total


def check():
    profiles=0
    for n in range(1,13):
        law1=law_by_coupon_states(n)
        law2=law_by_rsd_joint_probabilities(n)
        assert law1==law2,(n,law1,law2)
        assert sum(law1.values(), Fraction())==1
        H=sum((Fraction(1,j) for j in range(1,n+1)),Fraction())
        H2=sum((Fraction(1,j*j) for j in range(1,n+1)),Fraction())
        mu=sum(k*p for k,p in law1.items())
        var=sum(k*k*p for k,p in law1.items())-mu**2
        assert mu==H and var==H*H+2*H2-3*H
        if n<=4:
            law3,t=law_by_direct_rank_enumeration(n)
            profiles+=t
            assert law3==law1,(n,law3,law1)
            print('n',n,'conditional_profiles',t,'law',[(k,str(law1[k])) for k in sorted(law1)])
    print('VERIFY_OK n=1..12 coupon_exact=joint_probability_exact direct_ranks_n=1..4 count='+str(profiles))

if __name__=='__main__':check()
