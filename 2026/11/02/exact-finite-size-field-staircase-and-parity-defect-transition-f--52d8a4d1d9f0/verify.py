"""Exact integer verifier for the triangular-graph antiferromagnetic Ising ground-state theorem.
No external dependencies. Run: python verify.py
Spin states are enumerated by a Gray code, with exact incremental degree/energy updates.
This verifies n=4,5,6,7 and each half-integer h/J from 0 to 2(n-2)+1.
"""
from collections import Counter
from itertools import combinations


def expected_profiles(n, t):
    """t=2*h/J integer; returns the complete set of sorted signed degree tuples."""
    vals=list(range(-(n-1),n,2))
    value=lambda q: 2*q*q-t*q
    bottom=min(map(value,vals))
    best=[q for q in vals if value(q)==bottom]
    if len(best)==2:
        q=best[0];r=(n-1+q)//2
        return {tuple([q]*(n-k)+[q+2]*k) for k in range(n+1) if (n*r+k)%2==0}
    assert len(best)==1, (n,t,best)
    q=best[0];r=(n-1+q)//2
    if (n*r)%2==0:
        return {tuple([q]*n)}
    near=[q2 for q2 in (q-2,q+2) if q2 in vals]
    v=min(value(q2) for q2 in near)
    return {tuple(sorted([q]*(n-1)+[q2])) for q2 in near if value(q2)==v}


def gray_ground_profiles(n):
    edges=list(combinations(range(n),2))
    m=len(edges)
    incident=[-(n-1)]*n
    spin=[-1]*m
    M=-m
    Q=n*(n-1)**2
    # The gray code visits every one of the 2^m spin configurations once.
    profiles=Counter()
    for k in range(1<<m):
        if k:
            pos=(k&-k).bit_length()-1
            a,b=edges[pos]
            delta=-2*spin[pos]
            spin[pos]=-spin[pos]
            Q+=(incident[a]+delta)**2-incident[a]**2
            Q+=(incident[b]+delta)**2-incident[b]**2
            incident[a]+=delta;incident[b]+=delta
            M+=delta
        assert sum(incident)==2*M
        profiles[tuple(sorted(incident))]+=1
    print('n',n,'states',sum(profiles.values()),'degree profiles',len(profiles))
    for t in range(4*(n-2)+3):
        bestscore=min(sum(q*q for q in p)-t*sum(p)//2 for p in profiles)
        observed={p for p in profiles if sum(q*q for q in p)-t*sum(p)//2==bestscore}
        expected=expected_profiles(n,t)
        assert observed==expected, (n,t,observed,expected)
        if t in (0,2,4,6,8,10,12,16,20,24):
            g=sum(profiles[p] for p in observed)
            mags=sorted({sum(p)//2 for p in observed})
            print(f' h/J={t}/2  ground_states={g}  magnetizations={mags}')
    print('PASS',n)


if __name__=='__main__':
    for n in (4,5,6,7):
        gray_ground_profiles(n)
    print('PASS: exhaustive verification on n=4,5,6,7; all indicated fields and complete degeneracy counts.')
