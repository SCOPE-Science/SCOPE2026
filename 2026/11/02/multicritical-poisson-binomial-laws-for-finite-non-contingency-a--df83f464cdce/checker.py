"""Exact finite checks for random equicardinal S5 non-contingency-algebra theorem.

No third-party packages. Tests exhaustive valuations and independently computes
occupancy-law probabilities with exact rational arithmetic.
"""
from itertools import product, combinations
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb

def popcount(x): return x.bit_count()

def support(vs):
    out=0
    for c in vs: out |= 1<<c
    return out

def cluster_supports(v,q,r,m):
    return tuple(support(v[i*r:(i+1)*r]) for i in range(m))

def delta(A,r,m):
    """Non-contingency of a set A of world indices, as bit mask."""
    result=0
    for b in range(m):
        block=((1<<r)-1)<<(b*r)
        inter=A&block
        if inter==0 or inter==block:result|=block
    return result

def check_assignment(v,q,r,m):
    n=r*m
    supp=cluster_supports(v,q,r,m)
    expected={(supp[w//r],v[w]) for w in range(n)}
    prop_masks=[]
    for t in range(q):
        prop_masks.append(sum(1<<w for w in range(n) if v[w]==t))
    delta_single=[delta(x,r,m) for x in prop_masks]
    signatures={(v[w], tuple((a>>w)&1 for a in delta_single)) for w in range(n)}
    assert len(signatures)==len(expected), (v,expected,signatures)
    for T in range(1<<q):
        mask=sum(1<<w for w in range(n) if (T>>v[w])&1)
        dm=delta(mask,r,m)
        for w in range(n):
            for z in range(w+1,n):
                if (v[w],tuple((a>>w)&1 for a in delta_single)) == (v[z],tuple((a>>z)&1 for a in delta_single)):
                    assert ((dm>>w)&1)==((dm>>z)&1), (v,T,w,z)
    atoms=[]
    ids={}
    for w in range(n):
        key=(v[w],tuple((a>>w)&1 for a in delta_single))
        ids.setdefault(key,0)
        ids[key]|=1<<w
    atoms=list(ids.values())
    assert len(atoms)==sum(popcount(S) for S in set(supp))
    # Exhaustive closure test for arbitrary Boolean combinations of distinguished cells
    for bits in range(1<<len(atoms)):
        mask=0
        for j,A in enumerate(atoms):
            if bits>>j&1:mask|=A
        dm=delta(mask,r,m)
        assert all(not (dm&A) or (dm&A)==A for A in atoms), (v,bits)
    return len(atoms)

def support_prob(q,r,S):
    s=popcount(S)
    return Fraction(sum((-1)**(s-j)*comb(s,j)*j**r for j in range(s+1)),q**r)

def theoretical_law(q,r,m):
    allS=range(1,1<<q)
    probabilities={S:support_prob(q,r,S) for S in allS}
    assert sum(probabilities.values())==1
    state={0:Fraction(1)}
    for _ in range(m):
        out=defaultdict(Fraction)
        for present,prob in state.items():
            for S,p in probabilities.items():out[present|(1<<(S-1))]+=prob*p
        state=out
    dist=defaultdict(Fraction)
    for seen,p in state.items():
        atomcount=sum(popcount(S) for S in allS if (seen>>(S-1))&1)
        dist[atomcount]+=p
    assert sum(dist.values())==1
    return {z:p for z,p in dist.items() if p}

def test(q,r,m):
    cnt=Counter()
    for v in product(range(q),repeat=r*m):cnt[check_assignment(v,q,r,m)]+=1
    law={z:Fraction(c,q**(r*m)) for z,c in cnt.items()}
    theory=theoretical_law(q,r,m)
    assert law==theory,(q,r,m,law,theory)
    # Independently verify first moment by exact support occupancy
    expected=sum(Fraction(z)*p for z,p in law.items())
    expectation=sum(popcount(S)*(1-(1-support_prob(q,r,S))**m) for S in range(1,1<<q))
    assert expected==expectation,(q,r,m)
    print('PASS',q,r,m,'assignments',q**(r*m),'law',dict(sorted(law.items())))
    return q**(r*m)

if __name__=='__main__':
    total=0
    for q in (2,4):
        for r in (1,2,3,4) if q==2 else (1,2,3):
            for m in (1,2,3) if q==2 else (1,2):
                total+=test(q,r,m)
    print('ALL_CHECKS_OK exhaustive_assignments=',total)
