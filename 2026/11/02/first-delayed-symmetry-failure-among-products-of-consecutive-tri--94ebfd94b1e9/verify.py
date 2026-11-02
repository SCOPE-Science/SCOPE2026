"""Exact bounded membership and pseudo-Frobenius certificates for selected semigroup powers.

Requires Python 3 standard library. The proof that its finite loops suffice is in RESULT.md.
"""
from itertools import product
from heapq import heappop, heappush
from pathlib import Path
import json

# The first two coordinates are a and k, where A_a=<a,a+1,a+2>.
# The third coordinate is the complete pseudo-Frobenius set.
CASES = {
    (2,1): [1], (2,2): [11], (2,3): [49],
    (3,1): [1,2],
    (4,1): [7], (4,2): [83], (4,3): [607],
    (5,1): [8,9],
    (6,1): [17], (6,2): [207,215],
    (7,1): [19,20],
    (8,1): [31], (8,2): [519],
    (8,3): [4023,4095,5223,5431,5503,5567,5791],
}

EXPECTED_M8 = {
    1: (31,16,1),
    2: (519,260,1),
    3: (5791,3072,7),
}


def monomials(a,k):
    return sorted({a**i * (a+1)**j * (a+2)**(k-i-j)
                   for i in range(k+1) for j in range(k-i+1)})


def bounded_certificate(a,k,proposed_pf):
    generators=monomials(a,k)
    mult=a**k
    assert generators[0]==mult
    F=max(proposed_pf)
    limit=F+max(generators)+mult
    # Bounded recurrence, exact by induction: R[n] iff n is a nonnegative
    # integral sum of the displayed monomial generators.
    R=bytearray(limit+1)
    R[0]=1
    for n in range(1,limit+1):
        R[n]=int(any(R[n-g] for g in generators if g<=n))
    # One missing value followed by a full band of the least generator
    # certifies the actual Frobenius number, without any search cutoff guess.
    assert not R[F]
    assert all(R[n] for n in range(F+1,F+mult+1))
    assert not R[0] == 0
    pf=sorted(n for n in range(1,F+1) if not R[n]
              and all(R[n+g] for g in generators))
    assert pf==proposed_pf, (a,k,pf,proposed_pf)
    genus=sum(1 for n in range(1,F+1) if not R[n])
    return F,genus,len(pf),limit


def apery_dijkstra(a,k):
    generators=monomials(a,k)
    mult=generators[0]
    INF=10**40
    dist=[INF]*mult
    dist[0]=0
    heap=[(0,0)]
    while heap:
        n,r=heappop(heap)
        if dist[r]!=n:
            continue
        for g in generators[1:]:
            rr=(r+g)%mult
            nn=n+g
            if nn<dist[rr]:
                dist[rr]=nn
                heappush(heap,(nn,rr))
    assert all(v<INF for v in dist)
    f=max(dist)-mult
    genus_numerator=2*sum(dist)-mult*(mult-1)
    assert genus_numerator % (2*mult)==0
    genus=genus_numerator//(2*mult)
    # Computes the generators-minus-multiplicity maxima independently
    pfs=sorted(w-mult for w in dist[1:]
               if all(w-mult+g>=dist[(w-mult+g)%mult] for g in generators))
    return f,genus,pfs,dist


def verify():
    with Path(__file__).with_name("certificates.json").open(encoding="utf-8") as handle:
        certificate=json.load(handle)
    evidence={(c["a"],c["k"]):c for c in certificate["cases"]}
    assert set(evidence)==set(CASES)
    checked=0
    for (a,k),pf in CASES.items():
        F,g,t,limit=bounded_certificate(a,k,pf)
        f2,g2,pf2,apery=apery_dijkstra(a,k)
        assert (F,g,pf)==(f2,g2,pf2), (a,k, F,g,pf,f2,g2,pf2)
        cert=evidence[(a,k)]
        assert cert["generators"]==monomials(a,k)
        assert cert["apery"]==apery
        assert cert["F"]==F and cert["genus"]==g and cert["PF"]==pf
        if a==8:
            assert (F,g,t)==EXPECTED_M8[k]
        checked+=1
    assert [len(CASES[(8,k)]) for k in (1,2,3)]==[1,1,7]
    for a in range(2,8):
        if a==2:
            assert all(len(CASES[(a,k)])==1 for k in (1,2,3))
        elif a in (3,5,7):
            assert len(CASES[(a,1)])>1
        elif a==4:
            assert len(CASES[(a,3)])==1
        elif a==6:
            assert len(CASES[(a,2)])>1
    print('VERIFY_OK independent_dp=yes independent_dijkstra=yes'
          f' complete_cases={checked} first_delayed_m=8'
          ' type_profile=1,1,7 F_profile=31,519,5791'
          ' genus_profile=16,260,3072')


if __name__=='__main__':
    verify()
