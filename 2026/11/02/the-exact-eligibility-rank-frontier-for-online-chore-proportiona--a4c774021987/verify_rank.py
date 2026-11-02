"""Reproduce the rank-restricted proportional-share bounds and tree adversary.

Only standard Python 3.  Run: python verify_rank.py
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product
from random import Random


def construct(r: int, h: int, policy='left'):
    """Create adaptive r-ary champion tournament with unit-size tasks."""
    n=r**h
    champions=list(range(n))
    jobs=[]
    owner=[]
    loads=[0]*n
    shares=[Fraction(0) for _ in range(n)]
    for level in range(h):
        assert len(champions)%r==0
        nxt=[]
        for p in range(0,len(champions),r):
            eligible=tuple(champions[p:p+r])
            if policy=='left': choice=eligible[0]
            elif policy=='right':choice=eligible[-1]
            elif policy=='minload':choice=min(eligible,key=lambda i:(loads[i],i))
            elif policy=='hash':choice=eligible[(len(jobs)*17+5)%r]
            else:raise ValueError(policy)
            jobs.append(eligible)
            owner.append(choice)
            loads[choice]+=1
            for i in eligible:shares[i]+=Fraction(1,r)
            nxt.append(choice)
        champions=nxt
    champ=champions[0]
    assert len(jobs)==(n-1)//(r-1)
    assert loads[champ]==h
    assert shares[champ]==Fraction(h,r)
    assert sum(champ in edge for edge in jobs)==h
    assert len(set(jobs))==len(jobs)
    # Berge acyclicity: adding each hyperedge joins r previously disjoint components.
    parent=list(range(n))
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for edge in jobs:
        roots=[find(i) for i in edge]
        assert len(set(roots))==r,('cycle',edge)
        for root in roots[1:]:parent[root]=roots[0]
    assert len({find(i) for i in range(n)})==1
    # r-PROP is immediate for every valid assignment, not merely this construction.
    for i in range(n):assert loads[i]<=r*shares[i]
    assert loads[champ]-1==h-1
    assert Fraction(loads[champ]-1,1)/shares[champ]==Fraction(r*(h-1),h)
    return len(jobs),champ,Fraction(r*(h-1),h)


def random_allocation_upper(trials=1000):
    rng=Random(602)
    for _ in range(trials):
        n=rng.randrange(1,18)
        rank=rng.randrange(1,n+1)
        load=[Fraction(0) for _ in range(n)]
        share=[Fraction(0) for _ in range(n)]
        maxval=[Fraction(0) for _ in range(n)]
        for _ in range(rng.randrange(1,40)):
            k=rng.randrange(1,rank+1)
            eligible=rng.sample(range(n),k)
            size=Fraction(rng.randrange(1,100),rng.randrange(1,20))
            target=rng.choice(eligible)
            load[target]+=size
            maxval[target]=max(maxval[target],size)
            for i in eligible:share[i]+=size/k
        for i in range(n):
            assert load[i]-maxval[i]<=rank*share[i]
            assert load[i]<=rank*share[i]
    return trials


def exhaustive_branches(r: int,h: int):
    n=r**h
    leaves=0
    def dfs(current,level,loads,shares,edges,champ):
        nonlocal leaves
        if level==h:
            assert len(current)==1
            winner=current[0]
            assert loads[winner]==h
            assert shares[winner]==Fraction(h,r)
            assert sum(winner in s for s in edges)==h
            leaves+=1
            return
        # one level creates independent groups, so explore every possible recipient vector.
        groups=[tuple(current[j:j+r]) for j in range(0,len(current),r)]
        for picks in product(*groups):
            new_loads=loads.copy()
            new_shares=shares.copy()
            for s,pick in zip(groups,picks):
                new_loads[pick]+=1
                for i in s:new_shares[i]+=Fraction(1,r)
            dfs(list(picks),level+1,new_loads,new_shares,edges+groups,champ)
    dfs(list(range(n)),0,[0]*n,[Fraction(0) for _ in range(n)],[],None)
    return leaves


def main():
    trials=random_allocation_upper()
    print('arbitrary positive-size upper bound random profiles',trials,'PASS')
    for r,h in [(2,2),(2,3),(2,4),(2,11),(3,2),(3,3),(4,2),(5,2)]:
        for policy in ('left','right','minload','hash'):
            cnt,champ,ratio=construct(r,h,policy)
        print('rank',r,'height',h,'jobs',cnt,'adversarial Prop1 factor at least',ratio,'Berge-acyclic PASS')
    for r,h in [(2,2),(2,3),(2,4),(3,2),(4,2),(5,2)]:
        leaves=exhaustive_branches(r,h)
        expected=r**((r**h-1)//(r-1))
        assert leaves==expected
        print('exhaustive recipient pathways r,h',r,h,'leaves',leaves,'PASS')
    print('ALL TESTS PASSED')

if __name__=='__main__':main()
