"""Finite exact checks for the complete-feedback score collision identity.

This program verifies finite combinatorial identities and numerical plausibility;
it does not certify the weak-convergence theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import sqrt, pi
from random import Random


def path_score(cards,n,m):
    counts=[m]*n
    score=0
    collisions=0
    drops=0
    s=Fraction(0)
    mart=Fraction(0)
    z_prev=0
    regulator=Fraction(0)
    for k,c in enumerate(cards):
        oldmax=max(counts)
        leaders=[i for i,z in enumerate(counts) if z==oldmax]
        guess=leaders[0]  # predictable deterministic greedy tie rule
        event=int(c==guess)
        s+=Fraction(oldmax,n*m-k)
        mart+=event-Fraction(oldmax,n*m-k)
        score+=event
        counts[c]-=1
        newmax=max(counts)
        drop=oldmax-newmax
        drops+=drop
        collisions+=event-drop
        # Difference of the discrete maximum and its selected-coordinate increment.
        increment=(newmax-oldmax)+event
        regulator+=increment
        assert increment in (0,1)
        assert (increment==1)==(len(leaders)>=2 and c==guess)
    assert all(z==0 for z in counts)
    assert drops==m
    assert score-m==collisions==regulator
    assert s+mart==score
    return score,collisions,s


def all_multiset_perms(n,m):
    def rec(prefix,remaining):
        if len(prefix)==n*m:
            yield tuple(prefix)
            return
        for i in range(n):
            if remaining[i]:
                remaining[i]-=1
                prefix.append(i)
                yield from rec(prefix,remaining)
                prefix.pop()
                remaining[i]+=1
    yield from rec([], [m]*n)


def exact():
    checked=0
    for n,m in [(2,1),(2,4),(3,2),(3,3),(4,2)]:
        score_sum=0
        s_sum=Fraction(0)
        ct=0
        for deck in all_multiset_perms(n,m):
            score,coll,s=path_score(deck,n,m)
            score_sum+=score
            s_sum+=s
            ct+=1
        assert Fraction(score_sum,ct)==s_sum/ct
        checked+=ct
        print('exact',n,m,ct,'mean surplus',float(Fraction(score_sum,ct)-m))
    print('TOTAL_EXACT_DECKS',checked)


def simulation():
    rng=Random(83452)
    for n in (2,3):
        m=400
        values=[]
        for _ in range(340):
            d=[i for i in range(n) for j in range(m)]
            rng.shuffle(d)
            cnt=[m]*n
            surplus=0
            for c in d:
                w=max(cnt)
                # Select the lexicographically first remaining maximum.
                guess=cnt.index(w)
                if c==guess and cnt.count(w)>1:
                    surplus+=1
                cnt[c]-=1
            values.append(surplus/sqrt(m))
        empirical=sum(values)/len(values)
        target=(sqrt(pi)/2 if n==2 else 3*sqrt(pi)/4)
        print('simulation',n,m,'empirical',empirical,'target',target)
        assert abs(empirical-target)<0.3  # low-power plausibility only

if __name__=='__main__':
    exact()
    simulation()
