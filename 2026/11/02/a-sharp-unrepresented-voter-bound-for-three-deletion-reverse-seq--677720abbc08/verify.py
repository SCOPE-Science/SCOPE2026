#!/usr/bin/env python3
"""Exact-arithmetic spot checks for a three-deletion reverse-PAV theorem.

The infinite upper bound follows from the symbolic residual identities in RESULT.md;
finite tests below are independent consistency checks, not a substitute for them.
"""
from fractions import Fraction as F
from itertools import combinations


def losses(ballots, remaining):
    """Return candidate -> exact marginal PAV loss for weighted approval ballots."""
    remaining = frozenset(remaining)
    out = {c:F(0) for c in remaining}
    for approved, weight in ballots:
        common=approved & remaining
        if common:
            gain=F(weight,len(common))
            for c in common:
                out[c]+=gain
    return out


def gaps(k, mask, b):
    values=[]
    for j in range(3):
        kept=sum(bool(mask & (1<<i)) for i in range(j,3))
        t=kept+b
        if t:
            d={c:F(int(bool(mask&(1<<c))),t) for c in range(j,3)}
            d['w']=F(b,k*t)
        else:
            d={c:F(0) for c in range(j,3)}
            d['w']=F(0)
        values.append(d)
    d0,d1,d2=values
    return (d0[0]-d0['w'],d0[0]-d0[1],d0[0]-d0[2],
            d1[1]-d1['w'],d1[1]-d1[2],d2[2]-d2['w'])


def dual(k, position):
    assert k>=2
    q=(3*k+1)*(k+2)
    if position==0:
        return F(2*(2*k+1),q),(F(0),F(2*(k-1),3*k+1),
            F(2*(k+1),3*k+1),F(2*k*(k-1),q),
            F(2*(k-1),q),F(2*k,3*k+1))
    if position==1:
        return F(1,k+1),(F(0),F(0),F(0),F(0),F(k,k+1),F(k,k+1))
    return F(1,k+1),(F(0),F(0),F(0),F(0),F(0),F(k,k+1))


def finite_dual_checks():
    tests=0
    for k in range(2,81):
        for mask in range(8):
            for b in range(k+1):
                gg=gaps(k,mask,b)
                for pos in range(3):
                    bnd,coeff=dual(k,pos)
                    indicated=F(int(bool(mask&(1<<pos)) and b==0))
                    assert bnd+sum((a*v for a,v in zip(coeff,gg)),F(0))>=indicated
                    tests+=1
    return tests


def sharp_family(k):
    """Integer-weighted symmetric profile attaining the upper bound with ties."""
    assert k>=2
    winners=list(range(3,k+3))
    ballots=[]
    for w in winners:
        ballots.append((frozenset((w,)), k*(k+3)))
    for missing in winners:
        eligible=set(winners)-{missing}
        ballots.append((frozenset({1}|eligible),k*k))
        ballots.append((frozenset({2}|eligible),k*k))
    ballots.extend([(frozenset((0,1)),2*k*k),
                    (frozenset((0,2)),2*k*k),
                    (frozenset((0,1,2)),2*k)])
    n=sum(w for _,w in ballots)
    assert n==k*(k+2)*(3*k+1)
    return ballots,n


def sharp_family_checks():
    for k in range(2,61):
        ballots,n=sharp_family(k)
        assert sum(w for a,w in ballots if 0 in a and not (a & set(range(3,k+3))))==2*k*(2*k+1)
        for step in range(3):
            ll=losses(ballots,range(step,k+3))
            assert ll[step]==min(ll.values())
        bnd,_=dual(k,0)
        assert F(2*k*(2*k+1),n)==bnd
    return 59


def strict_example():
    """Nine candidates, six winners, 252 voters; all deletions strict."""
    k=6
    winners=list(range(3,9))
    ballots=[]
    for w in winners:
        ballots.append((frozenset((w,)),14))
    for missing in winners:
        others=set(winners)-{missing}
        ballots.append((frozenset({1}|others),11))
        ballots.append((frozenset({2}|others),10))
    ballots.extend([(frozenset((0,1)),19),
                    (frozenset((0,2)),21),
                    (frozenset((0,1,2)),2)])
    n=sum(w for _,w in ballots)
    assert n==252
    violators=sum(w for a,w in ballots if 0 in a and not (a & set(winners)))
    assert violators==42 and 6*violators==n
    stage_results=[]
    for j in range(3):
        ll=losses(ballots,range(j,9))
        assert all(ll[j]<ll[c] for c in ll if c!=j)
        stage_results.append((j,ll[j],min(v for c,v in ll.items() if c!=j)))
    assert stage_results==[(0,F(62,3),F(127,6)),
                           (1,F(31),F(63,2)),
                           (2,F(33),F(100,3))]
    return stage_results

if __name__=='__main__':
    n=finite_dual_checks()
    m=sharp_family_checks()
    s=strict_example()
    print('VERIFY_OK exact_dual_ballot_cases=',n,
          'sharp_family_population_cases=',m,
          'strict_252_voter_deletion_scores=',s)
