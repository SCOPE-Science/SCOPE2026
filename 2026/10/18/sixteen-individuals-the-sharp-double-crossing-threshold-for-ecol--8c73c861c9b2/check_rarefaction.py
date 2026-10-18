"""Exact, standalone verification of the finite rarefaction reversal boundary.

Run with Python 3.9 or newer. Uses only the Python standard library.
All comparisons are exact integers; no numerical tolerances are used.
"""
from functools import lru_cache
from math import comb

EXPECTED_P = (1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231)
WITNESSES = {
    ((8, 2, 2, 2, 2), (7, 5, 1, 1, 1, 1)),
    ((8, 2, 2, 2, 2), (6, 6, 1, 1, 1, 1)),
}

@lru_cache(None)
def partitions(total, ceiling):
    """All descending positive partitions of total, with largest part <= ceiling."""
    if total == 0:
        return ((),)
    return tuple((j,) + tail for j in range(min(total, ceiling), 0, -1)
                 for tail in partitions(total-j, j))

def histogram_partitions(total):
    """Independent enumeration by frequencies of parts (species of size j)."""
    result=[]
    def rec(j, remaining, hist):
        if j==0:
            if remaining==0:
                result.append(tuple(a for v in range(total, 0, -1)
                                    for a in [v]*hist.get(v,0)))
            return
        for count in range(remaining//j+1):
            hist[j]=count
            rec(j-1, remaining-j*count, hist)
        hist.pop(j, None)
    rec(total, total, {})
    return result

def numerators(abundances, total):
    """C(total,k) times exact expected species richness for k=1,...,total."""
    return tuple(len(abundances)*comb(total,k)
        -sum(comb(total-x,k) for x in abundances if total-x>=k)
        for k in range(1,total+1))

def sign_reversals(a, b):
    """Strict sign switches after zero differences have been discarded."""
    signs=[(u>v)-(u<v) for u,v in zip(a,b) if u!=v]
    return sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))

def direct_subset_totals(abundances):
    """Independent check by enumerating every labeled subset, 2^16 in total."""
    species=[]
    for label,count in enumerate(abundances):
        species.extend([label]*count)
    n=len(species)
    seen=[0]*(1<<n)
    totals=[0]*(n+1)
    for mask in range(1,1<<n):
        low=mask & -mask
        i=low.bit_length()-1
        seen[mask]=seen[mask^low] | (1<<species[i])
        totals[mask.bit_count()]+=seen[mask].bit_count()
    return tuple(totals[1:])

def main():
    counts=[]
    for n in range(1,17):
        all_p=partitions(n,n)
        independent=histogram_partitions(n)
        assert len(all_p)==EXPECTED_P[n-1]
        assert sorted(all_p)==sorted(independent)
        vals=[numerators(p,n) for p in all_p]
        crossings=[]
        for i in range(len(all_p)):
            for j in range(i):
                if sign_reversals(vals[i],vals[j])>=2:
                    crossings.append(tuple(sorted((all_p[i],all_p[j]),reverse=True)))
        counts.append((n,len(all_p),len(all_p)*(len(all_p)-1)//2,len(crossings)))
        if n<16:
            assert not crossings
        else:
            assert set(crossings)==WITNESSES and len(crossings)==2
    for pair in WITNESSES:
        for p in pair:
            assert numerators(p,16)==direct_subset_totals(p)
    A1=(7,5,1,1,1,1)
    A2=(6,6,1,1,1,1)
    B=(8,2,2,2,2)
    diffs=[]
    for a in (A1,A2):
        v=numerators(a,16);w=numerators(B,16)
        d=tuple(x-y for x,y in zip(v,w))
        assert sign_reversals(v,w)==2
        diffs.append(d)
    assert diffs[0] == (0,1,3,-22,-168,-518,-930,-1031,-628,-11,363,364,196,64,12,1)
    assert diffs[1] == (0,2,12,14,-84,-392,-804,-947,-592,-2,364,364,196,64,12,1)
    for n,p,pairs,twos in counts:
        print(f'N={n:2d} partitions={p:3d} unordered_pairs={pairs:5d} double_switch_pairs={twos}')
    print('Both boundary pairs verified by all 65,536 labeled subsets each (independent check).')
    print('PASS: minimum N=16, exactly two unordered abundance-partition pairs.')

if __name__=='__main__':
    main()
