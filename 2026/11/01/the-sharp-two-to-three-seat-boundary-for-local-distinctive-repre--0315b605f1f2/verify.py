#!/usr/bin/env python3
"""Finite corroboration for two-seat distinctive-representation results."""
from itertools import combinations
from random import Random


def jr(n, k, support, committee):
    q = (n+k-1)//k
    full = (1 << n)-1
    represented = 0
    for i in committee:
        represented |= support[i]
    unrepresented = full ^ represented
    return all((s & unrepresented).bit_count() < q for s in support)


def exact_dr(n, k, support, committee):
    q = (n+k-1)//k
    return jr(n,k,support,committee) and all(support[i].bit_count()==q for i in committee)


def local_dr(n,k,support,committee):
    if not jr(n,k,support,committee):
        return False
    q = (n+k-1)//k
    chosen = set(committee)
    for old in committee:
        for new in range(len(support)):
            if new in chosen:
                continue
            # The only exception in the source's local-DR definition.
            if support[old].bit_count()*k >= n and support[new].bit_count()*k < n:
                continue
            if abs(support[old].bit_count()-q) <= abs(support[new].bit_count()-q):
                continue
            successor = tuple(sorted((chosen-{old})|{new}))
            if jr(n,k,support,successor):
                return False
    return True


def check(n,k,support):
    committees = tuple(combinations(range(len(support)),k))
    exists = any(exact_dr(n,k,support,W) for W in committees)
    localbad = any(local_dr(n,k,support,W) and not exact_dr(n,k,support,W)
                   for W in committees)
    if k==2 and exists:
        assert not localbad, (n,k,support)
    return exists,localbad


def two_seat_formula(n,support):
    q=(n+1)//2
    qids=[i for i,s in enumerate(support) if s.bit_count()==q]
    if len(qids)<2:return False
    if n%2:return True
    if any(support[i]!=support[j] for i,j in combinations(qids,2)):
        return True
    full=(1<<n)-1
    return not any(((full ^ support[qids[0]]) & s)==(full ^ support[qids[0]]) for s in support)


def main():
    tested=0
    for n in range(1,6):
        candidates=list(range(1,1<<n))
        for m in range(2,min(5,len(candidates))+1):
            for supp in combinations(candidates,m):
                exists,_=check(n,2,supp)
                assert exists==two_seat_formula(n,supp), (n,supp)
                tested+=1
    rng=Random(937)
    duplicate_profiles=0
    for n in range(2,11):
        for _ in range(2000):
            m=rng.randrange(2,9)
            support=tuple(rng.randrange(1,1<<n) for __ in range(m))
            exists,_=check(n,2,support)
            assert exists==two_seat_formula(n,support), (n,support,exists,two_seat_formula(n,support))
            duplicate_profiles+=1
    # Five distinct candidate support sets, six voters, three seats.
    # Bit 0 is voter 1.
    witness=(15,20,24,34,48)
    bad=(0,1,4)
    good=(1,2,3)
    assert exact_dr(6,3,witness,good)
    assert jr(6,3,witness,bad) and local_dr(6,3,witness,bad)
    assert not exact_dr(6,3,witness,bad)
    for new in (2,3):
        assert not jr(6,3,witness,tuple(sorted((set(bad)-{0})|{new})))
    print(f'VERIFY_OK two_seat_unique_support_profiles={tested} random_profiles_including_duplicates={duplicate_profiles} three_seat_distinct_support_witness=6v_5c')

if __name__=='__main__':
    main()
